# Decidable Coherent Envelope Phase Firewall

**Project:** FCOA Admissibility Geometry  
**Date:** 2026-08-30  
**Status:** central separator theorem  
**Depends on:** `HOSTILE_AUDIT_ZECKENDORF_SELECTIVE_MEMORY.md`, `HOSTILE_AUDIT_ZECKENDORF_EVENT_COMPRESSION.md`, `BINARY_HISTORY_COMPRESSION_AND_OVERSHOOT.md`

---

## 1. Equal-linear-cost problem

The central line now contains two prefix-generated event histories with the same optimal materialized support scale:

\[
\boxed{\Theta(m)}.
\]

Yet their arithmetic phases differ:

\[
\boxed{\text{Zeckendorf events: exact AL1}}
\]

and

\[
\boxed{\text{binary/BIT events: AL2}.}
\]

Therefore scalar support cannot be the phase separator.

This note isolates a semantic one-sided separator: whether the finite prefix family admits a coherent infinite envelope with decidable first-order theory.

---

## 2. Coherent prefix families

Fix one finite relational signature `tau` containing the natural order symbol `<`.

A family

\[
\mathcal A=(A_m)_{m\ge1}
\]

is **prefix coherent** if every `A_m` has universe `[m]={0,...,m-1}` and for `m<n`,

\[
A_m=A_n\upharpoonright[m].
\]

Equivalently, there is a unique direct-limit relational structure on `N` obtained by taking the union of all atomic facts.

For the separator theorem it is useful to state the envelope explicitly.

### Definition 2.1 — coherent infinite envelope

A `tau`-structure

\[
A_\infty
\]

on universe `N` is a coherent infinite envelope of `(A_m)` if

\[
\boxed{A_m=A_\infty\upharpoonright[m]}
\tag{2.1}
\]

for every `m`.

### Definition 2.2 — DCE property

A prefix family has the **Decidable Coherent Envelope** property, abbreviated `DCE`, if its coherent infinite envelope has decidable first-order theory.

For a genuinely prefix-coherent relational family the envelope is determined by the family, so this is not an existential choice of a convenient completion.

---

## 3. Relativization lemma

Let

\[
\varphi(\bar x)
\]

be any fixed `FO(tau)` formula.

For a fresh variable `b`, define

\[
\varphi^{<b}(\bar x)
\]

by recursively replacing

\[
\exists y\,\psi
\]

with

\[
\exists y\,(y<b\land\psi^{<b})
\]

and

\[
\forall y\,\psi
\]

with

\[
\forall y\,(y<b\rightarrow\psi^{<b}).
\]

Free variables are not changed.

### Lemma 3.1 — exact prefix relativization

If `A_m=A_\infty|[m]`, then for every tuple `\bar a<m`,

\[
\boxed{
A_m\models\varphi(\bar a)
\iff
A_\infty\models\varphi^{<m}(\bar a),
}
\tag{3.1}
\]

where the right side uses `m` as the boundary element and therefore denotes the induced domain `[m]` via `<m`.

More syntactically, for any carrier element `b` greater than all entries of `\bar a`, evaluation of `\varphi^{<b}` in `A_\infty` is exactly evaluation of `\varphi` in the prefix `A_b`.

### Proof

Induction on formula complexity. Atomic formulas agree because `A_b` is the induced substructure on `[b]`. Boolean cases are immediate. Quantifier clauses are exactly the recursive relativization above. `□`

---

## 4. Prefix-lift theorem

Suppose one fixed formula

\[
R_m(\bar x)\equiv\varphi_R(\bar x)
\]

uniformly defines a relation on every prefix.

Define in the infinite envelope

\[
R_\infty(\bar x)
:\iff
\exists b\,
\left(
\bigwedge_i x_i<b
\land
\varphi_R^{<b}(\bar x)
\right).
\tag{4.1}
\]

If the intended finite-prefix relation is truncation-stable — once the tuple lies in the prefix its truth value is the ordinary natural-number truth value — then (4.1) lifts it to the corresponding infinite relation.

Canonical addition and multiplication have exactly this stability.

### Lemma 4.1 — arithmetic prefix lift

If one fixed formula `Add_A(x,y,z)` defines

\[
x+y=z<m
\]

