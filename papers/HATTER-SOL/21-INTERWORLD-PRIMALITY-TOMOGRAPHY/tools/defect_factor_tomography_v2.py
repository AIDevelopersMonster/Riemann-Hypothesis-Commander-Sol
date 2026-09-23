#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
from collections import Counter
from pathlib import Path

WORLDS = [
    {"name": "D-7", "B": 1, "C": -2},
    {"name": "D+5", "B": 1, "C": 1},
    {"name": "D-3", "B": 1, "C": -1},
    {"name": "D-11", "B": 1, "C": -3},
    {"name": "D+13", "B": 1, "C": 3},
    {"name": "D-19", "B": 1, "C": -5},
]


def jacobi(a: int, n: int) -> int:
    if n <= 0 or n % 2 == 0:
        raise ValueError
    a %= n
    out = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                out = -out
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            out = -out
        a %= n
    return out if n == 1 else 0


def mul(u, v, n: int, B: int, C: int):
    a, b = u
    c, d = v
    return (
        (a * c + b * d * C) % n,
        (a * d + b * c + b * d * B) % n,
    )


def pow_x(n: int, B: int, C: int):
    e = n
    acc = (1, 0)
    base = (0, 1)
    while e:
        if e & 1:
            acc = mul(acc, base, n, B, C)
        base = mul(base, base, n, B, C)
        e >>= 1
    return acc


def proper(n: int, x: int) -> bool:
    return 1 < x < n and n % x == 0


def world_witnesses(n: int, B: int, C: int):
    D = B * B + 4 * C
    out = set()

    g = math.gcd(n, abs(2 * C * D))
    if proper(n, g):
        out.add(g)
        return out
    if g == n:
        return out

    j = jacobi(D, n)
    if j == 0:
        gd = math.gcd(n, abs(D))
        if proper(n, gd):
            out.add(gd)
        return out

    got = pow_x(n, B, C)
    want = (0, 1) if j == 1 else (B % n, (-1) % n)
    d0 = (got[0] - want[0]) % n
    d1 = (got[1] - want[1]) % n

    for q in (math.gcd(n, d0), math.gcd(n, d1), math.gcd(n, d0, d1)):
        if proper(n, q):
            out.add(q)
    return out


def spf_sieve(limit: int):
    spf = list(range(limit))
    if limit > 1:
        spf[1] = 1
    for p in range(2, int(limit ** 0.5) + 1):
        if spf[p] == p:
            for x in range(p * p, limit, p):
                if spf[x] == x:
                    spf[x] = p
    return spf


def factorization(n: int, spf):
    fs = []
    x = n
    while x > 1:
        p = spf[x]
        fs.append(p)
        x //= p
    return fs


def shape(fs):
    if len(fs) == 1:
        return "prime"
    if len(fs) == 2:
        return "prime_square" if fs[0] == fs[1] else "semiprime_distinct"
    if len(set(fs)) == 1:
        return "higher_prime_power"
    return "other_composite"


