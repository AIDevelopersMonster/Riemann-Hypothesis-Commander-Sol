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

SEEDS = [1729, 271828, 314159, 1618033, 5772157]
WHEELS = [2, 6, 30, 210]


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
    d = 2
    while d * d <= n:
        if n % (d * d) == 0:
            return False
        d += 1
    return True


def omega(n: int) -> int:
    if n < 2:
        return 0
    x = n
    out = 0
    d = 2
    while d * d <= x:
        while x % d == 0:
            out += 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        out += 1
    return out


def is_semiprime(n: int) -> bool:
    return omega(n) == 2


def deterministic_shuffle(a, seed: int):
    state = seed & ((1 << 64) - 1)

    def next_u64():
        nonlocal state
        state = (state + 0x9E3779B97F4A7C15) & ((1 << 64) - 1)
        z = state
        z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9 & ((1 << 64) - 1)
        z = (z ^ (z >> 27)) * 0x94D049BB133111EB & ((1 << 64) - 1)
        return (z ^ (z >> 31)) & ((1 << 64) - 1)

    for i in range(len(a) - 1, 0, -1):
        j = next_u64() % (i + 1)
        a[i], a[j] = a[j], a[i]


def admissible_residues(m: int):
    return [r for r in range(m) if math.gcd(r, m) == 1]


def values_for(width: int, modulus: int, residue: int, family: str, seed: int | None = None):
    limit = 1 << width
    xs = list(range(residue, limit, modulus))

    if family == "prime":
        vals = [1 if is_prime(x) else 0 for x in xs]
    elif family == "squarefree":
        vals = [1 if is_squarefree(x) else 0 for x in xs]
    elif family == "semiprime":
        vals = [1 if is_semiprime(x) else 0 for x in xs]
    elif family in ("random_fixed", "shuffled_prime"):
        vals = [1 if is_prime(x) else 0 for x in xs]
        if family == "random_fixed":
            idx = list(range(len(vals)))
            deterministic_shuffle(idx, (seed or 0) + 1000003 * width + 1009 * modulus + 17 * residue)
            k = sum(vals)
            ones = set(idx[:k])
            vals = [1 if i in ones else 0 for i in range(len(vals))]
        else:
            deterministic_shuffle(vals, (seed or 0) + 2000003 * width + 2003 * modulus + 19 * residue)
    else:
        raise ValueError(family)

    return vals


def bit_order(depth: int, name: str):
    return list(range(depth - 1, -1, -1)) if name == "MSB" else list(range(depth))


