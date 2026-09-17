# HATTER-SOL-15 · Hostile Proof Audit of Universal First-Harmonic Dominance

**Target:** `UNIVERSAL_FIRST_HARMONIC_DOMINANCE_AND_ALL_PRIME_TOMOGRAPHY.md`  
**Audited revision:** v1.1  
**Status:** theorem survives audit after two repairs described below.

---

## 1. Audit scope

The audit independently rechecked the following chain:

\[
B_{\mu,1}-\sum_{n\ge2}B_{\mu,n}
=
\sum_{m\ge1}E_m(\mu),
\]

\[
E_m=c_m\left(4a_{m,1}^2+a_{m,0}^2-A_{2m}\right),
\qquad
c_m=\frac1m\binom{2m}{m},
\]

\[
A_k=s^{-k}P_{k-1}(x),
\qquad
s=\sqrt{\mu^2-4},
\quad
x=\mu/s,
\]

and the decomposition of the proof into:

- nonnegative low layers `m=1,...,7`;
- a near-boundary region `4<=mu<=4.1`;
- a far region `mu>=4.1` controlled by `E_1` plus a negative-tail majorant.

The audit also rederived the explicit low-layer polynomials and spot-checked the theorem numerically at several `mu` values.

---

## 2. Identity checks

### A. Parseval layer identity

Starting from

\[
B_{\mu,n}=2\sum_{m\ge1}c_m a_{m,n}^2,
\]

we have

\[
B_{\mu,1}-\sum_{n\ge2}B_{\mu,n}
=
\sum_m2c_m\left(a_{m,1}^2-\sum_{n\ge2}a_{m,n}^2\right).
\]

Since

\[
A_{2m}=a_{m,0}^2+2a_{m,1}^2+2\sum_{n\ge2}a_{m,n}^2,
\]

this equals

\[
\sum_mc_m\left(4a_{m,1}^2+a_{m,0}^2-A_{2m}\right).
\]

**Audit result:** correct.

### B. First Fourier coefficient recurrence

From

\[
(\mu-2\cos t)f_{m,\mu}(t)=f_{m-1,\mu}(t),
\]

averaging gives

\[
\mu A_m-2a_{m,1}=A_{m-1}.
\]

**Audit result:** correct.

### C. Legendre reduction

Using the classical resolvent-power identity

\[
A_k=s^{-k}P_{k-1}(x),
\]

one obtains

\[
E_m=c_ms^{-2m}Q_m(x)
\]

with

\[
Q_m(x)=
\frac4{x^2-1}
\bigl(xP_{m-1}(x)-P_{m-2}(x)\bigr)^2
+P_{m-1}(x)^2-P_{2m-1}(x).
\]

An independent symbolic derivation reproduced exactly the stored polynomials `H_m` for `m=2,...,7` after setting `x=1+y`.

**Audit result:** correct.

---

## 3. Low-layer positivity

For `mu>=4`,

\[
0\le y=x-1\le1/6.
\]

Independent symbolic factorization gives

\[
Q_m(1+y)=yH_m(y)
\]

with exactly the coefficients stored in the certificate.

The audited exact interval certificate proves

\[
H_m(y)>0
\quad
(2\le m\le7,\ 0\le y\le1/6),
\]

while `H_1(y)=(2-y)/(2+y)>0` directly.

Therefore

\[
E_m\ge0
\quad
(1\le m\le7).
\]

**Audit result:** correct.

---

## 4. Tail estimate and the first repaired defect

The proof only needs a **one-sided** estimate

\[
\sum_{m\ge8}E_m>-T.
\]

The first draft described this as an absolute-value estimate. That wording was unjustified because the bound

\[
E_m\ge-c_mA_{2m}
\]

is only one-sided.

The audited revision now states the correct form throughout.

From the comparison integral,

\[
A_{2m}
\le
\frac{\sqrt d}{4}d^{-2m}I_{2m},
\quad d=\mu-2,
\]

and

\[
K_m:=\frac{m}{4^m}\binom{2m}{m}I_{2m},
\]

independent algebra gives

\[
\frac{K_{m+1}}{K_m}
=
\frac{(4m-1)(4m+1)}{16m^2}
=1-\frac1{16m^2}.
\]

Thus `K_m` decreases. The check

\[
K_8<\sqrt{8/15}
\]

is valid.

Hence

\[
E_m
\ge
-\frac{\sqrt d}{4}\sqrt{\frac8{15}}
\left(\frac4{d^2}\right)^m\frac1{m^2}.
\]

