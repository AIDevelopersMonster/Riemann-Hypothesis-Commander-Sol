# Selector Geometry for Mixed Extensions of a Reflected Partial Algebra

**Malachevsky, A.A.**  
ORCID: 0009-0008-6009-3196  
Commander Sol Mathematics Programme

## Abstract

We study a selection problem for mixed-sector completions of a reflected partial algebra. The aim is to compare admissible completions without building the desired answer into the morphisms. The old partial algebra is fixed pointwise, protected undefined cells remain protected, and morphisms preserve only source-defined operations together with the inherited reflection and transport wherever those are defined. Within this weak, core-fixed category we obtain a staged universal ladder

\[
M_0\longrightarrow F_{\to}\longrightarrow F_{\mathrm{mix}}\longrightarrow B0\longrightarrow BR.
\]

The stages separate optional domain completion, ordered mixed-event identity, forgetting of argument orientation, forgetting of endpoint identity, and anchoring of the remaining event to the old root. The unbiased free full mixed completion is indexed by ordered mixed cells; mixed commutativity appears only after a quotient. After commutativity, pure event quotients are controlled by reflection-invariant equivalence relations. Inside this quotient geometry two canonically generated radial statistics, span and gap, yield incomparable kernels with exact meet and join

\[
\theta_{\rm span}\wedge\theta_{\rm gap}=\theta_{\rm orb},
\qquad
\theta_{\rm span}\vee\theta_{\rm gap}=\theta_{\rm phase}.
\]

Pure event quotients lie in a classical invariant-partition lattice, whereas allowing event-to-core anchoring while keeping the old core pointwise separated produces a quotient poset in which joins can fail. The relation-only object `B0` has a unique reflection-compatible base-line anchor, namely the root-return quotient `BR`. The arrow `B0 -> BR` exists for preservation-only morphisms but disappears under stronger output-typing or definedness-reflection requirements. The individual universal-algebraic tools used here are classical; the contribution is the combined selector architecture and its FCOA-specific quotient geometry.

**Keywords:** partial algebra; weak homomorphism; congruence; quotient; free completion; G-set; reflected algebra; mixed sector; selector geometry; FCOA.

---

## 1. Introduction

Suppose a partial algebra has already been constructed on a signed, reflected line. Same-side values are inherited from an older one-sided structure and are fixed, while the genuinely mixed pairs remain open. There are many possible ways to complete those mixed cells. One can return to the root, create a new cross-event, retain endpoint information, retain radial information, or introduce further output fibers and re-entry laws.

The central problem is not merely to list such completions. It is to compare them without inserting the desired comparison result into the definition of morphism.

The guiding rule is therefore:

\[
\boxed{\text{preserve the old holes by position, not their number.}}
\tag{1.1}
\]

In particular, the first morphism layer does not preserve the number of undefined cells, the number of new states, externality of outputs, terminality, re-entry, automorphism groups, model-theoretic complexity, or any externally chosen cost function.

The resulting structure has an unexpectedly rigid hierarchy. The first correction is that an all-mixed free object cannot be initial if mixed cells are optional. The second is that the first unbiased free completion must distinguish ordered mixed cells: commutativity is itself a quotient. Once these two corrections are made, the selector geometry becomes transparent.

The present paper develops that geometry and isolates the precise point at which a simple quotient lattice becomes a non-lattice anchored poset.

---

## 2. Background and scope

Preservation-only homomorphisms for partial algebras, weak and strong congruence conventions, quotient constructions, free completions, and congruence lattices of unary algebras or G-sets are classical topics. We use these tools as background rather than claim them as new. In particular, preservation-only morphisms are a standard convention in modern treatments of partial algebras, although terminology varies; see Hoefnagel and Jacqmin (2024). Congruence lattices of G-sets and related unary algebras have been studied extensively, including work of Vernikov (1997) and Seif (2013).

Our contribution is narrower: we use these standard ingredients to analyse a fixed reflected FCOA core, separate several distinct information-loss operations, construct an explicit incomparable pair of canonically generated quotient invariants, and identify a transition from a pure invariant-partition lattice to a core-anchored quotient poset with missing joins.

