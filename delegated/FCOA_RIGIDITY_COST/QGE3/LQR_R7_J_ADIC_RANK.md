# QGE3 LQR — J-adic Rank Collapse, Child Corank Four, and Syndrome Compression at r=7

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** active structural continuation  
**Scope:** pure defect-two synchronization at `r=7`  
**Proof status:** analytic for the `J^2` rank-collapse and child-corank-four theorems; syndrome-degree bound remains conjectural but strongly verified

This note continues `LQR_R7_XOR_CIRCULANT.md`. It records the augmentation-filtration mechanism behind the first two orders of the observed Pfaffian collapse at the fifteen-plane threshold.

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

For a parent set

\[
P=\{p_1,\dots,p_{15}\}\subset V\setminus\{0\}
\]

and a coefficient vector `z`, put

\[
g(z)=\sum_{a=1}^{15}z_aT_{p_a}\in A.
\]

Its augmentation and its class modulo `J^2` are

\[
\ell_0(z)=\sum_a z_a,
\qquad
\ell(z)=\sum_a z_ap_a\in V.
\]

Thus

\[
\boxed{
g(z)\in J^2
\iff
\ell_0(z)=0,\quad \ell(z)=0.}
\]

For Boolean `z=1_S`, this says

\[
|S|\equiv0\pmod2,
\qquad
\bigoplus_{p\in S}p=0.
\]

The seven syndromes define

\[
\sigma:\mathbb F_2^{15}\to\mathbb F_2^7,
\qquad
\sigma(S)=\left(|S|\bmod2,\ \bigoplus_{p\in S}p\right).
\]

When the parents span `V`, `ker sigma` has dimension eight.

---

## 2. Correct six-variable J^2 rank theorem

### Theorem 2.1 — full regular-module rank collapse

For every

\[
g\in J^2\subset A,
\]

multiplication by `g` on the 64-dimensional regular module satisfies

\[
\boxed{\operatorname{rank}m_g\le28.}
\]

### Proof
We work first over an algebraic closure of `F_2`; the final rank inequality then descends to every specialization over `F_2`.

Write

\[
g=q+g_3+\cdots+g_6,
\qquad q\in A_2.
\]

Consider the Zariski-open locus on which the quadratic part `q` is a nondegenerate alternating 2-form. After an invertible linear change of the six generators we may assume

\[
q=t_1t_2+t_3t_4+t_5t_6.
\tag{2.1}
\]

We first remove all higher-degree terms by an automorphism tangent to the identity. Suppose terms of degrees `<k` have already been reduced to `q`. Replace

\[
t_i\longmapsto t_i+a_i,
\qquad a_i\in A_{k-1},
\]

with `k>=3`. Because every element of the maximal ideal has square zero under Frobenius, such substitutions respect the relations `t_i^2=0`; their linear part is the identity, so they are algebra automorphisms.

To degree `k`, the change of `q` is

\[
\sum_{i=1}^6 \frac{\partial q}{\partial t_i}a_i.
\]

For the symplectic normal form (2.1), the six derivatives are

\[
t_2,t_1,t_4,t_3,t_6,t_5.
\]

The map

\[
A_{k-1}^{\oplus6}\longrightarrow A_k,
\qquad
(a_i)\longmapsto\sum_i(\partial_iq)a_i
\]

is surjective: for any degree-`k` squarefree monomial, choose one variable occurring in it and divide by that variable in the coefficient attached to its symplectic partner. Hence the degree-`k` term of `g` can be killed. Iterating for `k=3,4,5,6` gives an algebra automorphism carrying `g` to `q` whenever the quadratic part is nondegenerate.

It remains to compute the rank of multiplication by `q`. Decompose

\[
A=B_1\otimes B_2\otimes B_3,
\qquad
B_j=\mathbb F_2[x_j,y_j]/(x_j^2,y_j^2),
\]

and write

\[
q=q_1+q_2+q_3,
\qquad q_j=x_jy_j.
\]

Multiplication by `q` is the tensor-sum differential

\[
d=d_1+d_2+d_3,
\qquad d_j(b)=q_jb.
\]

