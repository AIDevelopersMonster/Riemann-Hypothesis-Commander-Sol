# HATTER-SOL-15 · Exact `p=11` Closure of Full Mahler Tomography

**Status:** exact theorem layer for `p=11`, valid throughout `mu>=4` (`lambda<=0`).  
**Purpose:** close the first prime world in which nontrivial character cancellation is genuinely possible by using the strict ordering of the five primitive Mahler values together with the exact `C_5` character geometry.

---

## 1. Reaction group and cyclic ordering

For `p=11`,

\[
G_{11}=\mathbf F_{11}^\times/\{\pm1\}
\]

has order five. The class of `2` generates `G_{11}`. Using the representatives

\[
1,\ 2,\ 4,\ 3,\ 5,
\]

corresponding to the powers

\[
[1],\ [2],\ [2^2],\ [2^3],\ [2^4],
\]

write

\[
A=f_\mu([1]),
\quad
B=f_\mu([2]),
\quad
C=f_\mu([4]),
\quad
D=f_\mu([3]),
\quad
E=f_\mu([5]),
\]

where

\[
f_\mu([k])=M_\mu\left(2\cos\frac{2\pi k}{11}\right).
\]

The strict Mahler channel-separation theorem says that `f_mu` is strictly decreasing in the absolute real cyclotomic coordinate.

Now

\[
\begin{aligned}
\left|2\cos\frac{6\pi}{11}\right|
&=2\cos\frac{5\pi}{11},\\
\left|2\cos\frac{4\pi}{11}\right|
&=2\cos\frac{4\pi}{11},\\
\left|2\cos\frac{8\pi}{11}\right|
&=2\cos\frac{3\pi}{11},\\
\left|2\cos\frac{2\pi}{11}\right|
&=2\cos\frac{2\pi}{11},\\
\left|2\cos\frac{10\pi}{11}\right|
&=2\cos\frac{\pi}{11}.
\end{aligned}
\]

Since cosine is strictly decreasing on `(0,pi)`,

\[
2\cos\frac{5\pi}{11}
<
2\cos\frac{4\pi}{11}
<
2\cos\frac{3\pi}{11}
<
2\cos\frac{2\pi}{11}
<
2\cos\frac{\pi}{11}.
\]

Therefore, for every `mu>=4`,

\[
\boxed{
D>B>C>A>E.
}
\]

This order is uniform in the spectral parameter.

---

## 2. The two nontrivial character pairs

Let

\[
\zeta=e^{2\pi i/5}.
\]

The nontrivial character frequencies on `G_11 con C_5` are `r=1,2,3,4`; frequencies `3,4` are complex conjugates of `2,1` respectively.

It is therefore enough to prove nonvanishing at `r=1` and `r=2`.

Define

\[
F_r
:=
A+B\zeta^{-r}+C\zeta^{-2r}+D\zeta^{-3r}+E\zeta^{-4r}.
\]

Centering the profile does not change `F_r` for `r ne 0`, because

\[
1+\zeta^{-r}+\zeta^{-2r}+\zeta^{-3r}+\zeta^{-4r}=0.
\]

Thus these are exactly the nontrivial Mahler character modes.

---

## Theorem H15.116 — the frequency-two mode is never zero

For every `mu>=4`,

\[
\boxed{F_2\ne0.}
\]

### Proof

Using

\[
\sin\frac{2\pi}{5}>0,
\qquad
\sin\frac{\pi}{5}>0,
\]

the imaginary part is

\[
\operatorname{Im}F_2
=
\sin\frac{2\pi}{5}(C-D)
+
\sin\frac{\pi}{5}(E-B).
\]

From the uniform order

\[
D>C,
\qquad
B>E,
\]

both differences are strictly negative. Hence

\[
\boxed{
\operatorname{Im}F_2<0,
}
\]

so `F_2` cannot vanish. QED.

By conjugation,

\[
F_3=\overline{F_2}\ne0.
\]

---

## Theorem H15.117 — the frequency-one mode is never zero

For every `mu>=4`,

\[
\boxed{F_1\ne0.}
\]

### Proof

Let

\[
c_1:=\cos\frac{2\pi}{5}=\frac{\sqrt5-1}{4},
\qquad
c_2:=\cos\frac{\pi}{5}=\frac{\sqrt5+1}{4}.
\]

Then

\[
c_2-c_1=\frac12,
\qquad
c_1+c_2=\frac{\sqrt5}{2}.
\]

The real part is

\[
\operatorname{Re}F_1
=
A+c_1(B+E)-c_2(C+D).
\]

Using only the strict order

\[
A<C,
\qquad
B<D,
\qquad
E<D,
\]

we obtain

\[
\operatorname{Re}F_1
<
C+2c_1D-c_2(C+D).
\]

Now

\[
1-c_2=c_1,
\]

so

\[
C+2c_1D-c_2(C+D)
=
(1-c_2)C+(2c_1-c_2)D.
\]

A direct trigonometric identity gives

\[
2c_1-c_2=-c_1.
\]

Hence

\[
\operatorname{Re}F_1
<
 c_1(C-D).
\]

Since

\[
C<D
\]

and `c_1>0`,

\[
\boxed{
\operatorname{Re}F_1<0.
}
\]

Therefore `F_1 ne 0`. QED.

By conjugation,

\[
F_4=\overline{F_1}\ne0.
\]

---

## Theorem H15.118 — exact full tomography closure for `p=11`

For every

\[
\boxed{\mu>=4}
\]

all four nontrivial multiplicative Mahler character modes are nonzero:

\[
\boxed{
F_r(\mu)\ne0,
\qquad
r=1,2,3,4.
}
\]

Therefore the centered primitive Mahler response operator for the prime dihedral world `p=11` is invertible on the full four-dimensional zero-sum reaction space for every

\[
\lambda=4-\mu\le0.
\]

Equivalently,

\[
\boxed{
\mathcal E_{11}\cap[4,\infty)=\varnothing.
}
\]

Thus `p=11`, the first prime at which nontrivial cancellation was not ruled out by dimension alone, has **no Mahler blind resonance anywhere on the full nonnegative spectral half-line**.

---

## 3. Why this matters

The proof does not use large-`mu` asymptotics, first-harmonic dominance, or numerical evaluation. It uses only:

1. strict primitive Mahler ordering by the absolute cyclotomic coordinate;
2. the exact cyclic ordering of the five signless multiplicative classes;
3. elementary geometry of the fifth roots of unity.

This is the first indication that the arithmetic arrangement of the mirror values may itself forbid character cancellation even when abstract real vectors of the same dimension could cancel.

The mechanism is therefore stronger than generic analyticity:

\[
\boxed{
\text{cyclotomic order geometry}
+\text{Mahler monotonicity}
\Longrightarrow
\text{character noncancellation}.
}
\]

---

## 4. Updated closed prime worlds

We now have exact full linear tomography for every `mu>=4` at

\[
\boxed{p=5,\ 7,\ 11.}
\]

The next prime is

\[
\boxed{p=13,}
\]

where

\[
|G_{13}|=6.
\]

This introduces character orders `2,3,6` and a more complicated sign pattern. It is the next minimal laboratory for deciding whether the `p=11` order argument extends to a general noncancellation principle.

---

## 5. Claim boundary

The character geometry of `C_5` and elementary trigonometric identities are classical. The H15-specific content is the way the previously proved strict Mahler ordering constrains the exact multiplicative character sums of the non-Abelian response ensemble strongly enough to exclude every blind mode.

No novelty priority is asserted before publication-stage literature review.
