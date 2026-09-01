# SOL-SELECTOR — Hostile Audit 0.1

**Branch:** `director/fcoa-selector`  
**Date:** 2026-09-01  
**Status:** PASS WITH TWO CLAIM-NARROWING CORRECTIONS

---

## 0. Audit target

This audit attempts to break the theorem nucleus established in:

- `CATEGORY_CLOSURE_AUDIT_0_1.md`;
- `QUOTIENT_POSET_0_1.md`;
- `INTRINSIC_DEFINABILITY_AUDIT_0_1.md`.

The hostile targets are:

1. preservation-only morphisms for partial algebras;
2. quotient well-definedness under weak congruence;
3. event-to-core anchoring when the anchor has additional defined operations;
4. complete-lattice claim for pure event quotients;
5. span/gap incomparability and meet/join;
6. the claim that span/gap are intrinsic rather than imported arithmetic;
7. novelty scope.

---

# 1. Morphism notion survives

The selector morphism law is:

```math
f_A(a_1,...,a_n)\downarrow
\Longrightarrow
f_B(h a_1,...,h a_n)\downarrow
```

with preservation of the value whenever the source operation is defined.

No reverse-definedness requirement is imposed.

This is a standard homomorphism convention for partial algebras. Stronger notions additionally reflect definedness.

### Verdict

**PASS.**

The selector category is not based on an ad hoc impossible morphism notion.

### Claim discipline

The paper should say:

> We use the preservation-only homomorphism convention for partial algebras and state it explicitly because terminology varies.

It should not claim that this is the unique standard convention.

---

# 2. Weak quotient construction survives

The selector uses an equivalence `theta` such that whenever equivalent input tuples are **both** in the source domain, their outputs are equivalent.

The quotient operation on classes is defined whenever at least one representative tuple lies in the source domain, and its value is the class of the corresponding source value.

### Hostile attack

Could two different defined representative tuples of the same class tuple produce different quotient values?

### Resolution

No. If both representative tuples are defined and coordinatewise equivalent, weak congruence compatibility forces their outputs to be equivalent. Therefore the quotient value is independent of the chosen defined representative.

### Verdict

**PASS.**

This is a legitimate partial-algebra quotient under a weak/non-closed congruence convention.

---

# 3. Anchoring into an operation-active core does not break the weak quotient

Suppose a terminal fresh event `e` is identified with an old core point `a` that has additional operations defined on it.

The quotient class

```math
[e]=[a]
```

then inherits any operation that is defined on the representative `a`, even though no such operation was defined on the representative `e`.

### Hostile objection

This appears to make the quotient depend on the representative and might invalidate the quotient.

### Resolution

Under the weak quotient convention, quotient **definedness** is existential over representatives. Only equality of values between two simultaneously defined representative tuples is required.

Therefore the quotient may indeed acquire additional definedness after an event-core identification.

The natural quotient map remains a preservation-only homomorphism because every operation defined in the source remains defined after quotienting with the required image value.

### Important limitation

This anchoring is **not** valid under a closed/strong congruence notion that requires definedness to be invariant across equivalent representatives.

Thus `B0 -> BR` is a theorem of the weak selector category, not of every category of partial algebras.

### Verdict

**PASS WITH SCOPE NARROWING.**

The weak/strong bifurcation is real and must be foregrounded.

---

# 4. Protected core holes survive anchoring

A possible failure would occur if anchoring an event to a core point caused a protected old core-core cell to become defined in the quotient.

But every core point remains in a class containing exactly one core point. Therefore a protected core pair `[a],[b]` has no alternative core representatives. Fresh events are output elements, not alternative representatives for the two core **input** coordinates unless one of those core input classes itself has been anchored to an event.

Even in that case the event representative is terminal and contributes no new input-side operation. Hence a protected core-core hole does not become defined merely because an output event is attached to one of its endpoint classes.

### Verdict

**PASS at the one-step terminal-event layer.**

This statement must be re-audited after re-entry is introduced.

---

# 5. Pure event complete-lattice theorem survives mathematically but is not novel

At the `F_mix` one-step layer, fresh event generators have no operation on them except the reflection involution. Pure quotients therefore correspond to reflection-stable equivalence relations on the event set.

Intersections of such equivalences remain reflection-stable. The equivalence closure of their union is also reflection-stable. Hence the pure quotient kernels form a complete lattice.

### Verdict on correctness

**PASS.**

### Verdict on novelty

**FAIL AS A NOVELTY CLAIM.**

Congruence lattices of unary algebras and G-sets are classical objects. The reflection-only event layer is a very small `C2`-set/unary algebra. Its invariant equivalences forming a congruence lattice are therefore background mathematics, not the article's novelty.

### Correction

The article may use the complete-lattice theorem as infrastructure, but the novelty claim must focus on the FCOA-generated subgeometry and on what happens when core anchoring is allowed.

---

# 6. Span/gap incomparability survives

The intrinsic span quotient is defined from total cross-root bridge-history size.

