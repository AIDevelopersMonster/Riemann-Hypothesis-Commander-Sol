# G4 Hostile Audit Reconciliation — R2

**Project:** FCOA Admissibility Geometry  
**Audit target:** `G4_BOUNDED_OUTPUT_AMPLIFICATION.md`  
**Date:** 2026-08-27  
**Status after reconciliation:** core G4 theorem confirmed; no mathematical repair to the active-sort claims; one-sorted definedness and order-recovery consequences made explicit.

## 1. Executive verdict

The independent hostile audit confirms the full G4 construction for every \(N\ge3\), including the exceptional smallest case \(N=3\).

For G4-C:

\[
\boxed{
\operatorname{Aut}(D_{4C}\upharpoonright X_N)\cong S_{N-1},
\qquad
\operatorname{Aut}(\otimes_{4C})\cong C_2.
}
\]

For G4-A:

\[
\boxed{
\operatorname{Aut}(D_{4A}\upharpoonright X_N)
\cong S_2\times S_{N-1},
\qquad
\operatorname{Aut}(\otimes_{4A})=1.
}
\]

The exact active-sort Value-Rigidity Indices are therefore

\[
\boxed{
\operatorname{VRI}(G4\text{-}C)=\frac{(N-1)!}{2},
}
\]

and

\[
\boxed{
\operatorname{VRI}(G4\text{-}A)=2(N-1)!.
}
\]

Thus the bounded-output amplification claim survives hostile audit:

\[
\boxed{
|O|=2
\quad\text{while}\quad
\operatorname{VRI}\to\infty
\text{ factorially.}
}
\]

## 2. Fiber-partition stabilizer

Let

\[
D_+=\{(P_i,P_j):2\le i<j\le N\},
\]

\[
D_-=\{(P_i,P_j):2\le j<i\le N\}.
\]

The audit independently proves that the setwise stabilizer of the unordered partition

\[
\{D_+,D_-\}
\]

inside \(S_{N-1}\) is exactly \(C_2\):

- the only permutation preserving the two fibers individually is the identity;
- the only permutation exchanging them globally is total reversal;
- no non-monotone permutation can preserve the fiber equivalence relation by mixing the two behaviors locally.

This closes the main group-theoretic gap in the G4-C proof.

## 3. G4-C exact invariants

The audit confirms:

\[
\boxed{
|\operatorname{Comm}_{4C}|=3(N-1).
}
\]

The exact Association Spectrum on \((X_N)^3\) is

\[
\boxed{
\begin{aligned}
EQ &= N^2+N-2,\\
NEQ &= 0,\\
LEFT &= 2N^2-N,\\
RIGHT &= 2N(N-1),\\
NONE &= N^3-2N^2+5N+3.
\end{aligned}}
\]

Since \(2N(N-1)=2N^2-2N\), this is exactly the formula recorded before audit.

Small cases:

\[
N=3:\quad (10,0,15,12,27),
\]

\[
N=4:\quad (18,0,28,24,55).
\]

For \(N=3\),

\[
S_2=C_2,
\qquad
\operatorname{VRI}(G4\text{-}C)=1,
\]

so the first strict amplification occurs at \(N=4\).

## 4. G4-A exact invariants

The audit confirms that the anchor

\[
P_1\otimes_{4A}P_0=\Omega_+
\]

internally fixes \(\Omega_+\), prevents the output swap required by generic reversal, and therefore kills the last nontrivial full-operation automorphism.

Hence

\[
\boxed{
\operatorname{Aut}(\otimes_{4A})=1.
}
\]

After value erasure, however, the anchor makes the two loopless boundary points symmetric and leaves the generic sector completely reflexive. Therefore

\[
\boxed{
\operatorname{Aut}(D_{4A}\upharpoonright X_N)
\cong S_2\times S_{N-1}.
}
\]

The commutation count remains

\[
\boxed{
|\operatorname{Comm}_{4A}|=3(N-1).
}
\]

The exact Association Spectrum is

\[
\boxed{
\begin{aligned}
EQ &= N^2+N-2,\\
NEQ &= 0,\\
LEFT &= 2N^2-N,\\
RIGHT &= 2N^2-N,\\
NONE &= N^3-2N^2+4N+3.
\end{aligned}}
\]

Small cases:

\[
N=3:\quad (10,0,15,15,24),
\]

