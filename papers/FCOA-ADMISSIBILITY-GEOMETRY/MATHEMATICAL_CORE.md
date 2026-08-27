# FCOA Admissibility Geometry — Mathematical Core

**Publication DOI:** 10.5281/zenodo.22129787  
**Status:** theorem-level companion checkpoint  
**Date:** 2026-08-27

## 1. Carrier and branch discipline

Work on the finite base carrier

\[
X_N=\{P_0,P_1,\ldots,P_N\},\qquad N\ge3,
\]

with indices used only as external labels. The branch construction deliberately distinguishes:

- operation values;
- operation definedness/domain geometry;
- external relational geometry.

No unspecified generic cell is filled by arithmetic extrapolation.

## 2. Branch M0

### Addition core

For \(1\le i\le N\):

\[
P_0\oplus P_i=P_i,
\qquad
P_i\oplus P_0=P_{i-1},
\qquad
P_i\oplus P_i=E_i^+.
\]

All other cells are undefined, including \(P_0\oplus P_0\).

Consequences:

\[
\operatorname{Aut}(X_N,\oplus)=1.
\]

The commutation locus is

\[
\operatorname{Comm}_\oplus
=
\{(P_i,P_i):1\le i\le N\}.
\]

The unique two-valued NEQ associativity witness is

\[
(P_1,P_0,P_1),
\]

because

\[
(P_1\oplus P_0)\oplus P_1=P_1
\]

while

\[
P_1\oplus(P_0\oplus P_1)=E_1^+.
\]

The exact Association Spectrum on \((X_N)^3\) is

\[
\begin{aligned}
EQ &= N-1,\\
NEQ &= 1,\\
LEFT &= 4N-2,\\
RIGHT &= 4N-2,\\
NONE &= (N+1)^3-9N+4.
\end{aligned}
\]

### Multiplication core

For \(1\le i\le N\):

\[
P_0\otimes P_i=P_0.
\]

For \(2\le i\le N\):

\[
P_i\otimes P_0=E_i^\ast,
\]

\[
P_1\otimes P_i=P_i\otimes P_1=P_i,
\]

\[
P_i\otimes P_i=E_i^\times.
\]

All remaining cells are undefined, in particular

\[
P_0\otimes P_0,
\quad
P_1\otimes P_0,
\quad
P_1\otimes P_1.
\]

Let

\[
G_N=\{P_2,\ldots,P_N\}.
\]

Then

\[
\operatorname{Aut}(\mathfrak M_N^\times)\cong S_{N-1},
\]

because \(P_0,P_1\) are fixed by their operational roles, while every permutation of \(G_N\) extends by

\[
E_i^\ast\mapsto E_{\pi(i)}^\ast,
\qquad
E_i^\times\mapsto E_{\pi(i)}^\times.
\]

The M0 commutation locus is

\[
\operatorname{Comm}_\otimes
=
\{(P_i,P_i):2\le i\le N\}
\cup
\{(P_1,P_i),(P_i,P_1):2\le i\le N\},
\]

hence

\[
|\operatorname{Comm}_\otimes|=3(N-1).
\]

The exact M0 Association Spectrum is

\[
\begin{aligned}
EQ &= 4(N-1),\\
NEQ &= 0,\\
LEFT &= N^2+2N-2,\\
RIGHT &= N^2+N-2,\\
NONE &= N^3+N^2-4N+9.
\end{aligned}
\]

The multiplication branch therefore has no two-valued NEQ witness, but it fails strong partial associativity through definedness asymmetry.

## 3. Role distinguishability versus rigidity

For both operations, the left and right translation families are injective on the base sort \(X_N\):

\[
P_i\mapsto L_{P_i}^\star,
\qquad
P_i\mapsto R_{P_i}^\star.
\]

For \(\otimes\), this coexists with

\[
\operatorname{Aut}(\mathfrak M_N^\times)\cong S_{N-1}.
\]

Thus

\[
\boxed{
\text{role distinguishability}
\neq
\text{structural rigidity}
}
\]

is an explicit feature of M0.

## 4. Branch G1 — external geometry

Let \(A\subseteq G_N^2\) be a separately named binary relation. The operation table remains M0.

### Automorphism-transfer proposition

For every such \(A\),

\[
\operatorname{Aut}(\mathfrak M_N^\times,A)
\cong
\operatorname{Aut}(G_N,A).
\]

Proof: M0 fixes \(P_0,P_1\), leaves every permutation of \(G_N\) available, and forces the induced permutation of the \(E\)-outputs. Adding \(A\) therefore restricts exactly to the automorphism group of \((G_N,A)\).

For the undirected path

\[
P_2-P_3-\cdots-P_N,
\]

the group is \(C_2\). For the directed path

\[
P_2\to P_3\to\cdots\to P_N,
\]

the group is trivial. Hence

