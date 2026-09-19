#!/usr/bin/env python3
"""HATTER-SOL-18 H18-01: exact adaptive word-tomography certificate.

The certificate reuses the canonical H17 PSL(2,7) model and its 114
simultaneous-conjugacy orbit representatives. The query pool Q_4 consists of
all class-valued observers induced by freely reduced words of length 1..4,
with observers deduplicated when they have exactly the same response vector on
all 114 canonical generating orbits.

Certified claims:
  * 160 freely reduced raw words of length <= 4 induce 50 distinct queries;
  * no adaptive decision tree of worst-case depth <= 3 identifies all 114
    orbits;
  * a depth-4 tree exists;
  * among depth-4 trees, minimum total path length is 382, hence minimum mean
    depth is 382/114 = 191/57;
  * one optimum has 48 internal nodes and uses 13 distinct query words;
  * its root query is AAB with nonempty branch sizes 32,30,21,21,10;
  * exactly 74 states terminate at depth 3 and 40 at depth 4;
  * no fixed set of <=4 queries separates all 114 states, while the five
    H16 words A,B,AB,Ab,ABab do. Thus within Q_4 the minimum fixed size is 5
    and adaptive worst-case depth is 4.

No floating point arithmetic is used.
"""

from __future__ import annotations
import argparse
import importlib.util
import json
from collections import Counter
from functools import lru_cache
from itertools import combinations
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
REPS = h17.REPS
ALL_MASK = (1 << len(REPS)) - 1
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

def observation_vector(word: str) -> tuple[int, ...]:
    return tuple(
        h17.CLASS_CODE[h17.CLASS_OF[h17.eval_word(word, a, b)]]
        for a, b in REPS
    )

def canonical_queries(max_len: int = 4):
    buckets: dict[tuple[int, ...], list[str]] = {}
    raw_words = reduced_words(max_len)
    for word in raw_words:
        buckets.setdefault(observation_vector(word), []).append(word)
    queries = []
    for vector, aliases in buckets.items():
        aliases.sort(key=lambda w: (len(w), w))
        queries.append((aliases[0], vector, tuple(aliases)))
    queries.sort(key=lambda q: (len(q[0]), q[0]))
    return raw_words, queries

RAW_WORDS, QUERIES = canonical_queries(4)
QUERY_MASKS: list[tuple[int, ...]] = []
for _, vector, _ in QUERIES:
    masks = [0] * len(CLASS_NAMES)
    for state, cls in enumerate(vector):
        masks[cls] |= 1 << state
    QUERY_MASKS.append(tuple(masks))

def popcount(mask: int) -> int:
    return mask.bit_count()

def partitions(mask: int, query_index: int) -> tuple[int, ...]:
    return tuple(mask & cm for cm in QUERY_MASKS[query_index] if mask & cm)

@lru_cache(maxsize=None)
def feasible(mask: int, depth: int) -> bool:
    n = popcount(mask)
    if n <= 1:
        return True
    if depth == 0 or n > len(CLASS_NAMES) ** depth:
        return False
    candidates = []
    for qi, (word, _, _) in enumerate(QUERIES):
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue
        max_part = max(popcount(p) for p in parts)
        if max_part > len(CLASS_NAMES) ** (depth - 1):
            continue
        candidates.append((max_part, -len(parts), len(word), word, qi, parts))
    candidates.sort()
    for *_, parts in candidates:
        if all(feasible(part, depth - 1) for part in parts):
            return True
    return False

@lru_cache(maxsize=None)
def optimum(mask: int, depth: int):
    """Lexicographically minimize path sum, node count, query-word-length sum."""
    n = popcount(mask)
    if n <= 1:
        return (0, 0, 0, -1)
    if depth == 0 or n > len(CLASS_NAMES) ** depth:
        return (INF, INF, INF, -1)
    best_key = None
    best = (INF, INF, INF, -1)
    for qi, (word, _, _) in enumerate(QUERIES):
        parts = partitions(mask, qi)
        if len(parts) <= 1:
            continue
        if max(popcount(p) for p in parts) > len(CLASS_NAMES) ** (depth - 1):
            continue
        children = [optimum(p, depth - 1) for p in parts]
        if any(c[0] >= INF for c in children):
            continue
        path_sum = n + sum(c[0] for c in children)
        nodes = 1 + sum(c[1] for c in children)
        word_cost = len(word) + sum(c[2] for c in children)
        key = (path_sum, nodes, word_cost, len(word), word)
        if best_key is None or key < best_key:
            best_key = key
            best = (path_sum, nodes, word_cost, qi)
    return best

