# FCOA-Z — Mixed Commutative Bridge Generator 0.1

**Date:** 2026-08-30  
**Status:** CANDIDATE GENERATOR / NOT YET CANONICAL / LEAKAGE AUDIT REQUIRED

## 1. Question

Can one obtain a genuinely mixed-sign commutative sector for the existing signed operation without replacing the operation globally by ordinary addition and without making the same-sign sectors commutative?

The desired pattern is

\[
\mathcal C_{++}\neq EQ,
\qquad
\mathcal C_{--}\neq EQ,
\qquad
\mathcal C_{+-}=\mathcal C_{-+}=EQ,
\]

for the mixed cells that are opened by the extension.

The generator below is the first conservative candidate.

---

## 2. Mixed domain

Let

\[
X^+=\{x_k:k>0\},
\qquad
X^-=\{x_k:k<0\},
\]

and

\[
M=(X^+\times X^-)\cup(X^-\times X^+).
\]

Let

\[
\tau(x,y)=(y,x)
\]

be argument transposition.

The key geometric fact is that a cross-origin bridge can be regarded as **unoriented**: the event “the two endpoints are connected across the root” does not intrinsically distinguish which endpoint was presented first.

---

## 3. Minimal bridge-event variant B0

Introduce one new terminal output symbol

\[
E_{\mathrm{cross}}
\]

fixed by output reflection:

\[
\nu_E(E_{\mathrm{cross}})=E_{\mathrm{cross}}.
\]

Open every genuinely mixed cell by the single rule

\[
\boxed{
 x\oplus_{B0} y=E_{\mathrm{cross}}
 \qquad((x,y)\in M).
}
\tag{1}
\]

All legacy same-sign and root cells remain exactly as before.

This is a generator rule, not a finite exception table: definedness is determined only by the intrinsic predicate “the nonzero endpoints lie on opposite sides of the root”.

### Proposition 3.1 — mixed commutativity

For every \((x,y)\in M\),

\[
\boxed{x\oplus_{B0}y=y\oplus_{B0}x.}
\tag{2}
\]

### Proof

The mixed relation is symmetric:

\[
(x,y)\in M\iff(y,x)\in M.
\]

Both cells are assigned the same terminal value \(E_{\mathrm{cross}}\) by (1). Therefore (2) follows. \(\square\)

### Proposition 3.2 — reflection equivariance

For every mixed pair,

\[
\nu_E(x\oplus_{B0}y)=\nu x\oplus_{B0}\nu y.
\tag{3}
\]

### Proof

Simultaneous reflection preserves the property of lying on opposite sides of the root, and both sides of (3) equal \(E_{\mathrm{cross}}\). \(\square\)

### Proposition 3.3 — same-sign noncommutativity is untouched

Every legacy same-sign or root/nonzero cell keeps its old value and definedness. Therefore all previously proved witnesses of legacy noncommutativity remain witnesses after the B0 extension.

### Proof

The new domain added in (1) is disjoint from the inherited same-sign and root sectors. \(\square\)

---

## 4. Why B0 is interesting

B0 exhibits the exact qualitative phenomenon sought by the programme:

\[
\boxed{
\text{one extended operation}
\quad+
\text{same carrier}
\quad\Longrightarrow\quad
\text{different commutation law in the interaction sector}.
}
\]

The mixed commutativity is not imposed as a global axiom. It follows from choosing an **unoriented terminal interaction event** as the value type of every cross-origin cell.

The price is that B0 deliberately forgets all metric/radial information about the two operands. It is therefore the weakest-information candidate and should be tested first.

---

## 5. Richer bridge-orbit variant B1

If B0 is too degenerate, introduce a terminal sort indexed by unoriented mixed bridges.

For a mixed pair define its transposition orbit

\[
\beta(x,y)=\{(x,y),(y,x)\}.
\]

Introduce outputs

\[
E_{\beta(x,y)}=E_{\beta(y,x)}
\]

and define

\[
\boxed{
x\oplus_{B1}y=E_{\beta(x,y)}.}
\tag{4}
\]

Again

\[
x\oplus_{B1}y=y\oplus_{B1}x
\]

because the output is indexed by the unoriented bridge rather than by an ordered pair.

Reflection acts by

\[
\nu_E(E_{\beta(x,y)})
=E_{\beta(\nu x,\nu y)}.
\]

B1 preserves more endpoint memory than B0 and therefore has a higher arithmetic-leakage risk.

---

## 6. Why not synchronous cancellation as the first candidate

A tempting mixed rule is to move both opposite-sign operands toward the root until one is exhausted and return the survivor.

For coordinates \(i,j>0\), this computes the signed magnitude difference \(|i-j|\) together with the surviving branch. In ordinary signed coordinates this is already the mixed-sign part of integer addition.

Therefore

\[
\boxed{\text{synchronous cancellation is an arithmetic-leaky control case, not the baseline generator}.}
\]

It remains useful as a comparison point for measuring when a mixed generator crosses into `EqSignedGap`/`Add` memory.

---

## 7. Current firewall facts

For B0 with \(E_{\mathrm{cross}}\) reflection-fixed:

1. the global zero reflection remains an automorphism;
2. therefore oriented signed order remains blocked from parameter-free definition by the existing reflection argument;
3. ordinary signed multiplication remains blocked by the same reflection argument;
4. the mixed-domain predicate becomes operationally visible;
5. reflection alone does **not** block ordinary signed addition, so Add non-definability is still an open audit question.

No stronger arithmetic-safety claim is made yet.

---

## 8. Association question

B0 outputs are terminal in the baseline FCOA sense. Hence a mixed product cannot immediately re-enter a second binary operation.

This creates a strong association-definedness wall rather than classical associativity.

The next test is to compute the full sign-word association spectrum after B0 and decide whether a later controlled re-entry law can make alternating words such as

\[
+-+\quad\text{and}\quad-+-
\]

strongly associative while same-sign words retain legacy partial nonassociation.

---

## 9. Acceptance criteria

B0 may become the canonical first mixed model only if it passes:

1. full finite-window coherence;
2. exact automorphism calculation;
3. exact commutation count;
4. sign-word association spectrum;
5. Add/EqSignedGap leakage audit;
6. comparison with B1 and directed-displacement candidates;
7. hostile audit showing that mixed commutativity is not merely hidden global commutativity.

Until then:

\[
\boxed{B0\text{ is a concrete test generator, not a theorem of canonicality}.}
\]