We make no claim in this paper that the unbounded span, gap, or phase relations are uniformly parameter-free first-order definable in the weakest infinite reduct. They are used as canonically generated structural invariants of the inherited contraction geometry.

---

## 3. Fixed reflected core

Let the old partial algebra be

\[
\mathcal M_0.
\]

Let its old universe be `C_0` and let

\[
X=\{P_0\}\sqcup\{P_n^+:n\ge1\}\sqcup\{P_n^-:n\ge1\}
\subseteq C_0
\tag{3.1}
\]

be the distinguished signed base line. The root is

\[
x_0=P_0.
\tag{3.2}
\]

Reflection acts by

\[
\nu(P_0)=P_0,
\qquad
\nu(P_n^+)=P_n^-,
\qquad
\nu(P_n^-)=P_n^+.
\tag{3.3}
\]

Let

\[
D_0=\operatorname{Dom}(\oplus_0)\cap(X\times X)
\tag{3.4}
\]

be the originally defined base-base cells. Let

\[
M=(X^+\times X^-)\cup(X^-\times X^+)
\tag{3.5}
\]

be the genuinely mixed frontier. The protected old holes are

\[
U_{\rm prot}=(X\times X)\setminus(D_0\cup M).
\tag{3.6}
\]

The parent signed construction implies that, once the inherited same-side table and reflection are fixed, all remaining new base-base freedom is localized in `M`.

---

## 4. Admissible extensions and weak core-fixed morphisms

### Definition 4.1. Admissible extension

An admissible extension `A` contains an injective copy

\[
i_A:\mathcal M_0\hookrightarrow A
\tag{4.1}
\]

such that:

1. every old defined operation and value is preserved exactly;
2. no cell in `U_{\rm prot}` becomes defined;
3. every new base-base core cell lies in `M`;
4. any reflection-compatible subset of `M` may be opened;
5. no primitive output-sort distinction is assumed at the first layer.

### Definition 4.2. Weak core-fixed morphism

A morphism

\[
f:A\to B
\tag{4.2}
\]

satisfies:

\[
f\circ i_A=i_B,
\tag{4.3}
\]

and whenever

\[
a\oplus_A b\downarrow,
\tag{4.4}
\]

we require

\[
f(a)\oplus_Bf(b)\downarrow,
\qquad
f(a\oplus_A b)=f(a)\oplus_Bf(b).
\tag{4.5}
\]

The same one-way preservation law is imposed for inherited partial unary operations such as transport. Reflection is preserved:

\[
f(\nu_Aa)=\nu_Bf(a).
\tag{4.6}
\]

No converse definedness condition is imposed, and no injectivity is required outside the old core.

### Theorem 4.3. Category closure

The admissible extensions and weak core-fixed morphisms form a category

\[
\mathbf{Ext}_{\le M}(M_0).
\tag{4.7}
\]

#### Proof

Identity maps clearly fix the old core, preserve each source-defined operation, and commute with reflection. Let

\[
A\xrightarrow{f}B\xrightarrow{g}C
\]

be morphisms. Core fixation gives

\[
(gf)i_A=g i_B=i_C.
\]

If `a oplus_A b` is defined, preservation by `f` makes `f(a) oplus_B f(b)` defined with value `f(a oplus_A b)`; preservation by `g` then gives

\[
gf(a\oplus_A b)=gf(a)\oplus_Cgf(b).
\]

Unary preservation and reflection equivariance compose in the same way. Associativity and identity laws are inherited from function composition. \(\square\)

The protected-hole condition is an axiom on objects, not reverse-definedness of morphisms. This distinction is essential.

---

## 5. The first obstruction: optional mixed definedness

### Proposition 5.1. Initial object of the broad category

The old algebra `M_0`, viewed as the extension with no newly opened mixed cells, is initial in

\[
\mathbf{Ext}_{\le M}(M_0).
\tag{5.1}
\]

#### Proof

Any morphism from `M_0` to an admissible extension is forced to equal the distinguished core embedding, because every source element is old. The embedding preserves all old defined operations by admissibility. Hence there is exactly one such morphism. \(\square\)

### Proposition 5.2. Domain-totality obstruction

