#!/usr/bin/env python3
"""HATTER-SOL-17 exact finite admissibility/erasure certificate for PSL(2,7)."""
from itertools import product, combinations
from collections import deque, Counter
P=7;N=8;INF=7;ID=tuple(range(N));NAMES=('1A','2A','3A','4A','7A','7B');WORDS=('A','B','AB','Ab','ABab')
def invmod(a):return pow(a,P-2,P)
def mob(a,b,c,d):
 o=[]
 for x in range(P):
  den=(c*x+d)%P;num=(a*x+b)%P;o.append(INF if den==0 else num*invmod(den)%P)
 o.append(INF if c%P==0 else a*invmod(c)%P);return tuple(o)
def comp(p,q):return tuple(p[q[i]] for i in range(N))
def inv(p):
 r=[0]*N
 for i,j in enumerate(p):r[j]=i
 return tuple(r)
G=sorted({mob(a,b,c,d) for a,b,c,d in product(range(P),repeat=4) if (a*d-b*c)%P==1});assert len(G)==168
INV={g:inv(g) for g in G}
def conj(h,g):return comp(comp(h,g),INV[h])
def order(g):
 x=ID
 for n in range(1,169):
  x=comp(x,g)
  if x==ID:return n
 raise AssertionError
def subgroup_size(a,b):
 s={ID};q=deque([ID]);gens=(a,b,INV[a],INV[b])
 while q:
  x=q.popleft()
  for g in gens:
   y=comp(x,g)
   if y not in s:s.add(y);q.append(y)
 return len(s)
u=set(G);classes=[]
while u:
 g=min(u);C={conj(h,g) for h in G};classes.append(C);u-=C
classes.sort(key=lambda C:(order(next(iter(C))),min(C)));assert [len(C) for C in classes]==[1,21,56,42,24,24]
CLASS={g:n for n,C in zip(NAMES,classes) for g in C}
def evalw(w,a,b):
 t={'A':a,'a':INV[a],'B':b,'b':INV[b]};g=ID
 for c in w:g=comp(g,t[c])
 return g
def sig(a,b):return tuple(CLASS[evalw(w,a,b)] for w in WORDS)
unseen={(a,b) for a in G for b in G};reps=[]
while unseen:
 a,b=min(unseen);orb={(conj(h,a),conj(h,b)) for h in G};unseen-=orb
 if subgroup_size(a,b)==168:reps.append(min(orb))
reps.sort();assert len(reps)==114
gen={sig(a,b) for a,b in reps};assert len(gen)==114
nongen=set();gp=np=0
for a in G:
 for b in G:
  if subgroup_size(a,b)==168:gp+=1;assert sig(a,b) in gen
  else:np+=1;nongen.add(sig(a,b))
assert gp==19152 and np==9072 and len(nongen)==66 and gen.isdisjoint(nongen)
def hd(s,t):return sum(a!=b for a,b in zip(s,t))
assert min(hd(s,t) for s,t in combinations(gen,2))==1
assert min(hd(s,t) for s in gen for t in nongen)==2
stats=[]
for drop in range(5):
 p=[tuple(x for i,x in enumerate(s) if i!=drop) for s in gen];c=Counter(p)
 stats.append((drop,len(c),sum(v for v in c.values() if v>1),sum(v>1 for v in c.values()),max(c.values())))
 gp4={tuple(x for i,x in enumerate(s) if i!=drop) for s in gen};np4={tuple(x for i,x in enumerate(s) if i!=drop) for s in nongen};assert gp4.isdisjoint(np4)
assert stats==[(0,88,52,26,2),(1,88,52,26,2),(2,110,8,4,2),(3,110,8,4,2),(4,107,14,7,2)]
print('HATTER-SOL-17 PSL(2,7) admissibility certificate')
print('group order =',len(G),'ordered pairs =',len(G)**2)
print('generating pairs =',gp,'non-generating pairs =',np)
print('generating orbit/signature image =',len(gen),'non-generating signature image =',len(nongen))
print('intersection =',len(gen & nongen),'union realized signatures =',len(gen|nongen))
print('min Hamming: generating/generating = 1; generating/non-generating = 2')
print('drop-one stats (drop,distinct,colliding_orbits,collision_buckets,max_bucket) =',stats)
print('PASS: ROM hit iff generating, and admissibility survives any one probe erasure')
