# QGE3 LQR — Generic Hyperplane Split and Block-Pfaffian Reduction

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** active continuation after exceptional-case closure  
**Scope:** compatible pure defect-two fifteen-plane families on seven phases  
**Proof status:** analytic reduction theorem; final parity vanishing in the generic regime remains open

---

## 1. Setup

Let

\[
V=\mathbb F_2^6,
\]

and let an oriented fifteen-line system have parent set

\[
P=\{p_1,\dots,p_{15}\}
\]

and child set

\[
C,
\qquad |C|=30.
\]

Fix a hyperplane

\[
H=\ker\alpha
\]

and write the two affine cosets as

\[
V=H\sqcup(H+e).
\]

Let

\[
I=P\cap H,
\qquad X=P\setminus H,
\qquad k=|I|.
\]

Let

\[
m=m_H
\]

be the number of canonical projective lines lying entirely in `H`.

The generic regime isolated in `LQR_R7_EXCEPTIONAL_CODE_THEOREM.md` is

\[
\boxed{m\le2.}
\]

---

## 2. Child counts in the two cosets

### Proposition 2.1
The child-set sizes are

\[
\boxed{|C\cap H|=15-k+2m}
\]

and

\[
\boxed{|C\cap(H+e)|=15+k-2m.}
\]

### Proof
A canonical line contributes according to its position and parent type.

1. A line contained in `H` contributes two children to `H`; there are `m` such lines.
2. A line not contained in `H` but whose parent lies in `H` has its two children in `H+e`; there are `k-m` such lines.
3. A line whose parent lies outside `H` has one child in each coset; there are `15-k` such lines.

Therefore

\[
|C\cap H|=2m+(15-k),
\]

\[
|C\cap(H+e)|=2(k-m)+(15-k).
\]
\(\square\)

---

## 3. Fixed internal-edge counts in every resolution

Consider any additive/XOR resolution of the same parent-child system.

A color `p in I` preserves the two cosets, so its matching edge is internal to one coset. A color `p in X` swaps the cosets, so its matching edge is crossing.

Let

\[
a_H
\]

be the number of internal matching edges lying in `H`, and let

\[
a_1
\]

be the number of internal matching edges lying in `H+e`.

### Theorem 3.1 — hyperplane profile rigidity
Every resolution satisfies

\[
\boxed{a_H=m,\qquad a_1=k-m.}
\]

### Proof
All `15-k` colors in `X` are crossing, so the number of crossing edges is fixed:

\[
c=15-k.
\]

Counting child vertices in `H` gives

\[
2a_H+c=|C\cap H|.
\]

Using Proposition 2.1,

\[
2a_H+(15-k)=15-k+2m,
\]

so

\[
a_H=m.
\]

Since the total number of internal colors is `k`,

\[
a_1=k-a_H=k-m.
\]
\(\square\)

This theorem is crucial: the canonical value `m_H` is not merely a property of the canonical resolution. It is forced in every resolution by the hyperplane grading.

---

## 4. Block form of the color-weighted Pfaffian matrix

Order the child vertices as

\[
C_0=C\cap H,
\qquad
C_1=C\cap(H+e).
\]

Let

\[
A(z_I)
\]

be the internal adjacency block on `C_0`,

\[
D(z_I)
\]

the internal adjacency block on `C_1`, and

\[
B(z_X)
\]

the crossing block.

Then the child translation matrix has block form

\[
G_C(z)=
\begin{pmatrix}
A(z_I)&B(z_X)\\
B(z_X)^T&D(z_I)
\end{pmatrix}
\]

over characteristic two.

The two internal blocks use only the variables indexed by `I`; the crossing block uses only the variables indexed by `X`.

---

## 5. Pfaffian minor-summation identity

For subsets

\[
S\subseteq C_0,
\qquad T\subseteq C_1,
\]

write `A_S` and `D_T` for the corresponding principal submatrices and

\[
B_{C_0\setminus S,\,C_1\setminus T}
\]

for the residual crossing minor.

Over `F_2`, the standard Pfaffian block expansion gives

\[
\boxed{
\operatorname{Pf}G_C
=
\sum_{S,T}
\operatorname{Pf}A_S\;
\operatorname{Pf}D_T\;
\det B_{C_0\setminus S,\,C_1\setminus T},
}
\]

where the sum runs over even `|S|,|T|` for which the residual row and column sizes agree.

For the full squarefree color coefficient, Theorem 3.1 forces exactly

\[
|S|=2m,
\qquad
|T|=2(k-m).
\]