If a source extension defines a mixed cell `p in M` while an admissible target leaves that same core cell undefined, then no weak core-fixed morphism from the source to the target exists.

#### Proof

Write `p=(x,y)`. Core fixation sends `x` and `y` to themselves. Since `x oplus y` is source-defined, morphism preservation forces the target cell `(x,y)` to be defined, contradiction. \(\square\)

Therefore an object defining all mixed cells cannot be initial in the broad optional-domain category.

---

## 6. Full mixed completions and the ordered free object

Let

\[
\mathbf{Comp}_M(M_0)
\subseteq
\mathbf{Ext}_{\le M}(M_0)
\tag{6.1}
\]

be the full subcategory in which every mixed cell is defined.

Before commutativity is imposed, ordered cells must remain distinct.

For each

\[
p=(x,y)\in M
\]

introduce a fresh terminal event

\[
e_{(x,y)}.
\]

Define

\[
|F_{\to}|=C_0\sqcup\{e_{(x,y)}:(x,y)\in M\},
\tag{6.2}
\]

with the old operations unchanged and

\[
x\oplus_{F_{\to}}y=e_{(x,y)}
\qquad((x,y)\in M).
\tag{6.3}
\]

No operation with a fresh event as input is added. Reflection acts by

\[
\nu(e_{(x,y)})=e_{(\nu x,\nu y)}.
\tag{6.4}
\]

### Theorem 6.1. Free full-completion theorem

`F_{\to}` is initial in `Comp_M(M_0)`.

#### Proof

For any full mixed target `A`, define `Phi_A` by identity on the old core and

\[
\Phi_A(e_{(x,y)})=x\oplus_A y.
\tag{6.5}
\]

This is defined for every generator because all mixed target cells are open. Old equations are preserved by exact core inheritance, and each mixed equation is preserved by construction. Reflection equivariance follows from that of `A`. Uniqueness is forced by (6.3): a homomorphism must send each `e_(x,y)` to the target value of the same mixed cell. \(\square\)

### Proposition 6.2. Unordered-pair obstruction

A source satisfying

\[
x\oplus y=y\oplus x=e_{\{x,y\}}
\]

cannot be initial in `Comp_M(M_0)` if that category contains any target with unequal mixed values for `(x,y)` and `(y,x)`.

#### Proof

A homomorphism would force the same source generator to map to both target values. \(\square\)

Thus mixed commutativity cannot be hidden inside the first free object.

---

## 7. Mixed commutativity as a quotient

Let `theta_tau` be the least reflection-compatible equivalence identifying

\[
e_{(x,y)}\sim e_{(y,x)}
\tag{7.1}
\]

for every mixed pair. Define

\[
F_{\rm mix}=F_{\to}/\theta_\tau.
\tag{7.2}
\]

Its event generators can be written

\[
e_{\{x,y\}}.
\]

Let `Comp_M^{comm}(M_0)` be the full subcategory of full mixed completions satisfying mixed commutativity.

### Theorem 7.1. Corrected free mixed theorem

\[
\boxed{F_{\rm mix}\text{ is initial in }\mathbf{Comp}^{comm}_M(M_0).}
\tag{7.3}
\]

#### Proof

The unique map from `F_{\to}` into a target `A` factors through `theta_tau` exactly when

\[
x\oplus_Ay=y\oplus_Ax
\]

for every mixed pair. In that case the induced map is unique. \(\square\)

The parent one-step bridge model `B1`, which assigns one terminal output to each unoriented mixed bridge, is therefore isomorphic to `F_mix` at this selector level.

---

## 8. The relation-only quotient and root return

Let all fresh mixed generators of `F_mix` be identified into one event class `E_cross`, without identifying that class with any old core point. The resulting quotient is `B0`:

\[
x\oplus_{B0}y=E_{\rm cross}
\qquad((x,y)\in M).
\tag{8.1}
\]

Since reflection permutes all mixed generators, the unique class is reflection-fixed:

\[
\nu(E_{\rm cross})=E_{\rm cross}.
\tag{8.2}
\]

Call a target relation-only if all mixed cells have one common value `c_A`, with no requirement that `c_A` be new.

### Theorem 8.1. Relation-only universality of `B0`

`B0` is initial among relation-only full mixed completions.