in every `A_m`, then (4.1) defines ordinary addition on `N` in `A_\infty`.

Likewise, if one fixed formula `Mul_A(x,y,z)` defines

\[
xy=z<m
\]

on every prefix, then its lift defines ordinary multiplication on `N`.

### Proof

For any fixed natural tuple `(x,y,z)`, choose any `b>max{x,y,z}`. By Lemma 3.1, the relativized formula agrees with the corresponding prefix formula. The truncated relation is true exactly when the ordinary equation is true, because the output `z` is already in `[b]`. `□`

---

## 5. Decidable-Envelope Barrier

### Theorem 5.1 — Decidable Coherent Envelope Phase Firewall

Let `(A_m)` be a prefix-coherent family in a fixed finite relational signature containing `<`. Assume:

1. its infinite coherent envelope `A_\infty` has decidable FO theory;
2. canonical truncated addition is uniformly FO-definable on every prefix `A_m`.

Then canonical truncated multiplication is **not** uniformly FO-definable on the prefixes.

Equivalently,

\[
\boxed{
DCE + Add\in FO_{unif}
\Longrightarrow
Mul\notin FO_{unif}.
}
\tag{5.1}
\]

### Proof

Assume for contradiction that one fixed formula uniformly defines truncated multiplication on all prefixes.

By Lemma 4.1, ordinary addition and multiplication on `N` are both first-order definable in `A_\infty`.

Therefore every first-order sentence of

\[
(\mathbb N,+,\times)
\]

can be effectively translated into an FO sentence of `A_\infty` by replacing the arithmetic relation symbols with their defining formulas.

But the FO theory of `(N,+,\times)` is undecidable, while by hypothesis `Th_FO(A_\infty)` is decidable. Contradiction. `□`

### Corollary 5.2

Any prefix family exposing both uniform truncated addition and uniform truncated multiplication has an undecidable coherent-envelope FO theory.

Thus every exact AL2 prefix family of this type fails `DCE`.

---

## 6. Zeckendorf event family satisfies DCE

Let

\[
\mathfrak Z=(\mathbb N,<,Z)
\]

be the infinite Zeckendorf incidence structure.

The earlier hostile audit established:

- canonical Zeckendorf representations form a regular language;
- order is synchronously recognizable;
- `Z(x,p)` is synchronously recognizable because the representation of `p` has exactly one `1`, and the `x`-track has `1` at that same position.

Hence `\mathfrak Z` is word-automatic.

Classically, the FO theory of every word-automatic structure is decidable (Khoussainov--Nerode; Blumensath--Graedel). Automatic structures are also closed under FO-definable relations.

The infinite event relations are FO-definable in `\mathfrak Z` by the adjacent-row formulas

\[
U(x,p),\qquad D(x,p),
\]

and conversely `Z` is FO-definable from `U,D` by latest-event integration.

Therefore

\[
\mathfrak E_F=(\mathbb N,<,U,D)
\]

is word-automatic and has decidable FO theory.

So the Zeckendorf event family satisfies

\[
\boxed{DCE.}
\tag{6.1}
\]

Together with its already proved uniform addition, Theorem 5.1 independently blocks uniform multiplication.

---

## 7. Binary event family necessarily fails DCE

Let

\[
\mathfrak E_2(m)=([m],<,U_2,D_2)
\]

be the differential binary history.

The event family is uniformly FO-interdefinable with the full BIT history on every finite prefix. By the classical finite-model-theory calibration

\[
FO(BIT)=FO(PLUS,TIMES),
\]

both truncated addition and truncated multiplication are uniformly FO-definable in `\mathfrak E_2(m)`.

Therefore Corollary 5.2 gives

\[
\boxed{\neg DCE\text{ for the binary event family}.}
\tag{7.1}
\]

In particular, the natural infinite event envelope has undecidable FO theory.

No separate direct proof that infinite BIT is nonautomatic is needed for the phase separation: undecidability follows semantically from the prefix-lift theorem.

---

## 8. Equal-linear-cost phase split

Both event families have exact support

\[
2m-2-O(\log m)=\Theta(m).
\]

Yet

