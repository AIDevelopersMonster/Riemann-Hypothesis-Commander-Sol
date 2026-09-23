#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
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

MASK_NAMES = {
    0: "{}",
    1: "{0}",
    2: "{1}",
    3: "{0,1}",
}


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


def pow_elem(base, e: int, n: int, B: int, C: int):
    acc = (1, 0)
    cur = base
    while e:
        if e & 1:
            acc = mul(acc, cur, n, B, C)
        cur = mul(cur, cur, n, B, C)
        e >>= 1
    return acc


def pow_x(e: int, n: int, B: int, C: int):
    return pow_elem((0, 1), e, n, B, C)


def tau(v, n: int, B: int):
    a, b = v
    return ((a + B * b) % n, (-b) % n)


def expected_x(sign: int, n: int, B: int):
    return (0, 1) if sign == 1 else (B % n, (-1) % n)


def sub(u, v, n: int):
    return ((u[0] - v[0]) % n, (u[1] - v[1]) % n)


def zero_mask(v, r: int):
    mask = 0
    if v[0] % r == 0:
        mask |= 1
    if v[1] % r == 0:
        mask |= 2
    return mask


def proper(n: int, d: int):
    return 1 < d < n and n % d == 0


def primes_upto(limit: int):
    is_prime = bytearray(b"\x01") * limit
    if limit > 0:
        is_prime[0] = 0
    if limit > 1:
        is_prime[1] = 0
    for p in range(2, int(limit ** 0.5) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start:limit:p] = b"\x00" * (((limit - 1 - start)//p)+1)
    return [p for p in range(3, limit, 2) if is_prime[p]], is_prime


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, default=19)
    ap.add_argument("--out-dir", default="lab06_out")
    args = ap.parse_args()

    limit = 1 << args.bits
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    plist, is_prime = primes_upto(limit)

    semiprimes = []
    for i, p in enumerate(plist):
        if p * p >= limit:
            break
        for q in plist[i+1:]:
            n = p * q
            if n >= limit:
                break
            semiprimes.append((p, q, n))

    theorem_mismatches = []
    cross_formula_mismatches = []
    per_world_exposed = [set() for _ in WORLDS]
    mask_pair_counts = [Counter() for _ in WORLDS]
    exposure_type_counts = [Counter() for _ in WORLDS]
    eligible_per_world = [0] * len(WORLDS)

    for p, q, n in semiprimes:
        for wi, w in enumerate(WORLDS):
            B, C = w["B"], w["C"]
            D = B * B + 4 * C

            if math.gcd(n, abs(2 * C * D)) != 1:
                continue

            cp = jacobi(D, p)
            cq = jacobi(D, q)
            if cp not in (-1, 1) or cq not in (-1, 1):
                continue

            eligible_per_world[wi] += 1

            # Global defect modulo n.
            got_n = pow_x(n, n, B, C)
            cn = cp * cq
            want_n = expected_x(cn, n, B)
            defect_n = sub(got_n, want_n, n)

            dp = (defect_n[0] % p, defect_n[1] % p)
            dq = (defect_n[0] % q, defect_n[1] % q)

            # Cross-Frobenius formula modulo p.
            xq_p = pow_x(q, p, B, C)
            target_q_in_p = expected_x(cq, p, B)
            rp = sub(xq_p, target_q_in_p, p)
            if cp == -1:
                rp = tau(rp, p, B)

            # Cross-Frobenius formula modulo q.
            xp_q = pow_x(p, q, B, C)
            target_p_in_q = expected_x(cp, q, B)
            rq = sub(xp_q, target_p_in_q, q)
            if cq == -1:
                rq = tau(rq, q, B)

            if rp != dp or rq != dq:
                cross_formula_mismatches.append({
                    "n": n, "p": p, "q": q, "world": w["name"],
                    "dp": dp, "rp": rp, "dq": dq, "rq": rq,
                })

            zp = zero_mask(dp, p)
            zq = zero_mask(dq, q)
            mask_pair_counts[wi][(zp, zq)] += 1

            g0 = math.gcd(n, defect_n[0])
            g1 = math.gcd(n, defect_n[1])
            actual = set()
            if proper(n, g0):
                actual.add(g0)
            if proper(n, g1):
                actual.add(g1)

            predicted = set()
            if (zp & 1) and not (zq & 1):
                predicted.add(p)
            if (zq & 1) and not (zp & 1):
                predicted.add(q)
            if (zp & 2) and not (zq & 2):
                predicted.add(p)
            if (zq & 2) and not (zp & 2):
                predicted.add(q)

            if actual != predicted or (bool(actual) != (zp != zq)):
                theorem_mismatches.append({
                    "n": n, "p": p, "q": q, "world": w["name"],
                    "zp": zp, "zq": zq,
                    "actual": sorted(actual),
                    "predicted": sorted(predicted),
                    "defect": defect_n,
                })

            if actual:
                per_world_exposed[wi].add(n)
                if actual == {p, q}:
                    exposure_type_counts[wi]["both"] += 1
                elif actual == {p}:
                    exposure_type_counts[wi]["p_only"] += 1
                elif actual == {q}:
                    exposure_type_counts[wi]["q_only"] += 1

    # 6x6 complementarity matrix on all distinct semiprimes, including
    # exceptional cases only insofar as the coordinate-defect observer exposes them.
    # Here theorem-lab exposure sets contain nonexceptional observations only.
    pair_rows = []
    for i, wi in enumerate(WORLDS):
        for j, wj in enumerate(WORLDS):
            Ei = per_world_exposed[i]
            Ej = per_world_exposed[j]
            pair_rows.append({
                "world_i": wi["name"],
                "world_j": wj["name"],
                "hit_i": len(Ei),
                "hit_j": len(Ej),
                "union": len(Ei | Ej),
                "gain_j_after_i": len(Ej - Ei),
                "intersection": len(Ei & Ej),
            })

    mask_rows = []
    for wi, w in enumerate(WORLDS):
        for (zp, zq), count in sorted(mask_pair_counts[wi].items()):
            mask_rows.append({
                "world": w["name"],
                "zp": MASK_NAMES[zp],
                "zq": MASK_NAMES[zq],
                "count": count,
                "exposes_factor": int(zp != zq),
            })

    world_rows = []
    for wi, w in enumerate(WORLDS):
        world_rows.append({
            "world": w["name"],
            "eligible_semiprimes": eligible_per_world[wi],
            "exposed_semiprimes": len(per_world_exposed[wi]),
            "fraction": len(per_world_exposed[wi]) / eligible_per_world[wi] if eligible_per_world[wi] else 0.0,
            "p_only": exposure_type_counts[wi]["p_only"],
            "q_only": exposure_type_counts[wi]["q_only"],
            "both": exposure_type_counts[wi]["both"],
        })

    with (out / "mask_pair_counts.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(mask_rows[0].keys()))
        wr.writeheader()
        wr.writerows(mask_rows)

    with (out / "world_semiprime_exposure.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(world_rows[0].keys()))
        wr.writeheader()
        wr.writerows(world_rows)

    with (out / "pair_complementarity.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(pair_rows[0].keys()))
        wr.writeheader()
        wr.writerows(pair_rows)

    payload = {
        "bits": args.bits,
        "limit": limit,
        "distinct_semiprimes": len(semiprimes),
        "cross_formula_mismatches": cross_formula_mismatches[:20],
        "cross_formula_mismatch_count": len(cross_formula_mismatches),
        "theorem_mismatches": theorem_mismatches[:20],
        "theorem_mismatch_count": len(theorem_mismatches),
        "world_rows": world_rows,
        "top_pair_gains": sorted(
            [r for r in pair_rows if r["world_i"] != r["world_j"]],
            key=lambda r: (-r["gain_j_after_i"], r["world_i"], r["world_j"])
        )[:12],
    }
    (out / "semiprime_exposure_validation.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )

    md = [
        "# H21-LAB-06 · Semiprime defect-asymmetry validation",
        "",
        f"Range: distinct odd semiprimes n=pq < 2^{args.bits}.",
        "",
        f"Semiprimes: **{len(semiprimes)}**.",
        "",
        f"Cross-Frobenius formula mismatches: **{len(cross_formula_mismatches)}**.",
        "",
        f"Zero-mask theorem mismatches: **{len(theorem_mismatches)}**.",
        "",
        "## Per-world nonexceptional semiprime exposure",
        "",
        "| world | eligible | exposed | fraction | p only | q only | both |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for r in world_rows:
        md.append(
            f"| {r['world']} | {r['eligible_semiprimes']} | {r['exposed_semiprimes']} | "
            f"{r['fraction']:.6%} | {r['p_only']} | {r['q_only']} | {r['both']} |"
        )

    top_pairs = sorted(
        [r for r in pair_rows if r["world_i"] != r["world_j"]],
        key=lambda r: (-r["gain_j_after_i"], r["world_i"], r["world_j"])
    )[:10]

    md += [
        "",
        "## Largest ordered pair gains",
        "",
        "| first | second | first hits | union | new hits from second | intersection |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for r in top_pairs:
        md.append(
            f"| {r['world_i']} | {r['world_j']} | {r['hit_i']} | "
            f"{r['union']} | {r['gain_j_after_i']} | {r['intersection']} |"
        )

    md += [
        "",
        "## Exact conclusion",
        "",
        "The theorem is accepted for this finite validation iff both mismatch counts are zero.",
    ]

    (out / "H21_LAB06_REPORT.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))

    if cross_formula_mismatches or theorem_mismatches:
        raise SystemExit(2)

    print("PASS: H21-SD1 and cross-Frobenius identities validated")


if __name__ == "__main__":
    main()
