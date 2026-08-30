# FCOA-Z — Interaction-Induced Laws Hypothesis 0.1

**Branch:** `director/fcoa-z-symmetric-line`  
**Date:** 2026-08-30  
**Status:** CONCEPTUAL PRINCIPLE + PROVED FORMAL REDUCTION / PHYSICAL INTERPRETATION OPEN

---

## 1. Core idea

FCOA-Z suggests reversing the usual algebraic order of explanation.

Instead of declaring first that a binary operation is globally commutative or associative, fix:

1. one carrier;
2. one binary partial operation;
3. one rooted/reflected coordinate geometry;
4. the actual domain and value rules of the operation.

Then ask **where** commutation and association happen.

Thus the operation remains the same operation on the same line. What changes with the participating arguments is the local interaction status.

---

## 2. Global laws as universal saturation

For a total operation with values in a common additive ambient algebra one normally writes the commutator and associator

\[
[x,y]_{\star}=x\star y-y\star x,
\]

\[
[x,y,z]_{\star}=(x\star y)\star z-x\star(y\star z).
\]

Global commutativity means

\[
[x,y]_{\star}=0
\quad\text{for all }x,y,
\]

and global associativity means

\[
[x,y,z]_{\star}=0
\quad\text{for all }x,y,z.
\]

In FCOA the output sorts and partiality make subtraction inappropriate in general, so the correct replacement is a status map.

For ordered pairs define a commutation status

\[
\mathcal C_\star(x,y)
\]

recording whether both directions are defined and equal, defined and unequal, or only one/neither direction is defined.

For triples use the existing FCOA association status

\[
\mathcal A_\star(x,y,z)
\in\{EQ,NEQ,LEFT,RIGHT,NONE\}.
\]

A global algebraic law is therefore a special case in which one status saturates the entire relevant domain.

---

## 3. Sign-sector law spectrum

The signed line gives the intrinsic geometric partition

\[
B^-,\qquad\{P_0\},\qquad B^+.
\]

Without changing the operation symbol, define restrictions of its interaction status by sign word.

For pairs:

\[
\mathcal C_{++},\quad
\mathcal C_{+-},\quad
\mathcal C_{-+},\quad
\mathcal C_{--}.
\]

For nonzero triples:

\[
\mathcal A_{+++},\mathcal A_{++-},\mathcal A_{+-+},\mathcal A_{+--},
\]

\[
\mathcal A_{-++},\mathcal A_{-+-},\mathcal A_{--+},\mathcal A_{---}.
\]

The same operation may therefore be noncommutative/nonassociative on one sector pattern and commutative/associative on another.

No second operation is required.

---

## 4. Interaction-Induced Law Principle

### Proposition 4.1

For a fixed partial operation \(\star\) on a fixed signed carrier, any statement of the form

\[
\mathcal A_\star(x,y,z)=EQ
\]

or

\[
\mathcal C_\star(x,y)=EQ
\]

on a restricted sign sector is a property of the restriction of the **same operation**, not the introduction of a new operation.

### Proof

The operation graph \(T_\star\) is unchanged. Restriction to a subset of the input domain merely selects tuples according to a predicate on their carrier positions. Equality or definedness of the corresponding operation values is then evaluated using the same graph relation. Therefore sector-local commutation/association is a derived property of one operation under a geometric input condition. \(\square\)

---

## 5. Consequence for FCOA-Z

Combined with the Mixed-Sector Localization Theorem, the current architecture has a special form:

- \((++)\) is the legacy interaction sector;
- \((--)\) is forced by reflection;
- \((+-)\) and \((-+)\) are the only new binary base-interaction sectors.

Hence any new algebraic law first discovered in a mixed sector can be interpreted as an **interaction-induced law** rather than an independently postulated global axiom.

For example, a future extension could in principle satisfy

\[
\mathcal C_{++}\ne EQ,
\qquad
\mathcal C_{+-}=EQ,
\]

or

\[
\mathcal A_{+++}\ne EQ,
\qquad
\mathcal A_{+-+}=EQ,
\]

while retaining a single operation \(\star\).

These displayed patterns are research possibilities, not current FCOA-Z theorems.

---

## 6. Relation to known mathematics

This principle is not the first appearance of local rather than global associativity.

Known precedents include:

- nuclei and centers of nonassociative algebras, where selected elements associate/commute with all others;
- alternative algebras, where the associator vanishes on selected repeated-variable patterns although the algebra need not be globally associative;
- partial semigroups/categories, where associativity is imposed only on composable triples;
- graded/super/color algebras, where exchange laws depend on grades;
- Jordan and associative pairs, where meaningful identities are organized by alternating sector patterns.

The distinctive FCOA-Z question is whether such local identities can arise from the **intrinsic reflected geometry of one numerical carrier** while a pre-existing legacy operation remains unchanged on the positive branch.

---

## 7. Physics analogy: geometric commutativity

Quantum field theory supplies a strong conceptual precedent. In local/algebraic QFT, observables associated with spacelike-separated regions commute (or fields satisfy the corresponding graded microcausality condition), while the full observable/operator algebra is not thereby globally commutative.

Thus commutativity can depend on the geometric relation between the participants rather than being a universal property of all pairs.

This is an analogy only. FCOA-Z does not yet model spacetime, causality, quantum observables, or QFT.

The relevant lesson is structural:

\[
\boxed{\text{geometry can determine where an algebraic compatibility law holds}.}
\]

---

## 8. Fundamental-law caution

The mathematical conclusion is stronger than an ordinary global-axiom viewpoint but weaker than a physical claim.

What FCOA-Z can legitimately test is:

\[
\boxed{\text{commutativity/associativity need not be primitive axioms; they can be emergent sector-local regularities}.}
\]

This does **not** by itself prove that physical commutativity or associativity laws are non-fundamental in nature.

A physical interpretation would require a model in which:

1. the carrier/interaction geometry has physical meaning;
2. the operation corresponds to an observable composition/interacting process;
3. the sector-local identities reproduce measured physics;
4. the global theory satisfies the required consistency and causality conditions.

Until then, `emergent law` is a mathematical/programmatic hypothesis.

---

## 9. Deferred origin-generation programme

The present branch treats the zero-symmetric line as already constructed from the rooted ray and its reflection completion.

The separate proposed derivation involving the roles of

\[
0^1
\qquad\text{and}\qquad
0^0
\]

in the emergence/unfolding of the numerical axis is intentionally **not** used here and remains a future foundational programme.

No current theorem depends on that proposed origin mechanism.

---

## 10. Research target

The next decisive test is constructive rather than philosophical:

\[
\boxed{
\text{find one natural mixed-sector generator for the existing }\star
\text{ whose law spectrum differs provably from the same-sign spectrum.}
}
\]

If this can be done without defining the sectors by a hand-written case table and without importing ordinary arithmetic, then FCOA-Z will have exhibited a genuine example of **geometry-induced algebraic law differentiation on one numerical line**.

That is the threshold needed before making a stronger novelty claim.