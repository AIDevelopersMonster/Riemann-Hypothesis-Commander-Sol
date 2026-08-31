# Reflection-Graded Partial Algebras — Foundations

**Version:** 0.1  
**Date:** 2026-08-31  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** SUCCESSOR THEORY OPEN / FOUNDATIONAL THEOREMS PROVED  
**Origin:** extracted from `SOL_GRADED_REPORT_v0_1.md`, `SOL_GRADED_EXCHANGE_SELECTION_v0_2.md`, and `SOL_GRADED_BILINEAR_LIFT_NO_GO_v0_3.md`  
**Base FCOA publication:** DOI 10.5281/zenodo.22169264

---

## 1. Executive result

The SOL-GRADED hostile test leaves behind a mathematical object that is more faithful to FCOA than a Lie superalgebra:

\[
\boxed{\text{a partial algebra carrying an involutive reflection whose linear eigenspaces grade the defined product,}}
\tag{1}
\]

with a distinguished locus on which reflection of both participants becomes literal argument exchange.

This note extracts that object from the FCOA example and proves that it supports an independent elementary theory of

1. morphisms and strong embeddings;
2. free linearization and induced `Z_2` grading;
3. conservative completion ordered by extension of the operation graph;
4. reflection-orbit classification of new cells;
5. forced and accidental exchange loci;
6. functoriality and completion monotonicity of exchange data.

The resulting class will be called **reflection-graded partial algebras** (RGPAs) at the linear level, with **reflection-partial magmas** (RPMs) as their set-level antecedents.

The claim made here is mathematical, not bibliographic:

\[
\boxed{\text{the axioms below define a coherent independent category with nontrivial completion and exchange theory.}}
\tag{2}
\]

A preliminary literature check finds close neighbors in partial magmas, locality semigroups, partial `*`-algebras, and partial groups, but not yet an exact standard framework centered on the simultaneous-reflection law and its exchange locus. A full novelty claim is deferred until a dedicated bibliography audit is complete.

---

## 2. Set-level object: reflection-partial magma

### Definition 2.1 — reflection-partial magma

A **reflection-partial magma** is a quadruple

\[
\mathcal A=(A,D,\mu,\nu)
\tag{3}
\]

where

- `A` is a set;
- `D subseteq A x A` is the domain of a partial binary operation;
- `mu:D -> A` is a function;
- `nu:A -> A` is an involution,
  \[
  \nu^2=\operatorname{id}_A;
  \tag{4}
  \]
- the domain is invariant under simultaneous reflection,
  \[
  (x,y)\in D
  \iff
  (\nu x,\nu y)\in D;
  \tag{5}
  \]
- the product is reflection-equivariant,
  \[
  \boxed{
  \mu(\nu x,\nu y)=\nu\mu(x,y)
  }
  \qquad((x,y)\in D).
  \tag{6}
  \]

No associativity, commutativity, unit, cancellation, or totality is assumed.

### Remark 2.2 — typed enhancement

For FCOA and similar systems, `A` may be partitioned into sorts

\[
A=\bigsqcup_{s\in S}A_s,
\tag{7}
\]

with an involution `sigma:S->S` satisfying

\[
\nu(A_s)=A_{\sigma(s)}.
\tag{8}
\]

Terminal outputs are simply elements of sorts that never occur in the input projection of `D`. Thus typed non-reentry can be preserved without identifying terminal outputs with null or base values.

The untyped theory below applies to the disjoint union `A`; sort-preserving morphisms give the typed subcategory.

---

## 3. Morphisms

### Definition 3.1 — RPM morphism

Let

\[
\mathcal A=(A,D_A,\mu_A,\nu_A),
\qquad
\mathcal B=(B,D_B,\mu_B,\nu_B).
\]

A map

\[
f:A\to B
\tag{9}
\]

is an **RPM morphism** if

\[
f\nu_A=\nu_B f,
\tag{10}
\]

and for every `(x,y) in D_A`,

