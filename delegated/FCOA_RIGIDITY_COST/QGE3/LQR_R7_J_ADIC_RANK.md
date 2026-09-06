# QGE3 LQR — J-adic Rank Collapse and Syndrome Compression at r=7

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** active structural continuation  
**Scope:** pure defect-two synchronization at `r=7`  
**Proof status:** analytic for the `J^2` rank-collapse theorem; syndrome-degree bound remains conjectural but strongly verified

This note continues `LQR_R7_XOR_CIRCULANT.md`. The purpose is to isolate the first genuinely useful consequence of the augmentation filtration

\[
J\supset J^2\supset J^3\supset\cdots
\]

for the fifteen-plane parity barrier.

---

## 1. Group algebra and the syndrome map

Let

\[
V=\mathbb F_2^6,
\qquad
A=\mathbb F_2[V]
\cong
\mathbb F_2[t_1,\dots,t_6]/(t_1^2,\dots,t_6^2).
\]

Write

\[
J=(t_1,\dots,t_6)
\]

for the augmentation ideal.

For an oriented fifteen-line system with parent points

\[
P=\{p_1,\dots,p_{15}\}\subset V\setminus\{0\},
\]

and a coefficient vector

\[
z=(z_1,\dots,z_{15}),
\]

put

\[
g(z)=\sum_{a=1}^{15} z_a T_{p_a}\in A.
\]

Its augmentation and linear `J/J^2` part are

\[
\ell_0(z)=\sum_a z_a,
\qquad
\ell(z)=\sum_a z_a p_a\in V.
\]

Thus

\[
\boxed{
g(z)\in J^2
\iff
\ell_0(z)=0,\quad \ell(z)=0.}
\]

For Boolean `z=1_S`, this is

\[
|S|\equiv0\pmod2,
\qquad
\bigoplus_{p\in S}p=0.
\]

The seven linear syndromes define a map

\[
\sigma:\mathbb F_2^{15}\to\mathbb F_2^7,
\qquad
\sigma(S)=\left(|S|\bmod2,\ \bigoplus_{p\in S}p\right).
\]

Whenever the parent points span `V`, the kernel has dimension eight.

---

## 2. Rank collapse inside J^2

### Theorem 2.1 — six-variable `J^2` rank bound

Let

\[
0\ne g\in J^2\subset A.
\]

Then multiplication by `g` on the 64-dimensional regular module satisfies

\[
\boxed{\operatorname{rank}m_g\le28.}
\]

### Proof
Use the degree filtration

\[
A=A_0\oplus A_1\oplus\cdots\oplus A_6,
\qquad
\dim A_k=\binom6k.
\]

Write

\[
g=g_2+g_3+\cdots+g_6,
\qquad
g_j\in A_j,
\]

where `g_2` may be zero.

Since `g in J^2`, multiplication raises degree by at least two. On the associated graded module the only possible source degrees are `0,1,2,3,4`, giving the crude rank bound

\[
1+6+15+7+1=30.
\]

The middle contribution

\[
A_2\longrightarrow A_4
\]

is multiplication by the quadratic initial part `g_2`. If `g_2=0`, its rank is zero and the total bound is already below 30. If `g_2\ne0`, then in characteristic two

\[
g_2^2=0,
\]

because every basis monomial in degree two squares to zero and all mixed products occur twice. Hence

\[
g_2\in\ker\left(A_2\xrightarrow{\cdot g_2}A_4\right),
\]

so this middle map has rank at most 14. Therefore

\[
\operatorname{rank}m_g\le
1+6+14+7+1=29.
\]

Finally `m_g` is represented in the group basis by an alternating matrix: every nonzero translation has zero diagonal, and the zero-augmentation condition removes the identity term. An alternating matrix over `F_2` has even rank. Thus

\[
\operatorname{rank}m_g\le28.
\]
\(\square\)

---

## 3. Consequence for the child Pfaffian

Let `C` be the 30 child points and let

\[
G_C(z)
\]

be the `30 x 30` principal child minor of the translation circulant.

### Corollary 3.1
If

\[
\ell_0(z)=0,
\qquad
\ell(z)=0,
\]

then

\[
\boxed{
\operatorname{Pf}G_C(z)=0.
}
\]

### Proof
The full multiplication operator has rank at most 28 by Theorem 2.1, so every 30 by 30 minor is singular. Since `G_C(z)` is alternating,

