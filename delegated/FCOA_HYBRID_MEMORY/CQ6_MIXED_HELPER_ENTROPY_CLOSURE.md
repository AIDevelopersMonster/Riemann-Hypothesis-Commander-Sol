# FCOA Hybrid Memory — CQ6 Mixed-Helper Entropy Closure

**Status:** positive lower bound in the standard conjunctive-query preprocessing model  
**Main result:** `CQ^6` exact truncated addition cannot be represented with `N^{1+o(1)}` preprocessing; in fact the storage exponent is at least `7/6`.

## 1. Setup

Let

\[
Add_N(x,y,z)\iff x+y=z<N.
\]

Consider a fixed `CQ^6`

\[
q(x,y,z)=\exists u\exists v\exists w\;\bigwedge_i R_i(\bar t_i)
\]

whose preprocessing structure `A_N` has total size

\[
S_N\le N^{\alpha+o(1)}.
\]

Assume, as in the previous free-pair lemma, that no atom contains two distinct free arithmetic variables among `x,y,z`; otherwise some primitive relation already contains `Omega(N^2)` tuples and the theorem is immediate.

We prove that

\[
\alpha\ge\frac76.
\]

Hence near-linear preprocessing is impossible in `CQ^6`.

---

## 2. A regular entropy slice of truncated addition

Let

\[
m=\lfloor N/3\rfloor
\]

and consider only the valid addition triples

\[
\mathcal T_m=\{(x,y,z):0\le x,y<m,\ z=x+y\}.
\]

Choose `(X,Y)` uniformly from `[m]^2` and set

\[
Z=X+Y.
\]

Then

\[
H(X)=H(Y)=\log m,
\]

\[
H(X,Y)=H(X,Z)=H(Y,Z)=2\log m,
\]

because each displayed pair determines the omitted variable inside this slice.

Moreover

\[
H(Z)=\log m+O(1),
\]

so all pairwise mutual informations satisfy

\[
I(X;Y)=0,
\qquad
I(X;Z)=O(1),
\qquad
I(Y;Z)=O(1).
\tag{2.1}
\]

Thus, on the `log N` scale, `X,Y,Z` are pairwise independent entropy-one variables while their joint entropy is only two units.

---

## 3. Deterministic witness selection

For every triple in `\mathcal T_m`, choose one satisfying helper triple

\[
(U,V,W).
\]

This selection may be arbitrary but deterministic.

Because no atom contains two free variables, after fixing `(u,v,w)` the set of free triples satisfying all free-variable atoms is a Cartesian box

\[
X_{uvw}\times Y_{uvw}\times Z_{uvw}.
\]

Exactness of the CQ implies that every such productive box is contained in `Add_N`. By the Latin-box lemma, a Cartesian box contained in the graph of addition has size at most one.

Therefore every productive helper triple determines a unique free triple:

\[
H(X,Y,Z\mid U,V,W)=0.
\tag{3.1}
\]

By deterministic witness selection,

\[
H(U,V,W\mid X,Y,Z)=0.
\tag{3.2}
\]

Hence

\[
H(U,V,W)=H(X,Y,Z)=2\log m.
\tag{3.3}
\]

The helper triple therefore carries exactly the two entropy units of the addition relation.

---

## 4. Adjacent-helper sets

For a free variable `F in {X,Y,Z}`, let

\[
A_F\subseteq\{U,V,W\}
\]

be the set of helper variables that occur together with `F` in at least one primitive atom of the CQ.

### Lemma 4.1 — every adjacent helper is almost a function of its free variable

Let `H` be one helper variable in `A_F`. Then

\[
H(H\mid F)\le (\alpha-1)\log N+o(\log N).
\tag{4.1}
\]

### Proof

Choose an atom containing both `F` and `H`. Every sampled witness tuple lies in its primitive relation. Hence the entropy of the variables in that atom is at most the logarithm of the relation cardinality, which is at most

\[
(\alpha+o(1))\log N.
\]

Since

\[
H(F)=\log N+o(\log N),
\]

we obtain (4.1) by monotonicity and the chain rule. `square`

---

## 5. Each free variable is determined by its adjacent helpers

### Lemma 5.1

For each `F in {X,Y,Z}`,

\[
H(F\mid A_F)=0.
\tag{5.1}
\]

### Proof

Fix two productive helper assignments with the same values on `A_F`. All atoms involving `F` see exactly the same helper values in the two assignments. Therefore they define the same allowed set of `F`-values.

But every productive full helper assignment admits exactly one free triple by (3.1), so that allowed set contains exactly one `F`-value. Hence the two assignments yield the same `F`. Thus `F` is a function of `A_F` on the selected witness support. `square`

Consequently

\[
H(A_F)\ge H(F)=\log N+o(\log N).
\tag{5.2}
\]

---

## 6. Shared helpers have small entropy

Suppose one helper variable `H` lies in both `A_F` and `A_G` for two distinct free variables `F,G`.

Using the standard approximate-common-information inequality

\[
H(H)
\le
I(F;G)+H(H\mid F)+H(H\mid G),
\]

and (2.1), (4.1), we get

\[
H(H)
\le
2(\alpha-1)\log N+o(\log N).
\tag{6.1}
\]

