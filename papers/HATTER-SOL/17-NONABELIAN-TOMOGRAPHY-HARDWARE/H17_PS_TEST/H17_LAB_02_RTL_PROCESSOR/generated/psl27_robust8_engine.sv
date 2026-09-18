// H17-08 closure-aware robust8 engine: 2 raw membership checks + 8 member-class decoders.
module psl27_robust8_engine(
    input logic [23:0] A, input logic [23:0] B,
    output logic valid, output logic [23:0] signature
);
function automatic [2:0] getp(input logic [23:0] p, input integer idx);
    getp = p[idx*3 +: 3];
endfunction
function automatic [23:0] compose_perm(input logic [23:0] p, input logic [23:0] q);
    integer i; logic [23:0] r; logic [2:0] qi;
    begin r='0; for(i=0;i<8;i=i+1) begin qi=getp(q,i); r[i*3 +: 3]=getp(p,qi); end compose_perm=r; end
endfunction
function automatic [23:0] inverse_perm(input logic [23:0] p);
    integer i; logic [23:0] r; logic [2:0] pi;
    begin r='0; for(i=0;i<8;i=i+1) begin pi=getp(p,i); r[pi*3 +: 3]=i[2:0]; end inverse_perm=r; end
endfunction
logic [23:0] invA,invB;
logic vA,vB;
logic [23:0] n_AB;
logic [23:0] n_Ab;
logic [23:0] n_BB;
logic [23:0] n_AAB;
logic [23:0] n_ABA;
logic [23:0] n_ABa;
logic [23:0] n_Abb;
logic [23:0] n_AAAB;
logic [23:0] n_AbAb;
logic [23:0] n_Abbb;
logic [23:0] n_AABAb;
logic [23:0] n_AAbAb;
logic [23:0] n_ABABB;
logic [23:0] n_ABaBB;
logic [2:0] c0;
logic [2:0] c1;
logic [2:0] c2;
logic [2:0] c3;
logic [2:0] c4;
logic [2:0] c5;
logic [2:0] c6;
logic [2:0] c7;
always_comb begin
  invA=inverse_perm(A); invB=inverse_perm(B);
  n_AB=compose_perm(A,B); // AB
  n_Ab=compose_perm(A,invB); // Ab
  n_BB=compose_perm(B,B); // BB
  n_AAB=compose_perm(A,n_AB); // AAB
  n_ABA=compose_perm(n_AB,A); // ABA
  n_ABa=compose_perm(n_AB,invA); // ABa
  n_Abb=compose_perm(n_Ab,invB); // Abb
  n_AAAB=compose_perm(A,n_AAB); // AAAB
  n_AbAb=compose_perm(n_Ab,n_Ab); // AbAb
  n_Abbb=compose_perm(n_Abb,invB); // Abbb
  n_AABAb=compose_perm(n_AAB,n_Ab); // AABAb
  n_AAbAb=compose_perm(A,n_AbAb); // AAbAb
  n_ABABB=compose_perm(n_ABA,n_BB); // ABABB
  n_ABaBB=compose_perm(n_ABa,n_BB); // ABaBB
  signature={c0,c1,c2,c3,c4,c5,c6,c7};
  valid=vA&vB;
end
psl27_membership_only uA(.perm(A),.valid(vA));
psl27_membership_only uB(.perm(B),.valid(vB));
psl27_member_class_only u0(.perm(n_AAB),.class_code(c0));
psl27_member_class_only u1(.perm(n_Abb),.class_code(c1));
psl27_member_class_only u2(.perm(n_AAAB),.class_code(c2));
psl27_member_class_only u3(.perm(n_Abbb),.class_code(c3));
psl27_member_class_only u4(.perm(n_AABAb),.class_code(c4));
psl27_member_class_only u5(.perm(n_AAbAb),.class_code(c5));
psl27_member_class_only u6(.perm(n_ABABB),.class_code(c6));
psl27_member_class_only u7(.perm(n_ABaBB),.class_code(c7));
endmodule
