#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path


MASK_NAMES = {0:"{}",1:"{0}",2:"{1}",3:"{0,1}"}


def squarefree(n: int) -> bool:
    n = abs(n)
    if n == 0:
        return False
    p = 2
    while p*p <= n:
        if n % (p*p) == 0:
            return False
        p += 1
    return True


def fundamental_discriminants(dmax: int):
    out=[]
    for D in range(-dmax,dmax+1):
        if D in (0,1):
            continue
        if D % 4 == 1 and squarefree(D):
            out.append(D)
        elif D % 4 == 0:
            d=D//4
            if d % 4 in (2,3) and squarefree(d):
                out.append(D)
    return out


def world_from_D(D: int):
    if D % 4 == 1:
        B=1; C=(D-1)//4
    else:
        B=0; C=D//4
    return B,C


def jacobi(a: int,n: int) -> int:
    a%=n
    out=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5):
                out=-out
        a,n=n,a
        if a%4==3 and n%4==3:
            out=-out
        a%=n
    return out if n==1 else 0


def mul(u,v,n,B,C):
    a,b=u; c,d=v
    return ((a*c+b*d*C)%n,(a*d+b*c+b*d*B)%n)


def pow_x(e,n,B,C):
    acc=(1,0); base=(0,1)
    while e:
        if e&1:
            acc=mul(acc,base,n,B,C)
        base=mul(base,base,n,B,C)
        e>>=1
    return acc


def lucas_triplet(m,mod,B,C):
    xm=pow_x(m,mod,B,C)
    um=xm[1]%mod
    up=mul(xm,(0,1),mod,B,C)[1]%mod
    um1=((up-B*um)*pow(C%mod,-1,mod))%mod
    return um1,um,up


