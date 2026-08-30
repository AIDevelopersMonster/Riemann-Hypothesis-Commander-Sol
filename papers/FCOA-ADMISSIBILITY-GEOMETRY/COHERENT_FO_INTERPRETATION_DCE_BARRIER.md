# Coherent FO-Interpretation DCE Barrier

**Project:** FCOA Admissibility Geometry  
**Date:** 2026-08-30  
**Status:** central interpretation theorem candidate  
**Depends on:** `DECIDABLE_COHERENT_ENVELOPE_PHASE_BARRIER.md`, `HOSTILE_AUDIT_DECIDABLE_COHERENT_ENVELOPE.md`  
**Scope:** effective fixed-dimensional FO interpretations, including definable quotients, whose finite interpreted data are prefix-coherent

---

## 1. Problem

The DCE barrier already proves, for same-base coherent families,

\[
\boxed{DCE+Add\Longrightarrow\neg Mul.}
\]

It is also invariant under coherent uniform FO **definitional** equivalence.

The remaining central question is whether an exotic recoding can evade the barrier by using:

- tuples instead of single carrier points;
- a definable quotient;
- a different interpreted carrier;
- nontrivial relation formulas on that carrier.

This note extends the barrier to exactly that setting, provided the interpretation itself respects the generated prefix history.

---

## 2. Effective FO interpretations

Let `sigma` and `tau` be fixed finite relational signatures.

A dimension-`d` FO interpretation scheme `I` of `tau` in `sigma` consists of fixed formulas:

\[
\delta(\bar x)
\]

for the raw interpreted domain, where `|\bar x|=d`;

\[
\varepsilon(\bar x,\bar y)
\]

for an equivalence relation on that domain; and for each `r`-ary symbol `R` of `tau`, a fixed formula

\[
\rho_R(\bar x_1,\ldots,\bar x_r).
\]

The formulas are effective and independent of the finite size.

For each finite `sigma`-structure `A_m`, the usual quotient interpretation is

\[
I(A_m)=D_m/E_m
\]

with relations induced by the `\rho_R` formulas, assuming the standard compatibility conditions.

This includes ordinary definitional expansions as the special case `d=1` and equality quotient.

---

## 3. Why ordinary infinite evaluation is not enough

Even when the finite family `(A_m)` is prefix coherent, a formula such as `\delta(\bar x)` can be boundary-sensitive: its truth on an old tuple may change when evaluated directly in the infinite envelope.

Therefore the correct infinite interpretation is not obtained by naively reusing the finite formulas in `A_\infty`.

As in the DCE hostile audit, every formula must first be relativized to a variable finite boundary and then lifted.

---

## 4. Prefix lifting of interpretation data

Let `\theta(\bar u)` be any formula among `\delta`, `\varepsilon`, or the `\rho_R`.

For a fresh bound variable `q`, let

\[
\theta^{<q}
\]

be the strict-prefix relativization restricting every quantified variable to `<q`.

Define the lifted relation on tuples of natural numbers by

\[
\theta^\uparrow(\bar u)
:\iff
\exists q\left(
\max(\bar u)<q
\land
\theta^{<q}(\bar u)
\right),
\tag{4.1}
\]

where `\max(\bar u)<q` abbreviates that every component of every tuple in `\bar u` is below `q`.

The existential bound is an ordinary FO variable of the infinite envelope, not an external size parameter.

---

## 5. Coherent interpretation schemes

Boundary lifting is correct only if the finite interpreted data themselves are stable.

### Definition 5.1 — raw prefix coherence

An interpretation scheme `I` is **raw prefix coherent** on a prefix-coherent source family `(A_m)` if the following finite relations are prefix coherent on old tuples:

1. the raw interpreted domain `D_m\subseteq[m]^d`;
2. the raw equivalence relation `E_m\subseteq D_m^2`;
3. every raw interpreted relation before quotienting.

Thus if all coordinates of an interpreted tuple already lie below `m`, later source growth never changes whether that tuple is a domain representative, equivalent to another old representative, or related to old representatives.

### Definition 5.2 — coherent quotient realization

Assume additionally that the quotient structures

