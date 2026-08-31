# SOL-QFIELD — Universal Linearization of Reversible History and the Non-Abelian Matrix Residue

**Version:** 0.6  
**Date:** 2026-08-31  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** SIXTH TARGET COMPLETE / CONDITIONAL A2 PROVED / COMPLEX GROUP-ALGEBRA ENVELOPE IDENTIFIED  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264  
**Depends on:** `SOL_QFIELD_REVERSIBLE_HISTORY_v0_5.md`

---

## 1. Executive verdict

Version 0.5 closed the reversible-history-size problem for the native radial associator diamond:

\[
LR\ne RL
\tag{1}
\]

is retained by the cardinality-minimal finite group \(S_3\), and its order distinction has a faithful two-dimensional unitary representation. However, group composition supplies only sequential composition. It does not itself define an addition of parallel histories.

The next question was whether a parallel-history addition can be obtained canonically rather than hand-written.

The answer is conditional but exact.

### Result A — FCOA alone still does not choose an additive coefficient system

The extensional FCOA operation and the history group do not choose whether parallel histories should be combined using Boolean union, natural-number multiplicity, real weights, complex amplitudes, tropical weights, or another semiring.

Thus there is no coefficient-free theorem saying

\[
\boxed{\text{FCOA itself forces }\mathbb C.}
\tag{2}
\]

### Result B — once complex additive amplitudes and bilinear composition are required, linearization is universal

Fix the reversible history group

\[
G=S_3.
\tag{3}
\]

If one requires a complex vector space of formal parallel histories, embeds each \(g\in G\) as a basis history, and requires sequential composition to extend complex-bilinearly from group multiplication, then the universal object is the complex group algebra

\[
\boxed{\mathbb C[S_3].}
\tag{4}
\]

This is not a model choice among many isomorphic-looking constructions; it is characterized by a universal extension property.

### Result C — the route-order difference survives only in the non-Abelian matrix block

Over \(\mathbb C\),

\[
\boxed{
\mathbb C[S_3]
\cong
\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C).
}
\tag{5}
\]

The two scalar summands are the trivial and sign representations. Both annihilate the radial order difference

\[
\Delta:=st-ts.
\tag{6}
\]

The faithful two-dimensional standard representation does not:

\[
\rho_{\mathrm{std}}(\Delta)\ne0.
\tag{7}
\]

Therefore the information that distinguishes \(LR\) from \(RL\) lives entirely in the genuinely noncommutative matrix component.

### Result D — conditional A2

Under the explicitly stated additional axioms

1. complex scalar coefficients;
2. linear superposition of parallel history symbols;
3. bilinear extension of sequential composition;

linearization through \(\mathbb C[S_3]\) is forced by the universal property.

Thus the previous frontier is resolved as

\[
\boxed{\texttt{A2-CONDITIONAL}.}
\tag{8}
\]

The qualifier is essential: FCOA does not derive the complex field or the superposition axiom. But **if** one asks for complex coherent addition, the algebraic completion is no longer arbitrary.

### Result E — this is still not quantum mechanics

The group algebra supplies a complex linear process algebra. It does not by itself supply:

- a distinguished Hilbert inner product on physical states;
- normalized state vectors;
- a Born measurement rule;
- a physical Hamiltonian;
- tensor products of independent systems;
- Fock space;
- CAR/CCR;
- particle/antiparticle dynamics.

The result is therefore an algebraic bridge to linear process structure, not a QFT derivation.

---

## 2. From history group to parallel histories

Version 0.5 identified the minimal finite reversible history group

\[
G=S_3
\tag{9}
\]

with generators

\[
s=g(L),
\qquad
t=g(R),
\tag{10}
\]

chosen as two noncommuting transpositions. The native diamond routes map to

\[
st\ne ts.
\tag{11}
\]

At the group level, the legal primitive operation is multiplication:

\[
(g_2,g_1)\mapsto g_2g_1.
\tag{12}
\]

There is no intrinsic group operation representing “take history \(g\) and history \(h\) as coherent alternatives.”

An additive completion is therefore a genuinely new semantic layer.

---

## 3. Coefficient-system underdetermination

### Proposition 3.1 — No coefficient-free additive selector

The multiplicative history group \(S_3\), together with the FCOA endpoint-forgetting map, does not determine a unique commutative addition law on formal parallel histories.

### Proof

For any commutative semiring \(K\), one may form the semiring/group-semiring

\[
K[S_3]
\tag{13}
\]

of finite formal sums

\[
\sum_{g\in S_3}a_g g,
\qquad a_g\in K,
\tag{14}
\]

with coefficientwise addition and convolution product extending the group law.

Distinct coefficient semirings give inequivalent notions of parallel combination. For example:

