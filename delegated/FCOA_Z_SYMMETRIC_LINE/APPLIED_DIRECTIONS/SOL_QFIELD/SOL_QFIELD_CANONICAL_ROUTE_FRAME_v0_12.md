# SOL-QFIELD — Generator-Independent Root-Comb Co-occurrence and the Canonical Route Tight Frame

**Version:** 0.12  
**Date:** 2026-09-01  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** ROBUSTNESS RECOVERY / CANONICAL ROUTE METRIC PROVED / CLIFFORD BASIS REMAINS NONCANONICAL  
**Depends on:** `SOL_QFIELD_QUOTIENT_ROBUSTNESS_AUDIT_v0_11.md`

---

## 1. Executive verdict

Version 0.11 found a genuine canonicity defect: the exact depth-two/depth-three Clifford pair of v0.9 is not forced by cardinality minimality alone. It depends on choosing the transposition/transposition, or Coxeter, generating orbit of the minimal reversible history group \(S_3\).

The correct repair is not to privilege another generator pair. Instead, take the **entire family of native root-comb reconvergence residues**.

This produces a robust result.

Let

\[
h:\{L,R\}^*\to S_3
\tag{1}
\]

be any cardinality-minimal reversible history realization satisfying

\[
h(L)h(R)\ne h(R)h(L).
\tag{2}
\]

Define two group elements \(g,g'\in S_3\) to be root-comb co-occurring if there exist two history words \(w,w'\) with the same length and the same number of \(R\)-steps such that

