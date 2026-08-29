# FCOA Morphisms, Equivalence and Representation 1.0

**Status:** normative working backend companion to `FCOA_DEFINITION_1_0.md`  
**Purpose:** fix the comparison language used when FCOA presentations are transformed, compiled, interpreted, compressed, or compared by resource cost  
**Scope:** typed partial algebras, their relationalizations, finite families, and uniform first-order interpretations  
**Rule:** frontier results must state which notion from this document is being used before any claim of “same structure”, “same memory”, “same phase”, or “cheaper representation” is accepted

---

## 1. Why this document is necessary

The FCOA programme now uses several transformations:

- erasing the external orientation;
- compiling a relation into a partial-operation domain;
- splitting or merging output fibers;
- replacing operation graphs by incidence structures;
- using auxiliary carriers;
- representing an `N`-element target by tuples over a smaller carrier;
- moving between finite truncations and uniformly generated families;
- recovering order, addition, or multiplication by first-order formulas.

These transformations do not preserve all mathematical features in the same sense.

Therefore the phrase

\[
\text{“the same FCOA”}
\]

is forbidden unless the equivalence level is specified.

---

## 2. Objects under comparison

An individual FCOA structure is denoted

\[
\mathfrak F.
\]

A uniformly generated finite family is denoted

\[
\mathcal F=(\mathfrak F_N)_{N\in I}.
\]

A presentation is a concrete signature together with its carriers, partial-operation graphs, output sorts, and any explicitly retained generator relations.

A semantic target is a relation or benchmark structure intended to be recovered, for example:

\[
<,
\qquad
\operatorname{Succ},
\qquad
\operatorname{EqGap},
\qquad
\operatorname{Add},
\qquad
\operatorname{Mul}.
\]

Resource comparison is always comparison of **presentations of a declared semantic target**, not comparison of abstract symbols alone.

---

## 3. Strict typed homomorphism

Let

\[
h:\mathfrak F\to\mathfrak G
\]

be sort-preserving.

It is a **strict typed homomorphism** if for every primitive partial operation \(\omega\), whenever

\[
\omega^{\mathfrak F}(x_1,\ldots,x_k)=y
\]

is defined, then

\[
\omega^{\mathfrak G}(h(x_1),\ldots,h(x_k))=h(y)
\]

is defined.

A homomorphism preserves existing operation facts but need not reflect undefinedness.

This is the default algebraic morphism from `FCOA_DEFINITION_1_0.md`.

---

## 4. Strong embedding

A strict typed homomorphism \(h\) is a **strong embedding** if it is injective and, for tuples from its image, both definedness and operation values are reflected:

\[
\omega^{\mathfrak G}(h(\bar x))\text{ defined}
\iff
\omega^{\mathfrak F}(\bar x)\text{ defined},
\]

and when defined the values correspond by \(h\).

Thus a strong embedding preserves the exact partial-operation table on the embedded substructure.

---

## 5. Isomorphism

An **FCOA isomorphism** is a bijective strong embedding preserving all declared sorts and primitive symbols.

Write

\[
\mathfrak F\cong\mathfrak G.
\]

This is the strongest routine notion of “same FCOA structure”.

If the explicit orientation is retained, isomorphism must preserve it. If the carrier-erased reduct is under study, the orientation is not part of the signature and is not required to be preserved.

Therefore

\[
\mathfrak F^{\rm or}\cong\mathfrak G^{\rm or}
\]

and

\[
\mathfrak F^\circ\cong\mathfrak G^\circ
\]

are different claims.

---

## 6. Definitional equivalence

Two relationalized presentations are **definitionally equivalent** when each primitive relation/function graph of one is uniformly first-order definable in the other on the same underlying interpreted universe, without quotienting and without an unbounded auxiliary construction.

Typical examples:

- a partial operation and its exact graph relation;
- definedness and an operation graph;
- a fixed incidence expansion in which all added roles are uniformly definable and eliminable.

Definitional equivalence is weaker than literal isomorphism of signatures but stronger than arbitrary FO interpretability.

Notation:

\[
\mathfrak F\equiv_{\rm def}\mathfrak G.
\]

When resource counts differ under definitional expansion, both the raw and normalized costs must be stated.

---

## 7. Uniform FO interpretation

For families

