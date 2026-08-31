# Minimal-Signature Review Audit 0.1

**Date:** 2026-08-31

## 1. What is accepted

The programme should move from operator-first design to task-driven carrier/signature co-design. The right optimisation target is not a visually simple formula but the weakest internal structure that makes the target phenomenon definable while keeping forbidden structure non-interpretable.

## 2. Corrections to the review

### 2.1 A pure carrier does not inherit external order/topology

A set such as \(\mathbb N\), when used in the empty language, is internally just a pure set with equality. The ordinary order, topology and arithmetic on the external labels are not present unless they are named or definable from the chosen signature.

Hence the correct danger is not `carrier leakage` in the literal sense, but **representation/carrier-structure leakage**: external coordinates become a problem only when the signature makes them internally recoverable.

### 2.2 Relational does not mean weaker

Every function can be replaced by its graph relation. For example,

\[
A(x,y,z)\iff x+y=z
\]

and

\[
M(x,y,z)\iff xy=z
\]

are purely relational presentations of addition and multiplication. Therefore switching from functions to relations does not by itself reduce expressive power.

The correct rule is:

\[
\boxed{\text{weakest-information first, not relations first}.}
\]

A relation is preferable only when it deliberately forgets information that a functional graph would retain.

### 2.3 Primitive VC bounds are insufficient

Finite VC-dimension for one primitive relation does not establish NIP for the whole theory. NIP is a theory/formula-level condition controlling every definable family. If NIP is used as an anti-arithmetic barrier, it must be proved for the full first-order theory (or uniformly for the relevant class), not merely checked on the generating relation.

### 2.4 Automorphisms are a diagnostic, not a complete definability test

Automorphism invariance is necessary for parameter-free definability, but in arbitrary infinite structures it is not automatically sufficient. Rigidity and definability power must remain separate audit axes.

## 3. Prime-Successor Skeleton Collapse

Let

\[
\mathcal P_S=(\mathbb P;S_P)
\]

where

\[
S_P(p,q)\iff q\text{ is the next prime after }p.
\]

Write the primes increasingly as \(p_1<p_2<\cdots\). The map

\[
p_n\longmapsto n
\]

is an isomorphism between \(\mathcal P_S\) and the one-way successor chain

\[
(\mathbb N_{\ge 1};S),\qquad S(n,m)\iff m=n+1.
\]

Therefore \(\mathcal P_S\) contains no prime-specific distributional information beyond the fact that the primes form a countable sequence with a first element and a successor relation.

In particular, replacing \(\mathbb P\) by any other countably infinite sequence and retaining only its successor relation yields the same isomorphism type.

### Prime-Successor Skeleton Collapse Theorem

A pure prime carrier equipped only with the next-prime relation is structurally indistinguishable from a generic rooted \(\omega\)-chain. Consequently it cannot, by itself, encode prime-gap irregularity or any other prime-specific metric/distributional phenomenon.

This is the opposite failure mode from arithmetic leakage: the signature is now **too weak** and erases the target phenomenon.

## 4. Prime-Specificity Test

Any proposed FCOA representation of prime structure should pass the following test:

> If the same signature, placed on every arbitrary strictly increasing countable sequence, always gives an isomorphic structure, then the signature has erased prime-specific information and cannot serve as a sufficient model for a prime-distribution problem.

Thus successful design must lie between two walls:

\[
\boxed{\text{target erasure} < \text{admissible structure} < \text{arithmetic leakage}.}
\]

## 5. Revised Minimal Structure Protocol

Given a target phenomenon \(Q\) and forbidden structure \(A\):

1. Fix what information about \(Q\) must remain invariantly observable.
2. Choose a carrier presentation without assuming external labels are internal.
3. Add the weakest relations/partial functions needed to retain that information.
4. Prove a **sufficiency test**: the target phenomenon has not been erased.
5. Prove a **leakage test**: the forbidden structure is not definable/interpretable.
6. Prove representation invariance: conclusions depend only on the isomorphism type, not on external names.
7. Minimise in the reduct/definability order, not merely by counting symbols.

## 6. Programme-level conclusion

The correct optimisation problem is two-sided:

\[
\boxed{
\text{retain enough structure to see the phenomenon, but not enough to reconstruct the forbidden machine.}
}
\]

For the prime programme, the purely relational successor skeleton is therefore useful as a **lower baseline**, not as a final model.
