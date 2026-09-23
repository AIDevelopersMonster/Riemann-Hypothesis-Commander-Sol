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


def lucas_pair(m: int, mod: int, B: int, C: int):
    # Returns (U_m, U_{m+1}) via the same quadratic algebra identity:
    # x^m = C U_{m-1} + U_m x.
    if m == 0:
        return 0, 1
    xm = pow_x(m, mod, B, C)
    um = xm[1] % mod
    # x^(m+1) coefficient of x is U_{m+1}
    xmp1 = mul(xm, (0, 1), mod, B, C)
    return um, xmp1[1] % mod


def lucas_triplet(m: int, mod: int, B: int, C: int):
    um, up = lucas_pair(m, mod, B, C)
    if m == 0:
        return None, um, up
    # C is invertible in all calls here.
    inv_c = pow(C % mod, -1, mod)
    um1 = ((up - B * um) * inv_c) % mod
    return um1, um, up


def direct_local_mask(p: int, q: int, B: int, C: int, D: int):
    cp = jacobi(D, p)
    cq = jacobi(D, q)
    if cp not in (-1, 1) or cq not in (-1, 1):
        raise ValueError

    n = p * q
    got = pow_x(n, n, B, C)
    cn = cp * cq
    want = (0, 1) if cn == 1 else (B % n, (-1) % n)
    d0 = (got[0] - want[0]) % n
    d1 = (got[1] - want[1]) % n

    mask = 0
    if d0 % p == 0:
        mask |= 1
    if d1 % p == 0:
        mask |= 2
    return mask


