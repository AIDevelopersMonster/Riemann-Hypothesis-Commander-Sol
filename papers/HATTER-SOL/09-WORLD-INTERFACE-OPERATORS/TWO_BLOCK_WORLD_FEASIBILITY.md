# HATTER-SOL-09 — Two-block world feasibility

Status: exact complete-support reduction for two arithmetic typed blocks; first lattice-front witness 65.

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

Thus complete-support feasibility is exactly the existence of a `(g,f)`-factor of `K_N` with block-constant lower and upper degree bounds.

This reduction is classical graph theory. The HATTER-SOL-specific part is that the bounds are generated canonically by arithmetic factor blocks.

## 2. Symmetry reduction to four integers

Lovasz's `(g,f)`-factor criterion ranges over disjoint vertex sets `S,T`. Because `g` and `f` are constant on each arithmetic block, only the block counts matter.

Put

\[
s_j:=|S\cap V_j|,
\qquad
t_j:=|T\cap V_j|,
\]

with

\[
0\le s_j,t_j,
\qquad s_j+t_j\le n_j.
\]

Let

\[
s=s_1+s_2,
\qquad t=t_1+t_2,
\qquad u=N-s-t.
\]

If `u>0`, the residual graph `K_N-(S\cup T)` is one connected component. Define the parity term

\[
\epsilon(s_1,s_2,t_1,t_2)
=
\begin{cases}
1,&u>0\text{ and }g(U)+ut\text{ is odd},\\
0,&\text{otherwise},
\end{cases}
\]

where

\[
g(U)=(n_1-s_1-t_1)g_1+(n_2-s_2-t_2)g_2.
\]

Then the complete-graph `(g,f)` obstruction is

\[
\boxed{
\Gamma_\Pi(s_1,s_2,t_1,t_2)
=
s_1f_1+s_2f_2
+t_1(c-g_1)+t_2(c-g_2)
-st
-\epsilon.
}
\]

### Theorem 2.1

Assume `g_j<=f_j` for both blocks. Complete typed support exists if and only if

\[
\boxed{
\Gamma_\Pi(s_1,s_2,t_1,t_2)\ge0
}
\]

for every admissible integer quadruple `(s_1,s_2,t_1,t_2)`.

Hence an apparently exponential vertex-subset condition collapses, for a two-block arithmetic profile, to a four-dimensional finite lattice check.

## 3. World obstruction margin

Define

\[
\boxed{
\mu(\Pi):=
\min\Gamma_\Pi(s_1,s_2,t_1,t_2).
}
\]

Then

\[
\boxed{
\mu(\Pi)\ge0
\iff
K_N\text{ admits a capacity-respecting P/Q coloring}.
}
\]

The argmin set should be retained as data:

\[
\boxed{
\mathcal M(\Pi):=\operatorname{Argmin}\Gamma_\Pi.
}
\]

Two worlds may have the same scalar margin but different minimizing block cuts. This makes `(mu,M)` a more informative pre-operator observable than the old scalar HATTER-SOL boundary alone.

For `b` arithmetic blocks the same symmetry argument gives `2b` count coordinates `(s_1,...,s_b,t_1,...,t_b)`.

## 4. First genuine two-split-block witness: 65

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

All three possible nonnegative parity points are attainable:

\[
\boxed{
\partial_P\mathfrak B_G^{(2)}(65)
=
\{(4,0),(2,2),(0,4)\}.
}
\]

Explicit realizations:

- `(4,0)`: choose three P-edges so each `(2,1)` vertex has P-degree 2 and each `(3,2)` vertex P-degree 1; color the complement Q.
- `(2,2)`: choose four P-edges, equivalently two Q-edges, one incident with each `(2,1)` vertex.
- `(0,4)`: choose five P-edges and make the unique Q-edge join the two `(2,1)` vertices.

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

## 5. Pre-operator interpretation

The natural object attached to a world is no longer only

\[
R\mapsto\Lambda_R(n).
\]

The current hierarchy is

\[
R
\longmapsto
\Gamma_R
\longmapsto
(\mu_R,\mathcal M_R)
\longmapsto
\partial_P\mathfrak B_R^{(2)}(n).
\]

A future operator of worlds should act on this structured response, or on a controlled projection of it, rather than on the scalar boundary alone.

No world Laplacian is defined yet. The next task is to determine natural inter-world comparison maps between the block-count obstruction landscapes.
