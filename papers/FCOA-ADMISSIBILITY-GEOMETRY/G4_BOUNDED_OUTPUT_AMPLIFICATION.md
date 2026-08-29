# G4 Research Checkpoint — Bounded Output Alphabet, Unbounded Value Rigidity

**Project:** FCOA Admissibility Geometry  
**Status:** hostile-audited and fixed post-publication result  
**Date opened:** 2026-08-27  
**Audit reconciliation:** [`G4_HOSTILE_AUDIT_RECONCILIATION.md`](G4_HOSTILE_AUDIT_RECONCILIATION.md)  
**Publication boundary:** not part of Zenodo DOI 10.5281/zenodo.22129787

## 1. Research question

The Fiber-Transport Theorem reduces value-memory to stabilization of the partition of operation-domain cells into equal-value fibers. G3-A gives a finite example with positive Value-Rigidity Index.

The next question is quantitative:

> Can a **fixed finite anonymous output alphabet** carry an amount of rigidity that grows without bound, even when the generic operation domain itself remains maximally symmetric?

G4 answers this in the affirmative with only two anonymous terminal outputs.

The construction deliberately does **not** introduce addition or multiplication on the external indices. It imports only the external linear orientation of the fixed carrier and compiles it into value fibers.

## 2. M0 backbone

Let

\[
X_N=\{P_0,\ldots,P_N\},\qquad N\ge3,
\]

with generic sector

\[
G_N=\{P_2,\ldots,P_N\}.
\]

Retain the M0 multiplication cells:

\[
P_0\otimes P_i=P_0\qquad(1\le i\le N),
\]

\[
P_i\otimes P_0=E_i^\ast\qquad(2\le i\le N),
\]

\[
P_1\otimes P_i=P_i\otimes P_1=P_i\qquad(2\le i\le N),
\]

\[
P_i\otimes P_i=E_i^\times\qquad(2\le i\le N),
\]

with all other M0 cells undefined.

All \(E\)-outputs and all new \(\Omega\)-outputs below are terminal.

## 3. G4-C — complete generic domain with two anonymous orientation values

Introduce two distinct anonymous terminal outputs

\[
\Omega_+,\qquad\Omega_-.
\]

For every two distinct generic points define

\[
\boxed{
P_i\otimes_{4C}P_j=
\begin{cases}
\Omega_+,& i<j,\\
\Omega_-,& i>j,
\end{cases}
\qquad 2\le i,j\le N,\ i\ne j.
}
\]

The indices describe the **external carrier order** only. No internal arithmetic on indices is added.

The off-diagonal generic domain is complete:

\[
D_{4C}\cap(G_N^2\setminus\Delta)
=G_N^2\setminus\Delta.
\]

Hence definedness alone carries no generic positional information.

## 4. Definedness symmetry of G4-C

On the active/base sort,

\[
\boxed{
\operatorname{Aut}(D_{4C}\upharpoonright X_N)\cong S_{N-1}.
}
\]

The generic definedness relation is complete reflexive, while the M0 boundary asymmetry fixes \(P_0,P_1\).

If all terminal outputs are retained as isolated points after value erasure, then there are \(2N\) such terminal points and

\[
\boxed{
\operatorname{Aut}_{\rm full}(D_{4C})
\cong S_{N-1}\times\operatorname{Sym}(2N).
}
\]

The VRI below always refers to the active/base-sort group.

## 5. Full-operation automorphisms of G4-C

The two generic value fibers are

\[
D_+=\{(P_i,P_j):2\le i<j\le N\},
\]

\[
D_-=\{(P_i,P_j):2\le j<i\le N\}.
\]

The hostile audit independently confirms that the setwise stabilizer of the unordered partition

\[
\{D_+,D_-\}
\]

inside \(S_{N-1}\) is exactly \(C_2\): identity preserves the fibers individually, and total reversal exchanges them. No non-monotone generic permutation survives.

Therefore

\[
\boxed{
\operatorname{Aut}(\otimes_{4C})\cong C_2.
}
\]

The nontrivial automorphism is total generic reversal together with

\[
\Omega_+\leftrightarrow\Omega_-.
\]

For \(N=3\), this group equals \(S_2\), so no strict symmetry reduction occurs in the smallest generic sector. For \(N\ge4\), the reduction is strict.

## 6. Bounded-output rigidity amplification

For finite active sort define the working invariant

\[
\operatorname{VRI}(\star)
=
\left[
\operatorname{Aut}(D_\star\upharpoonright X_N):
\pi_X\operatorname{Aut}(\star)
\right].
\]

For G4-C,

\[
\boxed{
\operatorname{VRI}(G4\text{-}C)
=
\frac{(N-1)!}{2}.
}
\]

Hence, with a fixed anonymous output alphabet of size two,

\[
\boxed{
|O|=2,
\qquad
\operatorname{VRI}(G4\text{-}C)\to\infty
}
\]

factorially as \(N\to\infty\).

## 7. Commutation locus of G4-C

For every distinct generic pair, the two directions receive different values \(\Omega_+,\Omega_-\), so no new generic commuting pair is created.

Thus

\[
\boxed{
\operatorname{Comm}_{4C}
=
\{(P_i,P_i):2\le i\le N\}
\cup
\{(P_1,P_i),(P_i,P_1):2\le i\le N\},
}
\]

and

\[
\boxed{|\operatorname{Comm}_{4C}|=3(N-1).}
\]

## 8. Exact Association Spectrum of G4-C

