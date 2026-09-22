#!/usr/bin/env python3
from __future__ import annotations

import argparse, csv, json, math, random
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
        if D%4==1 and squarefree(D):out.append(D)
        elif D%4==0:
            d=D//4
            if d%4 in (2,3) and squarefree(d):out.append(D)
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
    isp=bytearray(b"\x01")*(limit+1);isp[0:2]=b"\x00\x00"
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
    return e


def geometry(p,B,C,D,small):
    h=order_x(p,B,C,D,small)
    e=projective_order(p,B,C,D,small)
    d=h//e
    lam=pow_x(e,p,B,C)
    if lam[1]%p: raise AssertionError(("lambda",D,p,lam))
    lam0=lam[0]%p
    logs={}
    v=1
    for k in range(d):
        logs[v]=k
        v=(v*lam0)%p
    if len(logs)!=d: raise AssertionError(("logs",D,p,d,len(logs)))
    return h,e,d,lam0,logs


def observer_direction(p,m,B,C,D,G,sigma):
    h,e,d,lam,logs=G
    phase=m%h
    r=phase%e
    k=((phase-r)//e)%d
    y=pow_x(r,p,B,C)
    a,b=y
    cp=jacobi(D,p)

    forced=0
    support=0
    targets={}

    ell=b%p; c=sigma%p
    if ell:
        t=(c*pow(ell,-1,p))%p
        if t in logs:
            support|=2
            targets[1]=logs[t]

    if cp==1:
        ell0=a%p
        c0=(((1-sigma)//2)*B)%p
    else:
        ell0=(a+B*b)%p
        c0=(B*((1+sigma)//2))%p

    if c0==0:
        if ell0==0:
            forced|=1;support|=1
    elif ell0:
        t=(c0*pow(ell0,-1,p))%p
        if t in logs:
            support|=1
            targets[0]=logs[t]

    mask=forced
    for bit,kstar in targets.items():
        if k==kstar: mask|=(1<<bit)

    even=(d%2==0)
    s=d//2 if even else d
    beta=(k//s) if even else None

    target_info={}
    for bit,kstar in targets.items():
        if even:
            beta_star=kstar//s
            k0=k%s
            ks0=kstar%s
            norm_compatible=(k0==ks0)
            gamma=(beta^beta_star) if norm_compatible else None
            target_info[bit]=(beta_star,norm_compatible,gamma)
        else:
            target_info[bit]=(None,k==kstar,None)

    return {
        "mask":mask,"forced":forced,"support":support,
        "targets":targets,"target_info":target_info,
        "h":h,"e":e,"d":d,"r":r,"k":k,
        "even":even,"s":s,"beta":beta,
    }


def bernoulli_stats(rs):
    n=len(rs)
    if not n:return {}
    px=sum(r["hit_p"] for r in rs)/n
    py=sum(r["hit_q"] for r in rs)/n
    pxy=sum(r["hit_p"]*r["hit_q"] for r in rs)/n
    cov=pxy-px*py
    same=sum(r["hit_p"]==r["hit_q"] for r in rs)/n
    return dict(n=n,px=px,py=py,pxy=pxy,cov=cov,same=same)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bits",type=int,default=18)
    ap.add_argument("--dmax",type=int,default=127)
    ap.add_argument("--out-dir",default="lab21_out")
    a=ap.parse_args()

    limit=1<<a.bits
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    ps=plist(limit); odds=[p for p in ps if p>=3]; small=ps

    pairs=[];used=set()
    for i,p in enumerate(odds):
        if p*p>=limit:break
        for q in odds[i+1:]:
            if p*q>=limit:break
            if p>a.dmax and q>a.dmax:
                pairs.append((p,q));used|={p,q}

    failures=[]
    rows=[]
    exact_binary_checks=0
    odd_no_bit_checks=0

    for wi,D in enumerate(fdiscs(a.dmax),1):
        if D in (-3,-4):continue
        B,C=world(D)
        GG={p:geometry(p,B,C,D,small) for p in used}

        for p,q in pairs:
            cp=jacobi(D,p); cq=jacobi(D,q)
            sclass="++" if cp==cq==1 else "--" if cp==cq==-1 else "+-"
            P=observer_direction(p,q,B,C,D,GG[p],cq)
            Q=observer_direction(q,p,B,C,D,GG[q],cp)

            for data in (P,Q):
                if not data["even"]:
                    odd_no_bit_checks+=1
                    if data["beta"] is not None:
                        failures.append(("odd_beta",D,p,q,data["d"],data["beta"]))
                for bit,kstar in data["targets"].items():
                    if data["even"]:
                        exact_binary_checks+=1
                        beta_star,norm_compatible,gamma=data["target_info"][bit]
                        direct=(data["k"]==kstar)
                        binary=(norm_compatible and data["beta"]==beta_star)
                        if direct!=binary:
                            failures.append(("binary_equiv",D,p,q,bit,data["k"],kstar,data["d"]))

            # Restrict primary binary-coupling analysis to directions with
            # exactly one optional target, both even fibers, and norm compatibility.
            if len(P["targets"])==1 and len(Q["targets"])==1 and P["even"] and Q["even"]:
                bitp=next(iter(P["targets"]))
                bitq=next(iter(Q["targets"]))
                bstar_p,ncomp_p,gamma_p=P["target_info"][bitp]
                bstar_q,ncomp_q,gamma_q=Q["target_info"][bitq]
                if ncomp_p and ncomp_q:
                    hit_p=int(P["beta"]==bstar_p)
                    hit_q=int(Q["beta"]==bstar_q)
                    rows.append({
                        "world":f"D{D:+d}","D":D,"stratum":sclass,
                        "p":p,"q":q,
                        "bit_p":bitp,"bit_q":bitq,
                        "dp":P["d"],"dq":Q["d"],
                        "sp":P["s"],"sq":Q["s"],
                        "beta_p":P["beta"],"beta_q":Q["beta"],
                        "beta_star_p":bstar_p,"beta_star_q":bstar_q,
                        "gamma_p":gamma_p,"gamma_q":gamma_q,
                        "hit_p":hit_p,"hit_q":hit_q,
                        "same_beta":int(P["beta"]==Q["beta"]),
                        "same_gamma":int(gamma_p==gamma_q),
                        "same_bit_label":int(bitp==bitq),
                    })

        if wi%25==0:print("progress",wi)

    grouped=defaultdict(list)
    for r in rows:
        # Fix world, character, optional bit labels, and parity target-adjustment type.
        key=(r["world"],r["stratum"],r["bit_p"],r["bit_q"])
        grouped[key].append(r)

    stats=[]
    for key,rs in grouped.items():
        if len(rs)<20:continue
        st=bernoulli_stats(rs)
        shuf_covs=[]
        # deterministic pseudo-shuffle control
        vals=[r["hit_q"] for r in rs]
        for shift in (1,3,7,11,17):
            if len(vals)<=shift:continue
            shifted=vals[shift:]+vals[:shift]
            px=sum(r["hit_p"] for r in rs)/len(rs)
            py=sum(shifted)/len(rs)
            pxy=sum(r["hit_p"]*y for r,y in zip(rs,shifted))/len(rs)
            shuf_covs.append(pxy-px*py)
        stats.append({
            "world":key[0],"stratum":key[1],
            "bit_p":key[2],"bit_q":key[3],
            **st,
            "mean_shift_control_cov":sum(shuf_covs)/len(shuf_covs) if shuf_covs else 0.0,
            "same_gamma_fraction":sum(r["same_gamma"] for r in rs)/len(rs),
            "same_beta_fraction":sum(r["same_beta"] for r in rs)/len(rs),
        })

    summary={
        "bits":a.bits,"dmax":a.dmax,
        "failures":len(failures),"failure_examples":failures[:30],
        "exact_binary_checks":exact_binary_checks,
        "odd_no_bit_checks":odd_no_bit_checks,
        "eligible_binary_pairs":len(rows),
        "groups_n_ge20":len(stats),
        "mean_abs_cov":sum(abs(r["cov"]) for r in stats)/len(stats) if stats else 0.0,
        "max_abs_cov":max(abs(r["cov"]) for r in stats) if stats else 0.0,
        "mean_abs_shift_control_cov":sum(abs(r["mean_shift_control_cov"]) for r in stats)/len(stats) if stats else 0.0,
        "positive_cov_groups":sum(r["cov"]>0 for r in stats),
        "negative_cov_groups":sum(r["cov"]<0 for r in stats),
        "mean_same_gamma_fraction":sum(r["same_gamma_fraction"] for r in stats)/len(stats) if stats else 0.0,
    }

    with (out/"binary_lift_pairs.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0].keys()) if rows else ["world"])
        wr.writeheader();wr.writerows(rows)
    with (out/"binary_lift_group_stats.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(stats[0].keys()) if stats else ["world"])
        wr.writeheader();wr.writerows(stats)
    (out/"binary_lift_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")

    md=[
        "# H21-LAB-21 · Binary lift observer and reciprocal coupling","",
        f"bits={a.bits}, |D|<={a.dmax}.","",
        f"Exact binary observer checks: **{exact_binary_checks}**.","",
        f"Odd-fiber no-bit checks: **{odd_no_bit_checks}**.","",
        f"Failures: **{len(failures)}**.","",
        f"Eligible reciprocal even/even one-target norm-compatible pairs: **{len(rows)}**.","",
        f"Groups with n>=20: **{len(stats)}**.","",
        f"Mean |binary hit covariance|: **{summary['mean_abs_cov']:.6f}**.","",
        f"Max |binary hit covariance|: **{summary['max_abs_cov']:.6f}**.","",
        f"Mean |shift-control covariance|: **{summary['mean_abs_shift_control_cov']:.6f}**.","",
        f"Positive-covariance groups: **{summary['positive_cov_groups']}**.","",
        f"Negative-covariance groups: **{summary['negative_cov_groups']}**.","",
        f"Mean same target-adjusted lift-bit fraction: **{summary['mean_same_gamma_fraction']:.6%}**.","",
    ]
    (out/"H21_LAB21_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print("\n".join(md))
    if failures:raise SystemExit(2)
    print("PASS: binary lift observer theorem validated")


if __name__=="__main__":
    main()
