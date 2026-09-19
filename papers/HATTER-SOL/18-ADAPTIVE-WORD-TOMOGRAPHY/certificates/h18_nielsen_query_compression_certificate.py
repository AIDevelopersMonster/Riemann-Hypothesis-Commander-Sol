#!/usr/bin/env python3
"""HATTER-SOL-18 H18-09: Nielsen-compressed query-pool certificate.

This certificate works on the exact H18-06 197-state identify-or-REJECT model.

It proves:
  * exactly 24 of the 50 canonical W4 class queries are represented by
    primitive free-group words and are constructively reachable from a
    coordinate generator by elementary Nielsen moves with basis-word length
    <= 4;
  * on the 114 generating H17 orbits those 24 primitive queries leave exactly
    seven unresolved doublets, and they are exactly the seven H17 depth<=4
    commutator-defect pairs;
  * the commutator query ABab distinguishes every one of those seven pairs;
  * restricting the full H18 pool to 24 primitive queries plus the two oriented
    commutator queries ABab and AbaB leaves only 26 class-valued queries but
    preserves the exact worst-case adaptive depth 4;
  * under one persistent known query erasure, the restricted pool still needs
    and suffices with exactly four successful class answers, hence at most
    five total attempts;
  * the minimum fixed identify-or-REJECT set in the restricted pool is still
    five, with witness A,B,AB,Ab,ABab;
  * for generating-state tomography the restricted pool has minimum depth-4
    path sum 386 = 114*(193/57), versus the previously certified unrestricted
    W4 optimum 382.  Thus the Nielsen-normal restriction preserves worst-case
    depth but costs four aggregate queries over all 114 states.

No floating point arithmetic is used in the certified decisions.
"""

from __future__ import annotations

import importlib.util
import math
from collections import Counter, deque
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

INV_LETTER = {"A": "a", "a": "A", "B": "b", "b": "B"}
CLASS_INV = {0: 0, 1: 1, 2: 2, 3: 3, 4: 5, 5: 4}
INF = 10**12


def free_reduce(word: str) -> str:
    stack: list[str] = []
    for ch in word:
        if stack and INV_LETTER[stack[-1]] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


def inverse_word(word: str) -> str:
    return "".join(INV_LETTER[ch] for ch in reversed(word))


def multiply_words(left: str, right: str) -> str:
    return free_reduce(left + right)


def exponent_sum(word: str) -> tuple[int, int]:
    ea = sum(1 if ch == "A" else -1 if ch == "a" else 0 for ch in word)
    eb = sum(1 if ch == "B" else -1 if ch == "b" else 0 for ch in word)
    return ea, eb


def exponent_gcd(word: str) -> int:
    ea, eb = exponent_sum(word)
    return math.gcd(abs(ea), abs(eb))


def nielsen_bases(max_word_len: int = 4):
    """Construct bases reachable by elementary Nielsen moves.

    The length bound is only a finite witness-search bound.  Every primitive
    canonical W4 representative used below is explicitly found within it.
    """
    start = ("A", "B")
    parent = {start: None}
    move_name = {start: "ROOT"}
    queue = deque([start])

    def candidates(u: str, v: str):
        return (
            ("S", (v, u)),
            ("I_A", (inverse_word(u), v)),
            ("I_B", (u, inverse_word(v))),
            ("N_A+", (multiply_words(u, v), v)),
            ("N_A-", (multiply_words(u, inverse_word(v)), v)),
            ("N_B+", (u, multiply_words(v, u))),
            ("N_B-", (u, multiply_words(v, inverse_word(u)))),
        )

    while queue:
        u, v = queue.popleft()
        for name, pair in candidates(u, v):
            x, y = pair
            if len(x) > max_word_len or len(y) > max_word_len:
                continue
            if pair in parent:
                continue
            parent[pair] = (u, v)
            move_name[pair] = name
            queue.append(pair)

    return parent, move_name


BASIS_PARENT, BASIS_MOVE = nielsen_bases(4)
PRIMITIVE_WITNESS_WORDS = {
    w
    for u, v in BASIS_PARENT
    for w in (u, v)
    if 1 <= len(w) <= 4
}

QUERY_WORDS = [q[0] for q in c.QUERIES]
WORD_TO_QI = {word: i for i, word in enumerate(QUERY_WORDS)}

