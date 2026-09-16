#!/usr/bin/env python3
"""HATTER-SOL-17 H17-04: optimal joint one-erasure trace-code certificate.

The candidate coordinates are all cyclically reduced trace words of length <=5,
modulo cyclic rotation and inversion.  The exact finite model contains:
  * 114 simultaneous-conjugacy orbits of generating pairs in PSL(2,7),
  * 66 distinct non-generating signatures in the full 51-coordinate family.

We require a selected coordinate set S to satisfy simultaneously
  d(gen,gen) >= 2 and d(gen,non) >= 2.
Thus deletion of any one known probe coordinate preserves both canonical orbit
reconstruction and generating/non-generating admissibility.

SciPy/HiGHS solves the resulting exact binary covering MILP.  The script also
verifies the displayed optimal code directly and proves by complete enumeration
that an H16-backward-compatible solution cannot use only three added probes.
"""
from __future__ import annotations

import sys
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

from generate_psl27_golden_model import (  # noqa: E402
    G, INV, ID, REPS, CLASS_OF, compose, conjugate, eval_word, subgroup,
)

LETTERS = "AaBb"
INV_LETTER = {"A": "a", "a": "A", "B": "b", "b": "B"}


def reduce_word(w: str) -> str:
    st = []
    for c in w:
        if st and INV_LETTER[c] == st[-1]:
            st.pop()
        else:
            st.append(c)
    return "".join(st)


def cyclic_reduce(w: str) -> str:
    w = reduce_word(w)
    while len(w) >= 2 and INV_LETTER[w[0]] == w[-1]:
        w = w[1:-1]
    return w


def canonical_cyclic(w: str) -> str:
    w = cyclic_reduce(w)
    if not w:
        return ""
    wi = "".join(INV_LETTER[c] for c in reversed(w))
    n = len(w)
    return min(v[i:] + v[:i] for v in (w, wi) for i in range(n))


def words_exact(length: int) -> list[str]:
    out = set()

    def rec(pref: str, last: str | None, left: int) -> None:
        if left == 0:
            c = canonical_cyclic(pref)
            if c and len(c) == length:
                out.add(c)
            return
        for x in LETTERS:
            if last and INV_LETTER[x] == last:
                continue
            rec(pref + x, x, left - 1)

    rec("", None, length)
    return sorted(out)


WORDS = sum((words_exact(k) for k in range(1, 6)), [])
assert len(WORDS) == 51
INDEX = {w: i for i, w in enumerate(WORDS)}


def simultaneous_orbit_reps():
    unseen = {(a, b) for a in G for b in G}
    gen, non = [], []
    while unseen:
        a, b = min(unseen)
        orbit = {(conjugate(h, a), conjugate(h, b)) for h in G}
        unseen -= orbit
        rep = min(orbit)
        (gen if len(subgroup(a, b)) == 168 else non).append(rep)
    gen.sort(); non.sort()
    assert gen == REPS
    assert len(gen) == 114 and len(non) == 83
    return gen, non


def signature(pair):
    a, b = pair
    return tuple(CLASS_OF[eval_word(w, a, b)] for w in WORDS)


GEN_REPS, NON_REPS = simultaneous_orbit_reps()
GEN = [signature(r) for r in GEN_REPS]
NON = list(dict.fromkeys(signature(r) for r in NON_REPS))
assert len(GEN) == 114 and len(NON) == 66


def diff_mask(x, y) -> int:
    m = 0
    for k in range(len(WORDS)):
        if x[k] != y[k]:
            m |= 1 << k
    return m


CONSTRAINT_MASKS = []
for i, j in combinations(range(len(GEN)), 2):
    CONSTRAINT_MASKS.append(diff_mask(GEN[i], GEN[j]))
for g in GEN:
    for n in NON:
        CONSTRAINT_MASKS.append(diff_mask(g, n))
assert len(CONSTRAINT_MASKS) == 13965


def mask(words) -> int:
    m = 0
    for w in words:
        m |= 1 << INDEX[w]
    return m


def minimum_distance(selected, left, right=None) -> int:
    ii = [INDEX[w] for w in selected]
    if right is None:
        return min(sum(x[k] != y[k] for k in ii) for x, y in combinations(left, 2))
    return min(sum(x[k] != y[k] for k in ii) for x in left for y in right)