\[
\mathcal A=(\mathfrak A_N),
\qquad
\mathcal B=(\mathfrak B_N),
\]

write

\[
\mathcal A\le_{FO}\mathcal B
\]

when one fixed parameter-free first-order interpretation uniformly recovers \(\mathfrak A_N\) from \(\mathfrak B_N\) for every relevant \(N\).

The interpretation must declare:

1. its dimension \(d\);
2. domain formula;
3. equivalence/quotient formula if used;
4. formulas for every recovered primitive symbol;
5. treatment of sorts;
6. whether the interpretation is size-faithful;
7. whether auxiliary elements outside the interpreted target remain present.

### Interpretation dimension

If target elements are represented by \(d\)-tuples, the interpretation has dimension

\[
\dim(I)=d.
\]

This dimension is a resource parameter and must be charged in compression comparisons.

---

## 8. FO bi-interpretability / mutual interpretability

If

\[
\mathcal A\le_{FO}\mathcal B
\]

and

\[
\mathcal B\le_{FO}\mathcal A,
\]

then the families are **mutually FO interpretable**.

Write provisionally

\[
\mathcal A\equiv_{FO}\mathcal B.
\]

This notation records semantic mutual recoverability only. It does **not** assert literal categorical bi-interpretability with definable natural isomorphisms unless those extra coherence conditions are explicitly proved.

This firewall prevents the programme from using the technical term “bi-interpretability” too strongly.

---

## 9. Recovered-target equivalence

For a fixed target family \(T_N\), two FCOA families may be equivalent only with respect to that target.

Write

\[
\mathcal F\equiv_T\mathcal G
\]

when both uniformly recover the same canonical target \(T_N\) under the declared identification.

Examples:

\[
\equiv_{<},
\qquad
\equiv_{\operatorname{Add}},
\qquad
\equiv_{\operatorname{Mul}}.
\]

This is much weaker than mutual FO interpretation.

Two structures may both define addition while one also defines multiplication and the other does not.

Therefore

\[
\mathcal F\equiv_{\operatorname{Add}}\mathcal G
\]

does not imply equal arithmetic leakage.

---

## 10. Semantic phase equivalence

The FCOA Arithmetic-Leakage programme compares families by the strongest benchmark uniformly FO interpretable in them.

Use the benchmark ladder

\[
\mathsf B_0=([N],<),
\]

\[
\mathsf B_1=([N],<,+_{tr}),
\]

\[
\mathsf B_2=([N],<,+_{tr},\times_{tr}).
\]

Define the semantic transport rank

\[
\operatorname{FTR}(\mathcal F)
=
\max\{j\in\{0,1,2\}:\mathsf B_j\le_{FO}\mathcal F\}.
\]

Two families are **phase-equivalent** when they have the same FTR value:

\[
\mathcal F\equiv_{\rm phase}\mathcal G.
\]

Phase-equivalence does not imply equal resource cost or mutual interpretability.

This is the correct formal home for statements such as “both structures are AL1”.

---

## 11. Presentation equivalence versus semantic equivalence

The hierarchy of notions is intentionally non-collapsing:

\[
\boxed{
\text{isomorphism}
\Rightarrow
\text{definitional equivalence}
\Rightarrow
\text{mutual FO interpretability}
}
\]

while

\[
\boxed{
\text{same recovered target}
}
\]

and

\[
\boxed{
\text{same semantic phase}
}
\]

are weaker comparison relations and need not imply any of the stronger ones.

Resource-minimality statements must never move between these levels without proof.

---

## 12. Carrier-preserving transformations

A transformation is **carrier-preserving** when the active carrier sort is unchanged pointwise or by a declared canonical bijection and no growing auxiliary carrier is introduced.

Examples:

- adding a definable relation;
- relationalizing a partial operation;
- splitting a bounded terminal output fiber;
- compiling a relation into domain placement on the same carrier.

Carrier-preserving transformations are the default class for one-dimensional base-sorted resource comparisons.

---

## 13. Auxiliary-carrier transformations

A transformation is **auxiliary-carrier** when it introduces a growing sort \(A_N\) whose size depends on \(N\).

Examples:

- residue carriers in CRT representations;
- digit carriers of size \(\Theta(\sqrt N)\);
- configuration/pair sorts;
- explicit history-object sorts.

