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
        while x%p==0:
            c[p]+=1;x//=p
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


def projective_order(p,B,C,D,small):
    chi=jacobi(D,p)
    e=p-chi
    fac=factor_int(e,small)
    for r in sorted(fac):
        while e%r==0 and pow_x(e//r,p,B,C)[1]%p==0:
            e//=r
    return e


def v2(n):
    a=0
    while n%2==0:
        n//=2;a+=1
    return a,n


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--pmax",type=int,default=509)
    ap.add_argument("--dmax",type=int,default=127)
    ap.add_argument("--out-dir",default="lab29_out")
    args=ap.parse_args()

    out=Path(args.out_dir);out.mkdir(parents=True,exist_ok=True)
    ps=prime_list(args.pmax)
    small=[2]+prime_list(max(1024,args.pmax))

    rows=[]
    failures=[]
    checks=0
    lift_checks=0
    exponent_checks=0
    a_hist=Counter()

    for D in fdiscs(args.dmax):
        if D in (-3,-4):continue
        B,C=world(D)

        for p in ps:
            if math.gcd(p,abs(C*D))!=1:continue
            chi=jacobi(D,p)
            if chi not in (-1,1):continue

            h=order_x(p,B,C,D,small)
            e=projective_order(p,B,C,D,small)
            if h%e:
                failures.append(("h%e",D,p,h,e))
                continue
            d=h//e
            if d%2:
                continue

            a,u=v2(d)
            a_hist[a]+=1

            lam=pow_x(e,p,B,C)
            if lam[1]%p!=0:
                failures.append(("lambda",D,p,e,lam))
                continue
            lam0=lam[0]%p

            omega=pow(lam0,u,p)

            checks+=1
            # omega must have exact order 2^a.
            if pow(omega,1<<a,p)!=1:
                failures.append(("omega_order_upper",D,p,d,a,u,omega))
            if a>0 and pow(omega,1<<(a-1),p)==1:
                failures.append(("omega_order_exact",D,p,d,a,u,omega))

            # Validate the whole scalar subgroup exponent-by-exponent.
            for k in range(d):
                z=pow(lam0,k,p)
                eta=pow(z,u,p)
                expected=pow(omega,k,p)
                exponent_checks+=1
                if eta!=expected:
                    failures.append(("eta_exp",D,p,d,k,eta,expected))

                z2=(z*z)%p
                zneg=(-z)%p
                lift_checks+=1

                if (zneg*zneg)%p!=z2:
                    failures.append(("same_square",D,p,k,z,zneg))
                if pow(zneg,u,p)!=(-eta)%p:
                    failures.append(("antipode",D,p,k,eta,pow(zneg,u,p)))

                # Partner exponent differs by d/2.
                kp=(k+d//2)%d
                zp=pow(lam0,kp,p)
                if zp!=zneg:
                    failures.append(("partner",D,p,d,k,kp,z,zp,zneg))

                # 2-primary exponent coordinates differ only in top bit.
                mod=1<<a
                k2=k%mod
                kp2=kp%mod
                lowmask=(1<<(a-1))-1 if a>1 else 0
                if (k2 & lowmask)!=(kp2 & lowmask):
                    failures.append(("lowbits",D,p,d,a,k,kp,k2,kp2))
                if ((k2>>(a-1))&1)==((kp2>>(a-1))&1):
                    failures.append(("topbit",D,p,d,a,k,kp,k2,kp2))

                # Squared 2-primary projection forgets exactly the top bit.
                if pow(eta,2,p)!=pow(pow(zp,u,p),2,p):
                    failures.append(("eta_square",D,p,k,kp))

            rows.append({
                "D":D,"p":p,"chi":chi,
                "h":h,"e":e,"d":d,
                "v2_d":a,"odd_part_u":u,
                "omega":omega,
                "two_primary_order":1<<a,
            })

    with (out/"two_primary_lift.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        wr.writeheader();wr.writerows(rows)

    summary={
        "pmax":args.pmax,
        "dmax":args.dmax,
        "even_fiber_rows":len(rows),
        "checks":checks,
        "exponent_checks":exponent_checks,
        "lift_checks":lift_checks,
        "failures":len(failures),
        "failure_examples":failures[:30],
        "v2_d_histogram":dict(sorted(a_hist.items())),
        "max_v2_d":max(a_hist) if a_hist else 0,
    }
    (out/"two_primary_lift.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")

    md=[
        "# H21-LAB-29 · 2-primary lift-character validation","",
        f"p <= {args.pmax}, |D| <= {args.dmax}.","",
        f"Even-fiber local rows: **{len(rows)}**.","",
        f"2-primary subgroup checks: **{checks}**.","",
        f"Scalar exponent checks: **{exponent_checks}**.","",
        f"Norm-lift antipode checks: **{lift_checks}**.","",
        f"Maximum v2(d): **{summary['max_v2_d']}**.","",
        f"Failures: **{len(failures)}**.","",
        "## v2(d) histogram","",
    ]
    for a,n in sorted(a_hist.items()):
        md.append(f"- a={a}: {n}")

    (out/"H21_LAB29_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print("\n".join(md))

    if failures:
        raise SystemExit(2)
    print("PASS: 2-primary lift theorem validated")


if __name__=="__main__":
    main()
