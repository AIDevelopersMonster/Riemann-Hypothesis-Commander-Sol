#!/usr/bin/env python3
"""HATTER-SOL-18 H18-10: exact query-alphabet compression certificate.

The per-transaction H18-06 optimum uses at most four successful class answers
and at most five attempts under one persistent known query erasure.  This file
asks a different question:

    how many DISTINCT W4 query labels must the controller support globally?

Certified statements
--------------------
* any globally supported alphabet for one persistent known erasure must have
  distance >= 2 on every generating/generating and generating/non-generating
  pair of H18-06 states;
* in the full 50-query W4 pool there are exactly seven critical pairs
  distinguished by only two query labels, ABab and AbaB, so both labels are
  forced in every distance-2 alphabet;
* exhaustive exact search of all C(48,6)=12,271,512 completions proves that
  no 8-query distance-2 alphabet exists;
* a 9-query distance-2 witness exists, so the minimum fixed robust alphabet
  inside the 50 W4 query labels is exactly 9;
* the 12-query Nielsen-core witness
      A, B, ABab, AbaB, ABB, Abb, AAb, AAAB, AAAb, Baa, aab, abb
  preserves the exact H18-06 adaptive bounds:
      no-erasure depth D0 = 4,
      one-erasure successful-query complexity S1 = 4,
      worst total attempts A1 = 5;
* ten of those twelve labels are primitive/Nielsen-coordinate observers and
  the remaining two are the oriented commutator pair.

Consequently, if M1(W4) denotes the minimum size of a GLOBAL query alphabet
that still permits the H18-06 one-erasure strategy with four successful
answers, then this certificate proves the exact bracket

    9 <= M1(W4) <= 12.

No floating point arithmetic is used.
"""

from __future__ import annotations

import importlib.util
from functools import lru_cache
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve()
H18 = HERE.parents[1]
H18_06 = H18 / "certificates" / "h18_adaptive_one_erasure_certificate.py"

spec = importlib.util.spec_from_file_location("h18_e1", H18_06)
assert spec is not None and spec.loader is not None
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

WORD_TO_Q = {word: i for i, (word, _, _) in enumerate(c.QUERIES)}
QUERY_WORDS = [q[0] for q in c.QUERIES]

GEN_STATES = [i for i, g in enumerate(c.IS_GENERATING) if g]
NON_STATES = [i for i, g in enumerate(c.IS_GENERATING) if not g]

REQUIRED_PAIRS = []
for pos, i in enumerate(GEN_STATES):
    for j in GEN_STATES[pos + 1 :]:
        REQUIRED_PAIRS.append((i, j))
    for j in NON_STATES:
        REQUIRED_PAIRS.append((i, j))

assert len(REQUIRED_PAIRS) == 15903


def distinguishing_queries(i: int, j: int) -> tuple[int, ...]:
    return tuple(
        qi
        for qi, (_, vector, _) in enumerate(c.QUERIES)
        if vector[i] != vector[j]
    )


# ---------------------------------------------------------------------------
# Exact global distance-2 lower bound.
# ---------------------------------------------------------------------------

critical = [
    (i, j, distinguishing_queries(i, j))
    for i, j in REQUIRED_PAIRS
    if len(distinguishing_queries(i, j)) == 2
]

assert len(critical) == 7

K = WORD_TO_Q["ABab"]
KINV = WORD_TO_Q["AbaB"]
assert all(set(qs) == {K, KINV} for _, _, qs in critical)

# Translate the seven generating pairs back to canonical H17 orbit IDs.
H17_ID = {rep: oid for oid, rep in enumerate(c.h17.REPS)}
critical_h17 = sorted(
    tuple(sorted((H17_ID[c.REPS[i]], H17_ID[c.REPS[j]])))
    for i, j, _ in critical
)
EXPECTED_CRITICAL_H17 = [
    (12, 27),
    (13, 28),
    (14, 29),
    (84, 89),
    (90, 92),
    (100, 103),
    (106, 107),
]
assert critical_h17 == EXPECTED_CRITICAL_H17

# The two oriented commutator queries have exactly the same equality pattern:
# when one distinguishes a pair, the other also distinguishes it.
for i, j in REQUIRED_PAIRS:
    assert (
        c.QUERIES[K][1][i] != c.QUERIES[K][1][j]
    ) == (
        c.QUERIES[KINV][1][i] != c.QUERIES[KINV][1][j]
    )

# Every distance-2 alphabet must contain K and KINV.  For all pairs not already
# hit twice by them, choose at most six further labels if a size-8 alphabet
# were to exist.  Exhaust all C(48,6) possibilities using exact Python bitsets.
remaining_pairs = [
    (i, j)
    for i, j in REQUIRED_PAIRS
    if c.QUERIES[K][1][i] == c.QUERIES[K][1][j]
]
assert len(remaining_pairs) == 3556

extras = [qi for qi in range(len(c.QUERIES)) if qi not in (K, KINV)]
assert len(extras) == 48

coverage = []
for qi in extras:
    vector = c.QUERIES[qi][1]
    bits = 0
    for bit, (i, j) in enumerate(remaining_pairs):
        if vector[i] != vector[j]:
            bits |= 1 << bit
    coverage.append(bits)

