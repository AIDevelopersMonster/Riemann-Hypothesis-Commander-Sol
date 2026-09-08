# Coherent FO-Interpretation Invariance of the DCE Barrier

**Project:** FCOA Admissibility Geometry  
**Date:** 2026-08-30  
**Status:** central theorem checkpoint; proof complete  
**Depends on:** `DECIDABLE_COHERENT_ENVELOPE_PHASE_BARRIER.md`, `HOSTILE_AUDIT_DECIDABLE_COHERENT_ENVELOPE.md`

---

## 1. Target

The first DCE theorem proved invariance under same-base uniform FO definitional recodings.

The next question is whether the phase separator survives genuinely nontrivial first-order interpretations:

- tuples of fixed dimension `d>1`;
- definable interpreted domains;
- definable equivalence relations / quotients;
- definable interpreted primitive relations.

For arbitrary finite-only interpretations the answer cannot be asserted: the interpretation itself may depend on a finite boundary in a way that has no coherent infinite meaning.

The correct invariant class is therefore **coherently liftable FO interpretations**.

---

## 2. FO interpretations

Let `A` be a structure in signature `sigma` and `B` a structure in signature `tau`.

A fixed `d`-dimensional FO interpretation `I` consists of formulas in `sigma` defining:

1. a domain `delta(\bar x)` on `d`-tuples;
2. an equivalence relation `epsilon(\bar x,\bar y)` on the interpreted domain;
3. for each primitive relation `R` of `tau`, an invariant relation formula `rho_R` on interpreted tuples.

The quotient of the definable domain by `epsilon`, equipped with the `rho_R`, is the interpreted structure `I(A)`.

The dimension `d` and all formulas are fixed, independent of prefix size.

---

## 3. Coherently liftable finite-family interpretation

Let

\[
\mathcal A=(A_m)_{m\ge1},
\qquad
\mathcal B=(B_m)_{m\ge1}
\]

be prefix-coherent finite families.

### Definition 3.1 — coherently liftable interpretation (CLI)

A fixed FO interpretation `I` from `A` to `B` is **coherently liftable** for the two families if there exist coherent envelopes

\[
A_\infty,
\qquad
B_\infty
\]

such that:

\[
B_\infty\cong I(A_\infty),
\tag{3.1}
\]

and the finite interpretations agree with the target family under the same coherent identification:

\[
B_m\cong I(A_m)
\tag{3.2}
\]

for every `m`, with old interpreted elements and relations preserved by passage to larger prefixes.

The final coherence clause rules out an interpretation that reassigns the identity of an old quotient class when the ambient prefix grows.

This is a structural condition, not a syntactic restriction to one-dimensional recodings.

---

## 4. Classical interpretation lemma

### Lemma 4.1

If `Th(A)` is decidable and `B` is FO-interpretable in `A` by a fixed effective interpretation, then `Th(B)` is decidable.

### Proof

Every FO sentence `theta` in the language of `B` has an effective pullback `theta^I` in the language of `A`: quantified variables are replaced by interpreted tuples satisfying `delta`, equality is replaced by `epsilon`, and primitive relations by their defining formulas.

Then

\[
B\models\theta
\iff
A\models\theta^I.
\]

A decision procedure for `Th(A)` therefore decides `Th(B)`. `□`

The quotient case is included because interpreted equality is explicitly represented by the definable equivalence relation `epsilon`.

---

## 5. DCE preservation under CLI

### Theorem 5.1 — coherent interpretation invariance

Let `mathcal A` and `mathcal B` be prefix-coherent finite families. If

1. `mathcal A` has DCE;
2. there is a coherently liftable fixed-dimensional FO interpretation from `mathcal A` to `mathcal B`;

then

\[
\boxed{DCE(\mathcal B).}
\tag{5.1}
\]

### Proof

Choose a decidable coherent envelope `A_infty` witnessing `DCE(mathcal A)`.

By coherent liftability, the same fixed interpretation produces a coherent envelope

\[
B_\infty\cong I(A_\infty)
\]

whose finite restrictions are exactly the family `B_m` under the coherent identification.

By Lemma 4.1, `Th(B_infty)` is decidable because it reduces effectively to `Th(A_infty)`.

