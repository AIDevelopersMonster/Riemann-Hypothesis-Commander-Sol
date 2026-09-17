#!/usr/bin/env python3
from collections import deque, defaultdict, Counter
from fractions import Fraction
from itertools import permutations
import mpmath as mp

iv=mp.iv
N=5
ID=tuple(range(N))

def comp(p,q): return tuple(p[q[i]] for i in range(N))
def inv(p):
    out=[0]*N
    for i,j in enumerate(p): out[j]=i
    return tuple(out)
def parity(p): return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2
G=[p for p in permutations(range(N)) if parity(p)==0]
INV={g:inv(g) for g in G}
assert len(G)==60

def conj(h,g): return comp(comp(h,g),INV[h])
def subgroup(a,b):
    seen={ID}; q=deque([ID]); gs=(a,b,INV[a],INV[b])
    while q:
        x=q.popleft()
        for g in gs:
            y=comp(x,g)
            if y not in seen: seen.add(y); q.append(y)
    return seen

def comm(a,b): return comp(comp(comp(a,b),INV[a]),INV[b])

def cycles(p):
    seen=[False]*N; ls=[]
    for i in range(N):
        if seen[i]: continue
        j=i;n=0
        while not seen[j]: seen[j]=True;n+=1;j=p[j]
        ls.append(n)
    return tuple(sorted(ls,reverse=True))

g5=(1,2,3,4,0); g5sq=comp(g5,g5)
C5A={conj(h,g5) for h in G}; C5B={conj(h,g5sq) for h in G}
def cname(g):
    c=cycles(g)
    if c==(1,1,1,1,1): return '1A'
    if c==(2,2,1): return '2A'
    if c==(3,1,1): return '3A'
    if c==(5,): return '5A' if g in C5A else '5B'
    raise AssertionError(c)

CHI={
 '1A':(Fraction(3),Fraction(0)),
 '2A':(Fraction(-1),Fraction(0)),
 '3A':(Fraction(0),Fraction(0)),
 '5A':(Fraction(1,2),Fraction(1,2)),
 '5B':(Fraction(1,2),Fraction(-1,2)),
}
Q0=(Fraction(0),Fraction(0))
def qadd(x,y): return (x[0]+y[0],x[1]+y[1])
def qmul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qscale(x,s): return (x[0]*s,x[1]*s)
def padd(P,Q):
    R=dict(P)
    for k,v in Q.items(): R[k]=qadd(R.get(k,Q0),v)
    return {k:v for k,v in R.items() if v!=Q0}
def pscale(P,s): return {k:qscale(v,s) for k,v in P.items() if qscale(v,s)!=Q0}
def pmul(P,Q):
    R={}
    for (i,j),a in P.items():
        for (k,l),b in Q.items():
            key=(i+k,j+l); R[key]=qadd(R.get(key,Q0),qmul(a,b))
    return {k:v for k,v in R.items() if v!=Q0}

def trace_power(a,b,n):
    terms=((a,(1,0)),(INV[a],(-1,0)),(b,(0,1)),(INV[b],(0,-1)))
    st={(ID,0,0):1}
    for _ in range(n):
        ns=defaultdict(int)
        for (g,e1,e2),cnt in st.items():
            for h,(d1,d2) in terms:
                ns[(comp(g,h),e1+d1,e2+d2)]+=cnt
        st=ns
    P={}
    for (g,e1,e2),cnt in st.items():
        v=qscale(CHI[cname(g)],Fraction(cnt))
        P[(e1,e2)]=qadd(P.get((e1,e2),Q0),v)
    return {k:v for k,v in P.items() if v!=Q0}

def det_poly(a,b,mu=Fraction(4)):
    t1=trace_power(a,b,1); t2=trace_power(a,b,2); t3=trace_power(a,b,3)
    P={(0,0):(mu**3,Fraction(0))}
    P=padd(P,pscale(t1,-mu**2))
    P=padd(P,pscale(padd(pmul(t1,t1),pscale(t2,-1)),mu/2))
    cub=padd(padd(pmul(pmul(t1,t1),t1),pscale(pmul(t1,t2),-3)),pscale(t3,2))
    return padd(P,pscale(cub,Fraction(-1,6)))