\[
(fx,fy)\in D_B,
\tag{11}
\]

\[
f\mu_A(x,y)=\mu_B(fx,fy).
\tag{12}
\]

### Definition 3.2 — strong morphism and strong embedding

An RPM morphism is **strong** if it also reflects definedness:

\[
(x,y)\in D_A
\iff
(fx,fy)\in D_B.
\tag{13}
\]

A strong morphism is a **strong embedding** if `f` is injective.

This is the correct categorical form of FCOA legacy exactness: a strong embedding preserves not only old values but also old `UNDEF` cells.

### Theorem 3.3 — category theorem

Reflection-partial magmas and RPM morphisms form a category, denoted

\[
\mathbf{RPM}.
\tag{14}
\]

Strong morphisms are closed under composition, and strong embeddings define the natural exact-substructure notion.

### Proof

The identity map trivially preserves reflection, defined cells, and products.

Let `f:A->B` and `g:B->C` be RPM morphisms. If `(x,y) in D_A`, then `(fx,fy) in D_B`, hence `(gfx,gfy) in D_C`, and

\[
\begin{aligned}
(gf)\mu_A(x,y)
&=g\mu_B(fx,fy)\\
&=\mu_C(gfx,gfy).
\end{aligned}
\]

Also

\[
(gf)\nu_A=g\nu_B f=\nu_C(gf).
\]

Thus composition is again a morphism. If both maps reflect definedness, the two biconditionals compose. QED.

---

## 4. Linear object: reflection-graded partial algebra

Let `K` be a field with

\[
\operatorname{char}K\ne2.
\tag{15}
\]

### Definition 4.1 — RGPA

A **reflection-graded partial algebra** over `K` is a quadruple

\[
\mathcal V=(V,\mathscr D,m,J)
\tag{16}
\]

where

- `V` is a `K`-vector space;
- `J:V->V` is a linear involution;
- `mathscr D` is a linear subspace of `V tensor V`;
- `mathscr D` is invariant under `J tensor J`;
- `m:mathscr D->V` is linear and satisfies
  \[
  \boxed{
  Jm=m(J\otimes J).
  }
  \tag{17}
  \]

Because `char K != 2`,

\[
V=V_{\bar0}\oplus V_{\bar1},
\tag{18}
\]

where

\[
V_{\bar0}=\ker(J-I),
\qquad
V_{\bar1}=\ker(J+I).
\tag{19}
\]

### Theorem 4.2 — partial grade law

If

\[
u\in V_{\bar p},
\qquad
v\in V_{\bar q},
\qquad
u\otimes v\in\mathscr D,
\]

then

\[
\boxed{
m(u\otimes v)\in V_{\overline{p+q}}.
}
\tag{20}
\]

### Proof

Since

\[
(J\otimes J)(u\otimes v)=(-1)^{p+q}u\otimes v,
\]

(17) gives

\[
Jm(u\otimes v)=(-1)^{p+q}m(u\otimes v).
\]

Thus the output has parity `p+q mod 2`. QED.

The key distinction from an ordinary graded algebra is that (20) is asserted only when the tensor is in the actual partial domain `mathscr D`.

---

## 5. Free Linearization Theorem

### Construction 5.1

Let

\[
\mathcal A=(A,D,\mu,\nu)
\]

be an RPM. Define

\[
K[A]=\operatorname{span}_K\{e_x:x\in A\}.
\tag{21}
\]

Let

\[
Je_x=e_{\nu x}.
\tag{22}
\]

Define

\[
\mathscr D_A
=
\operatorname{span}_K
\{e_x\otimes e_y:(x,y)\in D\}.
\tag{23}
\]

and

\[
\widetilde\mu(e_x\otimes e_y)=e_{\mu(x,y)}
\qquad((x,y)\in D).
\tag{24}
\]

### Theorem 5.2 — free linearization

The quadruple

\[
K[\mathcal A]
=
(K[A],\mathscr D_A,\widetilde\mu,J)
\tag{25}
\]

is an RGPA.

