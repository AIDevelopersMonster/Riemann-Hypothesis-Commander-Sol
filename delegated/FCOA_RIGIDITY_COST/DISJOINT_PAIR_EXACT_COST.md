# FCOA Rigidity Cost — Exact Cell-Extension Cost for Disjoint Bidirected Pairs

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** new post-publication theorem; does not modify either frozen article.

---

## 1. The model family

Fix `r>=2`. Let

\[
G_r=\{a_1,b_1,\dots,a_r,b_r\}.
\]

The sparse domain consists of `r` disjoint bidirected pairs

\[
D_r=\bigcup_{i=1}^r\{(a_i,b_i),(b_i,a_i)\}.
\]

Color every pair oppositely:

\[
c(a_i,b_i)=0,
\qquad
c(b_i,a_i)=1.
\]

The ordered-cell incidence graph \(\Lambda(D_r)\) has exactly `r` connected components, one for each pair.

Independent transpositions

\[
s_i=(a_i\ b_i)
\]

realize all component phase flips. Therefore

\[
\Sigma(D_r,c)=\mathbf F_2^r
\]

and the fixed-domain phase-link cost is

\[
\boxed{\lambda(D_r,c)=r-1.}
\]

The problem is to determine the actual operation-cell exactness cost

\[
\alpha_r:=\alpha(D_r,c).
\]

---

## 2. Main theorem

### Theorem — Exact disjoint-pair cost

For every `r>=2`,

\[
\boxed{
\alpha_r=\left\lceil\frac r2\right\rceil.
}
\]

Thus this family has

\[
\boxed{
\lambda_r=r-1,
\qquad
\alpha_r=\left\lceil\frac r2\right\rceil.
}
\]

In particular:

\[
(\lambda_2,\alpha_2)=(1,1),
\]

\[
(\lambda_3,\alpha_3)=(2,2),
\]

\[
(\lambda_4,\alpha_4)=(3,2),
\]

so the six-carrier `(2,2)` states found after Article B are the first member of an infinite exact family, but the equality `alpha=lambda` does not persist beyond `r=3`.

---

## 3. Lower bound

Let `E` be any set of new operation cells that makes the extended ternary reduct exact.

Call an original pair `P_i={a_i,b_i}` **touched** if at least one endpoint of at least one cell of `E` lies in `P_i`.

### Lemma — every original pair must be touched

If `P_i` is untouched, the transposition

\[
s_i=(a_i\ b_i)
\]

preserves the extended domain and the sparse ternary equality reduct.

Indeed, `s_i` swaps the two old cells of `P_i` and fixes every new cell because no new cell is incident with `a_i` or `b_i`. On the `P_i` incidence component it produces phase 1, while on every other old/new cell it produces phase 0. Thus it is a reduct automorphism with a non-diagonal phase signature, so exactness fails.

Hence every one of the `r` original pairs must be touched.

A single new non-loop cell has exactly two endpoints and therefore can touch at most two original pairs. Consequently

\[
2|E|\ge r,
\]

so

\[
\boxed{
\alpha_r\ge\left\lceil\frac r2\right\rceil.
}
\]

---

## 4. Sharp construction for even r

Let `r=2m`.

Partition the pair-indices into `m` blocks

\[
\{1,2\},\{3,4\},\dots,\{2m-1,2m\}.
\]

For each block add one cell

\[
(a_{2j-1},a_{2j})
\]

and color it 0.

Thus exactly `m=r/2` new cells are added.

### Why the resulting reduct is exact

First, an old bidirected cell is intrinsically distinguished from every new bridge cell by the property that its reverse cell is also defined. Hence every carrier automorphism of the extended domain preserves the collection of original bidirected pairs setwise and preserves the bridge-cell collection setwise.

Within an incidence component containing a bridge between pair-indices `i,j`, Theorem 1 of Article B forces one common phase bit on the two original pair-components and the bridge cell.

Suppose that common phase were 1. Then each original pair would have its endpoints swapped relative to the temporary binary coding. The bridge

\[
(a_i,a_j)
\]

would therefore have to map to a defined bridge of the form