The cost vector must record at least

\[
|A_N|,
\]

all incidences linking \(A_N\) to the base carrier, and the primitive tables defined on \(A_N\).

A small base-sort trace does not imply a cheap representation if the auxiliary sort carries the missing information.

---

## 14. Size-faithful representations

A representation of an \(N\)-element target is **size-faithful** when its total active information-bearing universe is \(O(N)\), counting all growing auxiliary sorts.

This is a coarse notion only. It does not identify where the information is stored.

For sharper comparisons use the full cost vector from Section 17.

---

## 15. Dimension-1 and dimension-d representations

### Dimension 1

A representation is **dimension-1** when each target base element is represented by one element of the source structure, modulo at most a uniformly bounded finite fiber/quotient.

Dimension-1 forbids tuple-power digitization as a way to create \(N\) target elements from a \(\sqrt N\)-scale carrier.

### Dimension d

A representation is **dimension-d** when target elements are represented by fixed \(d\)-tuples over source sorts.

The distinction

\[
1\quad\text{versus}\quad2
\]

is now a central resource boundary in the additive-compression programme.

No theorem may call an \(O(N)\) dimension-2 encoding a counterexample to a lower bound proved only for dimension-1/base-sorted presentations.

---

## 16. Bounded-fiber interpretation

An interpretation has **bounded fiber** when every interpreted target element has at most \(C\) representatives for one constant \(C\) independent of \(N\).

Bounded-fiber dimension-1 interpretations are a preferred candidate equivalence class for intrinsic carrier-level resource comparisons because they prevent arbitrary polynomial blow-up by tuple coding while allowing harmless local recodings.

Status:

\[
\mathbf W
\]

as the likely frontier normalization; not yet a universal FCOA axiom.

---

## 17. Resource vector

Every frontier construction intended for comparison should report a resource vector of the form

\[
\mathcal C_N=
(
S_N,
A_N,
Q_N,
d,
k,
\alpha,
\eta,
\lambda
),
\]

where, at minimum:

- \(S_N\): primitive support / operation-cell count;
- \(A_N\): total auxiliary-carrier size;
- \(Q_N\): incidence/coordinate-map support linking carriers;
- \(d\): interpretation dimension;
- \(k\): number of growing coordinate/channel sorts;
- \(\alpha\): output alphabet growth class;
- \(\eta\): generator/provenance class;
- \(\lambda\): semantic leakage level / FTR.

Additional fields such as anchors, maximum arity, nesting depth, closure mechanism, state complexity, or degree may be appended when relevant.

Raw cell count is never a complete resource invariant.

---

## 18. Provenance classes

A representation comparison must declare how its primitive tables were generated.

At minimum distinguish:

1. **U0 / definitional:** uniformly FO-definable from the current base structure;
2. **finite-state/local generated:** fixed finite control with prefix-consistent local propagation;
3. **closure-generated:** uses unbounded reachability, recursion, least-fixed-point, or equivalent traversal;
4. **explicit numerical scaffold:** imports declared external arithmetic functions/moduli;
5. **varied size-dependent scaffold:** depends on final \(N\) through parameters such as changing moduli;
6. **arbitrary size oracle:** forbidden in minimality claims unless explicitly being studied as a negative benchmark.

Two equal-size representations from different provenance classes are not automatically comparable as equal-cost mechanisms.

---

## 19. Cost-preserving recodings

A recoding may be declared **cost-preserving up to constants** if:

- it is a fixed definitional/incidence compilation;
- each source record creates at most \(C\) target records;
- each target record has at most \(C\) source witnesses;
- only \(O(1)\) new role markers/singletons are introduced;
- interpretation dimension does not increase unless explicitly charged.

Then

\[
S_N=\Theta(T_N)
\]

may be transferred between the two presentations.

This is the normal justification for replacing a relation by a fixed partial-operation incidence gadget.

---

## 20. Non-cost-preserving recodings

The following transformations are not automatically cost-preserving:

- dimension increase;
- Cartesian-product reification;
- introducing a growing digit/residue sort;
- recursively materializing closure/history;
- adding a lookup table whose size is asymptotically larger than the original primitive support;
- using an interpretation with growing fibers;
- changing from an unvaried to a size-dependent scaffold.

Any such transformation starts a new resource profile even if it preserves the recovered arithmetic relation.

