#!/usr/bin/env python3
"""Finite verifier for QGE3 L_q(r) synchronization.

The theorem proofs live in the markdown files.  This script supplies independent
finite checks for the constructions and selected exact small values.

No carrier arithmetic is used.  Phase 0 is normalized to the identity using
global left composition.
"""

from itertools import combinations, permutations, product
from math import ceil


def all_constraints(q, r):
    return [(i, j, a) for i, j in combinations(range(r), 2) for a in range(q)]


def satisfies(pis, constraints):
    return all(pis[i][a] == pis[j][a] for i, j, a in constraints)


def is_synchronizing_exhaustive(q, r, constraints):
    """Exhaustive check after normalization pi_0=id.

    Intended for small q,r only.
    """
    perms = list(permutations(range(q)))
    ident = tuple(range(q))
    for rest in product(perms, repeat=r - 1):
        pis = (ident,) + rest
        if satisfies(pis, constraints):
            if any(p != ident for p in rest):
                return False, pis
    return True, None


def construct_q3(r):
    """Optimal construction of size ceil(3(r-1)/2)."""
    if r <= 1:
        return []
    if r == 2:
        return [(0, 1, 0), (0, 1, 1)]
    out = []
    if r % 2 == 0:
        out += [(0, 1, 0), (0, 1, 1)]
        anchor = 0
        start = 2
    else:
        anchor = 0
        start = 1
    # Attach two phases at a time to the synchronized anchor.
    for u in range(start, r, 2):
        v = u + 1
        out += [(anchor, u, 0), (anchor, v, 1), (u, v, 2)]
    return out


def construct_r3(q):
    """Optimal construction of size 2q-3 for q>=3."""
    assert q >= 3
    out = [(0, 1, 0), (0, 2, 1), (1, 2, 2)]
    for a in range(3, q):
        out += [(0, 1, a), (0, 2, a)]
    return out


def construct_general(q, r):
    """Three-active-color reduction upper bound."""
    assert q >= 3
    out = []
    # Synchronize colors 3,...,q-1 along a star.
    for a in range(3, q):
        for i in range(1, r):
            out.append((0, i, a))
    # Add optimal q=3 construction on colors 0,1,2.
    out += construct_q3(r)
    return out


def lower_half_density(q, r):
    return ceil(q * (r - 1) / 2)


def parent_partition(r, edges):
    parent = list(range(r))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            parent[y] = x

    for x, y in edges:
        union(x, y)
    blocks = {}
    for i in range(r):
        blocks.setdefault(find(i), []).append(i)
    return tuple(sorted(tuple(v) for v in blocks.values()))


def labels_of_partition(part, r):
    lab = [None] * r
    for b, block in enumerate(part):
        for v in block:
            lab[v] = b
    return tuple(lab)


def join_connected(part1, part2, r):
    l1 = labels_of_partition(part1, r)
    l2 = labels_of_partition(part2, r)
    seen = {0}
    stack = [0]
    while stack:
        x = stack.pop()
        for y in range(r):
            if y not in seen and (l1[x] == l1[y] or l2[x] == l2[y]):
                seen.add(y)
                stack.append(y)
    return len(seen) == r


def quotient_graph(parts, q, r):
    labs = [labels_of_partition(p, r) for p in parts]
    vertices = []
    index = {}
    for a in range(q):
        for b in sorted(set(labs[a])):
            index[(a, b)] = len(vertices)
            vertices.append((a, b))
    adj = [set() for _ in vertices]
    transversals = []
    for i in range(r):
        vs = [index[(a, labs[a][i])] for a in range(q)]
        transversals.append(vs)
        for x, y in combinations(vs, 2):
            adj[x].add(y)
            adj[y].add(x)
    return vertices, adj, transversals


