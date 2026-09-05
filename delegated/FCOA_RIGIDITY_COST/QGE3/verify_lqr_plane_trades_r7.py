#!/usr/bin/env python3
"""Verifier for LQR_PLANE_RESOLUTION_TRADES.md.

Checks the finite computer-assisted claims in the r=7 pure defect-two sector:
- S(7,3)=301 partition planes;
- 2,614,570 compatible unordered triples;
- 786 S7-orbits of compatible triples;
- exactly 6 obstructing triple orbits / 3,220 concrete bad triples;
- exactly 25 minimal obstructing four-plane S7-orbits;
- bad-four orbit-size distribution and 43,260 concrete bad four-cores;
- explicit synchronizing fourteen-plane construction;
- its unique compatible fifteenth extension is non-synchronizing.

The exact quotient-coloring test fixes the phase-0 transversal canonically and
searches for any distinct proper q-coloring.  In the pure-plane case this is
exactly the alternative-resolution test of the accompanying note.
"""
from itertools import permutations, combinations
from collections import Counter

R = 7


def canon_blocks(assign):
    return tuple(tuple(i for i, x in enumerate(assign) if x == b)
                 for b in range(max(assign) + 1))


def partitions_k(n, k):
    out = []
    a = [0]
    def rec(pos, mx):
        if pos == n:
            if mx + 1 == k:
                out.append(canon_blocks(a))
            return
        for b in range(min(mx + 1, k - 1) + 1):
            a.append(b)
            rec(pos + 1, max(mx, b))
            a.pop()
    rec(1, 0)
    return out


def cutmask(block):
    B = set(block)
    S = set(range(R)) - B if 0 in B else B
    return sum(1 << (i - 1) for i in S if i)


planes = []
for p in partitions_k(R, 3):
    cuts = frozenset(cutmask(B) for B in p)
    assert len(cuts) == 3 and 0 not in cuts
    planes.append((p, cuts))

N = len(planes)
assert N == 301

adj = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        if planes[i][1].isdisjoint(planes[j][1]):
            adj[i] |= 1 << j
            adj[j] |= 1 << i


def alternative_coloring(fam, node_cap=500000):
    """Return a normalized noncanonical coloring, or None if unique."""
    q = len(fam)
    verts = []
    phase_vs = [[] for _ in range(R)]
    for a, idx in enumerate(fam):
        for B in planes[idx][0]:
            v = len(verts)
            verts.append((a, B))
            for i in B:
                phase_vs[i].append(v)

    n = len(verts)
    full = (1 << q) - 1
    canonical = [a for a, _ in verts]
    dom = [full] * n
    for v in phase_vs[0]:
        dom[v] = 1 << canonical[v]

    peers = [set() for _ in range(n)]
    for vs in phase_vs:
        for v in vs:
            peers[v].update(vs)
            peers[v].discard(v)
    peers = [tuple(s) for s in peers]
    nodes = 0

    def propagate(d):
        changed = True
        while changed:
            changed = False
            for v, x in enumerate(d):
                if not x:
                    return False
                if x & (x - 1) == 0:
                    for u in peers[v]:
                        if d[u] & x:
                            if d[u] == x:
                                return False
                            d[u] &= ~x
                            changed = True
            for vs in phase_vs:
                for c in range(q):
                    bit = 1 << c
                    loc = [v for v in vs if d[v] & bit]
                    if not loc:
                        return False
                    if len(loc) == 1 and d[loc[0]] != bit:
                        d[loc[0]] = bit
                        changed = True
        return True

    def dfs(d):
        nonlocal nodes
        nodes += 1
        if nodes > node_cap:
            raise RuntimeError("node cap exceeded")
        if not propagate(d):
            return None
        if all(x & (x - 1) == 0 for x in d):
            vals = [x.bit_length() - 1 for x in d]
            return vals if vals != canonical else None
        cand = [v for v, x in enumerate(d) if x & (x - 1)]
        v = min(cand, key=lambda z: d[z].bit_count())
        opts = [c for c in range(q) if (d[v] >> c) & 1]
        opts.sort(key=lambda c: c == canonical[v])
        for c in opts:
            nd = d.copy()
            nd[v] = 1 << c
            ans = dfs(nd)
            if ans is not None:
                return ans
        return None

    return dfs(dom)


# S7 action on plane indices.
pidx = {planes[i][0]: i for i in range(N)}
actions = []
for pi in permutations(range(R)):
    row = []
    for p, _ in planes:
        pp = tuple(sorted((tuple(sorted(pi[i] for i in B)) for B in p),
                          key=lambda B: B[0]))
        row.append(pidx[pp])
    actions.append(row)
