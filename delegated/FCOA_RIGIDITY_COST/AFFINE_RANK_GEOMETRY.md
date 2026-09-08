# FCOA Rigidity Cost — Affine Rank Geometry of Survival Spaces

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** post-publication theorem refining the orbit-affine repair model.

## 1. Cell-color vector space

Fix an extension cell set `E` and write

\[
X=D\cup E.
\]

Let

\[
V_X=\mathbf F_2^X
\]

be the vector space of binary functions on all defined cells of the extended domain.

Let

\[
Z_X\subseteq V_X
\]

be the subspace of functions constant on every connected component of the ordered-cell incidence graph

\[
\Lambda(X).
\]

Thus

\[
\dim Z_X=\kappa(\Lambda(X)).
\]

Let

\[
P_X:V_X\to V_X/Z_X
\]

be the quotient map.

## 2. Discrepancy operator

Let `g` be a carrier permutation preserving the extended domain `X` setwise. It induces a permutation operator

\[
g^*:V_X\to V_X,
\qquad
(g^*f)(p)=f(gp).
\]

Define the binary discrepancy operator

\[
\boxed{\Delta_g=I+g^*.}
\]

For a coloring `f in V_X`, the Componentwise Phase Theorem says exactly that `g` preserves the ternary equality reduct iff

\[
\Delta_g f\in Z_X.
\]

Equivalently,

\[
\boxed{P_X\Delta_g f=0.}
\]

## 3. Restriction to new color variables

Let

\[
\iota_E:\mathbf F_2^E\hookrightarrow V_X
\]

extend a vector on new cells by zero on the old domain `D`.

Let `c_D in V_X` denote the fixed old coloring extended by zero on `E`.

Every extension coloring has the form

\[
f=c_D+\iota_E b,
\qquad b\in\mathbf F_2^E.
\]

Define

\[
\boxed{
A_{g,E}=P_X\Delta_g\iota_E:
\mathbf F_2^E\to V_X/Z_X.
}
\]

and

\[
y_{g,E}=P_X\Delta_g c_D.
\]

Then the survival condition is the affine system

\[
\boxed{A_{g,E}b=y_{g,E}.}
\]

## 4. Exact rank theorem

### Theorem 4.1

Assume `gX=X`. The survival-coloring set

\[
S_g(E)=\{b\in\mathbf F_2^E:g\in\operatorname{Aut}(G;X,Q_X)\}
\]

is either empty or an affine coset of

\[
\ker A_{g,E}.
\]

If nonempty, then

\[
\boxed{
\operatorname{codim}_{\mathbf F_2^E}S_g(E)
=
\operatorname{rank}A_{g,E}.
}
\]

In particular,

\[
|S_g(E)|=2^{|E|-\operatorname{rank}A_{g,E}}.
\]

### Proof

The equation `A_{g,E}b=y_{g,E}` is affine linear. If it is consistent, its solution set is one translate of the kernel. The dimension formula follows from rank-nullity. `square`

## 5. Intersections

For carrier permutations `g_1,...,g_m` all preserving `X`, stack the operators

\[
A_{\mathcal G,E}
=
\begin{bmatrix}
A_{g_1,E}\\
\vdots\\
A_{g_m,E}
\end{bmatrix}
\]

with the corresponding right-hand sides.

### Corollary 5.1

The common survival set

\[
\bigcap_{i=1}^m S_{g_i}(E)
\]

is empty or an affine subspace of codimension

\[
\boxed{
\operatorname{rank}A_{\mathcal G,E}.
}
\]

Thus all intersection data relevant to inclusion-exclusion or affine-cover arguments reduce to ordinary binary matrix rank.

## 6. Color-blind symmetries

Define the **color rank** of a domain-preserving carrier permutation by

\[
\boxed{\rho_E(g)=\operatorname{rank}A_{g,E}.}
\]

If `S_g(E)` is nonempty and

\[
\rho_E(g)=0,
\]

then

\[
S_g(E)=\mathbf F_2^E.
\]

Call such a symmetry **color-blind on E**: no choice of binary values on the chosen new cells can remove it from the ternary reduct.

Therefore a fixed-domain affine-color argument can eliminate only bad symmetries with positive color rank.

## 7. Rank-zero barrier to a color-only proof of alpha=beta

The unsafe minimum repair phenomenon shows that a beta-minimizing cell set may support a newly created bad automorphism for every coloring of that cell set. In the operator language this is precisely the rank-zero case

\[
\rho_E(h)=0,
\qquad
S_h(E)=\mathbf F_2^E.
\]

Hence no theorem based solely on counting proper affine survival subspaces inside the fixed cube `F_2^E` can prove the Safe-Minimizer conjecture in full generality.

A successful proof must first choose the geometry of `E` so that every newly created bad symmetry is either:

1. excluded at the domain level (`hX != X`); or
2. has positive color rank and can potentially be avoided by choosing `b`.

This gives a two-stage target:

\[
\boxed{
\text{structural rank-zero elimination}
\quad\longrightarrow\quad
\text{positive-rank affine avoidance}.
}
\]

## 8. A sufficient affine-avoidance criterion

Suppose `E` is beta-minimal and all bad carrier permutations of the enlarged uncolored domain which are not globally anonymous have nonempty survival spaces of positive codimension.

If

\[
\sum_h 2^{-\rho_E(h)}<1,
\]

where the sum ranges over all such bad permutations whose survival spaces are nonempty, then the union bound gives

\[
\left|\bigcup_h S_h(E)\right|
<2^{|E|}.
\]

Therefore there exists a coloring `b` outside every bad survival space, and the extension is exact.

Thus:

### Proposition 8.1

If a beta-minimal cell set `E` satisfies

\[
\boxed{
\sum_h 2^{-\rho_E(h)}<1,
}
\]

for all bad domain automorphisms `h` of `D union E`, then

\[
\boxed{\alpha=\beta.}
\]

This is only a sufficient criterion; it is not claimed to hold for every beta-minimal `E`.

## 9. Sharper counting via intersections

The union bound may be crude. Corollary 5.1 gives exact intersection sizes:

\[
\left|\bigcap_{h\in J}S_h(E)\right|
=
0
\quad\text{or}\quad
2^{|E|-\operatorname{rank}A_{J,E}}.
\]

Therefore inclusion-exclusion for the bad-color set is completely rank-controlled.

This makes the fixed-`E` exactness problem algorithmically reducible to rank data of stacked discrepancy operators.

## 10. Research consequence

The Safe-Minimizer conjecture should no longer be attacked as one undifferentiated statement.

The correct decomposition is:

### Structural problem

Does every sparse binary layer admit a beta-minimal cell set `E` with no newly created color-blind bad symmetry?

### Affine problem

For such an `E`, can the positive-rank bad survival spaces cover every old-obstruction-killing coloring?

The first problem is genuinely about operation-cell geometry and automorphism orbits. The second is finite affine-subspace covering theory.

A counterexample to `alpha=beta` must defeat at least one of these two stages for **every** beta-minimal cell set.

## Claim firewall

1. The rank formula is exact for a fixed domain-preserving permutation and fixed cell set `E`.
2. `rho_E(g)=0` does not by itself mean `g` survives; consistency of the affine system is still required. If it survives one coloring and rank is zero, it survives all colorings.
3. Proposition 8.1 is sufficient, not necessary.
4. No general theorem eliminating rank-zero new bad symmetries is claimed yet.
5. The global conjecture `alpha=beta` remains open.