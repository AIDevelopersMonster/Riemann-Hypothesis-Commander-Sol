#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,math
from collections import Counter,defaultdict
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
    a=(1,0);b=(0,1)
    while e:
        if e&1:a=mul(a,b,n,B,C)
        b=mul(b,b,n,B,C);e>>=1
    return a

def trip(m,p,B,C):
    xm=pow_x(m,p,B,C);u=xm[1]%p
    up=mul(xm,(0,1),p,B,C)[1]%p
    um1=((up-B*u)*pow(C%p,-1,p))%p
    return um1,u,up

def mask(p,q,B,C,D):
    cp=jacobi(D,p);cq=jacobi(D,q)
    um1,u,up=trip(q,p,B,C)
    z1=(u-cq)%p==0
    if cp==1:z0=(C*um1-((1-cq)//2)*B)%p==0
    else:z0=(up-B*((1+cq)//2))%p==0
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
    if chi==1:
        bound=p-1;fac=factors(bound,small)
    else:
        bound=p*p-1;fac=factors(p-1,small)
        for r,e in factors(p+1,small).items():fac[r]+=e
    h=bound
    for r in sorted(fac):
        while h%r==0 and pow_x(h//r,p,B,C)==(1,0):h//=r
    return h

def metr(rs):
    n=len(rs)
    if not n:return dict(n=0,same=0,Q=0,G=0,K=0)
    d=Counter();j=Counter()
    for r in rs:
        d[r["x"]]+=1;d[r["y"]]+=1;j[(r["x"],r["y"])]+=1
    pi=[d[z]/(2*n) for z in range(4)]
    same=sum(j[(z,z)] for z in range(4))/n
    Q=1-same;G=1-sum(v*v for v in pi)
    return dict(n=n,same=same,Q=Q,G=G,K=Q-G)

def bucket_g(g):
    if g<=2:return "trivial<=2"
    if g<=4:return "3-4"
    if g<=8:return "5-8"
    if g<=16:return "9-16"
    if g<=32:return "17-32"
    return ">32"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bits",type=int,default=18)
    ap.add_argument("--dmax",type=int,default=255)
    ap.add_argument("--out-dir",default="lab14_out")
    a=ap.parse_args()
    limit=1<<a.bits
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    ps=plist(limit);small=[p for p in ps if p*p<=limit+1]
    odds=[p for p in ps if p>=3]
    pairs=[];used=set()
    for i,p in enumerate(odds):
        if p*p>=limit:break
        for q in odds[i+1:]:
            if p*q>=limit:break
            if p>a.dmax and q>a.dmax:
                pairs.append((p,q));used|={p,q}

    rows=[];bucket_rows=[]
    eq_recip_mismatches=0;opp_neg_mismatches=0

    for wi,D in enumerate(fdiscs(a.dmax),1):
        if D in (-3,-4):continue
        B,C=world(D)
        h={p:order_x(p,B,C,D,small) for p in used}
        by=defaultdict(list)
        for p,q in pairs:
            cp=jacobi(D,p);cq=jacobi(D,q)
            s="++" if cp==cq==1 else "--" if cp==cq==-1 else "+-"
            x=mask(p,q,B,C,D);y=mask(q,p,B,C,D)
            g=math.gcd(h[p],h[q])
            eq=(p-q)%g==0;recip=(p*q-1)%g==0
            opp=(p+q)%g==0;neg=(p*q+1)%g==0
            eq_recip_mismatches+=int(eq!=recip)
            opp_neg_mismatches+=int(opp!=neg)
            if g<=2:lock="trivial"
            elif recip:lock="plus"
            elif neg:lock="minus"
            else:lock="other"
            r=dict(p=p,q=q,x=x,y=y,g=g,lock=lock,bucket=bucket_g(g))
            by[(s,lock)].append(r);by[(s,"all")].append(r)

        for s in ("++","+-","--"):
            mall=metr(by[(s,"all")])
            for lock in ("trivial","plus","minus","other"):
                m=metr(by[(s,lock)])
                rows.append({
                    "world":f"D{D:+d}","D":D,"stratum":s,"lock":lock,
                    "n":m["n"],"fraction":m["n"]/mall["n"] if mall["n"] else 0,
                    "same":m["same"],"K":m["K"],
                    "baseline_same":mall["same"],"baseline_K":mall["K"],
                    "same_lift":m["same"]-mall["same"] if m["n"] else 0,
                    "K_shift":m["K"]-mall["K"] if m["n"] else 0,
                })
            buckets=defaultdict(list)
            for r in by[(s,"all")]:buckets[r["bucket"]].append(r)
            for b,rs in buckets.items():
                m=metr(rs)
                bucket_rows.append({
                    "world":f"D{D:+d}","D":D,"stratum":s,"g_bucket":b,
                    "n":m["n"],"same":m["same"],"K":m["K"],
                    "baseline_same":mall["same"],"same_lift":m["same"]-mall["same"],
                })
        if wi%25==0:print("progress",wi)

    def summary(lock):
        rs=[r for r in rows if r["lock"]==lock and r["n"]>=5]
        return {
            "rows":len(rs),
            "mean_fraction":sum(r["fraction"] for r in rs)/len(rs) if rs else 0,
            "mean_same_lift":sum(r["same_lift"] for r in rs)/len(rs) if rs else 0,
            "positive_lift_fraction":sum(r["same_lift"]>0 for r in rs)/len(rs) if rs else 0,
            "mean_K_shift":sum(r["K_shift"] for r in rs)/len(rs) if rs else 0,
        }

    summaries={k:summary(k) for k in ("trivial","plus","minus","other")}
    with (out/"nontrivial_clock_locks.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
    with (out/"clock_g_buckets.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(bucket_rows[0].keys()));w.writeheader();w.writerows(bucket_rows)

    payload={"bits":a.bits,"dmax":a.dmax,"pairs":len(pairs),
             "eq_recip_mismatches":eq_recip_mismatches,
             "opp_neg_mismatches":opp_neg_mismatches,
             "summaries":summaries}
    (out/"nontrivial_clock_lock.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")

    md=["# H21-LAB-14 · Nontrivial shared-clock locks","",
        f"bits={a.bits}, |D|<={a.dmax}, common-core pairs={len(pairs)}.","",
        f"eq versus pq=+1 mismatches: **{eq_recip_mismatches}**.","",
        f"opp versus pq=-1 mismatches: **{opp_neg_mismatches}**.",""]
    for lock in ("trivial","plus","minus","other"):
        s=summaries[lock]
        md += [f"## {lock}","",
               f"rows >=5: **{s['rows']}**.","",
               f"mean fraction: **{s['mean_fraction']:.6%}**.","",
               f"mean same-mask lift: **{s['mean_same_lift']:+.6f}**.","",
               f"positive-lift fraction: **{s['positive_lift_fraction']:.6%}**.","",
               f"mean K shift: **{s['mean_K_shift']:+.6f}**.",""]
    (out/"H21_LAB14_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print("\n".join(md))
    if eq_recip_mismatches or opp_neg_mismatches:raise SystemExit(2)
    print("PASS: nontrivial clock locks classified")

if __name__=="__main__":main()
