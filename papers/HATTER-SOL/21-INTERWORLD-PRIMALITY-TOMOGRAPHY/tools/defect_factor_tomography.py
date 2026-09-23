#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
from collections import Counter, defaultdict
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
        raise ValueError("jacobi requires positive odd n")
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


def proper(n: int, x: int):
    return 1 < x < n and n % x == 0


def world_factor_response(n: int, B: int, C: int):
    D = B * B + 4 * C
    witnesses = set()
    mode = "normal"

    pre = math.gcd(n, abs(2 * C * D))
    if proper(n, pre):
        witnesses.add(pre)
        mode = "precheck"
        return {
            "mode": mode,
            "jacobi": None,
            "defect": None,
            "witnesses": sorted(witnesses),
        }
    if pre == n:
        return {
            "mode": "exceptional",
            "jacobi": None,
            "defect": None,
            "witnesses": [],
        }

    j = jacobi(D, n)
    if j == 0:
        g = math.gcd(n, abs(D))
        if proper(n, g):
            witnesses.add(g)
        return {
            "mode": "jacobi-zero",
            "jacobi": 0,
            "defect": None,
            "witnesses": sorted(witnesses),
        }

    got = pow_x(n, B, C)
    want = (0, 1) if j == 1 else (B % n, (-1) % n)
    d0 = (got[0] - want[0]) % n
    d1 = (got[1] - want[1]) % n

    g0 = math.gcd(n, d0)
    g1 = math.gcd(n, d1)
    g01 = math.gcd(n, d0, d1)

    for g in (g0, g1, g01):
        if proper(n, g):
            witnesses.add(g)

    return {
        "mode": "pass" if (d0 == 0 and d1 == 0) else "defect",
        "jacobi": j,
        "defect": [d0, d1],
        "gcds": [g0, g1, g01],
        "witnesses": sorted(witnesses),
    }


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
    out = []
    x = n
    while x > 1:
        p = spf[x]
        out.append(p)
        x //= p
    return out


def factor_shape(fs):
    if len(fs) == 1:
        return "prime"
    if len(fs) == 2:
        return "prime_square" if fs[0] == fs[1] else "semiprime_distinct"
    if len(set(fs)) == 1:
        return "higher_prime_power"
    return "other_composite"


