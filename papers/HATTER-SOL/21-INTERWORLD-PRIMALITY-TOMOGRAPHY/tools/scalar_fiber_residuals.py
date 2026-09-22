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
    if n==0:return False
    p=2
    while p*p<=n:
        if n%(p*p)==0:return False
        p+=1
    return True


def fdiscs(dmax):
    out=[]
    for D in range(-dmax,dmax+1):
        if D in (0,1):continue
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
    a%=n;o=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5):o=-o
        a,n=n,a
        if a%4==3 and n%4==3:o=-o
        a%=n
    return o if n==1 else 0


def mul(u,v,n,B,C):
    a,b=u;c,d=v
    return ((a*c+b*d*C)%n,(a*d+b*c+b*d*B)%n)


def pow_x(e,n,B,C):
    acc=(1,0);base=(0,1)
    while e:
        if e&1:acc=mul(acc,base,n,B,C)
        base=mul(base,base,n,B,C);e>>=1
    return acc


def plist(limit):
    isp=bytearray(b"\x01")*(limit+1)
    isp[0:2]=b"\x00\x00"
    for p in range(2,int(limit**0.5)+1):
        if isp[p]:
            st=p*p
            isp[st:limit+1:p]=b"\x00"*(((limit-st)//p)+1)
    return [p for p in range(2,limit+1) if isp[p]]


def factors(n,ps):
    c=Counter();x=n
    for p in ps:
        if p*p>x:break
        while x%p==0:
            c[p]+=1;x//=p
    if x>1:c[x]+=1
    return c


def order_x(p,B,C,D,small):
    chi=jacobi(D,p)
    if chi==1:
        bound=p-1;fac=factors(bound,small)
    else:
        bound=p*p-1;fac=factors(p-1,small)
        for r,e in factors(p+1,small).items():fac[r]+=e
    h=bound
    for r in sorted(fac):
        while h%r==0 and pow_x(h//r,p,B,C)==(1,0):
            h//=r
    return h


def projective_order(p,B,C,D,small):
    chi=jacobi(D,p)
    e=p-chi
    fac=factors(e,small)
    for r in sorted(fac):
        while e%r==0 and pow_x(e//r,p,B,C)[1]%p==0:
            e//=r
    if pow_x(e,p,B,C)[1]%p!=0:
        raise AssertionError(("projective order",D,p,e))
    return e


def geometry(p,B,C,D,small):
    h=order_x(p,B,C,D,small)
    e=projective_order(p,B,C,D,small)
    if h%e:
        raise AssertionError(("h/e",D,p,h,e))
    d=h//e
    lam=pow_x(e,p,B,C)
    if lam[1]%p:
        raise AssertionError(("lambda",D,p,lam))
    lam0=lam[0]%p
    log={}
    v=1
    for k in range(d):
        if v in log:
            raise AssertionError(("duplicate scalar",D,p,d,k))
        log[v]=k
        v=(v*lam0)%p
    return h,e,d,lam0,log


def observer_data(p,m,B,C,D,geom,sigma):
    h,e,d,lam0,log=geom
    phase=m%h
    r=phase%e
    k=((phase-r)//e)%d
    y=pow_x(r,p,B,C)
    a,b=y
    cp=jacobi(D,p)

    forced=0
    support=0
    targets={}

    # bit 1: b=sigma, always nonzero target
    ell=b%p
    c=sigma%p
    if ell:
        t=(c*pow(ell,-1,p))%p
        if t in log:
            support|=2
            targets[1]=log[t]

    # bit 0
    if cp==1:
        ell0=a%p
        c0=(((1-sigma)//2)*B)%p
    else:
        ell0=(a+B*b)%p
        c0=(B*((1+sigma)//2))%p

    if c0==0:
        if ell0==0:
            forced|=1
            support|=1
    elif ell0:
        t=(c0*pow(ell0,-1,p))%p
        if t in log:
            support|=1
            targets[0]=log[t]

    mask=forced
    residuals={}
    for bit,kstar in targets.items():
        u=(k-kstar)%d
        residuals[bit]=u
        if u==0:
            mask|=(1<<bit)

    return {
        "mask":mask,"forced":forced,"support":support,
        "targets":targets,"residuals":residuals,
        "r":r,"k":k,"d":d,"e":e,"h":h,
    }


def direct_mask(p,q,B,C,D):
    cp=jacobi(D,p);cq=jacobi(D,q)
    xm=pow_x(q,p,B,C)
    u=xm[1]%p
    up=mul(xm,(0,1),p,B,C)[1]%p
    um1=((up-B*u)*pow(C%p,-1,p))%p
    z1=(u-cq)%p==0
    if cp==1:
        z0=(C*um1-((1-cq)//2)*B)%p==0
    else:
        z0=(up-B*((1+cq)//2))%p==0
    return (1 if z0 else 0)|(2 if z1 else 0)


def metrics(records):
    n=len(records)
    if not n:return {"same":0.0,"Q":0.0,"G":0.0,"K":0.0}
    directed=Counter()
    joint=Counter()
    for r in records:
        directed[r["x"]]+=1;directed[r["y"]]+=1
        joint[(r["x"],r["y"])]+=1
    pi=[directed[z]/(2*n) for z in range(4)]
    same=sum(joint[(z,z)] for z in range(4))/n
    Q=1-same
    G=1-sum(v*v for v in pi)
    return {"same":same,"Q":Q,"G":G,"K":Q-G}


def summarize_lock(rows,field):
    eligible=[r for r in rows if r["one_one"] and r["gd"]>1]
    groups=defaultdict(list)
    for r in eligible:
        groups[(r["world"],r["stratum"],r[field])].append(r)
    out=[]
    for key,rs in groups.items():
        if len(rs)<5:continue
        m=metrics(rs)
        out.append((key,len(rs),m))
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bits",type=int,default=18)
    ap.add_argument("--dmax",type=int,default=127)
    ap.add_argument("--out-dir",default="lab19_out")
    a=ap.parse_args()

    limit=1<<a.bits
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    ps=plist(limit)
    odds=[p for p in ps if p>=3]
    small=ps

    pairs=[];used=set()
    for i,p in enumerate(odds):
        if p*p>=limit:break
        for q in odds[i+1:]:
            if p*q>=limit:break
            if p>a.dmax and q>a.dmax:
                pairs.append((p,q));used|={p,q}

    failures=[]
    rows=[]
    direction_optional_counts=Counter()
    target_collision_checks=0

    for wi,D in enumerate(fdiscs(a.dmax),1):
        if D in (-3,-4):continue
        B,C=world(D)
        G={p:geometry(p,B,C,D,small) for p in used}

        for p,q in pairs:
            cp=jacobi(D,p);cq=jacobi(D,q)
            s="++" if cp==cq==1 else "--" if cp==cq==-1 else "+-"

            xp=observer_data(p,q,B,C,D,G[p],cq)
            xq=observer_data(q,p,B,C,D,G[q],cp)

            dx=direct_mask(p,q,B,C,D)
            dy=direct_mask(q,p,B,C,D)
            if xp["mask"]!=dx:
                failures.append(("mask_p",D,p,q,xp["mask"],dx))
            if xq["mask"]!=dy:
                failures.append(("mask_q",D,p,q,xq["mask"],dy))

            op=len(xp["targets"])
            oq=len(xq["targets"])
            direction_optional_counts[op]+=1
            direction_optional_counts[oq]+=1

            # SF3: two optional targets collide only on distinguished projective ray.
            for prime,other,data,sigma in ((p,q,xp,cq),(q,p,xq,cp)):
                if len(data["targets"])==2:
                    target_collision_checks+=1
                    vals=list(data["targets"].values())
                    if vals[0]==vals[1]:
                        expected=(1 if sigma==1 else -1)%data["e"]
                        if data["r"]!=expected:
                            failures.append(("target_collision_ray",D,prime,other,sigma,data["r"],data["e"],vals))

            gd=math.gcd(xp["d"],xq["d"])
            one_one=(op==1 and oq==1)
            up=uq=None
            eq=opp=False
            both_gzero=False
            if one_one:
                up=next(iter(xp["residuals"].values()))
                uq=next(iter(xq["residuals"].values()))
                if gd>1:
                    eq=(up-uq)%gd==0
                    opp=(up+uq)%gd==0
                    both_gzero=(up%gd==0 and uq%gd==0)

            rows.append({
                "world":f"D{D:+d}","D":D,"stratum":s,
                "p":p,"q":q,"x":xp["mask"],"y":xq["mask"],
                "optional_p":op,"optional_q":oq,
                "one_one":int(one_one),
                "dp":xp["d"],"dq":xq["d"],"gd":gd,
                "up":-1 if up is None else up,
                "uq":-1 if uq is None else uq,
                "u_eq_mod_g":int(eq),
                "u_opp_mod_g":int(opp),
                "both_u_zero_mod_g":int(both_gzero),
                "exact_both_optional_hit":int(
                    one_one and up==0 and uq==0
                ),
            })

        if wi%25==0:print("progress",wi)

    # Global one-one diagnostics.
    oo=[r for r in rows if r["one_one"]]
    oo_g=[r for r in oo if r["gd"]>1]
    base=metrics(oo)

    def event_summary(name,pred):
        yes=[r for r in oo_g if pred(r)]
        no=[r for r in oo_g if not pred(r)]
        my=metrics(yes);mn=metrics(no)
        return {
            "name":name,
            "eligible":len(oo_g),
            "event_n":len(yes),
            "event_fraction":len(yes)/len(oo_g) if oo_g else 0.0,
            "event_same":my["same"],
            "nonevent_same":mn["same"],
            "same_lift":my["same"]-mn["same"],
            "event_K":my["K"],
            "nonevent_K":mn["K"],
            "K_shift":my["K"]-mn["K"],
        }

    events=[
        event_summary("u_eq_mod_g",lambda r:r["u_eq_mod_g"]),
        event_summary("u_opp_mod_g",lambda r:r["u_opp_mod_g"]),
        event_summary("both_u_zero_mod_g",lambda r:r["both_u_zero_mod_g"]),
    ]

    # How concentrated is the remaining projective-code residual in optional-count classes?
    optpair=defaultdict(list)
    for r in rows:
        key=tuple(sorted((r["optional_p"],r["optional_q"])))
        optpair[key].append(r)
    optstats=[]
    for key,rs in sorted(optpair.items()):
        m=metrics(rs)
        optstats.append({
            "optional_pair":str(key),
            "n":len(rs),
            "fraction":len(rs)/len(rows),
            "same":m["same"],"K":m["K"],
        })

    # Exact Bernoulli covariance for one-one optional-hit events.
    # For one optional bit per direction and fixed bit labels, a hit is u=0.
    hit_cov_groups=[]
    grouped=defaultdict(list)
    for r in oo:
        # Actual optional-bit label can be inferred from mask/projective code only
        # with more metadata; here group by world/character to avoid claiming exact
        # mask equivalence from hit indicators alone.
        grouped[(r["world"],r["stratum"])].append(r)
    for key,rs in grouped.items():
        if len(rs)<20:continue
        ax=[int(r["up"]==0) for r in rs]
        ay=[int(r["uq"]==0) for r in rs]
        ex=sum(ax)/len(rs);ey=sum(ay)/len(rs)
        exy=sum(a*b for a,b in zip(ax,ay))/len(rs)
        hit_cov_groups.append({
            "world":key[0],"stratum":key[1],"n":len(rs),
            "P_hit_p":ex,"P_hit_q":ey,"P_both":exy,
            "hit_covariance":exy-ex*ey,
        })

    summary={
        "bits":a.bits,"dmax":a.dmax,
        "rows":len(rows),
        "failures":len(failures),
        "failure_examples":failures[:30],
        "target_collision_checks":target_collision_checks,
        "optional_direction_counts":dict(direction_optional_counts),
        "one_one_pairs":len(oo),
        "one_one_fraction":len(oo)/len(rows),
        "one_one_gd_gt1":len(oo_g),
        "one_one_baseline_same":base["same"],
        "one_one_baseline_K":base["K"],
        "events":events,
        "mean_abs_hit_covariance":(
            sum(abs(r["hit_covariance"]) for r in hit_cov_groups)/len(hit_cov_groups)
            if hit_cov_groups else 0.0
        ),
        "max_abs_hit_covariance":(
            max(abs(r["hit_covariance"]) for r in hit_cov_groups)
            if hit_cov_groups else 0.0
        ),
    }

    with (out/"scalar_fiber_residuals.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        wr.writeheader();wr.writerows(rows)

    with (out/"optional_pair_stats.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(optstats[0].keys()))
        wr.writeheader();wr.writerows(optstats)

    with (out/"one_one_hit_covariance.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(hit_cov_groups[0].keys()))
        wr.writeheader();wr.writerows(hit_cov_groups)

    (out/"scalar_fiber_residuals.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")

    md=[
        "# H21-LAB-19 · Scalar-fiber normalized residuals","",
        f"bits={a.bits}, |D|<={a.dmax}.","",
        f"Directional-pair rows: **{len(rows)}**.","",
        f"Exact reconstruction failures: **{len(failures)}**.","",
        f"Two-target collision theorem checks: **{target_collision_checks}**.","",
        f"One-optional / one-optional pairs: **{len(oo)} ({len(oo)/len(rows):.6%})**.","",
        f"One-one pairs with gcd(d_p,d_q)>1: **{len(oo_g)}**.","",
        f"Mean absolute optional-hit covariance by world/character: **{summary['mean_abs_hit_covariance']:.6f}**.","",
        f"Max absolute optional-hit covariance: **{summary['max_abs_hit_covariance']:.6f}**.","",
        "## Shared scalar modulus diagnostics","",
    ]
    for ev in events:
        md += [
            f"### {ev['name']}","",
            f"event fraction: **{ev['event_fraction']:.6%}**.","",
            f"same-mask lift: **{ev['same_lift']:+.6f}**.","",
            f"K shift: **{ev['K_shift']:+.6f}**.","",
        ]
    md += ["## Optional-target count classes",""]
    for r in optstats:
        md.append(
            f"- {r['optional_pair']}: n={r['n']}, fraction={r['fraction']:.6%}, K={r['K']:+.6f}"
        )

    (out/"H21_LAB19_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print("\n".join(md))
    if failures:
        raise SystemExit(2)
    print("PASS: scalar-fiber single-coordinate theorem validated")


if __name__=="__main__":
    main()
