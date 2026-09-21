#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
from collections import Counter
from functools import lru_cache
from pathlib import Path


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def is_squarefree(n: int) -> bool:
    if n < 1:
        return False
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


def omega_with_multiplicity(n: int) -> int:
    if n < 2:
        return 0
    count = 0
    d = 2
    x = n
    while d * d <= x:
        while x % d == 0:
            count += 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        count += 1
    return count


def is_semiprime(n: int) -> bool:
    return omega_with_multiplicity(n) == 2


def bit_order(width: int, name: str):
    if name == "MSB":
        return list(range(width - 1, -1, -1))
    if name == "LSB":
        return list(range(width))
    raise ValueError(name)


def deterministic_shuffle(values, seed: int):
    state = seed & ((1 << 64) - 1)

    def next_u64():
        nonlocal state
        state = (state + 0x9E3779B97F4A7C15) & ((1 << 64) - 1)
        z = state
        z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9 & ((1 << 64) - 1)
        z = (z ^ (z >> 27)) * 0x94D049BB133111EB & ((1 << 64) - 1)
        return (z ^ (z >> 31)) & ((1 << 64) - 1)

    for i in range(len(values) - 1, 0, -1):
        j = next_u64() % (i + 1)
        values[i], values[j] = values[j], values[i]


def build_truth(width: int, family: str, seed: int = 0):
    n = 1 << width

    if family == "prime":
        return [1 if is_prime(x) else 0 for x in range(n)]
    if family == "odd":
        return [x & 1 for x in range(n)]
    if family == "squarefree":
        return [1 if is_squarefree(x) else 0 for x in range(n)]
    if family == "semiprime":
        return [1 if is_semiprime(x) else 0 for x in range(n)]

    prime = [1 if is_prime(x) else 0 for x in range(n)]
    k = sum(prime)

    if family == "random_density":
        idx = list(range(n))
        deterministic_shuffle(idx, seed + 1000003 * width)
        ones = set(idx[:k])
        return [1 if i in ones else 0 for i in range(n)]

    if family == "shuffled_prime":
        values = prime[:]
        deterministic_shuffle(values, seed + 1000003 * width + 7919)
        return values

    raise ValueError(family)