\[
B_m:=I(A_m)=D_m/E_m
\]

form a coherent directed system under the maps induced by inclusion of old representatives.

We then call `I` a **coherent effective FO interpretation** of the finite family `(B_m)` in `(A_m)`.

This is the exact compatibility condition needed for a generated finite history to have one well-defined interpreted infinite limit.

---

## 6. Interpretation prefix-lift lemma

### Lemma 6.1

Let `(A_m)` have coherent envelope `A_\infty`, and let `I` be raw prefix coherent.

Then the lifted formulas (4.1) define in `A_\infty` exactly the unions

\[
D_\infty=\bigcup_m D_m,
\]

\[
E_\infty=\bigcup_m E_m,
\]

and the corresponding unions of all raw interpreted relations.

### Proof

Apply the prefix-truth lemma separately to each interpretation formula.

If a lifted fact holds, it holds in some finite prefix `A_q`; raw prefix coherence makes it permanent in every later prefix and hence part of the union.

Conversely, any union fact already holds in some finite prefix, and a larger bound `q` witnesses its lifted formula.

Thus each lifted formula defines exactly the coherent infinite union. `□`

---

## 7. Infinite quotient interpretation

Because each finite `E_m` is an equivalence relation and the family is prefix coherent, the union

\[
E_\infty
\]

is an equivalence relation on `D_\infty`.

Compatibility of the finite relation formulas with the quotients also passes to the union.

Hence the lifted formulas define a genuine infinite quotient structure

\[
I^\uparrow(A_\infty):=D_\infty/E_\infty.
\]

If the finite quotient realizations `(B_m)` are coherent, their direct limit is canonically isomorphic to this infinite interpreted quotient.

Write this limit as

\[
B_\infty.
\]

Therefore

\[
\boxed{B_\infty\cong I^\uparrow(A_\infty).}
\tag{7.1}
\]

---

## 8. Decidability transfer through the lifted interpretation

### Lemma 8.1 — effective interpretation transfer

If `Th_FO(A_\infty)` is decidable and `B_\infty` is effectively FO-interpretable in `A_\infty` by the lifted quotient interpretation above, then

\[
\boxed{Th_FO(B_\infty)\text{ is decidable}.}
\tag{8.1}
\]

### Proof

Use the standard effective translation of FO formulas under an interpretation:

- each quantified target variable becomes a `d`-tuple satisfying `\delta^\uparrow`;
- equality becomes `\varepsilon^\uparrow`;
- each target relation is replaced by its lifted defining formula;
- quantifiers are relativized to the interpreted domain.

The interpretation formulas are fixed and effective. Hence any FO sentence of `B_\infty` is effectively translated to an FO sentence of `A_\infty` with the same truth value. Decidability transfers. `□`

No automaticity assumption is needed for this lemma; decidability of the source theory is sufficient.

---

## 9. Main theorem — DCE descends through coherent FO interpretations

### Theorem 9.1 — Coherent FO-Interpretation DCE Preservation

Let `(A_m)` be a prefix-coherent source family with DCE. Let `(B_m)` be coherently effectively FO-interpreted in `(A_m)` by a fixed finite-dimensional interpretation, allowing a definable quotient.

Then `(B_m)` also has DCE.

In symbols,

\[
\boxed{
A\xrightarrow{\;I_{coh}^{FO}\;}B
\quad\land\quad
DCE(A)
\Longrightarrow
DCE(B).
}
\tag{9.1}
\]

### Proof

Choose a decidable coherent envelope `A_\infty` of the source family.

Sections 6 and 7 construct from the finite coherent interpretation an infinite lifted quotient `B_\infty` whose finite coherent stages are exactly the target family.

By Lemma 8.1, `Th_FO(B_\infty)` is decidable.

Hence `B_\infty` is a decidable coherent envelope of `(B_m)`. `□`

---

## 10. AL2 non-interpretability corollary

Combine Theorem 9.1 with the hostile-audited DCE phase barrier.

### Corollary 10.1 — no coherent FO recoding from DCE to AL2

Let `(A_m)` have DCE. Let `(B_m)` be a prefix-coherent family that uniformly defines truncated addition and multiplication.