- \(K=\mathbb B\) records support only;
- \(K=\mathbb N\) records multiplicity;
- \(K=\mathbb R_{\ge0}\) supports nonnegative weights;
- \(K=\mathbb C\) supports complex linear amplitudes.

Nothing in the original FCOA carrier/value rules singles out one of these coefficient systems. Therefore the base/history data alone do not determine a unique additive enrichment. \(\square\)

### Consequence

The strict unconditional verdict remains

\[
\boxed{\texttt{A0 at the coefficient-selection level}.}
\tag{15}
\]

There is no native derivation of “use complex numbers” from the current FCOA axioms.

---

## 4. Complex linearization

Now impose the additional hypothesis motivated by the amplitude programme:

> Parallel histories may be combined with complex coefficients, and sequential composition must distribute bilinearly over those combinations.

### Definition 4.1 — Complex history algebra target

A complex history-algebra realization consists of a unital complex algebra \(A\) and a group homomorphism

\[
\iota:G\to A^\times
\tag{16}
\]

from the reversible history group into the units of \(A\).

The intended meaning is that group histories compose multiplicatively and formal complex parallel combinations are evaluated linearly.

---

## 5. Theorem A — universal complex completion

### Theorem 5.1 — Universal Linearization

Let \(G=S_3\). There exists a unital complex algebra \(\mathbb C[G]\) and canonical embedding

\[
j:G\to\mathbb C[G]^\times
\tag{17}
\]

such that for every unital complex algebra \(A\) and every group homomorphism

\[
\iota:G\to A^\times,
\tag{18}
\]

there exists a unique unital complex-algebra homomorphism

\[
\widetilde\iota:\mathbb C[G]\to A
\tag{19}
\]

with

\[
\widetilde\iota\circ j=\iota.
\tag{20}
\]

Thus \(\mathbb C[S_3]\) is the universal complex linear envelope of the reversible FCOA history group.

### Proof

As a vector space, define

\[
\mathbb C[G]
=
\left\{
\sum_{g\in G}a_g[g]:a_g\in\mathbb C
\right\}.
\tag{21}
\]

Because \(G\) is finite, every sum has six coefficients. Define multiplication on basis vectors by

\[
[g][h]=[gh]
\tag{22}
\]

and extend bilinearly:

\[
\left(\sum_g a_g[g]\right)
\left(\sum_h b_h[h]\right)
=
\sum_{g,h}a_gb_h[gh].
\tag{23}
\]

Associativity follows from associativity in \(G\); \([1_G]\) is the unit.

Set

\[
j(g)=[g].
\tag{24}
\]

Given \(A\) and \(\iota\), define

\[
\widetilde\iota\left(\sum_g a_g[g]\right)
:=
\sum_g a_g\iota(g).
\tag{25}
\]

This map is complex-linear and unital. Using (23) and the homomorphism law for \(\iota\), it preserves multiplication. It clearly satisfies (20).

Uniqueness follows because the basis elements \([g]\) span \(\mathbb C[G]\), so any complex-linear extension agreeing with \(\iota\) on all \([g]\) is forced on every element. \(\square\)

### Corollary 5.2 — Conditional A2

Once complex superposition and bilinear composition are required,

\[
\boxed{\text{the universal additive/multiplicative completion is }\mathbb C[S_3].}
\tag{26}
\]

This is the precise sense in which linearization becomes forced.

---

## 6. Parallel radial histories inside the group algebra

The two route histories are represented by basis elements

\[
[st],
\qquad
[ts].
\tag{27}
\]

A formal coherent alternative can now be written as

\[
\alpha[st]+\beta[ts],
\qquad
\alpha,\beta\in\mathbb C.
\tag{28}
\]

The symmetric and antisymmetric order combinations are

\[
\Sigma:=[st]+[ts],
\tag{29}
\]

\[
\Delta:=[st]-[ts].
\tag{30}
\]

The old extensional FCOA semantics forgets both the group-history label and these linear combinations, retaining only the common endpoint of the two evaluation histories.

Thus the group algebra is an enrichment, with a natural forgetful collapse back to the extensional value layer.

---

## 7. Representation structure of C[S3]

The complex irreducible representations of \(S_3\) are:

1. the trivial representation of dimension \(1\);
2. the sign representation of dimension \(1\);
3. the standard representation of dimension \(2\).

The dimension-square identity is

\[
1^2+1^2+2^2=6=|S_3|.
\tag{31}
\]

By the finite-group semisimple decomposition over \(\mathbb C\),

\[
\boxed{
\mathbb C[S_3]
\cong
\mathbb C
\oplus
\mathbb C
\oplus
M_2(\mathbb C).
}
\tag{32}
\]

