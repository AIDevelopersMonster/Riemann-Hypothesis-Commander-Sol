# HATTER-SOL-15 · p=17 Full Mahler Tomography via Octagon Order and Quadratic Majorisation

**Status:** exact theorem layer.  
**Input:** `PRIMITIVE_MAHLER_CHANNEL_SEPARATION.md`, `MAHLER_RESPONSE_ORBIT_CODE_AND_MULTIPLICATIVE_PARSEVAL.md`, `MAHLER_DIRICHLET_GAUSS_BRIDGE_AND_EVENTUAL_FULL_TOMOGRAPHY.md`, `P11_P13_ORDER_CONE_FULL_TOMOGRAPHY.md`.  
**Purpose:** close the first eight-channel signless reaction world. The primitive order-8, order-4, and order-2 character channels are all nonzero for every `mu>=4`. Thus `p=17` has no Mahler observer resonance anywhere on `lambda<=0`.

The proof separates into two mechanisms:

1. order geometry alone closes the primitive order-8 and order-4 channels;
2. the quadratic order-2 channel requires additional analytic structure of the Mahler autocorrelations and is closed by a weak-majorisation argument on quadratic-residue cosine squares.

---

## 1. The signless reaction octagon

For

\[
p=17,
\qquad
G_{17}=\mathbf F_{17}^\times/\{\pm1\}\cong C_8.
\]

Take

\[
g=[3].
\]

Its powers are represented by

\[
1,3,8,7,4,5,2,6.
\]

Let the primitive Mahler values in increasing mirror-angle order be

\[
b_1<b_2<\cdots<b_8.
\]

The signless angles are

\[
\frac\pi{17},\frac{2\pi}{17},\ldots,\frac{8\pi}{17},
\]

and the corresponding residue representatives are

\[
8,1,7,2,6,3,5,4.
\]

Therefore, in discrete-log order around the reaction octagon,

\[
\boxed{
(a_0,a_1,\ldots,a_7)
=(b_2,b_6,b_1,b_3,b_8,b_7,b_4,b_5).
}
\]

This ordering is valid for every `mu>=4` by strict primitive Mahler channel separation.

Put

\[
\zeta=e^{2\pi i/8}=e^{i\pi/4},
\qquad
S_q:=\sum_{j=0}^{7}a_j\zeta^{qj}.
\]

The nontrivial multiplicative Mahler modes are `S_q`, `1<=q<=7`.

---

## Theorem H15.120 — primitive order-8 channels are forced nonzero by order alone

For `q=1`, the real part of `S_1` is

\[
\Re S_1
=
\sum_{r=1}^8 c_r b_r,
\]

with

\[
(c_1,\ldots,c_8)
=
\left(
0,1,-\frac1{\sqrt2},0,\frac1{\sqrt2},\frac1{\sqrt2},-\frac1{\sqrt2},-1
\right).
\]

Let

\[
\Delta_r=b_{r+1}-b_r>0.
\]

Since the coefficient sum is zero, Abel summation gives

\[
\boxed{
\Re S_1
=
-\Delta_2
-\left(1-\frac1{\sqrt2}\right)(\Delta_3+\Delta_4)
-\Delta_5
-\left(1+\frac1{\sqrt2}\right)\Delta_6
-\Delta_7<0.
}
\]

Hence

\[
\boxed{S_1\ne0.}
\]

For `q=3`, the same calculation gives

\[
\boxed{
\Re S_3
=
-\Delta_2
-\left(1+\frac1{\sqrt2}\right)(\Delta_3+\Delta_4)
-\Delta_5
-\left(1-\frac1{\sqrt2}\right)\Delta_6
-\Delta_7<0.
}
\]

Therefore

\[
\boxed{S_3\ne0.}
\]

The `q=5,7` modes are complex conjugates of `q=3,1`, respectively. Thus every primitive order-8 character channel is nonzero for every `mu>=4`.

