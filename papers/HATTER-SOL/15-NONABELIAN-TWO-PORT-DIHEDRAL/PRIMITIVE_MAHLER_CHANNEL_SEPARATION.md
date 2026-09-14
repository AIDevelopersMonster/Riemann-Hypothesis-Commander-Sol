# HATTER-SOL-15 · Primitive Mahler Channel Separation

**Status:** exact theorem layer for the nontrivial mirror-channel Mahler measures in the nonnegative spectral half-line `lambda<=0`.  
**Purpose:** upgrade the numerical evidence in `TEMPERED_K2_DESCENT_AND_GALOIS_REGULATOR_ORBIT.md` to a proof that the scalar primitive Mahler observer separates all real cyclotomic mirror channels up to the unavoidable dihedral sign ambiguity.

---

## 1. Mirror block on the physical torus

Fix

\[
\mu=4-\lambda\ge4
\]

and a real cyclotomic channel

\[
\vartheta=2\cos\alpha,
\qquad 0<\alpha<\pi.
\]

On the physical torus write

\[
z=e^{it},
\qquad
w=e^{i\phi}.
\]

The mirror-block determinant is

\[
D_{\alpha,\mu}(t,\phi)
=
\mu^2-\mu X\vartheta+X^2+\vartheta^2-Y^2-4,
\]

where

\[
X=2\cos t,
\qquad
Y=2\cos\phi.
\]

Define

\[
A_\mu(u):=\mu-2\cos u.
\]

Then the determinant factors on the torus as

\[
\boxed{
D_{\alpha,\mu}(t,\phi)
=
A_\mu(t+\alpha)A_\mu(t-\alpha)-4\cos^2\phi.
}
\]

Indeed,

\[
A_\mu(t+\alpha)A_\mu(t-\alpha)
=\mu^2-4\mu\cos t\cos\alpha
+4(\cos^2t-\sin^2\alpha),
\]

which is exactly

\[
\mu^2-\mu X\vartheta+X^2+\vartheta^2-4.
\]

For `mu>4`,

\[
A_\mu(u)>2
\]

for every `u`, so the product is strictly bigger than `4`.

For `mu=4`,

\[
A_4(u)\ge2,
\]

and equality of the product with `4` would require simultaneously

\[
t+\alpha\equiv0,
\qquad
t-\alpha\equiv0
\pmod{2\pi},
\]

which is impossible for `0<alpha<pi`.

Hence throughout the nontrivial channel range

\[
\boxed{
C_{\alpha,\mu}(t)
:=A_\mu(t+\alpha)A_\mu(t-\alpha)>4.
}
\]

Thus `D_{alpha,mu}` is strictly positive on the physical torus for every nontrivial mirror channel when `mu>=4`.

---

## 2. Exact positive-series expansion

Define the logarithmic Mahler measure

\[
M_\mu(\alpha)
:=
\frac1{(2\pi)^2}
\int_0^{2\pi}\int_0^{2\pi}
\log D_{\alpha,\mu}(t,\phi)
\,d\phi\,dt.
\]

For fixed `t`, since `C_{alpha,mu}(t)>4`,

\[
\log(C-4\cos^2\phi)
=
\log C
+
\log\left(1-\frac4C\cos^2\phi\right).
\]

Using

\[
\log(1-x)
=-\sum_{m\ge1}\frac{x^m}{m}
\]

and

\[
\frac1{2\pi}
\int_0^{2\pi}\cos^{2m}\phi\,d\phi
=
\frac1{4^m}\binom{2m}{m},
\]

we obtain

\[
\frac1{2\pi}
\int_0^{2\pi}
\log(C-4\cos^2\phi)\,d\phi
=
\log C
-
\sum_{m\ge1}
\frac1m\binom{2m}{m}C^{-m}.
\]

Averaging over `t`, the first term is independent of `alpha` because

\[
\log C_{\alpha,\mu}(t)
=
\log A_\mu(t+\alpha)
+
\log A_\mu(t-\alpha),
\]