Every RPM morphism `f:A->B` induces a linear RGPA morphism

\[
K[f]:K[A]\to K[B],
\qquad
K[f](e_x)=e_{f(x)}.
\tag{26}
\]

Hence free linearization defines a functor

\[
\boxed{
K[-]:\mathbf{RPM}\longrightarrow\mathbf{RGPA}_K.
}
\tag{27}
\]

### Proof

Domain invariance (5) gives

\[
(J\otimes J)\mathscr D_A=\mathscr D_A.
\]

On a defined basis tensor,

\[
\begin{aligned}
J\widetilde\mu(e_x\otimes e_y)
&=e_{\nu\mu(x,y)}\\
&=e_{\mu(\nu x,\nu y)}\\
&=\widetilde\mu(Je_x\otimes Je_y).
\end{aligned}
\]

Thus (17) holds. Morphism compatibility follows from (10)-(12), and identities/composition are preserved by the ordinary free-vector-space construction. QED.

### Consequence

The `Z_2` grading is not additional data at the linear level once the set-level reflection has been fixed: it is generated by the involution through its eigenspaces.

---

## 6. Conservative completion as an ordered space

The natural completion object is the graph of the partial operation.

For an RPM `A`, define

\[
G_\mu
=
\{(x,y,z)\in A^3:(x,y)\in D,\ z=\mu(x,y)\}.
\tag{28}
\]

Reflection acts on triples by

\[
\widehat R(x,y,z)=(\nu x,\nu y,\nu z).
\tag{29}
\]

An RPM operation graph is precisely a functional relation `G subseteq A^3` invariant under `widehat R`.

### Definition 6.1 — completion problem

Fix

1. a reflected set `(A,nu)`;
2. a base invariant functional graph `G_0`;
3. a protected reflection-invariant set of forbidden input cells
   \[
   P\subseteq A^2.
   \tag{30}
   \]

A **conservative completion** is any invariant functional graph `G` such that

\[
G_0\subseteq G,
\tag{31}
\]

and no triple of `G` has first two coordinates in `P`.

Order completions by graph inclusion:

\[
G\preceq H
\iff
G\subseteq H.
\tag{32}
\]

Denote this poset by

\[
\operatorname{Comp}(G_0;P).
\tag{33}
\]

### Theorem 6.2 — completion-domain theorem

If `G_0` itself avoids `P`, then `Comp(G_0;P)` is

1. a pointed poset with bottom element `G_0`;
2. closed under arbitrary nonempty intersections;
3. closed under directed unions;
4. therefore a directed-complete partial order (dcpo) and a complete meet-semilattice;
5. not, in general, a lattice, because two completions may assign different outputs to the same previously undefined input cell and hence have no common upper bound.

### Proof

Every member contains `G_0`, so `G_0` is bottom.

The intersection of invariant functional graphs is again invariant and functional, still contains `G_0`, and still avoids `P`.

Let `{G_i}` be directed. Put

\[
G=\bigcup_iG_i.
\]

Invariance and avoidance of `P` pass to the union. To prove functionality, suppose both `(x,y,z)` and `(x,y,w)` lie in `G`. They lie in some `G_i` and `G_j`. Directedness gives a `G_k` containing both; since `G_k` is functional, `z=w`.

Thus `G` is the directed supremum.

Finally, if two extensions assign distinct outputs `z!=w` to one input pair `(x,y)`, no functional graph can contain both. Hence a join need not exist. QED.

### Corollary 6.3 — maximal completions exist

Every chain has an upper bound given by its union. Therefore Zorn's lemma gives at least one maximal conservative completion.

Maximal does not mean total: protected cells and fixed-orbit output obstructions may remain permanently undefined.

---

## 7. Orbitwise Completion Theorem

Let

\[
R_2(x,y)=(\nu x,\nu y)
\tag{34}
\]

act on input cells.

Ignore cells already fixed by `G_0` and protected cells `P`. The remaining cells split into `C_2`-orbits.

