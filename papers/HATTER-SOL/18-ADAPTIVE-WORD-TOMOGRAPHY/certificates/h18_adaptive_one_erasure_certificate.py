#!/usr/bin/env python3
"""HATTER-SOL-18 H18-06: exact adaptive one-erasure certificate.

Fault model
-----------
The observer may issue class-valued queries q_w for freely reduced words
of length <= 4.  At most one requested query may return ERASED.

To make the model comparable to a failed fixed probe rather than a transient
communication retry, an erased query is unavailable for the rest of the
transaction: the observer may not ask that same query again.  The observer
does know which requested query was erased.

Task
----
The state space is all simultaneous-conjugacy orbits in PSL(2,7)^2:
  * 114 generating orbits, each of which must be identified exactly;
  * all non-generating orbits, which share one terminal output REJECT.

Thus this is the H17 identify-or-reject/admissibility task, not merely
classification among already-known generating states.

Certified claims
----------------
  * PSL(2,7)^2 has 197 simultaneous-conjugacy pair orbits:
      114 generating + 83 non-generating;
  * the freely reduced length<=4 word pool has 160 raw words and 50 distinct
    class-valued queries on these 197 orbits;
  * without erasure, exact identify-or-reject depth is 4;
  * with at most one persistent known query erasure, four successful class
    answers still suffice;
  * therefore at most five query attempts suffice (4 successful + 1 erased);
  * three successful class answers are impossible even without erasure;
  * hence the one-erasure successful-query complexity is exactly 4 and the
    worst-case total-attempt complexity is exactly 5;
  * AAB is one admissible first query; in fact 16 canonical query
    representatives may serve as a first query in an exact 4-successful-answer
    one-erasure strategy.

No floating point arithmetic is used.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import deque
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve()
H18 = HERE.parents[1]
HATTER = H18.parent
H17_MODEL = HATTER / "17-NONABELIAN-TOMOGRAPHY-HARDWARE" / "tools" / "generate_psl27_golden_model.py"

spec = importlib.util.spec_from_file_location("h17_golden", H17_MODEL)
assert spec is not None and spec.loader is not None
h17 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h17)

ALPHABET = "ABab"
INVERSE_LETTER = {"A": "a", "a": "A", "B": "b", "b": "B"}
CLASS_NAMES = h17.CLASS_NAMES
CLASS_CODE = h17.CLASS_CODE
INF = 10**12


def reduced_words(max_len: int) -> list[str]:
    words: list[str] = []

    def visit(prefix: str) -> None:
        if prefix:
            words.append(prefix)
        if len(prefix) == max_len:
            return
        for ch in ALPHABET:
            if prefix and INVERSE_LETTER[prefix[-1]] == ch:
                continue
            visit(prefix + ch)

    visit("")
    return words


def all_pair_orbits():
    unseen = {(a, b) for a in h17.G for b in h17.G}
    rows = []
    generating_reps = set(h17.REPS)

    while unseen:
        a, b = min(unseen)
        orbit = {
            (h17.conjugate(g, a), h17.conjugate(g, b))
            for g in h17.G
        }
        unseen -= orbit
        rep = min(orbit)
        rows.append((rep, rep in generating_reps, len(orbit)))

    rows.sort(key=lambda row: row[0])
    assert len(rows) == 197
    assert sum(1 for _, is_generating, _ in rows if is_generating) == 114
    assert sum(1 for _, is_generating, _ in rows if not is_generating) == 83
    return rows


PAIR_ORBITS = all_pair_orbits()
REPS = [row[0] for row in PAIR_ORBITS]
IS_GENERATING = tuple(row[1] for row in PAIR_ORBITS)
GEN_MASK = sum((1 << i) for i, g in enumerate(IS_GENERATING) if g)
ALL_MASK = (1 << len(REPS)) - 1

RAW_WORDS = reduced_words(4)
assert len(RAW_WORDS) == 160


def observation_vector(word: str) -> tuple[int, ...]:
    return tuple(
        CLASS_CODE[h17.CLASS_OF[h17.eval_word(word, a, b)]]
        for a, b in REPS
    )


def canonical_queries():
    buckets: dict[tuple[int, ...], list[str]] = {}
    for word in RAW_WORDS:
        buckets.setdefault(observation_vector(word), []).append(word)

    queries = []
    for vector, aliases in buckets.items():
        aliases.sort(key=lambda w: (len(w), w))
        queries.append((aliases[0], vector, tuple(aliases)))

    queries.sort(key=lambda q: (len(q[0]), q[0]))
    assert len(queries) == 50
    return queries


QUERIES = canonical_queries()
QUERY_MASKS = []
for _, vector, _ in QUERIES:
    masks = [0] * len(CLASS_NAMES)
    for state, cls in enumerate(vector):
        masks[cls] |= 1 << state
    QUERY_MASKS.append(tuple(masks))


def popcount(mask: int) -> int:
    return mask.bit_count()


def terminal(mask: int) -> bool:
    if mask == 0:
        return True
    # All remaining states are non-generating: the correct answer is REJECT.
    if (mask & GEN_MASK) == 0:
        return True
    # A singleton generating state is exactly identified.
    return popcount(mask) == 1


def partitions(mask: int, query_index: int) -> tuple[int, ...]:
    return tuple(
        mask & class_mask
        for class_mask in QUERY_MASKS[query_index]
        if mask & class_mask
    )


@lru_cache(maxsize=None)
def no_erasure(mask: int, successful_left: int, banned_query: int) -> bool:
    """Exact feasibility after the unique erasure has already occurred."""
    if terminal(mask):
        return True
    if successful_left == 0:
        return False

    candidates = []
    for qi, (word, _, _) in enumerate(QUERIES):
        if qi == banned_query:
            continue
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue
        candidates.append(
            (max(popcount(p) for p in parts), -len(parts), len(word), word, qi, parts)
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
    """Feasibility while the one erasure is still available to the adversary.

    A successful class answer consumes one successful-query unit.
    An ERASED answer consumes no successful-query unit, leaves the candidate
    state set unchanged, permanently bans that query, and consumes the unique
    erasure budget.
    """
    if terminal(mask):
        return True
    if successful_left == 0:
        return False

    candidates = []
    for qi, (word, _, _) in enumerate(QUERIES):
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue

        # Adversary erases this query now.
        if not no_erasure(mask, successful_left, qi):
            continue

        candidates.append(
            (max(popcount(p) for p in parts), -len(parts), len(word), word, qi, parts)
        )

    candidates.sort()
    for *_, parts in candidates:
        # Successful response: erasure budget remains available.
        if all(one_erasure(part, successful_left - 1) for part in parts):
            return True
    return False


def good_roots(successful_budget: int) -> list[str]:
    roots = []
    for qi, (word, _, _) in enumerate(QUERIES):
        parts = partitions(ALL_MASK, qi)
        if len(parts) <= 1:
            continue
        if not no_erasure(ALL_MASK, successful_budget, qi):
            continue
        if all(one_erasure(part, successful_budget - 1) for part in parts):
            roots.append(word)
    return roots


def root_breakdown(word: str):
    qi = next(i for i, q in enumerate(QUERIES) if q[0] == word)
    vector = QUERIES[qi][1]
    out = {}
    for cls, name in enumerate(CLASS_NAMES):
        states = [i for i, value in enumerate(vector) if value == cls]
        out[name] = {
            "total": len(states),
            "generating": sum(1 for i in states if IS_GENERATING[i]),
            "non_generating": sum(1 for i in states if not IS_GENERATING[i]),
        }
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit-json", type=Path, default=None)
    args = parser.parse_args()

    assert len(PAIR_ORBITS) == 197
    assert len(RAW_WORDS) == 160
    assert len(QUERIES) == 50

    # No-erasure baseline.
    assert no_erasure(ALL_MASK, 3, -1) is False
    assert no_erasure(ALL_MASK, 4, -1) is True

    # Exact one-erasure result in successful-query units.
    assert one_erasure(ALL_MASK, 3) is False
    assert one_erasure(ALL_MASK, 4) is True

    roots = good_roots(4)
    expected_roots = [
        "AAB", "AAb", "ABB", "Abb",
        "BBa", "Baa", "aab", "abb",
        "AAAB", "AAAb", "ABBB", "Abbb",
        "BBBa", "Baaa", "aaab", "abbb",
    ]
    assert roots == expected_roots

    breakdown = root_breakdown("AAB")
    expected_breakdown = {
        "1A": {"total": 6, "generating": 0, "non_generating": 6},
        "2A": {"total": 27, "generating": 10, "non_generating": 17},
        "3A": {"total": 58, "generating": 30, "non_generating": 28},
        "4A": {"total": 46, "generating": 32, "non_generating": 14},
        "7A": {"total": 30, "generating": 21, "non_generating": 9},
        "7B": {"total": 30, "generating": 21, "non_generating": 9},
    }
    assert breakdown == expected_breakdown

    print("HATTER-SOL-18 H18-06 adaptive one-erasure certificate")
    print("all simultaneous-conjugacy pair orbits =", len(PAIR_ORBITS))
    print("generating pair orbits = 114")
    print("non-generating pair orbits = 83")
    print("raw freely reduced words length<=4 =", len(RAW_WORDS))
    print("distinct class-valued queries =", len(QUERIES))
    print("no-erasure depth<=3 possible =", no_erasure(ALL_MASK, 3, -1))
    print("no-erasure depth<=4 possible =", no_erasure(ALL_MASK, 4, -1))
    print("one-erasure with <=3 successful answers =", one_erasure(ALL_MASK, 3))
    print("one-erasure with <=4 successful answers =", one_erasure(ALL_MASK, 4))
    print("exact successful-query complexity = 4")
    print("exact worst-case total attempts = 5")
    print("canonical robust root AAB breakdown =", breakdown)
    print("admissible robust first-query representatives =", roots)
    print("PASS: exact identify-or-reject under one persistent known query erasure")

    if args.emit_json is not None:
        args.emit_json.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "state_space": {
                "simultaneous_conjugacy_pair_orbits": 197,
                "generating": 114,
                "non_generating_reject": 83,
            },
            "query_pool": {
                "raw_reduced_words_length_le_4": 160,
                "distinct_class_queries": 50,
            },
            "fault_model": {
                "maximum_erased_queries": 1,
                "erased_query_may_be_repeated": False,
                "erased_query_identity_known": True,
            },
            "result": {
                "minimum_successful_class_answers": 4,
                "maximum_total_query_attempts": 5,
                "canonical_first_query": "AAB",
                "admissible_first_queries": roots,
                "AAB_partition": breakdown,
            },
        }
        args.emit_json.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print("JSON emitted:", args.emit_json)


if __name__ == "__main__":
    main()
