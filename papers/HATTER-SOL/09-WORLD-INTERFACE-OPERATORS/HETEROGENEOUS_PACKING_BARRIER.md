# HATTER-SOL-09 · Heterogeneous typed profiles

Status: structural reduction + first tractable arithmetic subclass.

## 1. Saturation core

For a heterogeneous typed profile

\[
\Pi=((P_1,Q_1),\ldots,(P_k,Q_k)),
\qquad P_i\ge Q_i\ge0,
\]

exact typed saturation

\[
\mathbf B=(0,0)
\]

is equivalent, before the separate connected-support requirement, to finding two edge-disjoint simple graphs on the same labelled vertex set with degree sequences exactly

\[
P=(P_i),\qquad Q=(Q_i).
\]

So the algebraic closure core is a degree-sequence packing problem. This explains why the heterogeneous case does not collapse to the one-color b-matching formula from HATTER-SOL-07.

## 2. Arithmetic structure

Profiles coming from a positive rational integer have extra structure:

- an inert prime contributes factors of type `(p,0)`;
- a split prime contributes a positive-Q typed pair `(P,Q)` with even multiplicity;
- the ramified factor also contributes an even positive-Q block.

Thus every positive-Q factor type occurs in an even block.

## 3. One-step subclass

Assume

\[
Q_i\in\{0,1\}
\]

for every vertex. In an arithmetic profile, the number of `Q_i=1` vertices is automatically even, so `Q` is graphic: it is a matching degree sequence.

Moreover `Q` is almost regular.

A classical packing result of Kundu implies that, for this subclass, the degree sequences `P` and `Q` can be packed if and only if

1. `P` is graphic; and
2. `P+Q` is graphic.

Thus this arithmetic subclass reduces to two ordinary graphic-sequence tests.

## 4. Exact heterogeneous witness: n=6

### Square / Gaussian world

Up to units,

\[
2=(1+i)^2,
\]

while `3` is inert. Hence the typed factor profile is

\[
\mathcal P_G(6)=\{(1,1),(1,1),(3,0)\}.
\]

So

\[
P_G=(1,1,3),\qquad Q_G=(1,1,0).
\]

On three vertices the sequence `P_G` is not graphic because one requested degree is `3>2`. Exact typed saturation is impossible.

However the complete support `K_3` is feasible: color the two edges incident with the inert node by `P`, and color the edge between the two ramified nodes by `Q`. This yields

\[
(d_P;d_Q)=((1,1,2);(1,1,0)),
\]

hence

\[
\boxed{\mathbf B_G(6)=(1,0).}
\]

This dominates every other connected typed realization, so

\[
\boxed{\partial_P\mathfrak B_G^{(2)}(6)=\{(1,0)\}.}
\]

### Triangular / Eisenstein world

Here `2` is inert and `3` ramifies. The typed factor profile is

\[
\mathcal P_E(6)=\{(1,1),(1,1),(2,0)\}.
\]

Thus

\[
P_E=(1,1,2),\qquad Q_E=(1,1,0).
\]

The `P` graph is the two-edge path centered at the inert `(2,0)` node. The `Q` graph is the remaining edge between the two ramified nodes. They are edge-disjoint and together form `K_3`.

Therefore

\[
\boxed{\partial_P\mathfrak B_E^{(2)}(6)=\{(0,0)\}.}
\]

Hence

\[
\boxed{6:\quad (1,0)_\square\ \text{versus}\ (0,0)_\triangle.}
\]

This is the first exact heterogeneous world-separation witness in the branch.

## 5. Research consequence

Do not search for one universal closed heterogeneous typed-deficiency formula. Instead exploit arithmetic subclasses:

- uniform blocks: solved in `PARETO_DYNAMICS.md`;
- one-step profiles `Q_i in {0,1}`: reduced to graphicness tests;
- general block profiles: next target.

The future world operator, if it appears, should act on the resulting typed boundary data, not on an arbitrary unconstrained heterogeneous degree-packing problem.