def prime_support_of_divisor(d: int, spf):
    if d <= 1:
        return set()
    return set(factorization(d, spf))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, default=19)
    ap.add_argument("--out-dir", default="lab05_out")
    args = ap.parse_args()

    limit = 1 << args.bits
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    spf = spf_sieve(limit)

    records = []
    prime_witness_failures = []
    per_world_hits = [0] * len(WORLDS)
    per_world_shape = [Counter() for _ in WORLDS]

    for n in range(3, limit, 2):
        fs = factorization(n, spf)
        shape = factor_shape(fs)
        world_sets = []
        world_modes = []
        all_witness_values = set()

        for wi, w in enumerate(WORLDS):
            resp = world_factor_response(n, w["B"], w["C"])
            ws = set(resp["witnesses"])
            world_sets.append(ws)
            world_modes.append(resp["mode"])
            all_witness_values |= ws

            if shape == "prime" and ws:
                prime_witness_failures.append({
                    "n": n,
                    "world": w["name"],
                    "witnesses": sorted(ws),
                })

            if shape != "prime" and ws:
                per_world_hits[wi] += 1
                per_world_shape[wi][shape] += 1

        if shape == "prime":
            continue

        actual_support = set(fs)
        exposed_support = set()
        for d in all_witness_values:
            exposed_support |= prime_support_of_divisor(d, spf)

        mask = 0
        for wi, ws in enumerate(world_sets):
            if ws:
                mask |= 1 << wi

        records.append({
            "n": n,
            "shape": shape,
            "factors": fs,
            "actual_support": sorted(actual_support),
            "world_sets": [sorted(x) for x in world_sets],
            "world_mask": mask,
            "distinct_witnesses": sorted(all_witness_values),
            "exposed_support": sorted(exposed_support),
            "full_support_recovered": exposed_support >= actual_support,
        })

    composites = len(records)
    hit_records = [r for r in records if r["world_mask"]]
    any_hit = len(hit_records)
    multiple_witness_values = sum(len(r["distinct_witnesses"]) >= 2 for r in records)
    multiple_prime_support = sum(len(r["exposed_support"]) >= 2 for r in records)
    full_support = sum(r["full_support_recovered"] for r in records)

    shape_rows = []
    shapes = [
        "prime_square",
        "semiprime_distinct",
        "higher_prime_power",
        "other_composite",
    ]
    for sh in shapes:
        rs = [r for r in records if r["shape"] == sh]
        hits = [r for r in rs if r["world_mask"]]
        full = [r for r in rs if r["full_support_recovered"]]
        multi = [r for r in rs if len(r["distinct_witnesses"]) >= 2]
        shape_rows.append({
            "shape": sh,
            "count": len(rs),
            "any_factor": len(hits),
            "any_factor_fraction": (len(hits) / len(rs)) if rs else 0.0,
            "multiple_divisor_values": len(multi),
            "full_prime_support_recovered": len(full),
            "full_support_fraction": (len(full) / len(rs)) if rs else 0.0,
        })

    # Frozen-order marginal yield.
    frozen_order = tuple(range(len(WORLDS)))
    frozen_marginal = []
    unresolved = set(range(composites))
    for pos, wi in enumerate(frozen_order, 1):
        newly = {ri for ri in unresolved if records[ri]["world_mask"] & (1 << wi)}
        frozen_marginal.append({
            "step": pos,
            "world": WORLDS[wi]["name"],
            "new_factor_hits": len(newly),
            "remaining_without_factor": len(unresolved) - len(newly),
        })
        unresolved -= newly

    # Exhaust all 6! static orders.
    order_rows = []
    unresolved_penalty = len(WORLDS) + 1

    masks = [r["world_mask"] for r in records]
    hit_masks = [m for m in masks if m]

    for perm in itertools.permutations(range(len(WORLDS))):
        pos = [0] * len(WORLDS)
        for k, wi in enumerate(perm, 1):
            pos[wi] = k

        all_cost = 0
        hit_cost = 0
        for m in masks:
            if not m:
                all_cost += unresolved_penalty
                continue
            first = min(pos[wi] for wi in range(len(WORLDS)) if m & (1 << wi))
            all_cost += first
            hit_cost += first

        order_rows.append({
            "order": " -> ".join(WORLDS[i]["name"] for i in perm),
            "mean_cost_all_composites": all_cost / composites,
            "mean_first_factor_given_hit": hit_cost / len(hit_masks),
        })

    order_rows.sort(key=lambda r: (
        r["mean_cost_all_composites"],
        r["mean_first_factor_given_hit"],
        r["order"],
    ))

    best = order_rows[0]
    worst = max(order_rows, key=lambda r: (
        r["mean_cost_all_composites"],
        r["mean_first_factor_given_hit"],
    ))

    world_rows = []
    for wi, w in enumerate(WORLDS):
        row = {
            "world": w["name"],
            "discriminant": w["B"] * w["B"] + 4 * w["C"],
            "factor_hits": per_world_hits[wi],
            "hit_fraction_all_composites": per_world_hits[wi] / composites,
        }
        for sh in shapes:
            row["hits_" + sh] = per_world_shape[wi][sh]
        world_rows.append(row)

    with (out / "shape_factor_coverage.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(shape_rows[0].keys()))
        wr.writeheader()
        wr.writerows(shape_rows)

    with (out / "world_factor_yield.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(world_rows[0].keys()))
        wr.writeheader()
        wr.writerows(world_rows)

    with (out / "order_optimization.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(order_rows[0].keys()))
        wr.writeheader()
        wr.writerows(order_rows)

    payload = {
        "bits": args.bits,
        "limit": limit,
        "worlds": WORLDS,
        "prime_witness_failures": prime_witness_failures,
        "composites": composites,
        "any_factor": any_hit,
        "any_factor_fraction": any_hit / composites,
        "multiple_distinct_divisor_values": multiple_witness_values,
        "multiple_prime_support_exposed": multiple_prime_support,
        "full_prime_support_recovered": full_support,
        "shape_rows": shape_rows,
        "world_rows": world_rows,
        "frozen_marginal": frozen_marginal,
        "best_order": best,
        "worst_order": worst,
        "top10_orders": order_rows[:10],
    }

    # Keep compact examples only.
    examples_multiworld = []
    examples_multifactor = []
    for r in records:
        if len(examples_multiworld) < 12 and bin(r["world_mask"]).count("1") >= 2:
            examples_multiworld.append({
                "n": r["n"],
                "shape": r["shape"],
                "factors": r["factors"],
                "world_sets": r["world_sets"],
            })
        if len(examples_multifactor) < 12 and len(r["exposed_support"]) >= 2:
            examples_multifactor.append({
                "n": r["n"],
                "shape": r["shape"],
                "factors": r["factors"],
                "exposed_support": r["exposed_support"],
                "world_sets": r["world_sets"],
            })

    payload["examples_multiworld"] = examples_multiworld
    payload["examples_multifactor"] = examples_multifactor

    (out / "defect_factor_tomography.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )

    md = [
        "# H21-LAB-05 · Defect-surface factor tomography",
        "",
        f"Range: odd n with 3 <= n < 2^{args.bits}.",
        "",
        f"Composite inputs: **{composites}**.",
        "",
        f"Prime proper-divisor witness failures: **{len(prime_witness_failures)}**.",
        "",
        "## Global factor exposure",
        "",
        f"At least one proper divisor exposed: **{any_hit} / {composites} = {any_hit/composites:.6%}**.",
        "",
        f"At least two distinct proper-divisor values: **{multiple_witness_values}**.",
        "",
        f"At least two distinct prime divisors represented in witnesses: **{multiple_prime_support}**.",
        "",
        f"Full distinct-prime support recovered from the six handles: **{full_support}**.",
        "",
        "## By factor shape",
        "",
        "| shape | count | any factor | fraction | >=2 divisor values | full prime support |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for r in shape_rows:
        md.append(
            f"| {r['shape']} | {r['count']} | {r['any_factor']} | "
            f"{r['any_factor_fraction']:.6%} | {r['multiple_divisor_values']} | "
            f"{r['full_prime_support_recovered']} |"
        )

    md += [
        "",
        "## Per-world factor yield",
        "",
        "| world | factor hits | fraction of composites |",
        "|---|---:|---:|",
    ]
    for r in world_rows:
        md.append(
            f"| {r['world']} | {r['factor_hits']} | "
            f"{r['hit_fraction_all_composites']:.6%} |"
        )

    md += [
        "",
        "## Frozen-order marginal yield",
        "",
        "| step | world | new factor hits | remaining without factor |",
        "|---:|---|---:|---:|",
    ]
    for r in frozen_marginal:
        md.append(
            f"| {r['step']} | {r['world']} | {r['new_factor_hits']} | "
            f"{r['remaining_without_factor']} |"
        )

    md += [
        "",
        "## Exact 6! static-order optimization",
        "",
        f"Best order: **{best['order']}**.",
        "",
        f"Mean world evaluations over all composites (unresolved penalty 7): "
        f"**{best['mean_cost_all_composites']:.6f}**.",
        "",
        f"Mean first-factor handle among factorable composites: "
        f"**{best['mean_first_factor_given_hit']:.6f}**.",
        "",
        f"Worst order: **{worst['order']}**.",
        "",
        f"Worst mean all-composite cost: **{worst['mean_cost_all_composites']:.6f}**.",
        "",
        "## Claim boundary",
        "",
        "This is an exact finite optimization over the frozen six-world family and finite input range. "
        "It is not a general factorization theorem.",
    ]

    (out / "H21_LAB05_REPORT.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))
    print("PASS: H21-LAB-05 completed")

    if prime_witness_failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
