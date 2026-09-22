#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


MASKS=range(4)


def squarefree(n):
    n=abs(n)
    if n==0: return False
    p=2
    while p*p<=n:
        if n%(p*p)==0: return False
        p+=1
    return True


def fundamental_discriminants(dmax):
    out=[]
    for D in range(-dmax,dmax+1):
        if D in (0,1): continue
        if D%4==1 and squarefree(D):
            out.append(D)
        elif D%4==0:
            d=D//4
            if d%4 in (2,3) and squarefree(d):
                out.append(D)
    return out


def world(D):
    return (1,(D-1)//4) if D%4==1 else (0,D//4)


def jacobi(a,n):
    a%=n
    out=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): out=-out
        a,n=n,a
        if a%4==3 and n%4==3: out=-out
        a%=n
    return out if n==1 else 0


def mul(u,v,n,B,C):
    a,b=u; c,d=v
    return ((a*c+b*d*C)%n,(a*d+b*c+b*d*B)%n)


def pow_x(e,n,B,C):
    acc=(1,0); base=(0,1)
    while e:
        if e&1: acc=mul(acc,base,n,B,C)
        base=mul(base,base,n,B,C)
        e>>=1
    return acc


def trip(m,p,B,C):
    xm=pow_x(m,p,B,C)
    u=xm[1]%p
    up=mul(xm,(0,1),p,B,C)[1]%p
    um1=((up-B*u)*pow(C%p,-1,p))%p
    return um1,u,up


