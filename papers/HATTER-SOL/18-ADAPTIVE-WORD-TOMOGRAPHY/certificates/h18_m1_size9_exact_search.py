#!/usr/bin/env python3
"""Exact H18 M1(W4) size-9 search.

Search every size-9 W4 alphabet satisfying the necessary distance-two
condition, then test the exact H18-06 adaptive contract:

    D0 <= 4
    S1 <= 4 under one persistent known query erasure.

H18-10 proves that ABab and AbaB are forced in every distance-two alphabet.
Therefore a size-9 candidate is exactly those two labels plus 7 of the
remaining 48 labels.

The distance-two subset search is delegated to Z3 as an exact finite Boolean
constraint problem.  Every satisfying model is blocked after inspection, so
UNSAT after enumeration is an exhaustive certificate relative to the encoded
constraints.  Candidate alphabets are then checked by the same finite dynamic
programming semantics used in H18-06/H18-10.

No floating point arithmetic is used.
"""

from __future__ import annotations

import importlib.util
import time
from functools import lru_cache
from pathlib import Path

from z3 import Bool, If, Solver, Sum, sat

HERE = Path(__file__).resolve()
H18 = HERE.parents[1]
SRC = H18 / "certificates" / "h18_adaptive_one_erasure_certificate.py"

spec = importlib.util.spec_from_file_location("h18_e1", SRC)
assert spec is not None and spec.loader is not None
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

WORDS = [q[0] for q in c.QUERIES]
WORD_TO_Q = {w: i for i, w in enumerate(WORDS)}
K = WORD_TO_Q["ABab"]
KINV = WORD_TO_Q["AbaB"]
FORCED = (K, KINV)
EXTRAS = tuple(q for q in range(len(c.QUERIES)) if q not in FORCED)
assert len(EXTRAS) == 48

GEN = [i for i, g in enumerate(c.IS_GENERATING) if g]
NON = [i for i, g in enumerate(c.IS_GENERATING) if not g]

REQUIRED = []
for pos, i in enumerate(GEN):
    for j in GEN[pos + 1 :]:
        REQUIRED.append((i, j))
    for j in NON:
        REQUIRED.append((i, j))
assert len(REQUIRED) == 15903


def distinguishes(qi: int, i: int, j: int) -> bool:
    v = c.QUERIES[qi][1]
    return v[i] != v[j]


# Pairs not already separated twice by the forced pair need two hits from EXTRAS.
# H18-10 proved ABab/AbaB have the same equality pattern, so this is equivalent
# to requiring two extra hits exactly when the forced pair gives zero.
REMAINING = [
    (i, j)
    for i, j in REQUIRED
    if not distinguishes(K, i, j)
]
assert len(REMAINING) == 3556
assert all(not distinguishes(KINV, i, j) for i, j in REMAINING)

COVERERS = []
for i, j in REMAINING:
    qs = tuple(q for q in EXTRAS if distinguishes(q, i, j))
    assert len(qs) >= 2
    COVERERS.append(qs)


def partitions(mask: int, qi: int) -> tuple[int, ...]:
    return tuple(
        mask & class_mask
        for class_mask in c.QUERY_MASKS[qi]
        if mask & class_mask
    )


def adaptive_contract(alphabet: tuple[int, ...]) -> tuple[bool, bool, dict]:
    """Return (D0<=4, S1<=4, cache statistics)."""

    @lru_cache(maxsize=None)
    def no_erasure(mask: int, left: int, banned: int) -> bool:
        if c.terminal(mask):
            return True
        if left == 0:
            return False

        candidates = []
        for qi in alphabet:
            if qi == banned:
                continue
            parts = partitions(mask, qi)
            if len(parts) <= 1:
                continue
            candidates.append(
                (
                    max(c.popcount(p) for p in parts),
                    -len(parts),
                    len(WORDS[qi]),
                    WORDS[qi],
                    qi,
                    parts,
                )
            )
        candidates.sort()

        for *_, parts in candidates:
            if all(no_erasure(p, left - 1, banned) for p in parts):
                return True
        return False

    @lru_cache(maxsize=None)
    def one_erasure(mask: int, left: int) -> bool:
        if c.terminal(mask):
            return True
        if left == 0:
            return False

        candidates = []
        for qi in alphabet:
            parts = partitions(mask, qi)
            if len(parts) <= 1:
                continue
            if not no_erasure(mask, left, qi):
                continue
            candidates.append(
                (
                    max(c.popcount(p) for p in parts),
                    -len(parts),
                    len(WORDS[qi]),
                    WORDS[qi],
                    qi,
                    parts,
                )
            )
        candidates.sort()

        for *_, parts in candidates:
            if all(one_erasure(p, left - 1) for p in parts):
                return True
        return False

    d0 = no_erasure(c.ALL_MASK, 4, -1)
    if not d0:
        return False, False, {
            "no": no_erasure.cache_info(),
            "one": one_erasure.cache_info(),
        }

    s1 = one_erasure(c.ALL_MASK, 4)
    return d0, s1, {
        "no": no_erasure.cache_info(),
        "one": one_erasure.cache_info(),
    }


def main() -> None:
    t0 = time.time()

    x = {q: Bool(f"x_{q}") for q in EXTRAS}
    solver = Solver()

    solver.add(Sum([If(x[q], 1, 0) for q in EXTRAS]) == 7)

    for qs in COVERERS:
        solver.add(Sum([If(x[q], 1, 0) for q in qs]) >= 2)

    robust_models = 0
    d0_models = 0
    witness = None

    while solver.check() == sat:
        model = solver.model()
        chosen = tuple(q for q in EXTRAS if bool(model.eval(x[q], model_completion=True)))
        assert len(chosen) == 7

        alphabet = tuple(sorted(FORCED + chosen))
        robust_models += 1

        d0, s1, stats = adaptive_contract(alphabet)
        if d0:
            d0_models += 1

        if robust_models <= 20 or d0 or robust_models % 1000 == 0:
            print(
                "MODEL",
                robust_models,
                "alphabet=", tuple(WORDS[q] for q in alphabet),
                "D0<=4=", d0,
                "S1<=4=", s1,
                "no_cache=", stats["no"],
                "one_cache=", stats["one"],
                flush=True,
            )

        if d0 and s1:
            witness = alphabet
            break

        # Exact model blocking: with the exact-cardinality constraint, it is
        # sufficient to require that at least one currently selected extra is
        # deselected in the next model.
        solver.add(Sum([If(x[q], 1, 0) for q in chosen]) <= 6)

    elapsed = time.time() - t0

    print("size-9 robust models inspected =", robust_models)
    print("size-9 models with D0<=4 =", d0_models)
    print("elapsed seconds =", f"{elapsed:.3f}")

    if witness is not None:
        words = tuple(WORDS[q] for q in witness)
        print("RESULT: size-9 full adaptive witness =", words)
        print("COMBINED WITH H18-10 LOWER BOUND: M1(W4) = 9")
        return

    print("RESULT: no size-9 alphabet satisfies the full adaptive contract.")
    print("EXHAUSTIVE CONCLUSION: M1(W4) >= 10.")
    print("COMBINED WITH H18-10 UPPER BOUND: 10 <= M1(W4) <= 12.")


if __name__ == "__main__":
    main()
