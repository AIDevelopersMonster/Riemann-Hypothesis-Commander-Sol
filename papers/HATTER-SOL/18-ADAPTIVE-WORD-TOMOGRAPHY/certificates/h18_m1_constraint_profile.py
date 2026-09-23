#!/usr/bin/env python3
"""Profile the exact size-9 distance-two constraint system."""

from __future__ import annotations
import importlib.util
from collections import Counter
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
K,KI=WQ["ABab"],WQ["AbaB"]
EXTRAS=tuple(q for q in range(50) if q not in (K,KI))

GEN=[i for i,g in enumerate(c.IS_GENERATING) if g]
NON=[i for i,g in enumerate(c.IS_GENERATING) if not g]
pairs=[]
for pos,i in enumerate(GEN):
    for j in GEN[pos+1:]:
        pairs.append((i,j))
    for j in NON:
        pairs.append((i,j))

remaining=[]
for i,j in pairs:
    sep=(c.QUERIES[K][1][i]!=c.QUERIES[K][1][j])
    assert sep==(c.QUERIES[KI][1][i]!=c.QUERIES[KI][1][j])
    if sep:
        continue
    cover=tuple(q for q in EXTRAS if c.QUERIES[q][1][i]!=c.QUERIES[q][1][j])
    remaining.append((i,j,cover))

assert len(remaining)==3556
hist=Counter(len(x[2]) for x in remaining)

print("H18 size9 constraint profile")
print("remaining constraints =",len(remaining))
print("coverer-count histogram =",dict(sorted(hist.items())))
print("minimum coverers =",min(hist))
print("constraints at minimum =",hist[min(hist)])

# For each query, count how many remaining constraints it hits.
hits=Counter()
for _,_,cover in remaining:
    for q in cover:
        hits[q]+=1
ranked=sorted(((n,WORDS[q],q) for q,n in hits.items()),reverse=True)
print("top extra labels by remaining-pair coverage:")
for n,w,q in ranked[:20]:
    print(w,q,n)

# List the most constrained pair rows.
m=min(hist)
print("minimum-coverer constraints:")
shown=0
for i,j,cover in remaining:
    if len(cover)==m:
        print("states",i,j,"coverers",tuple(WORDS[q] for q in cover))
        shown+=1
        if shown>=30:
            break
print("PASS")
