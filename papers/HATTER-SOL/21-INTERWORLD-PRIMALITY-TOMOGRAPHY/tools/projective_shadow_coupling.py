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


def local_mask(p,q,B,C,D):
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


def local_geometry(p,B,C,D,h,e):
    d=h//e
    lam=pow_x(e,p,B,C)
    if lam[1]%p!=0:
        raise AssertionError(("lambda",D,p,h,e,lam))
    lam0=lam[0]%p
    scalars=set()
    v=1
    for _ in range(d):
        scalars.add(v)
        v=(v*lam0)%p
    if len(scalars)!=d:
        raise AssertionError(("scalar size",D,p,h,e,d,len(scalars)))
    return d,scalars


def projective_code(p,B,C,D,e,scalars,sigma,r):
    cp=jacobi(D,p)
    y=pow_x(r,p,B,C)
    a,b=y

    forced=0
    support=0

    # Bit 1: b = sigma, always nonzero affine level.
    ell=b%p
    c=sigma%p
    if ell!=0 and (c*pow(ell,-1,p))%p in scalars:
        support|=2

    # Bit 0.
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
    else:
        if ell0!=0 and (c0*pow(ell0,-1,p))%p in scalars:
            support|=1

    return forced,support


def metrics(records):
    n=len(records)
    if n==0:
        return {"K":0.0,"pi":[0.0]*4}
    d=Counter();j=Counter()
    for x,y in records:
        d[x]+=1;d[y]+=1;j[(x,y)]+=1
    pi=[d[z]/(2*n) for z in range(4)]
    Q=1-sum(j[(z,z)] for z in range(4))/n
    G=1-sum(v*v for v in pi)
    return {"K":Q-G,"pi":pi}


