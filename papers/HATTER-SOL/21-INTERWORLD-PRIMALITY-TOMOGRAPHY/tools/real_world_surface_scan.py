#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
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

CERT_STATES = {"F+", "F-", "G"}


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


def world_state(n: int, B: int, C: int):
    D = B * B + 4 * C
    g = math.gcd(n, abs(2 * C * D))
    if g != 1:
        if 1 < g < n:
            return "G", g
        return "E", None

    j = jacobi(D, n)
    if j not in (-1, 1):
        return "G", math.gcd(D, n)

    got = pow_x(n, B, C)
    want = (0, 1) if j == 1 else (B % n, (-1) % n)
    ok = got == want
    if ok:
        return ("P+" if j == 1 else "P-"), None

    da = (got[0] - want[0]) % n
    db = (got[1] - want[1]) % n
    witness = math.gcd(n, da, db)
    if witness in (1, n):
        witness = None
    return ("F+" if j == 1 else "F-"), witness


def spf_sieve(limit: int):
    spf = list(range(limit))
    if limit > 1:
        spf[1] = 1
    for p in range(2, int(limit ** 0.5) + 1):
        if spf[p] == p:
            for n in range(p * p, limit, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def factor_shape(n: int, spf):
    if spf[n] == n:
        return "prime"

    fac = []
    x = n
    while x > 1:
        p = spf[x]
        fac.append(p)
        x //= p

    if len(fac) == 2:
        if fac[0] == fac[1]:
            return "prime_square"
        return "semiprime_distinct"

    if len(set(fac)) == 1:
        return "higher_prime_power"
    return "other_composite"


def first_certificate(sig):
    for i, state in enumerate(sig, 1):
        if state in CERT_STATES:
            return i
    return None


def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))


def onehot_second_sq(prev_sig, cur_sig, next_sig):
    total = 0
    for a, b, c in zip(prev_sig, cur_sig, next_sig):
        if a == b == c:
            contrib = 0
        elif a == c and a != b:
            contrib = 8
        elif a == b or b == c:
            contrib = 2
        else:
            contrib = 6
        total += contrib
    return total


