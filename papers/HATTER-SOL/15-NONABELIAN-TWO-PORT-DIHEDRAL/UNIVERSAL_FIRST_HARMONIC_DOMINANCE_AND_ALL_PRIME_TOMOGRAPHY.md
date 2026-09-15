# HATTER-SOL-15 · Universal First-Harmonic Dominance and All-Prime Mahler Tomography

**Status:** exact theorem layer for every odd prime and every `mu>=4`.  
**Certificate:** `certificates/universal_first_harmonic_dominance_certificate.py`.  
**Purpose:** replace the prime-by-prime certificate ladder by one uniform inequality.

The main result is the inequality that had remained only a proposed sufficient route in earlier layers:

\[
\boxed{
B_{\mu,1}>
\sum_{n\ge2}B_{\mu,n}
\qquad(\mu\ge4).
}
\]

Here

\[
M_\mu(\alpha)
=C_\mu-
\sum_{n\ge1}B_{\mu,n}\cos(2n\alpha),
\qquad
B_{\mu,n}>0.
\]

This single inequality eliminates every possible nontrivial Dirichlet-character cancellation at once. Consequently the `p=43,q=8` obstruction is not an observer resonance; it was only the first failure of the earlier certificate templates.

---

## 1. Fourier coefficient notation

For `m>=1`, put

\[
f_{m,\mu}(t)=(\mu-2\cos t)^{-m},
\qquad \mu\ge4,
\]

and write

\[
f_{m,\mu}(t)
=\sum_{n\in\mathbf Z}a_{m,n}(\mu)e^{int}.
\]

The Mahler harmonic coefficients are

\[
\boxed{
B_{\mu,n}
=2\sum_{m\ge1}
 c_m a_{m,n}(\mu)^2,
\qquad
c_m:=\frac1m\binom{2m}{m}.
}
\]

Therefore

\[
B_{\mu,1}-\sum_{n\ge2}B_{\mu,n}
=
\sum_{m\ge1}E_m(\mu),
\]

where

\[
\boxed{
E_m(\mu)
:=
c_m\left(
4a_{m,1}^2+a_{m,0}^2-A_{2m}(\mu)
\right)
}
\]

and

\[
A_k(\mu)
:=\frac1{2\pi}\int_0^{2\pi}
(\mu-2\cos t)^{-k}\,dt.
\]

Indeed Parseval gives

\[
A_{2m}=a_{m,0}^2+2\sum_{n\ge1}a_{m,n}^2.
\]

---

## 2. Legendre representation of one `m`-layer

Set

\[
s:=\sqrt{\mu^2-4},
\qquad
x:=\frac\mu s>1.
\]

The classical integral identity gives

\[
\boxed{
A_k(\mu)
=s^{-k}P_{k-1}(x),
}
\]

where `P_j` is the Legendre polynomial.

Also

\[
\mu A_m-2a_{m,1}=A_{m-1},
\]

hence

\[
2a_{m,1}=\mu A_m-A_{m-1}.
\]

It follows that

\[
\boxed{
E_m(\mu)
=c_m s^{-2m}Q_m(x),
}
\]

with

\[
\boxed{
Q_m(x)
=
\frac{4}{x^2-1}
\bigl(xP_{m-1}(x)-P_{m-2}(x)\bigr)^2
+P_{m-1}(x)^2-P_{2m-1}(x).
}
\]

For `m=1`, interpret `P_{-1}` through the direct formula; equivalently

\[
\boxed{
Q_1(x)=\frac{(x-1)(3-x)}{x+1}.
}
\]

Thus the first-harmonic dominance problem is reduced to controlling the scalar layers `Q_m(x)`.

---

## 3. The first seven layers are nonnegative globally

For `mu>=4`,

\[
1<x\le\frac{2}{\sqrt3}<\frac76.
\]

Put

\[
y=x-1,
\qquad
0\le y\le\frac16.
\]