def decompose(allrs, strata):
    mt=metrics(allrs)
    n=len(allrs)
    kw=0.0
    hetero=0.0
    for rs in strata.values():
        if not rs:continue
        ms=metrics(rs)
        w=len(rs)/n
        kw+=w*ms["K"]
        for z in range(4):
            hetero+=w*(ms["pi"][z]-mt["pi"][z])**2
    return mt["K"],kw,hetero,abs(mt["K"]-(kw-hetero))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bits",type=int,default=18)
    ap.add_argument("--dmax",type=int,default=127)
    ap.add_argument("--out-dir",default="lab18_out")
    a=ap.parse_args()

    limit=1<<a.bits
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    ps=plist(limit)
    small=ps
    odds=[p for p in ps if p>=3]

    pairs=[];used=set()
    for i,p in enumerate(odds):
        if p*p>=limit:break
        for q in odds[i+1:]:
            if p*q>=limit:break
            if p>a.dmax and q>a.dmax:
                pairs.append((p,q));used|={p,q}

    rows=[]
    code_counts=Counter()
    containment_failures=0

    for wi,D in enumerate(fdiscs(a.dmax),1):
        if D in (-3,-4):continue
        B,C=world(D)

        geom={}
        for p in used:
            h=order_x(p,B,C,D,small)
            e=projective_order(p,B,C,D,small)
            if h%e:
                raise AssertionError(("h/e",D,p,h,e))
            d,scalars=local_geometry(p,B,C,D,h,e)
            geom[p]=(h,e,d,scalars)

        bys=defaultdict(list)
        shadow=defaultdict(lambda:defaultdict(list))
        proj=defaultdict(lambda:defaultdict(list))

        for p,q in pairs:
            cp=jacobi(D,p);cq=jacobi(D,q)
            s="++" if cp==cq==1 else "--" if cp==cq==-1 else "+-"

            x=local_mask(p,q,B,C,D)
            y=local_mask(q,p,B,C,D)

            hp,ep,dp,Sp=geom[p]
            hq,eq,dq,Sq=geom[q]

            rp=q%ep
            rq=p%eq

            Fp,Pp=projective_code(p,B,C,D,ep,Sp,cq,rp)
            Fq,Pq=projective_code(q,B,C,D,eq,Sq,cp,rq)

            if (x & Fp)!=Fp or (x | Pp)!=Pp:
                containment_failures+=1
            if (y & Fq)!=Fq or (y | Pq)!=Pq:
                containment_failures+=1

            codep=4*Fp+Pp
            codeq=4*Fq+Pq

            bys[s].append((x,y))
            skey=tuple(sorted((Pp,Pq)))
            pkey=tuple(sorted((codep,codeq)))
            shadow[s][skey].append((x,y))
            proj[s][pkey].append((x,y))
            code_counts[(D,s,codep,codeq)]+=1

        for s in ("++","+-","--"):
            allrs=bys[s]
            if len(allrs)<20:continue
            Ks,KwS,HS,errS=decompose(allrs,shadow[s])
            Ks2,KwP,HP,errP=decompose(allrs,proj[s])
            if abs(Ks-Ks2)>1e-12:
                raise AssertionError(("K mismatch",D,s,Ks,Ks2))

            rows.append({
                "world":f"D{D:+d}",
                "D":D,
                "stratum":s,
                "pairs":len(allrs),
                "K_stratum":Ks,
                "H_shadow":HS,
                "K_within_shadow":KwS,
                "shadow_identity_error":errS,
                "H_projective_code":HP,
                "K_within_projective_code":KwP,
                "projective_identity_error":errP,
                "shadow_share_absK":HS/abs(Ks) if Ks else 0.0,
                "projective_share_absK":HP/abs(Ks) if Ks else 0.0,
                "added_forced_optional_explanation":HP-HS,
            })

        if wi%25==0:print("progress",wi)

    eligible=[r for r in rows if abs(r["K_stratum"])>1e-12]
    neg=[r for r in eligible if r["K_stratum"]<0]

    summary={
        "bits":a.bits,
        "dmax":a.dmax,
        "world_character_rows":len(rows),
        "eligible_rows":len(eligible),
        "negative_rows":len(neg),
        "containment_failures":containment_failures,
        "max_shadow_identity_error":max(r["shadow_identity_error"] for r in rows),
        "max_projective_identity_error":max(r["projective_identity_error"] for r in rows),
        "mean_H_shadow":sum(r["H_shadow"] for r in eligible)/len(eligible),
        "mean_H_projective_code":sum(r["H_projective_code"] for r in eligible)/len(eligible),
        "mean_abs_K":sum(abs(r["K_stratum"]) for r in eligible)/len(eligible),
        "mean_abs_K_within_projective":sum(abs(r["K_within_projective_code"]) for r in eligible)/len(eligible),
        "negative_projective_ge_half_absK":sum(r["H_projective_code"]>=.5*abs(r["K_stratum"]) for r in neg),
        "negative_projective_ge_absK":sum(r["H_projective_code"]>=abs(r["K_stratum"]) for r in neg),
        "negative_shadow_ge_half_absK":sum(r["H_shadow"]>=.5*abs(r["K_stratum"]) for r in neg),
        "mean_added_forced_optional_explanation":sum(r["added_forced_optional_explanation"] for r in eligible)/len(eligible),
    }

    with (out/"projective_shadow_coupling.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        wr.writeheader();wr.writerows(rows)

    payload={
        "summary":summary,
        "top_projective_explained":sorted(
            eligible,key=lambda r:r["projective_share_absK"],reverse=True
        )[:20],
        "largest_projective_residual":sorted(
            eligible,key=lambda r:abs(r["K_within_projective_code"]),reverse=True
        )[:20],
    }
    (out/"projective_shadow_coupling.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")

    md=[
        "# H21-LAB-18 · Projective-shadow coupling decomposition","",
        f"bits={a.bits}, |D|<={a.dmax}.","",
        f"World/character rows: **{summary['world_character_rows']}**.","",
        f"Containment failures F subset Z subset S: **{containment_failures}**.","",
        f"Max shadow identity error: **{summary['max_shadow_identity_error']:.3e}**.","",
        f"Max projective-code identity error: **{summary['max_projective_identity_error']:.3e}**.","",
        f"Mean H_shadow: **{summary['mean_H_shadow']:.6f}**.","",
        f"Mean H_projective_code: **{summary['mean_H_projective_code']:.6f}**.","",
        f"Mean |K_s|: **{summary['mean_abs_K']:.6f}**.","",
        f"Mean |K_within_projective|: **{summary['mean_abs_K_within_projective']:.6f}**.","",
        f"Negative rows with H_projective >= 0.5|K_s|: **{summary['negative_projective_ge_half_absK']} / {summary['negative_rows']}**.","",
        f"Negative rows with H_projective >= |K_s|: **{summary['negative_projective_ge_absK']} / {summary['negative_rows']}**.","",
        f"Negative rows with H_shadow >= 0.5|K_s|: **{summary['negative_shadow_ge_half_absK']} / {summary['negative_rows']}**.","",
        f"Mean added explanation from forced-vs-optional distinction: **{summary['mean_added_forced_optional_explanation']:.6f}**.","",
    ]
    (out/"H21_LAB18_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print("\n".join(md))

    if containment_failures or summary["max_shadow_identity_error"]>1e-12 or summary["max_projective_identity_error"]>1e-12:
        raise SystemExit(2)
    print("PASS: projective-shadow coupling decomposition validated")


if __name__=="__main__":
    main()
