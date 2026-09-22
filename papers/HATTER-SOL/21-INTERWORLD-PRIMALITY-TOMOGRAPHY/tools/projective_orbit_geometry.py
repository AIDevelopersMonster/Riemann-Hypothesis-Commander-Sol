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


def inv_elem(y,p,B,C):
    # Inverse via brute exponent is sufficient on this small validation grid.
    # y belongs to the unit orbit H.
    # Find using Fermat-size exponent bounds through the orbit order outside.
    raise NotImplementedError


def pow_elem(base,e,n,B,C):
    acc=(1,0)
    cur=base
    while e:
        if e&1:acc=mul(acc,cur,n,B,C)
        cur=mul(cur,cur,n,B,C);e>>=1
    return acc


def pow_x(e,n,B,C):
    return pow_elem((0,1),e,n,B,C)


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


def scalar_phases(p,B,C,h):
    out=[]
    y=(1,0)
    for m in range(h):
        if y[1]%p==0:
            out.append(m)
        y=mul(y,(0,1),p,B,C)
    return out


def tau(y,p,B):
    a,b=y
    return ((a+B*b)%p,(-b)%p)


def projective_ratio_order(p,B,C,h):
    # e is the least positive m with x^m scalar.
    for m in range(1,h+1):
        y=pow_x(m,p,B,C)
        if y[1]%p==0:
            return m
    raise AssertionError