def pkey(P,sw,s1,s2):
    out=[]
    for (m,n),c in P.items():
        if sw: m,n=n,m
        m*=s1;n*=s2
        out.append((m,n,c[0].numerator,c[0].denominator,c[1].numerator,c[1].denominator))
    return tuple(sorted(out))
def canon(P):
    return min(pkey(P,sw,s1,s2) for sw in (0,1) for s1 in (-1,1) for s2 in (-1,1))

reps = [
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
((0,3,1,2,4),(4,0,3,1,2)),((1,0,3,2,4),(4,1,2,0,3)),
]
assert len(reps)==38

types={}
for a,b in reps:
    P=det_poly(a,b)
    key=canon(P)
    types.setdefault(key,(P,cname(comm(a,b))))
assert len(types)==14
assert Counter(c for P,c in types.values())==Counter({'3A':6,'5A':4,'5B':4})

iv.dps = 30
TYPE_INDICES=[0,1,2,3,4,6,10,12,13,16,17,21,23,30]
GAMMA={0:Fraction(3,4),1:Fraction(3,2),2:Fraction(3,8),3:Fraction(1),4:Fraction(5,4),
       6:Fraction(3,5),10:Fraction(1,5),12:Fraction(9,10),13:Fraction(4,5),16:Fraction(3,10),
       17:Fraction(1,2),21:Fraction(3,4),23:Fraction(2,3),30:Fraction(4,5)}
GRID={0:96,1:96,2:128,3:96,4:96,6:128,10:240,12:96,13:96,16:160,17:128,21:96,23:96,30:96}

chosen={canon(det_poly(*reps[i])) for i in TYPE_INDICES}
alltypes={canon(det_poly(*ab)) for ab in reps}
assert chosen==alltypes and len(chosen)==14

root_cache={}
def roots_and_pows(M):
    if M not in root_cache:
        roots=[iv.exp(2j*iv.pi*k/M) for k in range(M)]
        pows=[{n:r**n for n in range(-3,4)} for r in roots]
        root_cache[M]=(roots,pows)
    return root_cache[M]

s5iv=iv.sqrt(5)
def iq(c):
    a,b=c
    return iv.mpf(a.numerator)/a.denominator + (iv.mpf(b.numerator)/b.denominator)*s5iv

def trap(P,M):
    roots,pows=roots_and_pows(M)
    coeff={(m,n):iq(c) for (m,n),c in P.items()}
    s=iv.mpf(0); mingrid=None
    for i in range(M):
        zp=pows[i]
        cn={n:sum((coeff.get((m,n),iv.mpf(0))*zp[m] for m in range(-3,4)),iv.mpc(0)) for n in range(-3,4)}
        for j in range(M):
            v=sum((cn[n]*pows[j][n] for n in range(-3,4)),iv.mpc(0)).real
            assert v>0
            if mingrid is None or v < mingrid: mingrid=v
            s += iv.log(v)
    return s/(M*M),mingrid

records=[]
for idx in TYPE_INDICES:
    P=det_poly(*reps[idx]); c=cname(comm(*reps[idx])); M=GRID[idx]; gam=GAMMA[idx]
    avg,mn=trap(P,M)
    giv=iv.mpf(gam.numerator)/gam.denominator
    q=iv.sqrt(1-giv/6)
    err=6*(q**M)/(M*(1-q))
    exact=avg + err*iv.mpf([-1,1])
    records.append((idx,c,M,gam,avg,err,exact,mn))
    print('TYPE',idx,c,'M',M,'gamma>',gam,'avg=',avg,'alias<=',err,'exact=',exact,'grid_min=',mn,flush=True)

for i,ci,Mi,gi,ai,ei,I,mni in records:
    for j,cj,Mj,gj,aj,ej,J,mnj in records:
        if ci=='5A' and cj=='3A': assert I < J, (i,I,j,J)
        if ci=='3A' and cj=='5B': assert I < J, (i,I,j,J)
print('PASS: rigorous interval + aliasing certificate closes mu=4 ordering')