\[
h(w)=g,
\qquad
h(w')=g'.
\tag{3}
\]

Then the co-occurrence graph is independent of the chosen noncommuting generating pair:

\[
\boxed{
\Gamma_{\rm comb}
=
K_3[A_3]
\sqcup
K_3[S_3\setminus A_3].
}
\tag{4}
\]

Thus the six unordered native residue types are exactly the six edges of two disjoint triangles:

1. the even triangle \(\{e,a,a^2\}=A_3\);
2. the odd triangle of the three transpositions.

Every corresponding difference

\[
g-g'
\tag{5}
\]

vanishes in the trivial and sign representations, because \(g,g'\) have the same parity. Hence **every native root-comb residue lies entirely in the standard matrix block**.

More strongly, in the real standard representation the six normalized edge residues form a unit-norm tight frame for

\[
\boxed{M_2(\mathbb R)}
\tag{6}
\]

with frame operator

\[
\boxed{S=\frac32 I.}
\tag{7}
\]

The two parity triangles span orthogonal two-dimensional planes, each carrying the standard \(A_2\) equilateral edge frame.

Therefore the **metric geometry of the full real order sector is generator-independent**, even though a particular orthogonal Clifford basis is not.

This is the robust replacement for the overstrong v0.9 claim.

---

## 2. Root-comb equivalence classes

Recall the root actions

\[
L:x\mapsto x_0\oplus x=x,
\qquad
R:x\mapsto x\oplus x_0=\rho(x)
\tag{8}
\]

on non-root carrier points.

For a history word \(w\), the base endpoint depends only on

\[
r(w)=\#_R(w).
\tag{9}
\]

Thus words with the same pair

\[
(m,r)=(|w|,\#_R(w))
\tag{10}
\]

are natively reconvergent, subject to the usual safe-domain condition preventing the trajectory from reaching the root.

Define

\[
\mathcal W_{m,r}
=
\{w\in\{L,R\}^m:\#_R(w)=r\}.
\tag{11}
\]

The history map \(h\) sends each \(\mathcal W_{m,r}\) to a finite subset of \(S_3\). Co-occurrence records which group-history labels can arise inside the same native reconvergence class.

---

## 3. Definition of the co-occurrence graph

### Definition 3.1

Let \(\Gamma_h\) be the simple graph with vertex set \(S_3\), where distinct \(g,g'\) are adjacent iff there exist \(m,r\) and words

\[
w,w'\in\mathcal W_{m,r}
\tag{12}
\]

such that

\[
h(w)=g,
\qquad
h(w')=g'.
\tag{13}
\]

An edge \(\{g,g'\}\) determines the native route residue line

\[
\mathbb R(g-g')
\tag{14}
\]

in the real group algebra and, after complexification, the line

\[
\mathbb C(g-g')
\tag{15}
\]

in \(\mathbb C[S_3]\).

---

## 4. Parity obstruction: cross-edges are impossible

Let

\[
p=h(L),
\qquad
q=h(R).
\tag{16}
\]

For every word \(w\in\mathcal W_{m,r}\), its sign is

\[
\operatorname{sgn}(h(w))
=
\operatorname{sgn}(p)^{m-r}\operatorname{sgn}(q)^r.
\tag{17}
\]

The right-hand side depends only on \((m,r)\), not on the ordering of the letters.

Therefore all images of one reconvergence class have the same parity.

### Theorem 4.1 — Parity separation

There is no root-comb co-occurrence edge joining an even and an odd element of \(S_3\).

Hence

\[
\Gamma_h
\subseteq
K_3[A_3]\sqcup K_3[S_3\setminus A_3].
\tag{18}
\]

This half of the theorem is completely generator-independent.

---

## 5. Minimal generating-pair orbits

A noncommuting ordered generating pair of \(S_3\) has order type

\[
(2,2),
\qquad
(3,2),
\qquad
(2,3).
\tag{19}
\]

All pairs of a fixed ordered type are equivalent under inner automorphism. Interchanging \(L\) and \(R\) exchanges the last two types and maps the family \(\mathcal W_{m,r}\) to \(\mathcal W_{m,m-r}\).

Therefore, to prove the positive inclusion in (18), it suffices to check two representative realizations:

1. type \((2,2)\);
2. type \((3,2)\).

This is a finite classification, not a numerical experiment.

---

## 6. Coxeter representative: explicit edge witnesses

Take

\[
h(L)=(12),
\qquad
h(R)=(23).
\tag{20}
\]

Write

\[
a=(123),
\qquad
a^2=(132),
\tag{21}
\]

and denote the transpositions by

\[
t_{12},t_{13},t_{23}.
\tag{22}
\]

The following pairs of words belong to common root-comb classes and realize all six same-parity edges:

| Edge | \((m,r)\) | First history | Second history |
|---|---:|---|---|
| \(t_{12}-t_{13}\) | \((3,2)\) | `LRR` | `RLR` |
| \(t_{13}-t_{23}\) | \((3,1)\) | `LLR` | `LRL` |
| \(t_{12}-t_{23}\) | \((5,2)\) | `LLLRR` | `LRLRL` |
| \(a-a^2\) | \((2,1)\) | `LR` | `RL` |
| \(e-a\) | \((4,2)\) | `LLRR` | `RLRL` |
| \(e-a^2\) | \((4,2)\) | `LLRR` | `LRLR` |

Thus every edge of both parity triangles occurs.

---

## 7. Mixed-order representative: explicit edge witnesses

Take

\[
h(L)=(123),
\qquad
h(R)=(12).
\tag{23}
\]

Again all six same-parity edges occur:

| Edge | \((m,r)\) | First history | Second history |
|---|---:|---|---|
| \(t_{12}-t_{13}\) | \((3,1)\) | `LRL` | `RLL` |
| \(t_{12}-t_{23}\) | \((3,1)\) | `LLR` | `LRL` |
| \(t_{13}-t_{23}\) | \((2,1)\) | `LR` | `RL` |
| \(a-a^2\) | \((3,2)\) | `LRR` | `RLR` |
| \(e-a\) | \((4,2)\) | `LRLR` | `RLLR` |
| \(e-a^2\) | \((4,2)\) | `LLRR` | `LRLR` |

The \((2,3)\) case follows by exchanging \(L\) and \(R\).

Combining this table with Theorem 4.1 proves the full classification.

### Theorem 7.1 — Generator-independent co-occurrence graph

For every cardinality-minimal noncommuting \(S_3\) history realization,

\[
\boxed{
\Gamma_h
=
K_3[A_3]\sqcup K_3[S_3\setminus A_3].
}
\tag{24}
\]

Thus the complete set of unordered root-comb residue types is independent of the generator orbit.

---

## 8. Scalar sectors vanish on every native residue

Let \(g\sim g'\) be any co-occurring pair. By Theorem 4.1,

\[
\operatorname{sgn}(g)=\operatorname{sgn}(g').
\tag{25}
\]

In the trivial representation,

\[
\rho_{\rm triv}(g-g')=1-1=0.
\tag{26}
\]

In the sign representation,

\[
\rho_{\rm sign}(g-g')
=
\operatorname{sgn}(g)-\operatorname{sgn}(g')
=0.
\tag{27}
\]

Therefore every root-comb residue lies entirely in the standard block:

\[
\boxed{
g-g'\longmapsto(0,0,D_{g,g'}).}
\tag{28}
\]

This yields a robust strengthening of the earlier single-residue observation: the **entire native root-comb residue family** is supported on the non-Abelian matrix sector.

---

## 9. The canonical real standard block

Before complexification, the real group algebra decomposes as

\[
\mathbb R[S_3]
\cong
\mathbb R
\oplus
\mathbb R
\oplus
M_2(\mathbb R).
\tag{29}
\]

Let

\[
J_{\mathbb R}\cong M_2(\mathbb R)
\tag{30}
\]

be the standard real block.

Equip it with the normalized real Hilbert-Schmidt inner product

\[
\boxed{
\langle X,Y\rangle_{\mathbb R}
:=
\frac12\operatorname{Tr}(X^{\mathsf T}Y).
}
\tag{31}
\]

The standard representation of \(S_3\) is orthogonal, so every group matrix has norm one in (31).

The complex order block is simply

\[
J_{\mathbb R}\otimes_{\mathbb R}\mathbb C
\cong
M_2(\mathbb C).
\tag{32}
\]

This cleanly separates the robust real route geometry from the still-conditional complex coefficient step.

---

## 10. Two equilateral simplices

### Odd triangle

Let

\[
T_1,T_2,T_3
\tag{33}
\]

be the three standard-representation matrices of the transpositions.

Each satisfies

\[
T_i^{\mathsf T}=T_i,
\qquad
T_i^2=I,
\qquad
\|T_i\|=1.
\tag{34}
\]

The transposition class sum acts by zero in the standard irreducible representation, because the standard character on transpositions is zero. Therefore

\[
\boxed{T_1+T_2+T_3=0.}
\tag{35}
\]

By symmetry,

\[
\boxed{
\langle T_i,T_j\rangle_{\mathbb R}=-\frac12
\qquad(i\ne j).
}
\tag{36}
\]

Thus \(T_1,T_2,T_3\) are the vertices of a centered equilateral triangle in a two-dimensional real plane.

### Even triangle

Let

\[
U_0=I,
\qquad
U_1=\rho(a),
\qquad
U_2=\rho(a^2).
\tag{37}
\]

Since \(a^3=e\) and the standard representation contains no \(A_3\)-fixed vector,

\[
\boxed{U_0+U_1+U_2=0.}
\tag{38}
\]

Again

\[
\boxed{
\langle U_i,U_j\rangle_{\mathbb R}=-\frac12
\qquad(i\ne j).
}
\tag{39}
\]

Hence \(U_0,U_1,U_2\) form a second centered equilateral triangle.

---

## 11. Orthogonality of the parity planes

For every transposition \(t\) and every even element \(a^j\),

\[
t^{-1}a^j
\tag{40}
\]

is odd and therefore a transposition.

The standard character on a transposition is zero, so

\[
\begin{aligned}
\langle \rho(t),\rho(a^j)\rangle_{\mathbb R}
&=\frac12\operatorname{Re}\operatorname{Tr}(\rho(t)^*\rho(a^j))\\
&=\frac12\chi_{\rm std}(t^{-1}a^j)\\
&=0.
\end{aligned}
\tag{41}
\]

Therefore the two triangle planes are orthogonal:

\[
\boxed{
V_{\rm odd}\perp V_{\rm even}.
}
\tag{42}
\]

Each has real dimension two, and

\[
\boxed{
J_{\mathbb R}=V_{\rm odd}\oplus V_{\rm even}.
}
\tag{43}
\]

So the parity decomposition of the root-comb graph becomes an orthogonal decomposition of the entire real matrix block.

---

## 12. Normalized edge residues

For every unordered edge \(\{g,g'\}\) in either triangle define

\[
E_{g,g'}
:=
\frac{\rho(g)-\rho(g')}{\sqrt3}.
\tag{44}
\]

Because the vertices in each triangle have norm one and mutual inner product \(-1/2\),

\[
\begin{aligned}
\|\rho(g)-\rho(g')\|^2
&=1+1-2(-1/2)\\
&=3.
\end{aligned}
\tag{45}
\]

Hence

\[
\boxed{\|E_{g,g'}\|=1.}
\tag{46}
\]

There are exactly six such unordered normalized edge lines: three in each parity plane.

---

## 13. Theorem A — each triangle is an \(A_2\) unit-norm tight frame

For a centered equilateral triangle in a two-dimensional Euclidean space, its three normalized edge directions form a unit-norm tight frame with frame bound

\[
\frac32.
\tag{47}
\]

Thus, for either parity plane \(V\),

\[
\boxed{
\sum_{e\in E(V)}
\langle X,E_e\rangle E_e
=
\frac32 X
\qquad
\forall X\in V.
}
\tag{48}
\]

Equivalently, the edge-frame operator is

\[
S_V=\frac32 I_V.
\tag{49}
\]

This is the standard real \(A_2\) root-frame geometry.

---

## 14. Theorem B — full canonical route tight frame

Because the even and odd planes are orthogonal and each has the same frame bound, the union of all six normalized native route residues is a unit-norm tight frame for the full real order block.

### Theorem 14.1 — Canonical Route Tight Frame

Let \(\mathcal E\) be the six unordered co-occurrence edges of \(\Gamma_h\). Then

\[
\boxed{
\sum_{\{g,g'\}\in\mathcal E}
\langle X,E_{g,g'}\rangle_{\mathbb R}
E_{g,g'}
=
\frac32 X
\qquad
\forall X\in J_{\mathbb R}.
}
\tag{50}
\]

Hence

\[
\boxed{S_{\rm route}=\frac32 I_{J_{\mathbb R}}.}
\tag{51}
\]

The result is independent of whether the primitive generator pair is of type \((2,2)\), \((3,2)\), or \((2,3)\).

### Reconstruction formula

Every \(X\in J_{\mathbb R}\) is reconstructed from its route-frame coefficients by

\[
\boxed{
X
=
\frac23
\sum_{\{g,g'\}\in\mathcal E}
\langle X,E_{g,g'}\rangle_{\mathbb R}
E_{g,g'}.
}
\tag{52}
\]

Thus the complete root-comb residue family determines the whole real matrix sector without selecting a basis.

---

## 15. Why this repairs the generator-choice problem

The v0.9 construction chose one depth-two residue and one depth-three residue. Their angle depends on the generator orbit:

- Coxeter \((2,2)\): the chosen pair can be orthogonal;
- mixed \((3,2)\): the analogous direct pair can meet at \(60^\circ\).

The **complete** residue set does not depend on that choice. It is always the same abstract pair of \(A_2\) triangles and always yields the same tight-frame operator.

Therefore the canonical object is not a privileged Pauli basis but

\[
\boxed{
\text{the six-line route frame on }M_2(\mathbb R).
}
\tag{53}
\]

Any orthonormal basis or Clifford pair extracted from that frame requires a further choice, but the metric needed to define orthogonality does not.

---

## 16. Relation to Clifford/CAR

After complexification,

\[
J_{\mathbb R}\otimes\mathbb C
\cong M_2(\mathbb C).
\tag{54}
\]

The route frame therefore guarantees a generator-independent non-Abelian matrix sector with canonical Hilbert-Schmidt geometry.

However:

\[
\boxed{
\text{tight frame}
\not\Rightarrow
\text{canonical ordered Clifford basis}.
}
\tag{55}
\]

The Coxeter realization still gives the exact direct Clifford/CAR construction of v0.9–v0.10 as a useful specialization. In a mixed realization one may orthogonalize route residues inside the canonical metric, but the choice of an ordered orthogonal pair is not uniquely fixed by the full symmetry.

Thus the repaired hierarchy is

\[
\boxed{
\text{root-comb family}
\Rightarrow
\text{canonical route frame / metric}
\Rightarrow
M_2(\mathbb R)
\xrightarrow{\otimes\mathbb C}
M_2(\mathbb C),
}
\tag{56}
\]

with

\[
\boxed{
\text{Coxeter selector}
\Rightarrow
\text{direct Clifford pair}
\Rightarrow
\operatorname{CAR}_1
}
\tag{57}
\]

as a conditional side branch.

---

## 17. What is now robust

The audit/recovery sequence yields the following corrected status.

### Generator-independent within minimal \(S_3\) reversible history

\[
\boxed{
\begin{aligned}
&\Gamma_{\rm comb}=K_3\sqcup K_3,\\
&\text{all route residues vanish in scalar blocks},\\
&\text{route residues span }M_2(\mathbb R),\\
&\text{the six normalized residues form a tight frame},\\
&S_{\rm route}=\frac32 I,\\
&\text{complexification gives }M_2(\mathbb C).
\end{aligned}
}
\tag{58}
\]

### Not generator-independent

\[
\boxed{
\begin{aligned}
&\text{a preferred orthonormal basis},\\
&\text{a preferred ordered Clifford pair},\\
&\text{a preferred CAR creation/annihilation orientation}.
\end{aligned}
}
\tag{59}
\]

This is a cleaner and more conservative theorem boundary than v0.9.

---

## 18. Physical and dimensional verdict

The route tight frame is a finite internal geometry of the history sector. It does not imply physical space, spin, quantum measurement, or fermionic statistics.

The physical verdict remains

\[
\boxed{\texttt{ANALOGY ONLY}.}
\tag{60}
\]

and the line-completion verdict remains

\[
\boxed{\texttt{1D-CLOSED}.}
\tag{61}
\]

---

## 19. Publication assessment

The canonicity defect found in v0.11 is now repaired at the correct level: not by pretending that one Clifford basis is canonical, but by replacing it with a generator-independent tight-frame theorem.

The mathematically robust nucleus is now suitable for a dedicated publication audit.

Recommended publication core:

1. root-comb endpoint theorem;
2. minimal reversible group size six;
3. complete co-occurrence graph \(K_3\sqcup K_3\);
4. scalar-sector annihilation;
5. real standard-block reconstruction;
6. canonical six-edge tight-frame theorem;
7. conditional Coxeter/Clifford/CAR corollary;
8. strict two-mode capacity barrier for the fixed \(S_3\) algebra.

Status:

\[
\boxed{\texttt{PUBLICATION CANDIDATE — NOVELTY/LITERATURE AUDIT REQUIRED}.}
\tag{62}
\]

---

## 20. Next strike

The next task is no longer to generate another operator identity. It is to test **novelty and theorem positioning**:

- which parts are standard facts about \(S_3\), Coxeter groups, \(A_2\) root systems, frame theory, group algebras and CAR;
- which part is genuinely specific to the FCOA root-comb history construction;
- whether the co-occurrence-to-tight-frame theorem is already a known construction under another name;
- whether a shorter abstract formulation exists independent of FCOA terminology.

Only after that audit should the branch move from `PUBLICATION CANDIDATE` to publication assembly.

---

## 21. References

1. `SOL_QFIELD_QUOTIENT_ROBUSTNESS_AUDIT_v0_11.md`.
2. Standard representation theory of \(S_3\).
3. Standard \(A_2\) equilateral root-frame geometry and finite unit-norm tight-frame theory.
4. Standard real and complex group-algebra decompositions of \(S_3\).
5. FCOA-Z v1.1, DOI: https://doi.org/10.5281/zenodo.22169264