def fixed_separates(query_indices) -> bool:
    seen = set()
    for state in range(len(REPS)):
        signature = tuple(QUERIES[qi][1][state] for qi in query_indices)
        if signature in seen:
            return False
        seen.add(signature)
    return True

def reconstruct(mask: int, depth: int, used: set[int], leaf_depths: Counter, level: int = 0):
    if popcount(mask) <= 1:
        leaf_depths[level] += popcount(mask)
        state = next((i for i in range(len(REPS)) if (mask >> i) & 1), None)
        return {"state": state}
    _, _, _, qi = optimum(mask, depth)
    assert qi >= 0
    used.add(qi)
    children = {}
    for cls, class_mask in enumerate(QUERY_MASKS[qi]):
        child = mask & class_mask
        if child:
            children[CLASS_NAMES[cls]] = reconstruct(child, depth - 1, used, leaf_depths, level + 1)
    return {"word": QUERIES[qi][0], "state_count": popcount(mask), "children": children}

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit-json", type=Path, default=None)
    args = parser.parse_args()

    assert len(REPS) == 114
    assert len(RAW_WORDS) == 160
    assert len(QUERIES) == 50
    assert feasible(ALL_MASK, 3) is False
    assert feasible(ALL_MASK, 4) is True

    path_sum, node_count, word_cost, root_qi = optimum(ALL_MASK, 4)
    assert path_sum == 382
    assert node_count == 48
    assert QUERIES[root_qi][0] == "AAB"

    root_sizes = sorted((popcount(p) for p in partitions(ALL_MASK, root_qi)), reverse=True)
    assert root_sizes == [32, 30, 21, 21, 10]

    used: set[int] = set()
    leaf_depths: Counter = Counter()
    tree = reconstruct(ALL_MASK, 4, used, leaf_depths)
    assert dict(sorted(leaf_depths.items())) == {3: 74, 4: 40}
    assert sum(depth * count for depth, count in leaf_depths.items()) == 382
    assert len(used) == 13

    for k in range(1, 5):
        assert not any(fixed_separates(c) for c in combinations(range(len(QUERIES)), k))

    h16_words = ("A", "B", "AB", "Ab", "ABab")
    word_to_qi = {q[0]: i for i, q in enumerate(QUERIES)}
    h16_indices = tuple(word_to_qi[w] for w in h16_words)
    assert fixed_separates(h16_indices)

    print("HATTER-SOL-18 H18-01 adaptive depth-4 certificate")
    print("canonical generating orbits =", len(REPS))
    print("raw freely reduced words length<=4 =", len(RAW_WORDS))
    print("distinct class-valued queries on 114 orbits =", len(QUERIES))
    print("depth<=3 possible =", feasible(ALL_MASK, 3))
    print("depth<=4 possible =", feasible(ALL_MASK, 4))
    print("minimum depth-4 total path length =", path_sum)
    print("minimum mean depth = 382/114 = 191/57 =", path_sum / len(REPS))
    print("internal decision nodes in selected optimum =", node_count)
    print("root query =", QUERIES[root_qi][0])
    print("root nonempty branch sizes =", root_sizes)
    print("leaf-depth distribution =", dict(sorted(leaf_depths.items())))
    selected_words = [QUERIES[i][0] for i in sorted(used, key=lambda i: (len(QUERIES[i][0]), QUERIES[i][0]))]
    print("distinct query words in selected optimum =", len(selected_words), selected_words)
    print("minimum fixed probe count within Q4 = 5")
    print("fixed five-probe witness =", h16_words)

    if args.emit_json is not None:
        args.emit_json.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "query_pool": {
                "raw_reduced_words_length_le_4": len(RAW_WORDS),
                "distinct_observers": len(QUERIES),
                "representatives": [q[0] for q in QUERIES],
            },
            "adaptive": {
                "minimum_worst_case_depth": 4,
                "minimum_total_path_length_at_depth_4": path_sum,
                "minimum_average_depth_at_depth_4": "191/57",
                "selected_optimum_internal_nodes": node_count,
                "selected_optimum_root": QUERIES[root_qi][0],
                "selected_optimum_root_branch_sizes": root_sizes,
                "selected_optimum_leaf_depths": dict(sorted(leaf_depths.items())),
                "selected_optimum_distinct_words": selected_words,
                "tree": tree,
            },
            "fixed": {"minimum_probe_count": 5, "witness": list(h16_words)},
        }
        args.emit_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print("JSON emitted:", args.emit_json)

    print("PASS: exact finite adaptive/fixed comparison certified")

if __name__ == "__main__":
    main()
