#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json
from pathlib import Path

def M(e):
    if e<=0:return 0
    return (e.bit_length()-1)+(e.bit_count()-1)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--bits",type=int,default=24);ap.add_argument("--out-dir",default="lab26")
    a=ap.parse_args();out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    rows=[];rat=[]
    for n in range(3,1<<a.bits,2):
        ms=M((n-1)//2);mq=4*M(n)
        if ms:
            r=mq/ms;rat.append(r)
            if n<1000 or n in ((1<<k)-1 for k in range(3,a.bits+1)):
                rows.append({"n":n,"M_scalar":ms,"M_quad":mq,"ratio":r})
    s={"bits":a.bits,"odd_inputs":len(rat),"mean_ratio":sum(rat)/len(rat),
       "min_ratio":min(rat),"max_ratio":max(rat),
       "ratio_at_top":4*M((1<<a.bits)-1)/M(((1<<a.bits)-2)//2)}
    with (out/"summary.json").open("w") as f:json.dump(s,f,indent=2)
    with (out/"samples.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print("# H21-LAB-26 · B0 operation-cost collapse")
    for k,v in s.items():print(k,":",v)
if __name__=="__main__":main()
