# FCOA Admissibility Geometry — current state

**Canonical publication DOI:** 10.5281/zenodo.22129787  
**Publication date:** 2026-08-27  
**GitHub role:** theorem/reproducibility/demo companion  
**Maintenance boundary:** see [`WORKSPACE.md`](WORKSPACE.md)

## 1. Publication checkpoint — fixed

The published and audited chain remains

\[
\boxed{M0\longrightarrow G1\longrightarrow G2.}
\]

Nothing in G3/G4/Arithmetic-Leakage work silently revises the Zenodo publication.

## 2. G3 — fixed post-publication result

Files:

- [`G3_VALUE_GEOMETRY.md`](G3_VALUE_GEOMETRY.md)
- [`G3_HOSTILE_AUDIT_RECONCILIATION.md`](G3_HOSTILE_AUDIT_RECONCILIATION.md)
- verifier: `../../experiments/fcoa-domain-compilation/verify_g3.py`

Confirmed:

\[
\operatorname{Aut}(\otimes_S)\cong C_2,
\qquad
\operatorname{Aut}(\otimes_C)\cong C_2,
\qquad
\operatorname{Aut}(\otimes_A)=1.
\]

The repaired intrinsic definedness group of G3-A is

\[
\boxed{
\operatorname{Aut}(D_A\upharpoonright X_N)
\cong C_2\times C_2.
}
\]

G3 establishes value-memory beyond domain-memory.

## 3. Fiber-Transport Theorem — fixed relative typed result

See [`FIBER_TRANSPORT_THEOREM.md`](FIBER_TRANSPORT_THEOREM.md).

For a base/domain structure \((B,D)\) and a surjective anonymous terminal-output map

\[
c:D\to O,
\]

carrier automorphisms of the valued expansion are exactly the automorphisms of \((B,D)\) preserving the equality partition of domain cells induced by \(c\):

\[
\boxed{
\operatorname{Aut}(B,D,O;c)
\cong
\operatorname{Stab}_{\operatorname{Aut}(B,D)}(\equiv_c).
}
\]

Working finite invariant:

\[
\operatorname{VRI}(\star)
=
\left[
\operatorname{Aut}(D_\star\upharpoonright X):
\pi_X\operatorname{Aut}(\star)
\right].
\]

`Value-Rigidity Index` remains working terminology only.

## 4. G4 — hostile-audited and fixed

Files:

- [`G4_BOUNDED_OUTPUT_AMPLIFICATION.md`](G4_BOUNDED_OUTPUT_AMPLIFICATION.md)
- [`G4_HOSTILE_AUDIT_RECONCILIATION.md`](G4_HOSTILE_AUDIT_RECONCILIATION.md)
- verifier: `../../experiments/fcoa-domain-compilation/verify_g4.py`

Confirmed:

\[
\operatorname{Aut}(D_{4C}\upharpoonright X_N)\cong S_{N-1},
\qquad
\operatorname{Aut}(\otimes_{4C})\cong C_2,
\]

\[
\operatorname{VRI}(G4\text{-}C)=\frac{(N-1)!}{2},
\]

and after the boundary anchor

\[
P_1\otimes_{4A}P_0=\Omega_+,
\]

\[
\operatorname{Aut}(\otimes_{4A})=1,
\qquad
\operatorname{Aut}(D_{4A}\upharpoonright X_N)
\cong S_2\times S_{N-1},
\]

\[
\operatorname{VRI}(G4\text{-}A)=2(N-1)!.
\]

The exact generic total order is uniformly parameter-free definable in G4-A.

## 5. Arithmetic Leakage left wall — hostile-audited and fixed

Files:

- [`ARITHMETIC_LEAKAGE_BOUNDARY.md`](ARITHMETIC_LEAKAGE_BOUNDARY.md)
- [`G4A_GENERIC_FO_COLLAPSE.md`](G4A_GENERIC_FO_COLLAPSE.md)
- [`ARITHMETIC_LEAKAGE_HOSTILE_AUDIT_RECONCILIATION.md`](ARITHMETIC_LEAKAGE_HOSTILE_AUDIT_RECONCILIATION.md)

Relationalize the G4-A partial operation by

\[
T(x,y,z)\iff x\otimes_{4A}y=z.
\]

The hostile audit confirms the exact uniform-family collapse:

\[
\boxed{
FO(\text{G4-A on generic tuples})
=
FO(\text{finite linear order}).
}
\]

The source-to-target direction is formalized as a deterministic parameter-free fixed 7-copy FO transduction/copying interpretation. Conversely, \(P_0,P_1,G_N,\Omega_+\) and the generic order are uniformly parameter-free definable in the target graph signature.

Consequently:

\[
\boxed{
\operatorname{Add}_N
\text{ is not uniformly FO-definable in G4-A,}
}
\]

\[
\boxed{
\operatorname{Mul}_N
\text{ is not uniformly FO-definable in G4-A,}
}
\]

and

\[
\boxed{
\operatorname{EqGap}_N
\text{ is not uniformly FO-definable in G4-A.}
}
\]

The finite obstruction is the classical non-definability of cardinality parity in FO over finite linear orders. The proof uses only external ranks in the metalanguage; no index arithmetic is imported into the FCOA signature.

The natural infinite G4-A analogue is FO interpretable in \((\mathbb N,<)\), hence has decidable FO theory and cannot FO-interpret full standard arithmetic.

Thus G4-A is now a fixed **order wall** for the uniform FO programme.

## 6. Additive gateway — fixed relation, repaired minimality claim

For forward intervals define externally

\[
\operatorname{EqGap}(a,b;c,d)
\iff
\operatorname{rk}(b)-\operatorname{rk}(a)
=
\operatorname{rk}(d)-\operatorname{rk}(c).
\]

Over the ordered generic sector:

\[
\boxed{
\operatorname{Add}(x,y,z)
\iff
\operatorname{EqGap}(0_G,y;x,z),
}
\]

and conversely

\[
\boxed{
\operatorname{EqGap}(a,b;c,d)
\iff
\exists s\,
\bigl(\operatorname{Add}(a,s,b)\land\operatorname{Add}(c,s,d)\bigr).
}
\]

Hence EqGap is uniformly FO-interdefinable with truncated rank addition.

Audit repair: EqGap is **not** claimed to be the globally weakest possible non-order enrichment. Weaker modular/counting enrichments may sit between pure order and full additive leakage.

Correct statement:

\[
\boxed{
\text{EqGap is a canonical gateway to full additive leakage.}
}
\]

## 7. Refined leakage map

### AL0 — Order Wall

Generic uniform FO power is exactly FO of finite linear order. Successor and betweenness are already definable here.

G4-A is exactly at AL0.

### AL-MOD — possible intermediate non-order zone

Working placeholder for modular/counting or other non-FO[<] information that does not yet recover addition. No claim that this is a single canonical level.

### AL1 — Additive Gateway

EqGap / truncated rank addition becomes uniformly definable.

### AL2 — Full-Arithmetic Gateway

A mechanism uniformly interprets full first-order arithmetic, or meets another independently audited equivalent criterion.

## 8. Current status

\[
\mathbf F:\ M0,G1,G2\text{ published/audited checkpoint}
\]

\[
\mathbf F:\ G3\text{ hostile-audited after repair}
\]

\[
\mathbf F:\ \text{Fiber-Transport theorem in its stated relative typed setup}
\]

\[
\mathbf F:\ G4\text{-}C,G4\text{-}A\text{ hostile-audited}
\]

\[
\mathbf F:\ \text{uniform anchored generic-order recovery in G4-A}
\]

\[
\mathbf F:\ \text{G4-A Generic FO Collapse / Arithmetic Leakage left wall}
\]

\[
\mathbf F:\ \text{EqGap }\leftrightarrow\text{ truncated addition as the additive gateway}
\]

\[
\mathbf W:\ \text{Value-Rigidity Index / Bounded-Output Rigidity Amplification terminology}
\]

\[
\mathbf W:\ \text{AL0/AL-MOD/AL1/AL2 terminology and optimization programme}
\]

## 9. Immediate main-line questions

The left wall is closed. Do not add arbitrary G5 cells.

The central road now splits into two precise optimization problems:

\[
\boxed{
\text{What is the cheapest FCOA mechanism that leaves }FO[<]?
}
\]

and

\[
\boxed{
\text{What is the cheapest FCOA mechanism that reaches EqGap / additive leakage?}
}
\]

These questions need not have the same answer.

The next construction should first test whether a genuinely weaker intermediate leakage mechanism exists before deliberately targeting full EqGap.
