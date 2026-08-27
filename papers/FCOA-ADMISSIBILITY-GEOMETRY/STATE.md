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

Nothing in G3/G4 silently revises the Zenodo publication.

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

The only nontrivial full-operation automorphism is total generic reversal together with

\[
\Omega_+\leftrightarrow\Omega_-.
\]

Hence

\[
\boxed{
\operatorname{VRI}(G4\text{-}C)=\frac{(N-1)!}{2}.
}
\]

Exact spectrum:

\[
\boxed{
(N^2+N-2,\ 0,\ 2N^2-N,\ 2N(N-1),\ N^3-2N^2+5N+3).
}
\]

Commutation size:

\[
\boxed{3(N-1).}
\]

For \(N=3\), \(S_2=C_2\) and VRI=1; strict amplification starts at \(N=4\).

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

Exact spectrum:

\[
\boxed{
(N^2+N-2,\ 0,\ 2N^2-N,\ 2N^2-N,\ N^3-2N^2+4N+3).
}
\]

Commutation size remains

\[
\boxed{3(N-1).}
\]

### One-sorted definedness caveat

If terminal outputs are retained as isolated points after value erasure, then

\[
\operatorname{Aut}_{\rm full}(D_{4C})
\cong S_{N-1}\times\operatorname{Sym}(2N),
\]

and

\[
\operatorname{Aut}_{\rm full}(D_{4A})
\cong S_2\times S_{N-1}\times\operatorname{Sym}(2N).
\]

All VRI formulas in this line are explicitly active/base-sort indices.

## 5. New fixed consequence — anchored order recovery

G4-C remembers the generic finite order only up to global reversal.

G4-A fixes \(\Omega_+\) by the boundary anchor, so the exact generic total order becomes uniformly parameter-free definable across the finite family:

\[
\boxed{
x<y
\iff
x,y\in G_N
\land
x\otimes_{4A}y=P_1\otimes_{4A}P_0.
}
\]

Thus G4-A crosses the threshold from anonymous orientation to anchored definable order.

This is still order-memory, not internal addition or multiplication on indices.

## 6. Current status

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
\mathbf W:\ \text{Value-Rigidity Index and Bounded-Output Rigidity Amplification terminology}
\]

## 7. Main line now moves to Arithmetic Leakage

Do not open a new operation-rich G5 merely to continue the branch numbering.

The next main question is now:

\[
\boxed{
\text{After total order becomes uniformly definable, what is the weakest additional FCOA mechanism that first yields genuine arithmetic leakage?}
}
\]

The boundary analysis must keep separate at least:

1. exact finite order;
2. successor / betweenness / distance-style information;
3. Presburger-like additive structure;
4. full arithmetic / multiplication-level structure.

The immediate task is to define precise leakage levels and prove separation or collapse results between them without importing ordinary arithmetic by analogy.

No G5 cells are authorized yet. The next artifact should be an **Arithmetic Leakage Boundary note**, not another ad hoc operation table.
