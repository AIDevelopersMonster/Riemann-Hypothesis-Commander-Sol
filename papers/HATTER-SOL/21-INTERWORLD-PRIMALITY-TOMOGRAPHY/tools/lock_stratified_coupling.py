#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,math
from collections import Counter,defaultdict
from pathlib import Path

# Reuse the exact arithmetic core from LAB-14 in compact form.
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

def world(D): return (1,(D-1)//4) if D%4==1 else (0,D//4)

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
    a=(1,0);b=(0,1)
    while e:
        if e&1:a=mul(a,b,n,B,C)
        b=mul(b,b,n,B,C);e>>=1
    return a

def trip(m,p,B,C):
    xm=pow_x(m,p,B,C);u=xm[1]%p
    up=mul(xm,(0,1),p,B,C)[1]%p
    return ((up-B*u)*pow(C%p,-1,p))%p,u,up

def mask(p,q,B,C,D):
    cp=jacobi(D,p);cq=jacobi(D,q)
    um1,u,up=trip(q,p,B,C)
    z1=(u-cq)%p==0
    z0=(C*um1-((1-cq)//2)*B)%p==0 if cp==1 else (up-B*((1+cq)//2))%p==0
    return (1 if z0 else 0)|(2 if z1 else 0)

def plist(limit):
    isp=bytearray(b"\x01")*(limit+1);isp[0:2]=b"\x00\x00"
    for p in range(2,int(limit**.5)+1):
        if isp[p]:
            st=p*p
            isp[st:limit+1:p]=b"\x00"*(((limit-st)//p)+1)
    return [p for p in range(2,limit+1) if isp[p]]

def factors(n,ps):
    c=Counter();x=n
    for p in ps:
        if p*p>x:break
        while x%p==0:c[p]+=1;x//=p
    if x>1:c[x]+=1
    return c

def order_x(p,B,C,D,small):
    chi=jacobi(D,p)
    if chi==1: bound=p-1;fac=factors(bound,small)
    else:
        bound=p*p-1;fac=factors(p-1,small)
        for r,e in factors(p+1,small).items():fac[r]+=e
    h=bound
    for r in sorted(fac):
        while h%r==0 and pow_x(h//r,p,B,C)==(1,0):h//=r
    return h

def metrics(rs):
    n=len(rs)
    if not n:return {"K":0.0,"pi":[0.0]*4}
    d=Counter();j=Counter()
    for x,y in rs:
        d[x]+=1;d[y]+=1;j[(x,y)]+=1
    pi=[d[z]/(2*n) for z in range(4)]
    Q=1-sum(j[(z,z)] for z in range(4))/n
    G=1-sum(v*v for v in pi)
    return {"K":Q-G,"pi":pi}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bits",type=int,default=18)
    ap.add_argument("--dmax",type=int,default=255)
    ap.add_argument("--out-dir",default="lab15_out")
    a=ap.parse_args()

    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    ps=plist(1<<a.bits);small=[p for p in ps if p*p<=(1<<a.bits)+1]
    odds=[p for p in ps if p>=3]
    pairs=[];used=set()
    for i,p in enumerate(odds):
        if p*p>=1<<a.bits:break
        for q in odds[i+1:]:
            if p*q>=1<<a.bits:break
            if p>a.dmax and q>a.dmax:
                pairs.append((p,q));used|={p,q}

    rows=[]
    for wi,D in enumerate(fdiscs(a.dmax),1):
        if D in (-3,-4):continue
        B,C=world(D)
        h={p:order_x(p,B,C,D,small) for p in used}
        data=defaultdict(lambda:defaultdict(list))
        for p,q in pairs:
            cp=jacobi(D,p);cq=jacobi(D,q)
            s="++" if cp==cq==1 else "--" if cp==cq==-1 else "+-"
            x=mask(p,q,B,C,D);y=mask(q,p,B,C,D)
            g=math.gcd(h[p],h[q])
            if g<=2:l="T"
            elif (p*q-1)%g==0:l="+"
            elif (p*q+1)%g==0:l="-"
            else:l="0"
            data[s][l].append((x,y))

        for s in ("++","+-","--"):
            allrs=[xy for l in ("T","+","-","0") for xy in data[s][l]]
            mt=metrics(allrs)
            n=len(allrs)
            kw=0.0
            hetero=0.0
            for l in ("T","+","-","0"):
                rs=data[s][l]
                ml=metrics(rs)
                w=len(rs)/n if n else 0
                kw+=w*ml["K"]
                for z in range(4):
                    hetero+=w*(ml["pi"][z]-mt["pi"][z])**2
            rows.append({
                "world":f"D{D:+d}","D":D,"stratum":s,"pairs":n,
                "K_stratum":mt["K"],
                "K_within_lock":kw,
                "H_lock":hetero,
                "identity_error":abs(mt["K"]-(kw-hetero)),
                "Hlock_share_absK":hetero/abs(mt["K"]) if mt["K"] else 0,
            })
        if wi%25==0:print("progress",wi)

    eligible=[r for r in rows if r["pairs"]>=20 and abs(r["K_stratum"])>1e-12]
    neg=[r for r in eligible if r["K_stratum"]<0]
    summary={
        "rows":len(rows),
        "eligible_rows":len(eligible),
        "max_identity_error":max(r["identity_error"] for r in rows),
        "mean_Hlock":sum(r["H_lock"] for r in eligible)/len(eligible),
        "mean_abs_Kwithin_lock":sum(abs(r["K_within_lock"]) for r in eligible)/len(eligible),
        "mean_abs_Kstratum":sum(abs(r["K_stratum"]) for r in eligible)/len(eligible),
        "negative_rows":len(neg),
        "negative_Hlock_ge_half_absK":sum(r["H_lock"]>=.5*abs(r["K_stratum"]) for r in neg),
        "negative_Hlock_ge_absK":sum(r["H_lock"]>=abs(r["K_stratum"]) for r in neg),
    }

    with (out/"lock_stratified_coupling.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
    (out/"lock_stratified_coupling.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")

    md=["# H21-LAB-15 · Lock-stratified coupling","",
        f"bits={a.bits}, |D|<={a.dmax}, common-core pairs={len(pairs)}.","",
        f"Maximum identity error: **{summary['max_identity_error']:.3e}**.","",
        f"Eligible world/character rows: **{summary['eligible_rows']}**.","",
        f"Mean H_lock: **{summary['mean_Hlock']:.6f}**.","",
        f"Mean |K_within_lock|: **{summary['mean_abs_Kwithin_lock']:.6f}**.","",
        f"Mean |K_stratum|: **{summary['mean_abs_Kstratum']:.6f}**.","",
        f"Negative rows with H_lock >= 0.5|K_s|: **{summary['negative_Hlock_ge_half_absK']} / {summary['negative_rows']}**.","",
        f"Negative rows with H_lock >= |K_s|: **{summary['negative_Hlock_ge_absK']} / {summary['negative_rows']}**.",""]
    (out/"H21_LAB15_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print("\n".join(md))
    if summary["max_identity_error"]>1e-12:raise SystemExit(2)
    print("PASS: lock-stratified coupling theorem validated")

if __name__=="__main__":main()
