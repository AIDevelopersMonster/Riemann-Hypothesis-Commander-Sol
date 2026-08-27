# G4 Research Checkpoint — Bounded Output Alphabet, Unbounded Value Rigidity

**Project:** FCOA Admissibility Geometry  
**Status:** post-G3 theorem candidate; computationally checked, hostile audit pending  
**Date opened:** 2026-08-27  
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
\Omega_+,
\qquad
\Omega_-.
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

The indices here describe the **external carrier order** only. No internal arithmetic on indices is added.

The off-diagonal generic domain is now complete:

\[
D_{4C}\cap(G_N^2\setminus\Delta)
=G_N^2\setminus\Delta.
\]

Hence definedness alone has no generic positional information at all.

## 4. Definedness symmetry

Relative to the M0 boundary roles, the generic definedness reduct permits every permutation of \(G_N\):

\[
\boxed{
\operatorname{Aut}(D_{4C}\upharpoonright X_N)\cong S_{N-1}.
}
\]

Thus G4-C deliberately restores **maximal generic domain symmetry**.

This is the opposite of G2: in G2, orientation lived in a sparse directed domain; in G4-C, the generic domain is completely symmetric and all orientation information has been moved into the two value fibers.

## 5. Full-operation automorphisms

The two generic value fibers are

\[
D_+=\{(P_i,P_j):2\le i<j\le N\},
\]

\[
D_-=\{(P_i,P_j):2\le j<i\le N\}.
\]

By the Fiber-Transport Theorem, a generic permutation survives in the full operation exactly when it preserves the partition

\[
\{D_+,D_-\}
\]

setwise, allowing the two anonymous outputs to be swapped.

### Proposition G4-C.1

For every \(N\ge3\),

\[
\boxed{
\operatorname{Aut}(\otimes_{4C})\cong C_2.
}
\]

### Proof

If a generic permutation \(g\) fixes the two fibers individually, then

\[
i<j\iff g(i)<g(j),
\]

so \(g\) is an order automorphism of a finite linear order and therefore the identity.

If \(g\) exchanges the two fibers, then

\[
i<j\iff g(i)>g(j),
\]

so \(g\) is an order anti-automorphism. A finite linear order has exactly one such map: reversal.

Reversal extends to an automorphism by exchanging

\[
\Omega_+\leftrightarrow\Omega_-.
\]

Therefore only identity and reversal survive. \(\square\)

For \(N=3\), this group is \(C_2=S_2\), so no symmetry reduction occurs in the smallest generic sector. For \(N\ge4\), the reduction is strict.

## 6. Unbounded Value-Rigidity Index with two outputs

For finite active sort define

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

Hence

\[
\boxed{
\operatorname{VRI}(G4\text{-}C)\to\infty
\quad\text{as }N\to\infty,
}
\]

while the output alphabet remains fixed at exactly two anonymous values.

This gives the desired bounded-alphabet amplification:

\[
\boxed{
|O|=2
\quad\text{but}\quad
\operatorname{VRI}\text{ is unbounded.}
}
\]

No differentiated edge labels are needed; only the partition into the two orientation fibers is used.

## 7. Commutation locus

For every distinct generic pair,

\[
P_i\otimes_{4C}P_j\ne P_j\otimes_{4C}P_i,
\]

because the two directions receive \(\Omega_+\) and \(\Omega_-\).

Therefore no new generic commuting pairs are created, and the M0 commutation locus remains exact:

\[
\boxed{
|\operatorname{Comm}_{\otimes_{4C}}|=3(N-1).
}
\]

Thus G4-C can produce factorial symmetry reduction relative to definedness while leaving the commutation count at its M0 value.

## 8. Exact Association Spectrum of G4-C

On base triples \((X_N)^3\), direct enumeration gives

\[
\boxed{
\begin{aligned}
EQ &= N^2+N-2,\\
NEQ &= 0,\\
LEFT &= 2N^2-N,\\
RIGHT &= 2N^2-2N,\\
NONE &= N^3-2N^2+5N+3.
\end{aligned}
}
\]

The total is

