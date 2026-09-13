# HATTER-SOL-09 — Two-block world feasibility

Status: exact complete-support reduction for two arithmetic typed blocks; verified lattice-front witness 65. The earlier explicit Gamma formula has been withdrawn after audit: it was a parity-factor criterion, not a general `(g,f)`-factor criterion.

## 1. Two split blocks

Consider a typed profile

\[
\Pi=(P_1,Q_1)^{n_1}\cup(P_2,Q_2)^{n_2},
\]

with `n_1,n_2>=1`, and put

\[
N=n_1+n_2,
\qquad c=N-1.
\]

We ask whether the support may be the whole complete graph `K_N` while respecting the P/Q capacities.

Choose the P-colored subgraph `H`. Every edge not in `H` is then Q-colored. A vertex of block `j` must satisfy

\[
\max(0,c-Q_j)\le d_H(v)\le\min(P_j,c).
\]

Define

\[
\boxed{g_j:=\max(0,c-Q_j),\qquad f_j:=\min(P_j,c).}
\]

### Theorem 1.1 — exact reduction

Complete typed support exists if and only if `K_N` has a `(g,f)`-factor with block-constant lower and upper degree bounds `g_j,f_j`.

### Proof

If a complete typed support exists, let `H` be its P-edge subgraph. Since every non-P edge is Q-colored,

\[
d_Q(v)=c-d_H(v).
\]

The conditions `d_H(v)<=P_j` and `d_Q(v)<=Q_j` are exactly

\[
\max(0,c-Q_j)\le d_H(v)\le\min(P_j,c).
\]

Conversely, any spanning subgraph `H` satisfying these bounds may be colored P, with its complement in `K_N` colored Q, producing a capacity-respecting complete typed support. □

This reduction is classical graph theory. The HATTER-SOL-specific layer is that the interval bounds are generated canonically by arithmetic factor blocks.

## 2. What the audit changed

An earlier draft wrote an explicit four-variable obstruction function `Gamma` using an odd-component parity correction and claimed it characterized arbitrary `(g,f)`-factors.

That statement is withdrawn.

The audited formula is a Lovasz-type criterion for **parity factors**, not for unrestricted `(g,f)`-factors. Our typed complete-support problem is an unrestricted interval-degree factor problem unless an additional parity constraint is imposed.

Therefore the following are retained as proved:

1. the exact reduction in Theorem 1.1;
2. polynomial-time decidability by standard `(g,f)`-factor machinery;
3. the verified explicit arithmetic witnesses below.

The following are **not yet claimed**:

- a closed four-variable necessary-and-sufficient obstruction formula for arbitrary two-block profiles;
- a scalar world obstruction margin derived from that withdrawn formula.

A low-dimensional block criterion remains an open target.

## 3. First genuine two-split-block witness: 65

### Square world

Both rational primes split:

\[
5\rightsquigarrow(2,1)^2,
\qquad
13\rightsquigarrow(3,2)^2.
\]

Hence

\[
\boxed{
\Pi_G(65)=(2,1)^2\cup(3,2)^2.
}
\]

There are four factor vertices. The total typed capacity is

\[
\sum P_i=10,
\qquad
\sum Q_i=6.
\]

Complete support `K_4` has six edges, so every complete-support boundary point satisfies

\[
B_P+B_Q=10+6-12=4.
\]

All three nonnegative parity-compatible points are attainable:

\[
\boxed{
\partial_P\mathfrak B_G^{(2)}(65)
=
\{(4,0),(2,2),(0,4)\}.
}
\]

Explicit realizations, with split vertices `A,B` of type `(2,1)` and `C,D` of type `(3,2)`:

- `(4,0)`: P-edges `AB, AC, BD`; the complementary Q-graph has degrees `(1,1,2,2)`.
- `(2,2)`: choose a 4-cycle as the P-graph; the complementary Q-graph is a perfect matching.
- `(0,4)`: let `AB` be the unique Q-edge and color the other five edges P; P-degrees are `(2,2,3,3)`.

Each realization respects every typed capacity. Since all complete-support points have the minimum possible scalar sum `4`, and the three displayed points exhaust the possible even P-boundaries on that line, this is the exact Pareto frontier.

Thus the square world produces the first Pareto segment with an interior lattice point.

### Triangular world

Here `5` is inert while `13` splits with folded pair `(3,1)`:

\[
\boxed{
\Pi_E(65)=(5,0)\cup(3,1)^2.
}
\]

The support is `K_3`. The two axial-to-split edges are forced P. The split-split edge may be P or Q. Therefore

\[
\boxed{
\partial_P\mathfrak B_E^{(2)}(65)
=
\{(7,0),(5,2)\}.
}
\]

So changing the arithmetic world changes not merely a scalar boundary value but the combinatorial shape of the typed Pareto frontier:

\[
3\text{ lattice points in the square world}
\quad\text{versus}\quad
2\text{ in the triangular world}.
\]

## 4. Safe pre-operator data

Until an exact block obstruction formula is proved, the canonical world data retained are

\[
\boxed{
R\longmapsto
\left(
\mathcal P_R(n),
\partial_P\mathfrak B_R^{(2)}(n)
\right).
}
\]

The first component is the arithmetic typed factor profile; the second is the network response.

A future world operator should be built only after a natural comparison map between these world-dependent response objects is established.

No world Laplacian is defined yet.

## 5. Next target

Derive an exact block criterion for two block-constant interval degree classes directly, without importing a parity-factor theorem. Possible routes:

1. exploit symmetry of `K_N` to characterize feasible block degree totals;
2. formulate the problem as a small-dimensional `b`-matching / flow polytope after equitable symmetrization;
3. determine whether every feasible fractional block point admits an integral realization, and identify the parity corrections if not.

Only after this is closed should a scalar obstruction landscape be reintroduced.
