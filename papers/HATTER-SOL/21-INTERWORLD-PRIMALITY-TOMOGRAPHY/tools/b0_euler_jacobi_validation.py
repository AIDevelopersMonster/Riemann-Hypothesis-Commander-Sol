#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math
from pathlib import Path

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

def mul(u,v,n,C):
    a,b=u;c,d=v
    return ((a*c+b*d*C)%n,(a*d+b*c)%n)

def px(e,n,C):
    a=(1,0);b=(0,1)
    while e:
        if e&1:a=mul(a,b,n,C)
        b=mul(b,b,n,C);e>>=1
    return a

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--limit",type=int,default=262144);ap.add_argument("--out-dir",default="lab25")
    a=ap.parse_args();out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    Cs=[-31,-19,-11,-7,-3,-2,2,3,5,6,7,10,11,13,14,15,17,19,21,22,23,26,29,30,31]
    checks=0;fail=[]
    factor_checks=0
    for C in Cs:
        D=4*C
        for n in range(3,a.limit,2):
            if math.gcd(n,C)!=1:continue
            jD=jacobi(D,n);jC=jacobi(C,n)
            if jD!=jC:
                fail.append(("jacobi",C,n,jD,jC));continue
            y=px(n,n,C)
            scalar=pow(C%n,(n-1)//2,n)
            checks+=1
            if y!=(0,scalar):
                fail.append(("power",C,n,y,scalar))
            dquad=(y[1]-jD)%n
            dsc=(scalar-jC)%n
            if dquad!=dsc:
                fail.append(("defect",C,n,dquad,dsc))
            g1=math.gcd(n,dquad);g2=math.gcd(n,dsc)
            factor_checks+=1
            if g1!=g2:
                fail.append(("gcd",C,n,g1,g2))
    s={"limit":a.limit,"C_count":len(Cs),"checks":checks,"factor_checks":factor_checks,"failures":len(fail),"examples":fail[:20]}
    (out/"summary.json").write_text(json.dumps(s,indent=2))
    print("# H21-LAB-25 · B=0 Euler-Jacobi collapse")
    for k,v in s.items():
        if k!="examples":print(k,":",v)
    if fail:raise SystemExit(2)
    print("PASS: B=0 quadratic worlds exactly match scalar Euler-Jacobi observer")
if __name__=="__main__":main()
