#!/usr/bin/env python3
"""Exact solver for FCOA-Z partition-only prescribed support.

Input: integer partition type lambda on the command line, e.g.
    python solve_partition_only_support.py 4 3 2 1

Output:
- exact branch-level minimum d(lambda),
- selected K_lambda orbitals,
- exact FCOA support t^2 d(lambda) if --t is supplied.

The solver implements the Orbital XOR-Separation Program from
PARTITION_ONLY_EXACT_TWIN_SOLVER.md. It uses witness branching rather than
full graph-automorphism enumeration.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from typing import Dict, List, Tuple, Set

Orbital = Tuple


def build_partition(lam: List[int]):
    blocks = []
    point_block = []
    p = 0
    for bi, d in enumerate(lam):
        pts = list(range(p, p + d))
        p += d
        blocks.append(pts)
        point_block.extend([bi] * d)
    return blocks, point_block


def orbital_type(u: int, v: int, blocks, point_block) -> Orbital:
    bu, bv = point_block[u], point_block[v]
    du, dv = len(blocks[bu]), len(blocks[bv])
    if bu == bv:
        return ("W", du)
    if du == dv:
        return ("E", du)
    return ("C", du, dv)


def build_problem(lam: List[int]):
    lam = sorted(lam, reverse=True)
    blocks, point_block = build_partition(lam)
    b = sum(lam)

    orbital_cells: Dict[Orbital, List[Tuple[int, int]]] = defaultdict(list)
    for u in range(b):
        for v in range(b):
            if u == v:
                continue
            orbital_cells[orbital_type(u, v, blocks, point_block)].append((u, v))

    orbitals = sorted(orbital_cells, key=str)
    orbital_index = {o: i for i, o in enumerate(orbitals)}
    weights = [len(orbital_cells[o]) for o in orbitals]

    size_to_blocks: Dict[int, List[int]] = defaultdict(list)
    for bi, d in enumerate(lam):
        size_to_blocks[d].append(bi)
    sizes = sorted(size_to_blocks)

    forbidden = []

    # Representative transposition between distinct equal-size blocks.
    for d in sizes:
        if d >= 2 and len(size_to_blocks[d]) >= 2:
            b1, b2 = size_to_blocks[d][:2]
            u, v = blocks[b1][0], blocks[b2][0]
            perm = list(range(b))
            perm[u], perm[v] = perm[v], perm[u]
            forbidden.append((f"T[{d},{d}]", perm))

    # Representative transposition between distinct size classes.
    for ai, d in enumerate(sizes):
        for e in sizes[ai + 1 :]:
            b1 = size_to_blocks[d][0]
            b2 = size_to_blocks[e][0]
            u, v = blocks[b1][0], blocks[b2][0]
            perm = list(range(b))
            perm[u], perm[v] = perm[v], perm[u]
            forbidden.append((f"T[{d},{e}]", perm))

    # Exceptional singleton-union <-> non-singleton macro swap.
    m1 = len(size_to_blocks.get(1, []))
    if m1 >= 2 and m1 in size_to_blocks and size_to_blocks[m1]:
        singleton_union = [blocks[bi][0] for bi in size_to_blocks[1]]
        target_block = blocks[size_to_blocks[m1][0]]
        if len(singleton_union) == len(target_block):
            perm = list(range(b))
            for x, y in zip(singleton_union, target_block):
                perm[x] = y
                perm[y] = x
            forbidden.append((f"MACRO[{m1}]", perm))

    constraints = []
    for name, perm in forbidden:
        comparisons: Set[Tuple[int, int]] = set()
        for u in range(b):
            for v in range(b):
                if u == v:
                    continue
                i = orbital_index[orbital_type(u, v, blocks, point_block)]
                pu, pv = perm[u], perm[v]
                j = orbital_index[orbital_type(pu, pv, blocks, point_block)]
                if i != j:
                    comparisons.add(tuple(sorted((i, j))))
        constraints.append((name, sorted(comparisons)))

    return orbitals, weights, constraints


def solve(lam: List[int]):
    orbitals, weights, constraints = build_problem(lam)
    q = len(orbitals)

    best_cost = 10**100
    best_assignment = None
    seen = {}

    def recurse(assign: List[int], cost: int):
        nonlocal best_cost, best_assignment

        key = tuple(assign)
        if seen.get(key, 10**100) <= cost:
            return
        seen[key] = cost

        if cost >= best_cost:
            return

        branch_options = None

        for _name, comparisons in constraints:
            satisfied = False
            options = []

            for a, b in comparisons:
                va, vb = assign[a], assign[b]

                if va != -1 and vb != -1:
                    if va != vb:
                        satisfied = True
                        break
                    continue

                if va == -1 and vb == -1:
                    options.append(((a, 0), (b, 1)))
                    options.append(((a, 1), (b, 0)))
                elif va == -1:
                    options.append(((a, 1 - vb),))
                else:
                    options.append(((b, 1 - va),))

            if satisfied:
                continue

            if not options:
                return

            if branch_options is None or len(options) < len(branch_options):
                branch_options = options

        if branch_options is None:
            full = [0 if x == -1 else x for x in assign]
            best_cost = cost
            best_assignment = full
            return

        unique = []
        seen_opts = set()
        for option in branch_options:
            new_pairs = []
            increment = 0
            consistent = True
            for i, value in option:
                if assign[i] != -1 and assign[i] != value:
                    consistent = False
                    break
                if assign[i] == -1:
                    new_pairs.append((i, value))
                    if value == 1:
                        increment += weights[i]
            if not consistent:
                continue
            signature = tuple(sorted(new_pairs))
            if signature in seen_opts:
                continue
            seen_opts.add(signature)
            unique.append((increment, new_pairs))

        unique.sort(key=lambda x: x[0])

        for increment, new_pairs in unique:
            nxt = assign[:]
            for i, value in new_pairs:
                nxt[i] = value
            recurse(nxt, cost + increment)

    recurse([-1] * q, 0)

    if best_assignment is None:
        raise RuntimeError("No exact support relation found")

    selected = [orbitals[i] for i, bit in enumerate(best_assignment) if bit]
    return best_cost, selected, orbitals, weights, constraints


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("lambda_parts", nargs="+", type=int)
    parser.add_argument("--t", type=int, default=None,
                        help="internal branch degree; prints FCOA cost t^2 d(lambda)")
    args = parser.parse_args()

    lam = args.lambda_parts
    if any(x <= 0 for x in lam):
        raise SystemExit("partition parts must be positive integers")

    d_value, selected, orbitals, weights, constraints = solve(lam)

    print("lambda =", tuple(sorted(lam, reverse=True)))
    print("d(lambda) =", d_value)
    print("selected orbitals:")
    for o in selected:
        print("  ", o, "weight=", weights[orbitals.index(o)])
    print("forbidden symmetry constraints =", len(constraints))

    if args.t is not None:
        if args.t <= 0:
            raise SystemExit("--t must be positive")
        print("FCOA support =", args.t * args.t * d_value)


if __name__ == "__main__":
    main()
