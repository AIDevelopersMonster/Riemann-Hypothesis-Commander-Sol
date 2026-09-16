#!/usr/bin/env python3
"""Generate exact permutation-based PSL(2,7) H17 port engine RTL.

The generated core accepts A and B as 8-point permutations (8 x 3 bits),
computes A, B, AB, AB^{-1}, and [A,B], classifies all five values into the six
PSL(2,7) conjugacy classes, and packs the 15-bit five-probe signature expected
by the H17 orbit ROM.
"""
from itertools import product
from pathlib import Path
import argparse

P=7; N=8; INF=7; ID=tuple(range(N))
NAMES=('1A','2A','3A','4A','7A','7B')
CODE={n:i for i,n in enumerate(NAMES)}

def invmod(a): return pow(a,P-2,P)
def mobius_perm(a,b,c,d):
    out=[]
    for x in range(P):
        den=(c*x+d)%P; num=(a*x+b)%P
        out.append(INF if den==0 else (num*invmod(den))%P)
    out.append(INF if c%P==0 else (a*invmod(c))%P)
    return tuple(out)
def compose(p,q): return tuple(p[q[i]] for i in range(N))
def inverse(p):
    r=[0]*N
    for i,j in enumerate(p): r[j]=i
    return tuple(r)
G=set()
for a,b,c,d in product(range(P),repeat=4):
    if (a*d-b*c)%P==1: G.add(mobius_perm(a,b,c,d))
G=sorted(G); assert len(G)==168
INV={g:inverse(g) for g in G}
def conj(h,g): return compose(compose(h,g),INV[h])
def order(g):
    x=ID
    for n in range(1,169):
        x=compose(x,g)
        if x==ID:return n
    raise AssertionError
unseen=set(G); classes=[]
while unseen:
    g=min(unseen); C={conj(h,g) for h in G}; classes.append(C); unseen-=C
classes.sort(key=lambda C:(order(next(iter(C))),min(C)))
assert [len(C) for C in classes]==[1,21,56,42,24,24]
CLASS={g:n for n,C in zip(NAMES,classes) for g in C}

def pack(p):
    v=0
    for i,x in enumerate(p): v |= x << (3*i)
    return v

def emit_classifier(path):
    L=[
      '// Auto-generated exact PSL(2,7) permutation classifier.',
      'module psl27_classify_perm(input logic [23:0] perm, output logic valid, output logic [2:0] class_code);',
      'always_comb begin',
      "  valid = 1'b1; class_code = 3'b111;",
      '  unique case (perm)']
    for g in G:
        L.append(f"    24'h{pack(g):06x}: class_code = 3'd{CODE[CLASS[g]]}; // {CLASS[g]}")
    L += ["    default: begin valid=1'b0; class_code=3'b111; end",'  endcase','end','endmodule','']
    path.write_text('\n'.join(L))

def emit_engine(path):
    L=r'''// Auto-generated H17 permutation port-word engine.
module psl27_five_probe_engine(
    input  logic [23:0] A,
    input  logic [23:0] B,
    output logic        valid,
    output logic [14:0] signature,
    output logic [23:0] AB,
    output logic [23:0] AB_inv,
    output logic [23:0] K
);
function automatic [2:0] getp(input logic [23:0] p, input integer idx);
    getp = p[idx*3 +: 3];
endfunction
function automatic [23:0] compose_perm(input logic [23:0] p, input logic [23:0] q);
    integer i;
    logic [23:0] r;
    logic [2:0] qi;
    begin
      r='0;
      for(i=0;i<8;i=i+1) begin qi=getp(q,i); r[i*3 +: 3]=getp(p,qi); end
      compose_perm=r;
    end
endfunction
function automatic [23:0] inverse_perm(input logic [23:0] p);
    integer i;
    logic [23:0] r;
    logic [2:0] pi;
    begin
      r='0;
      for(i=0;i<8;i=i+1) begin pi=getp(p,i); r[pi*3 +: 3]=i[2:0]; end
      inverse_perm=r;
    end
endfunction
logic [23:0] invA,invB;
logic vA,vB,vAB,vAb,vK;
logic [2:0] cA,cB,cAB,cAb,cK;
always_comb begin
    invA = inverse_perm(A); invB = inverse_perm(B);
    AB = compose_perm(A,B);
    AB_inv = compose_perm(A,invB);
    K = compose_perm(compose_perm(compose_perm(A,B),invA),invB);
    signature={cA,cB,cAB,cAb,cK};
    valid=vA & vB & vAB & vAb & vK;
end
psl27_classify_perm uA(.perm(A),.valid(vA),.class_code(cA));
psl27_classify_perm uB(.perm(B),.valid(vB),.class_code(cB));
psl27_classify_perm uAB(.perm(AB),.valid(vAB),.class_code(cAB));
psl27_classify_perm uAb(.perm(AB_inv),.valid(vAb),.class_code(cAb));
psl27_classify_perm uK(.perm(K),.valid(vK),.class_code(cK));
endmodule
'''
    path.write_text(L)

def selftest():
    for a in G:
      assert inverse(inverse(a))==a
      assert compose(a,INV[a])==ID and compose(INV[a],a)==ID
      for b in G:
        ab=compose(a,b); abinv=compose(a,INV[b]); k=compose(compose(compose(a,b),INV[a]),INV[b])
        assert ab in CLASS and abinv in CLASS and k in CLASS
    print('PASS: exhaustive Python port-engine algebra over 168^2 ordered port pairs')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out-dir',default='generated'); args=ap.parse_args()
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    selftest()
    emit_classifier(out/'psl27_classify_perm.sv')
    emit_engine(out/'psl27_five_probe_engine.sv')
    print('PASS: classifier and five-probe engine RTL emitted')
if __name__=='__main__': main()