Then there is no coherent effective FO interpretation of `(B_m)` in `(A_m)`, of any fixed finite dimension, even allowing definable quotienting.

\[
\boxed{
DCE(A)\land AL2(B)
\Longrightarrow
A\not\xrightarrow{I_{coh}^{FO}}B.
}
\tag{10.1}
\]

### Proof

If such an interpretation existed, Theorem 9.1 would imply `DCE(B)`. But the DCE phase barrier gives `AL2(B) -> not DCE(B)`. Contradiction. `□`

This directly blocks a large class of “exotic recodings” of the Zeckendorf event family into a BIT/full-arithmetic family.

---

## 11. Mutual interpretation invariance

### Corollary 11.1

If two prefix-coherent families are connected by coherent effective FO interpretations in both directions, then

\[
\boxed{DCE(A)\iff DCE(B).}
\tag{11.1}
\]

Thus DCE is invariant under coherent FO bi-interpretability in this finite-family sense.

This strictly extends the earlier invariance under same-base definitional equivalence.

---

## 12. Application to the linear event pair

For the Zeckendorf event family

\[
E_F(m)=([m],<,U_F,D_F),
\]

DCE is hostile-audited.

For the binary event family

\[
E_2(m)=([m],<,U_2,D_2),
\]

uniform Add and Mul are available, so `not DCE` is hostile-audited.

Corollary 10.1 now yields

\[
\boxed{
E_F\not\xrightarrow{I_{coh}^{FO}}E_2
}
\tag{12.1}
\]

for every fixed-dimensional prefix-coherent effective FO interpretation, including quotient interpretations.

Therefore the equal-linear-cost phase separator is robust against:

- renaming and definitional recoding;
- fixed tuple encodings;
- fixed-dimensional coordinate changes;
- definable quotienting;
- combinations of the above that commute with finite-prefix growth.

This is substantially closer to an interpretation-invariant phase boundary than the original same-carrier DCE theorem.

---

## 13. What the theorem still does not cover

The coherence hypothesis is essential to the proof.

Not yet covered are recodings where:

- old interpreted representatives can disappear or merge only after future source elements arrive;
- the interpretation of an old tuple depends irreducibly on arbitrarily far future source points;
- the dimension grows with `m`;
- auxiliary domains of uncharged growing complexity are introduced;
- the target finite stages are not the coherent restrictions of one interpreted infinite limit;
- the logic is stronger than FO.

Such recodings do not behave like generated persistent memory and require a separate resource model.

Therefore the correct promoted statement is not “DCE is invariant under all interpretations”, but

\[
\boxed{
\text{DCE is preserved under all fixed-dimensional coherent effective FO interpretations, including quotients.}
}
\]

---

## 14. Programme consequence

The central question has moved again.

The Zeckendorf/BIT distinction can no longer be removed merely by a clever fixed-dimensional FO change of coordinates that respects generated-prefix persistence.

Any successful recoding from the DCE exact-AL1 side to AL2 must spend a genuinely new resource, for example:

- future-sensitive noncoherent interpretation;
- growing interpretation dimension;
- growing auxiliary carrier;
- stronger-than-FO interpretation logic;
- another mechanism that destroys decidable-envelope preservation.

This gives the programme a sharper candidate resource boundary:

\[
\boxed{
\text{coherence + fixed interpretation dimension + FO}
}
\]

is insufficient to cross from DCE/AL1 into AL2.

---

## 15. Status ledger

Fixed conditional on hostile audit:

\[
\boxed{\mathbf T:\ DCE\text{ descends through coherent fixed-dimensional effective FO interpretations}.}
\]

\[
\boxed{\mathbf T:\ DCE\text{ is invariant under coherent FO bi-interpretability}.}
\]

\[
\boxed{\mathbf T:\ \text{no coherent fixed-dimensional FO interpretation maps Zeckendorf events to an AL2 family}.}
\]

Open after this theorem:

\[
\boxed{\mathbf O:\ \text{is growing interpretation dimension the next genuine phase resource?}}
\]

\[
\boxed{\mathbf O:\ \text{can noncoherent future-sensitive recodings be meaningfully costed and bounded?}}
\]
