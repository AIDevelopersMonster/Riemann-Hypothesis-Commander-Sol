# FCOA Rigidity Cost — Orbit-Affine Repair Theorem

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** corrected post-publication theorem replacing the rejected singleton-hypergraph shortcut.

---

## 1. Setup

Let

\[
B_{\rm old}=A_Q(D,c)\setminus A_{\rm an}(D,c)
\]

be the old bad automorphisms of a sparse binary anonymous layer.

Let

\[
M=(G^2\setminus\Delta)\setminus D
\]

be the set of currently undefined operation cells.

For an extension choose

\[
E\subseteq M,
\qquad
b:E\to\mathbf F_2.
\]

Write

\[
D_E=D\cup E,
\qquad
c_E=c\cup b.
\]

Fix one old bad automorphism `g in B_old`.

Because `gD=D`, the set `M` is `g`-invariant and `g` acts on the missing cells.

---

## 2. Domain-orbit criterion

### Lemma 2.1

The enlarged domain `D_E` is preserved by `g` if and only if

\[
\boxed{gE=E.}
\]

Equivalently, `E` must be a union of complete `g`-orbits in `M`.

### Proof

Since `gD=D`,

\[
g(D\cup E)=D\cup gE.
\]

Thus equality with `D\cup E` is equivalent to `gE=E`. `square`

Hence any extension that is not a union of `g`-orbits kills `g` before colors are considered.

---

## 3. Discrepancy variables on an invariant extension

Assume now that

\[
gE=E.
\]

For old cells `p in D`, define the known discrepancy

\[
d_g(p)=c(gp)\oplus c(p).
\]

For new cells `e in E`, define

\[
d_g^b(e)=b(ge)\oplus b(e).
\]

Together these give a discrepancy function

\[
d_{g,E,b}:D_E\to\mathbf F_2.
\]

---

## 4. Orbit-Affine Survival Theorem

### Theorem 4.1

Assume `gE=E`. Then `g` preserves the enlarged ternary equality reduct

\[
(G;D_E,Q_{D_E})
\]

if and only if the discrepancy function `d_{g,E,b}` is constant on every connected component of the enlarged ordered-cell incidence graph

\[
\Lambda(D_E).
\]

Equivalently, for every composability edge `p~q` of `Lambda(D_E)`,

\[
\boxed{
d_{g,E,b}(p)=d_{g,E,b}(q).}
\]

### Proof

For composable cells `p,q`, preservation of the ternary equality predicate is exactly

\[
c_E(p)=c_E(q)
\iff
c_E(gp)=c_E(gq).
\]

Over `F_2` this is equivalent to

\[
c_E(gp)\oplus c_E(p)
=
c_E(gq)\oplus c_E(q),
\]

that is,

\[
d_{g,E,b}(p)=d_{g,E,b}(q).
\]

Propagation along paths gives constancy on incidence components, and the converse is immediate. `square`

---

## 5. Affine survival space

For fixed `g` and a fixed `g`-invariant cell set `E`, the equations of Theorem 4.1 are affine linear equations in the new color vector

\[
b\in\mathbf F_2^E.
\]

Define

\[
\boxed{
S_g(E)
=
\{b\in\mathbf F_2^E:
 g\in\operatorname{Aut}(G;D_E,Q_{D_E})\}.
}
\]

Then:

- if `gE != E`, put `S_g(E)=emptyset`;
- if `gE=E`, `S_g(E)` is an affine subspace of `F_2^E` (possibly empty).

Thus an old bad automorphism survives an extension exactly when

\[
\boxed{b\in S_g(E).}
\]

and it is killed exactly when

\[
\boxed{b\notin S_g(E).}
\]

---

## 6. Exact characterization of beta

### Corollary 6.1

The old-obstruction cost is exactly

\[
\boxed{
\beta(D,c)
=
\min\Bigl\{|E|:
\exists b\in\mathbf F_2^E
\text{ such that }
 b\notin\bigcup_{g\in B_{\rm old}}S_g(E)
\Bigr\}.
}
\]

In words:

> choose the smallest new-cell set `E` whose binary color cube contains at least one point outside every old-bad survival space.

This is an **orbit-sensitive affine avoidance problem**.

It is not an ordinary hitting-set problem.

---

## 7. Two distinct old-symmetry killing mechanisms

For an old bad `g`, an extension can kill it in exactly two qualitatively different ways.

### Type I — orbit breaking

\[
\boxed{gE\ne E.}
\]

The new domain is not invariant, so `g` dies independently of the new colors.

### Type II — affine phase breaking