\[
\boxed{
\begin{array}{c|c|c|c}
\text{family} & \text{support} & DCE & \text{phase}\\
\hline
\text{Zeckendorf events} & \Theta(m) & \text{yes} & AL1\\
\text{binary events} & \Theta(m) & \text{no} & AL2
\end{array}
}
\]

Thus the central comparison is no longer merely

\[
\text{same density, different leakage}.
\]

It has a semantic explanation:

\[
\boxed{
\text{decidable coherent envelope}
\quad\text{versus}\quad
\text{necessarily undecidable coherent envelope}.
}
\tag{8.1}
\]

This is a genuine theorem-level separator for the two canonical linear constructions.

---

## 9. Invariance properties

`DCE` is stronger than a presentation-specific automaton certificate.

The property “the coherent envelope has decidable FO theory” is invariant under effective uniform FO definitional equivalence of coherent prefix families: if two coherent envelopes are connected by fixed FO definitions in both directions, decidability of one FO theory transfers to the other by effective syntactic translation.

Therefore differential compression itself cannot change the `DCE` side of the phase boundary:

\[
Z\leftrightarrow_{FO} (U,D)
\]

preserves decidability, while

\[
BIT\leftrightarrow_{FO}(U_2,D_2)
\]

preserves undecidability.

This is the first separator on the central line that is explicitly stable under the event/full-history recoding used to obtain linear support.

### Limitation

`DCE` is a **one-sided firewall**, not a complete characterization of AL1.

An AL1 family could in principle have an undecidable coherent envelope for reasons unrelated to multiplication. Therefore one must not claim

\[
AL1\iff DCE.
\]

The proved implication is only (5.1), plus the concrete Zeckendorf/binary separation.

---

## 10. Stronger abstract interpretation

The result isolates two logically distinct resources:

1. **materialized information volume**, measured here by primitive support;
2. **theory complexity of the coherent infinite history envelope**.

Differential compression can drastically reduce the first without changing the second, because latest-event FO integration preserves definitional power.

This gives a sharpened Density-Leakage Orthogonality principle:

\[
\boxed{
\text{event density can be identical while envelope theory crosses decidable/undecidable.}
}
\tag{10.1}
\]

For exact AL1 design, a decidable coherent envelope is therefore a robust sufficient anti-AL2 certificate once uniform addition has been established.

---

## 11. Relation to automaticity

Automaticity is a convenient **sufficient certificate** for `DCE`, not the definition of the separator.

For the Zeckendorf family:

\[
\text{word-automatic}
\Longrightarrow
DCE
\Longrightarrow
\text{no uniform Mul once Add is present}.
\]

This is preferable to defining the phase boundary as “automatic versus nonautomatic”, because decidability of the coherent envelope is the exact property used by the contradiction proof and is invariant under broader effective FO recodings than a particular automatic presentation.

---

## 12. Status ledger

Fixed in this note:

\[
\boxed{\mathbf F:\ DCE+\text{uniform Add}\Rightarrow\text{no uniform Mul}.}
\]

\[
\boxed{\mathbf F:\ \text{Zeckendorf event family satisfies DCE}.}
\]

\[
\boxed{\mathbf F:\ \text{binary event family fails DCE}.}
\]

\[
\boxed{\mathbf F:\ \text{the two }\Theta(m)\text{-support event families are separated by DCE}.}
\]

\[
\boxed{\mathbf F:\ DCE\text{ is preserved under effective uniform FO definitional equivalence}.}
\]

Not claimed:

\[
\boxed{\mathbf N:\ DCE\text{ is not asserted to characterize all AL1 families}.}
\]

---

## 13. New frontier

The Equal-Linear-Cost Phase Separator problem is now solved for the canonical Zeckendorf-versus-binary pair by a semantic invariant.

The next stronger question is whether one can refine `DCE` into an **interpretation-invariant quantitative resource** that predicts where the envelope becomes undecidable before full AL2 is already known.

Natural candidates are:

- effective interpretation depth into automatic/decidable envelopes;
- recurrence-kernel complexity of the infinite history;
- synchronization dimension required to interpret arithmetic;
- generator workspace/recurrence width needed to force envelope undecidability.

A second worthwhile direction is an abstract **Event-Compression Theorem**: identify conditions under which differential materialization preserves FO power and reduces a generated history to linear support.