For `m=1,...,7`, direct Legendre reduction gives

\[
Q_m(1+y)=yH_m(y).
\]

For `m=1`,

\[
H_1(y)=\frac{2-y}{2+y}>0.
\]

For `m=2,...,7`, the exact integer polynomials `H_m` are recorded in the standalone certificate. Exact rational interval evaluation on `[0,1/6]` gives

\[
\boxed{H_m(y)>0\qquad(m=2,...,7).}
\]

Therefore

\[
\boxed{
E_m(\mu)\ge0
\qquad
(1\le m\le7,\ \mu\ge4).
}
\]

This fact will let us discard all but part of the positive low-`m` contribution whenever convenient.

---

## 4. Uniform bound on the negative tail

Let

\[
d:=\mu-2\ge2.
\]

Since

\[
\mu-2\cos t
=d+4\sin^2(t/2),
\]

and for `|t|<=pi`

\[
\sin(|t|/2)\ge\frac{|t|}{\pi},
\]

we get

\[
A_{2m}(\mu)
\le
\frac{\sqrt d}{4}d^{-2m}I_{2m},
\]

where

\[
I_{2m}:=
\int_{-\infty}^{\infty}(1+u^2)^{-2m}\,du.
\]

Since

\[
E_m\ge-c_mA_{2m},
\]

we need an efficient uniform estimate for `c_m I_{2m}`.

Define

\[
K_m:=
\frac{m}{4^m}\binom{2m}{m}I_{2m}.
\]

Using

\[
I_{2m}
=
\pi\frac{\binom{4m-2}{2m-1}}{4^{2m-1}},
\]

one obtains the exact ratio

\[
\boxed{
\frac{K_{m+1}}{K_m}
=
1-\frac1{16m^2}<1.
}
\]

Thus `K_m` is decreasing. An exact rational check at `m=8`, using `pi<22/7`, gives

\[
K_8<\sqrt{\frac8{15}}.
\]

Therefore for all `m>=8`,

\[
\boxed{
E_m(\mu)
\ge
-rac{\sqrt d}{4}\sqrt{\frac8{15}}
\left(\frac4{d^2}\right)^m\frac1{m^2}.
}
\]

Hence

\[
\boxed{
\sum_{m\ge8}E_m(\mu)
>
-rac{\sqrt d}{4}\sqrt{\frac8{15}}
\sum_{m\ge8}
\left(\frac4{d^2}\right)^m\frac1{m^2}.
}
\]

At the worst endpoint `d=2`, convexity of `x^{-2}` gives

\[
\sum_{m\ge8}\frac1{m^2}
<
\int_{15/2}^{\infty}\frac{dt}{t^2}
=
\frac2{15}.
\]

Thus throughout `d>=2`, the absolute worst boundary tail is

\[
\boxed{
\left|\sum_{m\ge8}E_m\right|
<
\frac{2}{15\sqrt{15}}
\approx0.03442652
}
\]

when no geometric decay beyond `d=2` is used.

---

## 5. Near-boundary region `4<=mu<=4.1`

Here

\[
2\le d\le\frac{21}{10}.
\]

The elementary inequalities

\[
\frac87\le x\le\frac76
\]

follow by squaring from

\[
49\mu^2\ge64(\mu^2-4),
\qquad
36\mu^2\le49(\mu^2-4).
\]

Therefore

\[
\frac17\le y=x-1\le\frac16.
\]

On this interval the exact certificate proves the rational lower bounds

\[
\boxed{
\begin{array}{c|c}
m&Q_m(x)>\beta_m\\
\hline
1&123/1000\\
2&51/100\\
3&129/100\\
4&27/10\\
5&101/20\\
6&79/10\\
7&19/10
\end{array}}
\]

Moreover

\[
s^2=d(d+4)\le\frac{1281}{100}.
\]

Hence