This decomposition is standard representation theory. Its relevance here is that it exactly separates scalar/abelian history information from the non-Abelian order information required by the native FCOA diamond.

---

## 8. Theorem B — order memory vanishes in every scalar block

Let

\[
s=(12),
\qquad
t=(23).
\tag{33}
\]

Then \(st\) and \(ts\) are the two 3-cycles and are both even permutations.

### Theorem 8.1 — Scalar-Block Annihilation of the Order Difference

For

\[
\Delta=[st]-[ts],
\tag{34}
\]

both one-dimensional irreducible representations send \(\Delta\) to zero:

\[
\rho_{\mathrm{triv}}(\Delta)=0,
\tag{35}
\]

\[
\rho_{\mathrm{sgn}}(\Delta)=0.
\tag{36}
\]

The standard two-dimensional representation satisfies

\[
\rho_{\mathrm{std}}(\Delta)\ne0.
\tag{37}
\]

### Proof

The trivial representation sends every group element to \(1\), hence

\[
\rho_{\mathrm{triv}}(\Delta)=1-1=0.
\tag{38}
\]

Both \(st\) and \(ts\) are 3-cycles and therefore even, so the sign representation also sends both to \(+1\):

\[
\rho_{\mathrm{sgn}}(\Delta)=1-1=0.
\tag{39}
\]

The standard representation is faithful. Since

\[
st\ne ts,
\tag{40}
\]

we have

\[
\rho_{\mathrm{std}}(st)\ne\rho_{\mathrm{std}}(ts),
\tag{41}
\]

and therefore (37). \(\square\)

### Corollary 8.2 — Non-Abelian Matrix Residue

Under the decomposition (32), the order-sensitive element \(\Delta\) has the form

\[
\boxed{
\Delta
\longmapsto
(0,0,D),
\qquad
D\in M_2(\mathbb C),\ D\ne0.
}
\tag{42}
\]

Thus the entire \(LR/RL\) order distinction is invisible to scalar sectors and survives only in the matrix block.

This sharpens the scalar-character no-go of v0.5 from a statement about representations to a statement about the full universal complex linear envelope.

---

## 9. Symmetric versus antisymmetric route combinations

Because \(st\) and \(ts\) form the conjugacy class of 3-cycles, their class sum

\[
\Sigma=[st]+[ts]
\tag{43}
\]

is central in \(\mathbb C[S_3]\).

By contrast,

\[
\Delta=[st]-[ts]
\tag{44}
\]

is not central and records orientation/order within that conjugacy class.

### Proposition 9.1

The two-dimensional subspace

\[
\operatorname{span}_{\mathbb C}\{[st],[ts]\}
\tag{45}
\]

splits into the symmetric line spanned by \(\Sigma\) and the order-antisymmetric line spanned by \(\Delta\).

### Interpretation

The universal linearization therefore separates two kinds of information that were collapsed at the old FCOA endpoint level:

- a conjugacy/class-symmetric parallel-history component;
- a noncentral order-sensitive residue.

No physical boson/fermion interpretation is licensed by the words “symmetric” and “antisymmetric” here. They refer only to exchange of the two route words \(st\leftrightarrow ts\).

---

## 10. What A2 does and does not mean

The phrase “linearization forced” is valid only under explicit premises.

### Premises

1. the finite reversible history group \(S_3\) is retained;
2. histories may be combined with coefficients in \(\mathbb C\);
3. parallel combination is vector addition;
4. sequential composition distributes bilinearly.

### Forced conclusion

The universal object is \(\mathbb C[S_3]\).

### Not forced

The current FCOA theory does not force premises 2-4.

Therefore

\[
\boxed{
\text{FCOA}\not\Rightarrow\mathbb C[S_3],
}
\tag{46}
\]

but

\[
\boxed{
\text{FCOA reversible history}
+
\text{complex linear-superposition axioms}
\Rightarrow
\mathbb C[S_3]
\text{ universally}.
}
\tag{47}
\]

This distinction is mandatory for claim discipline.

---

## 11. Why this still does not provide Born probabilities

An element

\[
v=\alpha[st]+\beta[ts]\in\mathbb C[S_3]
\tag{48}
\]

is a vector in a complex algebra, but no physical probability follows until a state/measurement functional or inner-product structure is chosen.

One could equip the group algebra with the standard coefficient inner product

\[
\left\langle
\sum_g a_g[g],
\sum_g b_g[g]
\right\rangle
=
\sum_g\overline{a_g}b_g,
\tag{49}
\]

under which the left regular representation is unitary. But this inner product is an additional mathematical choice/standard construction; current FCOA does not derive a physical interpretation of it.

Likewise, a matrix block \(M_2(\mathbb C)\) is not by itself a qubit observable algebra or state space.

---