def lucas_local_mask(p: int, q: int, B: int, C: int, D: int):
    cp = jacobi(D, p)
    cq = jacobi(D, q)
    if cp not in (-1, 1) or cq not in (-1, 1):
        raise ValueError

    uqm1, uq, uqp1 = lucas_triplet(q, p, B, C)

    z1 = (uq - cq) % p == 0

    if cp == 1:
        epsq = (1 - cq) // 2
        z0 = (C * uqm1 - epsq * B) % p == 0
    else:
        rhs = B * ((1 + cq) // 2)
        z0 = (uqp1 - rhs) % p == 0

    return (1 if z0 else 0) | (2 if z1 else 0)


def factor_int(n: int, small_primes):
    out = Counter()
    x = n
    for p in small_primes:
        if p * p > x:
            break
        while x % p == 0:
            out[p] += 1
            x //= p
    if x > 1:
        out[x] += 1
    return out


def prime_list(limit: int):
    isp = bytearray(b"\x01") * (limit + 1)
    isp[0:2] = b"\x00\x00"
    for p in range(2, int(limit ** 0.5) + 1):
        if isp[p]:
            start = p * p
            isp[start:limit+1:p] = b"\x00" * (((limit - start)//p)+1)
    return [p for p in range(2, limit + 1) if isp[p]], isp


def order_x(p: int, B: int, C: int, D: int, small_primes):
    chi = jacobi(D, p)
    if chi not in (-1, 1) or C % p == 0:
        return None

    if chi == 1:
        bound = p - 1
        fac = factor_int(bound, small_primes)
    else:
        # Safe universal bound p^2-1. Factor via p-1 and p+1.
        fac = factor_int(p - 1, small_primes)
        fp = factor_int(p + 1, small_primes)
        for r, e in fp.items():
            fac[r] += e
        bound = p * p - 1

    h = bound
    one = (1, 0)
    for r in sorted(fac):
        while h % r == 0 and pow_x(h // r, p, B, C) == one:
            h //= r
    if pow_x(h, p, B, C) != one:
        raise AssertionError(("bad order", p, B, C, D, h))
    return h


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, default=18)
    ap.add_argument("--out-dir", default="lab08_out")
    args = ap.parse_args()

    limit = 1 << args.bits
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    primes, isp = prime_list(limit)
    small_primes = [p for p in primes if p * p <= limit + 1]

    semiprimes = []
    used_primes = set()
    odd_primes = [p for p in primes if p >= 3]
    for i, p in enumerate(odd_primes):
        if p * p >= limit:
            break
        for q in odd_primes[i+1:]:
            if p * q >= limit:
                break
            semiprimes.append((p, q))
            used_primes.add(p)
            used_primes.add(q)

    lucas_formula_mismatches = []
    world_rows = []
    order_rows = []

    for w in WORLDS:
        B, C = w["B"], w["C"]
        D = B * B + 4 * C

        eligible = 0
        exposed = 0
        masks = Counter()

        for p, q in semiprimes:
            if math.gcd(p*q, abs(2*C*D)) != 1:
                continue
            cp = jacobi(D, p)
            cq = jacobi(D, q)
            if cp not in (-1,1) or cq not in (-1,1):
                continue
            eligible += 1

            lpq = lucas_local_mask(p, q, B, C, D)
            lqp = lucas_local_mask(q, p, B, C, D)

            dpq = direct_local_mask(p, q, B, C, D)
            dqp = direct_local_mask(q, p, B, C, D)

            if lpq != dpq or lqp != dqp:
                lucas_formula_mismatches.append({
                    "world": w["name"],
                    "p": p,
                    "q": q,
                    "lucas_pq": lpq,
                    "direct_pq": dpq,
                    "lucas_qp": lqp,
                    "direct_qp": dqp,
                })

            masks[(lpq, lqp)] += 1
            if lpq != lqp:
                exposed += 1

        local_orders = []
        for p in sorted(used_primes):
            if math.gcd(p, abs(C*D)) != 1:
                continue
            h = order_x(p, B, C, D, small_primes)
            if h is not None:
                local_orders.append((p, jacobi(D,p), h))
                order_rows.append({
                    "world": w["name"],
                    "p": p,
                    "chi": jacobi(D,p),
                    "order_x": h,
                    "log2_order": math.log2(h),
                })

        unique_orders = len(set(h for _,_,h in local_orders))
        mean_log = sum(math.log2(h) for _,_,h in local_orders) / len(local_orders)
        small6 = sum(h <= 6 for _,_,h in local_orders)

        world_rows.append({
            "world": w["name"],
            "eligible_semiprimes": eligible,
            "exposed_semiprimes": exposed,
            "exposure_fraction": exposed / eligible if eligible else 0.0,
            "primes_with_clock": len(local_orders),
            "unique_clock_orders": unique_orders,
            "mean_log2_clock_order": mean_log,
            "clock_order_le_6": small6,
            "clock_order_le_6_fraction": small6 / len(local_orders) if local_orders else 0.0,
        })

    with (out / "world_clock_summary.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(world_rows[0].keys()))
        wr.writeheader()
        wr.writerows(world_rows)

    with (out / "local_clock_orders.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(order_rows[0].keys()))
        wr.writeheader()
        wr.writerows(order_rows)

    payload = {
        "bits": args.bits,
        "limit": limit,
        "distinct_semiprimes": len(semiprimes),
        "lucas_formula_mismatch_count": len(lucas_formula_mismatches),
        "lucas_formula_mismatch_examples": lucas_formula_mismatches[:20],
        "world_rows": world_rows,
    }
    (out / "lucas_clock_validation.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )

    md = [
        "# H21-LAB-08 · Lucas local-clock validation",
        "",
        f"Range: distinct odd semiprimes pq < 2^{args.bits}.",
        "",
        f"Semiprimes: **{len(semiprimes)}**.",
        "",
        f"Lucas/direct zero-mask mismatches: **{len(lucas_formula_mismatches)}**.",
        "",
        "| world | eligible pq | exposed | exposure | prime clocks | unique orders | mean log2(h) | h<=6 fraction |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in world_rows:
        md.append(
            f"| {r['world']} | {r['eligible_semiprimes']} | {r['exposed_semiprimes']} | "
            f"{r['exposure_fraction']:.6%} | {r['primes_with_clock']} | "
            f"{r['unique_clock_orders']} | {r['mean_log2_clock_order']:.6f} | "
            f"{r['clock_order_le_6_fraction']:.6%} |"
        )

    md += [
        "",
        "## Interpretation",
        "",
        "The Lucas formulas are accepted as implementation-equivalent to direct quadratic defect coordinates iff mismatch count is zero.",
        "",
        "Clock order is reported as a structural descriptor, not assumed to be a monotone predictor of factor exposure.",
    ]

    (out / "H21_LAB08_REPORT.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))

    if lucas_formula_mismatches:
        raise SystemExit(2)
    print("PASS: Lucas local-clock formulas validated")


if __name__ == "__main__":
    main()