On base triples \((X_N)^3\), the hostile audit confirms

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

Equivalently, \(RIGHT=2N^2-2N\).

Small checks:

\[
N=3:\quad(10,0,15,12,27),
\]

\[
N=4:\quad(18,0,28,24,55),
\]

\[
N=6:\quad(40,0,66,60,177).
\]

No `NEQ` triples occur.

## 9. Terminal-output separation

For \(N\ge4\), each \(\Omega\)-fiber has \(\binom{N-1}{2}\) preimage cells, while each \(E_i^\ast,E_i^\times\) has one. For \(N=3\), cardinality alone no longer separates them, but their preimage configurations do:

- \(\Omega_\pm\): off-diagonal generic-generic pairs;
- \(E_i^\ast\): pairs \((P_i,P_0)\);
- \(E_i^\times\): diagonal pairs \((P_i,P_i)\).

Hence \(\Omega_\pm\) cannot mix with the indexed \(E\)-outputs, including at \(N=3\).

## 10. G4-A — one boundary anchor

Extend G4-C by exactly

\[
\boxed{
P_1\otimes_{4A}P_0=\Omega_+.
}
\]

Since \(P_0,P_1\) are fixed in the full M0 operation, the anchor internally fixes \(\Omega_+\). Generic reversal would require \(\Omega_+\leftrightarrow\Omega_-\), so it can no longer extend.

Therefore

\[
\boxed{
\operatorname{Aut}(\otimes_{4A})=1.
}
\]

for every \(N\ge3\).

## 11. Definedness symmetry of G4-A

After values are erased, the anchor turns \((P_1,P_0)\) into a second boundary direction. Then \(P_0,P_1\) become symmetric in definedness, while the generic sector remains complete reflexive.

Thus on the active/base sort,

\[
\boxed{
\operatorname{Aut}(D_{4A}\upharpoonright X_N)
\cong S_2\times S_{N-1}.
}
\]

If terminal outputs are retained as isolated one-sorted points,

\[
\boxed{
\operatorname{Aut}_{\rm full}(D_{4A})
\cong S_2\times S_{N-1}\times\operatorname{Sym}(2N).
}
\]

Consequently

\[
\boxed{
\operatorname{VRI}(G4\text{-}A)=2(N-1)!.
}
\]

## 12. Exact Association Spectrum of G4-A

The anchor adds exactly \(N\) new RIGHT-only triples

\[
(P_1,P_0,z),\qquad z\in\{P_1,\ldots,P_N\},
\]

and changes no other class.

Hence

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

The commutation locus remains exact:

\[
\boxed{|\operatorname{Comm}_{4A}|=3(N-1).}
\]

Small checks:

\[
N=3:\quad(10,0,15,15,24),
\]

\[
N=4:\quad(18,0,28,28,51).
\]

## 13. Bounded-Output Rigidity Amplification Theorem

For every \(N\ge3\), there exists an extension of the M0 multiplication reduct using exactly two anonymous terminal output values such that:

1. the generic operation domain is maximally symmetric under \(S_{N-1}\);
2. value fibers reduce the full-operation carrier automorphism group to \(C_2\);
3. one fixed boundary anchor makes the full operation rigid;
4. the active-sort Value-Rigidity Indices are

\[
\boxed{
\frac{(N-1)!}{2}
\quad\text{and}\quad
2(N-1)!.
}
\]

Therefore

\[
\boxed{
\text{bounded output alphabet}
\not\Rightarrow
\text{bounded value-induced rigidity}.
}
\]

This theorem name is working terminology; no novelty or priority claim is made for the general colored-relation mechanism.

## 14. Exact order-memory consequence

G4-C remembers the generic finite linear order only **up to global reversal**: the two orientation fibers are internally present but anonymous and exchangeable.

G4-A crosses a stronger threshold. The anchor fixes \(\Omega_+\), so the generic order becomes uniformly parameter-free definable across the finite family. One convenient definition is

\[
\boxed{
x<y
\iff
x,y\in G_N
\land
x\otimes_{4A}y=P_1\otimes_{4A}P_0.
}
\]

Here the boundary roles and generic sector are uniformly recognizable in the exact operation family.

Thus the mechanism ladder now contains

\[
\boxed{
\text{orientation up to reversal}
\longrightarrow
\text{anchored definable finite total order}.
}
\]

## 15. Arithmetic Leakage boundary

The hostile audit found no hidden addition or multiplication of the external indices in G4. What G4-A does recover is exact finite order, hence also finite order-theoretic derived relations such as successor and betweenness.

Accordingly, the next main-line problem is no longer whether order is remembered. It is:

\[
\boxed{
\text{What is the weakest additional FCOA mechanism beyond anchored order memory that first yields genuine arithmetic leakage?}
}
\]

The next boundary analysis must distinguish, rather than conflate,

\[
\text{order},
\quad
\text{successor/distance information},
\quad
\text{Presburger-like addition},
\quad
\text{full arithmetic}.
\]

No strict implication/non-implication chain among these levels is asserted here without proof.

## 16. Status

After computational verification and independent hostile audit:

\[
\boxed{
\mathbf F:\ G4\text{-}C,\ G4\text{-}A,
\text{ exact spectra, commutation counts, automorphism groups and VRI formulas.}
}
\]

\[
\boxed{
\mathbf F:\ \text{uniform anchored generic-order recovery in G4-A.}
}
\]

G4 remains post-publication relative to DOI 10.5281/zenodo.22129787 and is not silently folded into that release.
