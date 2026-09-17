# HATTER-SOL-15 · p=29 Full Mahler Tomography by Algorithmic Abel/Moment Certification

**Status:** exact theorem layer with standalone rational-interval certificate.  
**Certificate:** `certificates/p29_interval_certificate.py`.  
**Purpose:** test whether the H15 proof architecture developed at `p=23` scales to a larger reaction space with mixed character orders.

For

\[
p=29,
\qquad
G_{29}=\mathbf F_{29}^\times/\{\pm1\}\cong C_{14},
\]

all nontrivial primitive Mahler character modes are nonzero for every

\[
\mu\ge4.
\]

Hence

\[
\boxed{
\mathcal E_{29}\cap[4,\infty)=\varnothing,
}
\]

and the centered primitive Mahler response operator is invertible throughout

\[
\lambda\le0.
\]

The proof is the first genuinely algorithmic H15 closure:

- four independent frequencies are certified by order-Abel geometry alone;
- two independent complex frequencies are certified by shifted positive-moment Abel sums;
- the quadratic real frequency is certified by a finite set of low moments plus one shifted tail certificate.

---

## 1. The fourteen-channel reaction world

Take the generator

\[
g=[2]\in G_{29}.
\]

Its powers are represented by

\[
1,2,4,8,13,3,6,12,5,10,9,11,7,14.
\]

Let

\[
b_1<b_2<\cdots<b_{14}
\]

be the primitive Mahler values in increasing signless mirror-angle order.

The signless representatives attached to the angles

\[
\frac{j\pi}{29},
\qquad 1\le j\le14,
\]

are

\[
14,1,13,2,12,3,11,4,10,5,9,6,8,7.
\]

Therefore in discrete-log order around the reaction `14`-gon,

\[
\boxed{
(a_0,\ldots,a_{13})
=
(b_2,b_4,b_8,b_{13},b_3,b_6,b_{12},b_5,b_{10},b_9,b_{11},b_7,b_{14},b_1).
}
\]

This strict order is valid for every `mu>=4`.

Put

\[
\zeta=e^{2\pi i/14},
\qquad
S_q:=\sum_{j=0}^{13}a_j\zeta^{qj}.
\]

By complex conjugation it is enough to prove

\[
S_q\ne0
\qquad(q=1,2,3,4,5,6,7).
\]

---

## 2. Order-only Abel channels

For a fixed frequency `q`, rewrite

\[
S_q=\sum_{r=1}^{14}d_r^{(q)}b_r,
\]

and let

\[
D_k^{(q)}:=\sum_{r=1}^{k}d_r^{(q)}.
\]

Because the total coefficient sum is zero,

\[
S_q
=-\sum_{k=1}^{13}
D_k^{(q)}(b_{k+1}-b_k).
\]

Thus one fixed real projection of all proper cumulative sums is enough to exclude a zero for every strictly increasing response profile.

The exact rational-interval certificate verifies the following.

### Theorem H15.131 — order-Abel nonvanishing for `q=2,3,5,6`

For `q=2`, take the real projection itself. Then all proper cumulative sums have positive real part, with

\[
\boxed{
\min_k\Re D_k^{(2)}>0.22252092.
}
\]

For `q=3`, again the real projection works:

\[
\boxed{
\min_k\Re D_k^{(3)}>0.22252093.
}
\]

For `q=5`, rotate the projection by

\[
\phi=\frac{4\pi}{3}.
\]

Then

\[
\boxed{
\min_k\Re(e^{-i\phi}D_k^{(5)})>0.19821989.
}
\]

For `q=6`, rotate by

\[
\phi=-\frac\pi2.
\]

Then

\[
\boxed{
\min_k\Re(e^{-i\phi}D_k^{(6)})>0.19309642.
}
\]

Therefore

\[
\boxed{
S_2,S_3,S_5,S_6\ne0
}
\]

for every

\[
\mu\ge4.
\]

These four modes are closed by ordering alone.

---

## 3. Positive-moment kernel architecture

Use the global Mahler profile already proved in the previous layers:

\[
\boxed{
M_\mu(\alpha)
=C_\mu-
\sum_{j\ge1}D_{\mu,j}\cos^{2j}\alpha,
\qquad
D_{\mu,j}>0.
}
\]

For a character `chi_q` with

\[
\chi_q([2])=\zeta^q,
\]

set

\[
x_r:=\cos^2\frac{\pi r}{29}.
\]

Then the corresponding character coefficient is a nonzero unit multiple of

\[
-\sum_{j\ge1}D_{\mu,j}T_j^{(q)},
\]

where

\[
T_j^{(q)}
:=
\sum_{r=1}^{14}
\chi_q(r)x_r^j.
\]

A sufficient condition for nonvanishing is to place all `T_j^(q)` in one open half-plane.

The certificate establishes this by shifted Abel positivity.

---

## Theorem H15.132 — the `q=1` primitive order-14 channel is nonzero for all `mu>=4`

Use the real projection and the shifted coefficients

\[
c_r=\Re\chi_1(r)\,x_r.
\]

All cumulative sums

\[
C_k:=\sum_{r=1}^{k}c_r
\]

are strictly positive, with

\[
\boxed{
\min_k C_k>0.56878779.
}
\]

For every `j>=1`,

\[
\Re T_j^{(1)}
=
\sum_r c_r x_r^{j-1}.
\]

Since `x_r^(j-1)` is positive and decreasing, Abel summation gives

\[
\boxed{
\Re T_j^{(1)}>0
\qquad\forall j\ge1.
}
\]

Hence

\[
\boxed{S_1\ne0.}
\]

---

## Theorem H15.133 — the `q=4` order-7 channel is nonzero for all `mu>=4`