This part of the proof uses only the strict ordering of the Mahler channels around the octagon.

---

## Theorem H15.121 — order-4 character channel is forced nonzero by order alone

For `q=2`,

\[
\zeta^{2j}=i^j.
\]

Hence

\[
\Re S_2
=a_0-a_2+a_4-a_6.
\]

Using the octagon ordering,

\[
\boxed{
\Re S_2
=(b_2-b_1)+(b_8-b_4)>0.
}
\]

Therefore

\[
\boxed{S_2\ne0.}
\]

The `q=6` mode is its complex conjugate.

Thus every order-4 character channel is also nonzero throughout `mu>=4`.

---

## 2. Why order alone does not close the quadratic channel

For `q=4`,

\[
S_4
=
a_0-a_1+a_2-a_3+a_4-a_5+a_6-a_7.
\]

In terms of the ordered values,

\[
\boxed{
S_4
=b_1+b_2+b_4+b_8-b_3-b_5-b_6-b_7.
}
\]

Strict ordering by itself does **not** determine the sign of this expression. Indeed there exist strictly increasing real tuples `b_1<...<b_8` for which it vanishes.

Therefore the quadratic mode is the first `p=17` channel where pure order geometry is genuinely insufficient.

The remaining proof must use additional analytic structure of the Mahler profile.

---

## 3. Positive power expansion of every autocorrelation layer

Recall

\[
R_{m,\mu}(\delta)
=
\frac1{2\pi}
\int_0^{2\pi}
(\mu-2\cos t)^{-m}
(\mu-2\cos(t+\delta))^{-m}
\,dt.
\]

Set

\[
x=\cos^2\frac\delta2.
\]

## Theorem H15.122 — autocorrelation is a positive power series in `cos^2(delta/2)`

For every integer `m>=1` and every `mu>=4`,

\[
\boxed{
R_{m,\mu}(\delta)
=
\sum_{j\ge0}c_{m,j}(\mu)
\left(\cos^2\frac\delta2\right)^j,
}
\]

with

\[
\boxed{c_{m,j}(\mu)>0.}
\]

### Proof

Use the Feynman-parameter identity

\[
\frac1{A^mB^m}
=
\frac{\Gamma(2m)}{\Gamma(m)^2}
\int_0^1
\frac{u^{m-1}(1-u)^{m-1}}
{(uA+(1-u)B)^{2m}}\,du.
\]

Here

\[
A=\mu-2\cos t,
\qquad
B=\mu-2\cos(t+\delta).
\]

The trigonometric combination can be written as

\[
u\cos t+(1-u)\cos(t+\delta)
=\rho\cos(t+\varphi),
\]

where

\[
\rho^2
=
1-4u(1-u)\sin^2\frac\delta2
=
(2u-1)^2+4u(1-u)x.
\]

Thus the inner `t`-integral is

\[
H_{2m}(\rho)
=
\frac1{2\pi}
\int_0^{2\pi}
(\mu-2\rho\cos t)^{-2m}\,dt.
\]

Since `mu>=4` and `0<=rho<=1`, the binomial series converges absolutely and gives

\[
H_{2m}(\rho)
=
\sum_{\ell\ge0}
\mu^{-2m-2\ell}
\binom{2m+2\ell-1}{2\ell}
\binom{2\ell}{\ell}
\rho^{2\ell}.
\]

All coefficients are strictly positive.

Substituting

\[
\rho^2=(2u-1)^2+4u(1-u)x
\]

and expanding each power produces a power series in `x` with nonnegative coefficients. Integration against the positive beta weight makes every coefficient strictly positive. QED.

This is the additional analytic structure that the pure ordering argument did not use.

---

## 4. Quadratic-residue majorisation at `p=17`

Let

\[
\chi(r)=\left(\frac r{17}\right)
\]

be the quadratic character. Since `17 equiv 1 mod 4`, it is even. On representatives `1<=r<=8`,