\[
(N+1)^3.
\]

For \(N=3\), this reduces to

\[
(10,0,15,12,27),
\]

coinciding numerically with G3-C because a two-point generic sector has only one unordered generic pair.

For \(N=4\):

\[
(18,0,28,24,55).
\]

For \(N=6\):

\[
(40,0,66,60,177).
\]

The absence of `NEQ` persists even though the value fibers encode the full orientation of every generic pair.

## 9. G4-A — one boundary anchor

As in G3-A, add one fixed boundary cell

\[
\boxed{
P_1\otimes_{4A}P_0=\Omega_+.
}
\]

No other cell is added.

Because \(P_0,P_1\) are fixed in the full M0 operation, this cell fixes \(\Omega_+\). The reversal of the generic order would require

\[
\Omega_+\leftrightarrow\Omega_-,
\]

and is therefore impossible.

Hence:

\[
\boxed{
\operatorname{Aut}(\otimes_{4A})=1.
}
\]

## 10. Definedness symmetry of G4-A

After values are erased, the anchor makes the two M0 boundary points \(P_0,P_1\) symmetric exactly as in G3-A, while the complete off-diagonal generic domain still allows every permutation of \(G_N\).

Therefore

\[
\boxed{
\operatorname{Aut}(D_{4A}\upharpoonright X_N)
\cong C_2\times S_{N-1}.
}
\]

The two factors commute: one swaps \(P_0,P_1\), the other permutes \(G_N\).

Consequently

\[
\boxed{
\operatorname{VRI}(G4\text{-}A)=2(N-1)!.
}
\]

Again the output alphabet has only two anonymous values.

## 11. Exact Association Spectrum of G4-A

The single anchor adds exactly \(N\) new RIGHT-only triples to G4-C and changes no other association class. Therefore

\[
\boxed{
\begin{aligned}
EQ &= N^2+N-2,\\
NEQ &= 0,\\
LEFT &= 2N^2-N,\\
RIGHT &= 2N^2-N,\\
NONE &= N^3-2N^2+4N+3.
\end{aligned}
}
\]

The commutation locus remains

\[
\boxed{
|\operatorname{Comm}_{\otimes_{4A}}|=3(N-1).
}
\]

## 12. Main theorem candidate

### Bounded-Output Rigidity Amplification Theorem

For every \(N\ge3\), there exists an extension of the M0 multiplication reduct using exactly two anonymous terminal output values such that:

1. the generic off-diagonal operation domain is complete and therefore has full generic symmetry \(S_{N-1}\);
2. the full operation has carrier automorphism group \(C_2\);
3. after one boundary anchor, the full operation becomes rigid;
4. the corresponding Value-Rigidity Indices are

\[
\frac{(N-1)!}{2}
\quad\text{and}\quad
2(N-1)!,
\]

respectively.

Thus a fixed two-element anonymous output alphabet can induce unbounded — indeed factorial — rigidity relative to operation definedness.

## 13. What is and is not being claimed

The construction **does** show:

\[
\boxed{
\text{bounded output alphabet}
\not\Rightarrow
\text{bounded value-induced rigidity}.
}
\]

It does **not** show that two output values encode arbitrary structures, nor that ordinary arithmetic has been reconstructed.

The G4-C coloring imports the external total orientation of the fixed carrier. That is a carrier-geometry import, not an internally generated arithmetic operation.

It also does not establish novelty of the general colored-relation encoding principle; literature positioning remains separate.

## 14. Structural position in the FCOA ladder

The current mechanism ladder becomes

\[
\boxed{
\begin{array}{c}
M0:\ \text{generic exchangeability}\\
\downarrow\\
G1:\ \text{external interaction geometry}\\
\downarrow\\
G2:\ \text{domain-encoded orientation}\\
\downarrow\\
G3:\ \text{anchored value-fiber memory}\\
\downarrow\\
G4:\ \text{bounded-alphabet rigidity amplification}
\end{array}}
\]

G4 is not yet a publication checkpoint. Its exact formulas have been independently enumerated computationally, but the theorem candidate requires hostile audit before promotion to fixed status.
