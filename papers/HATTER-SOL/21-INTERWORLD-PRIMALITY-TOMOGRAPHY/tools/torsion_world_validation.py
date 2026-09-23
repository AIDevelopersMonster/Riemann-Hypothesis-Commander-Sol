#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


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


def pow_x(e: int, n: int, B: int, C: int):
    acc = (1, 0)
    base = (0, 1)
    while e:
        if e & 1:
            acc = mul(acc, base, n, B, C)
        base = mul(base, base, n, B, C)
        e >>= 1
    return acc


def expected(n: int, B: int, D: int):
    j = jacobi(D, n)
    if j == 1:
        return (0, 1), j
    if j == -1:
        return (B % n, (-1) % n), j
    return None, j


def sieve(limit: int):
    isp = bytearray(b"\x01") * limit
    if limit > 0:
        isp[0] = 0
    if limit > 1:
        isp[1] = 0
    for p in range(2, int(limit ** 0.5) + 1):
        if isp[p]:
            start = p * p
            isp[start:limit:p] = b"\x00" * (((limit - 1 - start)//p)+1)
    return isp


def test_world(limit: int, B: int, C: int, D: int, exceptional_prime: int | None):
    mismatches = []
    defect_nonzero = []
    character_mismatches = []
    precheck_factor_cases = 0
    odd_composite_cases = 0

    isp = sieve(limit)

    for n in range(3, limit, 2):
        if not isp[n]:
            odd_composite_cases += 1

        g = math.gcd(n, abs(2 * C * D))

        if exceptional_prime is not None and n % exceptional_prime == 0:
            if not isp[n] and 1 < exceptional_prime < n:
                precheck_factor_cases += 1
            continue

        if g != 1:
            continue

        want, j = expected(n, B, D)
        if j not in (-1, 1):
            mismatches.append(("jacobi", n, j))
            continue

        if D == -3:
            predicted_j = 1 if n % 6 == 1 else -1
        elif D == -4:
            predicted_j = 1 if n % 4 == 1 else -1
        else:
            predicted_j = j

        if j != predicted_j:
            character_mismatches.append((n, j, predicted_j))

        got = pow_x(n, n, B, C)
        if got != want:
            defect_nonzero.append((n, got, want, j))

    return {
        "odd_composite_cases": odd_composite_cases,
        "precheck_factor_cases": precheck_factor_cases,
        "character_mismatch_count": len(character_mismatches),
        "defect_nonzero_count": len(defect_nonzero),
        "character_mismatch_examples": character_mismatches[:20],
        "defect_nonzero_examples": defect_nonzero[:20],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, default=21)
    ap.add_argument("--out-dir", default="lab07_out")
    args = ap.parse_args()

    limit = 1 << args.bits
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    d3 = test_world(limit, B=1, C=-1, D=-3, exceptional_prime=3)
    d4 = test_world(limit, B=0, C=-1, D=-4, exceptional_prime=None)

    payload = {
        "bits": args.bits,
        "limit": limit,
        "D-3": d3,
        "D-4": d4,
    }
    (out / "torsion_world_validation.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )

    md = [
        "# H21-LAB-07 · Torsion-world no-go validation",
        "",
        f"Range: odd n with 3 <= n < 2^{args.bits}.",
        "",
        "## D=-3",
        "",
        f"Character-class mismatches: **{d3['character_mismatch_count']}**.",
        "",
        f"Nonzero defects away from multiples of 3: **{d3['defect_nonzero_count']}**.",
        "",
        f"Odd composite multiples of 3 caught by precheck: **{d3['precheck_factor_cases']}**.",
        "",
        "## D=-4",
        "",
        f"Character-class mismatches: **{d4['character_mismatch_count']}**.",
        "",
        f"Nonzero defects on odd inputs: **{d4['defect_nonzero_count']}**.",
        "",
        "## Exact interpretation",
        "",
        "Both torsion-world silence theorems pass iff all mismatch and nonzero-defect counts are zero.",
    ]
    (out / "H21_LAB07_REPORT.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))

    if (
        d3["character_mismatch_count"]
        or d3["defect_nonzero_count"]
        or d4["character_mismatch_count"]
        or d4["defect_nonzero_count"]
    ):
        raise SystemExit(2)

    print("PASS: torsion-world no-go validated")


if __name__ == "__main__":
    main()
