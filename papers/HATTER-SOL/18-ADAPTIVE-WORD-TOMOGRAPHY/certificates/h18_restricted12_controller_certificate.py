#!/usr/bin/env python3
"""HATTER-SOL-18 H18-11: restricted 12-query controller certificate.

Starting from the exact H18-06 197-state one-persistent-erasure model, freeze
the H18-10 12-query alphabet

    A, B, ABab, AbaB, ABB, Abb, AAb, AAAB, AAAb, Baa, aab, abb.

This certificate proves, by exact finite dynamic programming and deterministic
materialization, that:

  * D0 = 4 without erasure;
  * S1 = 4 successful answers with one persistent known query erasure;
  * A1 = 5 total attempts;
  * the selected restricted strategy has exactly 305 nonterminal query nodes;
  * these split as 67 pre-erasure + 238 post-erasure nodes;
  * all 12 supported query labels are actually used;
  * canonical 9-bit node addressing is still sufficient;
  * a direct microprogram representation requires exactly 18,425 explicit
    payload bits before vendor-specific memory packing.

The file also computes shortest elementary-Nielsen programs for the ten
primitive labels.  This provides a claim boundary: Nielsen transport compresses
the semantic observer vocabulary, but does not automatically reduce the number
of permutation compositions required to realize each query independently.
"""

from __future__ import annotations

import importlib.util
from collections import Counter, deque
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve()
H18 = HERE.parents[1]
H18_06 = H18 / "certificates" / "h18_adaptive_one_erasure_certificate.py"

spec = importlib.util.spec_from_file_location("h18_e1", H18_06)
assert spec is not None and spec.loader is not None
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