On one four-dimensional factor `B_j`, `d_j` has image `span{x_jy_j}` and kernel `span{x_j,y_j,x_jy_j}`, so its homology has dimension two, represented by `x_j,y_j`. By the Kunneth formula, the homology of `(A,d)` has dimension

\[
2^3=8.
\]

Since `d^2=0`,

\[
\dim H(A,d)=\dim A-2\operatorname{rank}d,
\]

and therefore

\[
\operatorname{rank}d=\frac{64-8}{2}=28.
\]

Thus multiplication by every `g` with nondegenerate quadratic initial part has rank exactly 28.

Finally, rank `<=28` is the common vanishing condition of all `29 x 29` minors of the multiplication matrix, whose entries are polynomial in the coefficients of `g`. The nondegenerate-quadratic locus is nonempty and Zariski dense in `J^2`. Since all `29 x 29` minors vanish on that dense open set, they vanish identically on `J^2`. Hence every specialization satisfies

\[
\operatorname{rank}m_g\le28.
\]
\(\square\)

### Remark 2.2
The proof deliberately avoids the earlier crude source/target degree count; the bound `28` comes from the generic symplectic quadratic normal form and the eight-dimensional homology of its multiplication complex.

---

## 3. Child corank-four theorem

Let

\[
C\subset V\setminus(\{0\}\cup P),
\qquad |C|=30,
\]

and let `G_C(z)` be the `30 x 30` principal child minor of the translation circulant.

### Theorem 3.1 — child rank collapse

Assume

\[
g(z)=\sum_{p\in P}z_pT_p\in J^2
\]

and `z` is nonzero. Then

\[
\boxed{\operatorname{rank}G_C(z)\le26.}
\]

### Proof
By Theorem 2.1, the full `64 x 64` multiplication matrix `G(z)` has rank at most 28.

Choose `p_i in P` with `z_i!=0`. Consider the principal submatrix on

\[
C\cup\{0,p_i\}.
\]

Because `P cap C` is empty, the row of the vertex `0` has no nonzero entry into `C`; its entry at `p_i` is exactly `z_i`. In the order `(C,0,p_i)` the submatrix has the form

\[
\begin{pmatrix}
G_C(z)&0&b\\
0&0&z_i\\
b^T&z_i&0
\end{pmatrix}.
\tag{3.1}
\]

Since `z_i` is invertible in the coefficient field, simultaneous row/column operations using the hyperbolic pair `(0,p_i)` clear the vector `b` without changing `G_C(z)`. Thus (3.1) is congruent to

\[
G_C(z)\oplus
\begin{pmatrix}0&z_i\\z_i&0\end{pmatrix},
\]

and hence has rank

\[
\operatorname{rank}G_C(z)+2.
\]

It is a principal submatrix of the full matrix, so

\[
\operatorname{rank}G_C(z)+2
\le
\operatorname{rank}G(z)
\le28.
\]

Therefore

\[
\operatorname{rank}G_C(z)\le26.
\]
\(\square\)

### Corollary 3.2 — double Pfaffian vanishing

Let

\[
P_C(z)=\operatorname{Pf}G_C(z).
\]

On the linear subspace

\[
L=\{z:\ell_0(z)=0,\ \ell(z)=0\},
\]

one has

\[
P_C|_L=0
\]

and every first derivative of `P_C` also vanishes on `L`.

Indeed, an alternating `30 x 30` matrix has singular-Pfaffian gradient precisely when all its `28 x 28` principal Pfaffians vanish; rank at most 26 guarantees this. Since `G_C(z)` depends linearly on `z`, the chain rule gives vanishing of all first derivatives in the coefficient variables.

Equivalently, if `I(L)` denotes the linear ideal of the syndrome-zero subspace, then

\[
\boxed{P_C(z)\in I(L)^2.}
\]

This is the first rigorous explanation for an extra order of ANF-degree collapse beyond mere vanishing on the kernel code.

---

## 4. Boolean kernel-code elimination

For Boolean subsets `S subseteq P`, define

\[
f_C(S)=\operatorname{Pf}(G_S)_C\in\mathbb F_2.
\]

