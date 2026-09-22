#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,math
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


def world(D):
    return (1,(D-1)//4) if D%4==1 else (0,D//4)


def jacobi(a,n):
    if n<=0 or n%2==0:raise ValueError
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


def prime_list(limit):
    isp=bytearray(b"\x01")*(limit+1);isp[0:2]=b"\x00\x00"
    for p in range(2,int(limit**.5)+1):
        if isp[p]:
            st=p*p;isp[st:limit+1:p]=b"\x00"*(((limit-st)//p)+1)
    return [p for p in range(3,limit+1,2) if isp[p]]


def defect_factor(n,B,C,D):
    # Cheap exceptional precheck is part of the runtime-safe world observer.
    g=math.gcd(n,abs(2*C*D))
    if 1<g<n:
        return g,"precheck"
    if g!=1:
        return None,"degenerate"

    j=jacobi(D,n)
    if j not in (-1,1):
        return None,"degenerate"

    got=pow_x(n,n,B,C)
    want=(0,1) if j==1 else (B%n,(-1)%n)
    d0=(got[0]-want[0])%n
    d1=(got[1]-want[1])%n

    for d in (d0,d1):
        gg=math.gcd(n,d)
        if 1<gg<n:
            return gg,"defect"
    return None,"none"


def revelation(schedule,exposures,pop):
    rank={n:None for n in pop}
    cumulative=[]
    seen=set()
    for i,D in enumerate(schedule,1):
        hits=exposures[D]
        new=hits-seen
        for n in new:
            if rank[n] is None:rank[n]=i
        seen|=hits
        cumulative.append({"step":i,"D":D,"new":len(new),"covered":len(seen),"fraction":len(seen)/len(pop)})
    vals=[v for v in rank.values() if v is not None]
    vals.sort()
    avg=sum(vals)/len(vals) if vals else 0
    med=vals[len(vals)//2] if vals else 0
    return cumulative,avg,med,len(vals)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bits",type=int,default=18)
    ap.add_argument("--dmax",type=int,default=127)
    ap.add_argument("--max-worlds",type=int,default=20)
    ap.add_argument("--out-dir",default="lab23_out")
    a=ap.parse_args()

    N=1<<a.bits
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    ps=prime_list(N)

    # common-core distinct odd semiprimes
    pop=[]
    for i,p in enumerate(ps):
        if p*p>=N:break
        for q in ps[i+1:]:
            if p*q>=N:break
            if p>a.dmax and q>a.dmax:
                pop.append(p*q)

    worlds=[D for D in fdiscs(a.dmax) if D not in (-3,-4)]
    exposures={}
    mechanisms={}

    for wi,D in enumerate(worlds,1):
        B,C=world(D)
        hit=set()
        mech={"precheck":0,"defect":0,"none":0,"degenerate":0}
        for n in pop:
            f,m=defect_factor(n,B,C,D)
            mech[m]=mech.get(m,0)+1
            if f is not None:
                hit.add(n)
        exposures[D]=hit
        mechanisms[D]=mech
        if wi%20==0:print("progress",wi,len(worlds))

    # individual ranking
    indiv=sorted(worlds,key=lambda D:(len(exposures[D]),-abs(D)),reverse=True)

    # greedy complementarity
    uncovered=set(pop)
    remaining=set(worlds)
    greedy=[]
    greedy_new=[]
    for _ in range(min(a.max_worlds,len(worlds))):
        if not remaining:break
        best=max(remaining,key=lambda D:(len(exposures[D]&uncovered),len(exposures[D]),-abs(D)))
        new=len(exposures[best]&uncovered)
        greedy.append(best);greedy_new.append(new)
        uncovered-=exposures[best]
        remaining.remove(best)
        if new==0:break

    hand=[D for D in (-7,5,-19,-11,13) if D in exposures]
    # extend hand by individual order without duplicates for fair k comparison
    hand_ext=hand+[D for D in indiv if D not in hand]

    schedules={
        "greedy":greedy,
        "individual":indiv[:a.max_worlds],
        "hand_extended":hand_ext[:a.max_worlds],
    }

    results={}
    curve_rows=[]
    for name,sched in schedules.items():
        curve,avg,med,cov=revelation(sched,exposures,pop)
        results[name]={
            "schedule":sched,
            "covered":cov,
            "coverage_fraction":cov/len(pop),
            "average_revelation_index_covered":avg,
            "median_revelation_index_covered":med,
            "curve":curve,
        }
        for r in curve:
            curve_rows.append({"schedule":name,**r})

    # prefix comparisons at 1,2,3,5,10,20
    checkpoints={}
    for k in (1,2,3,5,10,20):
        checkpoints[str(k)]={}
        for name,res in results.items():
            if not res["curve"]:continue
            idx=min(k,len(res["curve"]))-1
            checkpoints[str(k)][name]=res["curve"][idx]["fraction"]

    world_rows=[]
    for D in indiv:
        world_rows.append({
            "D":D,
            "individual_hits":len(exposures[D]),
            "individual_fraction":len(exposures[D])/len(pop),
            **mechanisms[D],
        })

    with (out/"schedule_curves.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(curve_rows[0].keys()));w.writeheader();w.writerows(curve_rows)
    with (out/"world_runtime_hits.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(world_rows[0].keys()));w.writeheader();w.writerows(world_rows)

    payload={
        "bits":a.bits,"dmax":a.dmax,
        "population":len(pop),"worlds":len(worlds),
        "results":results,"checkpoints":checkpoints,
        "greedy_new_hits":greedy_new,
    }
    (out/"runtime_world_compiler.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")

    print("# H21-LAB-23 · Runtime-safe world compiler")
    print("population:",len(pop))
    print("worlds:",len(worlds))
    for name,res in results.items():
        print(name,"schedule:",res["schedule"])
        print(name,"coverage:",f"{res['coverage_fraction']:.6%}")
        print(name,"avg revelation:",f"{res['average_revelation_index_covered']:.6f}")
    print("checkpoints:",json.dumps(checkpoints))
    print("PASS: runtime-safe compiler scan completed")

if __name__=="__main__":main()
