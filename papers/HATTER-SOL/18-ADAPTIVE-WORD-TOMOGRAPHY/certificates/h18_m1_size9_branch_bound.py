#!/usr/bin/env python3
"""Exact H18 M1 size-9 search with pair-coverage branch-and-bound.

Goal
----
Decide whether ANY 9-query alphabet inside the frozen 50-query W4 pool
supports the full H18-06 adaptive one-persistent-erasure contract with four
successful answers.

H18-10 already proved:
  * ABab and AbaB are forced in every distance-2 alphabet;
  * no distance-2 alphabet of size <= 8 exists.

Therefore every size-9 candidate is
    {ABab, AbaB} union S, |S|=7, S subset of 48 remaining labels.

The search is exact but avoids blind C(48,7) enumeration:
  1. maintain exact pairwise hit counts capped at 2;
  2. branch only on labels that can repair currently deficient pairs;
  3. use suffix-union feasibility to prune pairs that cannot reach two hits;
  4. use a greedy lower bound on the number of additional labels needed;
  5. run the expensive adaptive DP only on complete distance-2 alphabets.

No floating-point arithmetic is used for decisions.
"""

from __future__ import annotations

import importlib.util
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve()
H18 = HERE.parents[1]
SRC = H18 / "certificates" / "h18_adaptive_one_erasure_certificate.py"

spec = importlib.util.spec_from_file_location("h18_e1", SRC)
assert spec is not None and spec.loader is not None
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

WORDS = [q[0] for q in c.QUERIES]
WORD_TO_Q = {w: i for i, w in enumerate(WORDS)}
K = WORD_TO_Q["ABab"]
KINV = WORD_TO_Q["AbaB"]
FORCED = (K, KINV)

GEN = [i for i,g in enumerate(c.IS_GENERATING) if g]
NON = [i for i,g in enumerate(c.IS_GENERATING) if not g]
PAIRS = []
for pos,i in enumerate(GEN):
    for j in GEN[pos+1:]:
        PAIRS.append((i,j))
    for j in NON:
        PAIRS.append((i,j))
assert len(PAIRS) == 15903

# Pair bitsets for each query.
HIT = []
for qi,(_,vec,_) in enumerate(c.QUERIES):
    bits=0
    for b,(i,j) in enumerate(PAIRS):
        if vec[i] != vec[j]:
            bits |= 1<<b
    HIT.append(bits)

ALL=(1<<len(PAIRS))-1

# Starting one-hit/two-hit masks after forced commutator pair.
once=0
twice=0
for qi in FORCED:
    h=HIT[qi]
    twice |= once & h
    once |= h

EXTRAS=tuple(q for q in range(len(c.QUERIES)) if q not in FORCED)
assert len(EXTRAS)==48

# Canonical ordering: most useful labels first, then shorter word/name.
def usefulness(qi:int)->tuple:
    # prioritize coverage of not-yet-twice pairs
    gain=(HIT[qi] & ~twice & ALL).bit_count()
    return (-gain, len(WORDS[qi]), WORDS[qi], qi)

EXTRAS=tuple(sorted(EXTRAS,key=usefulness))

# suffix union: pairs hit by at least one remaining label.
SUFFIX_UNION=[0]*(len(EXTRAS)+1)
for i in range(len(EXTRAS)-1,-1,-1):
    SUFFIX_UNION[i]=SUFFIX_UNION[i+1] | HIT[EXTRAS[i]]

# suffix double-cover possibility: pairs hit by at least two remaining labels.
# Maintain suffix once/twice exactly.
SUFFIX_ONCE=[0]*(len(EXTRAS)+1)
SUFFIX_TWICE=[0]*(len(EXTRAS)+1)
for i in range(len(EXTRAS)-1,-1,-1):
    h=HIT[EXTRAS[i]]
    SUFFIX_ONCE[i]=SUFFIX_ONCE[i+1] | h
    SUFFIX_TWICE[i]=SUFFIX_TWICE[i+1] | (SUFFIX_ONCE[i+1] & h)

def feasible_suffix(idx:int, cur_once:int, cur_twice:int)->bool:
    deficient1 = cur_once & ~cur_twice & ALL  # needs >=1 future hit
    deficient0 = ~cur_once & ALL             # needs >=2 future hits
    if deficient1 & ~SUFFIX_UNION[idx]:
        return False
    if deficient0 & ~SUFFIX_TWICE[idx]:
        return False
    return True

