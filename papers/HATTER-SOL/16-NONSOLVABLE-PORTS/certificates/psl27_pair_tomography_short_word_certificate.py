#!/usr/bin/env python3
"""Exact finite certificate for short-word tomography of generating pairs in PSL(2,7).

Two regimes are certified.

(1) Unrestricted cyclic trace words:
    all cyclically reduced words of length <=3 give only 107 signatures on the
    114 simultaneous-conjugacy orbits, while length <=4 gives 114.  Thus trace
    depth 4 is necessary and sufficient.  Inside the depth-4 candidate family,
    the five probes A, B, AB, Ab, ABab already separate all 114 orbits, and no
    subfamily of at most four depth-4 candidates does.

(2) Torus-balanced words (zero exponent sum in A and B):
    cumulative trace depths 4,6,8,10,12,14 yield respectively
    4,22,98,110,112,114 distinct signatures.  Hence balanced trace depth 14 is
    necessary and sufficient.  An explicit eight-probe balanced signature is
    also certified.

Because the chosen complex 3D character is injective on the six conjugacy
classes of PSL(2,7), class signatures and exact oriented trace signatures are
equivalent.
"""

from collections import Counter, defaultdict, deque
from itertools import combinations, product

P = 7
N = 8
INF = 7
ID = tuple(range(N))
LETTERS = "AaBb"
INV_LETTER = {"A":"a", "a":"A", "B":"b", "b":"B"}


def invmod(a): return pow(a, P-2, P)

def mobius_perm(a,b,c,d):
    out=[]
    for x in range(P):
        den=(c*x+d)%P; num=(a*x+b)%P
        out.append(INF if den==0 else (num*invmod(den))%P)
    out.append(INF if c%P==0 else (a*invmod(c))%P)
    return tuple(out)

def compose(p,q): return tuple(p[q[i]] for i in range(N))

def inverse(p):
    out=[0]*N
    for i,j in enumerate(p): out[j]=i
    return tuple(out)

G=set()
for a,b,c,d in product(range(P), repeat=4):
    if (a*d-b*c)%P==1:
        G.add(mobius_perm(a,b,c,d))
G=list(G)
assert len(G)==168
INV={g:inverse(g) for g in G}


def conjugate(h,g): return compose(compose(h,g),INV[h])
def subgroup(a,b):
    seen={ID}; q=deque([ID]); gens=(a,b,INV[a],INV[b])
    while q:
        x=q.popleft()
        for g in gens:
            y=compose(x,g)
            if y not in seen:
                seen.add(y); q.append(y)
    return seen

def order(g):
    x=ID
    for n in range(1,169):
        x=compose(x,g)
        if x==ID: return n
    raise AssertionError

# 114 simultaneous-conjugacy orbits of generating pairs.
unseen={(a,b) for a in G for b in G}
REPS=[]
while unseen:
    a,b=next(iter(unseen))
    orbit={(conjugate(h,a),conjugate(h,b)) for h in G}
    unseen-=orbit
    if len(subgroup(a,b))==168:
        assert len(orbit)==168
        REPS.append((a,b))
assert len(REPS)==114

# Six conjugacy classes.
unseen=set(G); CLASSES=[]
while unseen:
    g=next(iter(unseen))
    C={conjugate(h,g) for h in G}
    CLASSES.append(C); unseen-=C
CLASSES.sort(key=lambda C:(order(next(iter(C))),min(C)))
NAMES=['1A','2A','3A','4A','7A','7B']
CLASS_OF={g:name for name,C in zip(NAMES,CLASSES) for g in C}
assert [len(C) for C in CLASSES]==[1,21,56,42,24,24]

# The oriented 3D character values are pairwise distinct, so a class label is
# equivalent to the exact character value.
CHI={
    '1A':(3,0), '2A':(-1,0), '3A':(0,0), '4A':(1,0),
    '7A':(-1,1), '7B':(-1,-1), # doubled coordinates: 2 chi = real + imag*i*sqrt7
}
assert len(set(CHI.values()))==6


def reduce_word(w):
    st=[]
    for c in w:
        if st and INV_LETTER[c]==st[-1]: st.pop()
        else: st.append(c)
    return ''.join(st)