Thus all other block terms are irrelevant to the rainbow-resolution parity.

---

## 6. Exact top-coefficient formula

Let

\[
R=[\prod_{p\in P}z_p]\operatorname{Pf}G_C
\in\mathbb F_2
\]

be the resolution parity.

For `J subseteq I`, write

\[
z_J=\prod_{p\in J}z_p.
\]

Then

\[
\boxed{
\begin{aligned}
R
=&\sum_{\substack{S\subseteq C_0\\|S|=2m}}
  \sum_{\substack{T\subseteq C_1\\|T|=2(k-m)}}
  \sum_{\substack{J\subseteq I\\|J|=m}}
  [z_J]\operatorname{Pf}A_S\\
&\qquad\cdot
  [z_{I\setminus J}]\operatorname{Pf}D_T\\
&\qquad\cdot
  [z_X]\det B_{C_0\setminus S,\,C_1\setminus T}.
\end{aligned}
}
\tag{6.1}
\]

Formula (6.1) is an exact decomposition of the global parity into bipartite prescribed-difference determinant coefficients with boundary data supplied by the internal edges.

---

## 7. Why the generic regime is small

If

\[
m\le2,
\]

then the internal `H`-side Pfaffian has size at most four.

### Case `m=0`

No internal edge occurs on the `H` side. The `A` factor is `1`, and the parity reduces to crossing determinant coefficients after choosing the forced `k` internal edges on the other side.

### Case `m=1`

The `H`-side contribution is one edge. For a two-vertex set

\[
S=\{x,y\},
\]

and color `p`,

\[
[z_p]\operatorname{Pf}A_S=1
\iff
x+y=p.
\]

Thus the only boundary datum on the `H` side is a single prescribed internal edge.

### Case `m=2`

The `H`-side contribution is a four-vertex Pfaffian. Its squarefree two-color coefficient is the parity of the at most three pairings of those four vertices using the chosen two internal colors.

Hence the generic case involves only zero-, one-, and two-edge boundary conditions on one side of the hyperplane.

---

## 8. Relation to the two-hole prescribed-difference method

Aryeh Lev Zabokritskiy, “Perfect Matchings with Prescribed Differences Beyond Hall: The Two-Hole Problem,” arXiv:2607.08630 (2026), proves the binary two-hole prescribed-difference problem by a character-minor method using group circulants, Walsh-Hadamard diagonalization, complementary minors, and exact `2`-adic noncancellation.

The present formula (6.1) reaches the same **boundary scale**: at most two internal edges occur on the `H` side.

However, the theorem from that paper does **not** apply verbatim here. Our residual crossing matrices are minors supported on the child subsets

\[
C_0\setminus S,
\qquad
C_1\setminus T,
\]

rather than punctured copies of an entire affine hyperplane. Therefore what transfers directly is the character-minor mechanism, not the final two-hole theorem as a black box.

The next target is to derive a parity identity for the sum in (6.1), using the common Walsh-Hadamard diagonalization of all crossing translations.

---

## 9. Computational stress test of the boundary decomposition

Exact resolution recursion on random compatible fifteen-plane families with `m<=2` shows the following consistent pattern:

- individual boundary assignments `J` can have odd completion parity;
- the total XOR over all admissible boundary assignments is nevertheless zero in all tested families;
- for `m=1`, examples occur with exactly two odd one-edge boundary choices;
- for `m=2`, examples occur with `2,4,6,8,10,...` odd two-edge boundary choices.

Thus the missing theorem is not that every determinant term in (6.1) vanishes separately. The cancellation occurs **between boundary patterns**.

This rules out an overly local determinant-vanishing strategy and points instead to a global character-minor identity across the sum over `J,S,T`.

---

## 10. Remaining generic-case barrier

After the coding-theory closure of the hyperplane-dense exceptional regime, the only unresolved geometric regime is

\[
\boxed{\exists H:\ m_H\le2.}
\]

For such an `H`, the global resolution parity is exactly the boundary-minor sum (6.1) with an `H`-side boundary of size at most four vertices.

The next proof target is therefore:

\[
\boxed{
\text{prove that the full boundary sum in (6.1) is zero in }\mathbb F_2.
}
\]

A promising route is a Walsh/character expansion of the residual determinants, followed by a boundary summation identity analogous to the noncancellation mechanism in the binary two-hole problem.

The LQR extremal status remains

\[
\boxed{14\le M_7\le21.}
\]

until this generic parity cancellation and the exceptional PDS parity are both closed analytically.
