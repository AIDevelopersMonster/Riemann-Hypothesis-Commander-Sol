#!/usr/bin/env python3
"""HATTER-SOL-17 H17-05: exact LUT-free PSL(2,7) membership/class certificate.

This certificate proves, exhaustively on all 8! permutations of P^1(F_7), that
five cross-ratio checks plus the projective triple orientation distinguish the
168-element PSL(2,7) subgroup from S_8 without a 168-entry membership LUT.

It then proves on all 168 group elements that conjugacy classes are recovered
structurally: order 1,2,3,4 determines 1A,2A,3A,4A and the projective orientation
of three consecutive points in the unique 7-cycle distinguishes 7A from 7B.
"""
from itertools import permutations, product

P=7; INF=7; N=8; ID=tuple(range(N))
SQUARES={1,2,4}
NAMES=('1A','2A','3A','4A','7A','7B')


def invmod(a): return pow(a,P-2,P)
def mob(a,b,c,d):
    out=[]
    for x in range(P):
        den=(c*x+d)%P; num=(a*x+b)%P
        out.append(INF if den==0 else num*invmod(den)%P)
    out.append(INF if c%P==0 else a*invmod(c)%P)
    return tuple(out)
def compose(p,q): return tuple(p[q[i]] for i in range(N))
def inverse(p):
    out=[0]*N
    for i,j in enumerate(p): out[j]=i
    return tuple(out)

G=sorted({mob(a,b,c,d) for a,b,c,d in product(range(P),repeat=4) if (a*d-b*c)%P==1})
assert len(G)==168
GSET=set(G)
INV={g:inverse(g) for g in G}

def conjugate(h,g): return compose(compose(h,g),INV[h])
def order(g):
    x=ID
    for n in range(1,169):
        x=compose(x,g)
        if x==ID: return n
    raise AssertionError

# Homogeneous representatives: finite x -> (x,1), infinity -> (1,0).
# Their determinant simplifies to the following function on point labels.
def det_point(x,y):
    if x==INF and y==INF: return 0
    if x==INF: return 1
    if y==INF: return 6
    return (x-y)%P

def orient(a,b,c):
    v=det_point(a,b)*det_point(b,c)*det_point(c,a)%P
    if v==0: return 0
    return 1 if v in SQUARES else -1

# For CR(x,0;1,infinity) the constants for x=2..6 are 1-x mod 7.
CR_CONST={2:6,3:5,4:4,5:3,6:2}
def is_pgl_perm(p):
    y0,y1,yinf=p[0],p[1],p[INF]
    for x,k in CR_CONST.items():
        lhs=det_point(p[x],y1)*det_point(y0,yinf)%P
        rhs=k*det_point(p[x],yinf)*det_point(y0,y1)%P
        if lhs!=rhs: return False
    return True

def is_psl_perm(p):
    return is_pgl_perm(p) and orient(p[0],p[1],p[INF])==1

pgl=[]; psl=[]
for p in permutations(range(N)):
    if is_pgl_perm(p):
        pgl.append(p)
        if is_psl_perm(p): psl.append(p)
assert len(pgl)==336
assert len(psl)==168
assert set(psl)==GSET

# Reference conjugacy classes, used only to verify the structural classifier.
unseen=set(G); classes=[]
while unseen:
    g=min(unseen); C={conjugate(h,g) for h in G}; classes.append(C); unseen-=C
classes.sort(key=lambda C:(order(next(iter(C))),min(C)))
assert [len(C) for C in classes]==[1,21,56,42,24,24]
CLASS={g:n for n,C in zip(NAMES,classes) for g in C}

def structural_class(g):
    o=order(g)
    if o==1: return '1A'
    if o==2: return '2A'
    if o==3: return '3A'
    if o==4: return '4A'
    if o!=7: raise AssertionError
    fixed=[x for x in range(N) if g[x]==x]
    assert len(fixed)==1
    x=next(y for y in range(N) if y!=fixed[0])
    y=g[x]; z=g[y]
    s=orient(x,y,z)
    # Verify independence of the chosen starting point on the 7-cycle.
    signs={orient(t,g[t],g[g[t]]) for t in range(N) if t!=fixed[0]}
    assert signs=={s}
    return '7A' if s==1 else '7B'

for g in G:
    assert structural_class(g)==CLASS[g]

counts={n:sum(structural_class(g)==n for g in G) for n in NAMES}
assert counts=={'1A':1,'2A':21,'3A':56,'4A':42,'7A':24,'7B':24}

print('HATTER-SOL-17 H17-05 structural processor certificate')
print('all S8 permutations checked = 40320')
print('PGL(2,7) accepted =',len(pgl))
print('PSL(2,7) accepted =',len(psl))
print('class counts =',counts)
print('PASS: membership and six-class channel require no 168-entry lookup table')
