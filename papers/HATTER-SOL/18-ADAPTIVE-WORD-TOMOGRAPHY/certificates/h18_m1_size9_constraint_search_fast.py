#!/usr/bin/env python3
"""Exact H18 size-9 search using 48-bit label masks.

Independent optimized implementation of the deficient-pair branching proof.

H18-10 proves ABab and AbaB have the same separation pattern and are forced.
Therefore every pair not already covered twice by this forced pair receives
zero forced hits and must be hit at least twice by seven labels chosen from
the other 48.

Each such pair is represented by a 48-bit coverer mask.
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
WQ={w:i for i,w in enumerate(WORDS)}
K=WQ["ABab"]
KI=WQ["AbaB"]
FORCED=(K,KI)
EXTRAS=tuple(q for q in range(len(c.QUERIES)) if q not in FORCED)
assert len(EXTRAS)==48
LOCAL={q:i for i,q in enumerate(EXTRAS)}
ALL_LOCAL=(1<<48)-1

GEN=[i for i,g in enumerate(c.IS_GENERATING) if g]
NON=[i for i,g in enumerate(c.IS_GENERATING) if not g]
PAIRS=[]
for pos,i in enumerate(GEN):
    for j in GEN[pos+1:]:
        PAIRS.append((i,j))
    for j in NON:
        PAIRS.append((i,j))
assert len(PAIRS)==15903

# K and KI must have identical equality/separation pattern.
for i,j in PAIRS:
    assert (c.QUERIES[K][1][i]!=c.QUERIES[K][1][j]) == (
        c.QUERIES[KI][1][i]!=c.QUERIES[KI][1][j]
    )

# Keep only the pairs receiving zero hits from the forced pair.
CONSTRAINTS=[]
for i,j in PAIRS:
    if c.QUERIES[K][1][i]!=c.QUERIES[K][1][j]:
        continue
    mask=0
    for q in EXTRAS:
        if c.QUERIES[q][1][i]!=c.QUERIES[q][1][j]:
            mask |= 1<<LOCAL[q]
    assert mask.bit_count()>=2
    CONSTRAINTS.append(mask)

assert len(CONSTRAINTS)==3556

# Order constraints by static number of possible coverers to improve early cuts.
CONSTRAINTS=tuple(sorted(CONSTRAINTS,key=int.bit_count))

def globals_from_mask(mask:int)->tuple[int,...]:
    return tuple(EXTRAS[i] for i in range(48) if (mask>>i)&1)

def partitions(state_mask:int,qi:int)->tuple[int,...]:
    return tuple(state_mask & cm for cm in c.QUERY_MASKS[qi] if state_mask & cm)

def adaptive_flags(local_mask:int)->tuple[bool,bool]:
    alphabet=tuple(sorted(FORCED+globals_from_mask(local_mask)))

    @lru_cache(maxsize=None)
    def no(mask:int,left:int,banned:int)->bool:
        if c.terminal(mask):
            return True
        if left==0:
            return False
        candidates=[]
        for qi in alphabet:
            if qi==banned:
                continue
            parts=partitions(mask,qi)
            if len(parts)<=1:
                continue
            candidates.append((
                max(c.popcount(p) for p in parts),
                -len(parts),len(WORDS[qi]),WORDS[qi],qi,parts
            ))
        candidates.sort()
        for *_,parts in candidates:
            if all(no(p,left-1,banned) for p in parts):
                return True
        return False

    n4=no(c.ALL_MASK,4,-1)
    if not n4:
        return False,False

    @lru_cache(maxsize=None)
    def one(mask:int,left:int)->bool:
        if c.terminal(mask):
            return True
        if left==0:
            return False
        candidates=[]
        for qi in alphabet:
            parts=partitions(mask,qi)
            if len(parts)<=1:
                continue
            if not no(mask,left,qi):
                continue
            candidates.append((
                max(c.popcount(p) for p in parts),
                -len(parts),len(WORDS[qi]),WORDS[qi],qi,parts
            ))
        candidates.sort()
        for *_,parts in candidates:
            if all(one(p,left-1) for p in parts):
                return True
        return False

    return True,one(c.ALL_MASK,4)

def propagate_forced(chosen:int):
    """Apply logically forced labels until a fixed point.

    If a deficient pair needs r additional hits and exactly r unchosen labels
    can still hit it, every valid completion must contain all of them.
    """
    while True:
        if chosen.bit_count()>7:
            return None
        inv=(~chosen)&ALL_LOCAL
        changed=False
        for cm in CONSTRAINTS:
            have=(cm & chosen).bit_count()
            if have>=2:
                continue
            need=2-have
            avail=cm & inv
            n=avail.bit_count()
            if n<need:
                return None
            if n==need:
                chosen |= avail
                changed=True
                break
        if not changed:
            return chosen

def choose_constraint(chosen:int):
    """Return (need, available_local_mask) for best deficient constraint."""
    best=None
    inv=(~chosen)&ALL_LOCAL
    for cm in CONSTRAINTS:
        have=(cm & chosen).bit_count()
        if have>=2:
            continue
        need=2-have
        avail=cm & inv
        n=avail.bit_count()
        if n<need:
            return (99,0)  # dead
        branches=n if need==1 else n*(n-1)//2
        score=(branches,n,-need)
        if best is None or score<best[0]:
            best=(score,need,avail)
            if branches==1:
                break
    if best is None:
        return None
    return best[1],best[2]

def iter_bits(mask:int):
    while mask:
        b=mask & -mask
        yield b
        mask ^= b

def iter_pairs(mask:int):
    bits=list(iter_bits(mask))
    for i in range(len(bits)):
        for j in range(i+1,len(bits)):
            yield bits[i]|bits[j]

visited=set()
nodes=0
distance2=0
no4_pass=0
adaptive_tests=0
witness=None
min_complete_size=99

def evaluate_full(mask:int):
    global distance2,no4_pass,adaptive_tests,witness,min_complete_size
    cnt=mask.bit_count()
    min_complete_size=min(min_complete_size,cnt)
    if cnt>7:
        return
    if cnt<7:
        # Exact H18-10 lower bound says this cannot occur. Keep completion
        # logic for algorithmic independence.
        free=(~mask)&ALL_LOCAL
        for add_positions in combinations([i for i in range(48) if (free>>i)&1],7-cnt):
            full=mask
            for i in add_positions:
                full |= 1<<i
            evaluate_full(full)
            if witness is not None:
                return
        return
    distance2+=1
    adaptive_tests+=1
    n4,e4=adaptive_flags(mask)
    if n4:
        no4_pass+=1
    if n4 and e4:
        witness=mask

def search(chosen:int):
    global nodes,witness
    if witness is not None:
        return

    chosen=propagate_forced(chosen)
    if chosen is None:
        return
    if chosen in visited:
        return
    visited.add(chosen)
    nodes+=1

    if chosen.bit_count()>7:
        return

    choice=choose_constraint(chosen)
    if choice is None:
        evaluate_full(chosen)
        return

    need,avail=choice
    if need==99:
        return
    if chosen.bit_count()+need>7:
        return

    if need==1:
        for add in iter_bits(avail):
            search(chosen|add)
            if witness is not None:
                return
    else:
        for add in iter_pairs(avail):
            search(chosen|add)
            if witness is not None:
                return

search(0)

print("H18 exact size-9 fast constraint search")
print("unsatisfied-after-forced constraints =",len(CONSTRAINTS))
print("visited chosen masks =",len(visited))
print("search nodes =",nodes)
print("minimum complete distance2 extra-count encountered =",min_complete_size)
print("distance2 size9 candidates =",distance2)
print("no-erasure depth4 candidates =",no4_pass)
print("adaptive tests =",adaptive_tests)
print("witness =",None if witness is None else tuple(WORDS[q] for q in FORCED+globals_from_mask(witness)))
if witness is None:
    print("RESULT: no size-9 alphabet satisfies full H18-06 adaptive contract")
    print("CONSEQUENCE: M1(W4) >= 10")
else:
    print("RESULT: size-9 adaptive alphabet exists")
    print("CONSEQUENCE: M1(W4) = 9")
print("PASS")