and Haar measure is translation invariant.

Set

\[
L_\mu
:=
\frac1{2\pi}\int_0^{2\pi}
\log A_\mu(t)\,dt
=
\log\frac{\mu+\sqrt{\mu^2-4}}2.
\]

For `m>=1`, define

\[
f_{m,\mu}(t):=A_\mu(t)^{-m}
\]

and its circular autocorrelation

\[
R_{m,\mu}(\delta)
:=
\frac1{2\pi}
\int_0^{2\pi}
 f_{m,\mu}(t)
 f_{m,\mu}(t+\delta)
\,dt.
\]

After shifting `t`,

\[
\frac1{2\pi}
\int_0^{2\pi}C_{\alpha,\mu}(t)^{-m}dt
=
R_{m,\mu}(2\alpha).
\]

Therefore

## Theorem H15.91 — exact autocorrelation expansion

For `mu>=4` and `0<alpha<pi`,

\[
\boxed{
M_\mu(\alpha)
=
2L_\mu
-
\sum_{m\ge1}
\frac1m\binom{2m}{m}
R_{m,\mu}(2\alpha).
}
\]

For every compact subinterval of `0<alpha<pi`, the series converges absolutely and uniformly.

The dependence on the arithmetic channel has therefore been isolated completely into a family of circular autocorrelations.

---

## 3. Strict monotonicity of the circular autocorrelations

For every `m>=1` and `mu>=4`, the function

\[
f_{m,\mu}(t)
=(\mu-2\cos t)^{-m}
\]

is `2pi`-periodic, even, positive, and strictly decreasing on

\[
0<t<\pi.
\]

The next lemma is elementary but is the key analytic step.

## Lemma H15.92 — strict circular autocorrelation decrease

Let `f` be a positive `2pi`-periodic even `C^1` function that is strictly decreasing on `(0,pi)`. Define

\[
R(\delta)
=
\frac1{2\pi}
\int_{-\pi}^{\pi}
f(t)f(t+\delta)dt.
\]

Then