def mask(p,q,B,C,D):
    cp=jacobi(D,p); cq=jacobi(D,q)
    um1,u,up=trip(q,p,B,C)
    z1=((u-cq)%p)==0
    if cp==1:
        z0=((C*um1-((1-cq)//2)*B)%p)==0
    else:
        z0=((up-B*((1+cq)//2))%p)==0
    return (1 if z0 else 0)|(2 if z1 else 0)


def primes(limit):
    isp=bytearray(b"\x01")*(limit+1)
    isp[0:2]=b"\x00\x00"
    for p in range(2,int(limit**0.5)+1):
        if isp[p]:
            st=p*p
            isp[st:limit+1:p]=b"\x00"*(((limit-st)//p)+1)
    return [p for p in range(3,limit+1,2) if isp[p]]


def metrics(joint,directed,n):
    if n==0:
        return dict(Q=0.0,G=0.0,K=0.0,pi=[0.0]*4)
    pi=[directed[a]/(2*n) for a in MASKS]
    same=sum(joint[(a,a)] for a in MASKS)/n
    Q=1-same
    G=1-sum(x*x for x in pi)
    return dict(Q=Q,G=G,K=Q-G,pi=pi)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bits",type=int,default=18)
    ap.add_argument("--dmax",type=int,default=255)
    ap.add_argument("--out-dir",default="lab12_out")
    args=ap.parse_args()

    limit=1<<args.bits
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)

    ps=primes(limit)
    pairs=[]
    for i,p in enumerate(ps):
        if p*p>=limit: break
        for q in ps[i+1:]:
            if p*q>=limit: break
            if p>args.dmax and q>args.dmax:
                pairs.append((p,q))

    rows=[]
    strata_rows=[]

    for wi,D in enumerate(fundamental_discriminants(args.dmax),1):
        B,C=world(D)

        joint=Counter(); directed=Counter()
        sj=defaultdict(Counter); sd=defaultdict(Counter); sn=Counter()

        for p,q in pairs:
            cp=jacobi(D,p); cq=jacobi(D,q)
            x=mask(p,q,B,C,D); y=mask(q,p,B,C,D)

            joint[(x,y)] += 1
            directed[x]+=1; directed[y]+=1

            if cp==1 and cq==1: s="++"
            elif cp==-1 and cq==-1: s="--"
            else: s="+-"

            sj[s][(x,y)] += 1
            sd[s][x]+=1; sd[s][y]+=1
            sn[s]+=1

        total=metrics(joint,directed,len(pairs))

        kwithin=0.0
        hetero=0.0
        # pooled pi must equal weighted stratum pis
        for s in ("++","+-","--"):
            ms=metrics(sj[s],sd[s],sn[s])
            w=sn[s]/len(pairs)
            kwithin += w*ms["K"]
            for a in MASKS:
                hetero += w*(ms["pi"][a]-total["pi"][a])**2

            strata_rows.append({
                "world":f"D{D:+d}",
                "D":D,
                "stratum":s,
                "pairs":sn[s],
                "weight":w,
                "Q":ms["Q"],
                "G":ms["G"],
                "K":ms["K"],
                **{f"pi{a}":ms["pi"][a] for a in MASKS},
            })

        identity=total["K"]-(kwithin-hetero)

        row={
            "world":f"D{D:+d}",
            "D":D,
            "torsion_control":int(D in (-3,-4)),
            "pairs":len(pairs),
            "Q":total["Q"],
            "G":total["G"],
            "K":total["K"],
            "K_within":kwithin,
            "H_char":hetero,
            "identity_error":abs(identity),
            "heterogeneity_share_of_negative_K":(
                hetero/(-total["K"]) if total["K"]<0 else 0.0
            ),
            "residual_ratio":(
                abs(kwithin)/abs(total["K"]) if total["K"]!=0 else 0.0
            ),
        }
        rows.append(row)

        if wi%25==0:
            print("progress",wi)

    nont=[r for r in rows if not r["torsion_control"]]
    neg=sorted([r for r in nont if r["K"]<0],key=lambda r:r["K"])
    pos=sorted([r for r in nont if r["K"]>0],key=lambda r:r["K"],reverse=True)

    with (out/"character_coupling.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        wr.writeheader(); wr.writerows(rows)

    with (out/"character_strata.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(strata_rows[0].keys()))
        wr.writeheader(); wr.writerows(strata_rows)

    checks={
        "max_identity_error":max(r["identity_error"] for r in rows),
        "negative_worlds":len(neg),
        "positive_worlds":len(pos),
        "mean_Hchar":sum(r["H_char"] for r in nont)/len(nont),
        "mean_abs_Kwithin":sum(abs(r["K_within"]) for r in nont)/len(nont),
        "mean_abs_K":sum(abs(r["K"]) for r in nont)/len(nont),
        "negative_worlds_Hchar_ge_half_absK":sum(
            r["H_char"]>=0.5*(-r["K"]) for r in neg
        ),
        "negative_worlds_Hchar_ge_absK":sum(
            r["H_char"]>=(-r["K"]) for r in neg
        ),
    }

    payload={
        "bits":args.bits,
        "dmax":args.dmax,
        "pairs":len(pairs),
        "worlds":len(rows),
        "checks":checks,
        "most_negative":neg[:15],
        "most_positive":pos[:15],
    }
    (out/"character_coupling.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")

    md=[
        "# H21-LAB-12 · Character-stratified coupling",
        "",
        f"bits={args.bits}, |D|<={args.dmax}, common-core pairs={len(pairs)}, worlds={len(rows)}.",
        "",
        f"Maximum decomposition error: **{checks['max_identity_error']:.3e}**.",
        "",
        f"Negative-K non-torsion worlds: **{checks['negative_worlds']}**.",
        "",
        f"Positive-K non-torsion worlds: **{checks['positive_worlds']}**.",
        "",
        f"Mean H_char: **{checks['mean_Hchar']:.6f}**.",
        "",
        f"Mean |K_within|: **{checks['mean_abs_Kwithin']:.6f}**.",
        "",
        f"Mean |K|: **{checks['mean_abs_K']:.6f}**.",
        "",
        f"Negative worlds with H_char >= 0.5|K|: **{checks['negative_worlds_Hchar_ge_half_absK']} / {len(neg)}**.",
        "",
        f"Negative worlds with H_char >= |K|: **{checks['negative_worlds_Hchar_ge_absK']} / {len(neg)}**.",
        "",
        "## Most negative K",
        "",
        "| world | K | K_within | H_char | H_char/|K| |",
        "|---|---:|---:|---:|---:|",
    ]
    for r in neg[:15]:
        md.append(
            f"| {r['world']} | {r['K']:+.6f} | {r['K_within']:+.6f} | "
            f"{r['H_char']:.6f} | {r['heterogeneity_share_of_negative_K']:.3f} |"
        )

    md += [
        "",
        "## Most positive K",
        "",
        "| world | K | K_within | H_char |",
        "|---|---:|---:|---:|",
    ]
    for r in pos[:10]:
        md.append(
            f"| {r['world']} | {r['K']:+.6f} | {r['K_within']:+.6f} | {r['H_char']:.6f} |"
        )

    md += [
        "",
        "## Exact interpretation",
        "",
        "K = K_within - H_char. Character-mixture heterogeneity is always a negative contribution; the residual K_within is the coupling left after controlling for split/inert type.",
    ]
    (out/"H21_LAB12_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print("\n".join(md))

    if checks["max_identity_error"]>1e-12:
        raise SystemExit(2)
    print("PASS: character-stratified coupling theorem validated")


if __name__=="__main__":
    main()