def cyclic_reduce(w):
    w=reduce_word(w)
    while len(w)>=2 and INV_LETTER[w[0]]==w[-1]:
        w=w[1:-1]
    return w

def canonical_cyclic(w):
    w=cyclic_reduce(w)
    if not w: return ''
    wi=''.join(INV_LETTER[c] for c in reversed(w))
    n=len(w)
    return min(v[i:]+v[:i] for v in (w,wi) for i in range(n))

def exponent_sums(w):
    return (w.count('A')-w.count('a'), w.count('B')-w.count('b'))

def generate_exact(L, balanced=False):
    words=set()
    def rec(pref,last,k,ea,eb):
        if abs(ea)+abs(eb)>k: return
        if k==0:
            if balanced and (ea!=0 or eb!=0): return
            c=canonical_cyclic(pref)
            if c and len(c)==L: words.add(c)
            return
        for x in LETTERS:
            if last and INV_LETTER[x]==last: continue
            da=1 if x=='A' else -1 if x=='a' else 0
            db=1 if x=='B' else -1 if x=='b' else 0
            rec(pref+x,x,k-1,ea+da,eb+db)
    rec('',None,L,0,0)
    return sorted(words)

def eval_word(w,a,b):
    table={'A':a,'a':INV[a],'B':b,'b':INV[b]}
    g=ID
    for c in w: g=compose(g,table[c])
    return g

def signature(words,a,b):
    return tuple(CLASS_OF[eval_word(w,a,b)] for w in words)

def distinct_signature_count(words):
    return len({signature(words,a,b) for a,b in REPS})

# Unrestricted depth theorem.
unrestricted=[]
counts_unrestricted=[]
for L in range(1,5):
    unrestricted += generate_exact(L, balanced=False)
    counts_unrestricted.append(distinct_signature_count(unrestricted))
assert counts_unrestricted == [24,107,107,114]
assert len(unrestricted)==25

FIVE=['A','B','AB','Ab','ABab']
assert all(w in unrestricted for w in FIVE)
assert distinct_signature_count(FIVE)==114
# Exact minimality inside the complete depth<=4 candidate family.
for k in range(1,5):
    assert all(distinct_signature_count([unrestricted[i] for i in S])<114
               for S in combinations(range(len(unrestricted)),k))

# Balanced depth theorem.
balanced=[]
balanced_counts=[]
balanced_word_counts=[]
for L in (4,6,8,10,12,14):
    new=generate_exact(L, balanced=True)
    balanced += new
    balanced_word_counts.append(len(new))
    balanced_counts.append(distinct_signature_count(balanced))
assert balanced_word_counts == [1,2,14,76,505,3386]
assert balanced_counts == [4,22,98,110,112,114]
assert len(balanced)==3984

EIGHT=[
    'AABBaabb',
    'AAABAbabbaBaaB',
    'AAbABaBBBabbab',
    'AABBAbababaB',
    'AAAABabaBabbaB',
    'AABabaBAAbaBab',
    'ABBAbaBBabbb',
    'ABABABaBabbabb',
]
assert all(exponent_sums(w)==(0,0) for w in EIGHT)
assert all(canonical_cyclic(w)==w for w in EIGHT)
assert distinct_signature_count(EIGHT)==114

if __name__=='__main__':
    print('HATTER-SOL-16 exact PSL(2,7) short-word tomography certificate')
    print('generating-pair orbits =',len(REPS))
    print('unrestricted distinct counts through depth 1..4 =',counts_unrestricted)
    print('depth<=4 candidate words =',len(unrestricted))
    print('five-probe depth-4 signature =',FIVE)
    print('no <=4-probe subfamily of the full depth<=4 family separates all 114 orbits')
    print('balanced exact-word counts at lengths 4,6,8,10,12,14 =',balanced_word_counts)
    print('balanced cumulative distinct counts =',balanced_counts)
    print('balanced depth 14 is necessary and sufficient')
    print('explicit eight-probe balanced signature =',EIGHT)
    print('PASS: all exact assertions succeeded')