\[
\boxed{gE=E,\qquad b\notin S_g(E).}
\]

The new cell set is orbit-complete but its coloring/comparison geometry makes the discrepancy inconsistent on an enlarged incidence component.

The rejected singleton-hypergraph model saw Type I only locally and therefore failed when several singleton cells completed a `g`-orbit and restored domain invariance.

---

## 8. Orbit restoration explained exactly

Suppose `e` is not fixed by `g`.

The singleton set

\[
E_1=\{e\}
\]

has

\[
gE_1\ne E_1,
\]

so it kills `g` by Type I.

But the complete orbit

\[
E_2=\operatorname{Orb}_g(e)
\]

satisfies

\[
gE_2=E_2.
\]

Therefore `g` may re-enter the candidate automorphism group. It survives precisely for the colorings

\[
b\in S_g(E_2).
\]

This is the exact algebraic form of old-orbit restoration.

---

## 9. Relation to the unsafe beta witness

The unsafe one-cell repair in `UNSAFE_BETA_WITNESS.md` is a different phenomenon.

There the selected cell really kills all old bad automorphisms, so the chosen coloring lies outside every old survival space.

The failure of exactness comes from a **new** domain-moving bad automorphism not contained in `B_old`.

Therefore the theory has two independent nonlinearities:

1. **orbit restoration inside beta** — old bad symmetries may return when new cells complete their orbits;
2. **symmetry creation between beta and alpha** — new bad symmetries may arise after all old ones are killed.

The first is now exactly controlled by the orbit-affine spaces `S_g(E)`. The second remains the Safe-Minimizer problem.

---

## 10. Fixed-domain color selection

For a fixed uncolored extension domain `E`, define the old-bad forbidden-color set

\[
\mathcal F_{\rm old}(E)
=
\bigcup_{g\in B_{\rm old}}S_g(E).
\]

Then `E` supports a genuine beta-repair if and only if

\[
\boxed{
\mathcal F_{\rm old}(E)\ne\mathbf F_2^E.
}
\]

The number of valid old-obstruction-killing colorings is

\[
2^{|E|}-|\mathcal F_{\rm old}(E)|.
\]

This opens a new route via finite affine-subspace covering theory.

In particular, if the proper survival spaces are few or have sufficiently large codimension, their union cannot cover the whole color cube, guaranteeing a valid coloring on the chosen cell set.

---

## 11. Safe-Minimizer reformulation

Let

\[
\mathcal E_\beta
=
\{E\subseteq M:|E|=\beta,
\mathcal F_{\rm old}(E)\ne\mathbf F_2^E\}.
\]

For each `E in E_beta`, let

\[
\mathcal B_\beta(E)
=
\mathbf F_2^E\setminus\mathcal F_{\rm old}(E)
\]

be the colorings that kill every old bad automorphism.

Then

\[
\boxed{
\alpha=\beta
}
\]

is equivalent to the existence of

\[
E\in\mathcal E_\beta,
\qquad
b\in\mathcal B_\beta(E)
\]

such that the enlarged layer is exact.

Thus the remaining problem has become:

> among all minimum cell sets whose color cube is not covered by old-bad affine survival spaces, prove that at least one admissible coloring also avoids every newly created bad symmetry.

---

## 12. New proof routes

The orbit-affine formulation suggests three concrete attacks.

### A. Affine covering bounds

Bound the number/codimension/intersections of the spaces `S_g(E)` and of analogous survival spaces for domain-moving automorphisms of the enlarged domain.

### B. Orbit-breaking extremality

Choose a minimum `E` maximizing the number of old bad automorphisms killed by Type I (`gE != E`). Such a choice minimizes dependence on color and may reduce the opportunity for symmetry creation.

### C. Lexicographic safe-selection

Among beta-minimizing pairs `(E,b)`, minimize successively:

1. number of domain-moving automorphisms of the enlarged reduct;
2. total number of old/new cell incidences moved across the boundary `D|E`;
3. automorphism-group order.

A replacement lemma that strictly decreases this finite defect would prove the Safe-Minimizer theorem.

---

## 13. Claim firewall

1. The ordinary singleton Repair Hypergraph theorem is false and has been withdrawn.
2. The orbit-affine characterization of old-bad survival is exact.
3. `S_g(E)` is affine only after fixing a `g`-invariant cell set `E`; otherwise it is empty by definition.
4. No affine-covering theorem sufficient for `alpha=beta` is claimed yet.
5. The exhaustive `eta=0` evidence remains valid because beta was computed by direct multi-cell automorphism tests.