### Theorem 7.1 — orbitwise completion

For a free untyped completion problem with no additional identities beyond reflection equivariance:

- on a two-point input orbit
  \[
  \{p,R_2p\},
  \qquad p\ne R_2p,
  \tag{35}
  \]
  choosing one output `z in A` for `p` uniquely forces
  \[
  \mu(R_2p)=\nu z;
  \tag{36}
  \]
- on a fixed input orbit
  \[
  R_2p=p,
  \tag{37}
  \]
  a value can be assigned only from the reflection-fixed output set
  \[
  A^\nu=\{z\in A:\nu z=z\}.
  \tag{38}
  \]

### Proof

For a two-point orbit, equivariance (6) gives (36), and applying reflection again is consistent because `nu^2=id`.

For a fixed pair `p`, equivariance requires

\[
\mu(p)=\mu(R_2p)=\nu\mu(p),
\]

hence the output must lie in `A^nu`. Conversely every such fixed output defines an invariant value on the fixed input orbit. QED.

### Flat-domain description

Choose one representative from each unresolved two-point orbit. Each such orbit contributes a flat choice poset

\[
\{\bot\}\cup A,
\tag{39}
\]

where `bot` means 'remain undefined'. Each fixed orbit contributes

\[
\{\bot\}\cup A^\nu.
\tag{40}
\]

Different non-bottom choices are incomparable.

Thus, before adding associativity or other global identities, the completion dcpo is a product of local flat choice domains, with coordinates already fixed by `G_0` removed.

This makes reflection-compatible completion explicitly orbit-computable.

---

## 8. Exchange geometry

Define swap

\[
S(x,y)=(y,x).
\tag{41}
\]

and simultaneous reflection `R_2` by (34).

### Definition 8.1 — geometric mirror locus

\[
M_\nu
=
\operatorname{Eq}(R_2,S)
=
\{(x,y):R_2(x,y)=S(x,y)\}.
\tag{42}
\]

### Theorem 8.2 — universal mirror-locus theorem

For every involution `nu`,

\[
\boxed{
M_\nu=\{(x,\nu x):x\in A\}.
}
\tag{43}
\]

### Proof

`R_2(x,y)=S(x,y)` is equivalent to

\[
\nu x=y,
\qquad
\nu y=x.
\]

The first condition is `y=nu x`; the second follows from involutivity. QED.

Thus the graph of the reflection is exactly the locus where geometry turns simultaneous reflection into exchange.

---

## 9. Forced and algebraic exchange loci

### Definition 9.1 — forced geometric exchange locus

For an RPM `mathcal A`, define

\[
E_{\mathrm{geom}}(\mathcal A)
=D\cap M_\nu.
\tag{44}
\]

These are the defined mirror cells.

### Definition 9.2 — algebraic exchange locus

Define

\[
E_{\mathrm{alg}}(\mathcal A)
=
\left\{
(x,y)\in D:
(y,x)\in D,
\ \mu(y,x)=\nu\mu(x,y)
\right\}.
\tag{45}
\]

This larger locus records every defined pair on which the same reflection-mediated exchange equation happens to hold, whether or not it is forced by participant geometry.

### Theorem 9.3 — exchange-locus inclusion

For every RPM,

\[
\boxed{
E_{\mathrm{geom}}(\mathcal A)
\subseteq
E_{\mathrm{alg}}(\mathcal A).
}
\tag{46}
\]

### Proof

Let `p=(x,nu x)` lie in `D`. Since `D` is reflection-invariant,

\[
R_2p=(\nu x,x)\in D.
\]

But on `M_nu`, `R_2p=Sp`. Equivariance gives

\[
\mu(Sp)
=
\mu(R_2p)
=
\nu\mu(p).
\]

Hence `p in E_alg`. QED.

### Definition 9.4 — excess exchange locus

\[
E_{\mathrm{excess}}
=
E_{\mathrm{alg}}\setminus E_{\mathrm{geom}}.
\tag{47}
\]

