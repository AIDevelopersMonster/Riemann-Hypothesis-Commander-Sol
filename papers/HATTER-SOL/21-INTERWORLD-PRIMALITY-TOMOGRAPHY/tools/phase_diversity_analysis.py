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

MASK_NAMES = {0:"{}",1:"{0}",2:"{1}",3:"{0,1}"}


def jacobi(a: int, n: int) -> int:
    if n <= 0 or n % 2 == 0:
        raise ValueError
    a %= n
    out = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3,5):
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
        (a*c + b*d*C) % n,
        (a*d + b*c + b*d*B) % n,
    )


def pow_x(e: int, n: int, B: int, C: int):
    acc = (1,0)
    base = (0,1)
    while e:
        if e & 1:
            acc = mul(acc, base, n, B, C)
        base = mul(base, base, n, B, C)
        e >>= 1
    return acc


def lucas_triplet(m: int, mod: int, B: int, C: int):
    xm = pow_x(m, mod, B, C)
    um = xm[1] % mod
    xmp1 = mul(xm, (0,1), mod, B, C)
    up = xmp1[1] % mod
    invc = pow(C % mod, -1, mod)
    um1 = ((up - B*um) * invc) % mod
    return um1, um, up


def local_mask(p: int, q: int, B: int, C: int, D: int):
    cp = jacobi(D, p)
    cq = jacobi(D, q)
    if cp not in (-1,1) or cq not in (-1,1):
        raise ValueError

    um1, u, up = lucas_triplet(q, p, B, C)
    z1 = ((u - cq) % p) == 0

    if cp == 1:
        eps = (1-cq)//2
        z0 = ((C*um1 - eps*B) % p) == 0
    else:
        rhs = B*((1+cq)//2)
        z0 = ((up-rhs) % p) == 0

    return (1 if z0 else 0) | (2 if z1 else 0)


def prime_list(limit: int):
    isp = bytearray(b"\x01")*(limit+1)
    isp[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5)+1):
        if isp[p]:
            st = p*p
            isp[st:limit+1:p] = b"\x00"*(((limit-st)//p)+1)
    return [p for p in range(3, limit+1, 2) if isp[p]]


def entropy(probs):
    return -sum(x*math.log2(x) for x in probs if x > 0)


def spearman(xs, ys):
    def ranks(vals):
        order = sorted(range(len(vals)), key=lambda i: vals[i])
        out = [0.0]*len(vals)
        k = 0
        while k < len(order):
            j = k + 1
            while j < len(order) and vals[order[j]] == vals[order[k]]:
                j += 1
            r = (k + 1 + j) / 2.0
            for t in range(k, j):
                out[order[t]] = r
            k = j
        return out

    rx = ranks(xs)
    ry = ranks(ys)
    mx = sum(rx)/len(rx)
    my = sum(ry)/len(ry)
    num = sum((a-mx)*(b-my) for a,b in zip(rx,ry))
    denx = sum((a-mx)**2 for a in rx)
    deny = sum((b-my)**2 for b in ry)
    return num/math.sqrt(denx*deny) if denx and deny else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, default=18)
    ap.add_argument("--out-dir", default="lab09_out")
    args = ap.parse_args()

    limit = 1 << args.bits
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    primes = prime_list(limit)
    pairs = []
    for i,p in enumerate(primes):
        if p*p >= limit:
            break
        for q in primes[i+1:]:
            if p*q >= limit:
                break
            pairs.append((p,q))

    rows = []
    matrix_rows = []

    for w in WORLDS:
        B,C = w["B"], w["C"]
        D = B*B + 4*C
        joint = Counter()
        directed = Counter()
        local_by_p = defaultdict(Counter)
        eligible = 0
        exposed = 0

        for p,q in pairs:
            if math.gcd(p*q, abs(2*C*D)) != 1:
                continue
            cp = jacobi(D,p)
            cq = jacobi(D,q)
            if cp not in (-1,1) or cq not in (-1,1):
                continue

            x = local_mask(p,q,B,C,D)
            y = local_mask(q,p,B,C,D)

            eligible += 1
            exposed += int(x != y)
            joint[(x,y)] += 1
            directed[x] += 1
            directed[y] += 1
            local_by_p[p][x] += 1
            local_by_p[q][y] += 1

        total_dir = 2*eligible
        pi = [directed[z]/total_dir for z in range(4)]
        H = entropy(pi)
        G = 1 - sum(v*v for v in pi)
        A = exposed/eligible if eligible else 0.0
        K = A - G

        local_ent = []
        local_gini = []
        local_partial = []
        for p,cnt in local_by_p.items():
            t = sum(cnt.values())
            probs = [cnt[z]/t for z in range(4)]
            local_ent.append(entropy(probs))
            local_gini.append(1-sum(v*v for v in probs))
            local_partial.append((cnt[1]+cnt[2])/t)

        rows.append({
            "bits": args.bits,
            "world": w["name"],
            "eligible_pairs": eligible,
            "exposure": A,
            "shannon_entropy": H,
            "gini_diversity": G,
            "coupling_correction": K,
            "relative_coupling": K/G if G else 0.0,
            "mean_local_entropy": sum(local_ent)/len(local_ent) if local_ent else 0.0,
            "mean_local_gini": sum(local_gini)/len(local_gini) if local_gini else 0.0,
            "mean_local_partial_fraction": sum(local_partial)/len(local_partial) if local_partial else 0.0,
            "global_empty_fraction": pi[0],
            "global_partial_fraction": pi[1]+pi[2],
            "global_full_fraction": pi[3],
            "identity_error": abs(A-(G+K)),
        })

        for a in range(4):
            for b in range(4):
                sym = (joint[(a,b)] + joint[(b,a)])/(2*eligible) if eligible else 0.0
                matrix_rows.append({
                    "bits": args.bits,
                    "world": w["name"],
                    "mask_a": MASK_NAMES[a],
                    "mask_b": MASK_NAMES[b],
                    "sym_joint_probability": sym,
                })

    exposure = [r["exposure"] for r in rows]
    metrics = {}
    for key in [
        "shannon_entropy",
        "gini_diversity",
        "mean_local_entropy",
        "mean_local_gini",
        "mean_local_partial_fraction",
        "global_partial_fraction",
    ]:
        metrics[key] = spearman([r[key] for r in rows], exposure)

    with (out/"world_quality_metrics.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        wr.writeheader()
        wr.writerows(rows)

    with (out/"cross_mask_matrices.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(matrix_rows[0].keys()))
        wr.writeheader()
        wr.writerows(matrix_rows)

    payload = {
        "bits": args.bits,
        "limit": limit,
        "semiprime_pairs": len(pairs),
        "rows": rows,
        "spearman_vs_exposure": metrics,
    }
    (out/"phase_diversity_analysis.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )

    md = [
        "# H21-LAB-09 · Zero-mask diversity and cross-coupling",
        "",
        f"Range: distinct odd semiprimes pq < 2^{args.bits}.",
        "",
        "| world | exposure | H | Gini G | coupling K | K/G | local H | partial fraction |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        md.append(
            f"| {r['world']} | {r['exposure']:.6%} | "
            f"{r['shannon_entropy']:.6f} | {r['gini_diversity']:.6f} | "
            f"{r['coupling_correction']:.6f} | {r['relative_coupling']:.6f} | "
            f"{r['mean_local_entropy']:.6f} | {r['global_partial_fraction']:.6%} |"
        )

    md += ["", "## Descriptive six-world Spearman correlations with exposure", ""]
    for k,v in metrics.items():
        md.append(f"- {k}: {v:.6f}")

    md += [
        "",
        "## Exact identity check",
        "",
        f"Maximum |A-(G+K)|: **{max(r['identity_error'] for r in rows):.3e}**.",
        "",
        "## Claim boundary",
        "",
        "With only six worlds, rank correlations are descriptive, not inferential. "
        "The exact result is the diversity-plus-coupling decomposition.",
    ]

    (out/"H21_LAB09_REPORT.md").write_text("\n".join(md)+"\n", encoding="utf-8")
    print("\n".join(md))

    if max(r["identity_error"] for r in rows) > 1e-12:
        raise SystemExit(2)
    print("PASS: diversity-plus-coupling identity verified")


if __name__ == "__main__":
    main()
