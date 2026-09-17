#!/usr/bin/env python3
"""Exact finite certificate for the HATTER-SOL-17 depth-5 erasure barrier."""
from collections import deque
from itertools import combinations, product
P=7; N=8; INF=7; ID=tuple(range(N)); LETTERS='AaBb'
INV_LETTER={'A':'a','a':'A','B':'b','b':'B'}; NAMES=('1A','2A','3A','4A','7A','7B')
def invmod(a): return pow(a,P-2,P)
def mob(a,b,c,d):
    o=[]
    for x in range(P):
        den=(c*x+d)%P; num=(a*x+b)%P
        o.append(INF if den==0 else num*invmod(den)%P)
    o.append(INF if c%P==0 else a*invmod(c)%P); return tuple(o)
def comp(p,q): return tuple(p[q[i]] for i in range(N))
def inv(p):
    r=[0]*N
    for i,j in enumerate(p): r[j]=i
    return tuple(r)
G=sorted({mob(a,b,c,d) for a,b,c,d in product(range(P),repeat=4) if (a*d-b*c)%P==1}); assert len(G)==168
INV={g:inv(g) for g in G}
def conj(h,g): return comp(comp(h,g),INV[h])
def subgroup_size(a,b):
    seen={ID}; q=deque([ID]); gens=(a,b,INV[a],INV[b])
    while q:
        x=q.popleft()
        for g in gens:
            y=comp(x,g)
            if y not in seen: seen.add(y); q.append(y)
    return len(seen)
def order(g):
    x=ID
    for n in range(1,169):
        x=comp(x,g)
        if x==ID: return n
    raise AssertionError
u=set(G); classes=[]
while u:
    g=min(u); C={conj(h,g) for h in G}; classes.append(C); u-=C
classes.sort(key=lambda C:(order(next(iter(C))),min(C)))
CLASS={g:n for n,C in zip(NAMES,classes) for g in C}
unseen={(a,b) for a in G for b in G}; REPS=[]
while unseen:
    a,b=min(unseen); O={(conj(h,a),conj(h,b)) for h in G}; unseen-=O
    if subgroup_size(a,b)==168: REPS.append(min(O))
REPS.sort(); assert len(REPS)==114
def reduce_word(w):
    st=[]
    for c in w:
        if st and INV_LETTER[c]==st[-1]: st.pop()
        else: st.append(c)
    return ''.join(st)
def cyclic_reduce(w):
    w=reduce_word(w)
    while len(w)>=2 and INV_LETTER[w[0]]==w[-1]: w=w[1:-1]
    return w
def canonical_cyclic(w):
    w=cyclic_reduce(w)
    if not w: return ''
    wi=''.join(INV_LETTER[c] for c in reversed(w)); n=len(w)
    return min(v[i:]+v[:i] for v in (w,wi) for i in range(n))
def generate_exact(L):
    out=set()
    def rec(pref,last,k):
        if k==0:
            c=canonical_cyclic(pref)
            if c and len(c)==L: out.add(c)
            return
        for x in LETTERS:
            if last and INV_LETTER[x]==last: continue
            rec(pref+x,x,k-1)
    rec('',None,L); return sorted(out)
def evalw(w,a,b):
    t={'A':a,'a':INV[a],'B':b,'b':INV[b]}; g=ID
    for c in w: g=comp(g,t[c])
    return g
def column(w): return tuple(CLASS[evalw(w,a,b)] for a,b in REPS)
W4=sum((generate_exact(L) for L in range(1,5)),[]); W5=generate_exact(5); ALL=W4+W5
assert len(W4)==25 and len(W5)==26 and len(ALL)==51
COL={w:column(w) for w in ALL}; INDEX={w:i for i,w in enumerate(ALL)}
PAIR=[]
for i,j in combinations(range(114),2):
    mask=0
    for k,w in enumerate(ALL):
        if COL[w][i]!=COL[w][j]: mask|=1<<k
    PAIR.append((i,j,mask))
def smask(words):
    m=0
    for w in words: m|=1<<INDEX[w]
    return m
def dmin_mask(m): return min((D&m).bit_count() for _,_,D in PAIR)
W4M=(1<<len(W4))-1
assert dmin_mask(W4M)==1
critical=[]
for i,j,D in PAIR:
    if (D&W4M).bit_count()==1:
        only=[w for w in W4 if D>>INDEX[w]&1]
        critical.append((i,j,only[0]))
assert critical==[(12,27,'ABab'),(13,28,'ABab'),(14,29,'ABab'),(84,89,'ABab'),(90,92,'ABab'),(100,103,'ABab'),(106,107,'ABab')]
assert dmin_mask(W4M | smask(['AABAb']))==2
assert dmin_mask((1<<len(ALL))-1)==5
BASE=['A','B','AB','Ab','ABab']; BM=smask(BASE)
for k in range(4):
    for extra in combinations(W5,k):
        assert dmin_mask(BM|smask(extra))<2
EXTRA4=('AAABB','AAAbb','AABab','ABBaB')
assert dmin_mask(BM|smask(EXTRA4))==2
print('HATTER-SOL-17 exact depth-5 one-erasure certificate')
print('orbits = 114; depth<=4 words = 25; exact depth-5 words = 26')
print('depth<=4 d_min = 1; critical pairs =',critical)
print('W<=4 + AABAb d_min = 2; therefore minimal maximum depth = 5')
print('frozen H16 five probes need at least four exact-depth-5 additions')
print('one exact 9-probe extension =',BASE+list(EXTRA4))
print('all 51 words through depth 5 have d_min = 5')
print('PASS')
