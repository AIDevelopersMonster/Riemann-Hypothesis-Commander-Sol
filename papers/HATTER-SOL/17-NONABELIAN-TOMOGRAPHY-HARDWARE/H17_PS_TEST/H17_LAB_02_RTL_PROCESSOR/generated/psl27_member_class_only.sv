// H17-08 PSL(2,7) conjugacy classifier for a value already known to be a member.
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
always_comb begin
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
