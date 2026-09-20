#!/usr/bin/env python3
"""Exact size-10 H18 search on the quotient by query response-partition type.

The 50 canonical W4 queries form exactly 25 pairs of queries with the same
equality partition on all 197 states. Members of one pair differ only by a
bijection of used response labels.

Adaptive decision feasibility is invariant under replacing one query by its
partition-equivalent partner: every branch partition of the state mask is the
same, only response names are relabelled. Under persistent known query erasure,
query *identity* still matters, so multiplicity 0/1/2 of each type is retained.

The forced commutator type {ABab,AbaB} has multiplicity two in every robust
alphabet. A size-10 alphabet therefore chooses seven query identities from the
remaining 24 partition types, each with available multiplicity two.

We search exact multiplicity vectors x_t in {0,1,2}, sum x_t=7, subject to
distance-two constraints. One canonical representative alphabet per vector is
then tested by the exact H18-06 adaptive DP.
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
            mp[x]=nxt; nxt+=1
        out.append(mp[x])
    return tuple(out)

groups=defaultdict(list)
for qi,(w,v,_) in enumerate(c.QUERIES):
    groups[partition_sig(v)].append(qi)
TYPES=tuple(sorted((tuple(g) for g in groups.values()),key=lambda g:WORDS[g[0]]))
assert len(TYPES)==25
assert all(len(g)==2 for g in TYPES)

TYPE_OF={q:t for t,g in enumerate(TYPES) for q in g}
K=next(i for i,w in enumerate(WORDS) if w=="ABab")
KI=next(i for i,w in enumerate(WORDS) if w=="AbaB")
FORCED_TYPE=TYPE_OF[K]
assert TYPE_OF[KI]==FORCED_TYPE
assert set(TYPES[FORCED_TYPE])=={K,KI}

FREE_TYPES=tuple(t for t in range(25) if t!=FORCED_TYPE)
LOCAL={t:i for i,t in enumerate(FREE_TYPES)}
assert len(FREE_TYPES)==24

# Required generating/generating and generating/non-generating pairs.
GEN=[i for i,g in enumerate(c.IS_GENERATING) if g]
NON=[i for i,g in enumerate(c.IS_GENERATING) if not g]
PAIRS=[]
for p,i in enumerate(GEN):
    for j in GEN[p+1:]:
        PAIRS.append((i,j))
    for j in NON:
        PAIRS.append((i,j))
assert len(PAIRS)==15903

# Each remaining pair constraint becomes a 24-bit mask of partition types that
# distinguish it. Forced type already contributes either 0 or 2 hits.
CONSTRAINTS=[]
for i,j in PAIRS:
    fv=c.QUERIES[TYPES[FORCED_TYPE][0]][1]
    forced_sep=(fv[i]!=fv[j])
    if forced_sep:
        # both forced identities separate: already distance two
        continue
    mask=0
    for t in FREE_TYPES:
        q=TYPES[t][0]
        v=c.QUERIES[q][1]
        if v[i]!=v[j]:
            mask |= 1<<LOCAL[t]
    assert mask
    CONSTRAINTS.append(mask)
assert len(CONSTRAINTS)==3556
CONSTRAINTS=tuple(sorted(set(CONSTRAINTS),key=lambda x:(x.bit_count(),x)))

# multiplicities encoded by two disjoint bitsets:
# once bit means >=1 selected from type; twice bit means 2 selected.
def constraint_hits(cm:int,once:int,twice:int)->int:
    # sum multiplicities over separating types, capped only by comparison >=2.
    if cm & twice:
        return 2
    return (cm & once).bit_count()

def distance2_complete(once:int,twice:int)->bool:
    return all(constraint_hits(cm,once,twice)>=2 for cm in CONSTRAINTS)

def canonical_alphabet(once:int,twice:int):
    out=[K,KI]
    for li,t in enumerate(FREE_TYPES):
        b=1<<li
        if twice & b:
            out.extend(TYPES[t])
        elif once & b:
            out.append(TYPES[t][0])
    assert len(out)==10
    return tuple(sorted(out))

def partitions(mask:int,qi:int)->tuple[int,...]:
    return tuple(mask & cm for cm in c.QUERY_MASKS[qi] if mask & cm)

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

# Exact DFS over multiplicity assignments. We branch by type with multiplicity
# 0/1/2; safe suffix feasibility uses the maximum possible two copies of every
# unassigned type.
N=24
SUFFIX_MASK=[0]*(N+1)
for i in range(N-1,-1,-1):
    SUFFIX_MASK[i]=SUFFIX_MASK[i+1] | (1<<i)

nodes=0
pruned_capacity=0
pruned_constraints=0
complete_vectors=0
distance2_vectors=0
no4_vectors=0
adaptive_tests=0
witness=None

def feasible(idx:int,once:int,twice:int,used:int)->bool:
    global pruned_constraints
    remaining_slots=8-used
    suffix=SUFFIX_MASK[idx]
    for cm in CONSTRAINTS:
        have=constraint_hits(cm,once,twice)
        if have>=2: continue
        # Maximum additional contribution: up to 2 from each unassigned type
        # in cm, but globally no more than remaining_slots.
        avail_types=(cm & suffix).bit_count()
        if avail_types==0:
            pruned_constraints+=1; return False
        max_add=min(remaining_slots,2*avail_types)
        if have+max_add<2:
            pruned_constraints+=1; return False
    return True

def dfs(idx:int,once:int,twice:int,used:int):
    global nodes,pruned_capacity,complete_vectors,distance2_vectors
    global no4_vectors,adaptive_tests,witness
    if witness is not None:
        return
    nodes+=1
    if used>8:
        return
    if idx==N:
        if used!=8: return
        complete_vectors+=1
        if not distance2_complete(once,twice):
            return
        distance2_vectors+=1
        alphabet=canonical_alphabet(once,twice)
        adaptive_tests+=1
        n4,e4=adaptive_flags(alphabet)
        if n4: no4_vectors+=1
        if n4 and e4:
            witness=(once,twice,alphabet)
        return

    if used + 2*(N-idx) < 8:
        pruned_capacity+=1; return
    if not feasible(idx,once,twice,used):
        return

    b=1<<idx

    # Heuristic ordering: try multiplicity 1, then 2, then 0 to find a witness
    # early if one exists. Completeness is unaffected.
    if used+1<=8:
        dfs(idx+1,once|b,twice,used+1)
    if witness is not None: return
    if used+2<=8:
        dfs(idx+1,once|b,twice|b,used+2)
    if witness is not None: return
    dfs(idx+1,once,twice,used)

dfs(0,0,0,0)

print("H18 exact size-10 partition-type quotient search")
print("query partition types =",len(TYPES))
print("all type multiplicities =",tuple(tuple(WORDS[q] for q in g) for g in TYPES))
print("forced type =",tuple(WORDS[q] for q in TYPES[FORCED_TYPE]))
print("unique remaining distance constraints =",len(CONSTRAINTS))
print("DFS nodes =",nodes)
print("capacity prunes =",pruned_capacity)
print("constraint prunes =",pruned_constraints)
print("complete multiplicity vectors =",complete_vectors)
print("distance2 multiplicity vectors =",distance2_vectors)
print("no-erasure depth4 vectors =",no4_vectors)
print("adaptive tests =",adaptive_tests)
print("witness =",None if witness is None else tuple(WORDS[q] for q in witness[2]))
if witness is None:
    print("RESULT: no size-10 partition-type multiplicity vector satisfies full H18-06 adaptive contract")
    print("CONSEQUENCE: M1(W4) >= 11")
else:
    print("RESULT: size-10 adaptive witness exists")
    print("CONSEQUENCE: M1(W4) = 10")
print("PASS")