def divisor_prime_support(d: int, spf):
    return set(factorization(d, spf))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, default=19)
    ap.add_argument("--out-dir", default="lab05_v2_out")
    args = ap.parse_args()

    limit = 1 << args.bits
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    spf = spf_sieve(limit)

    mask_counts = Counter()
    shape_counts = Counter()
    shape_hit_counts = Counter()
    shape_full_counts = Counter()
    per_world_hits = [0] * len(WORLDS)
    prime_witness_failures = []

    composites = 0
    any_factor = 0
    multi_divisor_values = 0
    multi_prime_support = 0
    full_support = 0

    frozen_new = [0] * len(WORLDS)
    frozen_seen_masks = 0
    examples = []

    for n in range(3, limit, 2):
        fs = factorization(n, spf)
        sh = shape(fs)

        world_sets = []
        all_divs = set()
        mask = 0

        for wi, w in enumerate(WORLDS):
            ws = world_witnesses(n, w["B"], w["C"])
            world_sets.append(ws)
            if ws:
                mask |= 1 << wi
                if sh != "prime":
                    per_world_hits[wi] += 1
            all_divs |= ws

        if sh == "prime":
            if all_divs:
                prime_witness_failures.append({
                    "n": n,
                    "witnesses": sorted(all_divs),
                })
            continue

        composites += 1
        shape_counts[sh] += 1
        mask_counts[mask] += 1

        if mask:
            any_factor += 1
            shape_hit_counts[sh] += 1

        if len(all_divs) >= 2:
            multi_divisor_values += 1

        actual_support = set(fs)
        exposed_support = set()
        for d in all_divs:
            exposed_support |= divisor_prime_support(d, spf)

        if len(exposed_support) >= 2:
            multi_prime_support += 1
        if exposed_support >= actual_support:
            full_support += 1
            shape_full_counts[sh] += 1

        if len(examples) < 20 and (len(all_divs) >= 2 or len(exposed_support) >= 2):
            examples.append({
                "n": n,
                "shape": sh,
                "factors": fs,
                "world_witnesses": [sorted(x) for x in world_sets],
                "exposed_support": sorted(exposed_support),
            })

    # Frozen-order marginal yield from mask frequencies only.
    remaining = Counter(mask_counts)
    unresolved = composites
    frozen_rows = []
    for step, wi in enumerate(range(len(WORLDS)), 1):
        newly = sum(c for m, c in remaining.items() if m & (1 << wi))
        frozen_rows.append({
            "step": step,
            "world": WORLDS[wi]["name"],
            "new_factor_hits": newly,
            "remaining_without_factor": unresolved - newly,
        })
        unresolved -= newly
        remaining = Counter({m: c for m, c in remaining.items() if not (m & (1 << wi))})

    # Exact 6! optimization through 64 mask frequencies.
    unresolved_penalty = len(WORLDS) + 1
    hit_total = composites - mask_counts[0]
    orders = []

    for perm in itertools.permutations(range(len(WORLDS))):
        pos = [0] * len(WORLDS)
        for k, wi in enumerate(perm, 1):
            pos[wi] = k

        all_cost = mask_counts[0] * unresolved_penalty
        hit_cost = 0

        for mask, count in mask_counts.items():
            if mask == 0:
                continue
            first = min(pos[wi] for wi in range(len(WORLDS)) if mask & (1 << wi))
            all_cost += count * first
            hit_cost += count * first

        orders.append({
            "order": " -> ".join(WORLDS[i]["name"] for i in perm),
            "mean_cost_all_composites": all_cost / composites,
            "mean_first_factor_given_hit": hit_cost / hit_total,
        })

    orders.sort(key=lambda r: (
        r["mean_cost_all_composites"],
        r["mean_first_factor_given_hit"],
        r["order"],
    ))
    best = orders[0]
    worst = orders[-1]

    world_rows = []
    for wi, w in enumerate(WORLDS):
        world_rows.append({
            "world": w["name"],
            "factor_hits": per_world_hits[wi],
            "hit_fraction": per_world_hits[wi] / composites,
        })

    shape_rows = []
    for sh in ["prime_square", "semiprime_distinct", "higher_prime_power", "other_composite"]:
        c = shape_counts[sh]
        shape_rows.append({
            "shape": sh,
            "count": c,
            "any_factor": shape_hit_counts[sh],
            "any_factor_fraction": shape_hit_counts[sh] / c if c else 0.0,
            "full_support": shape_full_counts[sh],
            "full_support_fraction": shape_full_counts[sh] / c if c else 0.0,
        })

    with (out / "mask_counts.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(["mask", "count"])
        for m in sorted(mask_counts):
            wr.writerow([m, mask_counts[m]])

    with (out / "world_yield.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(world_rows[0].keys()))
        wr.writeheader()
        wr.writerows(world_rows)

    with (out / "shape_coverage.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(shape_rows[0].keys()))
        wr.writeheader()
        wr.writerows(shape_rows)

    with (out / "order_optimization.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(orders[0].keys()))
        wr.writeheader()
        wr.writerows(orders)

    payload = {
        "bits": args.bits,
        "limit": limit,
        "composites": composites,
        "prime_witness_failures": prime_witness_failures,
        "any_factor": any_factor,
        "any_factor_fraction": any_factor / composites,
        "multiple_distinct_divisor_values": multi_divisor_values,
        "multiple_prime_support": multi_prime_support,
        "full_prime_support": full_support,
        "unresolved": mask_counts[0],
        "mask_counts": dict(mask_counts),
        "world_rows": world_rows,
        "shape_rows": shape_rows,
        "frozen_rows": frozen_rows,
        "best_order": best,
        "worst_order": worst,
        "top10_orders": orders[:10],
        "examples": examples,
    }
    (out / "defect_factor_tomography.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )

    md = [
        "# H21-LAB-05 v2 · Defect-surface factor tomography",
        "",
        f"Range: odd n with 3 <= n < 2^{args.bits}.",
        "",
        f"Composite inputs: **{composites}**.",
        "",
        f"Prime witness failures: **{len(prime_witness_failures)}**.",
        "",
        f"At least one proper divisor exposed: **{any_factor}/{composites} = {any_factor/composites:.6%}**.",
        "",
        f"Unresolved by all six worlds: **{mask_counts[0]}**.",
        "",
        f"At least two distinct divisor values exposed: **{multi_divisor_values}**.",
        "",
        f"At least two distinct prime factors represented: **{multi_prime_support}**.",
        "",
        f"Full distinct-prime support recovered: **{full_support}**.",
        "",
        "## Per world",
        "",
        "| world | factor hits | fraction |",
        "|---|---:|---:|",
    ]
    for r in world_rows:
        md.append(f"| {r['world']} | {r['factor_hits']} | {r['hit_fraction']:.6%} |")

    md += [
        "",
        "## By factor shape",
        "",
        "| shape | count | any factor | fraction | full support |",
        "|---|---:|---:|---:|---:|",
    ]
    for r in shape_rows:
        md.append(
            f"| {r['shape']} | {r['count']} | {r['any_factor']} | "
            f"{r['any_factor_fraction']:.6%} | {r['full_support']} |"
        )

    md += [
        "",
        "## Frozen order",
        "",
        "| step | world | new hits | remaining without factor |",
        "|---:|---|---:|---:|",
    ]
    for r in frozen_rows:
        md.append(
            f"| {r['step']} | {r['world']} | {r['new_factor_hits']} | "
            f"{r['remaining_without_factor']} |"
        )

    md += [
        "",
        "## Exact 720-order optimization",
        "",
        f"Best: **{best['order']}**.",
        "",
        f"Best mean cost over all composites: **{best['mean_cost_all_composites']:.6f}**.",
        "",
        f"Best mean first-factor handle given a hit: **{best['mean_first_factor_given_hit']:.6f}**.",
        "",
        f"Worst: **{worst['order']}**.",
        "",
        f"Worst mean cost over all composites: **{worst['mean_cost_all_composites']:.6f}**.",
        "",
        "## Non-claim",
        "",
        "This is exact only for the declared six-world family and finite range.",
    ]

    (out / "H21_LAB05_V2_REPORT.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))
    print("PASS: H21-LAB-05 v2 completed")

    if prime_witness_failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
