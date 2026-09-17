# HATTER-SOL-15 · Universal First-Harmonic Dominance and All-Prime Mahler Tomography

**Status:** exact theorem layer for every odd prime and every `mu>=4`; hostile-proof-audit revision v1.1.  
**Certificate:** `certificates/universal_first_harmonic_dominance_certificate.py`.  
**Audit:** `HOSTILE_PROOF_AUDIT_UNIVERSAL_DOMINANCE.md`.  
**Purpose:** replace the prime-by-prime certificate ladder by one uniform inequality.

The main result is

\[
\boxed{
B_{\mu,1}>\sum_{n\ge2}B_{\mu,n}
\qquad(\mu\ge4).
}
\]

Here

\[
M_\mu(\alpha)
=C_\mu-\sum_{n\ge1}B_{\mu,n}\cos(2n\alpha),
\qquad B_{\mu,n}>0.
\]

This single inequality eliminates every possible nontrivial Dirichlet-character cancellation at once. Consequently the earlier `p=43,q=8` obstruction was a failure of the previous certificate templates, not an observer resonance.

The v1.1 audit revision repairs two defects in the first draft of the proof:

1. a geometric-series estimate in the far region was too optimistic;
2. a one-sided lower bound for the high-`m` tail had been described incorrectly as an absolute-value bound.

Neither defect changes the theorem. The corrected far-region estimate is stronger and is certified exactly below.

---

## 1. Fourier coefficient notation

For `m>=1`, put

\[
f_{m,\mu}(t)=(\mu-2\cos t)^{-m},
\qquad \mu\ge4,
\]

and write

\[
f_{m,\mu}(t)=\sum_{n\in\mathbf Z}a_{m,n}(\mu)e^{int}.
\]

The Mahler harmonic coefficients are

\[
\boxed{
B_{\mu,n}=2\sum_{m\ge1}c_m a_{m,n}(\mu)^2,
\qquad
c_m:=\frac1m\binom{2m}{m}.
}
\]

Therefore

\[
B_{\mu,1}-\sum_{n\ge2}B_{\mu,n}
=\sum_{m\ge1}E_m(\mu),
\]

where

\[
\boxed{
E_m(\mu)
:=c_m\left(4a_{m,1}^2+a_{m,0}^2-A_{2m}(\mu)\right)
}
\]

and

\[
A_k(\mu)
:=\frac1{2\pi}\int_0^{2\pi}(\mu-2\cos t)^{-k}\,dt.
\]

Indeed Parseval gives

\[
A_{2m}=a_{m,0}^2+2\sum_{n\ge1}a_{m,n}^2.
\]

Hence

\[
2\left(a_{m,1}^2-\sum_{n\ge2}a_{m,n}^2\right)
=4a_{m,1}^2+a_{m,0}^2-A_{2m}.
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
A_k(\mu)=s^{-k}P_{k-1}(x),
}
\]

where `P_j` is the Legendre polynomial.

Also

\[
\mu A_m-2a_{m,1}=A_{m-1},
\]

because multiplication of `f_{m,mu}` by `mu-2 cos t` produces `f_{m-1,mu}`. Hence

\[
2a_{m,1}=\mu A_m-A_{m-1}.
\]

It follows that

\[
\boxed{
E_m(\mu)=c_m s^{-2m}Q_m(x),
}
\]

with

\[
\boxed{
Q_m(x)
=\frac{4}{x^2-1}
\bigl(xP_{m-1}(x)-P_{m-2}(x)\bigr)^2
+P_{m-1}(x)^2-P_{2m-1}(x).
}
\]

For `m=1`, use the direct formula

\[
\boxed{
Q_1(x)=\frac{(x-1)(3-x)}{x+1}.
}
\]

Thus first-harmonic dominance is reduced to controlling the scalar layers `Q_m(x)`.

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

For `m=1,...,7`, exact Legendre reduction gives

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
\qquad(1\le m\le7,\ \mu\ge4).
}
\]

---

## 4. One-sided bound on the high-`m` tail

Let

\[
d:=\mu-2\ge2.
\]

Since

\[
\mu-2\cos t=d+4\sin^2(t/2),
\]

and for `|t|<=pi`

\[
\sin(|t|/2)\ge\frac{|t|}{\pi},
\]

we obtain

\[
A_{2m}(\mu)
\le\frac{\sqrt d}{4}d^{-2m}I_{2m},
\]

where

\[
I_{2m}:=\int_{-\infty}^{\infty}(1+u^2)^{-2m}\,du.
\]

Since

\[
E_m\ge-c_mA_{2m},
\]

we need only a lower bound on the total tail; no upper bound on its absolute value is required.

Define

\[
K_m:=\frac{m}{4^m}\binom{2m}{m}I_{2m}.
\]

Using

\[
I_{2m}=\pi\frac{\binom{4m-2}{2m-1}}{4^{2m-1}},
\]

