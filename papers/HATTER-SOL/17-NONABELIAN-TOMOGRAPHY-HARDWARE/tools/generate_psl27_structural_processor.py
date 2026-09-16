#!/usr/bin/env python3
"""Emit LUT-free structural PSL(2,7) membership/classification SystemVerilog.

The emitted classifier contains no 168-entry permutation table.  It checks:
  1. the 24-bit input is an 8-point permutation;
  2. five projective cross-ratio identities, hence membership in PGL(2,7);
  3. the projective triple orientation of (0,1,infinity), selecting PSL(2,7);
  4. element order 1,2,3,4,7 by permutation composition;
  5. for order 7 only, the orientation of three consecutive points in the
     unique 7-cycle, separating 7A from 7B.

Class codes agree with H16/H17: 1A=0,2A=1,3A=2,4A=3,7A=4,7B=5.
"""
from pathlib import Path
import argparse

SV = r'''// Auto-generated H17-05 structural PSL(2,7) classifier. No class ROM.
module psl27_structural_classify(
    input  logic [23:0] perm,
    output logic        valid,
    output logic [2:0]  class_code
);
function automatic [2:0] getp(input logic [23:0] p, input integer idx);
    getp = p[idx*3 +: 3];
endfunction
function automatic [23:0] compose_perm(input logic [23:0] p, input logic [23:0] q);
    integer i; logic [23:0] r; logic [2:0] qi;
    begin
      r='0;
      for(i=0;i<8;i=i+1) begin qi=getp(q,i); r[i*3 +: 3]=getp(p,qi); end
      compose_perm=r;
    end
endfunction
function automatic logic perm_is_bijection(input logic [23:0] p);
    integer i,j; logic ok;
    begin
      ok=1'b1;
      for(i=0;i<8;i=i+1) begin
        if(getp(p,i)>3'd7) ok=1'b0;
        for(j=i+1;j<8;j=j+1) if(getp(p,i)==getp(p,j)) ok=1'b0;
      end
      perm_is_bijection=ok;
    end
endfunction
// det of homogeneous representatives: finite x=(x,1), infinity 7=(1,0).
function automatic [2:0] det_point(input logic [2:0] x,input logic [2:0] y);
    integer t;
    begin
      if(x==3'd7 && y==3'd7) det_point=3'd0;
      else if(x==3'd7) det_point=3'd1;
      else if(y==3'd7) det_point=3'd6;
      else begin t=x-y; while(t<0)t=t+7; det_point=t%7; end
    end
endfunction
function automatic [2:0] mul7(input logic [2:0] a,input logic [2:0] b);
    integer t; begin t=a*b; mul7=t%7; end
endfunction
function automatic logic orient_pos(input logic [2:0] a,input logic [2:0] b,input logic [2:0] c);
    logic [2:0] v;
    begin
      v=mul7(mul7(det_point(a,b),det_point(b,c)),det_point(c,a));
      orient_pos=(v==3'd1 || v==3'd2 || v==3'd4);
    end
endfunction
function automatic logic pgl_ok(input logic [23:0] p);
    integer x; logic ok; logic [2:0] y0,y1,yi,px,k,lhs,rhs;
    begin
      ok=perm_is_bijection(p); y0=getp(p,0); y1=getp(p,1); yi=getp(p,7);
      for(x=2;x<=6;x=x+1) begin
        px=getp(p,x);
        case(x) 2:k=3'd6; 3:k=3'd5; 4:k=3'd4; 5:k=3'd3; default:k=3'd2; endcase
        lhs=mul7(det_point(px,y1),det_point(y0,yi));
        rhs=mul7(k,mul7(det_point(px,yi),det_point(y0,y1)));
        if(lhs!=rhs) ok=1'b0;
      end
      pgl_ok=ok;
    end
endfunction
logic is_pgl,is_psl;
logic [23:0] p2,p3,p4,p7;
logic is_id,is_o2,is_o3,is_o4,is_o7;
logic [2:0] start,y,z;
integer i;
always_comb begin
    is_pgl=pgl_ok(perm);
    is_psl=is_pgl & orient_pos(getp(perm,0),getp(perm,1),getp(perm,7));
    p2=compose_perm(perm,perm);
    p3=compose_perm(p2,perm);
    p4=compose_perm(p2,p2);
    p7=compose_perm(compose_perm(p4,p2),perm);
    is_id =(perm==24'hfac688);
    is_o2 =(!is_id && p2==24'hfac688);
    is_o3 =(!is_id && p3==24'hfac688);
    is_o4 =(!is_id && !is_o2 && p4==24'hfac688);
    is_o7 =(!is_id && p7==24'hfac688);
    start=3'd0;
    for(i=0;i<8;i=i+1) if(getp(perm,i)!=i[2:0]) start=i[2:0];
    y=getp(perm,start); z=getp(perm,y);
    valid=is_psl;
    class_code=3'b111;
    if(is_psl) begin
      if(is_id) class_code=3'd0;
      else if(is_o2) class_code=3'd1;
      else if(is_o3) class_code=3'd2;
      else if(is_o4) class_code=3'd3;
      else if(is_o7) class_code=orient_pos(start,y,z) ? 3'd4 : 3'd5;
      else begin valid=1'b0; class_code=3'b111; end
    end
end
endmodule
'''

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out-dir',default='generated_structural'); args=ap.parse_args()
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    (out/'psl27_structural_classify.sv').write_text(SV,encoding='utf-8')
    print('PASS: emitted LUT-free structural classifier')

if __name__=='__main__': main()
