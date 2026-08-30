# Decidable Coherent Envelope Barrier — Equal-Linear-Cost AL1/AL2 Separator

**Project:** FCOA Admissibility Geometry  
**Date:** 2026-08-30  
**Status:** central theorem checkpoint; proof complete, hostile audit recommended before publication promotion  
**Depends on:** `HOSTILE_AUDIT_ZECKENDORF_EVENT_COMPRESSION.md`, `BINARY_HISTORY_COMPRESSION_AND_OVERSHOOT.md`  
**Scope:** prefix-coherent finite structures on explicit initial segments with ordinary FO queries

---

## 1. Why a new invariant is necessary

The event-compression audit establishes two generated histories with the same materialized support scale:

\[
\Theta(m).
\]

Yet their arithmetic phases differ:

\[
\text{Zeckendorf events}=AL1,
\qquad
\text{binary/BIT events}=AL2.
\]

Therefore neither scalar support nor amortized number of state changes can separate the phases.

The next separator must be semantic.

This note isolates a one-sided but rigorous invariant:

\[
\boxed{
\text{existence of a decidable coherent infinite envelope}
}
\]

and proves that it is incompatible with uniform AL2 once uniform addition is present.

---

## 2. Prefix-coherent families

Let

\[
\mathcal A=(\mathfrak A_m)_{m\ge1}
\]

be a family in one fixed finite relational signature `sigma`, with

\[
\operatorname{dom}(\mathfrak A_m)=[m]=\{0,1,\ldots,m-1\},
\]

and with `<` interpreted as the natural order.

Call the family **prefix-coherent** if for every `m<n`,

\[
\mathfrak A_m
=
\mathfrak A_n\upharpoonright[m].
\tag{2.1}
\]

Thus every primitive fact about an old tuple is permanent once generated.

Both Zeckendorf event history and binary event history are prefix-coherent.

---

## 3. Decidable coherent envelope

### Definition 3.1 — coherent envelope

A structure

\[
\mathfrak A_\infty=(\mathbb N,<,\ldots)
\]

in the same signature is a **coherent envelope** of `mathcal A` if

\[
\boxed{
\mathfrak A_m
=
\mathfrak A_\infty\upharpoonright[m]
\quad\text{for every }m.
}
\tag{3.1}
\]

### Definition 3.2 — DCE property

The family has the **Decidable Coherent Envelope** property, abbreviated `DCE`, if it admits at least one coherent envelope whose first-order theory is decidable.

This is an existence property of the whole prefix family, not a claim that one preferred encoding is canonical.

---

## 4. Boundary relativization

Let `phi(\bar x)` be any FO formula in the finite-family signature.

For a bound variable `q`, define the strict-prefix relativization

\[
\phi^{<q}(\bar x)
\]

by replacing recursively

\[
\exists y\,\psi
\quad\mapsto\quad
\exists y\,(y<q\land\psi^{<q}),
\]

and

\[
\forall y\,\psi
\quad\mapsto\quad
\forall y\,(y<q\to\psi^{<q}).
\]

Free variables are required separately to lie below `q`.

### Lemma 4.1 — prefix truth lemma

If `mathfrak A_infty` is a coherent envelope and every component of `\bar a` is below `q`, then

\[
\boxed{
\mathfrak A_\infty\models\phi^{<q}(\bar a)
\iff
\mathfrak A_q\models\phi(\bar a).
}
\tag{4.1}
\]

### Proof

Induct on the construction of `phi`. Atomic formulas agree because `mathfrak A_q` is the induced substructure on `[q]`. Boolean cases are immediate. Relativized existential and universal quantifiers range over exactly `[q]`. `□`

---

## 5. Prefix-lift theorem

Suppose a prefix-coherent base relation `R(\bar x)` is uniformly defined in every `mathfrak A_m` by one fixed formula `phi_R(\bar x)`.

Define in the infinite envelope

\[
R^\uparrow(\bar x)
:\iff
\exists q\,
\left(
\bigwedge_i x_i<q
\land
\phi_R^{<q}(\bar x)
\right).
\tag{5.1}
\]

### Lemma 5.1 — coherent relation lift

If the intended finite relation itself is prefix-coherent, then `R^uparrow` defines its unique infinite union.

### Proof

If the finite relation holds on tuple `\bar a`, choose any `q` larger than all coordinates and large enough to contain the tuple. Prefix coherence makes its truth stable in every later prefix, and Lemma 4.1 gives (5.1).

Conversely, if (5.1) holds for some `q`, Lemma 4.1 says the finite relation holds in prefix `q`; by prefix coherence this is exactly membership in the infinite union. `□`