`E_excess` measures exchange laws not explained solely by the reflection geometry of the participants. It is therefore a candidate invariant for detecting genuinely additional algebraic structure.

---

## 10. Exchange spectrum

On the forced exchange locus, define

\[
E_{\mathrm{fix}}
=
\{p\in E_{\mathrm{geom}}:\nu\mu(p)=\mu(p)\},
\tag{48}
\]

and

\[
E_{\mathrm{split}}
=
E_{\mathrm{geom}}\setminus E_{\mathrm{fix}}.
\tag{49}
\]

### Theorem 10.1 — set-level exchange classification

If `p in E_geom`, then

\[
\mu(Sp)=\nu\mu(p).
\tag{50}
\]

Therefore

\[
p\in E_{\mathrm{fix}}
\iff
\mu(Sp)=\mu(p),
\tag{51}
\]

while every `p in E_split` is two-way defined but noncommutative.

This generalizes the FCOA mirror-orbit theorem to every RPM.

### Theorem 10.2 — linear exchange decomposition

Let `K[A]` be the free linearization and let

\[
z=\widetilde\mu(e_x\otimes e_{\nu x}).
\]

Decompose

\[
z=z_{\bar0}+z_{\bar1},
\qquad
Jz_{\bar0}=z_{\bar0},
\quad
Jz_{\bar1}=-z_{\bar1}.
\tag{52}
\]

Then

\[
\boxed{
\widetilde\mu(e_{\nu x}\otimes e_x)
=z_{\bar0}-z_{\bar1}.
}
\tag{53}
\]

Hence reflection-even output is exchange-symmetric and reflection-odd output is exchange-antisymmetric.

### Proof

The reverse pair equals the simultaneous reflection of the original pair, so equivariance gives `Jz`. Substituting the eigenspace decomposition proves (53). QED.

---

## 11. Functoriality of exchange loci

### Theorem 11.1 — covariance under morphisms

Let

\[
f:\mathcal A\to\mathcal B
\]

be an RPM morphism. Then

\[
(f\times f)igl(E_{\mathrm{geom}}(\mathcal A)\bigr)
\subseteq
E_{\mathrm{geom}}(\mathcal B),
\tag{54}
\]

and

\[
(f\times f)igl(E_{\mathrm{alg}}(\mathcal A)\bigr)
\subseteq
E_{\mathrm{alg}}(\mathcal B).
\tag{55}
\]

### Proof

If `(x,nu_A x)` is a defined mirror pair, then

\[
(fx,f\nu_Ax)=(fx,\nu_Bfx)
\]

is defined by morphism preservation, proving (54).

If `(x,y)` lies in `E_alg(A)`, then both orientations are defined after applying `f`, and

\[
\begin{aligned}
\mu_B(fy,fx)
&=f\mu_A(y,x)\\
&=f\nu_A\mu_A(x,y)\\
&=\nu_B f\mu_A(x,y)\\
&=\nu_B\mu_B(fx,fy).
\end{aligned}
\]

Thus (55). QED.

### Theorem 11.2 — exactness under strong embeddings

If `f` is a strong embedding, then for pairs from `A x A`, both defined exchange loci are reflected exactly:

\[
E_{\mathrm{geom}}(\mathcal A)
=(f\times f)^{-1}igl(E_{\mathrm{geom}}(\mathcal B)\bigr),
\tag{56}
\]

\[
E_{\mathrm{alg}}(\mathcal A)
=(f\times f)^{-1}igl(E_{\mathrm{alg}}(\mathcal B)\bigr).
\tag{57}
\]

### Proof

Strongness reflects domain membership; injectivity reflects the mirror equation `fy=nu_B fx` back to `y=nu_A x` and also reflects equality of output images in the algebraic exchange equation. QED.

This shows why strong embeddings, not merely weak homomorphisms, are the correct morphisms for exact legacy-preserving analysis.

---

## 12. Exchange loci under completion

Suppose two conservative completions on the same reflected carrier satisfy

