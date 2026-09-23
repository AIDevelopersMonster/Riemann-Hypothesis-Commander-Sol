#!/usr/bin/env python3
"""HATTER-SOL-18 H18-04: does one Higman lift-trace query improve W4 adaptivity?

It augments the exact H18-01 50-query class-valued W4 pool by one additional
query tau(A,B)=tr([A~,B~]) in F_7, using the canonical lift invariant certified
by H18-03.

Exact result in the H17 114-state PSL(2,7) laboratory:
  * worst-case adaptive depth remains 4;
  * depth 3 remains impossible;
  * minimum total path length among depth-4 trees remains 382;
  * minimum mean depth remains 191/57;
  * a selected optimum still roots at AAB and has 48 internal nodes.

Thus tau explains the Nielsen decomposition but does not improve the optimum
adaptive decision complexity of the already rich W4 class-query pool.
"""

from __future__ import annotations
import importlib.util
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve()
CERTDIR = HERE.parent

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

a = load("h18_adaptive", CERTDIR / "h18_adaptive_depth4_certificate.py")
h = load("h18_higman", CERTDIR / "h18_higman_trace_lift_certificate.py")

N = len(a.REPS)
ALL_MASK = (1 << N) - 1
INF = 10**12

queries = [(q[0], q[1]) for q in a.QUERIES]
tau_vector = tuple(h.tau(x,y) for x,y in a.REPS)
queries.append(("TAU_COMMUTATOR_LIFT", tau_vector))

query_masks = []
for _, vector in queries:
    labels = sorted(set(vector))
    masks = []
    for label in labels:
        mask = 0
        for i, value in enumerate(vector):
            if value == label:
                mask |= 1 << i
        masks.append(mask)
    query_masks.append(tuple(masks))

def pc(mask):
    return mask.bit_count()

def parts(mask, qi):
    return tuple(mask & m for m in query_masks[qi] if mask & m)

@lru_cache(maxsize=None)
def feasible(mask, depth):
    if pc(mask) <= 1:
        return True
    if depth == 0:
        return False
    for qi in range(len(queries)):
        ps = parts(mask, qi)
        if len(ps) <= 1:
            continue
        if all(feasible(p, depth-1) for p in ps):
            return True
    return False

@lru_cache(maxsize=None)
def optimum(mask, depth):
    n = pc(mask)
    if n <= 1:
        return (0,0,-1)
    if depth == 0:
        return (INF,INF,-1)

    best = (INF,INF,-1)
    best_key = None
    for qi,(name,_) in enumerate(queries):
        ps = parts(mask, qi)
        if len(ps) <= 1:
            continue
        child = [optimum(p, depth-1) for p in ps]
        if any(x[0] >= INF for x in child):
            continue
        path_sum = n + sum(x[0] for x in child)
        nodes = 1 + sum(x[1] for x in child)
        key = (path_sum, nodes, len(name), name)
        if best_key is None or key < best_key:
            best_key = key
            best = (path_sum, nodes, qi)
    return best

def main():
    assert len(a.QUERIES) == 50
    assert len(queries) == 51
    assert feasible(ALL_MASK,3) is False
    assert feasible(ALL_MASK,4) is True

    path_sum,nodes,qi = optimum(ALL_MASK,4)
    assert path_sum == 382
    assert nodes == 48
    assert queries[qi][0] == "AAB"

    print("HATTER-SOL-18 H18-04 adaptive + tau certificate")
    print("class queries =", 50)
    print("extra Higman lift-trace query =", 1)
    print("depth<=3 possible =", feasible(ALL_MASK,3))
    print("depth<=4 possible =", feasible(ALL_MASK,4))
    print("minimum depth-4 total path length =", path_sum)
    print("minimum mean depth = 382/114 = 191/57 =", path_sum/N)
    print("selected optimum internal nodes =", nodes)
    print("selected optimum root =", queries[qi][0])
    print("PASS: tau explains dynamics but does not improve W4 adaptive optimum")

if __name__ == "__main__":
    main()
