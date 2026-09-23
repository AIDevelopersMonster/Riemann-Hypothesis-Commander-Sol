#!/usr/bin/env python3
"""Constructive size-11 neighborhood search around the certified adaptive12.

Search all alphabets obtained by removing two labels from the H18-11 witness
and adding one label from outside it. This is a witness search only:
- success gives M1(W4) <= 11;
- failure gives no global lower bound.
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
BASE_WORDS=("A","B","ABab","AbaB","ABB","Abb","AAb","AAAB","AAAb","Baa","aab","abb")
BASE=frozenset(WORD_TO_Q[w] for w in BASE_WORDS)
OUTSIDE=tuple(q for q in range(len(WORDS)) if q not in BASE)

def partitions(mask,qi):
    return tuple(mask & cm for cm in c.QUERY_MASKS[qi] if mask & cm)

def flags(alphabet):
    aset=tuple(sorted(alphabet))

    @lru_cache(maxsize=None)
    def no(mask,left,banned):
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
            if all(no(p,left-1,banned) for p in parts): return True
        return False

    n4=no(c.ALL_MASK,4,-1)
    if not n4: return False,False

    @lru_cache(maxsize=None)
    def one(mask,left):
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
            if all(one(p,left-1) for p in parts): return True
        return False

    return True,one(c.ALL_MASK,4)

tested=0
no4=0
witnesses=[]

for removed in combinations(sorted(BASE),2):
    core=BASE.difference(removed)
    for add in OUTSIDE:
        A=tuple(sorted(core | {add}))
        assert len(A)==11
        tested+=1
        n,e=flags(A)
        if n: no4+=1
        if n and e:
            witnesses.append(A)
            print("FOUND size11 witness =",tuple(WORDS[q] for q in A))
            print("removed =",tuple(WORDS[q] for q in removed),"added =",WORDS[add])
            # First witness is sufficient for the global upper bound.
            break
    if witnesses:
        break

print("candidates tested =",tested)
print("no-erasure depth4 candidates =",no4)
print("full witnesses found =",len(witnesses))
if witnesses:
    print("RESULT: constructive global upper bound M1(W4) <= 11")
else:
    print("RESULT: no witness in radius remove2/add1 around adaptive12")
    print("NO GLOBAL LOWER BOUND follows from this neighborhood search")
print("PASS")