\[
G_A\subseteq G_B.
\tag{58}
\]

### Theorem 12.1 — exchange monotonicity

Then

\[
E_{\mathrm{geom}}(A)
\subseteq
E_{\mathrm{geom}}(B),
\tag{59}
\]

and

\[
E_{\mathrm{alg}}(A)
\subseteq
E_{\mathrm{alg}}(B).
\tag{60}
\]

Moreover every previously defined geometric exchange cell retains its `fix/split` classification.

### Proof

Graph extension preserves every old defined value. A geometric cell remains defined, and its reflected reverse and outputs remain unchanged. The same is true for every old algebraic exchange pair. Hence both loci can only grow. Since the old output is unchanged, whether it is reflection-fixed is unchanged. QED.

### Finite exchange profile

For a finite RPM define

\[
\Xi(\mathcal A)
=
\bigl(
|E_{\mathrm{geom}}|,
|E_{\mathrm{fix}}|,
|E_{\mathrm{split}}|,
|E_{\mathrm{excess}}|
\bigr).
\tag{61}
\]

`Xi` is invariant under RPM isomorphism. Under conservative completion, the first three entries can increase only by adding new geometric exchange orbits; classifications of old cells cannot change. The excess term records genuinely non-geometric exchange laws and is therefore especially useful for comparing completions.

---

## 13. Non-FCOA examples

The class is not confined to the signed FCOA line.

### Example 13.1 — group with involutive automorphism

Let `G` be any group and let

\[
\nu:G\to G
\]

be an involutive group automorphism. With total multiplication

\[
D=G\times G,
\qquad
\mu(x,y)=xy,
\tag{62}
\]

we obtain an RPM because

\[
\mu(\nu x,\nu y)
=\nu x\,\nu y
=\nu(xy).
\]

For example, in a noncommutative matrix group one may take

\[
\nu(g)=P g P^{-1},
\qquad P^2=I.
\tag{63}
\]

Then the mirror law reads

\[
(\nu x)x
=
\nu(x\nu x),
\tag{64}
\]

which need not be ordinary commutativity.

Thus the mirror-exchange theorem is not an artifact of FCOA terminal outputs or its rooted ray.

### Example 13.2 — paths in a quiver with reflection automorphism

Let `Q` be a quiver with an involutive quiver automorphism `nu`. Let `A` be its set of finite paths and define `mu(p,q)` only when the paths are composable. The quiver automorphism preserves composability and satisfies

\[
\nu(pq)=\nu(p)\nu(q).
\tag{65}
\]

Hence the path system is an RPM.

Its domain is naturally directional and need not be a symmetric relation. This distinguishes the general RPM setting from locality-semigroup frameworks in which the defining locality relation is symmetric.

### Example 13.3 — FCOA-Z

The signed FCOA-Z carrier with its derived reflection and any reflection-compatible partial operation is a typed RPM. Its free linearization is an RGPA. The SOL-GRADED results are therefore one concrete nonassociative, typed, role-asymmetric member of the general theory.

---

## 14. Relation to neighboring theories

The present framework overlaps existing theories but is not identical to their defining axioms.

### 14.1 Partial magmas

A partial magma already provides a set and a partially defined binary product. RPM adds a distinguished involution acting **covariantly and without swapping inputs** as in (6), and studies the equalizer of simultaneous reflection with argument swap.

### 14.2 Locality semigroups

Locality semigroups use a partial product whose domain comes from a locality relation, typically symmetric, together with compatibility and associativity requirements. RPM permits asymmetric domains and makes no associativity assumption. The quiver-path example above is therefore naturally within RPM even when its raw composability relation is directional.

### 14.3 Partial `*`-algebras

A standard partial `*`-algebra uses an involution satisfying the anti-multiplicative law

\[
(xy)^*=y^*x^*.
\tag{66}
\]

RPM instead uses the automorphism-type law

\[
\nu(xy)=\nu x\,\nu y
\tag{67}
\]