def canonical_coloring_unique(parts, q, r):
    """Exact backtracking test for the quotient graph.

    The first transversal is fixed to colors 0,...,q-1, removing global color
    relabeling symmetry.  Returns True iff the canonical coloring is then the
    only proper q-coloring.
    """
    vertices, adj, trans = quotient_graph(parts, q, r)
    n = len(vertices)
    canonical = [a for a, _ in vertices]
    color = [-1] * n
    for a, v in enumerate(trans[0]):
        color[v] = a

    def dfs():
        best = None
        options = None
        for v in range(n):
            if color[v] >= 0:
                continue
            used = {color[u] for u in adj[v] if color[u] >= 0}
            avail = [c for c in range(q) if c not in used]
            if not avail:
                return False
            if options is None or len(avail) < len(options):
                best, options = v, avail
        if best is None:
            return any(color[v] != canonical[v] for v in range(n))
        # Search noncanonical colors first, because we only need one witness.
        options.sort(key=lambda c: c == canonical[best])
        for c in options:
            color[best] = c
            if dfs():
                color[best] = -1
                return True
        color[best] = -1
        return False

    alternative_exists = dfs()
    return not alternative_exists


def exact_r4_partition_search(q, max_cost):
    """Search reduced partition systems for r=4 up to max_cost.

    This avoids enumeration of S_q^4 and is practical for q<=7.
    Returns (minimum_cost, one_edge_family) or (None,None).
    """
    r = 4
    base_edges = list(combinations(range(r), 2))
    families = {0: [], 1: [], 2: [], 3: []}
    # One representative forest for each partition and cost.
    for k in range(4):
        seen = {}
        for es in combinations(base_edges, k):
            part = parent_partition(r, es)
            if len(part) != r - k:  # cyclic / redundant
                continue
            seen.setdefault(part, tuple(es))
        families[k] = [(es, part) for part, es in seen.items()]

    def integer_profiles(total, length, lo=0, hi=3):
        cur = []

        def rec(rem, left, minimum):
            if left == 0:
                if rem == 0:
                    yield tuple(cur)
                return
            for x in range(minimum, hi + 1):
                if x > rem:
                    break
                cur.append(x)
                yield from rec(rem - x, left - 1, x)
                cur.pop()

        yield from rec(total, length, lo)

    for cost in range(max_cost + 1):
        for profile in integer_profiles(cost, q):
            chosen = []

            def rec(pos, last_by_cost):
                if pos == q:
                    parts = [p for _, p in chosen]
                    if canonical_coloring_unique(parts, q, r):
                        return [e for e, _ in chosen]
                    return None
                k = profile[pos]
                start = last_by_cost.get(k, -1) + 1
                for idx in range(start, len(families[k])):
                    es, part = families[k][idx]
                    if not all(join_connected(part, p2, r) for _, p2 in chosen):
                        continue
                    old = last_by_cost.get(k, None)
                    last_by_cost[k] = idx
                    chosen.append((es, part))
                    ans = rec(pos + 1, last_by_cost)
                    chosen.pop()
                    if old is None:
                        del last_by_cost[k]
                    else:
                        last_by_cost[k] = old
                    if ans is not None:
                        return ans
                return None

            answer = rec(0, {})
            if answer is not None:
                return cost, answer
    return None, None


def main():
    print("QGE3 LQR finite verifier")
    print("========================")

    print("\nExact theorem construction checks:")
    for r in range(2, 7):
        S = construct_q3(r)
        ok, witness = is_synchronizing_exhaustive(3, r, S)
        target = ceil(3 * (r - 1) / 2)
        print(f"q=3 r={r}: size={len(S)} target={target} sync={ok}")
        assert len(S) == target and ok, witness

    for q in range(3, 7):
        S = construct_r3(q)
        ok, witness = is_synchronizing_exhaustive(q, 3, S)
        target = 2 * q - 3
        print(f"q={q} r=3: size={len(S)} target={target} sync={ok}")
        assert len(S) == target and ok, witness

    print("\nGeneral upper-bound construction sizes:")
    for q, r in [(4, 4), (5, 4), (4, 5), (5, 5)]:
        S = construct_general(q, r)
        target = (q - 3) * (r - 1) + ceil(3 * (r - 1) / 2)
        print(f"q={q} r={r}: size={len(S)} bound={target}")
        assert len(S) == target

    print("\nExact r=4 partition search (may take longer as q grows):")
    expected = {3: 5, 4: 7, 5: 9, 6: 12, 7: 14}
    for q, target in expected.items():
        cost, family = exact_r4_partition_search(q, target)
        print(f"q={q} r=4: optimum<= {cost}; expected={target}")
        assert cost == target

    print("\nAll requested finite checks passed.")


if __name__ == "__main__":
    main()
