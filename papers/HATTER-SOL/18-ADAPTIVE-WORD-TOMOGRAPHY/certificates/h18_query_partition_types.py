#!/usr/bin/env python3
"""Classify the 50 W4 queries by equality-partition on all 197 H18 states.

Two queries are partition-equivalent iff for every pair of states they give
equal answers simultaneously. Equivalently their answer vectors differ only by
a bijective relabelling of the used response symbols.

Such queries have identical pair-separation masks. For adaptive decision trees
they are isomorphic under local outcome relabelling when used as one query
identity. Multiplicity still matters when an alphabet contains two distinct
queries of the same partition type, because one-erasure faults refer to query
identity; therefore this script reports multiplicities explicitly.
"""

from __future__ import annotations
import importlib.util
from collections import defaultdict
from pathlib import Path

HERE=Path(__file__).resolve()
H18=HERE.parents[1]
SRC=H18/"certificates"/"h18_adaptive_one_erasure_certificate.py"

spec=importlib.util.spec_from_file_location("h18_e1",SRC)
assert spec is not None and spec.loader is not None
c=importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

def canonical_partition(vector):
    remap={}
    nxt=0
    sig=[]
    for x in vector:
        if x not in remap:
            remap[x]=nxt
            nxt+=1
        sig.append(remap[x])
    return tuple(sig)

groups=defaultdict(list)
for qi,(w,v,_) in enumerate(c.QUERIES):
    groups[canonical_partition(v)].append((qi,w))

items=sorted(groups.values(),key=lambda g:(-len(g),g[0][1]))

print("H18 W4 equality-partition types")
print("queries =",len(c.QUERIES))
print("partition types =",len(items))
print("multiplicity histogram =")
hist=defaultdict(int)
for g in items: hist[len(g)]+=1
print(dict(sorted(hist.items())))
for k,g in enumerate(items):
    print("TYPE",k,"mult",len(g),"members",tuple(w for _,w in g),"indices",tuple(q for q,_ in g))

# Verify pair-separation equality within each type.
for g in items:
    base=c.QUERIES[g[0][0]][1]
    for qi,_ in g[1:]:
        v=c.QUERIES[qi][1]
        for i in range(len(base)):
            for j in range(i+1,len(base)):
                assert (base[i]==base[j])==(v[i]==v[j])

print("PASS")
