#!/usr/bin/env python3
"""Exact size-11 H18 partition-type quotient search using bitset constraints.

Mathematically equivalent search space to h18_m1_size11_type_quotient.py:
- 25 equality-partition types, each of multiplicity two;
- forced commutator type at multiplicity two;
- choose total multiplicity nine from the remaining 24 types;
- every required state-pair constraint must receive at least two separating
  query identities;
- every complete distance-two multiplicity vector is tested against the exact
  H18-06 adaptive DP.

The improvement is computational only: the 882 unique distance constraints are
represented as bits in Python integers, so leaf feasibility is an exact bigint
comparison rather than a Python loop over constraints.
"""

from __future__ import annotations

import importlib.util
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

HERE=Path(__file__).resolve()
H18=HERE.parents[1]
SRC=H18/"certificates"/"h18_adaptive_one_erasure_certificate.py"

spec=importlib.util.spec_from_file_location("h18_e1",SRC)
assert spec is not None and spec.loader is not None
c=importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

WORDS=[q[0] for q in c.QUERIES]

def partition_sig(vector):
    mp={}
    nxt=0
    out=[]
    for x in vector:
        if x not in mp:
            mp[x]=nxt
            nxt+=1
        out.append(mp[x])
    return tuple(out)

groups=defaultdict(list)
for qi,(w,v,_) in enumerate(c.QUERIES):
    groups[partition_sig(v)].append(qi)

TYPES=tuple(sorted((tuple(g) for g in groups.values()),key=lambda g:WORDS[g[0]]))
assert len(TYPES)==25
assert all(len(g)==2 for g in TYPES)

TYPE_OF={q:t for t,g in enumerate(TYPES) for q in g}
K=WORD_TO_Q={w:i for i,w in enumerate(WORDS)}
KQ=WORD_TO_Q["ABab"]
KIQ=WORD_TO_Q["AbaB"]
FORCED_TYPE=TYPE_OF[KQ]
assert TYPE_OF[KIQ]==FORCED_TYPE

FREE_TYPES=tuple(t for t in range(25) if t!=FORCED_TYPE)
assert len(FREE_TYPES)==24

GEN=[i for i,g in enumerate(c.IS_GENERATING) if g]
NON=[i for i,g in enumerate(c.IS_GENERATING) if not g]
PAIRS=[]
for p,i in enumerate(GEN):
    for j in GEN[p+1:]:
        PAIRS.append((i,j))
    for j in NON:
        PAIRS.append((i,j))
assert len(PAIRS)==15903

# Unique constraints are sets of free partition types that distinguish the pair.
raw_constraints=set()
forced_vec=c.QUERIES[TYPES[FORCED_TYPE][0]][1]
for i,j in PAIRS:
    if forced_vec[i]!=forced_vec[j]:
        continue
    mask=0
    for li,t in enumerate(FREE_TYPES):
        v=c.QUERIES[TYPES[t][0]][1]
        if v[i]!=v[j]:
            mask |= 1<<li
    assert mask
    raw_constraints.add(mask)

CONSTRAINTS=tuple(sorted(raw_constraints,key=lambda x:(x.bit_count(),x)))
assert len(CONSTRAINTS)==882

# For every free type, bitset of unique constraints it separates.
TYPE_HITS=[]
for li in range(24):
    bit=1<<li
    hit=0
    for ci,cm in enumerate(CONSTRAINTS):
        if cm & bit:
            hit |= 1<<ci
    TYPE_HITS.append(hit)

ALL=(1<<len(CONSTRAINTS))-1

# Search high-coverage types first.  Keep original local index for reconstruction.
ORDER=tuple(sorted(range(24),key=lambda li:(-TYPE_HITS[li].bit_count(),WORDS[TYPES[FREE_TYPES[li]][0]],li)))
HITS=tuple(TYPE_HITS[li] for li in ORDER)

# Suffix: constraints coverable by at least one still-unassigned type.
SUFFIX_ANY=[0]*25
for i in range(23,-1,-1):
    SUFFIX_ANY[i]=SUFFIX_ANY[i+1] | HITS[i]