\[
\sum_{m=1}^{7}E_m(\mu)
>
\sum_{m=1}^{7}
 c_m\left(\frac{100}{1281}\right)^m\beta_m.
\]

The right side is the exact rational number

\[
L_*:=
\sum_{m=1}^{7}
 c_m\left(\frac{100}{1281}\right)^m\beta_m
\approx0.03540312.
\]

The certificate checks exactly that

\[
\boxed{
L_*^2>\frac4{3375},
}
\]

which is equivalent to

\[
L_*>rac{2}{15\sqrt{15}}.
\]

Combining with the tail bound yields

\[
\boxed{
B_{\mu,1}-\sum_{n\ge2}B_{\mu,n}>0
\qquad
(4\le\mu\le4.1).
}
\]

So the difficult physical endpoint `mu=4` is already closed.

---

## 6. Far region `mu>=4.1`

Now

\[
d\ge\frac{21}{10}.
\]

Because the first seven layers are nonnegative, it suffices to retain only `E_1` and dominate the entire `m>=8` negative tail.

Let

\[
r:=\frac{\mu-\sqrt{\mu^2-4}}2.
\]

The `m=1` layer has the exact form

\[
E_1
=
\frac{4r^4(1-2r^2)}{(1-r^2)^3}.
\]

For `mu>=4.1`, one has `r^2<1/14`. Expanding the resulting polynomial inequality gives

\[
\boxed{
E_1(\mu)
\ge
4\left(\frac{\mu}{\mu^2-1}\right)^4.
}
\]

For the tail, since

\[
y:=\frac4{d^2}<1,
\]

we use

\[
\sum_{m\ge8}\frac{y^m}{m^2}
\le
\frac{y^8}{64(1-y)}
\le
\frac{2}{15}y^8
\qquad(d\ge21/10),
\]

and therefore it is enough to compare `E_1` with the simpler larger majorant

\[
T_*(d)
:=
\frac{\sqrt d}{30}\sqrt{\frac8{15}}
\left(\frac4{d^2}\right)^8.
\]

The ratio of the lower bound for `E_1` to `T_*` is, up to a positive constant,

\[
R(d)
=
\frac{d^{31/2}(d+2)^4}{((d+2)^2-1)^4}.
\]

Its logarithmic derivative is