The intrinsic gap quotient is defined from synchronous radial contraction residue.

The witnesses remain valid:

- same span, different gap: histories `(1,4)` and `(2,3)`;
- same gap, different span: histories `(1,2)` and `(2,3)`.

No identification introduced by reflection changes these facts.

### Verdict

**PASS.**

---

# 7. Meet theorem survives

`theta_span ∩ theta_gap` determines both total bridge size and cancellation residue.

For two finite rooted chains attached at a common root, these two data reconstruct the unordered pair of chain lengths. Conversely the unordered pair determines both statistics.

Thus

```math
\boxed{
\theta_{span}\wedge\theta_{gap}=\theta_{orb}.
}
```

### Verdict

**PASS.**

---

# 8. Join theorem survives

Both span-equivalence and gap-equivalence preserve the two-phase parity of the endpoint-to-endpoint bridge.

Every even-phase event is connected in the generated equivalence to a symmetric bridge and all symmetric bridges are gap-equivalent.

Every odd-phase event is connected to a bridge whose two arms differ by one edge and all such bridges are gap-equivalent.

Thus exactly two generated classes remain:

```math
\boxed{
\theta_{span}\vee\theta_{gap}=\theta_{phase}.
}
```

### Verdict

**PASS.**

The proof is combinatorial and remains valid over the infinite event set because every equivalence witness uses only finitely many generating steps.

---

# 9. Intrinsicity claim requires terminological repair

The previous note called span/gap `intrinsic FCOA constructions`.

### Hostile objection

`span` compares cardinalities of finite generated paths, and `gap` uses unbounded finite iteration until termination. Neither is necessarily represented by a primitive operation, a term, or a uniformly first-order definable relation of the weakest reduct.

### Resolution

The mathematical constructions are still canonical and isomorphism-invariant, but the safest terminology is:

```math
\boxed{\text{canonically generated structural invariant}}
```

rather than simply `internal operation` or `FO-definable invariant`.

They are intrinsic in the category/metastructure sense:

- generated from the inherited contraction graph;
- invariant under isomorphism;
- independent of an external signed-coordinate labeling;
- no primitive integer addition/subtraction is used.

They are not yet proved intrinsic in the stronger logical sense of a uniform formula or term.

### Verdict

**PASS WITH CLAIM NARROWING.**

This is the second required correction.

---

# 10. Anchored no-join theorem survives

Take two admissible anchored kernels in which the same event class is attached respectively to distinct old core points `a` and `b`.

Any common upper kernel would contain

```math
a\sim e\sim b,
```

hence `a ~ b`, contradicting pointwise core separation.

Therefore the two anchored quotients have no common admissible upper bound.

### Verdict

**PASS.**

This is genuinely stronger than the pure-event congruence-lattice background: the admissible anchored quotient space is not generally a lattice because the fixed core imposes forbidden identifications.

---

# 11. `BR` uniqueness survives

The unique `B0` event block is reflection-fixed. A reflection-compatible anchor of that block to a base-line point must therefore land at a reflection-fixed base point.

The signed base line has exactly one such point, `P0`.

Hence among base-line anchors:

```math
\boxed{
BR\text{ is the unique reflection-compatible anchoring of }B0.
}
```

### Verdict

**PASS.**

---

# 12. Corrected novelty nucleus

After hostile review, the following should **not** be presented as new by themselves:

1. preservation-only homomorphisms of partial algebras;
2. weak congruence quotients of partial algebras;
3. existence of a congruence lattice for a reflection/C2 event set;
4. generic lattice operations on invariant equivalence relations.

The defensible SOL-SELECTOR novelty nucleus is instead the combined FCOA-specific architecture:

1. the staged universal ladder
   ```math
   M_0\to F_{\to}\to F_{mix}\to B0\to BR;
   ```
2. separation of domain completion, orientation forgetting, relation-only forgetting, and event-core anchoring as distinct categorical losses;
3. canonically generated FCOA span/gap quotients forming an explicit incomparable pair;
4. exact FCOA meet/join profile
   ```math
   orb = span\wedge gap,
   \qquad
   phase = span\vee gap;
   ```
5. transition from a pure-event congruence lattice to a core-anchored admissible quotient poset in which joins can fail;
6. uniqueness of `BR` as the zero-reflection-compatible base anchor of the `B0` relation-only event;
7. explicit demonstration that adding output typing or closed/strong definedness preservation destroys the `B0 -> BR` arrow.

This package is the candidate article contribution.

---

# 13. Final hostile verdict

```math
\boxed{\text{PASS WITH TWO CLAIM-NARROWING CORRECTIONS}.}
```

No counterexample was found to the theorem nucleus at the declared one-step weak-morphism scope.

Required corrections before publication:

1. replace broad `intrinsic` wording by `canonically generated structural invariant` unless a separate FO/term theorem is proved;
2. present the pure complete-lattice result explicitly as classical congruence/G-set infrastructure rather than novelty.

The branch may proceed to formal prior-art/novelty review and article architecture.