\[
N=4:\quad (18,0,28,28,51).
\]

## 5. Terminal-output separation

The audit explicitly checks the potentially dangerous small case \(N=3\), where each of \(\Omega_+\) and \(\Omega_-\) has only one preimage cell and therefore cannot be separated from the indexed terminal outputs merely by preimage cardinality.

Nevertheless mixing is impossible because the preimage configurations are structurally different:

- \(\Omega_\pm\) arise from off-diagonal generic-generic pairs;
- \(E_i^\ast\) arises from \((P_i,P_0)\);
- \(E_i^\times\) arises from the diagonal \((P_i,P_i)\).

Thus the only nontrivial anonymous-output action in G4-C is

\[
\Omega_+\leftrightarrow\Omega_-
\]

accompanied by total generic reversal.

## 6. Full one-sorted definedness caveat

The pre-audit G4 statements were deliberately active-sort statements. The audit confirms them and adds the corresponding one-sorted caveat.

If all terminal outputs are retained after value erasure, they are isolated points of the definedness relation. There are

\[
2(N-1)+2=2N
\]

such terminal points.

Therefore

\[
\boxed{
\operatorname{Aut}_{\rm full}(D_{4C})
\cong S_{N-1}\times\operatorname{Sym}(2N),
}
\]

and

\[
\boxed{
\operatorname{Aut}_{\rm full}(D_{4A})
\cong S_2\times S_{N-1}\times\operatorname{Sym}(2N).
}
\]

The VRI used in this line remains explicitly the active/base-sort index.

## 7. New consequence: order memory becomes exact

The audit sharpens the transition to the Arithmetic Leakage programme.

### G4-C

The full operation recovers the orientation coloring only up to global reversal. Equivalently, it remembers the finite generic linear order up to choice of direction. This is exactly reflected by

\[
\operatorname{Aut}(\otimes_{4C})\cong C_2.
\]

### G4-A

The anchor fixes \(\Omega_+\). Consequently the external generic order becomes internally and uniformly definable across the finite family:

\[
\boxed{
x<y
\iff
x,y\in G_N
\land
x\otimes_{4A}y=P_1\otimes_{4A}P_0.
}
\]

The boundary points and generic sort are themselves uniformly recognizable in the exact operation family. Hence G4-A crosses a genuine threshold:

\[
\boxed{
\text{anonymous orientation up to reversal}
\longrightarrow
\text{anchored definable total order}.
}
\]

This is **order memory**, not yet arithmetic on the external indices. No addition or multiplication relation follows merely from the existence of the definable finite order.

## 8. Arithmetic Leakage verdict at G4

The audit finds no hidden index addition or multiplication in G4.

What G4-A does provide is stronger than mere rigidity:

- exact generic total order is uniformly definable;
- therefore order-theoretic derived relations, such as finite successor/betweenness, are available;
- this must not be conflated with uniform interpretation of \((\mathbb N,+,\times)\) or with an internally generated arithmetic of indices.

Thus the next main-line question is now precise:

\[
\boxed{
\text{After total order becomes uniformly definable, what is the weakest additional FCOA mechanism that first yields genuine arithmetic leakage?}
}
\]

The programme must distinguish at least:

\[
\text{order}
\;<\;
\text{successor/distance information}
\;<\;
\text{Presburger-like addition}
\;<\;
\text{full arithmetic}.
\]

No strictness claim in this displayed ladder is asserted without proof; it is the agenda for the next boundary analysis.

## 9. Final classification

The hostile audit produces no repair to the central G4 theorem.

\[
\boxed{
\mathbf F:\ G4\text{-}C\text{ and G4\text{-}A group formulas}
}
\]

\[
\boxed{
\mathbf F:\ \text{exact Association Spectra and commutation counts}
}
\]

\[
\boxed{
\mathbf F:\ \operatorname{VRI}(G4\text{-}C)=\frac{(N-1)!}{2},
\quad
\operatorname{VRI}(G4\text{-}A)=2(N-1)!
}
\]

\[
\boxed{
\mathbf F:\ \text{uniform anchored generic-order recovery in G4-A}
}
\]

`Value-Rigidity Index` and `Bounded-Output Rigidity Amplification` remain working terminology / theorem naming; no priority claim is made.

G4 remains post-publication relative to DOI 10.5281/zenodo.22129787 and is not silently folded into that release.
