# HATTER-SOL-09 · Typed boundary region in the 07-faithful model

## 1. Why a region, not a scalar

Use the conservative simple-support model: each unordered pair of factor vertices carries at most one edge total, typed `P` or `Q`.

For a typed profile `((P_j,Q_j))`, define

\[
B_P=\sum_j P_j-2|E_P|,
\qquad
B_Q=\sum_j Q_j-2|E_Q|.
\]

Define the attainable typed boundary set

\[
\boxed{
\mathfrak B^{(2)}
:=
\{(B_P,B_Q):\text{admissible connected typed simple-support networks}\}.
}
\]

Its Pareto-minimal subset is denoted

\[
\boxed{\partial_P\mathfrak B^{(2)}}.
\]

The ordinary HATTER-SOL scalar boundary is the projection

\[
(B_P,B_Q)\mapsto B_P+B_Q.
\]

Thus scalarization can identify different typed boundary regions.

## 2. Exact two-node theorem

Consider two identical typed nodes with capacities

\[
(P,Q),\qquad P\ge Q>0.
\]

Connectivity forces exactly one support edge. It can have type `P` or type `Q`.

Therefore the full attainable set is already the Pareto frontier:

\[
\boxed{
\partial_P\mathfrak B^{(2)}(P,Q)
=
\{(2P-2,2Q),\ (2P,2Q-2)\}.
}
\]

Both points have the same scalar sum

\[
\boxed{2(P+Q)-2.}
\]

Hence the scalar HATTER-SOL boundary sees only

\[
S=P+Q.
\]

But the two differences are

\[
(2P-2)-2Q=2(P-Q)-2,
\]

\[
2P-(2Q-2)=2(P-Q)+2.
\]

Their midpoint is

\[
\boxed{2(P-Q).}
\]

Thus the typed Pareto frontier recovers

\[
S=P+Q,
\qquad
A=P-Q,
\]

and therefore

\[
\boxed{
P=\frac{S+A}{2},
\qquad
Q=\frac{S-A}{2}.
}
\]

### Theorem 2.1

For a two-node split-factor profile with `Q>0`, the typed Pareto frontier determines the canonical typed capacity pair `(P,Q)` exactly.

Consequently the forgetful scalar projection is genuinely lossy whenever two worlds have the same `P+Q` but different `P-Q`.

## 3. Prime 37 as exact witness

The rational prime `37` splits in both worlds.

Square world:

\[
\Pi_G(37)=(6,1).
\]

Hence

\[
\boxed{
\partial_P\mathfrak B_G^{(2)}(37)
=
\{(10,2),(12,0)\}.
}
\]

Triangle world:

\[
\Pi_E(37)=(4,3).
\]

Hence

\[
\boxed{
\partial_P\mathfrak B_E^{(2)}(37)
=
\{(6,6),(8,4)\}.
}
\]

In both worlds the scalar sum is

\[
12.
\]

Therefore

\[
\boxed{
\Lambda_G(37)=\Lambda_E(37)=12,
}
\]

but

\[
\boxed{
\partial_P\mathfrak B_G^{(2)}(37)
\ne
\partial_P\mathfrak B_E^{(2)}(37).
}
\]

This distinction survives entirely inside the original simple-graph support rule of HATTER-SOL-07.

## 4. Anisotropy readout

Define the typed-boundary imbalance coordinate

\[
\delta(B_P,B_Q)=B_P-B_Q.
\]

For the two-node frontier, the two imbalance values are

\[
2A-2,\qquad 2A+2,
\]

where

\[
A=P-Q.
\]

Hence

\[
\boxed{
A=rac14\left(\delta_-+\delta_+\right).
}
\]

For `37`:

- square: imbalance values `8,12`, so `A_G=5`;
- triangle: imbalance values `0,4`, so `A_E=1`.

Thus `37` is a scalar collision but a typed-boundary separation.

## 5. Significance for the future world operator

A scalar field on worlds,

\[
R\mapsto\Lambda_R(n),
\]

is too coarse: for `n=37` it assigns the same value to the square and triangular worlds.

The natural object is instead set/vector-valued:

\[
\boxed{
R\mapsto\partial_P\mathfrak B_R^{(2)}(n).
}
\]

Any future operator of worlds should therefore be tested first on typed boundary data, not only on the scalar `Lambda_R(n)`.

A possible later scalar observable is the recovered anisotropy `A_R(n)`, but no Laplacian is introduced yet.

## 6. Next obligation

Generalize the exact two-node frontier to `2m` identical typed nodes and determine which parts of `(P,Q)` survive in the Pareto frontier before full closure. This is the next theorem target.