def quotient_profile(values, width: int, order_name: str):
    order = bit_order(width, order_name)
    memo = {}
    next_id = 2

    @lru_cache(maxsize=None)
    def residual(level: int, assigned_value: int):
        nonlocal next_id

        if level == width:
            return values[assigned_value]

        bit = order[level]
        low = residual(level + 1, assigned_value & ~(1 << bit))
        high = residual(level + 1, assigned_value | (1 << bit))

        if low == high:
            return low

        key = (level, low, high)
        if key not in memo:
            memo[key] = next_id
            next_id += 1
        return memo[key]

    levels = []
    for depth in range(width + 1):
        ids = []
        for prefix in range(1 << depth):
            value = 0
            for j in range(depth):
                bit = order[j]
                digit = (prefix >> (depth - 1 - j)) & 1
                if digit:
                    value |= 1 << bit
            ids.append(residual(depth, value))

        class_counts = Counter(ids)
        multiplicities = sorted(class_counts.values(), reverse=True)
        total = len(ids)
        entropy = 0.0
        for m in multiplicities:
            q = m / total
            entropy -= q * math.log2(q)

        levels.append(
            {
                "depth": depth,
                "prefixes": total,
                "classes": len(class_counts),
                "largest_class": multiplicities[0],
                "singleton_classes": sum(1 for x in multiplicities if x == 1),
                "entropy_bits": entropy,
            }
        )

    root = residual(0, 0)
    serial = json.dumps(
        {
            "order": order_name,
            "width": width,
            "levels": levels,
            "nodes": sorted((k[0], k[1], k[2], v) for k, v in memo.items()),
        },
        sort_keys=True,
        separators=(",", ":"),
    )

    return {
        "root_id": root,
        "nonterminal_nodes": len(memo),
        "total_nodes_including_terminals": len(memo) + 2,
        "peak_classes": max(x["classes"] for x in levels),
        "peak_depth": max(levels, key=lambda x: x["classes"])["depth"],
        "profile_hash": hashlib.sha256(serial.encode()).hexdigest(),
        "levels": levels,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default="out")
    ap.add_argument("--widths", nargs="+", type=int, default=list(range(4, 17)))
    ap.add_argument("--seeds", nargs="+", type=int, default=[1729, 271828, 314159])
    args = ap.parse_args()

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    records = []
    for width in args.widths:
        for family in ["prime", "odd", "squarefree", "semiprime"]:
            values = build_truth(width, family)
            for order in ["MSB", "LSB"]:
                q = quotient_profile(values, width, order)
                records.append(
                    {
                        "width": width,
                        "family": family,
                        "seed": None,
                        "ones": sum(values),
                        "density": sum(values) / len(values),
                        "order": order,
                        **q,
                    }
                )

        for family in ["random_density", "shuffled_prime"]:
            for seed in args.seeds:
                values = build_truth(width, family, seed)
                for order in ["MSB", "LSB"]:
                    q = quotient_profile(values, width, order)
                    records.append(
                        {
                            "width": width,
                            "family": family,
                            "seed": seed,
                            "ones": sum(values),
                            "density": sum(values) / len(values),
                            "order": order,
                            **q,
                        }
                    )

        print(f"done W={width}")

    compact = []
    for r in records:
        compact.append(
            {
                "width": r["width"],
                "family": r["family"],
                "seed": r["seed"],
                "ones": r["ones"],
                "density": r["density"],
                "order": r["order"],
                "nonterminal_nodes": r["nonterminal_nodes"],
                "peak_classes": r["peak_classes"],
                "peak_depth": r["peak_depth"],
                "profile_hash": r["profile_hash"],
                "classes_by_depth": [x["classes"] for x in r["levels"]],
                "largest_class_by_depth": [x["largest_class"] for x in r["levels"]],
                "singletons_by_depth": [x["singleton_classes"] for x in r["levels"]],
            }
        )

    with (out / "continuation_quotient.json").open("w", encoding="utf-8") as f:
        json.dump(compact, f, indent=2, sort_keys=True)

    csv_rows = []
    for r in compact:
        row = dict(r)
        for key in ["classes_by_depth", "largest_class_by_depth", "singletons_by_depth"]:
            row[key] = ";".join(str(x) for x in row[key])
        csv_rows.append(row)

    with (out / "continuation_quotient.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys()))
        writer.writeheader()
        writer.writerows(csv_rows)

    def get(width, family, order, seed=None):
        return next(
            r for r in records
            if r["width"] == width
            and r["family"] == family
            and r["order"] == order
            and r["seed"] == seed
        )

    lines = [
        "# H20-EXT-LAB-01 · Exact continuation quotient census",
        "",
        "Status: **FIRST CPU EXPERIMENT COMPLETE / NO CONJECTURE FITTING IN THIS REPORT**",
        "",
        "## Prime predicate",
        "",
        "| W | order | ones | nonterminal quotient nodes | peak classes | peak depth |",
        "|---:|---|---:|---:|---:|---:|",
    ]

    for width in args.widths:
        for order in ["MSB", "LSB"]:
            r = get(width, "prime", order)
            lines.append(
                f"| {width} | {order} | {r['ones']} | "
                f"{r['nonterminal_nodes']} | {r['peak_classes']} | {r['peak_depth']} |"
            )

    lines += [
        "",
        "## Baseline screen",
        "",
        "| W | order | prime | odd | squarefree | semiprime | random-density mean | shuffled-prime mean |",
        "|---:|---|---:|---:|---:|---:|---:|---:|",
    ]

    for width in args.widths:
        for order in ["MSB", "LSB"]:
            prime = get(width, "prime", order)["nonterminal_nodes"]
            odd = get(width, "odd", order)["nonterminal_nodes"]
            squarefree = get(width, "squarefree", order)["nonterminal_nodes"]
            semiprime = get(width, "semiprime", order)["nonterminal_nodes"]
            rd = [
                r["nonterminal_nodes"] for r in records
                if r["width"] == width
                and r["family"] == "random_density"
                and r["order"] == order
            ]
            sh = [
                r["nonterminal_nodes"] for r in records
                if r["width"] == width
                and r["family"] == "shuffled_prime"
                and r["order"] == order
            ]
            lines.append(
                f"| {width} | {order} | {prime} | {odd} | {squarefree} | {semiprime} | "
                f"{statistics.mean(rd):.2f} | {statistics.mean(sh):.2f} |"
            )

    lines += [
        "",
        "## Observation",
        "",
        "The exact quotient census is recorded before any recurrence or asymptotic law is fitted.",
        "",
        "## Exact finite statement",
        "",
        f"All declared predicates, fixed seeds and both bit orders were evaluated exhaustively for W={min(args.widths)}..{max(args.widths)}.",
        "",
        "## Interpretation",
        "",
        "Any candidate law must be frozen on the discovery subset before being tested on a fresh validation layer.",
        "",
        "## Non-claim",
        "",
        "No asymptotic law, circuit lower bound, novelty claim, prime-distribution theorem, or RH connection is asserted.",
    ]

    (out / "H20_EXT_LAB01_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
