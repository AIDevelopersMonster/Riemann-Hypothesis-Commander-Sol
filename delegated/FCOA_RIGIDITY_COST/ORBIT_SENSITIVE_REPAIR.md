# FCOA Rigidity Cost — Orbit-Sensitive Repair and Affine Survival Spaces

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** new post-publication theorem replacing the false singleton-factorization model.

---

## 1. Setup

Let

\[
D\subseteq G^2\setminus\Delta,
\qquad c:D\to\mathbf F_2,
\]

and let

\[
g\in A_Q(D,c)=\operatorname{Aut}(G;D,Q_D).
\]

Let `E` be a set of new operation cells and let

\[
b:E\to\mathbf F_2
\]

be their colors. Put

\[
D_E=D\cup E,
\qquad c_E=c\cup b.
\]

We ask when the old automorphism `g` survives as an automorphism of the enlarged ternary reduct

\[
(G;D_E,Q_{D_E}).
\]

---

## 2. Domain-orbit condition

Because `gD=D`, preservation of the enlarged domain is equivalent to

\[
\boxed{gE=E.}
\]

If `gE\ne E`, then `g` is killed independently of the colors assigned to `E`.

Thus only `g`-invariant extension geometries need a color analysis.

---

## 3. Extended discrepancy

Assume now that

\[
gE=E.
\]

Define the discrepancy on the enlarged domain by

\[
\delta_g^{E,b}(p)=c_E(gp)\oplus c_E(p),
\qquad p\in D_E.
\]

On old cells this is already fixed by the original layer:

\[
\delta_g^{E,b}(p)=c(gp)\oplus c(p),
\qquad p\in D.
\]

On new cells it is linear in the unknown coloring `b`:

\[
\boxed{
\delta_g^{E,b}(e)=b(ge)\oplus b(e),
\qquad e\in E.
}
\]

---

## 4. Affine Survival Theorem

### Theorem 4.1

Assume `gE=E`. Then `g` is an automorphism of the enlarged ternary reduct if and only if

\[
\boxed{
\delta_g^{E,b}(p)=\delta_g^{E,b}(q)
}
\]

for every adjacent pair of ordered cells `p~q` in the enlarged incidence graph

\[
\Lambda(D_E).
\]

Equivalently, the discrepancy is constant on every connected component of

\[
\Lambda(D_E).
\]

### Proof

For adjacent composable cells `p=(x,y)` and `q=(y,z)`, preservation of `Q_{D_E}` is exactly

\[
c_E(p)=c_E(q)
\iff
c_E(gp)=c_E(gq).
\]

For binary values, this equivalence holds exactly when

\[
c_E(gp)\oplus c_E(p)
=
c_E(gq)\oplus c_E(q).
\]

That is

\[
\delta_g^{E,b}(p)=\delta_g^{E,b}(q).
\]

Propagation along paths gives the component formulation, and the converse is immediate edge by edge. \(\square\)

---

## 5. Survival color space

For fixed `g` and fixed extension geometry `E`, define

\[
\mathcal S_g(E)
=
\{b\in\mathbf F_2^E:
 g\in\operatorname{Aut}(G;D_E,Q_{D_E})\}.
\]

If

\[
gE\ne E,
\]

put

\[
\mathcal S_g(E)=\varnothing.
\]

If `gE=E`, Theorem 4.1 expresses survival by equations of the form

\[
b(ge)\oplus b(e)
=b(gf)\oplus b(f),
\]

or

\[
b(ge)\oplus b(e)=\epsilon,
\]

where `epsilon` is a fixed old discrepancy bit on an old incidence component.

Hence:

### Corollary 5.1

For every old reduct automorphism `g` and every extension geometry `E`,

\[
\boxed{
\mathcal S_g(E)
\text{ is either empty or an affine subspace of }
\mathbf F_2^E.
}
\]

Thus the colorings that kill `g` are precisely

\[
\mathbf F_2^E\setminus\mathcal S_g(E).
\]

---

## 6. Exact orbit-sensitive formula for beta

Let

\[
B_{\rm old}=A_Q(D,c)\setminus A_{\rm an}(D,c).
\]

For a fixed geometry `E`, a coloring `b` destroys all old bad automorphisms exactly when

\[
b\notin\mathcal S_g(E)
\qquad
\forall g\in B_{\rm old}.
\]

Therefore:

### Theorem 6.1 — exact beta formula

\[
\boxed{
\beta(D,c)
=
\min_E
\left\{
|E|:
\mathbf F_2^E
\setminus
\bigcup_{g\in B_{\rm old}}
\mathcal S_g(E)
\ne\varnothing
\right\}.
}
\]

The minimum ranges over sets of undefined non-loop cells.

This is the correct replacement for the false singleton hitting-set formula.

