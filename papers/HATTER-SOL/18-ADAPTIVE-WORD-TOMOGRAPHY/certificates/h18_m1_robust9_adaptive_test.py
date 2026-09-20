#!/usr/bin/env python3
"""H18 closure strike: test the certified minimum distance-2 9-query alphabet
against the full H18-06 adaptive one-persistent-erasure depth-four contract.

This does NOT assume that distance two implies adaptive depth four.  It tests the
actual dynamic programme with the same semantics as H18-06.

If the robust9 witness passes:
    M1(W4) = 9
because H18-10 already proved the global lower bound M1(W4) >= 9.

If it fails, no lower bound beyond 9 follows; a global search over other
size-9 alphabets is still required.
"""

from __future__ import annotations

import importlib.util
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve()
H18 = HERE.parents[1]
SRC = H18 / "certificates" / "h18_adaptive_one_erasure_certificate.py"

spec = importlib.util.spec_from_file_location("h18_e1", SRC)
assert spec is not None and spec.loader is not None
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

WORD_TO_Q = {word: i for i, (word, _, _) in enumerate(c.QUERIES)}
QUERY_WORDS = [q[0] for q in c.QUERIES]

ROBUST9_WORDS = (
    "a", "b", "Ba", "ab", "BBa", "aab", "aaab", "ABab", "AbaB"
)
ROBUST9 = tuple(WORD_TO_Q[w] for w in ROBUST9_WORDS)
assert len(ROBUST9) == 9


def partitions(mask: int, query_index: int) -> tuple[int, ...]:
    return tuple(
        mask & class_mask
        for class_mask in c.QUERY_MASKS[query_index]
        if mask & class_mask
    )


@lru_cache(maxsize=None)
def restricted_no_erasure(
    mask: int,
    successful_left: int,
    banned_query: int,
) -> bool:
    if c.terminal(mask):
        return True
    if successful_left == 0:
        return False

    candidates = []
    for qi in ROBUST9:
        if qi == banned_query:
            continue
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue
        candidates.append(
            (
                max(c.popcount(p) for p in parts),
                -len(parts),
                len(QUERY_WORDS[qi]),
                QUERY_WORDS[qi],
                qi,
                parts,
            )
        )

    candidates.sort()
    for *_, parts in candidates:
        if all(
            restricted_no_erasure(part, successful_left - 1, banned_query)
            for part in parts
        ):
            return True
    return False


@lru_cache(maxsize=None)
def restricted_one_erasure(mask: int, successful_left: int) -> bool:
    if c.terminal(mask):
        return True
    if successful_left == 0:
        return False

    candidates = []
    for qi in ROBUST9:
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue

        # If this query is erased now, it becomes permanently unavailable.
        if not restricted_no_erasure(mask, successful_left, qi):
            continue

        candidates.append(
            (
                max(c.popcount(p) for p in parts),
                -len(parts),
                len(QUERY_WORDS[qi]),
                QUERY_WORDS[qi],
                qi,
                parts,
            )
        )

    candidates.sort()
    for *_, parts in candidates:
        if all(
            restricted_one_erasure(part, successful_left - 1)
            for part in parts
        ):
            return True
    return False


def main() -> None:
    no3 = restricted_no_erasure(c.ALL_MASK, 3, -1)
    no4 = restricted_no_erasure(c.ALL_MASK, 4, -1)
    er3 = restricted_one_erasure(c.ALL_MASK, 3)
    er4 = restricted_one_erasure(c.ALL_MASK, 4)

    print("H18 M1 closure: robust9 adaptive-contract test")
    print("alphabet =", ROBUST9_WORDS)
    print("no-erasure <=3 successful answers =", no3)
    print("no-erasure <=4 successful answers =", no4)
    print("one-erasure <=3 successful answers =", er3)
    print("one-erasure <=4 successful answers =", er4)
    print("no-erasure cache =", restricted_no_erasure.cache_info())
    print("one-erasure cache =", restricted_one_erasure.cache_info())

    assert no3 is False
    assert er3 is False

    if no4 and er4:
        print("RESULT: ROBUST9 satisfies the full H18-06 adaptive contract.")
        print("COMBINED WITH H18-10 LOWER BOUND: M1(W4) = 9.")
    else:
        print("RESULT: ROBUST9 does NOT satisfy the full H18-06 adaptive contract.")
        print("GLOBAL M1(W4) remains in {9,10,11,12}; further alphabet search required.")


if __name__ == "__main__":
    main()
