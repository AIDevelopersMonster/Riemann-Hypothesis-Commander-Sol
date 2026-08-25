# Version 1.1 notes — Prime-Successor Fixed-Ball Interior

**Date:** 2026-08-25  
**Published DOI:** https://doi.org/10.5281/zenodo.22101603  
**Nature of revision:** post-publication clarification; no change to the principal mathematical result.

## Summary

Version 1.1 records clarifications prompted by a second adversarial review of the published fixed-ball manuscript. The review did not identify a counterexample to Mixed Quantifier Compression, Formula-Relative Tail Symmetry, non-definability of prime order/successor, or finite GIR. The revision therefore strengthens proof exposition rather than changing theorem statements.

## Changes

### 1. Definability of the fixed subgroup chain

The proof now explicitly states, for \(m>0\),

\[
B_m(x)\iff \exists y\,(13^m y=x\land B(y)),
\qquad
B_{-m}(x)\iff B(13^m x).
\]

This makes clear that the full fixed chain \(\{B_m\}\) is only a definitional expansion of the original target language \((\mathbb Q,+,0,B)\).

### 2. Private Denominator calculation

The valuation calculation is written out explicitly. If

\[
\tau(p)=p^ab,
\qquad p\nmid b,
\]

then Deligne's estimate gives \(a\le5\), so

\[
11-2a\in\{1,3,5,7,9,11\},
\]

and

\[
p\nmid b^2-p^{11-2a}.
\]

Hence

\[
v_p(u_p)=2a-11<0.
\]

### 3. Injectivity of good labels

A separate corollary now records

\[
p\ne q\text{ good}\Longrightarrow u_p\ne u_q.
\]

### 4. Compatibility of multiple pinning equations

The pinned case of Target-Witness Transport now explicitly checks that

\[
a_1y+t_1=0,
\qquad
a_2y+t_2=0
\]

are compatible exactly when

\[
a_2t_1-a_1t_2=0.
\]

The compatibility condition belongs to the finite target-template closure and is therefore preserved by the inductive transport invariant.

### 5. Multiplicity-Blind Bridge Principle

Version 1.1 isolates the structural fact that the bridge \(U_\Delta\) is defined on prime atoms only. It does not transmit the exponent of \(p^k\) to a target depth, to \(ku_p\), or to a subgroup \(B_k\). This is stated separately from the stronger No Scale Synchronization consequence.

### 6. Zero primes and the successor argument

If \(\tau(p)=0\), then

\[
u_p=-1.
\]

Thus all zero primes form one exact common-label movable class. The successor proof is reformulated using the finite formula-relative partition of the whole prime tail. It therefore does not require Lehmer nonvanishing or Serre's density-zero theorem. Serre's result may be cited as external context, but not as a logical premise.

### 7. Right-wall language

The programme diagram

\[
(\mathbb N_{>0},\times)<\mathcal B_\Delta<\text{right-wall grid regime}
\]

is clarified as a comparison of concrete definability/grid-amplification behaviour:

- the fixed-ball structure defines a specific prime atom (13), unlike pure prime-permutation symmetry;
- every fixed isolator in the fixed-ball structure has finite GIR;
- the previously studied right-wall structures admit explicit fixed relations with infinite GIR.

No global interpretability preorder is claimed by this notation.

## Unchanged conclusions

Version 1.1 leaves unchanged:

\[
S_{\mathbb P}\notin\operatorname{Def}(\mathcal B_\Delta),
\qquad
<_{\mathbb P}\notin\operatorname{Def}(\mathcal B_\Delta),
\]

and

\[
\forall I\quad \operatorname{GIR}(I)<\infty.
\]

It also leaves unchanged the explicit definability of prime 13 and the programme-level conclusion that the fixed-ball structure realizes an interior layer between the left symmetry wall and the known infinite-grid amplification mechanisms.

## Scope retained

The revision does not claim decidability of the complete theory, non-interpretability of full arithmetic by every possible interpretation, an explicit effective \(\Phi\mapsto K_\Phi\), or historical priority for the general model-theoretic mechanisms.