#### Proof

Fix the old core and send

\[
E_{\rm cross}\mapsto c_A.
\]

All mixed source equations are preserved, and uniqueness is forced by any one mixed cell. Reflection equivariance follows because the common target value is reflection-fixed. \(\square\)

Define `BR` by

\[
x\oplus_{BR}y=P_0
\qquad((x,y)\in M).
\tag{8.3}
\]

### Proposition 8.2. Directed comparison

There is a weak core-fixed morphism

\[
B0\longrightarrow BR,
\qquad
E_{\rm cross}\mapsto P_0.
\tag{8.4}
\]

If `E_cross != P_0` in `B0`, no reverse core-fixed weak morphism exists.

#### Proof

For the forward map, each mixed source value is sent to `P_0`, which equals the corresponding mixed value in `BR`. Reflection is preserved because both elements are fixed. For a hypothetical reverse map `h`, any mixed pair would give

\[
h(P_0)=h(x\oplus_{BR}y)=x\oplus_{B0}y=E_{\rm cross},
\]

while core fixation requires `h(P_0)=P_0`. Contradiction. \(\square\)

We have therefore obtained the staged universal ladder

\[
\boxed{
M_0\to F_{\to}\to F_{\rm mix}\to B0\to BR.
}
\tag{8.5}
\]

---

## 9. Weak quotient kernels and factorization

At the one-step level, fresh events are terminal. We use a weak partial congruence convention: equivalent input tuples are required to have equivalent outputs whenever both representative tuples are source-defined; definedness need not be invariant over the equivalence class.

For canonical quotient maps of `F_mix`, kernel inclusion controls factorization.

### Theorem 9.1. Kernel-factorization correspondence

Let `theta_A` and `theta_B` be admissible weak quotient kernels on `F_mix`. Then the canonical map

\[
F_{\rm mix}/\theta_A\to F_{\rm mix}/\theta_B
\tag{9.1}
\]

exists if and only if

\[
\theta_A\subseteq\theta_B.
\tag{9.2}
\]

#### Proof

If the inclusion holds, define `[a]_{theta_A} -> [a]_{theta_B}`. This is well-defined and operation-preserving by construction. Conversely, any factorization of the canonical quotient map must identify every pair already identified by `theta_A`, so `theta_A subseteq theta_B`. \(\square\)

This gives an intrinsic information order before any numerical cost is introduced.

---

## 10. Pure event quotient geometry

Write

\[
p_{ij}=\{P_i^+,P_j^-\},
\qquad i,j\ge1.
\tag{10.1}
\]

These index the fresh events of `F_mix`. Reflection acts by

\[
\nu(p_{ij})=p_{ji}.
\tag{10.2}
\]

Hence pure terminal-event quotient kernels are precisely equivalence relations on

\[
\mathbb N_{>0}^2
\tag{10.3}
\]

that are invariant under coordinate transposition. Their complete-lattice structure is classical unary-algebra/G-set background.

We now isolate four canonically generated structural quotients of the inherited rooted geometry.

### Definition 10.1. Orbit quotient

Two events are orbit-equivalent if the unordered pair of radial contraction-history types is the same. In coordinate representation:

\[
(i,j)\sim_{\rm orb}(k,l)
\iff
\{i,j\}=\{k,l\}.
\tag{10.4}
\]

### Definition 10.2. Span quotient

Join the two rooted contraction histories through the root and retain only total bridge-path size. In coordinates this has the representation

\[
\operatorname{span}(i,j)=i+j.
\tag{10.5}
\]

### Definition 10.3. Gap quotient

Synchronously contract both endpoints toward the root until one reaches the root, forget the surviving branch orientation, and retain only the residual rooted-history type. In coordinates:

\[
\operatorname{gap}(i,j)=|i-j|.
\tag{10.6}
\]

### Definition 10.4. Phase quotient

Retain only the alternating two-phase class of the full cross-root bridge. In coordinates it is represented by

\[
(i+j)\bmod 2.
\tag{10.7}
\]

These coordinate formulas are representations, not primitive definitions of the selector invariants.

---

## 11. The first incomparable pair

### Theorem 11.1. Span-gap incomparability