The existential choice of `q` is therefore not a hidden size oracle. It is an ordinary first-order quantifier inside the infinite ordered envelope.

---

## 6. Decidable Coherent Envelope Barrier

Let `Add_m(a,b,c)` mean canonical truncated addition:

\[
Add_m(a,b,c)
\iff
a+b=c<m.
\]

Let `Mul_m(a,b,c)` mean canonical truncated multiplication:

\[
Mul_m(a,b,c)
\iff
a\cdot b=c<m.
\]

Both families are prefix-coherent as relations on old tuples.

### Theorem 6.1 — DCE phase barrier

Let `mathcal A=(mathfrak A_m)` be a prefix-coherent family on `[m]` in a fixed finite signature containing `<`. Assume:

1. `mathcal A` has `DCE`;
2. truncated addition is uniformly FO-definable in `mathcal A`.

Then truncated multiplication is **not** uniformly FO-definable in `mathcal A`.

Equivalently,

\[
\boxed{
DCE+AL1\Longrightarrow\neg AL2.
}
\tag{6.1}
\]

### Proof

Let `mathfrak A_infty` be a coherent envelope with decidable FO theory.

By hypothesis there is a fixed finite-prefix formula `phi_Add`. Applying Lemma 5.1 yields an FO definition inside `mathfrak A_infty` of ordinary addition on `N`:

\[
Add_\infty(a,b,c)
\iff a+b=c.
\]

Assume for contradiction that a fixed formula `phi_Mul` uniformly defines every `Mul_m`. Applying the same prefix lift yields an FO definition inside `mathfrak A_infty` of ordinary multiplication:

\[
Mul_\infty(a,b,c)
\iff a\cdot b=c.
\]

Hence the standard structure

\[
(\mathbb N,+,\times)
\]

is first-order interpretable by definitions on the same domain inside `mathfrak A_infty`.

For every arithmetic sentence `theta`, replace `+` and `times` by those fixed definitions. This effectively produces an FO sentence `theta*` in the language of `mathfrak A_infty` such that

\[
(\mathbb N,+,\times)\models\theta
\iff
\mathfrak A_\infty\models\theta^*.
\]

True first-order arithmetic is undecidable. Therefore `Th(mathfrak A_infty)` would be undecidable, contradicting `DCE`.

Thus no uniform finite-prefix definition of multiplication exists. `□`

---

## 7. Immediate AL2 obstruction

### Corollary 7.1

Any prefix-coherent finite family that uniformly defines both truncated addition and truncated multiplication has **no** decidable coherent envelope.

Thus

\[
\boxed{
AL2\Longrightarrow\neg DCE
}
\tag{7.1}
\]

for prefix-coherent AL2 families in this sense.

This is stronger than saying that one natural infinite presentation happens to be undecidable: **no decidable coherent envelope in the same finite signature can exist at all.**

---

## 8. Zeckendorf events satisfy DCE

Let

\[
\mathfrak E_m^F=([m],<,U_F,D_F)
\]

be the hostile-audited Zeckendorf event family.

The full Zeckendorf incidence relation

\[
Z(n,p)
\]

has a standard synchronous finite-automaton presentation when natural numbers are represented canonically in Fibonacci/Zeckendorf numeration:

- canonical representations form a regular language;
- `p` is a digit anchor exactly when its canonical word has one `1`;
- `Z(n,p)` says that the unique `1` position of `p` is also a `1` position of `n`;
- order is automatic in the same numeration system.

The event relations are uniformly FO-definable from `Z` by predecessor comparison. Automatic structures are closed under FO definitions, and every word-automatic structure has decidable FO theory.

Therefore the infinite event structure

\[
\mathfrak E_\infty^F=(\mathbb N,<,U_F,D_F)
\]

is a decidable coherent envelope.

Hence

\[
\boxed{DCE(\mathcal E^F).}
\tag{8.1}
\]

The already established uniform addition plus Theorem 6.1 then supplies an independent structural firewall against uniform multiplication.

This recovers the exact-AL1 conclusion from an envelope property rather than from scalar support.

---

## 9. Binary/BIT events fail DCE

Let

\[
\mathfrak E_m^2=([m],<,U_2,D_2)
\]

be the binary event family obtained by differentially encoding ordinary binary counting.

Latest-event integration uniformly reconstructs BIT. Conversely `U_2,D_2` are uniformly definable from consecutive BIT rows. Hence the event family is uniformly FO-interdefinable with the previously established binary history.