## 12. Updated QFIELD ladder

The ladder now has an exact conditional linearization step:

### QF3a-R

Finite reversible history group \(S_3\), minimal size 6.

### QF3a-U

Faithful 2D unitary history representation.

### QF3b-K

Choose a coefficient semiring/ring \(K\). Universal additive enrichment is \(K[S_3]\).

### QF3b-C

Under complex amplitudes,

\[
\mathbb C[S_3]
\cong
\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C).
\tag{50}
\]

The route-order residue lies entirely in the matrix block.

### QF4

Physical/operational Hilbert-state and measurement structure.

Still absent.

### QF5

Fock/CAR structure.

Still absent.

Thus the current mathematical chain is

\[
\boxed{
\text{native diamond}
\to
M_3\text{-style finite memory}
\to
S_3\text{ reversible memory}
\to
\mathbb C[S_3]\text{ conditional linearization}
\to
M_2(\mathbb C)\text{ order residue}.
}
\tag{51}
\]

Here `M_3-style` means the three-element first-role monoid of v0.4, not a matrix algebra.

---

## 13. A0/A1/A2 decision

The previous alternatives require a nuanced answer.

### A0 — no additive selector

**True unconditionally at the coefficient-selection level.** FCOA does not choose \(K\).

### A1 — semiring/enrichment family

**True.** For every commutative semiring \(K\), the history system admits the canonical formal enrichment \(K[S_3]\).

### A2 — linearization forced

**True conditionally.** Once \(K=\mathbb C\) and bilinear complex superposition are required, the universal completion is uniquely characterized as \(\mathbb C[S_3]\).

Therefore the correct verdict is

\[
\boxed{
\texttt{A0 (coefficient choice)}
+
\texttt{A1 (canonical K-family)}
+
\texttt{A2-CONDITIONAL (complex linearization)}.
}
\tag{52}
\]

The alternatives were not logically exclusive once the coefficient-selection layer was separated from the universal-completion layer.

---

## 14. Line-completion consequence

Even the six-dimensional complex vector space underlying \(\mathbb C[S_3]\) is a fixed finite fiber attached to the radial history system. It is not a second unbounded coordinate.

Thus

\[
\boxed{
\text{finite complex linearization of history is still not DIMENSION-FORCING}.
}
\tag{53}
\]

This strengthens the programme's warning that an internal degree of freedom, matrix block, or finite-dimensional vector fiber must not be called emergent physical space.

---

## 15. Hostile audit

### “The complex group algebra proves quantum mechanics.”

**Rejected.** It proves a universal complex linear process algebra under explicitly added linear-superposition axioms.

### “FCOA derived the complex numbers.”

**Rejected.** The coefficient field remains externally chosen.

### “M2(C) means a qubit emerged.”

**Rejected.** The matrix block is the irreducible carrier of route-order information. No physical state/measurement interpretation has been derived.

### “The scalar blocks should also distinguish LR and RL because their phases differ.”

**Rejected.** Both scalar irreducible sectors annihilate \(\Delta=[st]-[ts]\).

### “The group algebra creates another spatial dimension.”

**Rejected.** It is a bounded internal linear fiber.

---

## 16. Publication decision

SOL-QFIELD has now accumulated a coherent abstract theorem chain substantial enough that a separate **mathematical history-memory note** is becoming plausible, although it should still not be framed as a QFT result.

Current recommendation:

\[
\boxed{\texttt{PREPUBLICATION NUCLEUS — DO NOT RELEASE YET}.}
\tag{54}
\]

Before separate publication, one more boundary should be settled: whether any FCOA-internal positivity/observation principle selects a norm or state functional on the linearized history algebra.

If that fails, the note can still be published as a clean no-go/architecture result ending at the group-algebra boundary. If a natural positive functional is selected, that would materially strengthen the bridge to operator-algebraic language.

---

## 17. Next strike — positive-functional selector

The next exact question is:

\[
\boxed{
\text{Does the FCOA history algebra carry a natural positive normalized functional}
\text{ selected by the old structure and reflection?}
}
\tag{55}
\]

For \(\mathbb C[S_3]\), many standard positive states exist, including those coming from unitary representations and vector states. The issue is **selection**, not existence.

Possible outcomes:

### P0 — state-selection no-go

FCOA/reflection invariance leaves a nontrivial convex family of positive normalized functionals. No Born-like state is canonically selected.

### P1 — canonical trace only

Natural invariance principles force the normalized regular trace/class function but do not produce a distinguished pure state or measurement structure.

### P2 — stronger positive structure

FCOA geometry/history/reflection selects a smaller state family or canonical GNS representation with nontrivial order-sensitive observables.

The `P0/P1/P2` problem is now the sharp frontier.