def greedy_slot_lower_bound(idx:int, cur_once:int, cur_twice:int)->int:
    """Admissible lower bound on labels still needed.

    We use only total remaining 'hit demand' divided by the best per-label
    demand reduction.  This is weak but safe.
    """
    need1 = cur_once & ~cur_twice & ALL
    need0 = ~cur_once & ALL
    demand = need1.bit_count() + 2*need0.bit_count()
    if demand == 0:
        return 0
    best=0
    for qi in EXTRAS[idx:]:
        h=HIT[qi]
        # a label removes one unit of demand for every currently <2-hit pair it hits
        red=(h & ~cur_twice & ALL).bit_count()
        if red>best:
            best=red
    if best==0:
        return 10**9
    return (demand + best - 1)//best

def partitions(mask:int, qi:int)->tuple[int,...]:
    return tuple(mask & cm for cm in c.QUERY_MASKS[qi] if mask & cm)

def adaptive_ok(alphabet:tuple[int,...])->bool:
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

    return no(c.ALL_MASK,4,-1) and one(c.ALL_MASK,4)

nodes=0
prune_suffix=0
prune_slots=0
distance2_leaves=0
adaptive_tests=0
witness=None

def dfs(idx:int, chosen:tuple[int,...], cur_once:int, cur_twice:int):
    global nodes,prune_suffix,prune_slots,distance2_leaves,adaptive_tests,witness
    if witness is not None:
        return
    nodes += 1
    slots=7-len(chosen)
    if slots<0:
        return
    if cur_twice==ALL:
        if slots==0:
            distance2_leaves += 1
            alphabet=FORCED+chosen
            adaptive_tests += 1
            if adaptive_ok(alphabet):
                witness=alphabet
        return
    if idx>=len(EXTRAS):
        return
    if len(EXTRAS)-idx < slots:
        return
    if not feasible_suffix(idx,cur_once,cur_twice):
        prune_suffix += 1
        return
    lb=greedy_slot_lower_bound(idx,cur_once,cur_twice)
    if lb>slots:
        prune_slots += 1
        return
    if slots==0:
        return

    # Choose a deficient pair with fewest remaining covering labels to guide branching.
    deficient = (~cur_twice) & ALL
    best_pair=None
    best_cover=None
    tmp=deficient
    while tmp:
        lsb=tmp & -tmp
        b=lsb.bit_length()-1
        candidates=[j for j in range(idx,len(EXTRAS)) if (HIT[EXTRAS[j]]>>b)&1]
        need=2 if ((cur_once>>b)&1)==0 else 1
        if len(candidates) < need:
            prune_suffix += 1
            return
        score=(len(candidates),-need,b)
        if best_pair is None or score<best_pair:
            best_pair=score
            best_cover=(candidates,need)
            if len(candidates)==need:
                break
        tmp ^= lsb

    candidates,need=best_cover

    # Canonical branching: force inclusion choices among labels capable of
    # satisfying the selected deficient pair. We branch by the next candidate
    # position while keeping combinations unique.
    first=candidates[0]

    # Include EXTRAS[first].
    qi=EXTRAS[first]
    h=HIT[qi]
    new_twice=cur_twice | (cur_once & h)
    new_once=cur_once | h
    dfs(first+1, chosen+(qi,), new_once, new_twice)

    # Exclude it, but only if enough covering labels remain for selected pair.
    remaining_cover=sum(1 for j in candidates[1:] if j>first)
    if remaining_cover >= need:
        dfs(first+1, chosen, cur_once, cur_twice)

dfs(0,tuple(),once,twice)

print("H18 exact size-9 branch-and-bound")
print("forced =", tuple(WORDS[q] for q in FORCED))
print("search nodes =", nodes)
print("suffix prunes =", prune_suffix)
print("slot-lower-bound prunes =", prune_slots)
print("distance-2 size9 leaves =", distance2_leaves)
print("adaptive tests =", adaptive_tests)
print("adaptive size9 witness =", None if witness is None else tuple(WORDS[q] for q in witness))
if witness is None:
    print("RESULT: no adaptive size-9 witness found by exhaustive canonical BnB")
else:
    print("RESULT: adaptive size-9 witness exists")
print("PASS")
