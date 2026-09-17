#!/usr/bin/env python3
"""HATTER-SOL-17 H17-07: optimal common-subexpression DAG for robust8 words.

The eight target words are
  AAB, Abb, AAAB, Abbb, AABAb, AAbAb, ABABB, ABaBB.

A naive independent evaluation needs sum(len(w)-1)=26 permutation compositions.
We optimize over all contiguous subwords of the targets.  Every selected
non-atomic word must be produced by concatenating two already available atoms
or selected subwords.  A zero-gap binary MILP proves the minimum number of
non-atomic DAG nodes/compositions is 14.

The displayed 14-node DAG is then checked exhaustively on all 168^2 ordered
PSL(2,7) input pairs against direct word evaluation.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

from generate_psl27_golden_model import G, INV, compose, eval_word  # noqa: E402

TARGETS = ("AAB", "Abb", "AAAB", "Abbb", "AABAb", "AAbAb", "ABABB", "ABaBB")
ATOMS = {"A", "a", "B", "b"}

# All contiguous non-atomic subwords available to a straight-line concatenation DAG.
SUBWORDS = set()
for t in TARGETS:
    for i in range(len(t)):
        for j in range(i + 2, len(t) + 1):
            SUBWORDS.add(t[i:j])
WORDS = sorted(SUBWORDS, key=lambda w: (len(w), w))
WI = {w: i for i, w in enumerate(WORDS)}

SPLITS = []
for w in WORDS:
    for k in range(1, len(w)):
        l, r = w[:k], w[k:]
        if (l in ATOMS or l in WI) and (r in ATOMS or r in WI):
            SPLITS.append((w, k, l, r))

nx = len(WORDS)
ny = len(SPLITS)
nvar = nx + ny
cost = np.zeros(nvar)
cost[:nx] = 1.0
lb = np.zeros(nvar)
ub = np.ones(nvar)
for t in TARGETS:
    lb[WI[t]] = 1.0
    ub[WI[t]] = 1.0

rows = []
lows = []
highs = []
for si, (w, _, l, r) in enumerate(SPLITS):
    y = nx + si
    rows.append({y: 1.0, WI[w]: -1.0}); lows.append(-np.inf); highs.append(0.0)
    for p in (l, r):
        if p not in ATOMS:
            rows.append({y: 1.0, WI[p]: -1.0}); lows.append(-np.inf); highs.append(0.0)
for w in WORDS:
    row = {WI[w]: -1.0}
    for si, s in enumerate(SPLITS):
        if s[0] == w:
            row[nx + si] = row.get(nx + si, 0.0) + 1.0
    rows.append(row); lows.append(0.0); highs.append(np.inf)

A = lil_matrix((len(rows), nvar))
for i, row in enumerate(rows):
    for j, v in row.items():
        A[i, j] = v
res = milp(
    cost,
    integrality=np.ones(nvar),
    bounds=Bounds(lb, ub),
    constraints=LinearConstraint(A.tocsr(), np.asarray(lows), np.asarray(highs)),
    options={"mip_rel_gap": 0.0},
)
assert res.success
assert round(res.fun) == 14

# One optimal DAG.  Each tuple is (new_word, left_word, right_word).
DAG = (
    ("AB", "A", "B"),
    ("Ab", "A", "b"),
    ("BB", "B", "B"),
    ("AAB", "A", "AB"),
    ("ABA", "AB", "A"),
    ("ABa", "AB", "a"),
    ("Abb", "Ab", "b"),
    ("AAAB", "A", "AAB"),
    ("AbAb", "Ab", "Ab"),
    ("Abbb", "Abb", "b"),
    ("AABAb", "AAB", "Ab"),
    ("AAbAb", "A", "AbAb"),
    ("ABABB", "ABA", "BB"),
    ("ABaBB", "ABa", "BB"),
)
assert len(DAG) == 14
assert {w for w, _, _ in DAG}.issuperset(TARGETS)


def eval_dag(a, b):
    values = {"A": a, "a": INV[a], "B": b, "b": INV[b]}
    for w, l, r in DAG:
        values[w] = compose(values[l], values[r])
    return tuple(values[w] for w in TARGETS)


for a in G:
    for b in G:
        got = eval_dag(a, b)
        ref = tuple(eval_word(w, a, b) for w in TARGETS)
        assert got == ref

print("HATTER-SOL-17 H17-07 robust8 word-DAG certificate")
print("naive independent composition count =", sum(len(w)-1 for w in TARGETS))
print("MILP optimum composition count =", round(res.fun))
print("selected DAG nodes =", [w for w,_,_ in DAG])
print("exhaustive pair checks =", len(G)*len(G))
print("PASS: 14 compositions are sufficient and MILP-optimal in the contiguous-subword DAG model")