\[
\boxed{R'(\delta)<0}
\]

for every

\[
0<\delta<\pi.
\]

### Proof

Differentiate and shift the integration variable:

\[
R'(\delta)
=
\frac1{2\pi}
\int_{-\pi}^{\pi}
f(u-\delta)f'(u)du.
\]

Split the integral at zero and use evenness of `f` and oddness of `f'`:

\[
R'(\delta)
=
\frac1{2\pi}
\int_0^\pi
\bigl(f(u-\delta)-f(u+\delta)\bigr)f'(u)du.
\]

Arguments are interpreted periodically.

Let `d(x)` denote circular distance from `x` to `0`. For

\[
0<u<\pi,
\qquad
0<\delta<\pi,
\]

one has

\[
\boxed{
d(u+\delta)>d(u-\delta).}
\]

Indeed, if `u+delta<=pi`, this is immediate. If `u+delta>pi`, then

\[
d(u+\delta)=2\pi-u-\delta,
\]

and comparison with `|u-delta|` reduces respectively to

\[
2(\pi-u)>0
\]

or

\[
2(\pi-\delta)>0.
\]

Since `f` is strictly decreasing with circular distance,

\[
f(u-\delta)-f(u+\delta)>0,
\]

while

\[
f'(u)<0.
\]

Hence the integrand is strictly negative for every `u in (0,pi)`, proving the claim. QED.

This is a special one-dimensional circular form of the classical principle that convolution preserves symmetric decreasing structure.

---

## Theorem H15.93 — strict Mahler monotonicity in the mirror angle

For fixed `mu>=4`,

\[
\boxed{
M_\mu(\alpha)
\text{ is strictly increasing on }
0<\alpha<\frac\pi2.
}
\]

Moreover,

\[
\boxed{
M_\mu(\pi-\alpha)=M_\mu(\alpha).
}
\]

Hence if

\[
\beta(\alpha):=\min(\alpha,\pi-\alpha),
\]

then

\[
\boxed{
M_\mu(\alpha)
\text{ is a strictly increasing function of }
\beta\in(0,\pi/2].
}
\]

### Proof

For `0<alpha<pi/2`, the argument `2alpha` lies in `(0,pi)`. By Lemma H15.92 every

\[
R_{m,\mu}(2\alpha)
\]

is strictly decreasing as `alpha` increases.

All coefficients

\[
\frac1m\binom{2m}{m}
\]

in H15.91 are positive. Therefore their negative weighted sum is strictly increasing. The constant term `2L_mu` is independent of `alpha`. Hence `M_mu(alpha)` is strictly increasing.

The symmetry follows from the even `2pi`-periodicity of each autocorrelation:

\[
R_{m,\mu}(2\pi-2\alpha)
=R_{m,\mu}(2\alpha).
\]

QED.

---

## Corollary H15.94 — strict monotonicity in the real cyclotomic coordinate

Write

\[
\vartheta=2\cos\alpha.
\]

Since

\[
|\vartheta|
=2\cos\beta,
\qquad
\beta=\min(\alpha,\pi-\alpha),
\]

and `2 cos beta` is strictly decreasing on `(0,pi/2)`, H15.93 gives

\[
\boxed{
M_\mu(\vartheta)
\text{ is an even and strictly decreasing function of }
|\vartheta|
\text{ for }0\le|\vartheta|<2.
}
\]

Thus

\[
\boxed{
0\le|\vartheta_1|<|\vartheta_2|<2
\Longrightarrow
M_\mu(\vartheta_1)>M_\mu(\vartheta_2).
}
\]

The numerical separation seen previously for `p=5` and `p=7` is therefore a theorem, not an accident.

---

## 4. Cyclotomic channel separation

Let `p` be an odd prime and

\[
\vartheta_k
=2\cos\frac{2\pi k}{p},
\qquad
1\le k\le\frac{p-1}{2}.
\]

## Lemma H15.95 — distinct mirror channels have distinct absolute real coordinates

If

\[
|\vartheta_k|=|\vartheta_\ell|,
\]

then

\[
\boxed{k=\ell}
\]

within the standard mirror range

\[
1\le k,\ell\le\frac{p-1}{2}.
\]

### Proof

Equality of absolute cosines implies

\[
\frac{2\pi k}{p}
\equiv
\pm\frac{2\pi\ell}{p}
\pmod\pi.
\]

The possibilities modulo `2pi` are

\[
2k\equiv\pm2\ell\pmod{2p}
\]

or

\[
2k\equiv p\pm2\ell\pmod{2p}.
\]

The second alternative is impossible because the left side is even and the right side is odd. Thus

\[
k\equiv\pm\ell\pmod p.
\]

In the chosen mirror range this forces `k=ell`. QED.

Combining H15.94 and H15.95 gives the main result.

## Theorem H15.96 — scalar primitive Mahler observer separates every prime mirror channel

For every odd prime `p`, every `mu>=4`, and every two distinct mirror channels

\[
1\le k,\ell\le\frac{p-1}{2},
\qquad
k\ne\ell,
\]

one has

\[
\boxed{
M_\mu(\vartheta_k)
\ne
M_\mu(\vartheta_\ell).
}
\]

Indeed their ordering is exactly the reverse ordering of the absolute cyclotomic coordinates:

\[
\boxed{
|\vartheta_k|<|\vartheta_\ell|
\iff
M_\mu(\vartheta_k)>M_\mu(\vartheta_\ell).
}
\]

Thus the scalar logarithmic Mahler measure of one labelled primitive mirror factor is already a complete invariant of the real mirror channel.

---

## Corollary H15.97 — exact signless recovery of an object reaction

Fix a nonzero labelled Fourier channel `k` in the prime dihedral world. An object reaction

\[
a\in\mathbf F_p^\times
\]

moves that channel to

\[
[ak]\in\mathbf F_p^\times/\{\pm1\}.
\]

The scalar primitive Mahler value

\[
M_\mu(\vartheta_{ak})
\]

determines `[ak]` uniquely by H15.96. Since `k` is fixed and invertible modulo `p`, it therefore determines

\[
\boxed{\{a,-a\}.}
\]

Hence the previously conjectural observer line is now exact:

\[
\boxed{
\text{labelled primitive scalar Mahler observer}
\quad\Longleftrightarrow\quad
\text{signless reaction coordinate }\{\pm a\}.
}
\]

The only ambiguity is precisely the dihedral reflection symmetry

\[
S R^a S^{-1}=R^{-a}.
\]

---

## 5. Full norm versus primitive scalar observer

The full prime spectral determinant multiplies all mirror factors over the Galois orbit. Therefore an object reaction `a!=0` merely permutes the factors and leaves the full norm invariant.

By contrast, H15.96 shows that the individual scalar factor values are pairwise distinct.

Thus there is now a strict theorem-level information gap:

\[
\boxed{
\text{primitive scalar Mahler value}
\succ
\text{full cyclotomic-norm Mahler value}.
}
\]

More explicitly,

\[
\boxed{
\begin{array}{c|c}
\text{observer} & \text{reaction information retained}\\
\hline
\text{labelled primitive scalar Mahler measure} & \{\pm a\}\\
\text{full prime norm/Mahler measure} & \mathbf1_{a\ne0}
\end{array}}
\]

This proves that the loss of channel information occurs at the **Galois-orbit multiplication step**, not at the scalar Mahler integration step.

---

## 6. Relation to the regulator layer

`TEMPERED_K2_DESCENT_AND_GALOIS_REGULATOR_ORBIT.md` proved that each primitive mirror factor carries a rational curve-`K_2` class and that the selected genus-two classes form a Galois orbit.

H15.96--97 now prove that, in the range `mu>=4`, the associated scalar Mahler period already separates those Galois mirror channels.

Therefore no appeal to an unproved special-value identity is needed to establish channel separation:

\[
\boxed{
\text{primitive algebraic sheet}
\to
\text{primitive }K_2\text{ class}
\to
\text{scalar Mahler period}
}
\]

all retain the same signless channel information.

An eventual `L`-value formula would explain the arithmetic nature of those distinct numbers, but separation itself is already proved analytically.

---

## 7. Prior-art and novelty boundary

The proof uses classical ingredients:

- Jensen expansion;
- central-binomial moments of `cos^{2m}`;
- translation invariance of Haar measure;
- monotonicity of circular autocorrelation for positive symmetric decreasing functions, a close relative of classical rearrangement/convolution principles.

A targeted literature search found broad Mahler-measure/regulator theory and classical symmetric-decreasing convolution machinery, but did not identify this exact dihedral mirror-block monotonicity statement.

The H15-specific candidate is the synthesis

\[
\boxed{
\text{dihedral object reaction}
\to
\text{mirror-angle shift}
\to
\text{primitive Mahler period}
\to
\text{strict cyclotomic-channel separation}
\to
\text{signless world-coordinate recovery}.
}
\]

No novelty priority is asserted without a dedicated publication-stage literature audit.

---

## 8. Next research target

The scalar-separation problem is closed for `mu>=4`.

The next serious questions are:

1. extend the separation theorem through the spectral interval `mu<4`, where the physical torus may meet the spectral curve and the positive Jensen series can fail;
2. determine whether the ordering of primitive Mahler values has a direct expression in the `L`-data of the selected genus-two motives;
3. test whether the vector of primitive Mahler values across all mirror channels admits an invertible or frame-like inter-world transform analogous to the projective Gram/Parseval law already proved for coarse Frobenius responses.

The third direction is particularly aligned with H15: it asks whether a **continuous arithmetic response vector** can replace the binary projective world signature while retaining exact reconstructibility.
