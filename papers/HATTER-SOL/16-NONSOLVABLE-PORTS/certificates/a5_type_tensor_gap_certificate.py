#!/usr/bin/env python3
from collections import deque
from fractions import Fraction
from itertools import permutations
import sympy as sp

N=5
ID=tuple(range(N))

def compose(p,q): return tuple(p[q[i]] for i in range(N))
def inverse(p):
    out=[0]*N
    for i,j in enumerate(p): out[j]=i
    return tuple(out)
def parity(p): return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2
G=[p for p in permutations(range(N)) if parity(p)==0]
INV={g:inverse(g) for g in G}
assert len(G)==60

def subgroup(a,b):
    seen={ID}; q=deque([ID]); gs=(a,b,INV[a],INV[b])
    while q:
        x=q.popleft()
        for g in gs:
            y=compose(x,g)
            if y not in seen: seen.add(y); q.append(y)
    return seen

def order(g):
    x=ID
    for n in range(1,61):
        x=compose(x,g)
        if x==ID: return n
    raise AssertionError

REPS=[
((2,4,1,0,3),(1,4,3,0,2)),((4,2,0,1,3),(4,2,3,0,1)),
((3,2,0,4,1),(0,3,1,2,4)),((2,0,3,4,1),(0,2,3,1,4)),
((4,3,1,0,2),(4,1,0,3,2)),((0,3,2,4,1),(4,0,1,2,3)),
((0,1,3,4,2),(2,3,0,1,4)),((0,3,1,2,4),(4,3,0,2,1)),
((1,2,4,0,3),(0,3,1,2,4)),((4,3,1,0,2),(2,1,3,0,4)),
((3,2,1,0,4),(0,1,3,4,2)),((1,2,0,3,4),(2,3,4,0,1)),
((2,4,1,0,3),(3,0,1,4,2)),((2,4,0,3,1),(1,4,0,2,3)),
((4,2,0,1,3),(4,0,1,2,3)),((3,4,1,2,0),(1,4,3,0,2)),
((2,0,4,1,3),(1,0,2,4,3)),((2,3,4,0,1),(0,2,1,4,3)),
((0,3,1,2,4),(1,0,4,3,2)),((1,4,3,0,2),(0,2,4,3,1)),
((3,4,1,2,0),(4,0,3,1,2)),((4,0,2,3,1),(0,3,1,2,4)),
((2,0,3,4,1),(1,0,3,2,4)),((2,3,4,0,1),(0,2,4,3,1)),
((0,4,3,2,1),(4,2,0,1,3)),((1,4,0,2,3),(2,1,3,0,4)),
((1,0,4,3,2),(1,4,3,0,2)),((0,2,4,3,1),(4,3,0,2,1)),
((2,4,1,0,3),(3,2,4,1,0)),((0,4,1,3,2),(3,1,0,2,4)),
((4,2,1,3,0),(1,3,0,4,2)),((0,1,3,4,2),(4,2,3,0,1)),
((2,0,4,1,3),(4,2,0,1,3)),((0,4,2,1,3),(4,3,0,2,1)),
((3,2,4,1,0),(2,1,0,4,3)),((3,1,0,2,4),(1,4,0,2,3)),
((0,3,1,2,4),(4,0,3,1,2)),((1,0,3,2,4),(4,1,2,0,3))]
TYPE_INDICES=[0,1,2,3,4,6,10,12,13,16,17,21,23,30]
GAMMA={0:Fraction(3,4),1:Fraction(3,2),2:Fraction(3,8),3:Fraction(1),4:Fraction(5,4),
       6:Fraction(3,5),10:Fraction(1,5),12:Fraction(9,10),13:Fraction(4,5),16:Fraction(3,10),
       17:Fraction(1,2),21:Fraction(3,4),23:Fraction(2,3),30:Fraction(4,5)}

pa=pb=None
for a in G:
    if order(a)!=2: continue
    for b in G:
        if order(b)==3 and order(compose(a,b))==5 and len(subgroup(a,b))==60:
            pa,pb=a,b; break
    if pa is not None: break
assert pa is not None

s5=sp.sqrt(5); phi=(1+s5)/2
T=sp.simplify(sp.Matrix([[-1,phi,1/phi],[phi,1/phi,1],[1/phi,1,-phi]])/2)
C=sp.Matrix([[0,0,1],[1,0,0],[0,1,0]])
assert sp.simplify(T.T*T-sp.eye(3))==sp.zeros(3)
assert T**2==sp.eye(3) and C**3==sp.eye(3) and sp.simplify((T*C)**5-sp.eye(3))==sp.zeros(3)

REP={ID:sp.eye(3)}; q=deque([ID])
while q:
    g=q.popleft(); M=REP[g]
    for h,H in ((pa,T),(INV[pa],T.T),(pb,C),(INV[pb],C.T)):
        y=compose(g,h); YM=sp.simplify(M*H)
        if y not in REP: REP[y]=YM; q.append(y)
        else: assert sp.simplify(REP[y]-YM)==sp.zeros(3)
assert len(REP)==60

cols=[]
for i in range(3):
    for j in range(3):
        if i!=j:
            v=sp.zeros(9,1); v[3*i+j]=1; cols.append(v)
d1=sp.zeros(9,1); d1[0]=1; d1[4]=-1; cols.append(d1)
d2=sp.zeros(9,1); d2[0]=1; d2[8]=-1; cols.append(d2)
Q=sp.Matrix.hstack(*cols)

def positive_qsqrt5(expr):
    e=sp.expand(sp.simplify(expr)); b=sp.simplify(e.coeff(s5)); a=sp.simplify(e-b*s5)
    assert a.is_Rational and b.is_Rational
    if b==0: return a>0
    if a>=0 and b>=0: return True
    if a<=0 and b<=0: return False
    if a>0 and b<0: return a*a>5*b*b
    if a<0 and b>0: return 5*b*b>a*a
    raise AssertionError

for idx in TYPE_INDICES:
    a,b=REPS[idx]; A=REP[a]; B=REP[b]
    SA=sp.kronecker_product(A,A); SB=sp.kronecker_product(B,B)
    L=sp.simplify(4*sp.eye(9)-SA-SA.T-SB-SB.T)
    g=sp.Rational(GAMMA[idx].numerator,GAMMA[idx].denominator)
    M=sp.simplify(Q.T*(L-g*sp.eye(9))*Q)
    for k in range(1,9):
        assert positive_qsqrt5(sp.simplify(M[:k,:k].det())), (idx,k)
    print('TYPE',idx,'gamma >',GAMMA[idx])

print('PASS: all fourteen Mahler types have the certified tensor gaps')