assert SUFFIX_ANY[0]==ALL

def partitions(mask:int,qi:int)->tuple[int,...]:
    return tuple(mask & cm for cm in c.QUERY_MASKS[qi] if mask & cm)

def canonical_alphabet(mult_by_original_local:tuple[int,...]):
    out=[KQ,KIQ]
    for li,m in enumerate(mult_by_original_local):
        t=FREE_TYPES[li]
        if m==1:
            out.append(TYPES[t][0])
        elif m==2:
            out.extend(TYPES[t])
    assert len(out)==11
    return tuple(sorted(out))

def adaptive_flags(alphabet:tuple[int,...])->tuple[bool,bool]:
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

    n4=no(c.ALL_MASK,4,-1)
    if not n4:
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

nodes=0
capacity_prunes=0
coverage_prunes=0
complete_vectors=0
distance2_vectors=0
no4_vectors=0
adaptive_tests=0
witness=None

# Multiplicities stored in search ORDER coordinates.
mult=[0]*24

def dfs(idx:int,used:int,once:int,twice:int):
    global nodes,capacity_prunes,coverage_prunes,complete_vectors
    global distance2_vectors,no4_vectors,adaptive_tests,witness

    if witness is not None:
        return

    nodes+=1
    slots=9-used
    remain=24-idx

    if slots<0 or slots>2*remain:
        capacity_prunes+=1
        return

    if idx==24:
        if used!=9:
            return
        complete_vectors+=1
        if twice!=ALL:
            return

        distance2_vectors+=1
        by_orig=[0]*24
        for pos,m in enumerate(mult):
            by_orig[ORDER[pos]]=m
        alphabet=canonical_alphabet(tuple(by_orig))
        adaptive_tests+=1
        n4,e4=adaptive_flags(alphabet)
        if n4:
            no4_vectors+=1
        if n4 and e4:
            witness=alphabet
        return

    # Necessary coverage feasibility.
    need1=once & (ALL ^ twice)
    need2=ALL ^ once
    if (need1 | need2) & ~SUFFIX_ANY[idx]:
        coverage_prunes+=1
        return
    if need2 and slots<2:
        coverage_prunes+=1
        return

    hit=HITS[idx]

    # Heuristic 1,2,0 seeks a compact witness early but remains exhaustive.
    if slots>=1:
        mult[idx]=1
        dfs(idx+1,used+1,once|hit,twice|(once&hit))
        if witness is not None: return

    if slots>=2:
        mult[idx]=2
        # Two identities of one partition type each separate exactly the same
        # constraints, so all 'hit' constraints become twice-covered.
        dfs(idx+1,used+2,once|hit,twice|hit)
        if witness is not None: return

    mult[idx]=0
    dfs(idx+1,used,once,twice)
    mult[idx]=0

def main():
    print("H18 exact size-11 partition-type bitset search")
    print("query partition types =",len(TYPES))
    print("forced type =",tuple(WORDS[q] for q in TYPES[FORCED_TYPE]))
    print("unique constraints =",len(CONSTRAINTS))
    print("search order =",tuple(tuple(WORDS[q] for q in TYPES[FREE_TYPES[li]]) for li in ORDER))

    dfs(0,0,0,0)

    print("DFS nodes =",nodes)
    print("capacity prunes =",capacity_prunes)
    print("coverage prunes =",coverage_prunes)
    print("complete multiplicity vectors =",complete_vectors)
    print("distance2 vectors =",distance2_vectors)
    print("no-erasure depth4 vectors =",no4_vectors)
    print("adaptive tests =",adaptive_tests)
    print("witness =",None if witness is None else tuple(WORDS[q] for q in witness))

    if witness is None:
        print("RESULT: no size-11 alphabet satisfies the full H18-06 adaptive contract")
        print("CONSEQUENCE: no size-11 alphabet exists; by monotonicity and the size-12 witness, M1(W4) = 12")
    else:
        print("RESULT: size-11 adaptive witness exists")
        print("CONSEQUENCE: global upper bound improves to M1(W4) <= 11")
    print("PASS")

if __name__=="__main__":
    main()
