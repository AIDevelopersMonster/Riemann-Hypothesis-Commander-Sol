# QGE3 LQR — Walsh–Bordered-Pfaffian Collapse for the Generic Hyperplane Case

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** active continuation after the generic hyperplane split  
**Scope:** the remaining regime with a hyperplane containing at most two canonical lines  
**Proof status:** exact character expansion and translation-orbit invariance; the final parity divisibility remains open

---

## 1. Hyperplane notation

Continue with the notation of `LQR_R7_GENERIC_HYPERPLANE_SPLIT.md`.

Let

\[
H\cong\mathbb F_2^5,
\qquad |H|=N=32,
\]

and write the two cosets as

\[
V=H\sqcup(H+e).
\]

Let

\[
I=P\cap H,
\qquad X=P\setminus H,
\qquad k=|I|,
\qquad n=|X|=15-k.
\]

Write every crossing parent uniquely as

\[
p=e+q,\qquad q\in H,
\]

and let

\[
Q=\{q:e+q\in X\}\subset H,
\qquad |Q|=n.
\]

For the child set put

\[
C_0=C\cap H,
\]

and translate the second coset back to `H`:

\[
\bar C_1=\{x-e:x\in C\cap(H+e)\}\subset H.
\]

If `m=m_H`, then

\[
|C_0|=n+2m,
\qquad
|\bar C_1|=n+2(k-m).
\]

The generic regime has

\[
\boxed{m\le2.}
\]

---

## 2. Crossing group circulant on H

For `q in H`, let `T_q` be translation by `q` on `H`. The full crossing operator is

\[
\mathcal C_Q(z)=\sum_{q\in Q}z_qT_q.
\]

Let `\widehat H` be the character group and let the Walsh matrix be

\[
W_{\chi,x}=(-1)^{\chi(x)},
\qquad
\chi\in\widehat H,\ x\in H.
\]

For each character define

\[
L_\chi(z)=\sum_{q\in Q}(-1)^{\chi(q)}z_q.
\]

The usual character diagonalization gives the exact rational identity

\[
\boxed{
\mathcal C_Q(z)
=
\frac1N W^T\operatorname{diag}(L_\chi(z))W.
}
\tag{2.1}
\]

---

## 3. Squarefree coefficient of an arbitrary crossing minor

Let `R,L subset H` with

\[
|R|=|L|=n.
\]

Cauchy–Binet applied twice to (2.1) gives

\[
\det \mathcal C_Q(z)_{R,L}
=
N^{-n}
\sum_{\substack{Y\subset\widehat H\\|Y|=n}}
\det W_{Y,R}\det W_{Y,L}
\prod_{\chi\in Y}L_\chi(z).
\]

Since the elements of `Q` are distinct and `|Q|=|Y|=n`, the squarefree coefficient is

\[
\boxed{
[z_Q]\det \mathcal C_Q(z)_{R,L}
=
N^{-n}
\sum_{\substack{Y\subset\widehat H\\|Y|=n}}
\det W_{Y,R}\det W_{Y,L}
\operatorname{per}W_{Y,Q}.
}
\tag{3.1}
\]

Here `per` is the ordinary permanent over the integers. The right side is an integer because the left side is.

Formula (3.1) is the correct character formula for the residual crossing determinant in the generic hyperplane decomposition.

---

## 4. Bordered Pfaffians absorb all boundary choices

Let

\[
A(z_I)
\]

be the internal alternating block on `C_0`, and let

\[
D(z_I)
\]

be the internal alternating block on `\bar C_1`.

For `Y subset \widehat H`, `|Y|=n`, define the bordered alternating matrices

\[
\mathcal M_0(Y,z_I)=
\begin{pmatrix}
A(z_I)&W_{Y,C_0}^T\\
-W_{Y,C_0}&0
\end{pmatrix},
\]

\[
\mathcal M_1(Y,z_I)=
\begin{pmatrix}
D(z_I)&W_{Y,\bar C_1}^T\\
-W_{Y,\bar C_1}&0
\end{pmatrix}
\]

and their Pfaffians

