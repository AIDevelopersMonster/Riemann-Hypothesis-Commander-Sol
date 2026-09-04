# SOL-SELECTOR — Prior-Art and Novelty Audit 0.1

**Branch:** `director/fcoa-selector`  
**Date:** 2026-09-04  
**Status:** PASS FOR ARTICLE ASSEMBLY / NOVELTY CLAIM NARROWED

---

## 0. Verdict

The literature check does **not** support claiming novelty for the background machinery:

- preservation-only homomorphisms of partial algebras;
- weak/strong variants of partial-algebra morphisms and congruences;
- quotient partial algebras;
- free completions/free partial structures;
- congruence lattices of G-sets / unary algebras;
- complete lattices of equivalence relations or invariant partitions;
- relative congruence lattices and congruence-extension phenomena.

These are established areas.

However, no located source reproduces the specific combined `SOL-SELECTOR` architecture:

```math
M_0\to F_{\to}\to F_{\mathrm{mix}}\to B0\to BR,
```

with the following FCOA-specific interpretation of the successive losses:

1. optional mixed-domain completion;
2. ordered-event free completion;
3. quotient by argument-orientation forgetting;
4. quotient to one relation-only event;
5. weak event-to-fixed-core anchoring;
6. disappearance of joins after incompatible anchors;
7. canonically generated span/gap incomparable quotients and their exact meet/join profile inside the mixed-event sector.

Therefore the branch passes the novelty gate **only as a combined construction/result package**, not as a claim that its individual categorical ingredients are new.

---

## 1. Partial-algebra morphisms are prior art

Hoefnagel–Jacqmin (Applied Categorical Structures, 2024) explicitly use the preservation-only convention for partial-algebra homomorphisms: whenever a source operation is defined, the corresponding target operation must be defined and the value preserved.

This directly confirms that the first-layer SOL-SELECTOR morphism convention is standard background mathematics.

The article must therefore say that SOL-SELECTOR **adopts** an explicit preservation-only convention; it must not present that convention as new.

Reference:

- M. Hoefnagel, P.-A. Jacqmin, *Partial Algebras and Implications of (Weak) Matrix Properties*, Applied Categorical Structures 32 (2024), Article 34, DOI `10.1007/s10485-024-09790-z`.

---

## 2. Quotients and weak congruence behavior are prior art

Classical partial-algebra literature distinguishes stronger and weaker congruence/homomorphism notions according to whether definedness itself must be invariant/reflected.

A standard quotient construction defines an operation on equivalence classes whenever a defined representative tuple exists, provided outputs from any two defined equivalent representative tuples are equivalent.

Thus the logical possibility exploited by

```math
B0\to BR
```

— namely that a quotient may acquire extra definedness after identifying a terminal event with an operation-active core state — belongs to the weak partial-algebra quotient regime and should not be claimed as a newly invented quotient notion.

The novelty question is instead what this weak quotient does inside the fixed-core FCOA selector architecture.

Background sources include the Burmeister tradition on partial algebras and subsequent treatments of quotient partial algebras.

---

## 3. Free completions and free partial structures are prior art

The literature contains universal free-completion constructions for partial algebras: undefined operations may be represented syntactically, and maps out of the original partial algebra uniquely extend to maps from the free completion under the relevant hypotheses.

Likewise, free partial structures are classically defined through the expected universal mapping property.

Therefore neither

```math
F_{\to}
```

nor the general idea “one formal generator per not-yet-identified operation event” should be advertised as a new concept in universal algebra.

What is specific to SOL-SELECTOR is the exact staged placement of these free objects between the fixed inherited `M0` and progressively more forgetful mixed completions.

---

## 4. G-set congruence lattices are prior art

After mixed commutativity, the terminal event set carries only the involution induced by zero reflection. Abstractly, this is a unary algebra / `C2`-set.

Congruences of G-sets and their lattices have a substantial literature, including:

- B. M. Vernikov, *On congruences of G-sets*, Comment. Math. Univ. Carolinae 38 (1997), 603–613;
- S. Seif, *Congruence lattices of intransitive G-Sets and flat M-Sets*, Comment. Math. Univ. Carolinae 54 (2013), 459–484.

Accordingly, the theorem that pure reflection-stable event equivalences form a complete lattice is infrastructure, not novelty.

---

## 5. Relative congruence theory is prior art

Universal algebra already studies relative congruence lattices and congruence extension properties for subalgebras/quasivarieties.

This is relevant because SOL-SELECTOR fixes an inherited core and allows congruences only if they do not collapse distinct core points.

The prior-art lesson is important:

```math
\text{“congruences constrained by a distinguished substructure”}
```

is not itself new.

However, ordinary relative congruence theory is not the same theorem as the selector's event-core anchoring obstruction. The selector imposes pointwise core separation while simultaneously allowing terminal mixed-event classes to attach to specific core points under weak partiality. The resulting failure of joins is a concrete structural phenomenon of that admissible quotient class, not merely a restatement of the congruence extension property.

