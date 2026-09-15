# HATTER-SOL-15 · p=23 Full Mahler Tomography from Order Geometry and Moment Certificates

**Status:** exact theorem layer with a standalone rational-interval certificate.  
**Certificate:** `certificates/p23_interval_certificate.py`.  
**Purpose:** close the first prime world with signless reaction group of prime order `11`.

For

\[
p=23,
\qquad
G_{23}=\mathbf F_{23}^\times/\{\pm1\}\cong C_{11},
\]

all ten nontrivial Mahler character modes are nonzero for every

\[
\mu\ge4.
\]

Therefore

\[
\boxed{
\mathcal E_{23}\cap[4,\infty)=\varnothing,
}
\]

and the centered primitive Mahler response operator is invertible throughout

\[
\lambda\le0.
\]

The proof exhibits a genuine mixed mechanism:

- three independent frequencies are excluded by order geometry alone;
- two independent frequencies require the stronger positive-moment structure of the Mahler kernel.

Because conjugation pairs the remaining frequencies, this closes all ten.

---

## 1. The eleven-channel reaction world

Take the generator

\[
g=[2]\in G_{23}.
\]

Its powers are represented by

\[
1,2,4,8,7,9,5,10,3,6,11.
\]

Let

\[
b_1<b_2<\cdots<b_{11}
\]

be the primitive Mahler values in increasing signless mirror-angle order.

The representative carrying angle

\[
\frac{j\pi}{23}
\]

is the unique signless `r` satisfying

\[
2r\equiv\pm j\pmod{23}.
\]

Thus the angle-ordered representatives are

\[
11,1,10,2,9,3,8,4,7,5,6.
\]

Consequently, in discrete-log order around the reaction `11`-gon,

\[
\boxed{
(a_0,a_1,\ldots,a_{10})
=
(b_2,b_4,b_8,b_7,b_9,b_5,b_{10},b_3,b_6,b_{11},b_1).
}
\]

This strict ordering holds for every `mu>=4` by the primitive Mahler separation theorem.

Set

\[
\zeta=e^{2\pi i/11},
\qquad
S_q:=\sum_{j=0}^{10}a_j\zeta^{qj}.
\]

It is enough to prove

\[
S_q\ne0
\qquad
(q=1,2,3,4,5),
\]

since

\[
S_{11-q}=\overline{S_q}.
\]

---

## 2. Order-only frequencies

For fixed `q`, rewrite

\[
S_q=\sum_{r=1}^{11}d_r^{(q)}b_r,
\]

where `d_r^(q)` is the `11`th-root coefficient attached to `b_r` by the discrete-log placement above.

Let

\[
D_k^{(q)}:=\sum_{r=1}^{k}d_r^{(q)}.
\]

Since the total coefficient sum is zero,

\[
\sum_{r=1}^{11}d_r^{(q)}=0,
\]

Abel summation gives

\[
\boxed{
S_q
=-\sum_{k=1}^{10}
D_k^{(q)}\,(b_{k+1}-b_k).
}
\]

Hence it is enough to find one real linear functional that is strictly positive on every proper cumulative sum `D_k^(q)`.

### Frequency `q=1`

Use

\[
\ell_1(z)=\Re(e^{-i\pi/6}z).
\]

The exact rational-interval certificate gives

\[
\ell_1(D_k^{(1)})>
0.06988044
\]

for every

\[
1\le k\le10.
\]

Therefore

\[
\ell_1(S_1)<0,
\]

so

\[
\boxed{S_1\ne0.}
\]

### Frequency `q=3`

Use

\[
\ell_3(z)=\Re(e^{2\pi i/11}z).
\]

The certificate gives

\[
\ell_3(D_k^{(3)})>
0.41541501
\]

for all proper cumulative sums. Hence

\[
\boxed{S_3\ne0.}
\]

### Frequency `q=4`

Use

\[
\ell_4(z)=\Re(e^{13\pi i/22}z).
\]

The certified lower bound is

\[
\ell_4(D_k^{(4)})>
0.62789943
\]

for every

\[
1\le k\le10.
\]

Thus

\[
\boxed{S_4\ne0.}
\]

The three frequencies `q=1,3,4` are therefore excluded from blindness by order geometry alone.

No numerical Mahler values enter this part of the argument.

---

## 3. Positive-moment reduction for the remaining frequencies

Use the global Mahler profile already proved in the preceding theorem layer:

\[
\boxed{
M_\mu(\alpha)
=C_\mu-
\sum_{j\ge1}D_{\mu,j}\cos^{2j}\alpha,
\qquad
D_{\mu,j}>0.
}
\]

For a multiplicative character `chi` on `G_23`, multiplication by `2` only contributes the nonzero unit factor `chi(2)^{-1}`. Therefore the corresponding Mahler coefficient is nonzero whenever

\[
\sum_{j\ge1}D_{\mu,j}T_j(\chi)
\]

is nonzero, where

\[
\boxed{
T_j(\chi)
=
\sum_{r=1}^{11}
\chi(r)
\cos^{2j}\frac{\pi r}{23}.
}
\]

Put

\[
x_r:=\cos^2\frac{\pi r}{23},
\]

so

\[
1>x_1>x_2>\cdots>x_{11}>0.
\]

It will suffice to prove

\[
\Re T_j(\chi)>0
\qquad
\forall j\ge1.
\]

Because every Mahler weight `D_{mu,j}` is positive, this places the entire positive Mahler combination in the open right half-plane.

---

## 4. The `q=2` character

Let `chi_2` be the character satisfying

\[
\chi_2([2])=\zeta^2.
\]

Write

\[
w_r:=\Re\chi_2(r).
\]