So every helper shared by two free branches has entropy at most `2(alpha-1)` units asymptotically.

---

## 7. The 7/6 threshold

Assume for contradiction that

\[
\alpha<\frac76.
\]

Write

\[
\varepsilon=\alpha-1<\frac16.
\]

Suppose some free variable `F` had **no exclusive helper**, meaning every helper in `A_F` also belonged to at least one other free branch.

Then every helper in `A_F` is shared, so by (6.1), and because there are only three helpers total,

\[
H(A_F)
\le
\sum_{H\in A_F}H(H)
\le
6\varepsilon\log N+o(\log N)
<
\log N-o(\log N).
\]

This contradicts (5.2).

Hence each of `X,Y,Z` must possess at least one helper variable exclusive to its own branch.

There are exactly three free variables and exactly three helpers. Therefore, after renaming,

\[
A_X=\{U\},
\qquad
A_Y=\{V\},
\qquad
A_Z=\{W\}.
\tag{7.1}
\]

Indeed, the three required exclusive helpers already exhaust the helper set; any additional adjacency would destroy exclusivity for one of them.

By Lemma 5.1,

\[
H(X\mid U)=H(Y\mid V)=H(Z\mid W)=0.
\tag{7.2}
\]

Thus the high-entropy helpers individually carry the three free coordinates.

---

## 8. Helper-only atoms cannot couple the three branches

From (7.2) and the pair entropies of the addition slice,

\[
H(U,V)\ge H(X,Y)=2\log m,
\]

\[
H(U,W)\ge H(X,Z)=2\log m,
\]

\[
H(V,W)\ge H(Y,Z)=2\log m.
\tag{8.1}
\]

Also

\[
H(U,V,W)\ge H(X,Y,Z)=2\log m.
\tag{8.2}
\]

But every primitive relation in the preprocessing structure has at most

\[
N^{\alpha+o(1)}
\]

tuples, with `alpha<7/6<2`. Therefore no helper-only atom containing two or three of `U,V,W` can contain the sampled witness support: its entropy would have to be asymptotically at least `2 log N`, contradicting the relation-size bound.

Hence every helper-only atom is unary (up to constants/repetitions) on the high-entropy helper variables.

Together with (7.1), the entire CQ body decomposes into three independent components:

\[
(X,U),
\qquad
(Y,V),
\qquad
(Z,W),
\]

plus unary restrictions.

A conjunction of three independent components has a Cartesian-product output on the three free variables. It therefore cannot equal the non-Cartesian Latin relation

\[
Z=X+Y.
\]

Contradiction.

---

## 9. Main theorem

### Theorem HM-CQ6-ENTROPY

Every static relational preprocessing representation of exact truncated addition decoded by a six-variable conjunctive query satisfies

\[
\boxed{
S_N\ge N^{7/6-o(1)}.
}
\]

Equivalently,

\[
\boxed{
\sigma_1^{CQ}(6)\ge\frac76>1.
}
\]

In particular, `CQ^6` cannot achieve near-linear preprocessing.

Since AL2 contains the additive benchmark,

\[
\boxed{
\sigma_2^{CQ}(6)\ge\frac76.
}
\]

Therefore the common near-linear threshold obeys

\[
\boxed{k_+=k_{AL1}=k_{AL2}\ge7.}
\]

Combined with the CRT `CQ^9` construction,

\[
\boxed{7\le k_+\le9.}
\]

---

## 10. Why this closes the mixed-helper case

The previous `CQ6_ENTROPY_BOTTLENECK.md` isolated a mixed helper-core as the unresolved case because simple AGM/rectangle arguments only handled specific helper hypergraphs.

The present proof bypasses helper-core classification entirely.

It uses only:

1. the Latin-box property of exact addition;
2. deterministic witness selection;
3. entropy upper bounds forced by preprocessing relation sizes;
4. pairwise near-independence of the three free arithmetic coordinates;
5. the fact that there are only three helper pebbles.

Thus cyclic, path-like, mixed, or branch-hosted helper couplings are covered uniformly.

---

## 11. Claim ceiling

The theorem proves a `7/6` storage-exponent lower bound, not a quadratic lower bound for `CQ^6`.

No claim is made here that

\[
\sigma_1^{CQ}(6)=2.
\]

The exact exponent between `7/6` and `2`, and the exact near-linear threshold among widths `7,8,9`, remain open.

---

## 12. Literature calibration

The entropy method is consistent with the standard use of entropy vectors for conjunctive-query size bounds under functional dependencies. In particular, Gogacz and Torunczyk characterize worst-case CQ size bounds with FDs through entropy methods, while recent factorised-representation work uses structural and communication-complexity lower bounds for succinct join representations.

The argument here is specialized to the exact addition relation and exploits its Latin/quasigroup functional dependencies rather than claiming a generic CQ entropy theorem.

References:

- Tomasz Gogacz, Szymon Torunczyk, *Entropy Bounds for Conjunctive Queries with Functional Dependencies*, ICDT 2017, DOI 10.4230/LIPIcs.ICDT.2017.15.
- Christoph Berkholz, Harry Vinall-Smeeth, *Factorised Representations of Join Queries: Tight Bounds and a New Dichotomy*, ICDT 2026, DOI 10.4230/LIPIcs.ICDT.2026.11.
