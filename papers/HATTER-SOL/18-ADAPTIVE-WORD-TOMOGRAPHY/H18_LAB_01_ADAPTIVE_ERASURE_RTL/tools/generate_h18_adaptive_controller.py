#!/usr/bin/env python3
"""Generate the frozen H18-07 adaptive one-erasure controller.

Outputs:
  * h18_adaptive_controller_rom.sv
  * h18_adaptive_word_rom.sv
  * h18_adaptive_controller.json
  * h18_adaptive_vectors.txt

The strategy is materialized from the exact H18-06 recurrence.

Target encoding used by the controller ROM:
  kind=0 -> another controller node, payload=node_id
  kind=1 -> terminal generating orbit, payload=canonical H17 orbit_id
  kind=2 -> terminal REJECT
  kind=3 -> invalid/unreachable transition

The generated vector set covers all 197 simultaneous-conjugacy pair-orbit
representatives and erasure injection positions 0..5.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve()
LAB = HERE.parents[1]
H18 = LAB.parent
CERT = H18 / "certificates" / "h18_adaptive_one_erasure_certificate.py"

spec = importlib.util.spec_from_file_location("h18_e1", CERT)
assert spec is not None and spec.loader is not None
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

NODE_KIND = 0
ORBIT_KIND = 1
REJECT_KIND = 2
INVALID_KIND = 3

GEN_ORBIT_ID = {rep: i for i, rep in enumerate(c.h17.REPS)}


def pick_no(mask: int, successful_left: int, banned_query: int):
    candidates = []
    for qi, (word, _, _) in enumerate(c.QUERIES):
        if qi == banned_query:
            continue
        parts = c.partitions(mask, qi)
        if len(parts) <= 1:
            continue
        candidates.append(
            (max(c.popcount(p) for p in parts), -len(parts), len(word), word, qi, parts)
        )
    candidates.sort()
    for *_, qi, parts in candidates:
        if all(c.no_erasure(p, successful_left - 1, banned_query) for p in parts):
            return qi
    raise AssertionError("no no-erasure strategy")


def pick_one(mask: int, successful_left: int):
    candidates = []
    for qi, (word, _, _) in enumerate(c.QUERIES):
        parts = c.partitions(mask, qi)
        if len(parts) <= 1:
            continue
        if not c.no_erasure(mask, successful_left, qi):
            continue
        candidates.append(
            (max(c.popcount(p) for p in parts), -len(parts), len(word), word, qi, parts)
        )
    candidates.sort()
    for *_, qi, parts in candidates:
        if all(c.one_erasure(p, successful_left - 1) for p in parts):
            return qi
    raise AssertionError("no one-erasure strategy")


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
    class_targets = [(INVALID_KIND, 0)] * 6
    for cls, class_mask in enumerate(c.QUERY_MASKS[qi]):
        part = mask & class_mask
        if part:
            class_targets[cls] = materialize_no(
                part, successful_left - 1, banned_query
            )

    nodes[nid] = {
        "mode": "post-erasure",
        "mask": mask,
        "successful_left": successful_left,
        "banned_query": banned_query,
        "query_index": qi,
        "word": c.QUERIES[qi][0],
        "class_targets": class_targets,
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
    class_targets = [(INVALID_KIND, 0)] * 6
    for cls, class_mask in enumerate(c.QUERY_MASKS[qi]):
        part = mask & class_mask
        if part:
            class_targets[cls] = materialize_one(part, successful_left - 1)

    erase_target = materialize_no(mask, successful_left, qi)

    nodes[nid] = {
        "mode": "pre-erasure",
        "mask": mask,
        "successful_left": successful_left,
        "banned_query": -1,
        "query_index": qi,
        "word": c.QUERIES[qi][0],
        "class_targets": class_targets,
        "erasure_target": erase_target,
    }
    return (NODE_KIND, nid)


ROOT = materialize_one(c.ALL_MASK, 4)
assert ROOT == (NODE_KIND, 0)

USED_WORDS = sorted(
    {node["word"] for node in nodes},
    key=lambda w: (len(w), w),
)
WORD_ID = {word: i for i, word in enumerate(USED_WORDS)}

# Frozen metrics: any change means the strategy/materialization changed.
assert len(nodes) == 308
assert sum(node["mode"] == "pre-erasure" for node in nodes) == 69
assert sum(node["mode"] == "post-erasure" for node in nodes) == 239
assert len(USED_WORDS) == 24
assert max(map(len, USED_WORDS)) == 4

SYMBOL = {"A": 0, "a": 1, "B": 2, "b": 3}


def pack_word(word: str):
    value = 0
    for pos, ch in enumerate(word):
        value |= SYMBOL[ch] << (2 * pos)
    return len(word), value


def target_sv(target):
    kind, payload = target
    return f"{{2'd{kind},9'd{payload}}}"


def emit_word_rom(path: Path):
    lines = [
        "// Auto-generated by generate_h18_adaptive_controller.py.",
        "module h18_adaptive_word_rom(",
        "    input  logic [4:0] word_id,",
        "    output logic [2:0] word_len,",
        "    output logic [7:0] word_ops",
        ");",
        "always_comb begin",
        "  word_len = 3'd0;",
        "  word_ops = 8'h00;",
        "  case (word_id)",
    ]
    for word, wid in WORD_ID.items():
        n, value = pack_word(word)
        lines.append(
            f"    5'd{wid}: begin word_len=3'd{n}; word_ops=8'h{value:02x}; end // {word}"
        )
    lines += [
        "    default: ;",
        "  endcase",
        "end",
        "endmodule",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def emit_controller_rom(path: Path):
    lines = [
        "// Auto-generated H18-07 adaptive one-erasure controller.",
        "// target[10:9]: 0=node, 1=orbit, 2=REJECT, 3=invalid.",
        "// target[8:0] : node_id or canonical H17 orbit_id.",
        "module h18_adaptive_controller_rom(",
        "    input  logic [8:0]  node_id,",
        "    output logic [4:0]  word_id,",
        "    output logic        erasure_allowed,",
        "    output logic [10:0] next_1A,",
        "    output logic [10:0] next_2A,",
        "    output logic [10:0] next_3A,",
        "    output logic [10:0] next_4A,",
        "    output logic [10:0] next_7A,",
        "    output logic [10:0] next_7B,",
        "    output logic [10:0] next_erased",
        ");",
        "always_comb begin",
        "  word_id = 5'd0;",
        "  erasure_allowed = 1'b0;",
        "  next_1A = {2'd3,9'd0}; next_2A = {2'd3,9'd0};",
        "  next_3A = {2'd3,9'd0}; next_4A = {2'd3,9'd0};",
        "  next_7A = {2'd3,9'd0}; next_7B = {2'd3,9'd0};",
        "  next_erased = {2'd3,9'd0};",
        "  case (node_id)",
    ]
    for nid, node in enumerate(nodes):
        t = node["class_targets"]
        lines += [
            f"    9'd{nid}: begin // {node['mode']} s={node['successful_left']} word={node['word']}",
            f"      word_id = 5'd{WORD_ID[node['word']]};",
            f"      erasure_allowed = 1'b{1 if node['mode']=='pre-erasure' else 0};",
            f"      next_1A = {target_sv(t[0])};",
            f"      next_2A = {target_sv(t[1])};",
            f"      next_3A = {target_sv(t[2])};",
            f"      next_4A = {target_sv(t[3])};",
            f"      next_7A = {target_sv(t[4])};",
            f"      next_7B = {target_sv(t[5])};",
            f"      next_erased = {target_sv(node['erasure_target'])};",
            "    end",
        ]
    lines += [
        "    default: ;",
        "  endcase",
        "end",
        "endmodule",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def choose_class_target(node, cls):
    return node["class_targets"][cls]


def simulate_state(state_index: int, erase_attempt: int):
    node_id = 0
    attempts = 0
    successes = 0
    while True:
        node = nodes[node_id]
        attempts += 1

        if erase_attempt != 0 and attempts == erase_attempt:
            target = node["erasure_target"]
        else:
            cls = c.QUERIES[node["query_index"]][1][state_index]
            target = choose_class_target(node, cls)
            successes += 1

        kind, payload = target
        if kind == NODE_KIND:
            node_id = payload
            continue
        if kind == ORBIT_KIND:
            return 2, payload, attempts, successes
        if kind == REJECT_KIND:
            return 1, 127, attempts, successes
        return 4, 127, attempts, successes


def pack_perm(p):
    value = 0
    for i, x in enumerate(p):
        value |= x << (3 * i)
    return value


def emit_vectors(path: Path):
    lines = [
        "# A B erase_attempt expected_status expected_orbit expected_attempts expected_successes"
    ]
    for state, (a, b) in enumerate(c.REPS):
        for erase_attempt in range(6):
            status, orbit, attempts, successes = simulate_state(
                state, erase_attempt
            )
            lines.append(
                f"{pack_perm(a):06x} {pack_perm(b):06x} {erase_attempt:x} "
                f"{status:x} {orbit:02x} {attempts:x} {successes:x}"
            )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def walk_worst(node_id=0, erased=False):
    node = nodes[node_id]
    word_len = len(node["word"])
    candidates = []
    for target in node["class_targets"]:
        kind, payload = target
        if kind == NODE_KIND:
            a, s, letters = walk_worst(payload, erased)
            candidates.append((1 + a, 1 + s, word_len + letters))
        elif kind in (ORBIT_KIND, REJECT_KIND):
            candidates.append((1, 1, word_len))

    if node["mode"] == "pre-erasure":
        kind, payload = node["erasure_target"]
        if kind == NODE_KIND:
            a, s, letters = walk_worst(payload, True)
            candidates.append((1 + a, s, word_len + letters))
        elif kind in (ORBIT_KIND, REJECT_KIND):
            candidates.append((1, 0, word_len))

    return tuple(max(row[i] for row in candidates) for i in range(3))


def emit_json(path: Path):
    pre = sum(node["mode"] == "pre-erasure" for node in nodes)
    post = len(nodes) - pre
    class_edges = sum(
        sum(t[0] != INVALID_KIND for t in node["class_targets"])
        for node in nodes
    )
    erase_edges = pre
    attempts, successes, letters = walk_worst(0)

    payload = {
        "strategy": {
            "controller_nodes": len(nodes),
            "pre_erasure_nodes": pre,
            "post_erasure_nodes": post,
            "class_edges": class_edges,
            "erase_edges": erase_edges,
            "used_words": USED_WORDS,
            "used_word_count": len(USED_WORDS),
            "max_word_length": max(map(len, USED_WORDS)),
            "worst_case_attempts": attempts,
            "worst_case_successful_answers": successes,
            "worst_case_letter_compositions": letters,
        },
        "comparison_proxy": {
            "H17_LAB03_fixed_probe_count": 8,
            "H17_LAB03_shared_DAG_compositions": 14,
            "H17_ROMfree_repair_internal_nodes": 306,
            "H18_adaptive_controller_nodes": len(nodes),
            "note": "Node counts are structural proxies, not FPGA LUT counts.",
        },
        "word_ids": WORD_ID,
        "nodes": nodes,
    }
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default="generated")
    args = ap.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    emit_word_rom(out / "h18_adaptive_word_rom.sv")
    emit_controller_rom(out / "h18_adaptive_controller_rom.sv")
    emit_vectors(out / "h18_adaptive_vectors.txt")
    emit_json(out / "h18_adaptive_controller.json")

    attempts, successes, letters = walk_worst(0)

    print("HATTER-SOL-18 H18-07 adaptive controller generator")
    print("controller nodes =", len(nodes))
    print("pre-erasure nodes = 69")
    print("post-erasure nodes = 239")
    print("distinct words used =", len(USED_WORDS))
    print("max word length =", max(map(len, USED_WORDS)))
    print("worst attempts =", attempts)
    print("worst successful answers =", successes)
    print("worst sequential letter-compositions =", letters)
    print("vectors =", len(c.REPS) * 6)
    print("PASS: controller ROM, word ROM, JSON and regression vectors emitted")


if __name__ == "__main__":
    main()
