# FCOA Hybrid Memory — FO Preprocessing Frontier Collapse

**Status:** CANONICAL ARTICLE-B NO-GO THEOREM; quantifier-free endpoint quarantined pending separate proof audit

## 1. Standard preprocessing model

For each `N`, let `X_N` be a distinguished `N`-element target sector inside a finite relational structure `A_N` over one fixed finite bounded-arity signature. Define total storage

\[
S(A_N)=|A_N|+\sum_R|R^{A_N}|.
\]

The canonical benchmark structures are

\[
B_0(N)=([N],<),
\]

\[
B_1(N)=([N],<,Add_N),
\]

\[
B_2(N)=([N],<,Add_N,Mul_N),
\]

where

\[
Add_N(x,y,z)\iff x+y=z<N,
\]

\[
Mul_N(x,y,z)\iff xy=z<N.
\]

For quantifier-rank budget `q`, let `sigma_j(q)` be the infimum storage exponent over presentations in which the relations of `B_j(N)` are recovered on the same target sector by fixed FO formulas of rank at most `q`.

The target sector itself gives the universal lower bound

\[
\sigma_j(q)\ge1.
\]

## 2. Linear-space order at constant FO rank

Take a two-coordinate representation with coordinate alphabets of size `Theta(sqrt N)`. Store the two coordinate maps for every target point and store the **complete strict order relations** on the coordinate alphabets. The complete coordinate orders cost `Theta(N)` tuples in total.

A fixed FO formula compares two target points lexicographically using their four coordinate witnesses. Hence for some constant `Q_0`,

\[
\sigma_0(q)=1\qquad(q\ge Q_0).
\]

Important: this construction uses the complete coordinate order as a primitive relation. It does **not** claim that FO can recover an unbounded total order from a sparse successor chain.

## 3. Linear-space addition at constant FO rank

Use a fixed two-digit representation with digit alphabet size `Theta(sqrt N)`. Store target-to-digit coordinate relations and a complete add-with-carry table on the digit alphabet. Both have total size `Theta(N)`. A fixed school-addition FO formula recovers `Add_N`.

Retaining the order layer from Section 2 gives, for some constant `Q_1`,

\[
\sigma_1(q)=1\qquad(q\ge Q_1).
\]

Equivalently, the two-channel CRT construction gives another linear-size constant-formula realization of exact addition.

## 4. Linear-space multiplication at constant FO rank

Add a complete digit multiply-and-split table on the `Theta(sqrt N)` digit alphabet. It has `Theta(N)` rows. Fixed-width school multiplication uses only constantly many digit-product and carry witnesses, so one fixed FO formula recovers `Mul_N`.

Thus for some constant `Q_2`,

\[
\sigma_2(q)=1\qquad(q\ge Q_2).
\]

## 5. FO Preprocessing Collapse Theorem

### Theorem HM-FOPC

There exists a constant

\[
Q=\max(Q_0,Q_1,Q_2)
\]

such that for all `q>=Q`,

\[
\boxed{\sigma_0(q)=\sigma_1(q)=\sigma_2(q)=1.}
\]

### Proof

Sections 2--4 give linear-size constructions with fixed FO formulas, hence upper exponent `1`. The target sector contains `N` elements, so total structure size is at least `N`, giving lower exponent `1`. `square`

Therefore unrestricted static preprocessing plus sufficiently expressive fixed-rank FO decoding does **not** separate the three canonical phases by total storage exponent.

## 6. Quantifier-free endpoint: not part of Article B theorem chain

An earlier draft asserted

\[
\sigma_0(0)=\sigma_1(0)=\sigma_2(0)=2.
\]

The intended argument uses finite atomic types and orientation of target pairs. That endpoint has not yet received the same hostile audit as HM-FOPC, especially for higher-arity atoms with repeated variables and named constants. It is therefore **quarantined** and must not be cited as an Article B theorem until separately re-proved.

The publication argument does not need it.

## 7. Consequence for the resource search

The collapse theorem rules out total storage exponent plus unrestricted constant-rank FO decoding as a persistent phase separator. This motivates a standard restriction on simultaneous logical coordination rather than another presentation-specific memory statistic.

The successful restriction is CQ variable width. See `EXISTENTIAL_PEBBLE_WIDTH_SEPARATION.md` for the width-3 base separation and `CQ8_EXACT_THRESHOLD.md` for the exact near-linear addition threshold `k_+=9`.

## 8. Claim ceiling

HM-FOPC concerns:

- a fixed finite bounded-arity relational signature;
- a distinguished target sector of size `N`;
- total preprocessing storage counting the whole structure;
- fixed FO formulas recovering the canonical target relations.

It does not imply an encoding-independent lower bound, and it does not distinguish AL1 from AL2 by storage exponent.
