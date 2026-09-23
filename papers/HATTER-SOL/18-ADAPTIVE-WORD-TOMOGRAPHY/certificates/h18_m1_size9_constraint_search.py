#!/usr/bin/env python3
"""Exact H18 M1 size-9 search by deficient-pair constraint branching.

This is an independent exhaustive algorithm from h18_m1_size9_branch_bound.py.

Every size-9 distance-two candidate contains the forced oriented commutator
pair ABab/AbaB plus seven labels from the remaining 48.

At each search state choose a pair that currently has fewer than two
distinguishing labels and minimizes the number of admissible remaining
coverers.  If the pair still needs r hits, every valid completion contains at
least r of those coverers.  Branch over all r-subsets of the coverers.  This is
complete: every valid completion contains at least one branched subset.

Memoization by chosen-label set removes duplicate paths.

Only complete distance-two 9-alphabets are passed to the adaptive H18-06 DP.
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
K=WORD_TO_Q["ABab"]
KI=WORD_TO_Q["AbaB"]
FORCED=(K,KI)
EXTRAS=tuple(q for q in range(len(c.QUERIES)) if q not in FORCED)
assert len(EXTRAS)==48

GEN=[i for i,g in enumerate(c.IS_GENERATING) if g]
NON=[i for i,g in enumerate(c.IS_GENERATING) if not g]
PAIRS=[]
for pos,i in enumerate(GEN):
    for j in GEN[pos+1:]:
        PAIRS.append((i,j))
    for j in NON:
        PAIRS.append((i,j))
assert len(PAIRS)==15903

# For each required pair, exact list of extra labels that distinguish it.
COVERERS=[]
forced_hits=[]
for i,j in PAIRS:
    fh=sum(c.QUERIES[q][1][i]!=c.QUERIES[q][1][j] for q in FORCED)
    forced_hits.append(fh)
    COVERERS.append(tuple(q for q in EXTRAS if c.QUERIES[q][1][i]!=c.QUERIES[q][1][j]))

# The H18-10 critical-pair theorem appears directly here.
assert min(forced_hits)==0
assert max(forced_hits)==2

def pair_hits(pair_index:int, chosen:frozenset[int])->int:
    return min(2, forced_hits[pair_index] + sum(q in chosen for q in COVERERS[pair_index]))

def partitions(mask:int,qi:int)->tuple[int,...]:
    return tuple(mask & cm for cm in c.QUERY_MASKS[qi] if mask & cm)

def adaptive_flags(alphabet:tuple[int,...])->tuple[bool,bool]:
    aset=tuple(sorted(alphabet))

    @lru_cache(maxsize=None)
    def no(mask:int,left:int,banned:int)->bool:
        if c.terminal(mask):
            return True
        if left==0:
            return False
        cand=[]
        for qi in aset:
            if qi==banned:
                continue
            parts=partitions(mask,qi)
            if len(parts)<=1:
                continue
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
        if c.terminal(mask):
            return True
        if left==0:
            return False
        cand=[]
        for qi in aset:
            parts=partitions(mask,qi)
            if len(parts)<=1:
                continue
            if not no(mask,left,qi):
                continue
            cand.append((max(c.popcount(p) for p in parts),-len(parts),len(WORDS[qi]),WORDS[qi],qi,parts))
        cand.sort()
        for *_,parts in cand:
            if all(one(p,left-1) for p in parts):
                return True
        return False

    return True,one(c.ALL_MASK,4)

visited=set()
nodes=0
distance2=0
no4_pass=0
adaptive_tests=0
witness=None

def choose_constraint(chosen:frozenset[int]):
    best=None
    for pi in range(len(PAIRS)):
        h=pair_hits(pi,chosen)
        if h>=2:
            continue
        need=2-h
        avail=tuple(q for q in COVERERS[pi] if q not in chosen)
        if len(avail)<need:
            return ("dead",pi,need,avail)
        # exact branching count is C(len(avail),need); compare cheaply.
        score=(len(avail) if need==1 else len(avail)*(len(avail)-1)//2,
               len(avail),-need,pi)
        if best is None or score<best[0]:
            best=(score,pi,need,avail)
    return best

def complete_to_seven(chosen:frozenset[int]):
    missing=7-len(chosen)
    if missing<0:
        return
    remaining=[q for q in EXTRAS if q not in chosen]
    for extra in combinations(remaining,missing):
        yield frozenset(set(chosen)|set(extra))

def search(chosen:frozenset[int]):
    global nodes,distance2,no4_pass,adaptive_tests,witness
    if witness is not None:
        return
    if chosen in visited:
        return
    visited.add(chosen)
    nodes+=1

    if len(chosen)>7:
        return

    constraint=choose_constraint(chosen)
    if constraint is None:
        # All distance-two constraints are already satisfied.  H18-10 proves
        # this cannot happen below 7 extras, but enumerate completions anyway
        # so this certificate does not depend on that optimization.
        for full in complete_to_seven(chosen):
            distance2+=1
            alphabet=FORCED+tuple(sorted(full))
            adaptive_tests+=1
            n4,e4=adaptive_flags(alphabet)
            if n4:
                no4_pass+=1
            if n4 and e4:
                witness=alphabet
                return
        return

    if constraint[0]=="dead":
        return

    _,pi,need,avail=constraint
    slots=7-len(chosen)
    if need>slots:
        return

    # Every valid completion must contain at least 'need' members of avail.
    # Branch over all such minimal forced subsets. Extra coverers, if useful for
    # other pairs, may still be added in later recursion.
    for add in combinations(avail,need):
        new=frozenset(set(chosen)|set(add))
        if len(new)<=7:
            search(new)
            if witness is not None:
                return

search(frozenset())

print("H18 exact size-9 deficient-pair constraint search")
print("visited chosen-label states =",len(visited))
print("search nodes =",nodes)
print("distance-2 size9 candidates tested =",distance2)
print("no-erasure depth4 candidates =",no4_pass)
print("adaptive tests =",adaptive_tests)
print("witness =",None if witness is None else tuple(WORDS[q] for q in witness))
if witness is None:
    print("RESULT: no size-9 alphabet satisfies the full H18-06 adaptive contract")
    print("CONSEQUENCE: M1(W4) >= 10")
else:
    print("RESULT: size-9 adaptive alphabet exists")
    print("CONSEQUENCE: M1(W4) = 9")
print("PASS")
