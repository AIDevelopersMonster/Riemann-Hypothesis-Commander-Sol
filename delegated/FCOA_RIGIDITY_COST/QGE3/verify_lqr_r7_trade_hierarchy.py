#!/usr/bin/env python3
"""Verifier for LQR_R7_TRADE_HIERARCHY.md.

Checks the finite claims that define the first higher-support layers:
- 301 partition planes for r=7;
- exact normalized cubic support-graph orbit counts for k=5 and k=6;
- minimal k=5 trade classification: 162 S7-orbits / 586,152 concrete cores;
- minimal k=6 trade classification: 1,908 S7-orbits / 9,027,480 concrete cores;
- explicit inclusion-minimal seven-plane trade.

The computation uses the Incidence-2-Factor reduction. It does not enumerate
all 5- or 6-subsets of the 301 planes.
"""
from itertools import permutations, combinations, combinations_with_replacement, product
from collections import Counter

R = 7


def canon_blocks(assign):
    return tuple(tuple(i for i, x in enumerate(assign) if x == b)
                 for b in range(max(assign) + 1))


def canon_from_values(vals):
    groups = {}
    for i, v in enumerate(vals):
        groups.setdefault(v, []).append(i)
    return tuple(sorted((tuple(g) for g in groups.values()), key=lambda B: B[0]))


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


parts = partitions_k(R, 3)
assert len(parts) == 301
pidx = {p: i for i, p in enumerate(parts)}
cuts = [frozenset(cutmask(B) for B in p) for p in parts]


def compatible(fam):
    return all(cuts[a].isdisjoint(cuts[b]) for a, b in combinations(fam, 2))


MU = []
for p in parts:
    A = next(B for B in p if 0 in B)
    U = [B for B in p if 0 not in B]
    MU.append((cutmask(A), tuple(cutmask(B) for B in U)))


def has_alt(fam):
    """Exact normalized alternative-resolution oracle."""
    q = len(fam)
    masks = []
    for x in fam:
        masks.extend(MU[x][1])
    opts = []
    for a, x in enumerate(fam):
        M = MU[x][0]
        o = []
        for i in range(2 * q):
            for j in range(i + 1, 2 * q):
                if masks[i] & masks[j]:
                    continue
                if (masks[i] | masks[j]) == M:
                    o.append((i, j))
        opts.append(o)
    order = sorted(range(q), key=lambda a: len(opts[a]))
    def rec(t, used, diff):
        if t == q:
            return diff
        a = order[t]
        for i, j in opts[a]:
            z = (1 << i) | (1 << j)
            if used & z:
                continue
            canonical = (i == 2 * a and j == 2 * a + 1)
            if rec(t + 1, used | z, diff or not canonical):
                return True
        return False
    return rec(0, 0, False)


# Natural S7 action on the 301 planes.
actions = []
for pi in permutations(range(R)):
    row = []
    for p in parts:
        pp = tuple(sorted((tuple(sorted(pi[i] for i in B)) for B in p),
                          key=lambda B: B[0]))
        row.append(pidx[pp])
    actions.append(row)
assert len(actions) == 5040


def orbit(fam):
    return {tuple(sorted(a[v] for v in fam)) for a in actions}


def support_graph_reps(k):
    rowchoices = [[(i,) + x for x in combinations([j for j in range(k) if j != i], 2)]
                  for i in range(k)]
    graphs = []
    for rows in product(*rowchoices):
        col = [0] * k
        for row in rows:
            for j in row:
                col[j] += 1
        if col != [3] * k:
            continue
        g = 0
        for i, row in enumerate(rows):
            for j in row:
                g |= 1 << (k * i + j)
        graphs.append(g)
    Sk = list(permutations(range(k)))
    def conj(g, s):
        out = 0
        for i in range(k):
            for j in range(k):
                if (g >> (k * i + j)) & 1:
                    out |= 1 << (k * s[i] + s[j])
        return out
    seen, reps = set(), []
    for g in graphs:
        if g in seen:
            continue
        o = {conj(g, s) for s in Sk}
        seen.update(o)
        reps.append(min(o))
    return reps, Sk


def offdiag_cycle_type(g, k):
    adj = [[] for _ in range(2 * k)]
    for i in range(k):
        for j in range(k):
            if i != j and ((g >> (k * i + j)) & 1):
                a, b = i, k + j
                adj[a].append(b)
                adj[b].append(a)
    seen, lens = set(), []
    for v in range(2 * k):
        if v in seen:
            continue
        cur, prev, n = v, -1, 0
        while cur not in seen:
            seen.add(cur)
            n += 1
            nxt = adj[cur][0] if adj[cur][0] != prev else adj[cur][1]
            prev, cur = cur, nxt
        lens.append(n)
    return tuple(sorted(lens))