WORDS = (
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

WORD_TO_QI = {q[0]: i for i, q in enumerate(c.QUERIES)}
Q = tuple(sorted(WORD_TO_QI[w] for w in WORDS))

NODE_KIND = 0
ORBIT_KIND = 1
REJECT_KIND = 2
INVALID_KIND = 3

GEN_ORBIT_ID = {rep: i for i, rep in enumerate(c.h17.REPS)}


def partitions(mask: int, qi: int):
    return tuple(
        mask & class_mask
        for class_mask in c.QUERY_MASKS[qi]
        if mask & class_mask
    )


@lru_cache(maxsize=None)
def no_erasure(mask: int, successful_left: int, banned_query: int) -> bool:
    if c.terminal(mask):
        return True
    if successful_left == 0:
        return False

    candidates = []
    for qi in Q:
        if qi == banned_query:
            continue
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue
        word = c.QUERIES[qi][0]
        candidates.append(
            (max(c.popcount(p) for p in parts), -len(parts), len(word), word, qi, parts)
        )

    candidates.sort()
    for *_, parts in candidates:
        if all(no_erasure(p, successful_left - 1, banned_query) for p in parts):
            return True
    return False


@lru_cache(maxsize=None)
def one_erasure(mask: int, successful_left: int) -> bool:
    if c.terminal(mask):
        return True
    if successful_left == 0:
        return False

    candidates = []
    for qi in Q:
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue
        if not no_erasure(mask, successful_left, qi):
            continue
        word = c.QUERIES[qi][0]
        candidates.append(
            (max(c.popcount(p) for p in parts), -len(parts), len(word), word, qi, parts)
        )

    candidates.sort()
    for *_, parts in candidates:
        if all(one_erasure(p, successful_left - 1) for p in parts):
            return True
    return False


assert no_erasure(c.ALL_MASK, 3, -1) is False
assert no_erasure(c.ALL_MASK, 4, -1) is True
assert one_erasure(c.ALL_MASK, 3) is False
assert one_erasure(c.ALL_MASK, 4) is True


def pick_no(mask: int, successful_left: int, banned_query: int):
    candidates = []
    for qi in Q:
        if qi == banned_query:
            continue
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue
        word = c.QUERIES[qi][0]
        candidates.append(
            (max(c.popcount(p) for p in parts), -len(parts), len(word), word, qi, parts)
        )
    candidates.sort()
    for *_, qi, parts in candidates:
        if all(no_erasure(p, successful_left - 1, banned_query) for p in parts):
            return qi
    raise AssertionError("no post-erasure strategy")


def pick_one(mask: int, successful_left: int):
    candidates = []
    for qi in Q:
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue
        if not no_erasure(mask, successful_left, qi):
            continue
        word = c.QUERIES[qi][0]
        candidates.append(
            (max(c.popcount(p) for p in parts), -len(parts), len(word), word, qi, parts)
        )
    candidates.sort()
    for *_, qi, parts in candidates:
        if all(one_erasure(p, successful_left - 1) for p in parts):
            return qi
    raise AssertionError("no pre-erasure strategy")


def terminal_target(mask: int):
    gm = mask & c.GEN_MASK
    if gm == 0:
        return (REJECT_KIND, 0)
    assert c.popcount(mask) == 1
    idx = mask.bit_length() - 1
    assert c.IS_GENERATING[idx]
    return (ORBIT_KIND, GEN_ORBIT_ID[c.REPS[idx]])


nodes = []
node_ids = {}


def materialize_no(mask: int, successful_left: int, banned_query: int):
    if c.terminal(mask):
        return terminal_target(mask)

    key = ("post", mask, successful_left, banned_query)
    if key in node_ids:
        return (NODE_KIND, node_ids[key])

    nid = len(nodes)
    node_ids[key] = nid
    nodes.append(None)

    qi = pick_no(mask, successful_left, banned_query)
    targets = [(INVALID_KIND, 0)] * 6
    for cls, class_mask in enumerate(c.QUERY_MASKS[qi]):
        part = mask & class_mask
        if part:
            targets[cls] = materialize_no(
                part,
                successful_left - 1,
                banned_query,
            )

    nodes[nid] = {
        "mode": "post-erasure",
        "word": c.QUERIES[qi][0],
        "query_index": qi,
        "targets": targets,
        "erasure_target": (INVALID_KIND, 0),
    }
    return (NODE_KIND, nid)


def materialize_one(mask: int, successful_left: int):
    if c.terminal(mask):
        return terminal_target(mask)

    key = ("pre", mask, successful_left)
    if key in node_ids:
        return (NODE_KIND, node_ids[key])

    nid = len(nodes)
    node_ids[key] = nid
    nodes.append(None)

    qi = pick_one(mask, successful_left)
    targets = [(INVALID_KIND, 0)] * 6
    for cls, class_mask in enumerate(c.QUERY_MASKS[qi]):
        part = mask & class_mask
        if part:
            targets[cls] = materialize_one(
                part,
                successful_left - 1,
            )

    erase_target = materialize_no(mask, successful_left, qi)

    nodes[nid] = {
        "mode": "pre-erasure",
        "word": c.QUERIES[qi][0],
        "query_index": qi,
        "targets": targets,
        "erasure_target": erase_target,
    }
    return (NODE_KIND, nid)


ROOT = materialize_one(c.ALL_MASK, 4)
assert ROOT == (NODE_KIND, 0)

PRE = sum(node["mode"] == "pre-erasure" for node in nodes)
POST = sum(node["mode"] == "post-erasure" for node in nodes)
USED = Counter(node["word"] for node in nodes)

assert len(nodes) == 305
assert PRE == 67
assert POST == 238
assert set(USED) == set(WORDS)

# Canonical terminal encoding:
#   0..304 query nodes
#   305..418 generating orbit terminals
#   419 REJECT
#   420 FAULT
# 421 distinct values still fit in 9 bits.
NODE_BITS = 9
assert 421 <= (1 << NODE_BITS)

# Direct explicit microprogram payload:
# query selector: 305 * ceil(log2(12)) = 305*4
# class transitions: 305*6*9
# erasure transitions: 67*9
# word descriptors: 12*(3-bit length + 8-bit packed letters)
QUERY_SELECTOR_BITS = 305 * 4
CLASS_TRANSITION_BITS = 305 * 6 * NODE_BITS
ERASURE_TRANSITION_BITS = PRE * NODE_BITS
WORD_DESCRIPTOR_BITS = 12 * 11
TOTAL_BITS = (
    QUERY_SELECTOR_BITS
    + CLASS_TRANSITION_BITS
    + ERASURE_TRANSITION_BITS
    + WORD_DESCRIPTOR_BITS
)

assert QUERY_SELECTOR_BITS == 1220
assert CLASS_TRANSITION_BITS == 16470
assert ERASURE_TRANSITION_BITS == 603
assert WORD_DESCRIPTOR_BITS == 132
assert TOTAL_BITS == 18425

# ---------------------------------------------------------------------------
# Constructive shortest elementary-Nielsen programs for the ten primitive
# labels in the 12-query witness.
# ---------------------------------------------------------------------------

INV_LETTER = {"A": "a", "a": "A", "B": "b", "b": "B"}


def free_reduce(word: str) -> str:
    stack = []
    for ch in word:
        if stack and INV_LETTER[stack[-1]] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


def inverse_word(word: str) -> str:
    return "".join(INV_LETTER[ch] for ch in reversed(word))


def mul(left: str, right: str) -> str:
    return free_reduce(left + right)


def neighbors(pair):
    u, v = pair
    return (
        ("S", (v, u)),
        ("I_A", (inverse_word(u), v)),
        ("I_B", (u, inverse_word(v))),
        ("N_A+", (mul(u, v), v)),
        ("N_A-", (mul(u, inverse_word(v)), v)),
        ("N_B+", (u, mul(v, u))),
        ("N_B-", (u, mul(v, inverse_word(u)))),
    )


PRIMITIVE = tuple(w for w in WORDS if w not in ("ABab", "AbaB"))
assert len(PRIMITIVE) == 10


def shortest_programs(max_word_len=8, max_depth=8):
    start = ("A", "B")
    queue = deque([start])
    parent = {start: (None, None)}
    depth = {start: 0}
    found = {}

    while queue and len(found) < len(PRIMITIVE):
        pair = queue.popleft()
        d = depth[pair]

        for word in PRIMITIVE:
            if word in found:
                continue
            if pair[0] == word:
                found[word] = (pair, 0)
            elif pair[1] == word:
                found[word] = (pair, 1)

        if d >= max_depth:
            continue

        for opname, nxt in neighbors(pair):
            if max(len(nxt[0]), len(nxt[1])) > max_word_len:
                continue
            if nxt in parent:
                continue
            parent[nxt] = (pair, opname)
            depth[nxt] = d + 1
            queue.append(nxt)

    assert len(found) == len(PRIMITIVE)

    out = {}
    for word, (pair, coordinate) in found.items():
        program = []
        cur = pair
        while parent[cur][0] is not None:
            prev, opname = parent[cur]
            program.append(opname)
            cur = prev
        program.reverse()
        out[word] = (len(program), coordinate, tuple(program), pair)
    return out


PROGRAMS = shortest_programs()

EXPECTED_NIELSEN_LENGTH = {
    "A": 0,
    "B": 0,
    "ABB": 2,
    "Abb": 2,
    "AAb": 2,
    "Baa": 2,
    "aab": 3,
    "abb": 3,
    "AAAb": 3,
    "AAAB": 4,
}

assert {w: PROGRAMS[w][0] for w in PRIMITIVE} == EXPECTED_NIELSEN_LENGTH

DIRECT_COMPOSITIONS = {w: len(w) - 1 for w in WORDS}
NIELSEN_DELTA = {
    w: PROGRAMS[w][0] - DIRECT_COMPOSITIONS[w]
    for w in PRIMITIVE
}

# Exact claim boundary:
# seven primitive labels tie direct execution, while three require one
# additional elementary Nielsen move.
assert Counter(NIELSEN_DELTA.values()) == Counter({0: 7, 1: 3})


def main() -> None:
    print("HATTER-SOL-18 H18-11 restricted 12-query controller certificate")
    print("query alphabet =", WORDS)
    print("D0 =", 4)
    print("S1 =", 4)
    print("A1 =", 5)
    print("query nodes =", len(nodes))
    print("pre-erasure nodes =", PRE)
    print("post-erasure nodes =", POST)
    print("query use counts =", dict(sorted(USED.items())))
    print("query-selector bits =", QUERY_SELECTOR_BITS)
    print("class-transition bits =", CLASS_TRANSITION_BITS)
    print("erasure-transition bits =", ERASURE_TRANSITION_BITS)
    print("word-descriptor bits =", WORD_DESCRIPTOR_BITS)
    print("total explicit microprogram payload bits =", TOTAL_BITS)
    print("shortest Nielsen program lengths =", EXPECTED_NIELSEN_LENGTH)
    print("Nielsen minus direct composition deltas =", NIELSEN_DELTA)
    print("PASS: restricted 12-query controller and representation certified")


if __name__ == "__main__":
    main()