\[
\boxed{
\theta_{\rm span}\not\subseteq\theta_{\rm gap},
\qquad
\theta_{\rm gap}\not\subseteq\theta_{\rm span}.
}
\tag{11.1}
\]

#### Proof

The events represented by `(1,4)` and `(2,3)` have the same total bridge size `5` but gaps `3` and `1`. Hence they are span-equivalent but not gap-equivalent.

Conversely, `(1,2)` and `(2,3)` both have gap `1`, but total bridge sizes `3` and `5`. Hence they are gap-equivalent but not span-equivalent. \(\square\)

Thus the selector order is not a chain.

### Theorem 11.2. Exact meet

\[
\boxed{
\theta_{\rm span}\wedge\theta_{\rm gap}=\theta_{\rm orb}.
}
\tag{11.2}
\]

#### Proof

If two events have equal span `s` and equal gap `d`, then their two radial lengths are the unordered pair

\[
\left\{\frac{s+d}{2},\frac{s-d}{2}\right\}.
\]

Thus their unordered contraction-history types agree. The converse is immediate. \(\square\)

### Theorem 11.3. Exact join

\[
\boxed{
\theta_{\rm span}\vee\theta_{\rm gap}=\theta_{\rm phase}.
}
\tag{11.3}
\]

#### Proof

Span-equivalence preserves the parity of total bridge length. Gap-equivalence does so as well because

\[
i+j\equiv i-j\equiv|i-j|\pmod2.
\]

Hence the generated join is contained in phase-equivalence.

For even span, every event is span-equivalent to a symmetric bridge `(n,n)`, and all symmetric bridges are gap-equivalent because their residual gap is zero. Thus all even-phase events lie in one generated class.

For odd span, every event is span-equivalent to some `(n,n+1)`, and all such events are gap-equivalent because their residual gap is one. Thus all odd-phase events lie in one generated class. Even and odd classes cannot merge because both generating relations preserve phase. \(\square\)

Therefore `F_mix -> B0` contains a genuine internal diamond-like interval with incomparable middle quotients.

---

## 12. Event-to-core anchoring

Pure event quotients identify fresh events only with fresh events. We now allow an event class to be identified with an old core point while still requiring distinct old core points to remain inequivalent.

At the one-step terminal-event level, an anchored kernel is therefore a reflection-stable equivalence relation on

\[
C_0\sqcup E
\tag{12.1}
\]

whose restriction to `C_0` is equality and which satisfies weak partial-operation compatibility.

### Proposition 12.1. Reflection constraint on anchors

If an event block `C` is anchored at a core point `a`, then its reflected block `nu C` must be anchored at `nu a`.

#### Proof

If `e in C` and `e ~ a`, reflection stability gives `nu e ~ nu a`. \(\square\)

### Corollary 12.2. Uniqueness of the `B0` base-line anchor

The unique event block of `B0` is reflection-fixed. On the signed base line the unique reflection-fixed point is `P_0`. Hence

\[
\boxed{BR\text{ is the unique reflection-compatible base-line anchor of }B0.}
\tag{12.2}
\]

This is stronger than the mere existence of `B0 -> BR`.

---

## 13. Missing joins after anchoring

The pure event quotient spectrum lies in a complete congruence lattice. The core-anchored admissible quotient spectrum need not.

### Theorem 13.1. Incompatible-anchor obstruction

Let the same event `e` be anchored to distinct old core points `a` and `b` in two individually admissible quotients. Then those two anchored kernels have no common admissible upper bound.

#### Proof

Any equivalence relation containing both kernels contains

\[
a\sim e\sim b,
\]

and therefore `a ~ b`. This violates the requirement that the old core remain pointwise separated. \(\square\)

Consequently the selector geometry undergoes a qualitative transition:

\[
\boxed{
\text{pure invariant-partition lattice}
\longrightarrow
\text{core-anchored quotient poset with possible missing joins}.
}
\tag{13.1}
\]

This is the main order-theoretic obstruction of the first selector layer.

---

## 14. Where the `B0/BR` bifurcation actually comes from

In the weak selector category the arrow

\[
B0\to BR
\]

exists. It is destroyed by stronger axioms.