PRIMITIVE_WORDS_EXPECTED = [
    "A", "B", "a", "b",
    "AB", "Ab", "Ba", "ab",
    "AAB", "AAb", "ABB", "Abb", "BBa", "Baa", "aab", "abb",
    "AAAB", "AAAb", "ABBB", "Abbb", "BBBa", "Baaa", "aaab", "abbb",
]

PRIMITIVE_Q = tuple(
    i for i, word in enumerate(QUERY_WORDS)
    if word in PRIMITIVE_WITNESS_WORDS
)
assert [QUERY_WORDS[i] for i in PRIMITIVE_Q] == PRIMITIVE_WORDS_EXPECTED
assert len(PRIMITIVE_Q) == 24

COMMUTATOR_WORDS = ("ABab", "AbaB")
COMMUTATOR_Q = tuple(WORD_TO_QI[w] for w in COMMUTATOR_WORDS)
assert all(exponent_sum(w) == (0, 0) for w in COMMUTATOR_WORDS)

# The two oriented commutator observers differ only by inversion of the
# projective class: 1A..4A are self-inverse, 7A and 7B are exchanged.
vec_k = c.QUERIES[COMMUTATOR_Q[0]][1]
vec_kinv = c.QUERIES[COMMUTATOR_Q[1]][1]
assert tuple(CLASS_INV[x] for x in vec_k) == vec_kinv

RESTRICTED_Q = tuple(sorted(set(PRIMITIVE_Q + COMMUTATOR_Q)))
assert len(RESTRICTED_Q) == 26


def signature_classes(states, query_indices):
    buckets = {}
    for state in states:
        sig = tuple(c.QUERIES[qi][1][state] for qi in query_indices)
        buckets.setdefault(sig, []).append(state)
    return buckets


GEN_STATES = [i for i, is_gen in enumerate(c.IS_GENERATING) if is_gen]
NON_STATES = [i for i, is_gen in enumerate(c.IS_GENERATING) if not is_gen]
H17_ID = {rep: i for i, rep in enumerate(c.h17.REPS)}

primitive_gen_buckets = signature_classes(GEN_STATES, PRIMITIVE_Q)
primitive_gen_collisions = [
    states for states in primitive_gen_buckets.values() if len(states) > 1
]
assert len(primitive_gen_buckets) == 107
assert len(primitive_gen_collisions) == 7
assert all(len(states) == 2 for states in primitive_gen_collisions)

critical_h17_pairs = sorted(
    tuple(sorted(H17_ID[c.REPS[state]] for state in states))
    for states in primitive_gen_collisions
)
EXPECTED_CRITICAL = [
    (12, 27),
    (13, 28),
    (14, 29),
    (84, 89),
    (90, 92),
    (100, 103),
    (106, 107),
]
assert critical_h17_pairs == EXPECTED_CRITICAL

# Every primitive collision is split by the oriented commutator class 7A/7B.
qk = COMMUTATOR_Q[0]
for states in primitive_gen_collisions:
    values = {c.QUERIES[qk][1][state] for state in states}
    assert values == {4, 5}

# On all 197 states primitive observers leave 32 doublets:
# seven generating-generating and 25 non-generating/non-generating, with no
# generating/non-generating mixed collision.
primitive_all_buckets = signature_classes(range(len(c.REPS)), PRIMITIVE_Q)
primitive_all_collisions = [
    states for states in primitive_all_buckets.values() if len(states) > 1
]
assert len(primitive_all_buckets) == 165
assert len(primitive_all_collisions) == 32
assert all(len(states) == 2 for states in primitive_all_collisions)
collision_types = Counter(
    sum(1 for state in states if c.IS_GENERATING[state])
    for states in primitive_all_collisions
)
assert collision_types == Counter({0: 25, 2: 7})


def partitions(mask: int, query_index: int):
    return tuple(
        mask & class_mask
        for class_mask in c.QUERY_MASKS[query_index]
        if mask & class_mask
    )