one obtains

\[
\boxed{
\frac{K_{m+1}}{K_m}=1-\frac1{16m^2}<1.
}
\]

Thus `K_m` is decreasing. At `m=8`, the elementary bound `pi<22/7` gives exactly

\[
K_8<\sqrt{\frac8{15}}.
\]

Therefore for every `m>=8`,

\[
\boxed{
E_m(\mu)
\ge
-\frac{\sqrt d}{4}\sqrt{\frac8{15}}
\left(\frac4{d^2}\right)^m\frac1{m^2}.
}
\]

Consequently

\[
\boxed{
\sum_{m\ge8}E_m(\mu)
>
-\frac{\sqrt d}{4}\sqrt{\frac8{15}}
\sum_{m\ge8}
\left(\frac4{d^2}\right)^m\frac1{m^2}.
}
\]

Each summand in the positive majorant on the right is proportional to

\[
d^{1/2-2m},
\]

so it decreases strictly with `d` for every `m>=8`. Thus the largest possible negative majorant over `d>=2` occurs at `d=2`.

At `d=2`,

\[
\sum_{m\ge8}\frac1{m^2}
<\int_{15/2}^{\infty}\frac{dt}{t^2}
=\frac2{15}.
\]

Hence, uniformly for `d>=2`,

\[
\boxed{
\sum_{m\ge8}E_m(\mu)
>-rac{2}{15\sqrt{15}}.
}
\]

This is deliberately a one-sided estimate.

---

## 5. Near-boundary region `4<=mu<=4.1`

Here

\[
2\le d\le\frac{21}{10}.
\]

The inequalities

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

On this interval the exact certificate proves

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

Define

\[
L_*:=
\sum_{m=1}^{7}
 c_m\left(\frac{100}{1281}\right)^m\beta_m.
\]

The exact certificate gives

\[
L_*\approx0.03540312
\]

and verifies

\[
\boxed{
L_*^2>\frac4{3375}.
}
\]

Since `L_*>0`, this is equivalent to

\[
L_*>\frac{2}{15\sqrt{15}}.
\]

Combining the low-layer lower bound with the one-sided tail estimate gives

\[
\boxed{
B_{\mu,1}-\sum_{n\ge2}B_{\mu,n}>0
\qquad(4\le\mu\le4.1).
}
\]

---

## 6. Far region `mu>=4.1`: corrected tail estimate

Now

\[
d\ge\frac{21}{10}.
\]

Because the layers `E_2,...,E_7` are nonnegative, it suffices to retain only `E_1` and a one-sided lower bound for the tail `m>=8`.

Let

\[
r:=\frac{\mu-\sqrt{\mu^2-4}}2,
\qquad
u:=r^2.
\]

The `m=1` layer is

\[
E_1
=\frac{4r^4(1-2r^2)}{(1-r^2)^3}.
\]

For `mu>=4.1`, one has

\[
\nu<\frac1{14}.
\]

Indeed `nu<1/14` is equivalent to `13mu<15s`, and after squaring it is enough that `mu^2>225/14`, which holds for `mu>=41/10`.

A direct algebraic subtraction gives

\[
E_1-4\left(\frac{\mu}{\mu^2-1}\right)^4
=
\frac{4\nu^3 P(\nu)}{(\nu-1)^3(\nu^2+\nu+1)^4},
\]

where

\[
P(\nu)
=2\nu^8+7\nu^7+15\nu^6+21\nu^5+25\nu^4
+16\nu^3+\nu^2-5\nu-1.
\]

For `0<nu<=1/14`, the positive part

\[
2\nu^8+7\nu^7+15\nu^6+21\nu^5+25\nu^4+16\nu^3+\nu^2
\]

is increasing and is already `<1` at `nu=1/14`. Hence `P(nu)<0`. Since `(nu-1)^3<0`, we obtain

\[
\boxed{
E_1(\mu)
\ge4\left(\frac{\mu}{\mu^2-1}\right)^4.
}
\]

Now put

\[
y:=\frac4{d^2}.
\]

For `d>=21/10`,

\[
0<y\le y_0:=\frac{400}{441}.
\]

Write

\[
\sum_{m\ge8}\frac{y^m}{m^2}
=y^8\sum_{k\ge0}\frac{y^k}{(k+8)^2}.
\]

The bracket is increasing in `y`. The exact certificate proves the rational endpoint estimate

\[
\boxed{
\sum_{k\ge0}\frac{y_0^k}{(k+8)^2}<\frac1{15}.
}
\]

For reproducibility, it bounds the terms `k=0,...,14` exactly and the remaining tail geometrically. Therefore

\[
\boxed{
\sum_{m\ge8}\frac{y^m}{m^2}<\frac1{15}y^8
\qquad(d\ge21/10).
}
\]

Substitution into the high-`m` lower bound gives