Every word of the kernel code

\[
K=\ker\sigma
=
\left\{S:\ |S|\equiv0\pmod2,\ \bigoplus_{p\in S}p=0\right\}
\]

satisfies

\[
\boxed{f_C(S)=0.}
\]

More strongly, the polynomial giving `f_C` has multiplicity at least two along the linear syndrome-zero locus.

When the syndrome map has rank seven, `K` has dimension eight.

Define the syndrome aggregate

\[
F(\tau)
=
\bigoplus_{S:\sigma(S)=\tau}f_C(S),
\qquad
\tau\in\mathbb F_2^7.
\]

Then the full rainbow parity is

\[
\boxed{
\bigoplus_{S\subseteq P}f_C(S)
=
\bigoplus_{\tau\in\mathbb F_2^7}F(\tau).
}
\]

Thus the fifteen-variable coefficient problem compresses to a seven-variable Boolean function.

---

## 5. Observed syndrome-degree collapse

For every compatible/oriented fifteen-line system tested so far, the syndrome aggregate has

\[
\boxed{\deg_{\rm ANF}F\le5.}
\]

The empirically observed bound is two degrees below the ambient syndrome dimension seven. Since total XOR over `F_2^7` detects only the degree-seven ANF coefficient, a proof of the weaker statement

\[
\deg F\le6
\]

would already force even rainbow-resolution parity.

The double-vanishing theorem above explains one additional order of collapse, but by itself it does not yet prove the full degree-six bound. A second structural identity is still needed.

### Syndrome-Degree Conjecture
For every relevant fifteen-parent system,

\[
\boxed{\deg_{\rm ANF}F\le5.}
\]

---

## 6. A stronger experimental target: disjoint parent-child parity

The child-rank proof uses only

\[
P\cap C=\varnothing,
\qquad 0\notin C,
\]

and not the existence of a canonical line decomposition. This motivates the stronger statement:

### Disjoint Parent-Child Parity Conjecture
Let

\[
P,C\subset\mathbb F_2^6\setminus\{0\},
\qquad |P|=15,\quad |C|=30,\quad P\cap C=\varnothing.
\]

Then the parity of perfect matchings of `C` whose fifteen distinct edge differences are exactly the elements of `P` is zero.

A necessary condition for any such matching is

\[
\bigoplus P=\bigoplus C.
\]

Directed experiments must therefore enforce this balance; unconditioned random tests are mostly vacuous. Balanced disjoint tests performed so far remain uniformly even, whereas analogous statements in dimensions four and five fail. Thus the `d=6,q=15` threshold appears genuinely special.

This stronger conjecture would imply the oriented-line parity theorem, hence the LQR bound `M_7<=14`, without using partition realizability.

---

## 7. Relation to complementary Pfaffians

From `LQR_R7_XOR_CIRCULANT.md`, with `D=V\setminus C`,

\[
\operatorname{Pf}G_D=s^2\operatorname{Pf}G_C,
\qquad s=\sum_{p\in P}z_p.
\]

The current evidence suggests that the missing second order of syndrome-degree collapse is created by the interaction of:

1. `P_C in I(L)^2` from child corank four;
2. the complementary identity above;
3. `P subseteq D` forced by `P cap C=empty`;
4. the balanced condition `xor P=xor C` whenever a rainbow matching exists.

This is now a much sharper algebraic target than enumerating higher resolution trades.

---

## 8. Computational status

The following checks have been used only as evidence, not as proofs:

```text
- exhaustive/random J^2 samples: full multiplication rank never exceeds 28;
- zero-syndrome directions in tested q=15 systems: child rank never exceeds 26;
- q=15 compatible/oriented systems: syndrome ANF degree <=5 in all tests;
- hundreds of balanced disjoint (P,C) pairs in F_2^6: no odd rainbow parity found;
- dimension-4 and dimension-5 analogues admit odd examples.
```

The exact numerical LQR status therefore remains

\[
\boxed{14\le M_7\le21.}
\]

The next proof barrier is to convert child corank four plus the complementary-Pfaffian identity into vanishing of the degree-seven syndrome coefficient.