\[
\Phi_0(Y,z_I)=\operatorname{Pf}\mathcal M_0(Y,z_I),
\]

\[
\Phi_1(Y,z_I)=\operatorname{Pf}\mathcal M_1(Y,z_I).
\]

Because `|C_0|=n+2m`, every perfect matching contributing to `Phi_0` must use exactly `2m` vertices of `C_0` in internal `A`-edges. Hence

\[
\boxed{\Phi_0(Y,z_I)\text{ is homogeneous of degree }m\text{ in }z_I.}
\]

Likewise,

\[
\boxed{\Phi_1(Y,z_I)\text{ is homogeneous of degree }k-m.}
\]

Expanding the bordered Pfaffians along their character vertices gives, with the standard order-dependent Pfaffian signs,

\[
\Phi_0(Y,z_I)
=
\sum_{\substack{S\subset C_0\\|S|=2m}}
\varepsilon_0(S)
\operatorname{Pf}A_S(z_I)
\det W_{Y,C_0\setminus S},
\tag{4.1}
\]

and

\[
\Phi_1(Y,z_I)
=
\sum_{\substack{T\subset \bar C_1\\|T|=2(k-m)}}
\varepsilon_1(T)
\operatorname{Pf}D_T(z_I)
\det W_{Y,\bar C_1\setminus T}.
\tag{4.2}
\]

The same signs occur in the block-Pfaffian minor expansion of the original child matrix. Therefore, after fixing compatible global orders, the entire boundary sum collapses to a single coefficient of the product `Phi_0 Phi_1`.

---

## 5. Exact Walsh–bordered-Pfaffian formula

Let

\[
\widetilde R=[z_P]\operatorname{Pf}G_C(z)\in\mathbb Z.
\]

Its reduction modulo two is the resolution parity.

Combining the exact boundary formula from `LQR_R7_GENERIC_HYPERPLANE_SPLIT.md`, the character formula (3.1), and the bordered expansions (4.1)–(4.2) gives

\[
\boxed{
\widetilde R
=
\pm N^{-n}
\sum_{\substack{Y\subset\widehat H\\|Y|=n}}
\operatorname{per}W_{Y,Q}\;
[z_I]\bigl(\Phi_0(Y,z_I)\Phi_1(Y,z_I)\bigr).
}
\tag{5.1}
\]

The global sign depends only on the fixed vertex/character ordering and is irrelevant to parity and `2`-adic valuation.

Define

\[
B_Y=[z_I]\bigl(\Phi_0(Y,z_I)\Phi_1(Y,z_I)\bigr)
\]

and

\[
T_Y=\operatorname{per}W_{Y,Q}\,B_Y.
\]

Then

\[
\boxed{N^n\widetilde R=\pm\sum_{|Y|=n}T_Y.}
\tag{5.2}
\]

This is the main reduction: the exponentially large sum over boundary subsets `(S,T,J)` has disappeared. Each character set contributes one permanent and one product of two bordered Pfaffians.

---

## 6. Character-translation law

Let `eta in \widehat H`. Translation of a character set means

\[
Y+\eta=\{\chi+\eta:\chi\in Y\}.
\]

For any point set `U subset H`, Walsh columns transform as

\[
W_{Y+\eta,U}
=
W_{Y,U}\,D_\eta(U),
\]

where

\[
D_\eta(U)_{u,u}=(-1)^{\eta(u)}.
\]

Hence

\[
\boxed{
\operatorname{per}W_{Y+\eta,Q}
=(-1)^{\eta(\oplus Q)}
\operatorname{per}W_{Y,Q}.
}
\tag{6.1}
\]

For the bordered Pfaffians, congruence by the diagonal point-sign matrix and the induced variable twist give

\[
\Phi_0(Y+\eta,z_I)
=(-1)^{\eta(\oplus C_0)}
\Phi_0\bigl(Y,((-1)^{\eta(p)}z_p)_{p\in I}\bigr),
\]

and

\[
\Phi_1(Y+\eta,z_I)
=(-1)^{\eta(\oplus \bar C_1)}
\Phi_1\bigl(Y,((-1)^{\eta(p)}z_p)_{p\in I}\bigr).
\]