---

## 21. Canonical comparison protocol

Before claiming that construction \(A\) is cheaper/stronger/weaker than construction \(B\), record:

1. **semantic target:** what must be recovered?;
2. **logical mode:** FO definability, computable recovery, TC/LFP, or another logic?;
3. **presentation class:** base-sorted, typed multi-sorted, auxiliary-carrier?;
4. **interpretation dimension:** 1, 2, ...?;
5. **fiber bound:** bounded or growing?;
6. **provenance:** U0/local/closure/numerical/varied/oracular?;
7. **resource vector:** support, auxiliary size, maps, outputs, arity, anchors;
8. **equivalence notion:** isomorphism, definitional, FO mutual, target-equivalent, or phase-equivalent?;
9. **uniformity:** one fixed construction/formula across all \(N\)?;
10. **erasure:** which external symbols are removed before testing recoverability?

If any of these is omitted, the comparison is provisional.

---

## 22. Application to the current additive-compression frontier

The current central comparison is now normalized as follows.

### Base-sorted unvaried Presburger representation

- target: truncated addition;
- active carrier size: \(N\);
- dimension: 1;
- no growing auxiliary sort;
- primitives: fixed unvaried Presburger relations;
- exact lower bound: \(\Theta(N^2)\) primitive support in the declared model.

### Digit representation

- target: truncated addition;
- target base size: \(N\);
- digit sort size: \(\Theta(\sqrt N)\);
- interpretation dimension: 2;
- coordinate maps: \(\Theta(N)\);
- digit addition table: \(\Theta(N)\);
- total representation cost: \(\Theta(N)\) in the declared vector.

These statements are compatible because they belong to different representation classes.

The open frontier question is therefore not “which theorem is wrong?” but:

\[
\boxed{
\text{how far can exact AL1 be compressed under dimension-1 bounded-fiber provenance-safe recodings?}
}
\]

---

## 23. Relation to RTP/FTR

Presentation-level quantities such as direct CRT resolution exponents are **normal-form resource descriptors**, not semantic invariants.

The semantic invariant is the FO interpretability phase, represented here by FTR.

Therefore the canonical architecture is

\[
\boxed{
\text{semantic phase}
+
\text{representation resource vector}.
}
\]

The first is stable under suitable semantic equivalence; the second records how a particular presentation realizes that phase.

---

## 24. Backend discipline

This document is normative backend guidance.

Future frontier files must consult it before stating:

- “same FCOA”;
- “equivalent encoding”;
- “linear cost”;
- “compression”;
- “counterexample to a lower bound”;
- “interpretation-invariant”;
- “minimal representation dimension”.

If a frontier result shows that one of these comparison notions is inadequate, the remedy is an explicit revision `1.1` or later, not an ad hoc redefinition inside the frontier branch.

---

## 25. Fixed / Working / Open ledger

### F — fixed for current comparisons

- isomorphism, strict homomorphism, strong embedding;
- relationalization interface;
- distinction between definitional equivalence, mutual FO interpretation, target-equivalence, and phase-equivalence;
- mandatory declaration of interpretation dimension and auxiliary carriers;
- full resource vector rather than raw cell count;
- no cross-class use of lower bounds without a reduction theorem;
- distinction between semantic phase and representation cost.

### W — working normalization

- bounded-fiber dimension-1 interpretations as the preferred carrier-faithful equivalence class for intrinsic resource lower bounds;
- FTR terminology as semantic transport rank;
- exact minimal fields of the resource vector.

### O — open

- whether bounded-fiber dimension-1 should become the canonical representation equivalence for all intrinsic FCOA complexity;
- whether a category of FCOA presentations with cost-preserving morphisms should be formalized;
- which provenance classes admit robust representation-independent lower bounds;
- whether interpretation dimension itself has a hierarchy theorem for AL0/AL1/AL2;
- whether a universal normal form exists for all linear-cost AL1 presentations.

---

## 26. Short rule

When two FCOA constructions are compared, always ask two separate questions:

\[
\boxed{\text{What semantic structure do they recover?}}
\]

and

\[
\boxed{\text{At what representation cost and under what allowed recoding?}}
\]

The first belongs to the semantic phase. The second belongs to the representation profile. FCOA resource theory must not merge them.