\[
\chi(r)=+1
\quad\text{for}\quad
r\in\{1,2,4,8\},
\]

and

\[
\chi(r)=-1
\quad\text{for}\quad
r\in\{3,5,6,7\}.
\]

Define

\[
x_r:=\cos^2\frac{\pi r}{17}.
\]

Since `x_r` strictly decreases with `r` on `1<=r<=8`, define the two decreasing four-vectors

\[
U=(x_1,x_2,x_4,x_8),
\qquad
V=(x_3,x_5,x_6,x_7).
\]

The first three partial-sum inequalities are immediate:

\[
x_1>x_3,
\]

\[
x_1+x_2>x_3+x_5,
\]

\[
x_1+x_2+x_4>x_3+x_5+x_6.
\]

For the total sums, use

\[
x_r=\frac{1+\cos(2\pi r/17)}2.
\]

Because there are four positive and four negative signs on the half-system,

\[
\sum_{r=1}^8\chi(r)=0.
\]

The quadratic Gauss sum satisfies

\[
\sum_{r=1}^{16}\chi(r)e^{2\pi ir/17}=\sqrt{17}.
\]

Evenness of `chi` gives

\[
2\sum_{r=1}^8\chi(r)\cos\frac{2\pi r}{17}
=\sqrt{17}.
\]

Therefore

\[
\boxed{
\sum_{r=1}^8\chi(r)x_r
=\frac{\sqrt{17}}4>0.
}
\]

Equivalently,

\[
\boxed{
\sum U_i>\sum V_i.
}
\]

Hence `U` weakly majorises `V` in descending order.

---

## Lemma H15.123 — all positive power moments favor the quadratic residues

For every integer `j>=1`,

\[
\boxed{
\sum_{r=1}^8\chi(r)x_r^j>0.
}
\]

### Proof

The function

\[
\phi_j(x)=x^j
\]

is increasing and convex on `[0,1]` for every integer `j>=1`.

By the weak-majorisation inequalities above,

\[
\sum_{u\in U}\phi_j(u)
\ge
\sum_{v\in V}\phi_j(v).
\]

The inequality is strict because the majorisation is strict. Therefore

\[
\sum_{r=1}^8\chi(r)x_r^j>0.
\]

QED.

Thus the quadratic-residue half of the cyclotomic cosine-square spectrum dominates the nonresidue half at **every positive power moment**.

---

## Theorem H15.124 — every autocorrelation layer has positive quadratic twist

For every `m>=1` and `mu>=4`,

\[
\boxed{
T_{m,\mu}
:=
\sum_{r=1}^8
\chi(r)
R_{m,\mu}\left(\frac{2\pi r}{17}\right)
>0.
}
\]

### Proof

By H15.122,

\[
R_{m,\mu}\left(\frac{2\pi r}{17}\right)
=
\sum_{j\ge0}c_{m,j}x_r^j.
\]

Hence

\[
T_{m,\mu}
=
\sum_{j\ge0}c_{m,j}
\sum_{r=1}^8\chi(r)x_r^j.
\]

The `j=0` term vanishes because

\[
\sum_{r=1}^8\chi(r)=0.
\]

Every `j>=1` inner sum is strictly positive by H15.123, and every `c_{m,j}` is positive. Therefore `T_{m,mu}>0`. QED.

---

## Theorem H15.125 — the quadratic Mahler channel is strictly nonzero for all `mu>=4`

The Mahler autocorrelation expansion is

\[
M_\mu(\alpha)
=
2L_\mu
-
\sum_{m\ge1}
\frac1m\binom{2m}{m}
R_{m,\mu}(2\alpha).
\]

The `q=4` character of the octagon is exactly the quadratic character modulo `17`.

Moreover

\[
\chi(2)=1,
\]

so multiplication by `2` permutes the signless residue classes without changing the character. Therefore