Rotate by

\[
\phi=\frac{2\pi}{5}.
\]

Set

\[
c_r=\Re(e^{-i\phi}\chi_4(r))\,x_r.
\]

The exact interval certificate gives

\[
\boxed{
\min_k\sum_{r=1}^{k}c_r>0.18931689.
}
\]

Therefore for every `j>=1`,

\[
\boxed{
\Re(e^{-i\phi}T_j^{(4)})>0.
}
\]

Hence every positive Mahler combination lies in the same open half-plane and

\[
\boxed{S_4\ne0.}
\]

for every `mu>=4`.

---

## 4. The quadratic `q=7` channel

The frequency `q=7` is the real quadratic character modulo `29` on the signless quotient.

Here the unshifted first-power cumulative sums are not all positive, so the simplest majorisation-style criterion fails. This is exactly the kind of situation for which the shifted-tail architecture was introduced.

The certificate proves that after the power shift

\[
h=12,
\]

all cumulative sums of

\[
c_r=\chi_7(r)x_r^{12}
\]

are strictly positive:

\[
\boxed{
\min_k\sum_{r=1}^{k}\chi_7(r)x_r^{12}
>0.02645132.
}
\]

Therefore Abel summation gives

\[
\boxed{
T_j^{(7)}>0
\qquad\forall j\ge12.
}
\]

The finitely many moments below the shift are certified directly:

\[
\boxed{
\begin{array}{c|c}
j&\text{certified lower bound for }T_j^{(7)}\\
\hline
1&1.34629118\\
2&1.00971839\\
3&0.67314559\\
4&0.44175179\\
5&0.29450119\\
6&0.20509904\\
7&0.15448164\\
8&0.12974815\\
9&0.12222949\\
10&0.12607099\\
11&0.13728991
\end{array}}
\]

Hence

\[
\boxed{
T_j^{(7)}>0
\qquad\forall j\ge1.
}
\]

Since all Mahler weights `D_{mu,j}` are positive,

\[
\boxed{S_7\ne0.}
\]

for every

\[
\mu\ge4.
\]

This closes the only real-character mode not handled by order geometry alone.

---

## Theorem H15.134 — complete nonvanishing for `p=29`

The seven independent frequencies satisfy

\[
\boxed{
S_q\ne0
\qquad(q=1,2,3,4,5,6,7)
}
\]

for every

\[
\mu\ge4.
\]

By conjugation, all remaining nontrivial frequencies are nonzero as well.

Therefore

\[
\boxed{
\mathcal E_{29}\cap[4,\infty)=\varnothing.
}
\]

Equivalently,

\[
\boxed{
\text{the centered primitive Mahler response operator for }p=29
\text{ is invertible for every }\lambda\le0.
}
\]

Combining all closed prime worlds:

\[
\boxed{
p\in\{5,7,11,13,17,19,23,29\}
\Longrightarrow
\text{full primitive Mahler tomography for all }\lambda\le0.
}
\]

---

## 5. Exact certification

All finite sign checks are reproduced by

`certificates/p29_interval_certificate.py`.

The script uses only the Python standard library and exact rational arithmetic.

It starts from the classical bounds

\[
\frac{103993}{33102}<\pi<\frac{104348}{33215}
\]

and encloses every required cosine through Taylor intervals with rigorous Lagrange remainder. Every subsequent operation is exact interval arithmetic over `Fraction`.

Thus every decimal bound quoted above is only a readable form of a strictly positive exact rational lower endpoint.

---

## 6. Why `p=29` changes the status of the method

Up to `p=23`, the proof architecture was promising. At `p=29` it becomes reusable in a precise sense.

Every independent character frequency was closed by one of only two templates:

### Template A — order-Abel

Find a phase `phi` such that every proper cumulative coefficient sum satisfies

\[
\Re(e^{-i\phi}D_k)>0.
\]

Then strict channel ordering alone forces nonvanishing.

### Template B — shifted moment-Abel

Find an integer `h>=1` and a phase `phi` such that

\[
\sum_{r\le k}
\Re(e^{-i\phi}\chi(r))x_r^h>0
\]

for every `k`.

Then all moments `j>=h` lie in one half-plane by Abel summation, and only the finite set `1<=j<h` requires direct certification.

At `p=29` all seven independent frequencies fit exactly into these two templates.

Thus the H15 low-prime program has crossed a methodological threshold:

\[
\boxed{
\text{prime world}
\to
\text{finite character scan}
\to
\text{automatic Abel/moment certificate}
\to
\text{rigorous tomography theorem}.
}
\]

This is now an algorithmic proof architecture rather than a sequence of handcrafted arguments.

---

## 7. Claim boundary

The ingredients are classical:

- finite cyclic Fourier analysis;
- Abel summation;
- positive cosine-square power expansions;
- exact rational interval arithmetic.

The H15-specific content is the synthesis of these tools with the non-Abelian primitive Mahler observer and the demonstration that the resulting certification pipeline closes every character mode through `p=29`.

No global theorem for all primes is claimed yet.

---

## 8. Next research target

The correct next move is no longer to hand-prove `p=31` immediately.

The new target is to formalize the **automatic certificate search**:

1. construct the discrete-log placement for a prime `p`;
2. test order-Abel phases for each independent character;
3. for unresolved modes search small shifts `h` and phases `phi` for positive cumulative moment sums;
4. certify the finite low-moment residue exactly;
5. record the first prime, if any, for which this architecture fails.

The next mathematical question is therefore sharper than another low-prime computation:

\[
\boxed{
\text{Does every odd prime admit an Abel/moment certificate, or is there a first genuine Mahler blind-mode obstruction?}
}
\]

That is now the natural frontier of HATTER-SOL-15.