@lru_cache(maxsize=None)
def restricted_no_erasure(mask: int, successful_left: int, banned_query: int) -> bool:
    if c.terminal(mask):
        return True
    if successful_left == 0:
        return False

    candidates = []
    for qi in RESTRICTED_Q:
        if qi == banned_query:
            continue
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue
        word = QUERY_WORDS[qi]
        candidates.append(
            (max(c.popcount(p) for p in parts), -len(parts), len(word), word, qi, parts)
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
    for qi in RESTRICTED_Q:
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue
        if not restricted_no_erasure(mask, successful_left, qi):
            continue
        word = QUERY_WORDS[qi]
        candidates.append(
            (max(c.popcount(p) for p in parts), -len(parts), len(word), word, qi, parts)
        )

    candidates.sort()
    for *_, parts in candidates:
        if all(
            restricted_one_erasure(part, successful_left - 1)
            for part in parts
        ):
            return True
    return False


def fixed_identify_or_reject(query_indices) -> bool:
    gen_seen = set()
    for state in GEN_STATES:
        sig = tuple(c.QUERIES[qi][1][state] for qi in query_indices)
        if sig in gen_seen:
            return False
        gen_seen.add(sig)

    non_seen = {
        tuple(c.QUERIES[qi][1][state] for qi in query_indices)
        for state in NON_STATES
    }
    return gen_seen.isdisjoint(non_seen)


# Exact fixed/adaptive claims in the 26-query Nielsen-normal pool.
assert restricted_no_erasure(c.ALL_MASK, 3, -1) is False
assert restricted_no_erasure(c.ALL_MASK, 4, -1) is True
assert restricted_one_erasure(c.ALL_MASK, 3) is False
assert restricted_one_erasure(c.ALL_MASK, 4) is True

for k in range(1, 5):
    assert not any(
        fixed_identify_or_reject(qs)
        for qs in combinations(RESTRICTED_Q, k)
    )

FIXED_WITNESS_WORDS = ("A", "B", "AB", "Ab", "ABab")
FIXED_WITNESS = tuple(WORD_TO_QI[w] for w in FIXED_WITNESS_WORDS)
assert all(qi in RESTRICTED_Q for qi in FIXED_WITNESS)
assert fixed_identify_or_reject(FIXED_WITNESS)


@lru_cache(maxsize=None)
def optimum_generating(mask: int, depth: int):
    """Minimize (total path length, internal nodes) on generating states."""
    n = c.popcount(mask)
    if n <= 1:
        return (0, 0, -1)
    if depth == 0 or n > len(c.CLASS_NAMES) ** depth:
        return (INF, INF, -1)

    best_key = None
    best = (INF, INF, -1)
    for qi in RESTRICTED_Q:
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue
        if max(c.popcount(p) for p in parts) > len(c.CLASS_NAMES) ** (depth - 1):
            continue
        children = [optimum_generating(part, depth - 1) for part in parts]
        if any(child[0] >= INF for child in children):
            continue
        path_sum = n + sum(child[0] for child in children)
        nodes = 1 + sum(child[1] for child in children)
        word = QUERY_WORDS[qi]
        key = (path_sum, nodes, len(word), word)
        if best_key is None or key < best_key:
            best_key = key
            best = (path_sum, nodes, qi)
    return best


path_sum, node_count, root_qi = optimum_generating(c.GEN_MASK, 4)
assert path_sum == 386
assert node_count == 48
assert QUERY_WORDS[root_qi] == "AAB"


def main() -> None:
    print("HATTER-SOL-18 H18-09 Nielsen query-compression certificate")
    print("W4 distinct class queries =", len(c.QUERIES))
    print("constructively primitive canonical queries =", len(PRIMITIVE_Q))
    print("primitive query words =", [QUERY_WORDS[i] for i in PRIMITIVE_Q])
    print("primitive-only generating signatures = 107")
    print("primitive-only unresolved generating doublets =", critical_h17_pairs)
    print("commutator ABab splits all seven doublets as 7A/7B")
    print("primitive-only full 197-state signature classes = 165")
    print("primitive-only doublets = 32 = 25 non-generating + 7 generating")
    print("restricted Nielsen-normal pool =", len(RESTRICTED_Q), "= 24 primitive + 2 commutator")
    print("restricted fixed minimum = 5")
    print("restricted fixed witness =", FIXED_WITNESS_WORDS)
    print("restricted no-erasure adaptive depth = 4")
    print("restricted one-erasure successful-query complexity = 4")
    print("restricted one-erasure worst total attempts = 5")
    print("restricted generating depth-4 optimum path sum =", path_sum)
    print("restricted generating mean depth = 386/114 = 193/57 =", path_sum / 114)
    print("restricted selected optimum internal nodes =", node_count)
    print("restricted selected optimum root =", QUERY_WORDS[root_qi])
    print("PASS: Nielsen primitive + commutator normal form preserves H18 worst-case query bounds")


if __name__ == "__main__":
    main()
