#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,math
from collections import Counter,defaultdict
from pathlib import Path

def squarefree(n):
    n=abs(n)
    if not n:return False
    p=2
    while p*p<=n:
        if n%(p*p)==0:return False
        p+=1
    return True

def fdiscs(dm):
    o=[]
    for D in range(-dm,dm+1):
        if D in (0,1):continue
        if D%4==1 and squarefree(D):o.append(D)
        elif D%4==0:
            d=D//4
            if d%4 in (2,3) and squarefree(d):o.append(D)
    return o

def world(D):return (1,(D-1)//4) if D%4==1 else (0,D//4)

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

def px(e,n,B,C):
    a=(1,0);b=(0,1)
    while e:
        if e&1:a=mul(a,b,n,B,C)
        b=mul(b,b,n,B,C);e>>=1
    return a

def primes(N):
    z=bytearray(b"\x01")*(N+1);z[0:2]=b"\x00\x00"
    for p in range(2,int(N**.5)+1):
        if z[p]:
            st=p*p;z[st:N+1:p]=b"\x00"*(((N-st)//p)+1)
    return [p for p in range(2,N+1) if z[p]]

def fac(n,ps):
    c=Counter();x=n
    for p in ps:
        if p*p>x:break
        while x%p==0:c[p]+=1;x//=p
    if x>1:c[x]+=1
    return c

def ordx(p,B,C,D,ps):
    ch=jacobi(D,p)
    if ch==1:b=p-1;f=fac(b,ps)
    else:
        b=p*p-1;f=fac(p-1,ps)
        for r,e in fac(p+1,ps).items():f[r]+=e
    h=b
    for r in sorted(f):
        while h%r==0 and px(h//r,p,B,C)==(1,0):h//=r
    return h

def orde(p,B,C,D,ps):
    e=p-jacobi(D,p);f=fac(e,ps)
    for r in sorted(f):
        while e%r==0 and px(e//r,p,B,C)[1]%p==0:e//=r
    return e

def geom(p,B,C,D,ps):
    h=ordx(p,B,C,D,ps);e=orde(p,B,C,D,ps);d=h//e
    la=px(e,p,B,C)[0]%p
    logs={};v=1
    for k in range(d):logs[v]=k;v=v*la%p
    return h,e,d,la,logs

def obs(p,m,B,C,D,G,sig):
    h,e,d,la,logs=G;m%=h;r=m%e;k=(m-r)//e;y=px(r,p,B,C);a,b=y
    cp=jacobi(D,p);targets={}
    if b%p:
        t=sig*pow(b%p,-1,p)%p
        if t in logs:targets[1]=logs[t]
    if cp==1:el=a%p;c=((1-sig)//2)*B%p
    else:el=(a+B*b)%p;c=B*((1+sig)//2)%p
    if c and el:
        t=c*pow(el,-1,p)%p
        if t in logs:targets[0]=logs[t]
    even=d%2==0;s=d//2 if even else d
    out=[]
    for bit,ks in targets.items():
        if even:
            k0=k%s;ks0=ks%s;nc=k0==ks0
            if nc:
                bp=k//s;bs=ks//s
                out.append((bit,bp,bs,bp^bs,s%2))
    return d,e,targets,out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--bits",type=int,default=20);ap.add_argument("--dmax",type=int,default=63);ap.add_argument("--out-dir",default="lab22")
    a=ap.parse_args();N=1<<a.bits;out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    ps=primes(N);odd=[p for p in ps if p>=3]
    pairs=[];used=set()
    for i,p in enumerate(odd):
        if p*p>=N:break
        for q in odd[i+1:]:
            if p*q>=N:break
            if p>a.dmax and q>a.dmax:pairs.append((p,q));used|={p,q}
    rows=[];fail=0
    for wi,D in enumerate(fdiscs(a.dmax),1):
        if D in (-3,-4):continue
        B,C=world(D);G={p:geom(p,B,C,D,ps) for p in used}
        for p,q in pairs:
            cp=jacobi(D,p);cq=jacobi(D,q);sc="++" if cp==cq==1 else "--" if cp==cq==-1 else "+-"
            dp,ep,tp,op=obs(p,q,B,C,D,G[p],cq);dq,eq,tq,oq=obs(q,p,B,C,D,G[q],cp)
            # exactly one norm-compatible optional target each
            if len(op)==1 and len(oq)==1:
                bp=op[0];bq=oq[0]
                rows.append({"world":f"D{D:+d}","D":D,"stratum":sc,"p":p,"q":q,
                    "bit_p":bp[0],"bit_q":bq[0],"gamma_p":bp[3],"gamma_q":bq[3],
                    "sp_parity":bp[4],"sq_parity":bq[4],
                    "hit_p":int(bp[3]==0),"hit_q":int(bq[3]==0),
                    "same_gamma":int(bp[3]==bq[3])})
        if wi%20==0:print("progress",wi)
    groups=defaultdict(list)
    for r in rows:
        key=(r["world"],r["stratum"],r["bit_p"],r["bit_q"],r["sp_parity"],r["sq_parity"])
        groups[key].append(r)
    stats=[]
    for key,rs in groups.items():
        if len(rs)<10:continue
        n=len(rs);pxx=sum(x["hit_p"] for x in rs)/n;pyy=sum(x["hit_q"] for x in rs)/n
        pxy=sum(x["hit_p"]*x["hit_q"] for x in rs)/n;cov=pxy-pxx*pyy
        ctr=[]
        ys=[x["hit_q"] for x in rs]
        for sh in (1,3,7,11):
            if n<=sh:continue
            yy=ys[sh:]+ys[:sh];ctr.append(sum(x["hit_p"]*y for x,y in zip(rs,yy))/n-pxx*(sum(yy)/n))
        stats.append({"world":key[0],"stratum":key[1],"bit_p":key[2],"bit_q":key[3],
            "sp_parity":key[4],"sq_parity":key[5],"n":n,"cov":cov,
            "control_cov":sum(ctr)/len(ctr) if ctr else 0,
            "same_gamma":sum(x["same_gamma"] for x in rs)/n,
            "P_hit_p":pxx,"P_hit_q":pyy,"P_both":pxy})
    summ={"bits":a.bits,"dmax":a.dmax,"eligible_pairs":len(rows),"groups_ge10":len(stats),
        "groups_ge20":sum(x["n"]>=20 for x in stats),
        "mean_abs_cov":sum(abs(x["cov"]) for x in stats)/len(stats) if stats else 0,
        "mean_abs_control":sum(abs(x["control_cov"]) for x in stats)/len(stats) if stats else 0,
        "max_abs_cov":max([abs(x["cov"]) for x in stats],default=0),
        "positive":sum(x["cov"]>0 for x in stats),"negative":sum(x["cov"]<0 for x in stats)}
    with (out/"lift_stats.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(stats[0].keys()) if stats else ["world"]);w.writeheader();w.writerows(stats)
    (out/"summary.json").write_text(json.dumps(summ,indent=2))
    print("# H21-LAB-22 · Expanded binary-lift statistics")
    for k,v in summ.items():print(f"{k}: **{v}**")
if __name__=="__main__":main()