\[
\sum_{[k]\in G_{17}}
\chi(k)R_{m,\mu}\left(\frac{4\pi k}{17}\right)
=
\sum_{r=1}^8
\chi(r)R_{m,\mu}\left(\frac{2\pi r}{17}\right)
=T_{m,\mu}>0.
\]

The constant Mahler term vanishes against the nontrivial character. Thus

\[
\boxed{
S_4
=
-\sum_{m\ge1}
\frac1m\binom{2m}{m}T_{m,\mu}<0.
}
\]

Hence

\[
\boxed{S_4\ne0}
\]

for every `mu>=4`.

This closes the only `p=17` character channel not determined by order alone.

---

## Corollary H15.126 — `p=17` has full Mahler tomography on the entire half-line `lambda<=0`

All nontrivial character modes `q=1,...,7` are nonzero for every `mu>=4`.

Therefore

\[
\boxed{
\mathcal E_{17}\cap[4,\infty)=\varnothing.
}
\]

Equivalently,

\[
\boxed{
\text{the centered primitive Mahler response operator for }p=17
\text{ is invertible for every }\lambda\le0.
}
\]

Combining previous layers:

\[
\boxed{
p\in\{5,7,11,13,17\}
\Longrightarrow
\text{full primitive Mahler tomography for all }\lambda\le0.
}
\]

---

## 5. Structural lesson

The `p=17` world is the first one where two different nonblindness mechanisms coexist.

The order-8 and order-4 channels are excluded by the **ordinal geometry** of the Mahler profile:

\[
\boxed{
\text{strict mirror ordering}
\Longrightarrow
\text{nonclosure of weighted octagon modes}.
}
\]

The quadratic channel is not order-forced. It survives because every Mahler autocorrelation layer has a stronger positivity property:

\[
\boxed{
R_{m,\mu}(\delta)
\in
\mathbf R_{>0}\!\left[\!\left[\cos^2(\delta/2)\right]\!\right]
}
\]

and the quadratic residues modulo `17` weakly majorise the nonresidues in the cosine-square coordinates.

Thus:

\[
\boxed{
\text{non-Abelian Mahler tomography}
=
\text{order geometry}
+
\text{positive analytic kernel geometry}.
}
\]

The second ingredient is genuinely stronger than the first and is likely reusable for larger prime worlds.

---

## 6. New reusable criterion

The proof isolates a general sufficient condition for a real even character `chi`.

Suppose, after choosing half-system representatives `1<=r< p/2`, the positive cosine-square vector

\[
\left\{\cos^2\frac{\pi r}{p}:\chi(r)=+1\right\}
\]

weakly majorises the corresponding negative vector.

Then every positive-power-series kernel in `cos^2(delta/2)` has positive `chi`-twist.

Since every Mahler autocorrelation layer has exactly this positive-power-series form, the corresponding character channel can never be blind on `mu>=4`.

This converts part of the analytic Mahler nonvanishing problem into a finite majorisation problem on cyclotomic cosine squares.

---

## 7. Claim boundary

The ingredients used here are classical:

- Abel summation for ordered linear forms;
- Feynman/Beta parameterisation;
- binomial expansion of resolvent powers;
- quadratic Gauss sums;
- weak majorisation and convex power sums.

The H15-specific content is their combination with the non-Abelian primitive Mahler observer to prove uniform full tomography in the first eight-channel reaction world.

No novelty priority is asserted before publication-stage literature audit.

---

## 8. Next attack

The next prime is

\[
\boxed{p=19},
\]

with

\[
|G_{19}|=9.
\]

The signless reaction group is now odd-order. There is no quadratic order-2 character, so the octagon majorisation obstruction disappears. The new issue is order-9 and order-3 polygon closure.

This makes `p=19` a clean test of whether the order-cone/Abel mechanism can scale beyond the small worlds without needing a real-character majorisation correction.
