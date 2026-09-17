# QGE3 LQR — Tangent–Socle Theorem on the J^2 Pfaffian Locus

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** active structural continuation  
**Scope:** local algebra behind the r=7 fifteen-plane Pfaffian barrier

This note isolates the local algebraic mechanism behind the observed vanishing of tangent kernel forms on the syndrome-zero locus.

---

## 1. The algebra

Let

\[
A=\mathbb F_2[t_1,\dots,t_6]/(t_1^2,\dots,t_6^2),
\qquad J=(t_1,\dots,t_6).
\]

Via `T_{e_i}=1+t_i`, this is the group algebra `F_2[F_2^6]`.

Let

\[
\lambda:A\to\mathbb F_2
\]

be the coefficient of the identity group element `T_0`. In the `t`-monomial basis,

\[
\boxed{\lambda(t_S)=1\quad\text{for every }S\subseteq[6].}
\]

Thus

\[
\langle a,b\rangle=\lambda(ab)
\]

is the symmetric Frobenius pairing corresponding to the standard dot product in the group basis.

The socle is

\[
\operatorname{Soc}(A)=J^6=\langle t_1t_2t_3t_4t_5t_6\rangle.
\]

Since `J` has codimension one and every socle element annihilates `J`,

\[
\boxed{J^\perp=J^6.}
\]

---

## 2. Symplectic normal form

Consider

\[
q=t_1t_2+t_3t_4+t_5t_6.
\]

Multiplication by `q` has rank `28` and kernel dimension `36`.

The graded kernels of

\[
L_q:A_k\to A_{k+2},\qquad x\mapsto qx
\]

have dimensions

\[
0,0,1,14,14,6,1
\]

in degrees `0,1,2,3,4,5,6`, respectively. In particular,

\[
\ker L_q\cap A_2=\langle q\rangle,
\]

and there are no kernel elements in degrees zero or one.

### Theorem 2.1 — annihilator-square theorem

\[
\boxed{\operatorname{Ann}(q)^2=J^6.}
\]

### Proof
Let `x,y in Ann(q)` and decompose them by degree.

Because the kernel has no degree-zero or degree-one part, both start in degree at least two. Their degree-two components are scalar multiples of `q`.

The degree-four component of `xy` is therefore a scalar multiple of

\[
q^2=0.
\]

The degree-five component is a sum of terms of the form

\[
qz
\]

with `z in Ann(q) cap A_3`, hence also vanishes.

Every component of degree greater than six is zero in `A`. Thus

\[
xy\in A_6=J^6.
\]

So `Ann(q)^2 subseteq J^6`.

The inclusion is nonzero: the two kernel elements

\[
x=t_1t_3t_5,
\qquad
y=t_2t_4t_6
\]

satisfy `qx=qy=0` and

\[
xy=t_1t_2t_3t_4t_5t_6\ne0.
\]

Hence equality holds. \(\square\)

---

## 3. Generic rank-28 elements of J^2

Let `g in J^2` have nondegenerate quadratic initial part. As established in `LQR_R7_J_ADIC_RANK.md`, an algebra automorphism carries `g` to the symplectic normal form `q`.

Algebra automorphisms preserve annihilators and the one-dimensional socle. Therefore:

### Theorem 3.1 — generic tangent–socle theorem

For every `g in J^2` with nondegenerate quadratic initial part,

\[
\boxed{\operatorname{Ann}(g)^2=J^6.}
\]

In particular `rank(m_g)=28`.

---

## 4. Tangent kernel forms vanish

Let `h in J^2`. For `x,y in Ann(g)`, using associativity and the Frobenius pairing,

\[
\langle x,m_hy\rangle
=\lambda(xhy)
=\lambda(hxy).
\]

By Theorem 3.1,

\[
xy\in J^6.
\]

Since `h in J^2 subseteq J` and `J^6 J=0`,

\[
\lambda(hxy)=0.
\]

Therefore:

### Corollary 4.1 — tangent-zero theorem

For generic rank-28 `g in J^2` and every tangent direction `h in J^2`, the alternating bilinear form induced by `m_h` on the radical of `m_g` vanishes identically:

\[
\boxed{
\langle x,m_hy\rangle=0
\quad\forall x,y\in\ker m_g.
}
\]

Thus the first-order variation of the Pfaffian kernel geometry along the `J^2` locus is zero. Only directions normal to the seven syndrome equations can contribute to the induced kernel forms.

This gives an analytic explanation for the experimentally observed factorization of the local Pfaffian geometry through the seven-dimensional syndrome quotient.

---

## 5. Consequence for the r=7 programme

For the fifteen-parent translation family, the syndrome-zero coefficient space is exactly

\[
K_P=\operatorname{span}\{T_p:p\in P\}\cap J^2.
\]

At a generic point `g in K_P` with rank `28`, all tangent directions inside `K_P` induce zero forms on the full radical. Consequently, after passage to a complementary principal minor with the same rank, the nontrivial first-order kernel forms factor through the seven syndrome-normal directions.

This result does **not** by itself prove the vanishing of the top squarefree coefficient

\[
[z_1\cdots z_{15}]\operatorname{Pf}G_C.
\]

The remaining task is to identify the additional relation among the seven normal kernel forms that kills the degree-seven syndrome coefficient.

---

## 6. Degree-14 clarification

Let

\[
P_C(z)=\operatorname{Pf}G_C(z)
\]

be homogeneous of degree `15`. Every perfect-matching monomial

\[
\prod_i z_i^{m_i}
\]

satisfies

\[
\sum_i m_i\equiv1\pmod2,
\qquad
\sum_i(m_i\bmod2)p_i=\bigoplus_{c\in C}c.
\]

In the balanced canonical case

\[
\bigoplus C=\bigoplus P,
\]

so the parity vector `(m_i mod 2)` has the same seven-dimensional syndrome as the all-ones vector.

A Boolean monomial of support `14` in a homogeneous degree-15 polynomial would necessarily have one exponent `2`, one exponent `0`, and all other exponents `1`. Its exponent-parity vector would therefore differ from the all-ones vector in exactly two coordinates. That would give a weight-two word in `ker sigma`, impossible because the parent points are distinct.

Hence, independently of the unresolved top coefficient,

\[
\boxed{
\text{the Boolean degree-14 layer is identically zero.}
}
\]

Therefore once the degree-15 squarefree coefficient is shown to vanish, the Boolean Pfaffian degree drops immediately to at most `13`, and the previously observed syndrome degree at most `5` follows from the eight-dimensional fiber summation. It should not be treated as an independent barrier.

---

## 7. Rigorous status

The tangent–socle theorem, tangent-zero corollary, and degree-14 exclusion are analytic results. The final fifteen-plane parity theorem remains open.

The rigorous LQR bound remains

\[
\boxed{14\le M_7\le21.}
\]