\[
\boxed{
\sum_{m\ge8}E_m(\mu)
>
-T_*(d),
}
\]

where

\[
T_*(d)
:=
\frac{\sqrt d}{60}\sqrt{\frac8{15}}
\left(\frac4{d^2}\right)^8.
\]

It remains to compare the lower bound for `E_1` with `T_*`.

Up to a positive constant their ratio is

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

Thus the comparison is hardest at `d=21/10`. The corrected exact endpoint inequality is

\[
\boxed{
16\left(
\frac{41/10}{(41/10)^2-1}
\right)^8
>
\frac{4^{16}}{3600}\frac8{15}
\left(\frac{10}{21}\right)^{31}.
}
\]

It is verified by exact rational arithmetic in the certificate. Therefore

\[
E_1>T_*(d)
\qquad(d\ge21/10),
\]

and hence

\[
E_1+\sum_{m\ge8}E_m>0.
\]

Since `E_2,...,E_7>=0`, we conclude

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
B_{\mu,1}>\sum_{n\ge2}B_{\mu,n}
\qquad\text{for every }\mu\ge4.
}
\]

This is uniform: it contains no prime, no character, and no finite-world parameter.

---

## Theorem H15.138 — every nontrivial even Dirichlet-character Mahler mode is nonzero

Let `p` be any odd prime and let `chi mod p` be any nontrivial even character.

From the Mahler–Dirichlet–Gauss bridge,

\[
\widehat f_\mu(\chi)
=-\frac12\tau(\overline\chi)\chi(2)
\sum_{\substack{n\ge1\\p\nmid n}}B_{\mu,n}\chi(n).
\]

Since `|chi(n)|<=1`,

\[
\left|
\sum_{\substack{n\ge2\\p\nmid n}}B_{\mu,n}\chi(n)
\right|
\le\sum_{n\ge2}B_{\mu,n}<B_{\mu,1}.
\]

The `n=1` term therefore cannot be cancelled. Since the Gauss sum of a nontrivial character modulo the prime `p` is nonzero,

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
\boxed{\lambda\le0,}
\]

the centered primitive Mahler response operator is invertible on the entire zero-sum signless reaction space

\[
\mathbf C[G_p]_0,
\qquad
G_p=\mathbf F_p^\times/\{\pm1\}.
\]

For `p=3` this space is zero-dimensional and the statement is vacuous; for every odd prime `p>=5` it is the genuine character-by-character nonvanishing theorem above.

---

## 7. Resolution of the `p=43,q=8` obstruction

The channel

\[
(p,q)=(43,8)
\]

was the first one that escaped both earlier automatic certificate templates:

- order-Abel failed;
- single-phase shifted moment-Abel failed.

H15.137–139 show that this was not a genuine Mahler observer resonance:

\[
\boxed{
F_{43,8}(\mu)\ne0
\qquad\forall\mu\ge4.
}
\]

The obstruction occurred because the individual twisted moments rotate too much for a common half-plane certificate, while the actual Mahler harmonic weights obey the stronger global first-harmonic dominance inequality.

---

## 8. Return to the non-Abelian square

Earlier H15 layers established:

- the commutator square defect is
  \[
  [R,S]=R^2;
  \]
- the fourth spectral moment is the first local moment sensitive to this square holonomy;
- the first channel-dependent term in the large-`mu` Mahler expansion occurs at order `mu^{-4}` and is the harmonic `cos(2alpha)`.

The present theorem adds the global inequality

\[
\boxed{
B_{\mu,1}>\sum_{n\ge2}B_{\mu,n}
\qquad(\mu\ge4).
}
\]

Thus the first channel-dependent Mahler harmonic remains dominant on the entire nonpositive spectral half-line, not merely asymptotically.

The rigorous chain is

\[
\boxed{
\text{noncommuting dihedral ports}
\to
\text{square commutator holonomy}
\to
\text{first channel-dependent Mahler harmonic}
\to
\text{universal harmonic dominance}
\to
\text{all-prime character nonvanishing}
\to
\text{full linear reaction tomography}.
}
\]

The wording deliberately avoids a stronger causal claim than the proved spectral identities support.

---

## 9. Claim boundary and publication status

The proof uses classical components:

- Fourier/Parseval identities;
- the Legendre formula for powers of the resolvent kernel;
- Wallis/Beta integrals;
- central-binomial estimates;
- Abel/geometric tail bounds;
- exact rational interval certification of finitely many low-layer polynomial bounds.

The H15-specific candidate theorem is their synthesis into the universal Mahler first-harmonic dominance inequality and the resulting all-prime non-Abelian reaction tomography.

No novelty-priority claim is made here.

**Publication assessment after v1.1 hostile audit:** the theorem remains above the mathematical publication threshold, but publication assembly should use this audited revision, not the pre-audit draft. A literature/prior-art audit and independent certificate reproduction remain mandatory before Zenodo release.
