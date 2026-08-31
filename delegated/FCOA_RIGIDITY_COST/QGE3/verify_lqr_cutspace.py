#!/usr/bin/env python3
"""Independent hostile verifier for LQR cut-space reduction.

Checks:
1. Bell counts for set partitions through r=6.
2. |W(P)| = 2^(|P|-1).
3. W(P) cap W(Q) = W(P join Q).
4. For r=5, exact maximum weighted defect of pairwise-joining positive-defect
   partition families for q=1,...,15.

The theorem proof is independent of this script.
"""


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


def all_set_partitions(r):
    """Restricted-growth-string generation."""
    if r == 0:
        return [tuple()]

    out = []
    seq = [0]

    def rec(pos, mx):
        if pos == r:
            blocks = []
            for b in range(mx + 1):
                blocks.append(tuple(i for i, x in enumerate(seq) if x == b))
            out.append(tuple(blocks))
            return
        for b in range(mx + 2):
            seq.append(b)
            rec(pos + 1, max(mx, b))
            seq.pop()

    rec(1, 0)
    return out


def cut_space_masks(part, r):
    """Normalized binary cut space, represented by masks on vertices 1,...,r-1."""
    out = set()
    for mask in range(1 << (r - 1)):
        bits = [0] + [((mask >> (i - 1)) & 1) for i in range(1, r)]
        if all(len({bits[i] for i in block}) == 1 for block in part):
            out.add(mask)
    return out


def join_partitions(part1, part2, r):
    edges = []
    for part in (part1, part2):
        for block in part:
            for x in block[1:]:
                edges.append((block[0], x))
    return parent_partition(r, edges)


def compatible(part1, part2, r):
    return len(join_partitions(part1, part2, r)) == 1


def verify_lattice(max_r=6):
    bells = {2: 2, 3: 5, 4: 15, 5: 52, 6: 203}
    for r in range(2, max_r + 1):
        parts = all_set_partitions(r)
        assert len(parts) == bells[r], (r, len(parts), bells[r])

        spaces = {p: cut_space_masks(p, r) for p in parts}

        for p in parts:
            assert len(spaces[p]) == (1 << (len(p) - 1)), (r, p)

        for i, p in enumerate(parts):
            for q in parts[i:]:
                join = join_partitions(p, q, r)
                assert spaces[p] & spaces[q] == spaces[join], (r, p, q)

        print(f"r={r}: Bell={len(parts)} lattice identities PASS")


def max_weight_clique_at_most_q(r, q):
    """Exact weighted clique search in partition-compatibility graph.

    Weight = defect = number of blocks - 1.
    """
    parts = [p for p in all_set_partitions(r) if len(p) > 1]
    weights = [len(p) - 1 for p in parts]
    n = len(parts)

    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if compatible(parts[i], parts[j], r):
                adj[i].add(j)
                adj[j].add(i)

    best_weight = 0
    best = []

    def rec(candidates, selected, weight):
        nonlocal best_weight, best

        if weight > best_weight:
            best_weight = weight
            best = selected[:]

        if len(selected) >= q or not candidates:
            return

        slots = q - len(selected)
        ub = weight + sum(sorted((weights[v] for v in candidates), reverse=True)[:slots])
        if ub <= best_weight:
            return

        candidates = list(candidates)
        cand_set = set(candidates)
        candidates.sort(
            key=lambda v: (weights[v], len(adj[v] & cand_set)),
            reverse=True,
        )

        while candidates:
            slots = q - len(selected)
            ub = weight + sum(
                sorted((weights[v] for v in candidates), reverse=True)[:slots]
            )
            if ub <= best_weight:
                return

            v = candidates.pop(0)
            new_candidates = [u for u in candidates if u in adj[v]]
            rec(new_candidates, selected + [v], weight + weights[v])

    rec(list(range(n)), [], 0)
    return best_weight, [parts[i] for i in best]


def verify_r5_defect_capacity():
    expected = {
        1: 4,
        2: 4,
        3: 6,
        4: 8,
        5: 10,
        6: 10,
        7: 11,
        8: 11,
        9: 12,
        10: 12,
        11: 13,
        12: 13,
        13: 14,
        14: 14,
        15: 15,
    }

    for q, target in expected.items():
        value, family = max_weight_clique_at_most_q(5, q)
        assert value == target, (q, value, target)
        dims = sorted((len(p) - 1 for p in family), reverse=True)
        print(f"r=5 q={q}: packing defect={value} dims={dims} PASS")


def main():
    print("LQR cut-space hostile verifier")
    print("==============================")
    verify_lattice()
    print()
    verify_r5_defect_capacity()
    print()
    print("All cut-space hostile checks passed.")


if __name__ == "__main__":
    main()
