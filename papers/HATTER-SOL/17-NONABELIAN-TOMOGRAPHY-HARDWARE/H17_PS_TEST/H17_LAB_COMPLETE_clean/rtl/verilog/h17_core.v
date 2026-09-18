/*
 * HATTER-SOL-17 / H17-LAB-01
 * Sequential table-driven reference processor (synthesizable Verilog-2001).
 *
 * Input A,B: packed permutations, p[i*3 +: 3] = p(i), i=0..7.
 * Identity permutation: 24'hfac688.
 *
 * Pipeline at the mathematical level:
 *   A,B membership in PSL(2,7)
 *   -> 8 robust observer words
 *   -> 8 conjugacy-class codes = 24-bit raw_signature
 *   -> optional known one-coordinate erasure
 *   -> 114 generating-orbit signature scan
 *   -> repaired_signature + legacy orbit_id.
 *
 * mode_in: 0=no erasure, 1..8=erase coordinate 0..7, >8=invalid.
 * status: 0=idle/reset or non-PSL input, 1=no orbit match,
 *         2=unique match, 3=multiple matches, 4=invalid mode.
 * orbit_id=127 is the invalid sentinel.
 * done is a one-clock pulse; start is accepted only in IDLE.
 *
 * Valid PSL transactions with status 1/2 take exactly 1663 clocks:
 * 168 membership + 1 check + 34 word steps + 8*168 class scans
 * + 1 mask + 114 orbit scans + 1 finish.
 *
 * This file is the readable LAB-01 reference implementation, not the
 * optimized H17-08 closure-aware / ROM-free processor.
 */
module h17_core(input clk,input rst,input start,input [23:0] a_in,b_in,
 input [3:0] mode_in,output reg busy,output reg done,
 output reg [2:0] status,output reg [6:0] orbit_id,
 output reg [23:0] raw_signature,observed_signature,repaired_signature);
`include "h17_tables.vh"

// Packed permutation arithmetic. compose(p,q) implements p o q.
function [23:0] compose; input [23:0] p,q; integer j; begin
 for(j=0;j<8;j=j+1) compose[j*3+:3]=p[q[j*3+:3]*3+:3]; end endfunction
function [23:0] inverse; input [23:0] p; integer j; begin
 inverse=0; for(j=0;j<8;j=j+1) inverse[p[j*3+:3]*3+:3]=j; end endfunction
// The FSM intentionally reuses one small datapath for all scans.
localparam IDLE=0,MEMBER=1,CHECK=2,WORD=3,CLASSIFY=4,MASK=5,DECODE=6,FINISH=7;
reg [3:0] state,mode; reg [23:0] a,b,ia,ib,acc,mask;
reg va,vb; integer idx,w,k,hits; reg [26:0] row;reg [23:0] letter;
// Shared table read and current probe-letter selector.
// probe_letter: 0=A, 1=B, 2=A^-1, 3=B^-1.
always @* begin
 row=group_row(idx);
 case(probe_letter(w,k)) 0:letter=a;1:letter=b;2:letter=ia;default:letter=ib;endcase
end
always @(posedge clk) begin
 if(rst) begin state<=IDLE;busy<=0;done<=0;status<=0;orbit_id<=127;
 raw_signature<=0;observed_signature<=0;repaired_signature<=0;
 a<=0;b<=0;ia<=0;ib<=0;acc<=0;mask<=0;mode<=0;va<=0;vb<=0;idx<=0;w<=0;k<=0;hits<=0;
 end else begin
 done<=0;
 case(state)
 // Latch a complete request only while idle.
 IDLE:if(start) begin
 a<=a_in;b<=b_in;mode<=mode_in;busy<=1;status<=0;orbit_id<=127;
 raw_signature<=0;observed_signature<=0;repaired_signature<=0;va<=0;vb<=0;idx<=0;hits<=0;
 if(mode_in>8) begin status<=4;state<=FINISH;end else state<=MEMBER;
 end
 // Scan all 168 PSL(2,7) elements for A and B.
 MEMBER:begin
 if(row[23:0]==a)va<=1; if(row[23:0]==b)vb<=1;
 if(idx==167)state<=CHECK;else idx<=idx+1;
 end
 CHECK:if(!(va&&vb))state<=FINISH;else begin
 ia<=inverse(a);ib<=inverse(b);w<=0;k<=0;acc<=24'hfac688;state<=WORD;
 end
 // Evaluate one observer word one letter per clock.
 WORD:begin acc<=compose(acc,letter);
 if(k==probe_len(w)-1)begin idx<=0;state<=CLASSIFY;end else k<=k+1;
 end
 // Matching group row supplies the class code in row[26:24].
 CLASSIFY:begin
 if(row[23:0]==acc)raw_signature[21-3*w+:3]<=row[26:24];
 if(idx==167)begin
 if(w==7)state<=MASK;else begin w<=w+1;k<=0;acc<=24'hfac688;state<=WORD;end
 end else idx<=idx+1;
 end
 // Known erasure: mark one 3-bit coordinate as 111 and mask it.
 MASK:begin
 if(mode==0)begin mask<=24'hffffff;observed_signature<=raw_signature;end
 else begin mask<=24'hffffff^(24'h7<<(24-3*mode));observed_signature<=raw_signature|(24'h7<<(24-3*mode));end
 idx<=0;state<=DECODE;
 end
 // Compare surviving coordinates against all 114 orbit signatures.
 DECODE:begin
 if((orbit_row(idx)&mask)==(observed_signature&mask))begin
 hits<=hits+1;orbit_id<=idx;repaired_signature<=orbit_row(idx);end
 if(idx==113)state<=FINISH;else idx<=idx+1;
 end
 FINISH:begin
 if(mode<=8 && va && vb)begin
 if(hits==1)status<=2;
 else begin status<=(hits==0)?1:3;orbit_id<=127;repaired_signature<=0;end
 end
 busy<=0;done<=1;state<=IDLE;
 end
 default:begin state<=IDLE;busy<=0;end
 endcase
 end
end
endmodule
