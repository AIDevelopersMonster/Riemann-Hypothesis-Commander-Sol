#!/usr/bin/env python3
"""Exhaustive hostile verifier for PARTITION_ONLY_EXACT_TWIN_SOLVER.md.

For every integer partition lambda of b, 2 <= b <= MAX_B, and every
K_lambda-invariant orbital union R, compare:

  (A) the recognition theorem criterion:
      all representative forbidden cross-block transpositions are broken,
      plus the exceptional singleton macro-swap when size-compatible;

  (B) direct enumeration of the full symmetric group S_b and the exact test
      Aut(R) = K_lambda.

Default MAX_B=7. This is supporting finite verification, not the proof.
"""

from __future__ import annotations

import argparse
import itertools
import math
from collections import defaultdict


def integer_partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for p in range(max_part, 0, -1):
        for rest in integer_partitions(n - p, p):
            yield (p,) + rest


def build_partition(lam):
    blocks = []
    point_block = []
    p = 0
    for bi, d in enumerate(lam):
        pts = list(range(p, p + d))
        p += d
        blocks.append(pts)
        point_block.extend([bi] * d)
    return blocks, point_block


def orbital_type(u, v, blocks, point_block):
    bu, bv = point_block[u], point_block[v]
    du, dv = len(blocks[bu]), len(blocks[bv])
    if bu == bv:
        return ("W", du)
    if du == dv:
        return ("E", du)
    return ("C", du, dv)


def build_problem(lam):
    lam = sorted(lam, reverse=True)
    blocks, point_block = build_partition(lam)
    b = sum(lam)

    orbital_cells = defaultdict(list)
    for u in range(b):
        for v in range(b):
            if u != v:
                orbital_cells[orbital_type(u, v, blocks, point_block)].append((u, v))

    orbitals = sorted(orbital_cells, key=str)
    orbital_index = {o: i for i, o in enumerate(orbitals)}

    size_to_blocks = defaultdict(list)
    for bi, d in enumerate(lam):
        size_to_blocks[d].append(bi)
    sizes = sorted(size_to_blocks)

    forbidden = []

    for d in sizes:
        if d >= 2 and len(size_to_blocks[d]) >= 2:
            u = blocks[size_to_blocks[d][0]][0]
            v = blocks[size_to_blocks[d][1]][0]
            perm = list(range(b))
            perm[u], perm[v] = perm[v], perm[u]
            forbidden.append((f"T[{d},{d}]", perm))

    for ai, d in enumerate(sizes):
        for e in sizes[ai + 1 :]:
            u = blocks[size_to_blocks[d][0]][0]
            v = blocks[size_to_blocks[e][0]][0]
            perm = list(range(b))
            perm[u], perm[v] = perm[v], perm[u]
            forbidden.append((f"T[{d},{e}]", perm))

    m1 = len(size_to_blocks.get(1, []))
    if m1 >= 2 and m1 in size_to_blocks and m1 != 1:
        singleton_union = [blocks[bi][0] for bi in size_to_blocks[1]]
        target = blocks[size_to_blocks[m1][0]]
        if len(singleton_union) == len(target):
            perm = list(range(b))
            for x, y in zip(singleton_union, target):
                perm[x] = y
                perm[y] = x
            forbidden.append((f"MACRO[{m1}]", perm))

    constraints = []
    for name, perm in forbidden:
        comparisons = set()
        for u in range(b):
            for v in range(b):
                if u == v:
                    continue
                i = orbital_index[orbital_type(u, v, blocks, point_block)]
                j = orbital_index[
                    orbital_type(perm[u], perm[v], blocks, point_block)
                ]
                if i != j:
                    comparisons.add(tuple(sorted((i, j))))
        constraints.append((name, sorted(comparisons)))

    return blocks, point_block, orbitals, constraints


def target_group_order(lam):
    counts = defaultdict(int)
    for d in lam:
        counts[d] += 1
    out = 1
    for d, m in counts.items():
        out *= math.factorial(d) ** m
        out *= math.factorial(m)
    return out


def theorem_criterion(lam, mask):
    _blocks, _pb, orbitals, constraints = build_problem(lam)
    bits = [(mask >> i) & 1 for i in range(len(orbitals))]
    for _name, comparisons in constraints:
        if not any(bits[a] != bits[b] for a, b in comparisons):
            return False
    return True


def direct_aut_order(lam, mask):
    blocks, point_block, orbitals, _constraints = build_problem(lam)
    b = sum(lam)
    selected = {orbitals[i] for i in range(len(orbitals)) if (mask >> i) & 1}

    def edge(u, v):
        return u != v and orbital_type(u, v, blocks, point_block) in selected

    count = 0
    for perm in itertools.permutations(range(b)):
        ok = True
        for u in range(b):
            for v in range(b):
                if u == v:
                    continue
                if edge(u, v) != edge(perm[u], perm[v]):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            count += 1
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-b", type=int, default=7)
    args = parser.parse_args()

    checked_partitions = 0
    checked_relations = 0

    for b in range(2, args.max_b + 1):
        for lam in integer_partitions(b):
            _blocks, _pb, orbitals, _constraints = build_problem(lam)
            target = target_group_order(lam)

            for mask in range(1 << len(orbitals)):
                criterion = theorem_criterion(lam, mask)
                direct = direct_aut_order(lam, mask) == target
                checked_relations += 1

                if criterion != direct:
                    print("FAIL")
                    print("lambda =", lam)
                    print("mask =", mask)
                    print("orbitals =", orbitals)
                    print("criterion =", criterion)
                    print("direct =", direct)
                    raise SystemExit(1)

            checked_partitions += 1
            print("PASS", lam, "orbitals=", len(orbitals))

    print("ALL PASS")
    print("partitions checked =", checked_partitions)
    print("orbital unions checked =", checked_relations)


if __name__ == "__main__":
    main()