---

## 6. Closest structural comparison and distinction

The closest abstract backgrounds found are:

1. free completion/reflection of partial algebras;
2. weak partial quotients;
3. congruence lattices of unary algebras / G-sets;
4. relative congruence lattices with distinguished subalgebras.

None of the located sources packages these into the SOL-SELECTOR progression

```math
\text{domain completion}
\to
\text{orientation forgetting}
\to
\text{relation-only forgetting}
\to
\text{event-core anchoring}
```

for a reflected signed partial algebra while also deriving a non-chain span/gap subgeometry and a no-join anchoring region.

This absence is not a proof that no prior paper exists anywhere; it is a literature-search result sufficient to justify a cautious novelty formulation.

---

## 7. Novelty claims that are NOT allowed

The article must not claim any of the following as new:

1. weak homomorphisms of partial algebras;
2. weak congruences or existentially defined quotient operations;
3. free completion of a partial algebra;
4. the universal-property definition of a free partial structure;
5. congruence lattices of `C2`-sets/G-sets;
6. the fact that equivalence relations form a complete lattice;
7. relative congruence lattices or congruence extension theory in general.

---

## 8. Defensible SOL-SELECTOR contribution

Subject to the existing theorem-scope restrictions, the article may present as its main contribution the following combined package.

### Contribution A — staged universal selector ladder

For the fixed signed FCOA core and weak core-fixed morphisms:

```math
\boxed{
M_0\to F_{\to}\to F_{\mathrm{mix}}\to B0\to BR.
}
```

Each arrow corresponds to a distinct, explicitly identified loss of mixed-interaction information.

### Contribution B — free-object correction

The unbiased full mixed completion is indexed by **ordered** mixed cells; mixed commutativity appears only after the transposition quotient.

This prevents commutativity from being silently inserted into the free object.

### Contribution C — FCOA-generated incomparable quotients

The canonically generated span and gap invariants yield incomparable quotient kernels:

```math
\theta_{span}\parallel\theta_{gap}.
```

Their exact profile is

```math
\theta_{span}\wedge\theta_{gap}=\theta_{orb},
```

```math
\theta_{span}\vee\theta_{gap}=\theta_{phase}.
```

The coordinate formulas `i+j`, `|i-j|`, and parity are representations of these structural invariants, not primitive selector definitions.

### Contribution D — transition from lattice to non-lattice behavior

Pure terminal-event quotients live inside the classical invariant-equivalence lattice, but once admissible event-to-core anchors are allowed while distinct core points must remain separated, incompatible anchors may have no common admissible upper bound.

Thus the selector space exhibits a concrete transition

```math
\boxed{
\text{pure invariant-partition lattice}
\to
\text{core-anchored quotient poset with possible missing joins}.
}
```

### Contribution E — uniqueness of `BR`

Because the unique `B0` event class is reflection-fixed and the signed base line has a unique reflection-fixed base point, `BR` is the unique reflection-compatible **base-line** anchoring of `B0`.

### Contribution F — exact weak/strong bifurcation

The morphism

```math
B0\to BR
```

survives in the weak preservation-only category but is destroyed by output-sort preservation or sufficiently strong reflection of definedness.

This locates precisely which additional axioms create the `B0/BR` bifurcation.

---

## 9. Required publication wording

Recommended strength:

> We do not claim novelty for weak partial-algebra homomorphisms, free completions, quotient constructions, or congruence lattices of group actions. The contribution is the FCOA-specific selector architecture obtained by combining these standard tools with a fixed reflected core, staged mixed-event forgetting, canonically generated incomparable radial quotients, and constrained event-to-core anchoring.

Avoid:

> We introduce a new theory of congruences of partial algebras.

Avoid:

> We discover that invariant equivalence relations form a lattice.

Avoid:

> Span and gap are first-order definable in the weakest infinite reduct.

The last statement remains unproved.

---

## 10. Publication gate

### Mathematical theorem audit

PASS with the two scope corrections already recorded in `HOSTILE_AUDIT_0_1.md`.

### Prior-art gate

PASS for a **carefully scoped article**.

No searched source collapses the full theorem nucleus into an already-known named construction.

### Remaining tasks before release

1. write the article around the combined novelty package rather than around background category theory;
2. include explicit references to partial-algebra homomorphisms/free completions and G-set congruence theory;
3. state the weak/strong scope at the first definition;
4. keep structural-generation claims separate from FO definability claims;
5. run the normal prepublication numbering/bibliography/metadata audit on RU and EN versions.

---

## 11. Decision

```math
\boxed{
\text{SOL-SELECTOR HAS CROSSED THE ARTICLE-ASSEMBLY THRESHOLD.}
}
```

The research branch should now move from theorem discovery to article construction unless a later bibliographic search produces a direct prior-art collision with the combined selector architecture.
