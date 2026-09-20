#!/usr/bin/env python3
"""Targeted H18 M1 closure: all size-10 and size-11 subsets of the certified
12-query adaptive witness.

This is not an exhaustive search over all W4 alphabets.  It is a cheap exact
strike inside the already successful 12-query family.

Because size 9 has already been exhaustively excluded by the partition-type
quotient search, any successful size-10 subset immediately proves M1(W4)=10.
A successful size-11 subset gives the improved upper bound M1(W4)<=11 if no
size-10 witness is found here.
"""

from __future__ import annotations

import importlib.util
from functools import lru_cache
from itertools import combinations
from pathlib import Path

HERE=Path(__file__).resolve()
H18=HERE.parents[1]
SRC=H18/"certificates"/"h18_adaptive_one_erasure_certificate.py"

spec=importlib.util.spec_from_file_location("h18_e1",SRC)
assert spec is not None and spec.loader is not None
c=importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

WORDS=[q[0] for q in c.QUERIES]
WORD_TO_Q={w:i for i,w in enumerate(WORDS)}

ADAPTIVE12_WORDS=(
    "A","B","ABab","AbaB","ABB","Abb","AAb","AAAB","AAAb","Baa","aab","abb"
)
ADAPTIVE12=tuple(WORD_TO_Q[w] for w in ADAPTIVE12_WORDS)


def partitions(mask:int,qi:int)->tuple[int,...]:
    return tuple(mask & cm for cm in c.QUERY_MASKS[qi] if mask & cm)


def flags(alphabet:tuple[int,...])->tuple[bool,bool]:
    aset=tuple(sorted(alphabet))

    @lru_cache(maxsize=None)
    def no(mask:int,left:int,banned:int)->bool:
        if c.terminal(mask): return True
        if left==0: return False
        cand=[]
        for qi in aset:
            if qi==banned: continue
            parts=partitions(mask,qi)
            if len(parts)<=1: continue
            cand.append((max(c.popcount(p) for p in parts),-len(parts),len(WORDS[qi]),WORDS[qi],qi,parts))
        cand.sort()
        for *_,parts in cand:
            if all(no(p,left-1,banned) for p in parts):
                return True
        return False

    no4=no(c.ALL_MASK,4,-1)
    if not no4:
        return False,False

    @lru_cache(maxsize=None)
    def one(mask:int,left:int)->bool:
        if c.terminal(mask): return True
        if left==0: return False
        cand=[]
        for qi in aset:
            parts=partitions(mask,qi)
            if len(parts)<=1: continue
            if not no(mask,left,qi): continue
            cand.append((max(c.popcount(p) for p in parts),-len(parts),len(WORDS[qi]),WORDS[qi],qi,parts))
        cand.sort()
        for *_,parts in cand:
            if all(one(p,left-1) for p in parts):
                return True
        return False

    return True,one(c.ALL_MASK,4)


def scan(k:int):
    total=0
    no4_count=0
    full=[]
    for subset in combinations(ADAPTIVE12,k):
        total+=1
        n4,e4=flags(subset)
        if n4: no4_count+=1
        if n4 and e4:
            full.append(subset)
            # keep scanning: the full witness list is useful structurally
    return total,no4_count,full


def main():
    for k in (10,11):
        total,no4,full=scan(k)
        print(f"size-{k} subsets tested =",total)
        print(f"size-{k} no-erasure depth4 =",no4)
        print(f"size-{k} full one-erasure depth4 =",len(full))
        for s in full:
            print(f"size-{k} witness =",tuple(WORDS[q] for q in s))

        if k==10 and full:
            print("CONSEQUENCE: global size-9 exclusion + size-10 witness => M1(W4)=10")
        elif k==11 and full:
            print("CONSEQUENCE: targeted upper bound M1(W4)<=11")

    print("PASS")


if __name__=="__main__":
    main()