Thus `B_infty` witnesses `DCE(mathcal B)`. `□`

---

## 6. Bidirectional consequence

If there are coherently liftable FO interpretations in both directions, then

\[
\boxed{
DCE(\mathcal A)\iff DCE(\mathcal B).
}
\tag{6.1}
\]

So DCE is invariant not only under same-base definitional equivalence but under fixed-dimensional coherent FO bi-interpretability, including definable quotient presentations.

This substantially enlarges the representation class under which the equal-cost phase separator is stable.

---

## 7. Arithmetic phase obstruction under interpreted recoding

Combine Theorem 5.1 with the hostile-audited DCE arithmetic barrier:

\[
DCE+Add\Rightarrow\neg Mul.
\]

### Corollary 7.1 — no coherent FO collapse from DCE-AL1 to AL2

Let `mathcal A` be a DCE family. Let `mathcal B` be a prefix-coherent family uniformly defining truncated Add and Mul. Then there is no coherently liftable fixed-dimensional FO interpretation

\[
\mathcal A\to\mathcal B.
\]

### Proof

If such an interpretation existed, Theorem 5.1 would imply `DCE(mathcal B)`. But Add+Mul in a prefix-coherent family implies `not DCE(mathcal B)` by the DCE phase barrier. Contradiction. `□`

Thus

\[
\boxed{
DCE\text{-}AL1\not\xrightarrow{\ coherent\ FO\ interpretation\ }AL2.
}
\tag{7.1}
\]

---

## 8. Canonical equal-cost application

For the central pair:

\[
\mathcal E^F
=\text{Zeckendorf event history},
\]

\[
\mathcal E^2
=\text{binary/BIT event history},
\]

we have

\[
DCE(\mathcal E^F),
\qquad
\neg DCE(\mathcal E^2),
\]

while both have materialized support

\[
\Theta(m).
\]

Therefore:

### Theorem 8.1 — equal-cost non-collapse

There is no coherently liftable fixed-dimensional FO interpretation, even with a definable quotient, from the Zeckendorf event family to the binary/BIT event family:

\[
\boxed{
\mathcal E^F
\not\xrightarrow{\ coherent\ FO\ interp.\ }
\mathcal E^2.
}
\tag{8.1}
\]

This is the first rigorous answer in the central line to the concern that an “exotic recoding” might collapse the AL1/AL2 distinction at equal materialized cost.

---

## 9. Why the coherence hypothesis is essential

A finite-family interpretation can inspect or exploit the ambient finite boundary through formulas whose quotient classes or chosen representatives rearrange as `m` grows.

Such a construction need not be the restriction of any single infinite interpretation. In that situation automatic/decidable-envelope arguments cannot simply be transported to the target family.

Therefore this note does **not** claim invariance under every imaginable sequence of per-prefix FO interpretations.

It proves invariance under the maximal natural class for which one can point to a single fixed infinite semantic recoding whose finite restrictions are the given constructions.

This distinction is itself aligned with the programme's no-hidden-size-oracle principle.

---

## 10. Strengthened phase resource

The central separator can now be stated at three nested representation levels:

\[
\boxed{
\begin{array}{c}
\text{same-base uniform FO definitional equivalence}\\
\Downarrow\\
\text{coherent fixed-dimensional FO interpretation}\\
\Downarrow\\
\text{coherent FO bi-interpretation / quotient recoding}
\end{array}
}
\]

DCE survives throughout this class.

Consequently the Zeckendorf exact-AL1 phase is not merely an artifact of choosing Fibonacci digit names, event names, or a one-dimensional primitive presentation.

---

## 11. Remaining frontier

The remaining interpretation-invariance question is now sharply delimited.

Can one eliminate or weaken the explicit coherent-lift hypothesis and derive coherence automatically from a natural uniformity condition on the finite interpretations?

Equivalently:

\[
\boxed{
\text{when does a uniform sequence of finite FO interpretations admit one coherent infinite lift?}
}
\]

This is now the true obstruction between the current DCE invariant and a fully presentation-independent phase theory.

A second route is to define a stronger invariant directly as the existence of a decidable infinite structure from which the entire prefix family is uniformly FO-interpretable with coherent decoding.

Either route would move the programme from a robust separator to a general interpretation-invariant resource theory.