ALL_REMAINING = (1 << len(remaining_pairs)) - 1
checked_size8_completions = 0
size8_witness = None

for six in combinations(range(len(extras)), 6):
    checked_size8_completions += 1
    once = 0
    twice = 0
    for local_q in six:
        hit = coverage[local_q]
        twice |= once & hit
        once |= hit
    if twice == ALL_REMAINING:
        size8_witness = tuple(extras[q] for q in six)
        break

assert checked_size8_completions == 12271512
assert size8_witness is None


def minimum_required_distance(query_indices: tuple[int, ...]) -> int:
    return min(
        sum(
            c.QUERIES[qi][1][i] != c.QUERIES[qi][1][j]
            for qi in query_indices
        )
        for i, j in REQUIRED_PAIRS
    )


ROBUST9_WORDS = (
    "a", "b", "Ba", "ab", "BBa", "aab", "aaab", "ABab", "AbaB"
)
ROBUST9 = tuple(WORD_TO_Q[w] for w in ROBUST9_WORDS)
assert minimum_required_distance(ROBUST9) >= 2

# Thus the minimum distance-2 W4 alphabet is exactly 9:
#   no <=8 set exists, and ROBUST9 is a size-9 witness.


# ---------------------------------------------------------------------------
# Exact 12-query adaptive one-erasure upper bound.
# ---------------------------------------------------------------------------

NIELSEN_PRIMITIVE_WORDS = {
    "A", "B", "a", "b",
    "AB", "Ab", "Ba", "ab",
    "AAB", "AAb", "ABB", "Abb", "BBa", "Baa", "aab", "abb",
    "AAAB", "AAAb", "ABBB", "Abbb", "BBBa", "Baaa", "aaab", "abbb",
}

ADAPTIVE12_WORDS = (
    "A",
    "B",
    "ABab",
    "AbaB",
    "ABB",
    "Abb",
    "AAb",
    "AAAB",
    "AAAb",
    "Baa",
    "aab",
    "abb",
)
ADAPTIVE12 = tuple(WORD_TO_Q[w] for w in ADAPTIVE12_WORDS)

assert len(ADAPTIVE12) == 12
assert max(map(len, ADAPTIVE12_WORDS)) <= 4
assert sum(w in NIELSEN_PRIMITIVE_WORDS for w in ADAPTIVE12_WORDS) == 10
assert set(ADAPTIVE12_WORDS) - NIELSEN_PRIMITIVE_WORDS == {"ABab", "AbaB"}
assert minimum_required_distance(ADAPTIVE12) >= 2


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
    for qi in ADAPTIVE12:
        if qi == banned_query:
            continue
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue
        word = QUERY_WORDS[qi]
        candidates.append(
            (
                max(c.popcount(p) for p in parts),
                -len(parts),
                len(word),
                word,
                qi,
                parts,
            )
        )

    candidates.sort()
    for *_, parts in candidates:
        if all(
            restricted_no_erasure(
                part,
                successful_left - 1,
                banned_query,
            )
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
    for qi in ADAPTIVE12:
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue

        # If this query is erased now, it becomes unavailable permanently.
        if not restricted_no_erasure(mask, successful_left, qi):
            continue

        word = QUERY_WORDS[qi]
        candidates.append(
            (
                max(c.popcount(p) for p in parts),
                -len(parts),
                len(word),
                word,
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


assert restricted_no_erasure(c.ALL_MASK, 3, -1) is False
assert restricted_no_erasure(c.ALL_MASK, 4, -1) is True

assert restricted_one_erasure(c.ALL_MASK, 3) is False
assert restricted_one_erasure(c.ALL_MASK, 4) is True


def main() -> None:
    print("HATTER-SOL-18 H18-10 query-alphabet compression certificate")
    print("full W4 canonical query pool =", len(c.QUERIES))
    print("required gen/gen + gen/non pairs =", len(REQUIRED_PAIRS))
    print("critical pairs with only two W4 separators =", critical_h17)
    print("the two forced separators are =", ("ABab", "AbaB"))
    print("remaining pair constraints after forced commutator pair =", len(remaining_pairs))
    print("exhaustive size-8 completions checked =", checked_size8_completions)
    print("size-8 distance-2 alphabet exists =", size8_witness is not None)
    print("size-9 distance-2 witness =", ROBUST9_WORDS)
    print("minimum distance-2 W4 alphabet size = 9")
    print("adaptive 12-query witness =", ADAPTIVE12_WORDS)
    print("adaptive witness composition = 10 primitive + 2 commutator orientations")
    print("restricted no-erasure depth<=3 possible =", restricted_no_erasure(c.ALL_MASK, 3, -1))
    print("restricted no-erasure depth<=4 possible =", restricted_no_erasure(c.ALL_MASK, 4, -1))
    print("restricted one-erasure <=3 successful answers =", restricted_one_erasure(c.ALL_MASK, 3))
    print("restricted one-erasure <=4 successful answers =", restricted_one_erasure(c.ALL_MASK, 4))
    print("certified global alphabet bracket: 9 <= M1(W4) <= 12")
    print("PASS: exact H18 query-alphabet compression bounds certified")


if __name__ == "__main__":
    main()