# Earlier lower layers, used only for minimality filtering.
bad3_reps = {
    (2, 9, 21), (2, 10, 19), (2, 47, 59),
    (12, 42, 77), (12, 43, 75), (15, 40, 78),
}
bad4_reps = {
    (2,9,15,18),(2,9,18,19),(2,9,40,70),(2,9,56,78),
    (2,10,38,69),(2,10,39,70),(2,10,54,78),(2,10,55,79),
    (2,14,40,77),(2,14,40,88),(2,14,56,65),(2,14,56,87),
    (2,14,59,68),(2,15,55,88),(2,15,57,68),(2,47,53,56),
    (2,47,53,57),(12,33,75,83),(12,33,151,245),(12,34,77,82),
    (12,34,150,245),(12,42,62,75),(15,40,60,70),
    (15,40,143,241),(15,40,144,242),
}

bad3 = set()
for x in bad3_reps:
    bad3.update(orbit(x))
bad4 = set()
for x in bad4_reps:
    bad4.update(orbit(x))
assert len(bad3) == 3220
assert len(bad4) == 43260


# ---------- k=5 ----------
reps5, S5 = support_graph_reps(5)
assert len(reps5) == 5
assert Counter(offdiag_cycle_type(g, 5) for g in reps5) == Counter({(10,): 4, (4,6): 1})

id5 = tuple(range(5))
minimal5 = set()
for g in reps5:
    pm = [p for p in S5 if all((g >> (5 * i + p[i])) & 1 for i in range(5))]
    em = []
    for p in pm:
        m = 0
        for i in range(5):
            m |= 1 << (5 * i + p[i])
        em.append(m)
    base = em[pm.index(id5)]
    for inds in combinations_with_replacement(range(len(pm)), 6):
        u = base
        for z in inds:
            u |= em[z]
        if u != g:
            continue
        rhos = [id5] + [pm[z] for z in inds]
        fam = [pidx[canon_from_values([rho[a] for rho in rhos])] for a in range(5)]
        if len(set(fam)) < 5 or not compatible(fam):
            continue
        F = tuple(sorted(fam))
        if any(tuple(sorted(T)) in bad3 for T in combinations(F, 3)):
            continue
        if any(tuple(sorted(T)) in bad4 for T in combinations(F, 4)):
            continue
        assert has_alt(F)
        minimal5.add(F)

raw = set(minimal5)
oreps5 = []
while raw:
    F = raw.pop()
    o = orbit(F)
    oreps5.append(min(o))
    raw.difference_update(o)
oreps5 = sorted(set(oreps5))
assert len(oreps5) == 162
sizes5 = [len(orbit(F)) for F in oreps5]
assert Counter(sizes5) == Counter({5040:75, 2520:81, 1008:2, 504:4})
assert sum(sizes5) == 586152

bad5 = set()
for F in oreps5:
    bad5.update(orbit(F))
assert len(bad5) == 586152


# ---------- k=6 ----------
reps6, S6 = support_graph_reps(6)
assert len(reps6) == 23
assert Counter(offdiag_cycle_type(g, 6) for g in reps6) == Counter({
    (12,): 10, (4,8): 4, (6,6): 7, (4,4,4): 2
})

id6 = tuple(range(6))
minimal6 = set()
productive_support_types = 0
for g in reps6:
    before = len(minimal6)
    pm = [p for p in S6 if all((g >> (6 * i + p[i])) & 1 for i in range(6))]
    em = []
    for p in pm:
        m = 0
        for i in range(6):
            m |= 1 << (6 * i + p[i])
        em.append(m)
    base = em[pm.index(id6)]
    for inds in combinations_with_replacement(range(len(pm)), 6):
        u = base
        for z in inds:
            u |= em[z]
        if u != g:
            continue
        rhos = [id6] + [pm[z] for z in inds]
        fam = [pidx[canon_from_values([rho[a] for rho in rhos])] for a in range(6)]
        if len(set(fam)) < 6 or not compatible(fam):
            continue
        F = tuple(sorted(fam))
        if any(tuple(sorted(T)) in bad3 for T in combinations(F, 3)):
            continue
        if any(tuple(sorted(T)) in bad4 for T in combinations(F, 4)):
            continue
        if any(tuple(sorted(T)) in bad5 for T in combinations(F, 5)):
            continue
        assert has_alt(F)
        minimal6.add(F)
    if len(minimal6) > before:
        productive_support_types += 1

assert productive_support_types == 16
raw = set(minimal6)
oreps6 = []
while raw:
    F = raw.pop()
    o = orbit(F)
    oreps6.append(min(o))
    raw.difference_update(o)
oreps6 = sorted(set(oreps6))
assert len(oreps6) == 1908
sizes6 = [len(orbit(F)) for F in oreps6]
assert Counter(sizes6) == Counter({5040:1684, 2520:202, 1680:13, 1260:4, 840:5})
assert sum(sizes6) == 9027480


# ---------- explicit genuine 7-core ----------
core7 = (70, 73, 136, 164, 211, 224, 295)
assert compatible(core7)
assert has_alt(core7)
for k in range(3, 7):
    assert all(not has_alt(T) for T in combinations(core7, k))

print("PASS: 301 partition planes")
print("PASS: k=5 support graph orbits = 5")
print("PASS: minimal 5-core S7-orbits = 162 / concrete = 586,152")
print("PASS: k=6 support graph orbits = 23, productive = 16")
print("PASS: minimal 6-core S7-orbits = 1,908 / concrete = 9,027,480")
print("PASS: explicit inclusion-minimal 7-core")
print("ALL PASS")