Define

\[
c_r:=w_r x_r,
\qquad
C_k:=\sum_{r=1}^{k}c_r.
\]

The exact rational-interval certificate proves

\[
\boxed{
C_k>0
\qquad
(1\le k\le11),
}
\]

with the smallest certified lower bound

\[
\boxed{
\min_k C_k>0.03207258.
}
\]

For every integer `j>=1`,

\[
\Re T_j(\chi_2)
=
\sum_{r=1}^{11}c_r x_r^{j-1}.
\]

Since

\[
x_1^{j-1}\ge x_2^{j-1}\ge\cdots\ge x_{11}^{j-1}>0,
\]

Abel summation gives

\[
\Re T_j(\chi_2)
=
C_{11}x_{11}^{j-1}
+
\sum_{k=1}^{10}
C_k
\left(x_k^{j-1}-x_{k+1}^{j-1}\right).
\]

Every term is nonnegative and the first is strictly positive. Therefore

\[
\boxed{
\Re T_j(\chi_2)>0
\qquad\forall j\ge1.
}
\]

Hence

\[
\boxed{S_2\ne0.}
\]

---

## 5. The `q=5` character

Let

\[
\chi_5([2])=\zeta^5.
\]

Again write

\[
w_r:=\Re\chi_5(r).
\]

For the large moments use

\[
c_r:=w_r x_r^6.
\]

The exact certificate proves that all cumulative sums

\[
C_k^{(6)}:=\sum_{r=1}^{k}w_r x_r^6
\]

are strictly positive, with

\[
\boxed{
\min_k C_k^{(6)}>0.05193515.
}
\]

Therefore for every

\[
j\ge6,
\]

Abel summation applied to the decreasing sequence `x_r^(j-6)` gives

\[
\boxed{
\Re T_j(\chi_5)>0.
}
\]

The remaining five moments are finite. The standalone exact interval certificate gives

\[
\boxed{
\begin{array}{c|c}
j&\text{certified lower bound for }\Re T_j(\chi_5)\\
\hline
1&0.45762866\\
2&0.26980278\\
3&0.18090229\\
4&0.15433503\\
5&0.16023732
\end{array}}
\]

Hence

\[
\boxed{
\Re T_j(\chi_5)>0
\qquad\forall j\ge1.
}
\]

Therefore

\[
\boxed{S_5\ne0.}
\]

---

## 6. Exact certification method

All finite sign checks above are reproduced by

`certificates/p23_interval_certificate.py`.

The script uses only Python's standard library and exact rational arithmetic.

It starts from the classical rational bounds

\[
\frac{103993}{33102}<\pi<\frac{104348}{33215},
\]

then encloses every required cosine by interval evaluation of the Taylor polynomial together with the rigorous Lagrange remainder

\[
|R_{2N+2}(x)|
\le
\frac{|x|^{2N+2}}{(2N+2)!}.
\]

All subsequent arithmetic is exact interval arithmetic over `Fraction`.

Thus the decimal lower bounds quoted in the proof are display forms of exact positive rational lower endpoints, not floating-point assumptions.

---

## Theorem H15.130 — complete nonvanishing for `p=23`

The five independent frequencies satisfy

\[
\boxed{
S_q\ne0
\qquad
q=1,2,3,4,5
}
\]

for every

\[
\mu\ge4.
\]

By complex conjugation the same holds for

\[
q=6,7,8,9,10.
\]

Therefore every nontrivial even Dirichlet-character Mahler mode is nonzero.

Hence

\[
\boxed{
\mathcal E_{23}\cap[4,\infty)=\varnothing.
}
\]

Equivalently,

\[
\boxed{
\text{the centered primitive Mahler response operator for }p=23
\text{ is invertible for every }\lambda\le0.
}
\]

Combining all closed prime worlds so far:

\[
\boxed{
p\in\{5,7,11,13,17,19,23\}
\Longrightarrow
\text{full primitive Mahler tomography for all }\lambda\le0.
}
\]

---

## 7. Structural lesson

`p=23` is the first case where the signless reaction group itself has prime order greater than `5`:

\[
|G_{23}|=11.
\]

There are no lower-order subgroup modes to dispose of.

Nevertheless all channels remain visible.

The proof shows that two geometries cooperate:

\[
\boxed{
\text{ordered response polygon geometry}
}
\]

and

\[
\boxed{
\text{positive cosine-square moment geometry}.
}
\]

The first excludes frequencies `1,3,4`; the second excludes `2,5`.

So the new pattern is not merely prime-by-prime coincidence. The Mahler observer carries more rigidity than monotonicity alone:

\[
\boxed{
M_\mu(\alpha)-C_\mu
\text{ lies in the negative cone generated by }
\{\cos^{2j}\alpha:j\ge1\}.
}
\]

Blindness must therefore be compatible simultaneously with an ordered cyclotomic polygon and with all positive cosine-square moments. By `p=23` these constraints are already strong enough to eliminate every character.

---

## 8. Next research target

The next prime is

\[
\boxed{p=29},
\]

with

\[
|G_{29}|=14.
\]

This brings back a real quadratic channel together with order-7 and order-14 complex channels.

The reusable attack is now clear:

1. apply order-Abel separation to every frequency whose cumulative root polygon lies in an open half-plane;
2. for the remaining frequencies, seek a power shift `h` such that the cumulative sums of
   \[
   \Re(e^{-i\phi}\chi(r))x_r^h
   \]
   are all positive;
3. certify the finitely many moments below `h` by exact rational interval arithmetic.

If this succeeds uniformly for `p=29`, the method has become an algorithmic proof architecture rather than a sequence of ad hoc low-prime arguments.
