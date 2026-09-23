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


def order_fp(a,p,small):
    a%=p
    if a==0:return None
    h=p-1
    fac=factors(h,small)
    for r in sorted(fac):
        while h%r==0 and pow(a,h//r,p)==1:
            h//=r
    return h


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
    if lam[1]%p:
        raise AssertionError(("lambda",D,p,lam))
    lam0=lam[0]%p
    t=order_fp((-C)%p,p,small)
    s=t//math.gcd(t,e)
    return h,e,d,lam0,t,s


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--pmax",type=int,default=509)
    ap.add_argument("--dmax",type=int,default=127)
    ap.add_argument("--out-dir",default="lab20_out")
    a=ap.parse_args()

    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    ps=[p for p in plist(a.pmax) if p>=3]
    small=plist(max(a.pmax,1024))
    if 2 not in small:small=[2]+small

    rows=[]
    failures=[]
    odd_count=even_count=double_count=0
    norm_checks=0
    odd_reconstruct_checks=0

    for D in fdiscs(a.dmax):
        if D in (-3,-4):continue
        B,C=world(D)
        for p in ps:
            if math.gcd(p,abs(C*D))!=1:continue
            chi=jacobi(D,p)
            if chi not in (-1,1):continue

            h,e,d,lam,t,s=geometry(p,B,C,D,small)

            if d not in (s,2*s):
                failures.append(("d_options",D,p,h,e,d,t,s))
            if d==s and s%2==0:
                failures.append(("even_s_single",D,p,d,s))
            if d%2==0:
                even_count+=1
                if d!=2*s:
                    failures.append(("even_double",D,p,d,s))
                if pow(lam,s,p)!=(p-1)%p:
                    failures.append(("lambda_s",D,p,lam,s,pow(lam,s,p)))
                double_count+=1
            else:
                odd_count+=1
                if d!=s:
                    failures.append(("odd_equal",D,p,d,s))

            if (lam*lam-pow((-C)%p,e,p))%p!=0:
                failures.append(("norm_square_generator",D,p,e,lam,C))

            # Validate incoming exponent samples through all residue phases m mod h.
            # Keep grid finite by sampling deterministic phase representatives.
            samples={0,1,h-1,h//2,e,(2*e)%h,(3*e+1)%h}
            for m in sorted(x%h for x in samples):
                r=m%e
                k=((m-r)//e)%d
                z=pow(lam,k,p)
                norm_checks+=1
                if (z*z-pow((-C)%p,m-r,p))%p!=0:
                    failures.append(("norm_phase",D,p,m,r,k,z))
                if d%2==1:
                    odd_reconstruct_checks+=1
                    rhs=pow((-C)%p,m-r,p)
                    zrec=pow(rhs,(d+1)//2,p)
                    if zrec!=z:
                        failures.append(("odd_reconstruct",D,p,m,r,k,z,zrec,d))

            rows.append({
                "D":D,"p":p,"chi":chi,
                "h":h,"e":e,"d":d,
                "t_order_minusC":t,
                "s_norm_order":s,
                "double_cover":int(d==2*s),
                "d_odd":int(d%2==1),
                "compression_h_to_e":d,
            })

    with (out/"norm_lift_geometry.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        wr.writeheader();wr.writerows(rows)

    summary={
        "pmax":a.pmax,"dmax":a.dmax,
        "rows":len(rows),"failures":len(failures),
        "failure_examples":failures[:30],
        "odd_d":odd_count,"even_d":even_count,
        "odd_fraction":odd_count/len(rows),
        "even_fraction":even_count/len(rows),
        "double_cover_count":double_count,
        "norm_phase_checks":norm_checks,
        "odd_reconstruct_checks":odd_reconstruct_checks,
        "mean_d":sum(r["d"] for r in rows)/len(rows),
        "mean_s":sum(r["s_norm_order"] for r in rows)/len(rows),
        "mean_e":sum(r["e"] for r in rows)/len(rows),
        "B0_rows":sum(1 for r in rows if r["D"]%4==0),
        "B1_rows":sum(1 for r in rows if r["D"]%4==1),
    }
    (out/"norm_lift_geometry.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")

    md=[
        "# H21-LAB-20 · Norm-lift / double-cover validation","",
        f"p <= {a.pmax}, |D| <= {a.dmax}.","",
        f"World/prime rows: **{len(rows)}**.","",
        f"Failures: **{len(failures)}**.","",
        f"Odd d_p rows: **{odd_count} ({summary['odd_fraction']:.6%})**.","",
        f"Even d_p rows: **{even_count} ({summary['even_fraction']:.6%})**.","",
        f"d_p=2s_p checks: **{double_count}**.","",
        f"Norm phase checks: **{norm_checks}**.","",
        f"Odd-fiber exact scalar reconstructions: **{odd_reconstruct_checks}**.","",
        f"Mean d_p: **{summary['mean_d']:.6f}**.","",
        f"Mean s_p: **{summary['mean_s']:.6f}**.","",
        f"Mean e_p: **{summary['mean_e']:.6f}**.","",
    ]
    (out/"H21_LAB20_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print("\n".join(md))
    if failures:raise SystemExit(2)
    print("PASS: norm-lift / double-cover theorem validated")


if __name__=="__main__":
    main()
