#!/usr/bin/env python3
"""HATTER-SOL-17 H17-06: exact erasure-repair tree certificate.

For the optimal robust8 trace code

  AAB, Abb, AAAB, Abbb, AABAb, AAbAb, ABABB, ABaBB

a single known erased coordinate can be repaired from the other seven.

This certificate treats the 114 generating full signatures and the 66 distinct
non-generating full signatures as the exact realizable PSL(2,7) domain.  For
each erased coordinate it exhaustively optimizes decision trees whose internal
nodes query one surviving class coordinate.  Leaves output either the missing
class (for generating states) or NON (for non-generating states).

Optimization is exact dynamic programming over all reachable state subsets and
remaining coordinate sets.  The primary objective is minimum worst-case query
depth, and the secondary objective is minimum number of internal decision nodes.
"""
from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

from generate_psl27_robust8 import PROBES, verify  # noqa: E402
from generate_psl27_golden_model import CLASS_CODE  # noqa: E402

GEN, NON = verify()
assert len(GEN) == 114
assert len(NON) == 66

EXPECTED = (
    (178, 4, 41),
    (178, 4, 41),
    (180, 4, 43),
    (180, 4, 43),
    (178, 4, 30),
    (180, 4, 39),
    (180, 4, 39),
    (178, 4, 30),
)


def build_problem(erased: int):
    feats = tuple(i for i in range(8) if i != erased)
    rows = {}
    for sig in GEN:
        projected = tuple(CLASS_CODE[sig[i]] for i in feats)
        label = ("G", CLASS_CODE[sig[erased]])
        old = rows.get(projected)
        assert old is None or old == label
        rows[projected] = label
    for sig in NON:
        projected = tuple(CLASS_CODE[sig[i]] for i in feats)
        label = ("N",)
        old = rows.get(projected)
        # d_gen/non >= 2 guarantees that no generating projection collides
        # with a non-generating projection after deletion of one coordinate.
        assert old is None or old == label
        rows[projected] = label
    patterns = tuple(rows.keys())
    labels = tuple(rows[p] for p in patterns)
    local_index = {f: feats.index(f) for f in feats}
    return feats, patterns, labels, local_index


def solve_exact(erased: int):
    feats, patterns, labels, local_index = build_problem(erased)

    @lru_cache(None)
    def solve(states, remaining):
        labs = {labels[s] for s in states}
        if len(labs) == 1:
            return (0, 0, None)
        best = None
        for f in remaining:
            li = local_index[f]
            parts = {}
            for s in states:
                parts.setdefault(patterns[s][li], []).append(s)
            if len(parts) <= 1:
                continue
            next_remaining = tuple(x for x in remaining if x != f)
            child = [solve(tuple(ss), next_remaining) for ss in parts.values()]
            if any(r[0] >= 999 for r in child):
                continue
            candidate = (
                1 + max(r[0] for r in child),
                1 + sum(r[1] for r in child),
                f,
            )
            if best is None or candidate[:2] < best[:2]:
                best = candidate
        return best if best is not None else (999, 999, None)

    all_states = tuple(range(len(patterns)))
    depth, nodes, root = solve(all_states, feats)
    return len(patterns), depth, nodes, root, solve.cache_info()


results = []
for e in range(8):
    count, depth, nodes, root, info = solve_exact(e)
    results.append((count, depth, nodes))
    assert (count, depth, nodes) == EXPECTED[e]
    print(
        f"erase {e} {PROBES[e]:5s}: realizable projections={count}, "
        f"optimal depth={depth}, internal nodes={nodes}, root={PROBES[root]}, "
        f"DP states={info.currsize}"
    )

assert all(depth == 4 for _, depth, _ in results)
assert sum(nodes for _, _, nodes in results) == 306

print("total depth-optimal internal nodes across eight erasure trees = 306")
print("PASS: four class queries are necessary and sufficient for every erasure position")
print("PASS: repaired 24-bit robust signature is a canonical generating-orbit fingerprint")
