#!/usr/bin/env python3
"""Exact H18 M1 closure search at global alphabet size 9.

H18-10 already proves:
  * ABab and AbaB are forced in every distance-2 alphabet;
  * no distance-2 alphabet of size <= 8 exists.

Therefore every size-9 candidate has the form
    {ABab, AbaB} U S, |S| = 7,
with S chosen from the remaining 48 canonical W4 query labels.

This program performs an exhaustive branch-and-bound enumeration of only those
7-subsets that can still satisfy the pairwise distance-2 constraints.  Every
surviving robust alphabet is then tested against the exact H18-06 adaptive
one-persistent-known-erasure contract with four successful answers.

If an adaptive size-9 alphabet is found, H18-10's lower bound immediately gives
M1(W4)=9.

If the entire branch-and-bound tree is exhausted without a witness, size 9 is
excluded and the certified bracket improves to 10 <= M1(W4) <= 12.

No floating point arithmetic is used in any decision.
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

GEN_STATES = [i for i, g in enumerate(c.IS_GENERATING) if g]
NON_STATES = [i for i, g in enumerate(c.IS_GENERATING) if not g]

REQUIRED_PAIRS = []
for pos, i in enumerate(GEN_STATES):
    for j in GEN_STATES[pos + 1 :]:
        REQUIRED_PAIRS.append((i, j))
    for j in NON_STATES:
        REQUIRED_PAIRS.append((i, j))

assert len(REQUIRED_PAIRS) == 15903

K = WORD_TO_Q["ABab"]
KINV = WORD_TO_Q["AbaB"]

# Only pairs on which the forced pair contributes zero separations remain.
remaining_pairs = [
    (i, j)
    for i, j in REQUIRED_PAIRS
    if c.QUERIES[K][1][i] == c.QUERIES[K][1][j]
]
assert len(remaining_pairs) == 3556

ALL = (1 << len(remaining_pairs)) - 1

raw_extras = [qi for qi in range(len(c.QUERIES)) if qi not in (K, KINV)]
assert len(raw_extras) == 48

coverage_by_q = {}
for qi in raw_extras:
    vector = c.QUERIES[qi][1]
    bits = 0
    for bit, (i, j) in enumerate(remaining_pairs):
        if vector[i] != vector[j]:
            bits |= 1 << bit
    coverage_by_q[qi] = bits

# A fixed deterministic coverage-descending order improves pruning while
# preserving exhaustive enumeration of subsets.
EXTRAS = tuple(
    sorted(
        raw_extras,
        key=lambda qi: (-coverage_by_q[qi].bit_count(), QUERY_WORDS[qi], qi),
    )
)
COV = tuple(coverage_by_q[qi] for qi in EXTRAS)
N = len(EXTRAS)

# Suffix coverage by at least one / at least two remaining query labels.
suffix_once = [0] * (N + 1)
suffix_twice = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    hit = COV[i]
    suffix_twice[i] = suffix_twice[i + 1] | (suffix_once[i + 1] & hit)
    suffix_once[i] = suffix_once[i + 1] | hit

assert suffix_once[0] == ALL
assert suffix_twice[0] == ALL


def partitions(mask: int, query_index: int) -> tuple[int, ...]:
    return tuple(
        mask & class_mask
        for class_mask in c.QUERY_MASKS[query_index]
        if mask & class_mask
    )


def adaptive_contract(alphabet: tuple[int, ...]) -> tuple[bool, bool]:
    """Return (no-erasure depth<=4, one-erasure successful-depth<=4)."""

    @lru_cache(maxsize=None)
    def no_erasure(mask: int, successful_left: int, banned_query: int) -> bool:
        if c.terminal(mask):
            return True
        if successful_left == 0:
            return False

        candidates = []
        for qi in alphabet:
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
                no_erasure(part, successful_left - 1, banned_query)
                for part in parts
            ):
                return True
        return False

    @lru_cache(maxsize=None)
    def one_erasure(mask: int, successful_left: int) -> bool:
        if c.terminal(mask):
            return True
        if successful_left == 0:
            return False

        candidates = []
        for qi in alphabet:
            parts = partitions(mask, qi)
            if len(parts) <= 1:
                continue

            # If this query is erased now, it becomes permanently unavailable.
            if not no_erasure(mask, successful_left, qi):
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
                one_erasure(part, successful_left - 1)
                for part in parts
            ):
                return True
        return False

    no4 = no_erasure(c.ALL_MASK, 4, -1)
    if not no4:
        return False, False
    er4 = one_erasure(c.ALL_MASK, 4)
    return True, er4


nodes = 0
prune_suffix1 = 0
prune_suffix2 = 0
prune_slots = 0
robust_candidates = 0
no4_candidates = 0
adaptive_candidates = 0
witness = None


def dfs(start: int, chosen: tuple[int, ...], once: int, twice: int) -> bool:
    global nodes, prune_suffix1, prune_suffix2, prune_slots
    global robust_candidates, no4_candidates, adaptive_candidates, witness

    nodes += 1
    used = len(chosen)
    slots = 7 - used

    if slots == 0:
        if twice != ALL:
            return False

        robust_candidates += 1
        alphabet = tuple(sorted((K, KINV) + tuple(EXTRAS[i] for i in chosen)))
        no4, er4 = adaptive_contract(alphabet)
        if no4:
            no4_candidates += 1
        if no4 and er4:
            adaptive_candidates += 1
            witness = alphabet
            print("FOUND adaptive size-9 witness =", tuple(QUERY_WORDS[q] for q in alphabet))
            return True
        return False

    if N - start < slots:
        prune_slots += 1
        return False

    need2 = ALL ^ once
    need1 = once & (ALL ^ twice)

    if slots < 2 and need2:
        prune_slots += 1
        return False

    if need2 & ~suffix_twice[start]:
        prune_suffix2 += 1
        return False

    if need1 & ~suffix_once[start]:
        prune_suffix1 += 1
        return False

    # Choose remaining indices in strictly increasing position order.
    last = N - slots
    for pos in range(start, last + 1):
        hit = COV[pos]
        new_twice = twice | (once & hit)
        new_once = once | hit

        # Cheap branch-local suffix checks after choosing pos.
        rem = slots - 1
        nxt = pos + 1
        if rem:
            new_need2 = ALL ^ new_once
            new_need1 = new_once & (ALL ^ new_twice)
            if rem < 2 and new_need2:
                continue
            if new_need2 & ~suffix_twice[nxt]:
                continue
            if new_need1 & ~suffix_once[nxt]:
                continue

        if dfs(nxt, chosen + (pos,), new_once, new_twice):
            return True

    return False


def main() -> None:
    print("H18 M1 exact size-9 adaptive search")
    print("forced words =", ("ABab", "AbaB"))
    print("remaining labels =", N)
    print("remaining pair constraints =", len(remaining_pairs))
    print("raw size-9 completion count =", 73629072)

    found = dfs(0, (), 0, 0)

    print("DFS nodes =", nodes)
    print("robust distance-2 size-9 candidates tested =", robust_candidates)
    print("candidates with no-erasure depth<=4 =", no4_candidates)
    print("candidates satisfying full one-erasure depth<=4 =", adaptive_candidates)
    print("prune suffix-one =", prune_suffix1)
    print("prune suffix-two =", prune_suffix2)
    print("prune slots =", prune_slots)

    if found:
        print("RESULT: adaptive size-9 alphabet exists.")
        print("M1(W4) = 9 by H18-10 lower bound.")
        print("witness =", tuple(QUERY_WORDS[q] for q in witness))
    else:
        print("RESULT: exhaustive size-9 search found no adaptive witness.")
        print("CERTIFIED UPDATE: 10 <= M1(W4) <= 12.")

    print("PASS: exact size-9 search completed")


if __name__ == "__main__":
    main()
