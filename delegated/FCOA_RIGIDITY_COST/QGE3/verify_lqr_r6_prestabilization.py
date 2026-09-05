#!/usr/bin/env python3
"""Independent verifier for LQR_R6_PRESTABILIZATION.md.

Checks:
- Bell(6)=203 and partition counts by defect;
- all compatible 8-plane cores: 58,800 cores / 88 S6-orbits;
- every 8-plane orbit representative is non-synchronizing;
- all compatible d3+5-plane cores: 75,120 cores / 108 S6-orbits;
- every mixed orbit representative is non-synchronizing;
- sharp constructions for q=4,5,6;
- seven-plane completion chain q=7..17;
- plane-splitting chain q=19,21,...,31;
- connected-color extensions q=18,20,...,30;
- arithmetic defect envelope.
"""
from itertools import combinations, permutations
from collections import Counter
R=6

def canon(p): return tuple(sorted(tuple(sorted(B)) for B in p))
def all_parts(n):
    out=[]; seq=[0]
    def rec(pos,mx):
        if pos==n:
            out.append(canon(tuple(tuple(i for i,x in enumerate(seq) if x==b) for b in range(mx+1))))
            return
        for b in range(mx+2):
            seq.append(b); rec(pos+1,max(mx,b)); seq.pop()
    rec(1,0); return out

def cutmask(p):
    s=0
    for m in range(1<<(R-1)):
        bits=[0]+[(m>>(i-1))&1 for i in range(1,R)]
        if all(len({bits[i] for i in B})==1 for B in p): s|=1<<m
    return s&~1

def labels(p):
    lab=[0]*R
    for b,B in enumerate(p):
        for i in B: lab[i]=b
    return lab

def unique(fam):
    q=len(fam); labs=[labels(p) for p in fam]; idx={}; verts=[]
    for a in range(q):
        for b in sorted(set(labs[a])):
            idx[a,b]=len(verts); verts.append((a,b))
    adj=[set() for _ in verts]; trans=[]
    for i in range(R):
        vs=[idx[a,labs[a][i]] for a in range(q)]; trans.append(vs)
        for x,y in combinations(vs,2): adj[x].add(y); adj[y].add(x)
    can=[a for a,b in verts]; col=[-1]*len(verts)
    for a,v in enumerate(trans[0]): col[v]=a
    def dfs():
        best=None; opts=None
        for v in range(len(verts)):
            if col[v]>=0: continue
            used={col[u] for u in adj[v] if col[u]>=0}
            av=[c for c in range(q) if c not in used]
            if not av: return False
            if opts is None or len(av)<len(opts): best,opts=v,av
        if best is None:
            return any(col[v]!=can[v] for v in range(len(verts)))
        opts.sort(key=lambda c:c==can[best])
        for c in opts:
            col[best]=c
            if dfs(): col[best]=-1; return True
        col[best]=-1; return False
    return not dfs()

def linepart(mask):
    b0=[0]+[i for i in range(1,R) if not ((mask>>(i-1))&1)]
    b1=[i for i in range(1,R) if ((mask>>(i-1))&1)]
    return canon((tuple(b0),tuple(b1)))

