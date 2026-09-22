#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path


def squarefree(n: int) -> bool:
    n = abs(n)
    if n == 0:
        return False
    p = 2
    while p * p <= n:
        if n % (p*p) == 0:
            return False
        p += 1
    return True


def fundamental_discriminants(dmax: int):
    out = []
    for D in range(-dmax, dmax + 1):
        if D in (0, 1):
            continue
        if D % 4 == 1 and squarefree(D):
            out.append(D)
            continue
        if D % 4 == 0:
            d = D // 4
            if d % 4 in (2, 3) and squarefree(d):
                out.append(D)
    return out


def world_from_D(D: int):
    if D % 4 == 1:
        B = 1
        C = (D - 1) // 4
    elif D % 4 == 0:
        B = 0
        C = D // 4
    else:
        raise ValueError(D)
    if B*B + 4*C != D:
        raise AssertionError((D, B, C))
    return {
        "D": D,
        "B": B,
        "C": C,
        "name": f"D{D:+d}",
        "torsion_control": D in (-3, -4),
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
        (a*c + b*d*C) % n,
        (a*d + b*c + b*d*B) % n,
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


def lucas_triplet(m: int, mod: int, B: int, C: int):
    xm = pow_x(m, mod, B, C)
    um = xm[1] % mod
    xmp1 = mul(xm, (0, 1), mod, B, C)
    up = xmp1[1] % mod
    invc = pow(C % mod, -1, mod)
    um1 = ((up - B*um) * invc) % mod
    return um1, um, up


def local_mask(p: int, q: int, B: int, C: int, D: int):
    cp = jacobi(D, p)
    cq = jacobi(D, q)
    if cp not in (-1, 1) or cq not in (-1, 1):
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


def metrics_from_counts(joint: Counter, directed: Counter, eligible: int):
    if eligible == 0:
        return {
            "eligible": 0,
            "exposure": 0.0,
            "entropy": 0.0,
            "gini": 0.0,
            "coupling": 0.0,
            "relative_coupling": 0.0,
            "empty_fraction": 0.0,
            "partial_fraction": 0.0,
            "full_fraction": 0.0,
        }

    total_dir = 2*eligible
    pi = [directed[z]/total_dir for z in range(4)]
    exposed = sum(c for (a,b),c in joint.items() if a != b)
    Q = exposed/eligible
    G = 1 - sum(x*x for x in pi)
    K = Q - G

    return {
        "eligible": eligible,
        "exposure": Q,
        "entropy": entropy(pi),
        "gini": G,
        "coupling": K,
        "relative_coupling": K/G if G else 0.0,
        "empty_fraction": pi[0],
        "partial_fraction": pi[1] + pi[2],
        "full_fraction": pi[3],
    }


def ranks(values, reverse=False):
    order = sorted(range(len(values)), key=lambda i: values[i], reverse=reverse)
    out = [0.0]*len(values)
    k = 0
    while k < len(order):
        j = k+1
        while j < len(order) and values[order[j]] == values[order[k]]:
            j += 1
        rank = (k+1+j)/2.0
        for t in range(k,j):
            out[order[t]] = rank
        k = j
    return out


def spearman(xs, ys):
    rx = ranks(xs)
    ry = ranks(ys)
    mx = sum(rx)/len(rx)
    my = sum(ry)/len(ry)
    num = sum((a-mx)*(b-my) for a,b in zip(rx,ry))
    denx = sum((a-mx)**2 for a in rx)
    deny = sum((b-my)**2 for b in ry)
    return num/math.sqrt(denx*deny) if denx and deny else 0.0


def pearson(xs, ys):
    mx = sum(xs)/len(xs)
    my = sum(ys)/len(ys)
    num = sum((a-mx)*(b-my) for a,b in zip(xs,ys))
    denx = sum((a-mx)**2 for a in xs)
    deny = sum((b-my)**2 for b in ys)
    return num/math.sqrt(denx*deny) if denx and deny else 0.0


def ranking_inversions(rows, xkey, ykey):
    comparable = 0
    discord = 0
    examples = []
    for i in range(len(rows)):
        for j in range(i+1, len(rows)):
            dx = rows[i][xkey] - rows[j][xkey]
            dy = rows[i][ykey] - rows[j][ykey]
            if dx == 0 or dy == 0:
                continue
            comparable += 1
            if dx*dy < 0:
                discord += 1
                if len(examples) < 20:
                    examples.append({
                        "world_a": rows[i]["world"],
                        "world_b": rows[j]["world"],
                        xkey+"_a": rows[i][xkey],
                        xkey+"_b": rows[j][xkey],
                        ykey+"_a": rows[i][ykey],
                        ykey+"_b": rows[j][ykey],
                    })
    return {
        "comparable_pairs": comparable,
        "discordant_pairs": discord,
        "discordant_fraction": discord/comparable if comparable else 0.0,
        "examples": examples,
    }


def topk_overlap(rows, xkey, ykey, k):
    a = {r["world"] for r in sorted(rows, key=lambda r:r[xkey], reverse=True)[:k]}
    b = {r["world"] for r in sorted(rows, key=lambda r:r[ykey], reverse=True)[:k]}
    return len(a & b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, default=17)
    ap.add_argument("--dmax", type=int, default=127)
    ap.add_argument("--out-dir", default="lab10_out")
    args = ap.parse_args()

    limit = 1 << args.bits
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    Ds = fundamental_discriminants(args.dmax)
    worlds = [world_from_D(D) for D in Ds]

    primes = prime_list(limit)
    pairs = []
    common_pairs = []
    for i,p in enumerate(primes):
        if p*p >= limit:
            break
        for q in primes[i+1:]:
            if p*q >= limit:
                break
            pairs.append((p,q))
            if p > args.dmax and q > args.dmax:
                common_pairs.append((p,q))

    rows = []

    for wi,w in enumerate(worlds, 1):
        B,C,D = w["B"],w["C"],w["D"]

        all_joint = Counter()
        all_directed = Counter()
        all_eligible = 0

        core_joint = Counter()
        core_directed = Counter()
        core_eligible = 0

        for p,q in pairs:
            if math.gcd(p*q, abs(2*C*D)) != 1:
                continue
            cp = jacobi(D,p)
            cq = jacobi(D,q)
            if cp not in (-1,1) or cq not in (-1,1):
                continue

            x = local_mask(p,q,B,C,D)
            y = local_mask(q,p,B,C,D)

            all_eligible += 1
            all_joint[(x,y)] += 1
            all_directed[x] += 1
            all_directed[y] += 1

            if p > args.dmax and q > args.dmax:
                core_eligible += 1
                core_joint[(x,y)] += 1
                core_directed[x] += 1
                core_directed[y] += 1

        ma = metrics_from_counts(all_joint, all_directed, all_eligible)
        mc = metrics_from_counts(core_joint, core_directed, core_eligible)

        row = {
            "world": w["name"],
            "D": D,
            "B": B,
            "C": C,
            "sign": "negative" if D < 0 else "positive",
            "torsion_control": int(w["torsion_control"]),
        }
        for prefix,m in (("all",ma),("core",mc)):
            for k,v in m.items():
                row[prefix+"_"+k] = v
        rows.append(row)

        if wi % 25 == 0 or wi == len(worlds):
            print(f"progress {wi}/{len(worlds)} worlds")

    non_torsion = [r for r in rows if not r["torsion_control"]]

    def summary(pop):
        qkey = pop+"_exposure"
        gkey = pop+"_gini"
        hkey = pop+"_entropy"
        kkey = pop+"_coupling"

        inv_g = ranking_inversions(non_torsion, gkey, qkey)
        inv_h = ranking_inversions(non_torsion, hkey, qkey)

        q = [r[qkey] for r in non_torsion]
        g = [r[gkey] for r in non_torsion]
        h = [r[hkey] for r in non_torsion]
        absrel = [abs(r[pop+"_relative_coupling"]) for r in non_torsion if r[gkey] > 0]

        ranks_q = ranks(q, reverse=True)
        ranks_g = ranks(g, reverse=True)
        for r,rq,rg in zip(non_torsion,ranks_q,ranks_g):
            r[pop+"_rank_exposure"] = rq
            r[pop+"_rank_gini"] = rg
            r[pop+"_rank_displacement"] = abs(rq-rg)

        return {
            "worlds": len(non_torsion),
            "spearman_gini_exposure": spearman(g,q),
            "pearson_gini_exposure": pearson(g,q),
            "spearman_entropy_exposure": spearman(h,q),
            "pearson_entropy_exposure": pearson(h,q),
            "gini_inversions": inv_g,
            "entropy_inversions": inv_h,
            "top5_gini_overlap": topk_overlap(non_torsion,gkey,qkey,min(5,len(non_torsion))),
            "top10_gini_overlap": topk_overlap(non_torsion,gkey,qkey,min(10,len(non_torsion))),
            "top20_gini_overlap": topk_overlap(non_torsion,gkey,qkey,min(20,len(non_torsion))),
            "mean_abs_relative_coupling": sum(absrel)/len(absrel) if absrel else 0.0,
            "max_abs_relative_coupling": max(absrel) if absrel else 0.0,
            "coupling_gt_10pct": sum(x>0.10 for x in absrel),
            "coupling_gt_25pct": sum(x>0.25 for x in absrel),
        }

    summaries = {
        "all": summary("all"),
        "core": summary("core"),
    }

    rows.sort(key=lambda r:r["core_exposure"], reverse=True)

    with (out/"broad_world_metrics.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        wr.writeheader()
        wr.writerows(rows)

    payload = {
        "bits": args.bits,
        "limit": limit,
        "dmax": args.dmax,
        "fundamental_world_count": len(worlds),
        "non_torsion_world_count": len(non_torsion),
        "semiprime_pairs": len(pairs),
        "common_core_pairs": len(common_pairs),
        "summaries": summaries,
        "top10_core_exposure": [
            {
                "world": r["world"],
                "D": r["D"],
                "Q": r["core_exposure"],
                "G": r["core_gini"],
                "K": r["core_coupling"],
                "H": r["core_entropy"],
            }
            for r in rows[:10]
        ],
        "bottom10_core_exposure": [
            {
                "world": r["world"],
                "D": r["D"],
                "Q": r["core_exposure"],
                "G": r["core_gini"],
                "K": r["core_coupling"],
                "H": r["core_entropy"],
            }
            for r in rows[-10:]
        ],
    }
    (out/"broad_world_scan.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    s = summaries["core"]
    md = [
        "# H21-LAB-10 · Broad fundamental-discriminant world scan",
        "",
        f"bits={args.bits}, |D|<={args.dmax}.",
        "",
        f"Fundamental worlds: **{len(worlds)}**; non-torsion ranking worlds: **{len(non_torsion)}**.",
        "",
        f"All distinct semiprime pairs: **{len(pairs)}**.",
        "",
        f"Common-core pairs p,q>{args.dmax}: **{len(common_pairs)}**.",
        "",
        "## Common-core compiler test",
        "",
        f"Spearman(G,Q): **{s['spearman_gini_exposure']:.6f}**.",
        "",
        f"Pearson(G,Q): **{s['pearson_gini_exposure']:.6f}**.",
        "",
        f"Gini rank inversions: **{s['gini_inversions']['discordant_pairs']} / {s['gini_inversions']['comparable_pairs']} = {s['gini_inversions']['discordant_fraction']:.6%}**.",
        "",
        f"Top-10 overlap G vs Q: **{s['top10_gini_overlap']}/10**.",
        "",
        f"Mean |K|/G: **{s['mean_abs_relative_coupling']:.6%}**.",
        "",
        f"Max |K|/G: **{s['max_abs_relative_coupling']:.6%}**.",
        "",
        "## Top common-core worlds by exact exposure",
        "",
        "| rank | world | Q | G | K |",
        "|---:|---|---:|---:|---:|",
    ]
    for i,r in enumerate(rows[:15],1):
        md.append(
            f"| {i} | {r['world']} | {r['core_exposure']:.6%} | "
            f"{r['core_gini']:.6f} | {r['core_coupling']:+.6f} |"
        )

    md += [
        "",
        "## Torsion controls",
        "",
    ]
    for r in rows:
        if r["torsion_control"]:
            md.append(
                f"- {r['world']}: core Q={r['core_exposure']:.6%}, "
                f"G={r['core_gini']:.6f}, K={r['core_coupling']:+.6f}"
            )

    md += [
        "",
        "## Claim boundary",
        "",
        "This is a broad finite compiler validation. It is not an asymptotic theorem.",
    ]

    (out/"H21_LAB10_REPORT.md").write_text("\n".join(md)+"\n", encoding="utf-8")
    print("\n".join(md))
    print("PASS: broad world scan completed")


if __name__ == "__main__":
    main()