on defined products. The swap in RPM is therefore not built into the involution law: it emerges only on `M_nu` where `R_2=S`.

This distinction is precisely what makes the exchange locus nontrivial.

### 14.4 Partial groups

Partial groups carry an inversion and a product on selected words satisfying strong group-like axioms. RPM imposes none of those word, inverse, or unit axioms. Reflection need not be inversion.

### 14.5 Superalgebras

A superalgebra begins with a `Z_2`-grading and usually a total bilinear product/bracket. RGPA begins with an involution and a partial tensor domain. The grading is generated from the reflection eigenspaces after linearization, while no braiding or super sign is forced.

---

## 15. What is genuinely new inside the extracted theory

The following package is intrinsic to the RPM/RGPA viewpoint rather than inherited verbatim from the neighboring definitions:

\[
\boxed{
R_2=\nu\times\nu,
\qquad
S=\text{swap},
\qquad
M_\nu=\operatorname{Eq}(R_2,S)=\operatorname{graph}(\nu).
}
\tag{68}
\]

From this one gets automatically:

1. forced mirror exchange;
2. fixed-versus-split exchange spectrum;
3. an excess exchange locus measuring additional laws;
4. functoriality under reflection-preserving partial homomorphisms;
5. exact preservation under strong embeddings;
6. monotone growth under conservative completion;
7. reflection-orbit coordinates for the completion dcpo.

This is enough structure to justify treating RPM/RGPA as a mathematical class in its own right.

---

## 16. Publication threshold

### Mathematical readiness

The class is now **well-defined and nonempty**, has a category, a strong-embedding notion, a free-linearization functor, an orbitwise completion theorem, and functorial exchange loci.

Therefore the answer to the internal research question

> Do reflection-graded partial algebras form an independent mathematical class with their own morphism, completion, and exchange-locus theory?

is

\[
\boxed{\textbf{YES, at the foundational mathematical level.}}
\tag{69}
\]

### Bibliographic readiness

A standalone novelty claim is **not yet frozen**. The nearest literature already contains substantial theories of partial magmas, locality semigroups, partial `*`-algebras, and partial groups. The exact simultaneous-reflection/exchange-locus package appears distinct in the preliminary search, but a dedicated literature audit is required before claiming priority.

### Publication decision

Do **not** publish the standalone RGPA note yet.

The next publication threshold should require at least:

1. a systematic literature/terminology audit;
2. one representation or universal-property theorem beyond free linearization;
3. at least two genuinely non-FCOA examples with computed exchange profiles;
4. a classification theorem for a nontrivial finite completion family.

At that point the RGPA theory would justify separation from SOL-GRADED into its own paper/module.

---

## 17. Next research frontier

The highest-value next strike is finite classification.

Given a finite reflected carrier `(A,nu)`, protected domain `P`, and legacy graph `G_0`, classify conservative completions up to strong RPM isomorphism using

\[
\boxed{
\text{reflection input-orbits}
+
\text{output reflection-orbits}
+
\Xi(\mathcal A).
}
\tag{70}
\]

The first decisive question is whether the exchange profile `Xi`, together with orbit data, is complete for minimal one-orbit extensions or whether two non-isomorphic completions can share the same profile.

A counterexample would identify the next invariant; a positive theorem would give the first genuine classification result of the new theory.

---

## 18. Preliminary literature anchors

The comparison layer should cite primary or reliable sources for the neighboring classes:

- Jean-Pierre Antoine and W. Karwowski, *Partial *-Algebras of Closed Linear Operators in Hilbert Space*, Publ. RIMS 21 (1985), 205-236, DOI 10.2977/PRIMS/1195179844.
- Pierre Clavier, Li Guo, Sylvie Paycha, Bin Zhang and related locality-structure work on locality semigroups and locality morphisms.
- Partial-group literature following Chermak, where products are defined on selected words and inversion is part of the axioms.

These sources are comparison targets only; the RPM/RGPA theorems above are derived directly from Definitions 2.1 and 4.1.
