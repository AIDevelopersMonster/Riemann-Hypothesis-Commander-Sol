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

G3 therefore establishes value-memory beyond domain-memory.

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

### G4-C

Every off-diagonal generic pair is defined, using only two anonymous terminal outputs according to external orientation:

\[
P_i\otimes_{4C}P_j=
\begin{cases}
\Omega_+,&i<j,\\
\Omega_-,&i>j.
\end{cases}
\]

Confirmed active-sort groups:

\[
\boxed{
\operatorname{Aut}(D_{4C}\upharpoonright X_N)\cong S_{N-1},
\qquad
\operatorname{Aut}(\otimes_{4C})\cong C_2.
}
\]

Hence

\[
\boxed{
\operatorname{VRI}(G4\text{-}C)=\frac{(N-1)!}{2}.
}
\]

### G4-A

Add one boundary anchor:

\[
P_1\otimes_{4A}P_0=\Omega_+.
\]

Confirmed:

\[
\boxed{
\operatorname{Aut}(\otimes_{4A})=1,
}
\]

while after value erasure

\[
\boxed{
\operatorname{Aut}(D_{4A}\upharpoonright X_N)
\cong S_2\times S_{N-1}.
}
\]

Therefore

\[
\boxed{
\operatorname{VRI}(G4\text{-}A)=2(N-1)!.
}
\]

The exact generic total order is uniformly parameter-free definable in G4-A.

## 5. Arithmetic Leakage Boundary — opened

New file:

- [`ARITHMETIC_LEAKAGE_BOUNDARY.md`](ARITHMETIC_LEAKAGE_BOUNDARY.md)

No new G5 operation cells have been introduced.

### AL0 — Order Wall

The exact G4-A family is uniformly obtainable from finite linear orders by a fixed finite-copy interpretation: one generic ordered copy, two indexed terminal copies \(E^\ast,E^\times\), and finitely many fixed singleton tags.

Therefore every uniformly FO-definable relation on the generic sector reduces to a relation uniformly FO-definable on finite linear orders.

Using the classical non-definability of cardinality parity in FO over finite linear orders, the note derives:

\[
\boxed{
\text{canonical truncated rank addition is not uniformly FO-definable in G4-A,}
}
\]

and

\[
\boxed{
\text{canonical truncated rank multiplication is not uniformly FO-definable in G4-A.}
}
\]

Thus G4-A is order-memory but not yet additive/multiplicative arithmetic leakage in the uniform family sense.

### Successor is not a higher level than order

In a discrete total order,

\[
\operatorname{Succ}(x,y)
\iff
x<y\land\neg\exists z\,(x<z<y),
\]

so successor and betweenness are already FO consequences of G4-A order. They must not be treated as an expressive step above exact order.

### Infinite left wall

The natural infinite analogue of G4-A is uniformly interpretable in \((\mathbb N,<)\). By the classical decidability of the first-order theory of \((\mathbb N,<)\), it cannot parameter-free FO-interpret full true arithmetic \((\mathbb N,+,\times)\).

This provides an infinite-carrier calibration of the same left wall.

## 6. First genuine leakage gateway — variable equal-gap geometry

Define externally on generic ranks:

\[
\operatorname{EqGap}(a,b;c,d)
\iff
\operatorname{rk}(b)-\operatorname{rk}(a)
=
\operatorname{rk}(d)-\operatorname{rk}(c),
\]

for forward intervals.

The note proves that over the ordered generic sector, directed equal-gap geometry and truncated addition are FO-interdefinable:

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

Therefore EqGap is not uniformly FO-definable in G4-A, but it is the first natural FCOA-native target whose appearance would cross the order wall into additive/Presburger leakage.

## 7. Revised leakage levels

### AL0 — Order Wall

Uniform total order (hence successor/betweenness), but no uniform canonical rank addition or multiplication.

G4-A is at AL0.

### AL1 — Additive / Presburger Leakage

Uniform variable displacement / EqGap, equivalently truncated rank addition.

### AL2 — Full Arithmetic Leakage

A mechanism strong enough to uniformly define multiplication over the additive ordered structure, or otherwise interpret full first-order arithmetic.

The immediate main-line target is now

\[
\boxed{AL0\longrightarrow AL1.}
\]

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
\mathbf F:\ \operatorname{VRI}(G4\text{-}C)=\frac{(N-1)!}{2},
\quad
\operatorname{VRI}(G4\text{-}A)=2(N-1)!
\]

\[
\mathbf F:\ \text{uniform anchored generic-order recovery in G4-A}
\]

\[
\mathbf W:\ \text{Arithmetic Leakage Boundary theorem candidate; hostile audit pending}
\]

\[
\mathbf W:\ \text{Value-Rigidity Index / Bounded-Output Rigidity Amplification terminology}
\]

## 9. Immediate next step

Do not open arbitrary G5 cells.

Hostile-audit the Arithmetic Leakage Boundary note, especially:

1. the finite-copy reduction of exact G4-A to finite linear order;
2. the parity reduction used to rule out uniform rank addition;
3. the multiplication-to-parity reduction;
4. the claim that successor adds no FO power once order is already definable;
5. the infinite decidability obstruction;
6. EqGap/addition interdefinability and boundary conditions;
7. the distinction between fixed-finite definability and uniform family definability.

Only after this survives should the main line design the weakest AL0-to-AL1 FCOA mechanism.