assert len(actions) == 5040


# Complete compatible-triple orbit classification.
seen = set()
triple_reps = []
bad3 = []
total_triples = 0
for i in range(N):
    for j in range(i + 1, N):
        if not ((adj[i] >> j) & 1):
            continue
        common = adj[i] & adj[j] & ~((1 << (j + 1)) - 1)
        while common:
            b = common & -common
            k = b.bit_length() - 1
            common -= b
            tri = (i, j, k)
            total_triples += 1
            if tri in seen:
                continue
            orb = {tuple(sorted((a[i], a[j], a[k]))) for a in actions}
            seen.update(orb)
            triple_reps.append(tri)
            if alternative_coloring(list(tri)) is not None:
                bad3.append((tri, len(orb)))

assert total_triples == 2_614_570
assert len(triple_reps) == 786
assert len(bad3) == 6
assert Counter(s for _, s in bad3) == Counter({420: 2, 280: 1, 1260: 1, 630: 1, 210: 1})
assert sum(s for _, s in bad3) == 3220

expected_bad3 = {
    (2, 9, 21),
    (2, 10, 19),
    (2, 47, 59),
    (12, 42, 77),
    (12, 43, 75),
    (15, 40, 78),
}
assert {x for x, _ in bad3} == expected_bad3

# Concrete bad-triple closure.
bad3_concrete = set()
for tri, _ in bad3:
    for a in actions:
        bad3_concrete.add(tuple(sorted(a[v] for v in tri)))
assert len(bad3_concrete) == 3220


# Minimal bad-four classification.
sync_triple_reps = [t for t in triple_reps if t not in expected_bad3]
raw_bad4 = []
for T in sync_triple_reps:
    x = (1 << N) - 1
    for u in T:
        x &= adj[u]
    for v in range(N):
        if not ((x >> v) & 1) or v in T:
            continue
        F = tuple(sorted(T + (v,)))
        if any(tuple(sorted(s)) in bad3_concrete for s in combinations(F, 3)):
            continue
        if alternative_coloring(list(F)) is not None:
            raw_bad4.append(F)

bad4_reps = set()
for F in raw_bad4:
    c = min(tuple(sorted(a[v] for v in F)) for a in actions)
    bad4_reps.add(c)
assert len(bad4_reps) == 25

bad4_sizes = []
for c in bad4_reps:
    orb = {tuple(sorted(a[v] for v in c)) for a in actions}
    bad4_sizes.append(len(orb))
assert Counter(bad4_sizes) == Counter({2520: 13, 1260: 5, 630: 5, 840: 1, 210: 1})
assert sum(bad4_sizes) == 43_260

expected_bad4 = {
(2, 9, 15, 18),(2, 9, 18, 19),(2, 9, 40, 70),(2, 9, 56, 78),
(2, 10, 38, 69),(2, 10, 39, 70),(2, 10, 54, 78),(2, 10, 55, 79),
(2, 14, 40, 77),(2, 14, 40, 88),(2, 14, 56, 65),(2, 14, 56, 87),
(2, 14, 59, 68),(2, 15, 55, 88),(2, 15, 57, 68),(2, 47, 53, 56),
(2, 47, 53, 57),(12, 33, 75, 83),(12, 33, 151, 245),(12, 34, 77, 82),
(12, 34, 150, 245),(12, 42, 62, 75),(15, 40, 60, 70),
(15, 40, 143, 241),(15, 40, 144, 242),
}
assert bad4_reps == expected_bad4


# Explicit synchronizing fourteen-plane construction.
sync14 = [136, 237, 268, 105, 160, 284, 88, 68, 118, 211, 168, 83, 8, 191]
assert alternative_coloring(sync14) is None

common = (1 << N) - 1
for v in sync14:
    common &= adj[v]
extensions = [i for i in range(N) if ((common >> i) & 1) and i not in sync14]
assert extensions == [281]
assert alternative_coloring(sync14 + [281]) is not None

print("PASS: 301 r=7 partition planes")
print("PASS: 2,614,570 compatible triples / 786 S7-orbits")
print("PASS: 6 bad triple orbits / 3,220 concrete bad triples")
print("PASS: 25 minimal bad four orbits / 43,260 concrete bad fours")
print("PASS: synchronizing 14-plane construction")
print("PASS: its unique compatible 15th plane destroys synchronization")
print("ALL PASS")
