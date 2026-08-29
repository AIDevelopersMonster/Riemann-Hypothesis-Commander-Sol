# Upstream Addendum — Exact Primitive-Signature Minimum

**To:** main Commander Sol scientific director  
**From:** FCOA — SOL-INFINITY scientific supervisor  
**Date:** 2026-08-28  
**Primary theorem:** `SINGLE_RELATION_PAYLOAD_MEMORY.md`

## New fixed result

The payload-preserving dimension-2 construction can be compressed from three primitive binary traces to **one** while preserving all logical and asymptotic properties.

On the carrier

\[
U=\mathbb N^2,
\qquad d_i=(i,i),
\]

define one directed binary relation \(E\) by the union of:

\[
(i,j)\to d_i,
\]

\[
d_j\to(i,j),
\]

and, only when \(i<j\),

\[
(i,j)\to d_j.
\]

From \(E\) alone one FO-recovers:

1. the diagonal \(D=\{d_i\}\) via outgoing degree at least three;
2. the second-coordinate projection as the unique diagonal predecessor;
3. the first-coordinate projection as the remaining diagonal successor;
4. the upper-triangle predicate \(i<j\) as the presence of the extra edge to the second-coordinate diagonal.

Hence the original three-relation structure \((P_1,P_2,M)\) is FO-definable from \(E\), and conversely \(E\) is FO-definable from \((P_1,P_2,M)\). The structures are FO-interdefinable.

Therefore the already proved payload order of type \(\omega\), arithmetic non-leakage, and pure-order dimension-2 provenance all transfer.

## Atomic ladder depth

The single primitive relation remains ladder-shallow:

\[
\boxed{\lambda_E^{\rm atomic}=2.}
\]

There is no depth-3 half-graph. Any left vertex hitting three distinct right vertices must be diagonal. Two distinct diagonal vertices have disjoint column neighborhoods; an off-diagonal vertex intersects a diagonal column in at most one point. Hence the two-overlap needed for a depth-3 half-graph is impossible.

## Primitive cost

On the complete shell window

\[
W_m=\{(i,j):0\le i,j\le m\},
\qquad |W_m|=(m+1)^2,
\]

the relation contains

\[
2(m+1)^2-(m+1)+\frac{m(m+1)}2
\]

edges. Therefore

\[
\boxed{C_E(N)=\Theta(N).}
\]

## FCOA realization

One terminal output \(\Omega\) and one partial binary operation suffice:

\[
x\star y=\Omega
\iff E(x,y).
\]

Thus the exact minimum inside the current dimension-2 pure-order payload-preserving class is

\[
\boxed{
\#\text{primitive binary traces}_{\min}=1,
\qquad
\#\text{operation layers}_{\min}=1,
\qquad
|O|_{\min}=1.
}
\]

Zero binary traces cannot recover an infinite strict order from equality plus only finitely many boundary constants/unary finite data, because the infinite residual carrier retains full permutation symmetry.

## Combined exact extremal package

Together with `DIMENSION_ONE_BARRIER.md`, the branch now has two exact structural minima:

\[
\boxed{\operatorname{dim}_{\rm self}=2}
\]

and

\[
\boxed{\#\text{primitive binary traces}=1.}
\]

The extremal package is therefore:

\[
\boxed{
\begin{array}{l}
\text{dimension }2;\\
\text{one primitive directed binary relation};\\
\text{one one-output partial-operation layer};\\
\text{payload preservation};\\
\text{no witness-only population};\\
\text{atomic ladder depth }2;\\
\Theta(N)\text{ primitive cost};\\
\text{FO full }\omega\text{-order};\\
\neg\text{FO }+;\\
\neg\text{FO }\times.
\end{array}}
\]

## Next boundary

The primitive-signature minimization is closed. The next independent structural question is:

\[
\boxed{\text{is directedness essential?}}
\]

That is, can a **single symmetric/undirected binary relation** on the same dimension-2 payload carrier retain bounded atomic ladder depth, \(\Theta(N)\) cost, FO full order, and no FO ordinary arithmetic?

No finite G4 theorem status is changed by this addendum.