**Audit result after wording repair:** correct.

---

## 5. Near-boundary region

For

\[
4\le\mu\le4.1,
\]

the proof uses

\[
1/7\le y\le1/6
\]

and exact rational lower bounds `beta_m` for `Q_m`.

Independent extremum checks confirm that the chosen rational values lie below the true minima on this interval.

The exact certificate gives

\[
L_*\approx0.03540311582
\]

while

\[
\frac{2}{15\sqrt{15}}
\approx0.03442651863.
\]

Thus the positive low-layer contribution strictly dominates the worst one-sided tail majorant.

**Audit result:** correct.

---

## 6. Far region and the second repaired defect

The first draft used

\[
\sum_{m\ge8}\frac{y^m}{m^2}
\le
\frac{y^8}{64(1-y)}
\le
\frac2{15}y^8
\qquad(d\ge21/10).
\]

The second inequality is **false** at the endpoint `d=21/10`.

This was the substantive defect found by hostile audit.

The theorem nevertheless survives because the required endpoint series admits a stronger exact bound.

Let

\[
y_0=400/441.
\]

Then for `0<y<=y_0`,

\[
\sum_{m\ge8}\frac{y^m}{m^2}
=y^8
\sum_{k\ge0}\frac{y^k}{(k+8)^2}.
\]

The bracket increases with `y`, and exact rational arithmetic proves

\[
\sum_{k\ge0}\frac{y_0^k}{(k+8)^2}<\frac1{15}.
\]

The certificate proves this by summing `k=0,...,14` exactly and bounding the remainder geometrically.

Therefore

\[
\sum_{m\ge8}\frac{y^m}{m^2}<\frac1{15}y^8.
\]

This yields the corrected tail majorant

\[
T_*(d)
=
\frac{\sqrt d}{60}\sqrt{\frac8{15}}
\left(\frac4{d^2}\right)^8.
\]

The far proof also uses

\[
E_1\ge4\left(\frac\mu{\mu^2-1}\right)^4.
\]

An independent symbolic subtraction reproduces the polynomial criterion used in v1.1, and the condition `r^2<1/14` is valid for `mu>=4.1`.

The ratio of this lower bound to `T_*` is increasing in `d`, since

\[
\frac{R'}R
=
\frac{23d^3+154d^2+301d+186}
{2d(d+1)(d+2)(d+3)}>0.
\]

The corrected endpoint comparison is

\[
16\left(
\frac{41/10}{(41/10)^2-1}
\right)^8
>
\frac{4^{16}}{3600}\frac8{15}
\left(\frac{10}{21}\right)^{31},
\]

and the exact squared ratio is greater than `5`.

**Audit result after repair:** correct.

---

## 7. Independent numerical sanity check

A direct Fourier quadrature, not used in the proof, gives approximately:

\[
\begin{array}{c|c}
\mu&B_{\mu,1}-\sum_{n\ge2}B_{\mu,n}\\
\hline
4&0.03767\\
4.1&0.03558\\
5&0.01105\\
10&0.0004488
\end{array}
\]

All are comfortably positive and consistent with the theorem and asymptotic regime.

These values are sanity checks only, not proof inputs.

---

## 8. Character-theoretic consequence

Once

\[
B_{\mu,1}>\sum_{n\ge2}B_{\mu,n}
\]

is established, every nontrivial even character satisfies

\[
\left|
\sum_{n\ge2}B_{\mu,n}\chi(n)
\right|<B_{\mu,1}.
\]

Thus the `n=1` term cannot be cancelled. Together with the nonzero Gauss sum this proves

\[
\widehat f_\mu(\chi)\ne0.
\]

**Audit result:** correct.

---

## 9. Audit verdict

The hostile audit found two real defects in the pre-audit draft:

1. an incorrect far-region geometric-tail inequality;
2. an overstatement of a one-sided tail estimate as an absolute-value estimate.

Both have been repaired in v1.1. The replacement far-tail estimate is exact, reproducible, and leaves a large endpoint margin.

No further contradiction was found in the audited chain.

Therefore the current internal status is:

\[
\boxed{
\text{H15.137--H15.139 survive hostile proof audit.}
}
\]

This is still not a substitute for external peer review or a prior-art search. Before publication, the required next steps are:

- reproduce the exact certificate in a clean environment;
- audit bibliography and priority claims;
- assemble the theorem with all dependencies stated explicitly;
- keep the pre-audit draft out of the publication package.