\[
S_{N-1}\longrightarrow C_2\longrightarrow1.
\]

However, erasing \(A\) restores \(S_{N-1}\). Therefore G1 supplies **external rigidity**, not internal memory of the operation.

Because \(A\) is separate from \(\otimes\), adding it does not change the operation-based translation profiles, commutation locus, or Association Spectrum.

## 5. Branch G2 — domain compilation

Introduce one fresh terminal output \(\Omega\), with no products defined when \(\Omega\) is used as an argument. Add exactly

\[
P_i\otimes_1P_{i+1}=\Omega,
\qquad
2\le i<N.
\]

Reverse and non-adjacent generic cells remain undefined.

### Rigidity theorem

For every \(N\ge3\),

\[
\boxed{
\operatorname{Aut}(\otimes_1)=1.
}
\]

Reason: the off-diagonal generic definedness pattern is exactly the directed path

\[
P_2\to P_3\to\cdots\to P_N,
\]

which is rigid. M0 already fixes \(P_0,P_1\), and the remaining output elements are then forced.

### Recoverability of directed adjacency

After erasing any external symbol \(A_{\rm dir}\), the relation remains recoverable from the reduct:

\[
A_{\rm dir}(x,y)
\iff
x,y\in G_N,\ x\ne y,\ \operatorname{Def}(x\otimes_1y).
\]

Equivalently, once \(\Omega\) is internally separated as the terminal G2 output,

\[
A_{\rm dir}(x,y)
\iff
x,y\in G_N,\ x\otimes_1 y=\Omega.
\]

This is uniform across the finite family \(N\ge3\). It recovers directed adjacency, not automatically a uniformly first-order definable transitive closure/full linear order in an infinite limit.

## 6. Exact G2 invariants

The commutation locus is unchanged from M0:

\[
\operatorname{Comm}_{\otimes_1}
=
\operatorname{Comm}_{\otimes},
\]

so

\[
|\operatorname{Comm}_{\otimes_1}|=3(N-1).
\]

The exact G2 Association Spectrum on \((X_N)^3\) is

\[
\begin{aligned}
EQ &= 5N-6,\\
NEQ &= 0,\\
LEFT &= N^2+3N-4,\\
RIGHT &= N^2+2N-4,\\
NONE &= N^3+N^2-7N+15.
\end{aligned}
\]

The new G2 EQ family is

\[
(P_i,P_1,P_{i+1}),
\qquad 2\le i<N,
\]

because both bracketings equal \(\Omega\).

Each compiled edge contributes exactly one new EQ, one new LEFT, and one new RIGHT triple relative to M0, while \(NEQ\) remains zero.

Thus the automorphism group changes maximally

\[
S_{N-1}\to1
\]

without any change in commutation locus and without creating a two-valued NEQ associativity witness.

## 7. Typed Domain Compilation Theorem

Let \(G\) be an input sort and let \(O=\{\Omega\}\) be a singleton output sort. Let \(A\subseteq G^2\). Define

\[
\star_A:G\times G\rightharpoonup O
\]

by

\[
x\star_Ay=\Omega
\iff
A(x,y),
\]

with all other cells undefined.

Then restriction to \(G\) induces a canonical isomorphism

\[
\boxed{
\operatorname{Aut}(G,O;\star_A)
\cong
\operatorname{Aut}(G;A).
}
\]

### Proof

Every automorphism preserves sorts, hence fixes the unique element \(\Omega\in O\). Since

\[
A(x,y)
\iff
\operatorname{Def}(x\star_Ay),
\]

its restriction to \(G\) preserves \(A\). Conversely, every automorphism of \((G,A)\) extends uniquely by fixing \(\Omega\).

### One-sorted caveat

If one instead works on the one-sorted carrier \(G\sqcup\{\Omega\}\), the unqualified theorem fails when \(A=\varnothing\), because the operation is nowhere defined and \(\Omega\) need not be structurally distinguished from the unused input elements. The typed singleton-output formulation avoids this defect even for the empty relation.

## 8. Claim boundaries

The branch establishes:

- finite rigidity results;
- exact automorphism groups for M0, G1 and G2;
- exact commutation loci and Association Spectra;
- injectivity of base-indexed left/right translations;
- uniform recovery of directed adjacency in G2;
- typed domain compilation of an arbitrary binary relation into a constant-valued partial operation.

It does not establish:

- that the full linear order on an infinite carrier is uniformly first-order definable from successor alone;
- that the broad classes of partial algebra, many-sorted algebra, conditional operations, or left/right translations are new;
- any automatic connection to ordinary arithmetic on the external indices.

The central structural distinction is

\[
\boxed{
\text{external geometry}
\to
\text{external rigidity}
\to
\text{geometry compiled into the operation domain}
\to
\text{internal recoverable memory}.
}
\]
