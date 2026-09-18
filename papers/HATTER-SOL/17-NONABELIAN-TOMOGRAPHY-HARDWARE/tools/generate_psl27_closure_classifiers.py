#!/usr/bin/env python3
"""Emit closure-aware PSL(2,7) membership-only and member-class-only RTL.

H17-08 uses group closure explicitly:

    A,B in PSL(2,7)  =>  w(A,B) in PSL(2,7)

for every free-group word w.  Raw ports therefore need membership checking,
while derived word values need only conjugacy-class decoding.
"""
from pathlib import Path
import argparse

MEMBERSHIP_SV = r'''// H17-08 structural PSL(2,7) membership-only checker.
module psl27_membership_only(
    input  logic [23:0] perm,
    output logic        valid
);
function automatic [2:0] getp(input logic [23:0] p, input integer idx);
    getp = p[idx*3 +: 3];
endfunction
function automatic logic perm_is_bijection(input logic [23:0] p);
    integer i,j; logic ok;
    begin
      ok=1'b1;
      for(i=0;i<8;i=i+1)
        for(j=i+1;j<8;j=j+1) if(getp(p,i)==getp(p,j)) ok=1'b0;
      perm_is_bijection=ok;
    end
endfunction
function automatic [2:0] det_point(input logic [2:0] x,input logic [2:0] y);
    integer t;
    begin
      if(x==3'd7 && y==3'd7) det_point=3'd0;
      else if(x==3'd7) det_point=3'd1;
      else if(y==3'd7) det_point=3'd6;
      else begin
        t=x-y; if(t<0) t=t+7; det_point=t;
      end
    end
endfunction
function automatic [2:0] mul7(input logic [2:0] a,input logic [2:0] b);
    integer t;
    begin
      t=a*b;
      if(t>=35) t=t-35;
      else if(t>=28) t=t-28;
      else if(t>=21) t=t-21;
      else if(t>=14) t=t-14;
      else if(t>=7) t=t-7;
      mul7=t;
    end
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
always @* begin
    valid = pgl_ok(perm) & orient_pos(getp(perm,0),getp(perm,1),getp(perm,7));
end
endmodule
'''

MEMBER_CLASS_SV = r'''// H17-08 PSL(2,7) conjugacy classifier for a value already known to be a member.
// Contract: perm MUST be in PSL(2,7).  No membership logic is duplicated here.
module psl27_member_class_only(
    input  logic [23:0] perm,
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
function automatic [2:0] det_point(input logic [2:0] x,input logic [2:0] y);
    integer t;
    begin
      if(x==3'd7 && y==3'd7) det_point=3'd0;
      else if(x==3'd7) det_point=3'd1;
      else if(y==3'd7) det_point=3'd6;
      else begin
        t=x-y; if(t<0) t=t+7; det_point=t;
      end
    end
endfunction
function automatic [2:0] mul7(input logic [2:0] a,input logic [2:0] b);
    integer t;
    begin
      t=a*b;
      if(t>=35) t=t-35;
      else if(t>=28) t=t-28;
      else if(t>=21) t=t-21;
      else if(t>=14) t=t-14;
      else if(t>=7) t=t-7;
      mul7=t;
    end
endfunction
function automatic logic orient_pos(input logic [2:0] a,input logic [2:0] b,input logic [2:0] c);
    logic [2:0] v;
    begin
      v=mul7(mul7(det_point(a,b),det_point(b,c)),det_point(c,a));
      orient_pos=(v==3'd1 || v==3'd2 || v==3'd4);
    end
endfunction
logic [23:0] p2,p3,p4,p7;
logic is_id,is_o2,is_o3,is_o4,is_o7;
logic [2:0] start,y,z;
integer i;
always @* begin
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
    class_code=3'b111;
    if(is_id) class_code=3'd0;
    else if(is_o2) class_code=3'd1;
    else if(is_o3) class_code=3'd2;
    else if(is_o4) class_code=3'd3;
    else if(is_o7) class_code=orient_pos(start,y,z) ? 3'd4 : 3'd5;
end
endmodule
'''


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out-dir',default='generated_closure'); args=ap.parse_args()
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    (out/'psl27_membership_only.sv').write_text(MEMBERSHIP_SV,encoding='utf-8')
    (out/'psl27_member_class_only.sv').write_text(MEMBER_CLASS_SV,encoding='utf-8')
    print('PASS: emitted H17-08 closure-aware membership-only and member-class-only RTL')

if __name__=='__main__': main()
