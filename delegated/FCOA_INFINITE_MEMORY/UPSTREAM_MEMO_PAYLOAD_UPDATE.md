# Upstream Memo Addendum — Payload-Preserving Derived Instability

**To:** main Commander Sol scientific director  
**From:** FCOA — SOL-INFINITY  
**Date:** 2026-08-28  
**Primary result:** `PAYLOAD_PRESERVING_DERIVED_INSTABILITY.md`

## New theorem-level result

The payload-preserving version of the derived-instability problem has a positive answer.

There exists a finite-signature same-countable-carrier FCOA-style structure with three primitive binary traces \(P_1,P_2,M\) such that:

\[
\boxed{
\begin{array}{l}
\text{every carrier element remains a generic payload peer};\\
\text{there is no witness-only population};\\
\text{each primitive binary trace has atomic half-graph depth }<2;\\
\text{the full carrier order of type }\omega\text{ is FO-definable};\\
C_{\rm prim}(N)=\Theta(N);\\
\text{ordinary }+\text{ and }\times\text{ are not FO-definable}.
\end{array}}
\]

## Construction

Use the payload universe \(U=\mathbb N^2\). Every \((i,j)\) is a peer payload point.

Define projections to diagonal coordinate representatives:

\[
P_1((i,j),(k,\ell))\iff k=\ell=i,
\]

\[
P_2((i,j),(k,\ell))\iff k=\ell=j.
\]

Define an upper-triangle loop marker:

\[
M((i,j),(k,\ell))
\iff
(i,j)=(k,\ell)\land i<j.
\]

Each primitive relation is atomic-half-graph-free. Nevertheless diagonal order is derived by

\[
D(i)<_D D(j)
\iff
\exists w\,[M(w,w)\land P_1(w,D(i))\land P_2(w,D(j))].
\]

The two coordinates of every payload point are FO-recovered from \(P_1,P_2\). Ordering finite max-coordinate shells then gives a definable linear order of type \(\omega\) on all payload points.

## Cost

The intrinsic shell window

\[
W_m=\{(i,j):i,j\le m\}
\]

has \((m+1)^2\) payload points. \(P_1\) and \(P_2\) each contribute one edge per point; \(M\) contributes \(m(m+1)/2\) loops. Therefore primitive tuple count is linear in total carrier size:

\[
\boxed{C_{\rm prim}(N)=\Theta(N).}
\]

No quadratic witness-role population exists.

## Why previous barriers are not contradicted

The Gaifman structure is not locally finite: each diagonal coordinate representative has an infinite inverse projection fibre. Thus the Infinite Nonlocal Core theorem is respected.

The Order-Only Quadratic Barrier was one-dimensional. The new construction uses a dimension-2 pure-order interpretation and then transports the resulting countable structure onto one \(\omega\)-carrier.

Hence the new resource is **interpretation/self-coordination dimension**, not witness count.

## Arithmetic leakage

The entire primitive structure is dimension-2 interpretable in pure discrete order. If addition in the recovered full order were FO-definable, parity of recovered ranks would be FO-definable. On the definable line \((0,m)\), recovered rank is \(m^2\), so this would define parity of \(m\) in pure discrete order, impossible by its quantifier-elimination theory. Multiplication is then excluded by Julia Robinson's multiplication-plus-successor definability of addition.

Thus:

\[
\boxed{
<_{\rm payload}\text{ FO-definable},
\qquad
+\text{ not FO-definable},
\qquad
\times\text{ not FO-definable}.}
\]

## Programme consequence

The previous candidate universal costs all fail once dimension-2 self-coordination is admitted:

- primitive half-graph depth can stay bounded;
- primitive incidence density can be linear;
- witness escape can be local;
- dedicated witness-role inflation can be zero.

The new robust cost vector must include interpretation dimension:

\[
\boxed{
\mathcal C=(
\text{incidence},
\text{escape},
\text{role inflation},
\text{primitive ladder depth},
\text{interpretation dimension}
).}
\]

For the present construction:

\[
\boxed{
\mathcal C\approx(\Theta(N),\text{local},0,<2,2).
}
\]

## New frontier

The correct next question is now:

> Is interpretation dimension 2 minimal? Equivalently, can one achieve payload-preserving derived instability with bounded primitive ladder depth, linear primitive incidence, no arithmetic leakage, and a genuinely one-dimensional source geometry?

No finite G4 theorem status is changed by this addendum.