def build_milp_constraints():
    rows = []
    for m in CONSTRAINT_MASKS:
        rows.append([(m >> k) & 1 for k in range(len(WORDS))])
    A = csr_matrix(np.asarray(rows, dtype=float))
    return LinearConstraint(A, np.full(len(rows), 2.0), np.full(len(rows), np.inf))


JOINT = build_milp_constraints()
BOUNDS = Bounds(np.zeros(len(WORDS)), np.ones(len(WORDS)))
INTEGRALITY = np.ones(len(WORDS))

# Primary optimum: minimum number of probes.
res = milp(
    np.ones(len(WORDS)),
    integrality=INTEGRALITY,
    bounds=BOUNDS,
    constraints=JOINT,
    options={"mip_rel_gap": 0.0},
)
assert res.success and round(res.fun) == 8

# Among 8-probe optima, minimize the number of length-5 probes.
card8 = LinearConstraint(np.ones((1, len(WORDS))), [8.0], [8.0])
depth5_cost = np.asarray([1.0 if len(w) == 5 else 0.0 for w in WORDS])
res5 = milp(
    depth5_cost,
    integrality=INTEGRALITY,
    bounds=BOUNDS,
    constraints=[JOINT, card8],
    options={"mip_rel_gap": 0.0},
)
assert res5.success and round(res5.fun) == 4

# Among 8-probe, four-depth-5 optima, minimize total word length.
exact4d5 = LinearConstraint(depth5_cost.reshape(1, -1), [4.0], [4.0])
length_cost = np.asarray([float(len(w)) for w in WORDS])
reslen = milp(
    length_cost,
    integrality=INTEGRALITY,
    bounds=BOUNDS,
    constraints=[JOINT, card8, exact4d5],
    options={"mip_rel_gap": 0.0},
)
assert reslen.success and round(reslen.fun) == 34

OPTIMAL_EIGHT = ("AAB", "Abb", "AAAB", "Abbb", "AABAb", "AAbAb", "ABABB", "ABaBB")
assert [len(w) for w in OPTIMAL_EIGHT] == [3, 3, 4, 4, 5, 5, 5, 5]
assert sum(map(len, OPTIMAL_EIGHT)) == 34
assert minimum_distance(OPTIMAL_EIGHT, GEN) == 2
assert minimum_distance(OPTIMAL_EIGHT, GEN, NON) == 2

# Backward-compatible H16 core.  Complete enumeration of all C(46,3)=15180
# three-coordinate extensions proves that eight total probes cannot suffice if
# these five coordinates are frozen.
H16 = ("A", "B", "AB", "Ab", "ABab")
H16_MASK = mask(H16)
remaining = [w for w in WORDS if w not in H16]
bad = [m for m in CONSTRAINT_MASKS if (m & H16_MASK).bit_count() < 2]
assert len(bad) == 67
for extra in combinations(remaining, 3):
    sm = H16_MASK | mask(extra)
    assert any((m & sm).bit_count() < 2 for m in bad)

H16_NINE = ("A", "B", "AA", "AB", "Ab", "ABB", "Abb", "ABab", "ABaBB")
assert minimum_distance(H16_NINE, GEN) == 2
assert minimum_distance(H16_NINE, GEN, NON) == 2
assert max(map(len, H16_NINE)) == 5
assert sum(len(w) == 5 for w in H16_NINE) == 1

print("HATTER-SOL-17 H17-04 joint one-erasure certificate")
print("candidate trace coordinates =", len(WORDS))
print("generating orbits =", len(GEN))
print("distinct non-generating full signatures =", len(NON))
print("joint pair constraints =", len(CONSTRAINT_MASKS))
print("minimum probe count = 8")
print("minimum depth-5 count among 8-probe optima = 4")
print("minimum total word length in that class = 34")
print("optimal eight =", OPTIMAL_EIGHT)
print("d_gen/gen =", minimum_distance(OPTIMAL_EIGHT, GEN))
print("d_gen/non =", minimum_distance(OPTIMAL_EIGHT, GEN, NON))
print("H16-compatible minimum count = 9 (C(46,3) exact exclusion)")
print("H16-compatible nine =", H16_NINE)
print("PASS")
