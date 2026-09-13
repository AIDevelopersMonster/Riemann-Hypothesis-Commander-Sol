# HATTER-SOL-09 — Axial + split block theorem

Status: closed theorem in the 07-faithful simple-support typed model.

## 1. Profile

Consider

\[
\Pi=(a,0)^r\cup(P,Q)^n,
\qquad n=2m,
\]

with `r>=1`, `m>=1`, `P>=Q>=0`, and put `N=r+n`.

The `r` axial vertices have no Q-capacity. The `n` split vertices form an even arithmetic block.

## 2. Complete-support criterion

Assume the support is the complete graph `K_N`.

Every edge incident with an axial vertex must be P-type. Hence every axial vertex has forced P-degree `N-1`, so necessarily

\[
 a\ge N-1.
\]

A split vertex already uses `r` P-edges toward the axial block. If its internal P-degree is `d`, then its internal Q-degree is `n-1-d`. Therefore

\[
\max(0,n-1-Q)\le d\le\min(n-1,P-r).
\]

Because `n` is even, every integer degree `d` in `[0,n-1]` has a regular realization on the split block.

### Theorem 2.1

Complete typed support `K_N` exists if and only if

\[
\boxed{a\ge N-1}
\]

and

\[
\boxed{P+\min(Q,n-1)\ge N-1.}
\]

The second condition is exactly non-emptiness of the admissible internal P-degree interval.

## 3. Exact Pareto frontier in the complete-support regime

Assume Theorem 2.1 holds. Define

\[
D:=ra+n(P+Q)-N(N-1),
\]

\[
L_P:=r(a-N+1)+n(P-N+1)_+,
\]

\[
L_Q:=n(Q-n+1)_+.
\]

Every complete-support realization satisfies

\[
B_P+B_Q=D.
\]

### Theorem 3.1

The global typed Pareto frontier is

\[
\boxed{
\partial_P\mathfrak B^{(2)}(\Pi)
=
\{(B_P,B_Q):
B_P+B_Q=D,
\ L_P\le B_P\le D-L_Q,
\ B_P\equiv ra+nP\pmod 2\}.
}
\]

Since `n` is even, the parity condition may be written `B_P congruent ra mod 2`.

### Proof

All axial-axial and axial-split edges are forced P-edges. Within the split block let

\[
l:=\max(0,n-1-Q),
\qquad
u:=\min(n-1,P-r).
\]

For every integer edge count

\[
\frac{nl}{2}\le e\le\frac{n\nu}{2},
\]

there exists a simple graph on the split block with `e` edges and all degrees between `l` and `nu`: take an almost-regular realization. Color those edges P and the complementary split-block edges Q. This realizes every parity-compatible boundary point between the two coordinate minima.

The absolute P-boundary minimum is obtained by saturating all possible P-incidences. Axial vertices contribute `r(a-N+1)`, while each split vertex has unavoidable excess `(P-N+1)_+`; this gives `L_P`. Q-edges occur only inside the split block, so their absolute boundary minimum is `L_Q`.

Any incomplete support uses fewer than `N(N-1)/2` edges and hence has strictly larger total boundary. Its P- and Q-edge counts are each bounded by the corresponding maxima used above, so one can choose a complete-support realization with at least as many edges of each type. Thus every incomplete-support point is dominated by a point on the displayed segment. QED.

## 4. Witness 6

Square world:

\[
\Pi_G(6)=(3,0)\cup(1,1)^2.
\]

The theorem gives

\[
\boxed{\partial_P\mathfrak B_G^{(2)}(6)=\{(1,0)\}.}
\]

Triangular world:

\[
\Pi_E(6)=(2,0)\cup(1,1)^2,
\]

so

\[
\boxed{\partial_P\mathfrak B_E^{(2)}(6)=\{(0,0)\}.}
\]

Thus 6 is an exact heterogeneous closure separator.

## 5. Scalar-collision witness 15

Square world:

\[
\Pi_G(15)=(3,0)\cup(2,1)^2,
\]

and

\[
\boxed{\partial_P\mathfrak B_G^{(2)}(15)=\{(1,2),(3,0)\}.}
\]

Triangular world:

\[
\Pi_E(15)=(5,0)\cup(1,1)^2,
\]

and

\[
\boxed{\partial_P\mathfrak B_E^{(2)}(15)=\{(3,0)\}.}
\]

In both worlds the scalar minimum is 3, but the typed Pareto frontiers differ. Therefore 15 is the first heterogeneous analogue of the prime-37 scalar collision.

## 6. Consequence

For one axial block plus one even split block, arithmetic symmetry collapses the heterogeneous two-color problem to one interval of internal split degrees. The resulting Pareto frontier is an exact parity segment rather than a generic hard packing instance.

Next target: two even split blocks and the geometry of the resulting block-feasibility region.