\[
(b_{\sigma(i)},b_{\sigma(j)}),
\]

for some induced permutation of pair-indices. No such bridge is present: every new bridge has `a-a` form. Therefore phase 1 is impossible on every bridge component.

Hence every realized component phase is 0. The ternary reduct is exact.

Thus

\[
\alpha_{2m}\le m.
\]

Combined with the lower bound,

\[
\boxed{\alpha_{2m}=m.}
\]

---

## 5. Sharp construction for odd r

Let `r=2m+1`, with `m>=1`.

Use the even construction on the first `2m` pairs, giving `m` bridges

\[
(a_1,a_2),\ (a_3,a_4),\dots,(a_{2m-1},a_{2m}).
\]

Add one additional 0-colored bridge

\[
(a_{2m+1},a_1).
\]

The total number of new cells is

\[
m+1=\left\lceil\frac r2\right\rceil.
\]

Every original pair lies in an incidence component containing at least one `a-a` bridge. As in the even case, reverse-definedness distinguishes old pair cells from bridge cells, and phase 1 on any enlarged incidence component would send an `a-a` bridge to a nonexistent `b-b` bridge. Hence every realized phase is 0 and the extended ternary reduct is exact.

Therefore

\[
\alpha_{2m+1}\le m+1.
\]

Together with the lower bound,

\[
\boxed{\alpha_{2m+1}=m+1.}
\]

This completes the proof of the main theorem.

---

## 6. Structural consequences

The disjoint-pair family reveals a third cost geometry, distinct from both published Article B extremes.

### Hub family from Article B

\[
\lambda=r-1,
\qquad
\alpha=1.
\]

One new operation cell touches all phase components through a shared carrier hub.

### Disjoint-pair family

\[
\boxed{
\lambda=r-1,
\qquad
\alpha=\left\lceil\frac r2\right\rceil.
}
\]

There is no shared hub. Every new cell touches at most two old components, and exactness forces every original pair to be touched.

Thus the actual operation-cell cost is governed by **endpoint coverage geometry**, not merely by the number of abstract phase freedoms.

The ratio is

\[
\frac{\lambda_r}{\alpha_r}
=\frac{r-1}{\lceil r/2\rceil},
\]

which approaches 2 rather than infinity.

---

## 7. New invariant suggested by the theorem

For a sparse layer with old incidence components \(C_1,\dots,C_r\), let a candidate new cell `e` have touch set

\[
\mathcal T_D(e)\subseteq\{C_1,\dots,C_r\}.
\]

Article B already introduced these touch sets. The present theorem shows that their **covering number** can supply an actual lower bound when untouched components retain realizable local bad symmetries.

For the disjoint-pair family, every touch set has size at most 2, and every old component must be touched. Hence the exact cost equals the minimum number of touch sets needed to cover all old components:

\[
\boxed{
\alpha_r=\tau(\mathcal H_D)=\lceil r/2\rceil,
}
\]

where \(\mathcal H_D=\{\mathcal T_D(e):e\notin D\}\) and \(\tau\) denotes the hypergraph covering number.

This suggests a broader programme: identify classes in which actual extension cost is controlled by a touch-hypergraph covering invariant rather than by the fixed-domain phase-link number \(\lambda\).

---

## 8. Relation to Conjecture 14

For this infinite family,

\[
\alpha_r=\left\lceil\frac r2\right\rceil\le r-1=\lambda_r
\qquad(r\ge2).
\]

Hence the family supplies an infinite nontrivial verification of Conjecture 14.

It is especially useful because it contains genuine `alpha>1` examples and therefore tests the conjecture beyond the one-cell-repair regime.

---

## 9. Claim firewall

1. The theorem concerns exactly the disjoint oppositely colored bidirected-pair family defined above.
2. The lower bound uses the fact that an untouched pair retains an independent local swap that preserves all new cells.
3. The upper-bound construction deliberately uses one-way `a-a` bridges and no `b-b` bridges; this asymmetry kills phase 1 on every bridge-containing incidence component.
4. No claim is made that a touch-hypergraph cover computes `alpha` for arbitrary sparse domains.
5. Articles A and B remain frozen and are used only as published foundations.