def defect(fam): return sum(len(p)-1 for p in fam)
def C(q):
    if 2<=q<=5: return 2*q+1
    if q==6: return 12
    return min(31,q+7,(q+31)//2)

P=all_parts(R)
assert len(P)==203
counts=Counter(len(p)-1 for p in P)
assert counts==Counter({2:90,3:65,1:31,4:15,0:1,5:1})
print('Bell(6)=203 and defect counts PASS')

planes=[p for p in P if len(p)==3]
threes=[p for p in P if len(p)==4]
Wp={p:cutmask(p) for p in planes+threes}
n=len(planes); adj=[0]*n
for i in range(n):
    for j in range(i+1,n):
        if not (Wp[planes[i]]&Wp[planes[j]]):
            adj[i]|=1<<j; adj[j]|=1<<i

def clique_masks(K,allowed=None):
    out=[]; base=(1<<n)-1 if allowed is None else allowed
    def rec(cand,chosen):
        need=K-len(chosen)
        if need==0:
            m=0
            for v in chosen: m|=1<<v
            out.append(m); return
        if cand.bit_count()<need: return
        while cand:
            l=cand&-cand; v=l.bit_length()-1; cand^=l
            if cand.bit_count()+1<need: return
            rec(cand&adj[v],chosen+[v])
    rec(base,[]); return out

perms=list(permutations(range(R)))
pidx={p:i for i,p in enumerate(planes)}; tidx={p:i for i,p in enumerate(threes)}
def act(p,s): return canon(tuple(tuple(s[i] for i in B) for B in p))
pmaps=[[pidx[act(p,s)] for p in planes] for s in perms]
tmaps=[[tidx[act(p,s)] for p in threes] for s in perms]
def imask(m,mp):
    y=0
    while m:
        l=m&-m; i=l.bit_length()-1; m^=l; y|=1<<mp[i]
    return y

cl8=clique_masks(8)
assert len(cl8)==58800
unseen=set(cl8); reps=[]; sizes=[]
while unseen:
    x=next(iter(unseen)); orb={imask(x,mp) for mp in pmaps}
    unseen.difference_update(orb); reps.append(x); sizes.append(len(orb))
assert len(reps)==88 and sum(sizes)==58800
assert Counter(sizes)==Counter({720:77,360:7,240:3,120:1})
for x in reps:
    fam=[planes[i] for i in range(n) if (x>>i)&1]
    assert not unique(fam)
print('8-plane obstruction: 58800 cores / 88 S6-orbits PASS')

families=[]
for ti,t in enumerate(threes):
    allowed=0
    for i,p in enumerate(planes):
        if not (Wp[t]&Wp[p]): allowed|=1<<i
    for cm in clique_masks(5,allowed): families.append((ti,cm))
assert len(families)==75120
unseen=set(families); reps=[]; sizes=[]
while unseen:
    ti,cm=next(iter(unseen))
    orb={(tmaps[k][ti],imask(cm,pmaps[k])) for k in range(len(perms))}
    unseen.difference_update(orb); reps.append((ti,cm)); sizes.append(len(orb))
assert len(reps)==108 and sum(sizes)==75120
assert Counter(sizes)==Counter({720:101,360:6,240:1})
for ti,cm in reps:
    fam=[threes[ti]]+[planes[i] for i in range(n) if (cm>>i)&1]
    assert not unique(fam)
print('d3+5-plane obstruction: 75120 cores / 108 S6-orbits PASS')

small={
4:[((0,1,4),(2,3),(5,)),((0,2),(1,3,5),(4,)),((0,4),(1,2),(3,5)),((0,5),(1,),(2,4),(3,))],
5:[((0,1,2),(3,),(4,5)),((0,1),(2,4),(3,5)),((0,3,5),(1,2),(4,)),((0,4),(1,3),(2,5)),((0,),(1,5),(2,),(3,4))],
6:[((0,1,2,5),(3,4)),((0,1,5),(2,3),(4,)),((0,1),(2,4),(3,5)),((0,2),(1,3,4),(5,)),((0,3),(1,),(2,),(4,5)),((0,),(1,4),(2,3,5))],
}
for q,f in small.items():
    fam=[canon(x) for x in f]
    assert unique(fam) and defect(fam)==C(q)
print('q=4,5,6 sharp constructions PASS')

core=[
((0,1,3),(2,5),(4,)),((0,2,5),(1,4),(3,)),((0,2),(1,5),(3,4)),
((0,),(1,2,3),(4,5)),((0,4),(1,2),(3,5)),((0,3),(1,4,5),(2,)),
((0,5),(1,3),(2,4))]
core=[canon(x) for x in core]
used=set()
for p in core:
    m=cutmask(p); used|={x for x in range(1,32) if (m>>x)&1}
line_order=[1,6,11,14,16,19,21,22,28,30]
assert set(line_order)==set(range(1,32))-used
for k in range(11):
    fam=core+[linepart(x) for x in line_order[:k]]
    q=7+k
    assert unique(fam) and defect(fam)==C(q)
print('q=7..17 seven-plane completion chain PASS')

cur_planes=core[:]; cur_lines=line_order[:]
odd_fams={17:cur_planes+[linepart(x) for x in cur_lines]}
for t in range(1,8):
    p=cur_planes.pop(0); m=cutmask(p)
    vecs=[x for x in range(1,32) if (m>>x)&1]
    assert len(vecs)==3
    cur_lines.extend(vecs)
    fam=cur_planes+[linepart(x) for x in cur_lines]
    q=17+2*t
    assert unique(fam) and defect(fam)==C(q)
    odd_fams[q]=fam
print('q=19,21,...,31 plane-splitting chain PASS')

connected=(tuple(range(R)),)
for q in range(18,31,2):
    fam=odd_fams[q-1]+[connected]
    assert unique(fam) and defect(fam)==C(q)
print('q=18,20,...,30 connected extensions PASS')

for q in range(4,50):
    best=5
    best=max(best,4+min(q-1,16))
    for m in range(5):
        if 1+m<=q and 7+3*m<=31:
            ell=max(0,min(q-1-m,31-7-3*m))
            best=max(best,3+2*m+ell)
    for m in range(8):
        if m<=q and 3*m<=31:
            ell=max(0,min(q-m,31-3*m))
            best=max(best,2*m+ell)
    assert best==C(q),(q,best,C(q))
print('analytic defect envelope arithmetic PASS')
print('ALL PASS')
