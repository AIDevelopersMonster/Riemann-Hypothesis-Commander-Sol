#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter
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


def prime_list(limit):
    isp=bytearray(b"\x01")*(limit+1)
    isp[0:2]=b"\x00\x00"
    for p in range(2,int(limit**0.5)+1):
        if isp[p]:
            st=p*p
            isp[st:limit+1:p]=b"\x00"*(((limit-st)//p)+1)
    return [p for p in range(3,limit+1,2) if isp[p]]


def factor_int(n,ps):
    c=Counter();x=n
    for p in ps:
        if p*p>x:break
        while x%p==0:c[p]+=1;x//=p
    if x>1:c[x]+=1
    return c


def order_x(p,B,C,D,small):
    chi=jacobi(D,p)
    if chi==1:
        bound=p-1;fac=factor_int(bound,small)
    else:
        bound=p*p-1;fac=factor_int(p-1,small)
        for r,e in factor_int(p+1,small).items():fac[r]+=e
    h=bound
    for r in sorted(fac):
        while h%r==0 and pow_x(h//r,p,B,C)==(1,0):
            h//=r
    return h


def scalar_part_by_enumeration(p,B,C,h):
    pts=[]
    y=(1,0)
    for m in range(h):
        if y[1]%p==0 and y[0]%p!=0:
            pts.append(y[0]%p)
        y=mul(y,(0,1),p,B,C)
    return set(pts)


def roots_mod_p(B,C,p):
    roots=[]
    for r in range(p):
        if (r*r-B*r-C)%p==0:
            roots.append(r)
    return roots


def order_fp(a,p,small):
    if a%p==0:return None
    h=p-1
    fac=factor_int(p-1,small)
    for r in sorted(fac):
        while h%r==0 and pow(a,h//r,p)==1:
            h//=r
    return h


def line_counts_and_masks(p,B,C,D,h,sigma):
    chi_p=jacobi(D,p)
    N0=N1=full_direct=0
    mask_counts=Counter()

    y=(1,0)
    target=(0,1) if sigma==1 else (B%p,(-1)%p)

    for m in range(h):
        a,b=y
        z1=(b-sigma)%p==0
        if chi_p==1:
            rhs=((1-sigma)//2)*B
            z0=(a-rhs)%p==0
        else:
            rhs=((1+sigma)//2)*B
            z0=(a+B*b-rhs)%p==0

        if z0:N0+=1
        if z1:N1+=1
        if z0 and z1:full_direct+=1

        mask=(1 if z0 else 0)|(2 if z1 else 0)
        mask_counts[mask]+=1
        y=mul(y,(0,1),p,B,C)

    f=1 if target in orbit_set(p,B,C,h) else 0
    predicted={
        3:f,
        1:N0-f,
        2:N1-f,
        0:h-N0-N1+f,
    }
    return N0,N1,full_direct,f,mask_counts,predicted


def orbit_set(p,B,C,h):
    s=set()
    y=(1,0)
    for _ in range(h):
        s.add(y)
        y=mul(y,(0,1),p,B,C)
    return s


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--pmax",type=int,default=257)
    ap.add_argument("--dmax",type=int,default=63)
    ap.add_argument("--out-dir",default="lab16_out")
    a=ap.parse_args()

    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    ps=prime_list(a.pmax)
    small=prime_list(max(a.pmax,512))

    rows=[]
    failures=[]
    zero_level_checks=0
    nonzero_bound_checks=0
    full_checks=0
    mask_formula_checks=0
    scalar_formula_checks=0

    for D in fdiscs(a.dmax):
        if D in (-3,-4):
            continue
        B,C=world(D)
        for p in ps:
            if math.gcd(p,abs(C*D))!=1:
                continue
            chi=jacobi(D,p)
            if chi not in (-1,1):
                continue

            h=order_x(p,B,C,D,small)
            scalars=scalar_part_by_enumeration(p,B,C,h)
            d=len(scalars)

            if chi==-1:
                dpred=math.gcd(h,p-1)
            else:
                roots=roots_mod_p(B,C,p)
                if len(roots)!=2 or 0 in roots:
                    failures.append(("roots",D,p,roots))
                    continue
                r,s=roots
                ratio=(r*pow(s,-1,p))%p
                ord_ratio=order_fp(ratio,p,small)
                dpred=h//ord_ratio

            scalar_formula_checks+=1
            if d!=dpred:
                failures.append(("d_formula",D,p,h,d,dpred,chi))

            # Validate arbitrary linear levels by using the two actual observer
            # functionals for both incoming signs.
            for sigma in (1,-1):
                N0,N1,full_direct,f,mask_counts,predicted=line_counts_and_masks(
                    p,B,C,D,h,sigma
                )

                full_checks+=1
                if full_direct!=f or full_direct not in (0,1):
                    failures.append(("full",D,p,sigma,full_direct,f))

                mask_formula_checks+=1
                for z in range(4):
                    if mask_counts[z]!=predicted[z]:
                        failures.append(("mask_formula",D,p,sigma,z,mask_counts[z],predicted[z]))

                # z1 line is always nonzero level b=sigma.
                nonzero_bound_checks+=1
                if N1>min(p,h//d):
                    failures.append(("N1_bound",D,p,sigma,h,d,N1))

                # z0 level may be zero or nonzero.
                chi_p=chi
                if chi_p==1:
                    c0=((1-sigma)//2)*B
                else:
                    c0=((1+sigma)//2)*B

                if c0%p==0:
                    zero_level_checks+=1
                    if N0 not in (0,d):
                        failures.append(("N0_zero",D,p,sigma,h,d,N0))
                else:
                    nonzero_bound_checks+=1
                    if N0>min(p,h//d):
                        failures.append(("N0_bound",D,p,sigma,h,d,N0))

                rows.append({
                    "D":D,"p":p,"chi_p":chi,"sigma":sigma,
                    "h":h,"d":d,"h_over_d":h//d,
                    "N0":N0,"N1":N1,"full":f,
                    "mask_empty":mask_counts[0],
                    "mask_z0":mask_counts[1],
                    "mask_z1":mask_counts[2],
                    "mask_full":mask_counts[3],
                    "N0_fraction":N0/h,
                    "N1_fraction":N1/h,
                })

    with (out/"orbit_line_incidence.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        wr.writeheader();wr.writerows(rows)

    summary={
        "pmax":a.pmax,
        "dmax":a.dmax,
        "rows":len(rows),
        "failures":len(failures),
        "failure_examples":failures[:30],
        "scalar_formula_checks":scalar_formula_checks,
        "zero_level_checks":zero_level_checks,
        "nonzero_bound_checks":nonzero_bound_checks,
        "full_checks":full_checks,
        "mask_formula_checks":mask_formula_checks,
        "max_N1_fraction":max(r["N1_fraction"] for r in rows),
        "max_N0_fraction":max(r["N0_fraction"] for r in rows),
        "max_h_over_d":max(r["h_over_d"] for r in rows),
        "min_d":min(r["d"] for r in rows),
        "max_d":max(r["d"] for r in rows),
    }
    (out/"orbit_line_incidence.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")

    md=[
        "# H21-LAB-16 · Scalar-coset orbit/line incidence validation","",
        f"p <= {a.pmax}, |D| <= {a.dmax}.","",
        f"World/prime/sign rows: **{len(rows)}**.","",
        f"Scalar-subgroup formula checks: **{scalar_formula_checks}**.","",
        f"Zero-level checks: **{zero_level_checks}**.","",
        f"Nonzero-line bound checks: **{nonzero_bound_checks}**.","",
        f"Full-mask one-point checks: **{full_checks}**.","",
        f"Exact mask-count formula checks: **{mask_formula_checks}**.","",
        f"Failures: **{len(failures)}**.","",
        f"Maximum observed N1/h: **{summary['max_N1_fraction']:.6f}**.","",
        f"Maximum observed N0/h: **{summary['max_N0_fraction']:.6f}**.","",
        "## Acceptance rule","",
        "The theorem layer is implementation-validated iff all failure counts are zero."
    ]
    (out/"H21_LAB16_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print("\n".join(md))
    if failures:
        raise SystemExit(2)
    print("PASS: scalar-coset incidence theorem validated")

if __name__=="__main__":
    main()