\[
\det G_C(z)=\operatorname{Pf}(G_C(z))^2=0,
\]

hence the Pfaffian vanishes. \(\square\)

This is a polynomial statement, not merely a Boolean one: the child Pfaffian vanishes on the entire codimension-seven linear subspace

\[
\ell_0=\ell_1=\cdots=\ell_6=0
\]

over every characteristic-two extension field.

Equivalently,

\[
\boxed{
\operatorname{Pf}G_C(z)
\in
(\ell_0,\ell_1,\dots,\ell_6).
}
\]

---

## 4. Boolean kernel-code elimination

For Boolean subsets `S subseteq P`, define

\[
f_C(S)=\operatorname{Pf}(G_S)_C\in\mathbb F_2.
\]

Then every subset in the eight-dimensional kernel code

\[
K=\ker\sigma
=
\left\{
S:\ |S|\equiv0\pmod2,\ \bigoplus_{p\in S}p=0
\right\}
\]

satisfies

\[
\boxed{f_C(S)=0.}
\]

Thus 256 of the 32768 Boolean subset evaluations disappear for structural reasons before any resolution counting is performed.

More importantly, the parity problem can be compressed along the cosets of `K`.

Define the syndrome aggregate

\[
F(\tau)
=
\bigoplus_{S:\,\sigma(S)=\tau} f_C(S),
\qquad
\tau\in\mathbb F_2^7.
\]

Then the desired full rainbow parity is simply

\[
\boxed{
\bigoplus_{S\subseteq P}f_C(S)
=
\bigoplus_{\tau\in\mathbb F_2^7}F(\tau).
}
\]

So the final fifteen-variable top coefficient is reduced to a seven-variable Boolean function.

---

## 5. Observed syndrome-degree collapse

For arbitrary oriented compatible fifteen-line partial spreads tested to date, the syndrome function `F` has algebraic-normal-form degree at most five:

\[
\boxed{
\deg_{\rm ANF}F\le5
}
\]

in every tested case.

This is substantially stronger than the formal derivative bound

\[
\deg F\le7
\]

coming only from summing a fifteen-variable function over an eight-dimensional kernel.

Representative random tests repeatedly produced degree exactly five.

If the bound

\[
\deg F\le6
\]

can be proved in general, then the total XOR over the seven-dimensional syndrome cube vanishes automatically. The empirically stronger degree-five statement would therefore more than suffice.

### Syndrome-Degree Conjecture
For every oriented compatible fifteen-line partial spread in `PG(5,2)`,

\[
\boxed{\deg_{\rm ANF}F\le5.}
\]

This conjecture implies the fifteen-line parity theorem and hence, in the partition-realizable LQR sector,

\[
M_7=14.
\]

---

## 6. Why this is the correct next barrier

The previous approaches attacked the full resolution hypergraph or the full mixed Pfaffian coefficient. The `J^2` theorem removes an eight-dimensional family of subset states and exposes a much smaller quotient problem.

The remaining task is now:

\[
\boxed{
\text{explain the extra two degrees of ANF collapse on }\mathbb F_2^7.
}
\]

A likely source is the interaction between:

1. the `J^2` rank defect;
2. the complementary identity
   \[
   \operatorname{Pf}G_D=s^2\operatorname{Pf}G_C;
   \]
3. the fact that the 15 canonical projective lines are pairwise point-disjoint;
4. the special dimensions
   \[
   |V|=64,\quad |C|=30,\quad |D|=34.
   \]

The next proof attack should therefore be directed at the quotient syndrome function rather than at individual obstruction cores.

---

## 7. Computational cross-checks

Independent experiments used the exact determinant/Pfaffian parity formula and gave the following persistent pattern:

```text
q=13 : ANF degree may reach 13
q=14 : ANF degree may reach 14
q=15 : all tested systems have child-Pfaffian ANF degree <=13
        and syndrome-aggregate degree <=5
```

Thus the algebraic drop appears exactly at the fifteen-line threshold.

These observations are evidence only; the only theorem claimed in this note beyond the previously established circulant identities is the `J^2` rank-collapse theorem and its vanishing corollary.

---

## 8. Rigorous status

The exact numerical status remains

\[
\boxed{14\le M_7\le21.}
\]

The new theorem does not yet prove `M_7=14`, but it reduces the unresolved parity mechanism from fifteen Boolean variables to a seven-dimensional syndrome quotient and supplies the first analytic rank reason for the observed parity collapse.