First, if externality is represented by a primitive output sort or predicate and morphisms preserve it, then `E_cross` cannot map to the old base point `P_0`.

Second, if morphisms strongly reflect definedness, then identifying a terminal event with an operation-active core state generally fails because the target has operations defined at the image that are not reflected back to the source event.

Thus output typing and strong definedness reflection are not neutral background assumptions. They are explicit bifurcation axioms.

---

## 15. Information order versus numerical cost

The existence of incomparable quotients shows why a single scalar cost is premature. The factorization order already records structural information that a scalar would erase.

Possible later invariants include height, coheight, meet/join profile, number of reflection-fixed event blocks, anchorability, and an incompatibility graph of possible core anchors. A Pareto vector may become useful only after this intrinsic order-theoretic structure is exhausted.

At the first layer, no numerical selector is required.

---

## 16. Discussion

The selector problem began with an apparent choice between two natural mixed completions: one that creates a cross-event and one that returns immediately to the root. In the weak category these are not disconnected alternatives. They are related by a quotient map. The true structure is finer.

There are at least five distinct information losses:

\[
\text{optional interaction}
\to
\text{ordered event identity}
\to
\text{unoriented event identity}
\to
\text{relation-only event}
\to
\text{root anchoring}.
\tag{16.1}
\]

The first three are controlled by free objects and event partitions. The fourth produces `B0`. The fifth leaves the pure event world and interacts with the protected old core. That final step is precisely where lattice completeness can fail.

The span-gap diamond shows that the region between full event memory and relation-only collapse is already non-linear. Therefore a selector should not be expected to return a unique completion unless further criteria are introduced and justified independently of the preferred target.

---

## 17. Conclusion

We have constructed a minimal category of reflected mixed extensions that deliberately avoids preserving likely hidden selectors. Two structural corrections are essential: optional mixed domains force `M_0` to be initial in the broad category, and ordered mixed events must precede mixed commutativity.

The resulting universal ladder is

\[
\boxed{
M_0\to F_{\to}\to F_{\rm mix}\to B0\to BR.
}
\tag{17.1}
\]

Within `F_mix`, canonically generated span and gap quotients are incomparable and satisfy

\[
\boxed{
\theta_{\rm span}\wedge\theta_{\rm gap}=\theta_{\rm orb},
\qquad
\theta_{\rm span}\vee\theta_{\rm gap}=\theta_{\rm phase}.
}
\tag{17.2}
\]

Pure event quotients live inside a classical invariant-partition lattice, but core anchoring produces a constrained quotient poset in which joins can fail. The relation-only event admits exactly one reflection-compatible base-line anchor, the root-return quotient `BR`. The weak arrow `B0 -> BR` disappears only after additional output-typing or strong definedness axioms are imposed.

The next natural level is re-entry. Once mixed outputs themselves become operation inputs, one-step free events are replaced by genuine term-tree closure, and the present quotient geometry must be reconstructed at a higher syntactic depth.

---

## References

1. Hoefnagel, M.; Jacqmin, P.-A. *Partial Algebras and Implications of (Weak) Matrix Properties*. Applied Categorical Structures **32** (2024), Article 34. DOI: 10.1007/s10485-024-09790-z.
2. Vernikov, B. M. *On congruences of G-sets*. Commentationes Mathematicae Universitatis Carolinae **38** (1997), no. 3, 603--613.
3. Seif, S. *Congruence lattices of intransitive G-Sets and flat M-Sets*. Commentationes Mathematicae Universitatis Carolinae **54** (2013), no. 4, 459--484.
4. Burmeister, P. *A Model Theoretic Oriented Approach to Partial Algebras*. Akademie-Verlag, Berlin, 1986.

---

## Research provenance

This article was assembled from the `SOL-SELECTOR` research line in the repository `Riemann-Hypothesis-Commander-Sol`, based on the theorem packages `CATEGORY_CLOSURE_AUDIT_0_1.md`, `QUOTIENT_POSET_0_1.md`, `INTRINSIC_DEFINABILITY_AUDIT_0_1.md`, `HOSTILE_AUDIT_0_1.md`, and `PRIOR_ART_NOVELTY_AUDIT_0_1.md`.