\[
\boxed{
\frac{R'(d)}{R(d)}
=
\frac{23d^3+154d^2+301d+186}
{2d(d+1)(d+2)(d+3)}>0.
}
\]

Thus the comparison is hardest at `d=21/10`. The exact endpoint square inequality

\[
\boxed{
16\left(
\frac{41/10}{(41/10)^2-1}
\right)^8
>
\frac{4^{16}}{900}\frac8{15}\left(\frac{10}{21}\right)^{31}
}
\]

is verified by exact rational arithmetic in the certificate.

Hence

\[
\boxed{
E_1>\left|\sum_{m\ge8}E_m\right|
\qquad(\mu\ge4.1),
}
\]

and therefore

\[
\boxed{
B_{\mu,1}-\sum_{n\ge2}B_{\mu,n}>0
\qquad(\mu\ge4.1).
}
\]

---

## Theorem H15.137 — universal first-harmonic dominance

Combining the near-boundary and far regions:

\[
\boxed{
B_{\mu,1}>
\sum_{n\ge2}B_{\mu,n}
\qquad
\text{for every }\mu\ge4.
}
\]

This is uniform: it contains no prime, no character, and no finite-world parameter.

The first Mahler harmonic generated by the length-four non-Abelian square defect dominates the entire higher-harmonic tail on the full half-line `lambda<=0`.

---

## Theorem H15.138 — every nontrivial even Dirichlet-character Mahler mode is nonzero

Let `p` be any odd prime and let `chi mod p` be any nontrivial even character.

From the Mahler–Dirichlet–Gauss bridge,

\[
\widehat f_\mu(\chi)
=-\frac12\tau(\overline\chi)\chi(2)
\sum_{\substack{n\ge1\\p\nmid n}}
B_{\mu,n}\chi(n).
\]

Since `|chi(n)|<=1`,

\[
\left|
\sum_{\substack{n\ge2\\p\nmid n}}
B_{\mu,n}\chi(n)
\right|
\le
\sum_{n\ge2}B_{\mu,n}
<
B_{\mu,1}.
\]

The `n=1` term therefore cannot be cancelled.

Hence

\[
\boxed{
\widehat f_\mu(\chi)\ne0
}
\]

for every odd prime `p`, every nontrivial even `chi`, and every `mu>=4`.

---

## Corollary H15.139 — all-prime full primitive Mahler tomography

For every odd prime `p`,

\[
\boxed{
\mathcal E_p\cap[4,\infty)=\varnothing.
}
\]

Equivalently, for every

\[
\boxed{
\lambda\le0,
}
\]

the centered primitive Mahler response operator is invertible on the entire zero-sum signless reaction space

\[
\mathbf C[G_p]_0,
\qquad
G_p=\mathbf F_p^\times/\{\pm1\}.
\]

Thus the earlier low-prime ladder was not accidental:

\[
\boxed{
\text{full primitive Mahler tomography holds for every odd prime world.}
}
\]

---

## 7. Resolution of the `p=43,q=8` obstruction

The channel

\[
(p,q)=(43,8)
\]

was the first one that escaped both automatic certificate templates:

- order-Abel failed;
- single-phase shifted moment-Abel failed.

H15.137–139 show that this was **not** a genuine Mahler observer resonance.

Indeed

\[
\boxed{
F_{43,8}(\mu)\ne0
\qquad\forall\mu\ge4.
}
\]

The obstruction occurred because the moment vectors rotate too much for a common half-plane certificate, while the actual Mahler harmonic weights are constrained strongly enough that the first harmonic dominates all later rotations in aggregate.

This is exactly the stronger ingredient that the `p=43` frontier demanded.

---

## 8. Return to the non-Abelian square

Earlier H15 layers established:

- the commutator square defect is
  \[
  [R,S]=R^2;
  \]
- the fourth spectral moment is the first local moment that sees this square holonomy;
- the first channel-dependent Mahler term occurs at order `mu^{-4}` and is the harmonic `cos(2alpha)`.

The present theorem adds the global statement

\[
\boxed{
\text{that first non-Abelian harmonic dominates every higher Mahler harmonic for all }\mu\ge4.
}
\]

Hence the square defect is not merely the first visible correction asymptotically. On the entire nonpositive spectral half-line it is strong enough to prevent **every multiplicative arithmetic character mode** from disappearing.

The chain is now:

\[
\boxed{
[R,S]\ne1
\to
\text{length-four square holonomy}
\to
\text{first Mahler harmonic}
\to
\text{universal harmonic dominance}
\to
\text{all-prime character nonvanishing}
\to
\text{full linear reaction tomography}.
}
\]

This is the strongest direct answer obtained so far to the HATTER-SOL-15 question of what becomes visible specifically because the ports do not commute.

---

## 9. Claim boundary and publication status

The proof uses classical components:

- Fourier/Parseval identities;
- the Legendre formula for powers of the Poisson resolvent;
- Wallis/Beta integrals;
- elementary central-binomial and convex-sum estimates;
- exact rational interval certification of finitely many low-layer polynomial bounds.

The H15-specific theorem is their synthesis into the universal Mahler first-harmonic dominance inequality and the resulting all-prime non-Abelian reaction tomography.

No external novelty-priority claim is made here. A hostile literature audit remains mandatory before publication.

**Internal publication assessment:** this result crosses the mathematical threshold for a dedicated publication candidate inside HATTER-SOL-15, subject to independent proof audit, reproduction of the exact certificate, bibliography/prior-art review, and RU/EN publication assembly.