Therefore the full internal squarefree coefficient obeys

\[
\boxed{
B_{Y+\eta}
=(-1)^{\eta(\oplus C_0+\oplus\bar C_1+\oplus I)}B_Y.
}
\tag{6.2}
\]

The canonical XOR balance `xor C = xor P`, after translating the second coset back to `H`, is exactly

\[
\boxed{
\oplus C_0+\oplus\bar C_1+\oplus I+\oplus Q=0.
}
\tag{6.3}
\]

Multiplying (6.1) and (6.2) and using (6.3) gives the exact invariance

\[
\boxed{T_{Y+\eta}=T_Y\qquad\forall\eta\in\widehat H.}
\tag{6.4}
\]

Possible signs caused by reordering the translated character set occur in both bordered Pfaffians and cancel in their product.

---

## 7. Translation-orbit divisibility

Let

\[
\operatorname{Stab}(Y)=\{\eta\in\widehat H:Y+\eta=Y\}.
\]

This is a subgroup of the 32-element additive character group. Since `Y` is a union of cosets of its stabilizer,

\[
|\operatorname{Stab}(Y)|\mid |Y|=n.
\]

Hence

\[
|\operatorname{Stab}(Y)|\le2^{\nu_2(n)}
\]

and every translation orbit satisfies

\[
\boxed{
\nu_2(|\mathcal O_Y|)
=5-\nu_2(|\operatorname{Stab}(Y)|)
\ge5-\nu_2(n).
}
\tag{7.1}
\]

In particular, if `n` is odd, every stabilizer is trivial and

\[
\boxed{|\mathcal O_Y|=32.}
\]

By (6.4), formula (5.2) becomes

\[
\boxed{
N^n\widetilde R
=
\pm\sum_{\mathcal O}
|\mathcal O|\,T_{Y_\mathcal O}.
}
\tag{7.2}
\]

Thus the numerator already contains a nontrivial global power of two from character translation alone.

---

## 8. What the orbit factor does and does not prove

To prove even resolution parity one needs

\[
\nu_2\left(\sum_YT_Y\right)\ge5n+1,
\]

because `N^n=2^{5n}`.

The orbit factor (7.1) by itself is far too small. It must combine with additional `2`-adic divisibility of

\[
\operatorname{per}W_{Y,Q}
\]

and, more importantly, of the bordered coefficient

\[
B_Y=[z_I](\Phi_0\Phi_1).
\]

Exact experiments show that `B_Y` is typically highly divisible by two, but a termwise bound currently visible is still insufficient to reach `5n+1`. Therefore the remaining theorem is expected to require a second layer of cancellation or a sharper Walsh-minor divisibility statement, not merely valuation of individual summands.

---

## 9. New immediate target

The generic parity problem is now compressed to the following arithmetic statement:

### Walsh–Bordered Divisibility Target
For the data arising from a compatible fifteen-line system and a hyperplane with `m_H<=2`, prove

\[
\boxed{
\nu_2\left(
\sum_{\substack{Y\subset\widehat H\\|Y|=n}}
\operatorname{per}W_{Y,Q}\,
[z_I](\Phi_0(Y)\Phi_1(Y))
\right)
\ge5n+1.
}
\]

The translation-orbit invariance (6.4) should be treated as a first exact symmetry of this sum, not as the final divisibility mechanism.

A parallel coding reformulation is also available: resolutions are weight-15 solutions of the binary incidence system on the 3-uniform linear hypergraph with edges `{p,x,x+p}`. The seven obvious left-kernel relations of that incidence matrix match the seven syndrome coordinates encountered in the `J`-adic analysis. This may provide the missing global mod-two symmetry if the `2`-adic character route stalls.

---

## 10. Rigorous status

The exceptional hyperplane-dense geometry is classified, and the generic boundary sum is now compressed to the single character expression (5.1). The final parity cancellation is not yet proved.

Therefore the current LQR extremal status remains

\[
\boxed{14\le M_7\le21.}
\]
