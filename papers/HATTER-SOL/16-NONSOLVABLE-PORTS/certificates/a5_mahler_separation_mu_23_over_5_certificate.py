#!/usr/bin/env python3
from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import permutations

N = 5
ID = tuple(range(N))

def compose(p, q): return tuple(p[q[i]] for i in range(N))
def inverse(p):
    out = [0] * N
    for i, j in enumerate(p): out[j] = i
    return tuple(out)
def parity(p): return sum(p[i] > p[j] for i in range(N) for j in range(i + 1, N)) % 2

G = [p for p in permutations(range(N)) if parity(p) == 0]
assert len(G) == 60
IDX = {g: i for i, g in enumerate(G)}
MUL = [[IDX[compose(a, b)] for b in G] for a in G]
INV = [IDX[inverse(g)] for g in G]

def subgroup_generated(a, b):
    seen = {0}; todo = deque([0]); gens = (a, b, INV[a], INV[b])
    while todo:
        x = todo.popleft()
        for h in gens:
            y = MUL[x][h]
            if y not in seen: seen.add(y); todo.append(y)
    return seen

def conjugate(h, g): return MUL[MUL[h][g]][INV[h]]
def commutator(a, b): return MUL[MUL[MUL[a][b]][INV[a]]][INV[b]]

def cycle_lengths(gi):
    p = G[gi]; seen = [False] * N; lengths = []
    for i in range(N):
        if seen[i]: continue
        j = i; n = 0
        while not seen[j]: seen[j] = True; n += 1; j = p[j]
        lengths.append(n)
    return tuple(sorted(lengths, reverse=True))

g5 = IDX[(1, 2, 3, 4, 0)]
C5A = {conjugate(h, g5) for h in range(60)}

def class_name(g):
    ct = cycle_lengths(g)
    if ct == (1,1,1,1,1): return '1A'
    if ct == (2,2,1): return '2A'
    if ct == (3,1,1): return '3A'
    if ct == (5,): return '5A' if g in C5A else '5B'
    raise AssertionError(ct)

CHI_NUM = {'1A': (6,0), '2A': (-2,0), '3A': (0,0), '5A': (1,1), '5B': (1,-1)}

generating_pairs = [(a,b) for a in range(60) for b in range(60) if len(subgroup_generated(a,b)) == 60]
assert len(generating_pairs) == 2280
assert Counter(class_name(commutator(a,b)) for a,b in generating_pairs) == Counter({'3A':1080,'5A':600,'5B':600})

unseen = set(generating_pairs); reps = []
while unseen:
    a,b = next(iter(unseen))
    orbit = {(conjugate(h,a), conjugate(h,b)) for h in range(60)}
    assert len(orbit) == 60
    reps.append((a,b)); unseen -= orbit
assert len(reps) == 38

def moments(a, b, max_n=40):
    cur = {(0,0,0): 1}
    steps = ((a,1,0),(INV[a],-1,0),(b,0,1),(INV[b],0,-1))
    out = []
    for n in range(1, max_n + 1):
        nxt = defaultdict(int)
        for (g,x,y), count in cur.items():
            for h,dx,dy in steps: nxt[(MUL[g][h],x+dx,y+dy)] += count
        cur = nxt
        if n % 2 == 0:
            A = B = 0
            for (g,x,y), count in cur.items():
                if x == 0 and y == 0:
                    aa,bb = CHI_NUM[class_name(g)]
                    A += count * aa; B += count * bb
            out.append((A,B))
    return tuple(out)

signature_sets = defaultdict(set)
for a,b in reps:
    signature_sets[class_name(commutator(a,b))].add(moments(a,b))
assert {k:len(v) for k,v in signature_sets.items()} == {'3A':6,'5A':4,'5B':4}

SQ5_LO = Fraction(22360679, 10_000_000)
SQ5_HI = Fraction(22360680, 10_000_000)
assert SQ5_LO*SQ5_LO < 5 < SQ5_HI*SQ5_HI

def qsqrt_interval(a,b):
    a = Fraction(a); b = Fraction(b)
    return (a+b*SQ5_LO, a+b*SQ5_HI) if b >= 0 else (a+b*SQ5_HI, a+b*SQ5_LO)
def iadd(x,y): return (x[0]+y[0], x[1]+y[1])
def imul(x,y):
    vals = (x[0]*y[0],x[0]*y[1],x[1]*y[0],x[1]*y[1])
    return (min(vals),max(vals))
def coeff(si,sj,m):
    ai,bi = si[m-1]; aj,bj = sj[m-1]
    return qsqrt_interval(Fraction(-(ai-aj),4*m), Fraction(-(bi-bj),4*m))
def q_interval(si,sj,ta,tb):
    out = coeff(si,sj,20); T = (ta,tb)
    for m in range(19,1,-1): out = iadd(imul(out,T), coeff(si,sj,m))
    return out

def tail_bound(t):
    if t == 0: return Fraction(0)
    return Fraction(3,21) * (16**21) * (t**19) / (1 - 16*t)

T0 = Fraction(25,529)  # mu >= 23/5
assert 16*T0 < 1

def certify(left,right,subdivisions=128):
    minimum = None
    for s in range(subdivisions):
        ta = T0*Fraction(s,subdivisions); tb = T0*Fraction(s+1,subdivisions)
        tail = tail_bound(tb)
        for si in signature_sets[left]:
            for sj in signature_sets[right]:
                lo,_ = q_interval(si,sj,ta,tb)
                margin = lo - tail
                assert margin > 0
                minimum = margin if minimum is None or margin < minimum else minimum
    return minimum

m1 = certify('3A','5A')
m2 = certify('5B','3A')

if __name__ == '__main__':
    print('HATTER-SOL-16 exact A5 Mahler separation certificate')
    print('ordered generating pairs =', len(generating_pairs))
    print('simultaneous-conjugacy orbits =', len(reps))
    print('40-moment signature counts =', {k:len(v) for k,v in sorted(signature_sets.items())})
    print('mu threshold = 23/5 =', float(Fraction(23,5)))
    print('normalized minimum margin, 3A over 5A =', float(m1))
    print('normalized minimum margin, 5B over 3A =', float(m2))
    print('PASS: M(5A) < M(3A) < M(5B) for every generating pair and every mu >= 23/5')