def mean(xs):
    return (sum(xs) / len(xs)) if xs else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, default=19)
    ap.add_argument("--out-dir", default="lab03_out")
    args = ap.parse_args()

    limit = 1 << args.bits
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    spf = spf_sieve(limit)

    records = []
    prime_failures = []

    for n in range(3, limit, 2):
        shape = factor_shape(n, spf)
        states = []
        witnesses = []
        for w in WORLDS:
            state, witness = world_state(n, w["B"], w["C"])
            states.append(state)
            witnesses.append(witness)
            if shape == "prime" and state in CERT_STATES:
                prime_failures.append((n, w["name"], state, witness))

        records.append({
            "n": n,
            "shape": shape,
            "states": tuple(states),
            "first_certificate": first_certificate(states),
            "witnesses": witnesses,
        })

    prefix_rows = []
    for g in range(1, len(WORLDS) + 1):
        prime_sigs = set()
        composite_sigs = set()
        survivor_counts = Counter()
        survivor_total = 0

        for r in records:
            sig = r["states"][:g]
            if r["shape"] == "prime":
                prime_sigs.add(sig)
            else:
                composite_sigs.add(sig)
                if r["first_certificate"] is None or r["first_certificate"] > g:
                    survivor_total += 1
                    survivor_counts[r["shape"]] += 1

        prefix_rows.append({
            "genus": g,
            "world": WORLDS[g - 1]["name"],
            "composite_survivors": survivor_total,
            "prime_signatures": len(prime_sigs),
            "composite_signatures": len(composite_sigs),
            "mixed_signatures": len(prime_sigs & composite_sigs),
            "survive_prime_square": survivor_counts["prime_square"],
            "survive_semiprime_distinct": survivor_counts["semiprime_distinct"],
            "survive_higher_prime_power": survivor_counts["higher_prime_power"],
            "survive_other_composite": survivor_counts["other_composite"],
        })

    revelation = Counter()
    revelation_by_shape = defaultdict(Counter)
    for r in records:
        if r["shape"] == "prime":
            continue
        key = str(r["first_certificate"]) if r["first_certificate"] is not None else "unresolved"
        revelation[key] += 1
        revelation_by_shape[r["shape"]][key] += 1

    speed_by_shape = defaultdict(list)
    curvature_by_shape = defaultdict(list)
    for i, r in enumerate(records):
        if i > 0:
            speed_by_shape[r["shape"]].append(
                hamming(records[i - 1]["states"], r["states"])
            )
        if 0 < i < len(records) - 1:
            curvature_by_shape[r["shape"]].append(
                onehot_second_sq(
                    records[i - 1]["states"],
                    r["states"],
                    records[i + 1]["states"],
                )
            )

    trajectory_rows = []
    shapes = [
        "prime",
        "prime_square",
        "semiprime_distinct",
        "higher_prime_power",
        "other_composite",
    ]
    for shape in shapes:
        trajectory_rows.append({
            "shape": shape,
            "count": sum(1 for r in records if r["shape"] == shape),
            "mean_hamming_speed": mean(speed_by_shape[shape]),
            "mean_curvature_proxy": mean(curvature_by_shape[shape]),
            "max_curvature_proxy": max(curvature_by_shape[shape]) if curvature_by_shape[shape] else None,
        })

    factor_witness_count = 0
    composites = 0
    for r in records:
        if r["shape"] == "prime":
            continue
        composites += 1
        if any(w is not None and 1 < w < r["n"] for w in r["witnesses"]):
            factor_witness_count += 1

    payload = {
        "bits": args.bits,
        "limit": limit,
        "worlds": WORLDS,
        "prime_failures": prime_failures,
        "prefix_rows": prefix_rows,
        "revelation": dict(revelation),
        "revelation_by_shape": {k: dict(v) for k, v in revelation_by_shape.items()},
        "trajectory_rows": trajectory_rows,
        "composites": composites,
        "composites_with_explicit_factor_witness": factor_witness_count,
    }
    (out / "real_world_surface_scan.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )

    with (out / "prefix_surface.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(prefix_rows[0].keys()))
        wr.writeheader()
        wr.writerows(prefix_rows)

    with (out / "trajectory_stats.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(trajectory_rows[0].keys()))
        wr.writeheader()
        wr.writerows(trajectory_rows)

    md = [
        "# H21-LAB-03 · Real quadratic worlds on a surface",
        "",
        f"Range: odd n with 3 <= n < 2^{args.bits}.",
        "",
        "World order: " + " -> ".join(w["name"] for w in WORLDS) + ".",
        "",
        f"Prime certificate failures: **{len(prime_failures)}**.",
        "",
        "## Surface-prefix tomography",
        "",
        "| genus | last world | composite survivors | mixed prime/composite signatures | prime sigs | composite sigs |",
        "|---:|---|---:|---:|---:|---:|",
    ]
    for row in prefix_rows:
        md.append(
            f"| {row['genus']} | {row['world']} | {row['composite_survivors']} | "
            f"{row['mixed_signatures']} | {row['prime_signatures']} | {row['composite_signatures']} |"
        )

    md += [
        "",
        "## Revelation distribution for composites",
        "",
        "~~~text",
        json.dumps(dict(sorted(revelation.items())), indent=2),
        "~~~",
        "",
        "## Trajectory diagnostics",
        "",
        "| class | count | mean Hamming speed | mean curvature proxy | max curvature proxy |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in trajectory_rows:
        md.append(
            f"| {row['shape']} | {row['count']} | "
            f"{row['mean_hamming_speed']:.6f} | "
            f"{row['mean_curvature_proxy']:.6f} | "
            f"{row['max_curvature_proxy']} |"
        )

    md += [
        "",
        "## Explicit factor witnesses",
        "",
        f"Composites with at least one nontrivial gcd/defect factor witness: "
        f"**{factor_witness_count} / {composites}**.",
        "",
        "## Claim boundary",
        "",
        "The speed/curvature quantities are finite observer diagnostics. "
        "They are not intrinsic geometric curvature and are not accepted as prime-specific "
        "without stronger residue-periodicity and null-model controls.",
    ]

    (out / "H21_LAB03_REPORT.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))
    print("PASS: H21-LAB-03 completed")

    if prime_failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
