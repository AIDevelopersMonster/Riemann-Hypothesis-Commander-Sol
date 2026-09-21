#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

WORLDS = [
    {"name": "D-7", "B": 1, "C": -2},
    {"name": "D+5", "B": 1, "C": 1},
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


def world_pass(n: int, B: int, C: int):
    D = B * B + 4 * C
    g = math.gcd(n, abs(2 * C * D))
    if g != 1:
        if 1 < g < n:
            return False, f"gcd-witness:{g}"
        return None, "degenerate-world"

    j = jacobi(D, n)
    if j not in (-1, 1):
        return False, "jacobi-zero"

    got = pow_x(n, B, C)
    want = (0, 1) if j == 1 else (B % n, (-1) % n)
    return got == want, f"jacobi:{j}"


def sieve(limit: int):
    is_prime = bytearray(b"\x01") * limit
    if limit > 0:
        is_prime[0] = 0
    if limit > 1:
        is_prime[1] = 0
    p = 2
    while p * p < limit:
        if is_prime[p]:
            start = p * p
            is_prime[start:limit:p] = b"\x00" * (((limit - 1 - start) // p) + 1)
        p += 1
    return is_prime


def smallest_factor(n: int):
    if n % 2 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, default=22)
    ap.add_argument("--out-dir", default="lab01_out")
    args = ap.parse_args()

    limit = 1 << args.bits
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    prime = sieve(limit)

    # Prime sanity: every nondegenerate declared world must satisfy Frobenius law.
    prime_failures = []
    for n in range(3, limit, 2):
        if not prime[n]:
            continue
        for w in WORLDS:
            ok, why = world_pass(n, w["B"], w["C"])
            if ok is False:
                prime_failures.append((n, w["name"], why))

    survivors = [n for n in range(3, limit, 2) if not prime[n]]
    initial = len(survivors)
    rows = []

    first_survivors = None

    for idx, w in enumerate(WORLDS, 1):
        nxt = []
        for n in survivors:
            ok, _ = world_pass(n, w["B"], w["C"])
            if ok is None or ok:
                nxt.append(n)
        survivors = nxt
        if idx == 1:
            first_survivors = survivors[:]
        rows.append({
            "step": idx,
            "world": w["name"],
            "B": w["B"],
            "C": w["C"],
            "discriminant": w["B"] * w["B"] + 4 * w["C"],
            "composite_survivors": len(survivors),
        })

    survivor_detail = []
    for n in first_survivors or []:
        f = smallest_factor(n)
        survivor_detail.append({
            "n": n,
            "factor_a": f,
            "factor_b": n // f,
        })

    payload = {
        "bits": args.bits,
        "limit": limit,
        "odd_composites": initial,
        "prime_failures": prime_failures,
        "worlds": rows,
        "first_world_survivors": survivor_detail,
        "final_composite_survivors": survivors,
    }

    (out / "world_scan.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    with (out / "world_scan.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        wr.writeheader()
        wr.writerows(rows)

    md = [
        "# H21-LAB-01 · Quadratic world-response scan",
        "",
        f"Range: odd n with 3 <= n < 2^{args.bits}.",
        "",
        f"Odd composites: **{initial}**.",
        "",
        f"Prime sanity failures: **{len(prime_failures)}**.",
        "",
        "| step | world | discriminant | composite survivors |",
        "|---:|---|---:|---:|",
    ]
    for r in rows:
        md.append(
            f"| {r['step']} | {r['world']} | {r['discriminant']} | {r['composite_survivors']} |"
        )

    md += [
        "",
        "## First-world survivors",
        "",
        "| n | factorization witness |",
        "|---:|---|",
    ]
    for x in survivor_detail:
        md.append(f"| {x['n']} | {x['factor_a']} x {x['factor_b']} |")

    md += [
        "",
        "## Exact finite statement",
        "",
        f"On the declared finite range, the ordered world sequence {WORLDS[0]['name']} -> {WORLDS[1]['name']} leaves "
        f"{len(survivors)} odd composite survivors.",
        "",
        "## Non-claim",
        "",
        "This is a finite computational result in known Frobenius probable-prime territory. "
        "It is not a new primality theorem and no asymptotic claim is made.",
    ]

    (out / "H21_LAB01_REPORT.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"odd composites: {initial}")
    for r in rows:
        print(f"{r['world']}: survivors={r['composite_survivors']}")
    print(f"prime sanity failures: {len(prime_failures)}")
    print(f"FINAL_SURVIVORS={len(survivors)}")

    if prime_failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
