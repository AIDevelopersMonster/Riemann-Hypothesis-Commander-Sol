#!/usr/bin/env python3
"""HATTER-SOL-18 H18-05: three projective shadow classes reconstruct Higman trace.

This certificate closes the structural bridge suggested after H18-04.

Let x=tr(A~), y=tr(B~), z=tr(A~B~), and
    tau=tr([A~,B~]) in F_7.
Define the three length-four shadow words
    Rz = AABB   = A^2 B^2
    Rx = ABAb   = A B A B^-1
    Ry = ABaB   = A B A^-1 B.

For any SL(2) lifts, the trace identities are
    tr(Rx)=x^2-tau,
    tr(Ry)=y^2-tau,
    tr(Rz)=z^2-tau.

Projectively, sigma(g)=tr(g~)^2 is well defined.  On the H17 generating
locus the triple
    (sigma(Rz), sigma(Rx), sigma(Ry))
reconstructs tau by the four-line decoder:

    if any coordinate is 0:             tau=4
    elif all three coordinates are 2:   tau=5
    elif at least two coordinates are 4:tau=6
    else:                               tau=3

The certificate proves:
  * the three identities on all 114 canonical H17 orbit states;
  * the four-line decoder on all 114 states;
  * no one or two W4 class queries determine tau;
  * exactly 16 W4 query triples determine tau; the shadow triple is one;
  * after collapsing 7A/7B orientation to projective trace-square, the same
    shadow triple still determines tau;
  * on all 7^3 Fricke trace triples with tau in {3,4,5,6}, the decoder fails
    at exactly seven triples, namely (0,0,0) and the six permutations/signs
    of (0,0,1);
  * every exceptional triple has at least two of x,y,z equal to zero;
  * no generating H17 pair can have two of x,y,z zero.

The last point has an elementary group-theoretic explanation: trace zero in
SL(2,7) gives a projective involution; if two among x,y,z vanish, a Nielsen-
equivalent generating pair consists of two involutions, hence generates a
dihedral group, not PSL(2,7).

No floating point arithmetic is used.
"""

from __future__ import annotations

import importlib.util
from itertools import combinations, product
from pathlib import Path

P=7
HERE=Path(__file__).resolve()
CERTDIR=HERE.parent

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    assert spec is not None and spec.loader is not None
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

a=load("h18_adaptive",CERTDIR/"h18_adaptive_depth4_certificate.py")
h=load("h18_higman",CERTDIR/"h18_higman_trace_lift_certificate.py")

REPS=a.REPS
QUERIES=a.QUERIES
TAUS=[h.tau(x,y) for x,y in REPS]
WORD_TO_QI={q[0]:i for i,q in enumerate(QUERIES)}

SHADOWS=("AABB","ABAb","ABaB")

def sigma_of_projective(g):
    vals={(h.mtrace(M)*h.mtrace(M))%P for M in h.SL_LIFTS[g]}
    assert len(vals)==1
    return next(iter(vals))

def shadow_sigmas(state):
    A,B=REPS[state]
    return tuple(sigma_of_projective(a.h17.eval_word(w,A,B)) for w in SHADOWS)

def decoder(s):
    if 0 in s:
        return 4
    if s==(2,2,2):
        return 5
    if s.count(4)>=2:
        return 6
    return 3

def determines_tau(indices):
    table={}
    for state in range(len(REPS)):
        key=tuple(QUERIES[i][1][state] for i in indices)
        t=TAUS[state]
        if key in table and table[key]!=t:
            return False
        table[key]=t
    return True

def mword_trace(word,A,B):
    table={"A":A,"a":h.minv(A),"B":B,"b":h.minv(B)}
    M=(1,0,0,1)
    for c in word:
        M=h.mmul(M,table[c])
    return h.mtrace(M)

def fricke_tau(x,y,z):
    return (x*x+y*y+z*z-x*y*z-2)%P

def shadow_squares_from_xyz(x,y,z,t):
    # order matches AABB, ABAb, ABaB = z-shadow, x-shadow, y-shadow
    return (((z*z-t)%P)**2%P,
            ((x*x-t)%P)**2%P,
            ((y*y-t)%P)**2%P)

def main():
    assert len(REPS)==114

    # Exact trace identities on all canonical generating states.
    for state,(pa,pb) in enumerate(REPS):
        A=h.SL_LIFTS[pa][0]
        B=h.SL_LIFTS[pb][0]
        x=h.mtrace(A)
        y=h.mtrace(B)
        z=h.mtrace(h.mmul(A,B))
        t=TAUS[state]
        assert t==fricke_tau(x,y,z)
        assert mword_trace("ABAb",A,B)==(x*x-t)%P
        assert mword_trace("ABaB",A,B)==(y*y-t)%P
        assert mword_trace("AABB",A,B)==(z*z-t)%P
        assert decoder(shadow_sigmas(state))==t

    # Minimal W4 query count for tau reconstruction.
    assert not any(determines_tau((i,)) for i in range(len(QUERIES)))
    assert not any(determines_tau(pair) for pair in combinations(range(len(QUERIES)),2))
    triples=[c for c in combinations(range(len(QUERIES)),3) if determines_tau(c)]
    assert len(triples)==16
    witness=tuple(WORD_TO_QI[w] for w in SHADOWS)
    assert determines_tau(witness)
    assert tuple(QUERIES[i][0] for i in witness)==SHADOWS

    # Orientation 7A/7B is not needed: trace-square shadows alone suffice.
    seen={}
    for state in range(len(REPS)):
        key=shadow_sigmas(state)
        t=TAUS[state]
        if key in seen:
            assert seen[key]==t
        seen[key]=t
    assert len(seen)==28

    # Structural finite-field sweep.
    bad=[]
    tested=0
    for x,y,z in product(range(P),repeat=3):
        t=fricke_tau(x,y,z)
        if t not in {3,4,5,6}:
            continue
        tested+=1
        s=shadow_squares_from_xyz(x,y,z,t)
        if decoder(s)!=t:
            bad.append((x,y,z,t,s,decoder(s)))

    expected_bad={
        (0,0,0,5),
        (0,0,1,6),(0,0,6,6),
        (0,1,0,6),(0,6,0,6),
        (1,0,0,6),(6,0,0,6),
    }
    assert {(x,y,z,t) for x,y,z,t,_,_ in bad}==expected_bad
    assert all(sum(v==0 for v in (x,y,z))>=2 for x,y,z,_,_,_ in bad)

    # A generating pair cannot have two trace-zero Fricke coordinates.
    # Zero is sign-independent for SL lifts.
    for pa,pb in REPS:
        A=h.SL_LIFTS[pa][0]
        B=h.SL_LIFTS[pb][0]
        x=h.mtrace(A); y=h.mtrace(B); z=h.mtrace(h.mmul(A,B))
        assert sum(v==0 for v in (x,y,z))<=1

    print("HATTER-SOL-18 H18-05 three-shadow reconstruction certificate")
    print("shadow words =",SHADOWS)
    print("minimum number of W4 class queries determining tau = 3")
    print("number of minimal W4 triples =",len(triples))
    print("distinct trace-square shadow triples on 114 states =",len(seen))
    print("Fricke triples tested with tau in {3,4,5,6} =",tested)
    print("decoder exceptions in full F7^3 trace space =",len(bad))
    for row in bad:
        print(" exception:",row)
    print("PASS: class-only short words reconstruct Higman trace on the generating locus")

if __name__=="__main__":
    main()
