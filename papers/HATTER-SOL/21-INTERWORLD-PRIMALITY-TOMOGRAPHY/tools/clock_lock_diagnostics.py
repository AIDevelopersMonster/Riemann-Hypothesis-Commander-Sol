#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


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


def prime_list(limit):
    isp=bytearray(b"\x01")*(limit+1)
    isp[0:2]=b"\x00\x00"
    for p in range(2,int(limit**0.5)+1):
        if isp[p]:
            st=p*p
            isp[st:limit+1:p]=b"\x00"*(((limit-st)//p)+1)
    return [p for p in range(2,limit+1) if isp[p]], isp


def factor_int(n, small_primes):
    out=Counter()
    x=n
    for p in small_primes:
        if p*p>x: break
        while x%p==0:
            out[p]+=1
            x//=p
    if x>1: out[x]+=1
    return out


def order_x(p,B,C,D,small_primes):
    chi=jacobi(D,p)
    if chi not in (-1,1) or C%p==0:
        return None
    if chi==1:
        bound=p-1
        fac=factor_int(bound,small_primes)
    else:
        fac=factor_int(p-1,small_primes)
        fp=factor_int(p+1,small_primes)
        for r,e in fp.items(): fac[r]+=e
        bound=p*p-1

    h=bound
    one=(1,0)
    for r in sorted(fac):
        while h%r==0 and pow_x(h//r,p,B,C)==one:
            h//=r
    if pow_x(h,p,B,C)!=one:
        raise AssertionError((D,p,h))
    return h


def metrics(records):
    n=len(records)
    if n==0:
        return {"n":0,"same":0.0,"Q":0.0,"G":0.0,"K":0.0}
    joint=Counter((r["x"],r["y"]) for r in records)
    directed=Counter()
    for r in records:
        directed[r["x"]]+=1
        directed[r["y"]]+=1
    pi=[directed[z]/(2*n) for z in range(4)]
    same=sum(joint[(z,z)] for z in range(4))/n
    Q=1-same
    G=1-sum(v*v for v in pi)
    return {"n":n,"same":same,"Q":Q,"G":G,"K":Q-G}


def quantile_cut(values,q):
    if not values: return None
    xs=sorted(values)
    idx=min(len(xs)-1,max(0,int(q*(len(xs)-1))))
    return xs[idx]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bits",type=int,default=18)
    ap.add_argument("--dmax",type=int,default=255)
    ap.add_argument("--out-dir",default="lab13_out")
    args=ap.parse_args()

    limit=1<<args.bits
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)

    plist,isp=prime_list(limit)
    small=[p for p in plist if p*p<=limit+1]
    odd=[p for p in plist if p>=3]

    pairs=[]
    used=set()
    for i,p in enumerate(odd):
        if p*p>=limit: break
        for q in odd[i+1:]:
            if p*q>=limit: break
            if p>args.dmax and q>args.dmax:
                pairs.append((p,q))
                used.add(p); used.add(q)

    world_rows=[]
    stratum_rows=[]
    feature_rows=[]

    for wi,D in enumerate(fundamental_discriminants(args.dmax),1):
        B,C=world(D)
        if D in (-3,-4):
            continue

        h={}
        for p in sorted(used):
            h[p]=order_x(p,B,C,D,small)

        bys=defaultdict(list)
        for p,q in pairs:
            cp=jacobi(D,p); cq=jacobi(D,q)
            if cp==1 and cq==1: s="++"
            elif cp==-1 and cq==-1: s="--"
            else: s="+-"

            x=mask(p,q,B,C,D); y=mask(q,p,B,C,D)
            g=math.gcd(h[p],h[q])
            min_h=min(h[p],h[q])
            shared=(math.log2(g)/math.log2(min_h)) if g>1 and min_h>1 else 0.0

            rec={
                "p":p,"q":q,"x":x,"y":y,"same":int(x==y),
                "g":g,"shared":shared,
                "eq":int((p-q)%g==0),
                "opp":int((p+q)%g==0),
                "recip":int((p*q-1)%g==0),
            }
            bys[s].append(rec)

        total_records=[r for rs in bys.values() for r in rs]
        mt=metrics(total_records)

        wr={
            "world":f"D{D:+d}","D":D,
            "pairs":len(total_records),
            "Q":mt["Q"],"G":mt["G"],"K":mt["K"],
        }

        for s in ("++","+-","--"):
            rs=bys[s]
            ms=metrics(rs)
            wr[f"K_{s}"]=ms["K"]
            wr[f"same_{s}"]=ms["same"]

            shares=[r["shared"] for r in rs]
            q25=quantile_cut(shares,0.25)
            q75=quantile_cut(shares,0.75)
            low=[r for r in rs if r["shared"]<=q25] if q25 is not None else []
            high=[r for r in rs if r["shared"]>=q75] if q75 is not None else []
            ml=metrics(low); mh=metrics(high)

            stratum_rows.append({
                "world":f"D{D:+d}","D":D,"stratum":s,
                "pairs":len(rs),"K":ms["K"],"same":ms["same"],
                "shared_q25":q25 if q25 is not None else 0.0,
                "shared_q75":q75 if q75 is not None else 0.0,
                "low_n":ml["n"],"low_same":ml["same"],"low_K":ml["K"],
                "high_n":mh["n"],"high_same":mh["same"],"high_K":mh["K"],
                "high_minus_low_same":mh["same"]-ml["same"],
                "high_minus_low_K":mh["K"]-ml["K"],
            })

            for feat in ("eq","opp","recip"):
                yes=[r for r in rs if r[feat]]
                no=[r for r in rs if not r[feat]]
                my=metrics(yes); mn=metrics(no)
                feature_rows.append({
                    "world":f"D{D:+d}","D":D,"stratum":s,"feature":feat,
                    "pairs":len(rs),
                    "event_n":len(yes),
                    "event_fraction":len(yes)/len(rs) if rs else 0.0,
                    "event_same":my["same"],"nonevent_same":mn["same"],
                    "same_lift":my["same"]-mn["same"],
                    "event_K":my["K"],"nonevent_K":mn["K"],
                    "K_shift":my["K"]-mn["K"],
                })
        world_rows.append(wr)

        if wi%25==0:
            print("progress",wi)

    neg=sorted(world_rows,key=lambda r:r["K"])[:20]
    pos=sorted(world_rows,key=lambda r:r["K"],reverse=True)[:10]

    def summarize_feature(feat):
        rows=[r for r in feature_rows if r["feature"]==feat and r["event_n"]>=5]
        if not rows:
            return {}
        return {
            "rows_with_at_least_5_events":len(rows),
            "mean_event_fraction":sum(r["event_fraction"] for r in rows)/len(rows),
            "mean_same_lift":sum(r["same_lift"] for r in rows)/len(rows),
            "median_same_lift":sorted(r["same_lift"] for r in rows)[len(rows)//2],
            "positive_same_lift_fraction":sum(r["same_lift"]>0 for r in rows)/len(rows),
            "mean_K_shift":sum(r["K_shift"] for r in rows)/len(rows),
        }

    highlow=[r for r in stratum_rows if r["pairs"]>=20]
    summary={
        "worlds":len(world_rows),
        "pairs":len(pairs),
        "eq":summarize_feature("eq"),
        "opp":summarize_feature("opp"),
        "recip":summarize_feature("recip"),
        "shared_order_quartile_rows":len(highlow),
        "mean_high_minus_low_same":(
            sum(r["high_minus_low_same"] for r in highlow)/len(highlow) if highlow else 0.0
        ),
        "positive_high_minus_low_same_fraction":(
            sum(r["high_minus_low_same"]>0 for r in highlow)/len(highlow) if highlow else 0.0
        ),
        "mean_high_minus_low_K":(
            sum(r["high_minus_low_K"] for r in highlow)/len(highlow) if highlow else 0.0
        ),
    }

    with (out/"clock_lock_worlds.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(world_rows[0].keys()))
        wr.writeheader(); wr.writerows(world_rows)

    with (out/"clock_lock_strata.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(stratum_rows[0].keys()))
        wr.writeheader(); wr.writerows(stratum_rows)

    with (out/"clock_lock_features.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(feature_rows[0].keys()))
        wr.writeheader(); wr.writerows(feature_rows)

    payload={
        "bits":args.bits,"dmax":args.dmax,
        "worlds":len(world_rows),"pairs":len(pairs),
        "summary":summary,
        "most_negative_K":neg,
        "most_positive_K":pos,
        "top_eq_lifts":sorted(
            [r for r in feature_rows if r["feature"]=="eq" and r["event_n"]>=5],
            key=lambda r:r["same_lift"],reverse=True
        )[:20],
        "top_shared_quartile_lifts":sorted(
            highlow,key=lambda r:r["high_minus_low_same"],reverse=True
        )[:20],
    }
    (out/"clock_lock_diagnostics.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")

    md=[
        "# H21-LAB-13 · Fixed-stratum clock-lock diagnostics",
        "",
        f"bits={args.bits}, |D|<={args.dmax}, worlds={len(world_rows)}, common-core pairs={len(pairs)}.",
        "",
        "## Shared-order quartiles",
        "",
        f"Eligible world/stratum rows: **{summary['shared_order_quartile_rows']}**.",
        "",
        f"Mean same-mask lift, high shared-order quartile minus low: **{summary['mean_high_minus_low_same']:+.6f}**.",
        "",
        f"Fraction with positive same-mask lift: **{summary['positive_high_minus_low_same_fraction']:.6%}**.",
        "",
        f"Mean K shift, high minus low: **{summary['mean_high_minus_low_K']:+.6f}**.",
        "",
        "## Simple reciprocal lock events",
        "",
    ]
    for feat in ("eq","opp","recip"):
        s=summary[feat]
        md += [
            f"### {feat}",
            "",
            f"Rows with >=5 events: **{s.get('rows_with_at_least_5_events',0)}**.",
            "",
            f"Mean event frequency: **{s.get('mean_event_fraction',0):.6%}**.",
            "",
            f"Mean same-mask lift: **{s.get('mean_same_lift',0):+.6f}**.",
            "",
            f"Positive-lift fraction: **{s.get('positive_same_lift_fraction',0):.6%}**.",
            "",
            f"Mean conditional K shift: **{s.get('mean_K_shift',0):+.6f}**.",
            "",
        ]

    md += [
        "## Interpretation rule",
        "",
        "A shared-clock mechanism is supported only if same-mask lift is positive and stable across many fixed-stratum rows. Otherwise the full phase-set incidence, not gcd/order alone, is required.",
    ]
    (out/"H21_LAB13_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print("\n".join(md))
    print("PASS: fixed-stratum clock-lock diagnostics completed")


if __name__=="__main__":
    main()