The geometry `E` is first required to break enough old cell-orbits or incidence compatibility. The remaining old symmetries then exclude affine regions of the color cube. A beta-optimal repair is a smallest geometry whose binary color cube is not covered by these survival spaces.

---

## 7. Two independent mechanisms for killing an old symmetry

For fixed `g`, an extension kills `g` in one of two fundamentally different ways.

### Geometry kill

\[
\boxed{gE\ne E.}
\]

The enlarged domain itself is not invariant.

### Phase kill

\[
\boxed{gE=E
\quad\text{but}\quad
b\notin\mathcal S_g(E).}
\]

The cell geometry is invariant, but the new colors make the discrepancy inconsistent on an enlarged incidence component.

Thus beta mixes orbit-breaking geometry and affine phase exclusion.

---

## 8. Automatic geometry obstruction

Suppose an enlarged incidence component contains old cells from two original components on which the old phase signature of `g` has different bits.

Then no coloring of the new cells can make the enlarged discrepancy constant on that component.

Hence:

### Corollary 8.1

If `E` merges two old incidence components carrying different `g`-phase bits, then

\[
\boxed{\mathcal S_g(E)=\varnothing.}
\]

This recovers the basic bridge mechanism behind the published inequality

\[
\beta\le\lambda.
\]

It also shows why some repair cells kill a symmetry independently of their binary value.

---

## 9. Orbit-cycle parity

Assume `gE=E`. Let

\[
e,ge,g^2e,\dots,g^{\ell-1}e
\]

be a `g`-orbit of new cells contained in one enlarged incidence component whose required discrepancy is a fixed bit `theta`.

Then the survival equations contain

\[
b(g^{j+1}e)\oplus b(g^je)=\theta.
\]

Summing around the orbit gives

\[
\ell\theta=0
\quad\text{in }\mathbf F_2.
\]

Therefore:

### Corollary 9.1

An odd new-cell orbit cannot support discrepancy `theta=1`.

In particular, if an odd `g`-orbit of added cells lies in an enlarged incidence component forced by old cells to have phase 1, then `g` is killed for **every** coloring of that orbit.

This gives a second color-independent repair mechanism beyond direct merging of opposite old phase components.

---

## 10. Counting consequence

When `\mathcal S_g(E)` is nonempty, it is an affine subspace of codimension

\[
\rho_g(E)
\]

for some integer `rho_g(E)>=0`. Hence

\[
|\mathcal S_g(E)|=2^{|E|-\rho_g(E)}.
\]

By the union bound, a sufficient condition for the existence of a coloring that kills every old bad automorphism is

\[
\boxed{
\sum_{g\in B_{\rm old}:\mathcal S_g(E)\ne\varnothing}
2^{-\rho_g(E)}<1.
}
\]

Then the union of all old-survival spaces cannot cover the full color cube.

This is only a sufficient condition, since survival spaces may overlap heavily, but it converts part of the beta problem into a codimension budget.

---

## 11. Relation to alpha and the Safe-Minimizer problem

The theorem above solves the **old-obstruction** side exactly. It does not by itself control new automorphisms `h` of the enlarged reduct that move the old domain.

Thus the full chain is now

\[
\boxed{
\text{old }g\text{-orbits on missing cells}
+
\text{affine survival spaces}
\longrightarrow
\beta
\longrightarrow
\text{new domain-moving symmetries}
\longrightarrow
\alpha.
}
\]

The conjecture

\[
\alpha=\beta
\]

is equivalent to saying that some beta-optimal geometry `E` admits a color vector outside both:

1. every old survival space `\mathcal S_g(E)`;
2. every bad survival condition arising from newly created domain-moving automorphisms of the enlarged structure.

The first family is now completely linearized. The remaining difficulty is entirely the second family.

---

## 12. Research direction

The next target is a **safe-color / safe-geometry theorem**.

Two promising sufficient routes are now visible:

1. choose beta-optimal `E` so that every domain-moving carrier permutation fails `h(D_E)=D_E`;
2. when domain-moving permutations remain, show that their bad colorings also form proper affine subsets of `F_2^E` and prove that the union of old and new bad spaces cannot cover the full color cube for at least one beta-optimal geometry.

The second route would turn Safe-Minimizer into an affine-subspace avoidance theorem.

---

## 13. Claim firewall

1. The affine theorem is only for binary anonymous terminal values.
2. `gE=E` is essential before the color equations are considered.
3. The theorem concerns survival of an already existing old reduct automorphism `g`.
4. Newly created domain-moving automorphisms are not parameterized by `B_old` and remain the unresolved part of `alpha`.
5. The union-bound criterion is sufficient, not necessary.
6. No singleton-factorization or matroid structure is claimed.
