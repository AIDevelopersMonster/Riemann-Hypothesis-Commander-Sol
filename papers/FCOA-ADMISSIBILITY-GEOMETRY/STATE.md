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

Consequently:

\[
\boxed{
\operatorname{Add}_N,
\operatorname{Mul}_N,
\operatorname{EqGap}_N
\text{ are not uniformly FO-definable in G4-A.}
}
\]

Thus G4-A is a fixed **order wall** for the uniform FO programme.

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

Correct statement:

\[
\boxed{
\text{EqGap is a canonical gateway to full additive leakage, not the globally weakest possible non-order enrichment.}
}
\]

## 7. Threshold-compression calibration

See [`THRESHOLD_COMPRESSION_CALIBRATION.md`](THRESHOLD_COMPRESSION_CALIBRATION.md).

External threshold benchmarks such as

\[
R_d(x,y)\iff x^d\le y
\]

have support

\[
|R_d\cap[N]^2|
=
\frac{d}{d+1}N^{1+1/d}+O(N),
\]

so subquadratic support can carry a nonlinear unary scale.

This establishes a programme-level warning:

\[
\boxed{
\text{support-growth complexity and arithmetic-leakage complexity are independent optimization axes.}
}
\]

The external functions are calibration benchmarks only, not accepted FCOA mechanisms.

## 8. New central theorem candidate — One-Cell Oracle / FO-Compilation Barrier

New file:

- [`ONE_CELL_ORACLE_AND_FO_COMPILATION_BARRIER.md`](ONE_CELL_ORACLE_AND_FO_COMPILATION_BARRIER.md)

### One-cell oracle degeneracy

For an arbitrary set of sizes

\[
S\subseteq\{2,3,4,\ldots\},
\]

modify exactly one previously undefined G4-A cell by

\[
P_0\otimes_S P_0=P_0
\iff
|G_N|\in S.
\]

Then the fixed sentence

\[
\exists b\,[B_0(b)\land T(b,b,b)]
\]

recognizes exactly the chosen size spectrum \(S\).

Therefore unrestricted external import can produce arbitrarily strong family-level leakage at only

\[
O(1)
\]

new-cell cost.

Thus raw cell-count minimization is degenerate unless external-import complexity is constrained.

### Strict intermediate parity benchmark

Taking

\[
S=\{m:m\equiv0\pmod2\}
\]

gives a family strictly stronger than FO[<] but still too weak to define truncated addition. The key reason is that with only one global parity bit, every definable size-spectrum is eventually constant on each parity class, while addition would define for example

\[
m\equiv1\pmod3.
\]

This gives an explicit benchmark strictly between the order wall and additive leakage, though it is deliberately an external-oracle construction.

### FO-Compilation Barrier

If finitely many new relation/operation symbols are uniformly parameter-free FO-definable in G4-A, then the expansion remains at exactly the same generic FO strength:

\[
\boxed{
FO(\text{definitional expansion of G4-A})=FO[<].
}
\]

Hence fixed-depth compositions, term operations, translations, commutation predicates and association predicates cannot escape the order wall when they are merely FO-definitional consequences of G4-A.

This yields the central dichotomy:

\[
\boxed{
\text{unrestricted external oracle: too powerful and artificially cheap}
}
\]

versus

\[
\boxed{
\text{uniform FO compilation from G4-A: provably unable to leave AL0.}
}
\]

A genuine next-stage FCOA mechanism must lie between these extremes.

## 9. Refined leakage map

### AL0 — Order Wall

Generic uniform FO power exactly FO[<]. G4-A is exactly here.

### AL-INT — intermediate non-order zone

Umbrella for modular/counting, sparse unary-scale, threshold-like, or other non-order enrichments that do not yet recover addition. This is not asserted to be one canonical level.

### AL1 — Additive Gateway

EqGap / truncated rank addition.

### AL2 — Full-Arithmetic Gateway

Uniform interpretation of full first-order arithmetic, or another independently audited equivalent criterion.

## 10. Current status

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
\mathbf W:\ \text{One-Cell Oracle Degeneracy / FO-Compilation Barrier; hostile audit pending}
\]

\[
\mathbf W:\ \text{Density-Leakage Orthogonality and multi-axis cost programme}
\]

\[
\mathbf W:\ \text{Value-Rigidity Index / Bounded-Output Rigidity Amplification terminology}
\]

## 11. Immediate main-line question

Do not optimize raw cell count and do not open an arbitrary G5 table.

The current central problem is now:

\[
\boxed{
\text{What is the weakest genuinely generated, non-oracular FCOA mechanism that escapes the FO-compilation barrier?}
}
\]

Candidate mechanism classes to test next:

1. unbounded iteration / closure whose depth grows with the carrier;
2. transitive-closure or least-fixed-point style memory;
3. a genuinely new primitive operation whose cells are not FO-definable from G4-A order;
4. hybrid interaction where neither operation is merely a definitional copy of the other.

The One-Cell Oracle / FO-Compilation Barrier must be hostile-audited before any such mechanism is promoted.