def local_mask(p,q,B,C,D):
    cp=jacobi(D,p); cq=jacobi(D,q)
    um1,u,up=lucas_triplet(q,p,B,C)
    z1=((u-cq)%p)==0
    if cp==1:
        z0=((C*um1-((1-cq)//2)*B)%p)==0
    else:
        z0=((up-B*((1+cq)//2))%p)==0
    return (1 if z0 else 0)|(2 if z1 else 0)


def prime_list(limit):
    isp=bytearray(b"\x01")*(limit+1)
    isp[0:2]=b"\x00\x00"
    for p in range(2,int(limit**0.5)+1):
        if isp[p]:
            st=p*p
            isp[st:limit+1:p]=b"\x00"*(((limit-st)//p)+1)
    return [p for p in range(3,limit+1,2) if isp[p]]


def mutual_information_bits(joint,pi,eligible):
    out=0.0
    for (a,b),count in joint.items():
        if count==0:
            continue
        pab=count/eligible
        denom=pi[a]*pi[b]
        if denom>0:
            out += pab*math.log2(pab/denom)
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bits",type=int,default=18)
    ap.add_argument("--dmax",type=int,default=255)
    ap.add_argument("--out-dir",default="lab11_out")
    args=ap.parse_args()

    limit=1<<args.bits
    out=Path(args.out_dir)
    out.mkdir(parents=True,exist_ok=True)

    worlds=fundamental_discriminants(args.dmax)
    primes=prime_list(limit)
    pairs=[]
    for i,p in enumerate(primes):
        if p*p>=limit:
            break
        for q in primes[i+1:]:
            if p*q>=limit:
                break
            if p>args.dmax and q>args.dmax:
                pairs.append((p,q))

    rows=[]
    component_rows=[]

    for wi,D in enumerate(worlds,1):
        B,C=world_from_D(D)
        joint=Counter()
        directed=Counter()

        for p,q in pairs:
            x=local_mask(p,q,B,C,D)
            y=local_mask(q,p,B,C,D)
            joint[(x,y)] += 1
            directed[x] += 1
            directed[y] += 1

        eligible=len(pairs)
        total_dir=2*eligible
        pi=[directed[z]/total_dir for z in range(4)]

        same=sum(joint[(z,z)] for z in range(4))/eligible
        Q=1-same
        G=1-sum(v*v for v in pi)
        K=Q-G
        pmax=max(pi)
        qmax=min(1.0,2*(1-pmax))
        klow=-G
        kup=qmax-G

        mi_bits=mutual_information_bits(joint,pi,eligible)
        pinsker=math.sqrt(math.log(2)*mi_bits/2) if mi_bits>0 else 0.0

        tv=0.0
        for a in range(4):
            for b in range(4):
                pab=joint[(a,b)]/eligible
                tv += abs(pab-pi[a]*pi[b])
        tv*=0.5

        cov_sum=0.0
        comps={}
        for z in range(4):
            jaa=joint[(z,z)]/eligible
            c=jaa-pi[z]*pi[z]
            comps[z]=c
            cov_sum += c
            component_rows.append({
                "world":f"D{D:+d}",
                "D":D,
                "mask":MASK_NAMES[z],
                "pi":pi[z],
                "joint_diag":jaa,
                "diag_covariance":c,
                "contribution_to_K":-c,
            })

        row={
            "world":f"D{D:+d}",
            "D":D,
            "torsion_control":int(D in (-3,-4)),
            "eligible_pairs":eligible,
            "Q":Q,
            "G":G,
            "K":K,
            "pmax":pmax,
            "Qmax_fixed_marginal":qmax,
            "K_lower":klow,
            "K_upper":kup,
            "lower_slack":K-klow,
            "upper_slack":kup-K,
            "TV_joint_vs_product":tv,
            "mutual_information_bits":mi_bits,
            "pinsker_bound":pinsker,
            "K_over_TV":abs(K)/tv if tv else 0.0,
            "K_over_pinsker":abs(K)/pinsker if pinsker else 0.0,
            "covariance_identity_error":abs(K+cov_sum),
            "tv_bound_error":max(0.0,abs(K)-tv),
            "pinsker_bound_error":max(0.0,abs(K)-pinsker),
            "frechet_lower_error":max(0.0,klow-K),
            "frechet_upper_error":max(0.0,K-kup),
        }
        for z in range(4):
            row[f"c{z}"]=comps[z]
        rows.append(row)

        if wi%25==0 or wi==len(worlds):
            print(f"progress {wi}/{len(worlds)}")

    nont=[r for r in rows if not r["torsion_control"]]
    neg=sorted(nont,key=lambda r:r["K"])[:10]
    pos=sorted(nont,key=lambda r:r["K"],reverse=True)[:10]
    coupling=sorted(nont,key=lambda r:abs(r["K"])/r["G"] if r["G"] else 0,reverse=True)[:15]

    with (out/"coupling_bounds.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        wr.writeheader(); wr.writerows(rows)

    with (out/"coupling_components.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(component_rows[0].keys()))
        wr.writeheader(); wr.writerows(component_rows)

    checks={
        "max_covariance_identity_error":max(r["covariance_identity_error"] for r in rows),
        "max_tv_bound_error":max(r["tv_bound_error"] for r in rows),
        "max_pinsker_bound_error":max(r["pinsker_bound_error"] for r in rows),
        "max_frechet_lower_error":max(r["frechet_lower_error"] for r in rows),
        "max_frechet_upper_error":max(r["frechet_upper_error"] for r in rows),
    }

    payload={
        "bits":args.bits,
        "dmax":args.dmax,
        "world_count":len(worlds),
        "common_core_pairs":len(pairs),
        "checks":checks,
        "most_negative_K":neg,
        "most_positive_K":pos,
        "most_coupling_dominated":coupling,
    }
    (out/"coupling_structure.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")

    md=[
        "# H21-LAB-11 · Coupling structure and exact bounds",
        "",
        f"bits={args.bits}, |D|<={args.dmax}, common-core pairs={len(pairs)}.",
        "",
        f"Worlds: **{len(worlds)}**.",
        "",
        "## Exact check maxima",
        "",
    ]
    for k,v in checks.items():
        md.append(f"- {k}: **{v:.3e}**")

    md += [
        "",
        "## Most negative K",
        "",
        "| world | Q | G | K | MI bits | TV | dominant c-mask |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for r in neg:
        dom=max(range(4),key=lambda z:r[f"c{z}"])
        md.append(
            f"| {r['world']} | {r['Q']:.6%} | {r['G']:.6f} | {r['K']:+.6f} | "
            f"{r['mutual_information_bits']:.6f} | {r['TV_joint_vs_product']:.6f} | "
            f"{MASK_NAMES[dom]} ({r[f'c{dom}']:+.6f}) |"
        )

    md += [
        "",
        "## Most positive K",
        "",
        "| world | Q | G | K | MI bits | TV | dominant repulsive mask |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for r in pos:
        dom=min(range(4),key=lambda z:r[f"c{z}"])
        md.append(
            f"| {r['world']} | {r['Q']:.6%} | {r['G']:.6f} | {r['K']:+.6f} | "
            f"{r['mutual_information_bits']:.6f} | {r['TV_joint_vs_product']:.6f} | "
            f"{MASK_NAMES[dom]} ({r[f'c{dom}']:+.6f}) |"
        )

    md += [
        "",
        "## Bound sharpness",
        "",
        f"max |K|/TV among non-torsion worlds: **{max(r['K_over_TV'] for r in nont):.6f}**.",
        "",
        f"max |K|/Pinsker among non-torsion worlds: **{max(r['K_over_pinsker'] for r in nont):.6f}**.",
        "",
        "## Interpretation",
        "",
        "K is exactly the negative total diagonal covariance. "
        "TV and Pinsker give certified upper bounds; fixed-marginal Frechet bounds give the exact feasible interval.",
    ]

    (out/"H21_LAB11_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print("\n".join(md))

    if max(checks.values())>1e-12:
        raise SystemExit(2)
    print("PASS: coupling identities and bounds verified")


if __name__=="__main__":
    main()