def phase_set(p,B,C,h,ell,c):
    vals=[]
    y=(1,0)
    for m in range(h):
        if ell(y)%p==c%p:
            vals.append(m)
        y=mul(y,(0,1),p,B,C)
    return vals


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--pmax",type=int,default=257)
    ap.add_argument("--dmax",type=int,default=63)
    ap.add_argument("--out-dir",default="lab17_out")
    a=ap.parse_args()

    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    ps=prime_list(a.pmax)
    small=[2]+prime_list(max(512,a.pmax))

    failures=[]
    rows=[]
    pg1_checks=0
    zero_fiber_checks=0
    nonzero_graph_checks=0
    translation_checks=0
    special_fiber_checks=0
    b0_checks=0

    for D in fdiscs(a.dmax):
        if D in (-3,-4):continue
        B,C=world(D)
        for p in ps:
            if math.gcd(p,abs(C*D))!=1:continue
            chi=jacobi(D,p)
            if chi not in (-1,1):continue

            h=order_x(p,B,C,D,small)
            scalars=scalar_phases(p,B,C,h)
            d=len(scalars)
            e=h//d
            e_direct=projective_ratio_order(p,B,C,h)

            pg1_checks+=1
            if e!=e_direct or (p-chi)%e!=0:
                failures.append(("PG1",D,p,h,d,e,e_direct,chi))

            # D=<x^e>; scalar phases must be exactly multiples of e.
            expected_scalars=list(range(0,h,e))
            if scalars!=expected_scalars:
                failures.append(("scalar_fibers",D,p,h,d,e,scalars[:20],expected_scalars[:20]))

            lam=pow_x(e,p,B,C)
            if lam[1]%p!=0:
                failures.append(("lambda_not_scalar",D,p,e,lam))
                continue
            lam0=lam[0]%p

            # Validate both coordinate observer functionals and a third generic linear functional.
            functionals=[
                ("b",lambda y,p=p:y[1]%p),
                ("a",lambda y,p=p:y[0]%p),
                ("a+Bb",lambda y,B=B,p=p:(y[0]+B*y[1])%p),
            ]

            for lname,ell in functionals:
                zeros=phase_set(p,B,C,h,ell,0)
                zero_fiber_checks+=1
                if zeros:
                    r0=zeros[0]%e
                    expected=[r0+k*e for k in range(d)]
                    if zeros!=expected:
                        failures.append(("zero_fiber",D,p,lname,h,d,e,zeros[:30],expected[:30]))

                # Sample nonzero levels c=1 and c=-1.
                phase_sets={}
                for c in (1,p-1):
                    M=phase_set(p,B,C,h,ell,c)
                    phase_sets[c]=M
                    nonzero_graph_checks+=1
                    residues=[m%e for m in M]
                    if len(residues)!=len(set(residues)):
                        failures.append(("not_partial_transversal",D,p,lname,c,h,d,e,M[:30]))

                    # Check exact graph equation through the scalar fiber.
                    for m in M:
                        r=m%e
                        if (m-r)%e!=0:
                            failures.append(("decomp",D,p,m,r,e))
                            continue
                        k=(m-r)//e
                        sr=ell(pow_x(r,p,B,C))%p
                        if sr==0 or (pow(lam0,k,p)*sr-c)%p!=0:
                            failures.append(("graph_equation",D,p,lname,c,m,r,k,sr,lam0))

                # If -1 belongs to D, c=-1 set is h/2 translate of c=1 set.
                if d%2==0:
                    translation_checks+=1
                    shifted=sorted((m+h//2)%h for m in phase_sets[1])
                    target=sorted(phase_sets[p-1])
                    if shifted!=target:
                        failures.append(("minus_translation",D,p,lname,h,d,e,shifted[:30],target[:30]))

            # Special zero observer fiber when the declared zero-level line contains x.
            # Split sigma=+1 constant observer is a=0.
            if chi==1:
                ell0=lambda y,p=p:y[0]%p
                M=phase_set(p,B,C,h,ell0,0)
                special_fiber_checks+=1
                if not M or {m%e for m in M}!={1%e}:
                    failures.append(("split_plus_fiber",D,p,h,d,e,M[:30]))

            # Inert sigma=-1 constant observer is a+B b = 0 and contains tau(x).
            if chi==-1:
                ell0=lambda y,B=B,p=p:(y[0]+B*y[1])%p
                M=phase_set(p,B,C,h,ell0,0)
                special_fiber_checks+=1
                if not M or {m%e for m in M}!={(-1)%e}:
                    failures.append(("inert_minus_fiber",D,p,h,d,e,M[:30]))

            if B==0:
                b0_checks+=1
                if e>2:
                    failures.append(("B0_projective_order",D,p,h,d,e))

            rows.append({
                "D":D,"p":p,"chi":chi,
                "h":h,"d":d,"e":e,
                "compression_factor_d":d,
                "projective_fraction":e/h,
                "B":B,
            })

    with (out/"projective_orbit_geometry.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        wr.writeheader();wr.writerows(rows)

    summary={
        "pmax":a.pmax,"dmax":a.dmax,
        "rows":len(rows),
        "failures":len(failures),
        "failure_examples":failures[:30],
        "PG1_checks":pg1_checks,
        "zero_fiber_checks":zero_fiber_checks,
        "nonzero_graph_checks":nonzero_graph_checks,
        "translation_checks":translation_checks,
        "special_fiber_checks":special_fiber_checks,
        "B0_checks":b0_checks,
        "mean_d":sum(r["d"] for r in rows)/len(rows),
        "median_d":sorted(r["d"] for r in rows)[len(rows)//2],
        "max_d":max(r["d"] for r in rows),
        "mean_e":sum(r["e"] for r in rows)/len(rows),
        "max_e":max(r["e"] for r in rows),
    }
    (out/"projective_orbit_geometry.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")

    md=[
        "# H21-LAB-17 · Projective orbit geometry validation","",
        f"p <= {a.pmax}, |D| <= {a.dmax}.","",
        f"World/prime rows: **{len(rows)}**.","",
        f"Projective-order checks: **{pg1_checks}**.","",
        f"Zero-fiber placement checks: **{zero_fiber_checks}**.","",
        f"Nonzero partial-transversal checks: **{nonzero_graph_checks}**.","",
        f"Minus-level translation checks: **{translation_checks}**.","",
        f"Special +/-1 projective-fiber checks: **{special_fiber_checks}**.","",
        f"B=0 collapse checks: **{b0_checks}**.","",
        f"Failures: **{len(failures)}**.","",
        f"Mean scalar-fiber size d: **{summary['mean_d']:.6f}**.","",
        f"Median d: **{summary['median_d']}**.","",
        f"Max d: **{summary['max_d']}**.","",
        f"Mean projective clock e: **{summary['mean_e']:.6f}**.","",
        f"Max e: **{summary['max_e']}**.","",
    ]
    (out/"H21_LAB17_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print("\n".join(md))
    if failures:
        raise SystemExit(2)
    print("PASS: projective orbit phase-placement theorem validated")


if __name__=="__main__":
    main()