That history uniformly reaches `AL2`: both truncated addition and multiplication are FO-definable.

Corollary 7.1 therefore gives

\[
\boxed{\neg DCE(\mathcal E^2).}
\tag{9.1}
\]

No appeal to an informal claim that “binary looks more arithmetic” is needed.

---

## 10. Equal-linear-cost phase split

Both differential families have exact event counts of the form

\[
2m-2-O(\log m),
\]

hence both use

\[
\Theta(m)
\]

materialized primitive tuples.

But

\[
\boxed{
\begin{array}{c|c|c}
\text{family} & \text{materialized support} & \text{coherent-envelope phase}\\
\hline
\text{Zeckendorf events} & \Theta(m) & DCE\ \text{and exact }AL1\\
\text{binary/BIT events} & \Theta(m) & \neg DCE\ \text{and }AL2
\end{array}
}
\tag{10.1}
\]

This is the first rigorous equal-linear-cost semantic separator in the central line.

It proves that the phase distinction is not carried by support density, event density, or the existence of a finite-control successor mechanism alone.

---

## 11. Definitional invariance

The `DCE` property is stable under a useful class of representation changes.

### Theorem 11.1 — DCE under coherent uniform FO definitional equivalence

Let `mathcal A=(mathfrak A_m)` and `mathcal B=(mathfrak B_m)` be prefix-coherent families on the same ordered base carrier. Suppose every primitive relation of `mathcal B` is uniformly FO-definable in `mathcal A` by fixed formulas.

If `mathcal A` has DCE, then `mathcal B` has DCE.

### Proof

Choose a decidable coherent envelope `mathfrak A_infty`.

For each primitive relation `R_B` of `mathcal B`, take its uniform finite-prefix defining formula in `mathcal A` and apply the prefix-lift construction (5.1). Prefix coherence of `mathcal B` guarantees that the lifted relation has exactly `mathfrak B_m` as its restriction to every `[m]`.

Thus these lifted relations define a coherent envelope `mathfrak B_infty` inside `mathfrak A_infty` by FO formulas. Its FO theory reduces effectively to `Th(mathfrak A_infty)` and is therefore decidable. `□`

If the families are uniformly FO-interdefinable, DCE holds for one iff it holds for the other.

Therefore DCE is not tied to the choice between full-state and event-state presentations:

\[
\boxed{
DCE(Z)\iff DCE(U_F,D_F).
}
\tag{11.1}
\]

This gives the desired first step toward an interpretation-invariant phase resource.

---

## 12. What this theorem does and does not prove

The theorem gives a **one-sided semantic firewall**:

\[
DCE+Add\Rightarrow\neg Mul.
\]

It does **not** claim:

- every exact-AL1 family has DCE;
- every non-DCE family is AL2;
- DCE is invariant under arbitrary high-dimensional FO interpretations with quotients or non-prefix-preserving recodings;
- automaticity is necessary for exact AL1.

So DCE is already strong enough to separate the two canonical equal-cost examples, but it is not yet a complete classification invariant.

The next interpretation-invariance problem is narrower and now well posed:

\[
\boxed{
\text{how far beyond coherent FO definitional equivalence does the DCE separator survive?}
}
\]

---

## 13. Literature interface

The external facts used are classical and are not claimed as FCOA novelties:

1. word-automatic structures have decidable first-order theory (Hodgson; Khoussainov--Nerode; Blumensath--Gradel and subsequent surveys);
2. FO-definable relations in an automatic structure remain automatic;
3. Fibonacci/Zeckendorf numeration admits finite-automaton treatments of normalization/addition.

The FCOA contribution in this note is the **prefix-lift use of decidable coherent envelopes as a finite-family arithmetic-phase barrier**, together with its application to the equal-linear-support differential Zeckendorf/BIT comparison.

A publication version must retain this conservative novelty boundary.

---

## 14. New central frontier

The original equal-cost question has now been answered at the first nontrivial semantic level:

\[
\boxed{
DCE\ \text{separates the canonical linear }AL1\text{ and }AL2\text{ histories}.
}
\]

The next strongest strike is to determine whether DCE can be upgraded to an interpretation-level invariant, or replaced by a stronger invariant built from effective envelope interpretability.

A second natural direction is a class theorem:

> characterize numeration histories whose full state has a decidable/automatic coherent envelope, whose addition automaton is FO-realizable, and whose successor changes only amortized `O(1)` features; their differential histories should yield optimal linear exact AL1.

That would turn the Zeckendorf witness into a general **Aperiodic Automatic Numeration Corridor** rather than a single construction.
