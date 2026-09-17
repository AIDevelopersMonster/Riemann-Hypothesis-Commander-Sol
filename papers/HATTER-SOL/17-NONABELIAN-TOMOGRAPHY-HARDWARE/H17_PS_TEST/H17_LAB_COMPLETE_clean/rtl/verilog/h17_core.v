// H17-LAB-01 sequential reference processor. Verilog-2001 synthesizable RTL.
// start accepted only when busy=0. Outputs held until next accepted start/reset.
module h17_core(input clk,input rst,input start,input [23:0] a_in,b_in,
 input [3:0] mode_in,output reg busy,output reg done,
 output reg [2:0] status,output reg [6:0] orbit_id,
 output reg [23:0] raw_signature,observed_signature,repaired_signature);
`include "h17_tables.vh"
function [23:0] compose; input [23:0] p,q; integer j; begin
 for(j=0;j<8;j=j+1) compose[j*3+:3]=p[q[j*3+:3]*3+:3]; end endfunction
function [23:0] inverse; input [23:0] p; integer j; begin
 inverse=0; for(j=0;j<8;j=j+1) inverse[p[j*3+:3]*3+:3]=j; end endfunction
localparam IDLE=0,MEMBER=1,CHECK=2,WORD=3,CLASSIFY=4,MASK=5,DECODE=6,FINISH=7;
reg [3:0] state,mode; reg [23:0] a,b,ia,ib,acc,mask;
reg va,vb; integer idx,w,k,hits; reg [26:0] row;reg [23:0] letter;
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
 IDLE:if(start) begin
 a<=a_in;b<=b_in;mode<=mode_in;busy<=1;status<=0;orbit_id<=127;
 raw_signature<=0;observed_signature<=0;repaired_signature<=0;va<=0;vb<=0;idx<=0;hits<=0;
 if(mode_in>8) begin status<=4;state<=FINISH;end else state<=MEMBER;
 end
 MEMBER:begin
 if(row[23:0]==a)va<=1; if(row[23:0]==b)vb<=1;
 if(idx==167)state<=CHECK;else idx<=idx+1;
 end
 CHECK:if(!(va&&vb))state<=FINISH;else begin
 ia<=inverse(a);ib<=inverse(b);w<=0;k<=0;acc<=24'hfac688;state<=WORD;
 end
 WORD:begin acc<=compose(acc,letter);
 if(k==probe_len(w)-1)begin idx<=0;state<=CLASSIFY;end else k<=k+1;
 end
 CLASSIFY:begin
 if(row[23:0]==acc)raw_signature[21-3*w+:3]<=row[26:24];
 if(idx==167)begin
 if(w==7)state<=MASK;else begin w<=w+1;k<=0;acc<=24'hfac688;state<=WORD;end
 end else idx<=idx+1;
 end
 MASK:begin
 if(mode==0)begin mask<=24'hffffff;observed_signature<=raw_signature;end
 else begin mask<=24'hffffff^(24'h7<<(24-3*mode));observed_signature<=raw_signature|(24'h7<<(24-3*mode));end
 idx<=0;state<=DECODE;
 end
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
