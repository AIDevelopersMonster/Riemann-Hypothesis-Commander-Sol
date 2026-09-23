#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

DISCS = [-7, 5, -3, -11, 13, -19]


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


def spf_sieve(limit):
    spf = list(range(limit))
    if limit > 1:
        spf[1] = 1
    for p in range(2, int(limit ** 0.5) + 1):
        if spf[p] == p:
            for x in range(p * p, limit, p):
                if spf[x] == x:
                    spf[x] = p
    return spf


def shape(n, spf):
    if spf[n] == n:
        return "prime"
    fs = []
    x = n
    while x > 1:
        p = spf[x]
        fs.append(p)
        x //= p
    if len(fs) == 2:
        return "prime_square" if fs[0] == fs[1] else "semiprime_distinct"
    if len(set(fs)) == 1:
        return "higher_prime_power"
    return "other_composite"


def sig(n):
    return tuple(jacobi(d, n) for d in DISCS)


def ham(a,b):
    return sum(x != y for x,y in zip(a,b))


def curvature(a,b,c):
    # one-hot second-difference squared for symbols -1,0,+1
    total=0
    for x,y,z in zip(a,b,c):
        if x==y==z: total += 0
        elif x==z and x!=y: total += 8
        elif x==y or y==z: total += 2
        else: total += 6
    return total


def mean(xs):
    return sum(xs)/len(xs) if xs else None


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bits",type=int,default=19)
    ap.add_argument("--out-dir",default="lab04_out")
    args=ap.parse_args()

    limit=1<<args.bits
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    spf=spf_sieve(limit)

    rec=[]
    for n in range(3,limit,2):
        rec.append((n,shape(n,spf),sig(n)))

    speed=defaultdict(list); curv=defaultdict(list)
    for i,(n,sh,s) in enumerate(rec):
        if i>0: speed[sh].append(ham(rec[i-1][2],s))
        if 0<i<len(rec)-1:
            curv[sh].append(curvature(rec[i-1][2],s,rec[i+1][2]))

    rows=[]
    shapes=["prime","prime_square","semiprime_distinct","higher_prime_power","other_composite"]
    for sh in shapes:
        rows.append({
            "shape":sh,
            "count":sum(1 for _,x,_ in rec if x==sh),
            "mean_hamming_speed":mean(speed[sh]),
            "mean_curvature_proxy":mean(curv[sh]),
            "max_curvature_proxy":max(curv[sh]) if curv[sh] else None
        })

    # Periodicity check on values coprime to all discriminants.
    modulus=1
    for d in DISCS:
        modulus=math.lcm(modulus,abs(d))
    mismatches=0; checked=0
    for n in range(3, min(limit-modulus, modulus*4), 2):
        if math.gcd(n, modulus)!=1 or math.gcd(n+modulus,modulus)!=1:
            continue
        checked += 1
        if sig(n)!=sig(n+modulus):
            mismatches += 1

    with (out/"sign_only_stats.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    payload={"bits":args.bits,"discriminants":DISCS,"modulus":modulus,
             "periodicity_checked":checked,"periodicity_mismatches":mismatches,
             "rows":rows}
    (out/"sign_only_control.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")

    md=["# H21-LAB-04 · Sign-only negative control","",
        f"Discriminants: {DISCS}.","",f"Character period candidate: **{modulus}**.","",
        f"Periodicity checks: **{checked}**, mismatches: **{mismatches}**.","",
        "| class | count | mean Hamming speed | mean curvature proxy | max |",
        "|---|---:|---:|---:|---:|"]
    for r in rows:
        md.append(f"| {r['shape']} | {r['count']} | {r['mean_hamming_speed']:.6f} | {r['mean_curvature_proxy']:.6f} | {r['max_curvature_proxy']} |")
    md += ["","## Interpretation","",
           "This observer contains only quadratic-character geometry.  Any structure here is bounded by the finite residue-character system and is not a new primality mechanism.",
           ""]
    (out/"H21_LAB04_REPORT.md").write_text("\n".join(md),encoding="utf-8")
    print("\n".join(md))
    if mismatches:
        raise SystemExit(2)


if __name__=="__main__":
    main()
