#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,math
from collections import Counter
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
    out=[]
    for D in range(-dm,dm+1):
        if D in (0,1):continue
        if D%4==1 and squarefree(D):out.append(D)
        elif D%4==0:
            d=D//4
            if d%4 in (2,3) and squarefree(d):out.append(D)
    return out

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
    return [p for p in range(3,N+1,2) if z[p]]

def exposure(n,B,C,D):
    g=math.gcd(n,abs(2*C*D))
    if 1<g<n:return True
    if g!=1:return False
    j=jacobi(D,n)
    if j not in (-1,1):return False
    y=px(n,n,B,C);want=(0,1) if j==1 else (B%n,(-1)%n)
    for d in ((y[0]-want[0])%n,(y[1]-want[1])%n):
        gg=math.gcd(n,d)
        if 1<gg<n:return True
    return False

def semiprimes(ps,lo,hi,cut):
    vals=[]
    for i,p in enumerate(ps):
        if p*p>=hi:break
        for q in ps[i+1:]:
            n=p*q
            if n>=hi:break
            if p<=cut or q<=cut:continue
            if n>=lo:vals.append(n)
    return vals

def greedy(worlds,E,pop,K):
    U=set(pop);rem=set(worlds);s=[]
    for _ in range(K):
        b=max(rem,key=lambda D:(len(E[D]&U),len(E[D]),-abs(D)))
        s.append(b);U-=E[b];rem.remove(b)
    return s

def individual(worlds,E,K):
    return sorted(worlds,key=lambda D:(len(E[D]),-abs(D)),reverse=True)[:K]

def eval_sched(s,E,pop,K):
    costs=[];rank={n:None for n in pop};seen=set();curve=[]
    for i,D in enumerate(s[:K],1):
        new=E[D]-seen
        for n in new:
            if n in rank and rank[n] is None:rank[n]=i
        seen |= E[D]
        cov=sum(v is not None for v in rank.values())
        curve.append(cov/len(pop))
    for n in pop:costs.append(rank[n] if rank[n] is not None else K+1)
    return {
      "coverage":sum(v is not None for v in rank.values())/len(pop),
      "capped_mean_cost":sum(costs)/len(costs),
      "curve":curve
    }

def spearman(x,y):
    def ranks(v):
        order=sorted(range(len(v)),key=lambda i:v[i]);r=[0]*len(v);i=0
        while i<len(order):
            j=i+1
            while j<len(order) and v[order[j]]==v[order[i]]:j+=1
            rr=(i+1+j)/2
            for k in range(i,j):r[order[k]]=rr
            i=j
        return r
    a=ranks(x);b=ranks(y);ma=sum(a)/len(a);mb=sum(b)/len(b)
    num=sum((u-ma)*(v-mb) for u,v in zip(a,b))
    den=math.sqrt(sum((u-ma)**2 for u in a)*sum((v-mb)**2 for v in b))
    return num/den if den else 0

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--dmax",type=int,default=127);ap.add_argument("--K",type=int,default=20);ap.add_argument("--out-dir",default="lab24")
    a=ap.parse_args();out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    ps=primes(1<<18);train=semiprimes(ps,0,1<<17,a.dmax);test=semiprimes(ps,1<<17,1<<18,a.dmax)
    worlds=[D for D in fdiscs(a.dmax) if D not in (-3,-4)]
    ET={};EV={}
    for wi,D in enumerate(worlds,1):
        B,C=world(D);ET[D]={n for n in train if exposure(n,B,C,D)};EV[D]={n for n in test if exposure(n,B,C,D)}
        if wi%20==0:print("progress",wi)
    sg=greedy(worlds,ET,train,a.K);si=individual(worlds,ET,a.K);so=greedy(worlds,EV,test,a.K)
    hand=[D for D in (-7,5,-19,-11,13) if D in worlds]+[D for D in si if D not in (-7,5,-19,-11,13)]
    schedules={"train_greedy":sg,"train_individual":si,"hand":hand[:a.K],"oracle_test_greedy":so}
    res={name:eval_sched(s,EV,test,a.K) for name,s in schedules.items()}
    train_hits=[len(ET[D]) for D in worlds];test_hits=[len(EV[D]) for D in worlds]
    rho=spearman(train_hits,test_hits)
    cps={}
    for k in (1,2,3,5,10,20):
        cps[str(k)]={}
        for name,s in schedules.items():
            ev=eval_sched(s,EV,test,min(k,a.K))
            cps[str(k)][name]={"coverage":ev["coverage"],"cost":ev["capped_mean_cost"]}
    payload={"dmax":a.dmax,"train_n":len(train),"test_n":len(test),"worlds":len(worlds),
      "spearman_train_test_hits":rho,"schedules":schedules,"results":res,"checkpoints":cps,
      "prefix_overlap_greedy_oracle":{str(k):len(set(sg[:k])&set(so[:k])) for k in (5,10,20)}}
    (out/"out_of_sample.json").write_text(json.dumps(payload,indent=2))
    rows=[]
    for k,dd in cps.items():
        for name,v in dd.items():rows.append({"k":k,"schedule":name,**v})
    with (out/"out_of_sample.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print("# H21-LAB-24 · Out-of-sample world compiler")
    print("train_n:",len(train));print("test_n:",len(test));print("worlds:",len(worlds));print("rho:",rho)
    for n,v in res.items():print(n,"coverage",v["coverage"],"cost",v["capped_mean_cost"],"schedule",schedules[n])
    print("overlap",payload["prefix_overlap_greedy_oracle"])
if __name__=="__main__":main()