def quotient(values, order_name: str):
    n = len(values)
    depth = max(1, math.ceil(math.log2(max(1, n))))
    order = bit_order(depth, order_name)
    terminals = {0: 0, 1: 1, "PAD": 2}
    memo = {}
    next_id = 3

    @lru_cache(maxsize=None)
    def residual(level: int, assigned: int):
        nonlocal next_id
        if level == depth:
            if assigned >= n:
                return terminals["PAD"]
            return terminals[values[assigned]]

        b = order[level]
        low = residual(level + 1, assigned & ~(1 << b))
        high = residual(level + 1, assigned | (1 << b))
        if low == high:
            return low
        key = (level, low, high)
        if key not in memo:
            memo[key] = next_id
            next_id += 1
        return memo[key]

    levels = []
    for d in range(depth + 1):
        ids = []
        for p in range(1 << d):
            assigned = 0
            for j in range(d):
                b = order[j]
                digit = (p >> (d - 1 - j)) & 1
                if digit:
                    assigned |= 1 << b
            ids.append(residual(d, assigned))
        c = Counter(ids)
        levels.append((d, len(c)))

    serial = json.dumps(
        {
            "n": n,
            "depth": depth,
            "order": order_name,
            "nodes": sorted((k[0], k[1], k[2], v) for k, v in memo.items()),
        },
        separators=(",", ":"),
    )
    return {
        "nodes": len(memo),
        "peak_classes": max(x[1] for x in levels),
        "peak_depth": max(levels, key=lambda x: x[1])[0],
        "hash": hashlib.sha256(serial.encode()).hexdigest(),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default="lab02_out")
    ap.add_argument("--widths", nargs="+", type=int, default=list(range(8, 17)))
    args = ap.parse_args()

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    rows = []

    for w in args.widths:
        for m in WHEELS:
            for r in admissible_residues(m):
                for family in ["prime", "squarefree", "semiprime"]:
                    vals = values_for(w, m, r, family)
                    for order in ["MSB", "LSB"]:
                        q = quotient(vals, order)
                        rows.append({
                            "width": w, "modulus": m, "residue": r,
                            "family": family, "seed": "",
                            "length": len(vals), "ones": sum(vals),
                            "order": order, **q,
                        })
                for family in ["random_fixed", "shuffled_prime"]:
                    for seed in SEEDS:
                        vals = values_for(w, m, r, family, seed)
                        for order in ["MSB", "LSB"]:
                            q = quotient(vals, order)
                            rows.append({
                                "width": w, "modulus": m, "residue": r,
                                "family": family, "seed": seed,
                                "length": len(vals), "ones": sum(vals),
                                "order": order, **q,
                            })
        print(f"done W={w}")

    csv_path = out / "wheel_conditioned_quotient.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        wr.writeheader()
        wr.writerows(rows)

    summary = []
    for w in args.widths:
        for m in WHEELS:
            for order in ["MSB", "LSB"]:
                prime = [x["nodes"] for x in rows if x["width"] == w and x["modulus"] == m and x["family"] == "prime" and x["order"] == order]
                rnd_by_seed = []
                sh_by_seed = []
                for seed in SEEDS:
                    rnd_by_seed.append(sum(x["nodes"] for x in rows if x["width"] == w and x["modulus"] == m and x["family"] == "random_fixed" and x["order"] == order and x["seed"] == seed))
                    sh_by_seed.append(sum(x["nodes"] for x in rows if x["width"] == w and x["modulus"] == m and x["family"] == "shuffled_prime" and x["order"] == order and x["seed"] == seed))
                prime_sum = sum(prime)
                entry = {
                    "width": w,
                    "modulus": m,
                    "order": order,
                    "residue_classes": len(admissible_residues(m)),
                    "prime_nodes_sum": prime_sum,
                    "random_mean": statistics.mean(rnd_by_seed),
                    "random_min": min(rnd_by_seed),
                    "random_max": max(rnd_by_seed),
                    "shuffled_mean": statistics.mean(sh_by_seed),
                    "shuffled_min": min(sh_by_seed),
                    "shuffled_max": max(sh_by_seed),
                    "rho_random": prime_sum / statistics.mean(rnd_by_seed) if statistics.mean(rnd_by_seed) else 0.0,
                    "rho_shuffled": prime_sum / statistics.mean(sh_by_seed) if statistics.mean(sh_by_seed) else 0.0,
                }
                summary.append(entry)

    (out / "wheel_conditioned_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    lines = [
        "# H20-EXT-LAB-02 · Wheel-conditioned continuation quotient",
        "",
        "Status: **COMPUTATION COMPLETE**",
        "",
        "| W | wheel | order | prime nodes | random mean | rho(random) | shuffled mean | rho(shuffled) |",
        "|---:|---:|---|---:|---:|---:|---:|---:|",
    ]
    for s in summary:
        lines.append(
            f"| {s['width']} | {s['modulus']} | {s['order']} | {s['prime_nodes_sum']} | "
            f"{s['random_mean']:.2f} | {s['rho_random']:.4f} | "
            f"{s['shuffled_mean']:.2f} | {s['rho_shuffled']:.4f} |"
        )
    lines += [
        "",
        "## Observation",
        "",
        "This report records the exact predeclared wheel-conditioned quotient statistics without fitting an asymptotic law.",
        "",
        "## Exact finite statement",
        "",
        f"The declared experiment was evaluated exhaustively for W={min(args.widths)}..{max(args.widths)}, wheels 2,6,30,210, every admissible residue class, both bit orders, and all fixed seeds.",
        "",
        "## Non-claim",
        "",
        "No asymptotic theorem, novelty claim, circuit lower bound, prime-distribution theorem, or RH implication is asserted by this computation alone.",
    ]
    (out / "H20_EXT_LAB02_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
