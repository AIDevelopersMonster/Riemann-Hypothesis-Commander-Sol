# HATTER-SOL-21 · H21-LAB-15 RESULT

Status: **CI REPRODUCED / COARSE CLOCK-LOCK EXPLANATION REJECTED**

Run:

\`35717473749\`

## 1. Exact theorem validation

Inside each fixed character stratum,

\[
\boxed{
K_s
=
K_{s,\mathrm{within-lock}}
-
H_{s,\mathrm{lock}}
}
\]

was verified.

Maximum decomposition error:

\[
3.23\times10^{-16}.
\]

## 2. Broad result

For

\[
|D|\le255,\qquad pq<2^{18},\qquad p,q>255,
\]

there are

\[
460
\]

eligible world/character rows.

Mean lock-mixture penalty:

\[
\boxed{
\operatorname{mean}H_{\rm lock}=0.000381.
}
\]

Mean residual coupling remaining inside lock classes:

\[
\boxed{
\operatorname{mean}|K_{\rm within-lock}|=0.002906.
}
\]

Mean original fixed-stratum coupling magnitude:

\[
\boxed{
\operatorname{mean}|K_s|=0.003166.
}
\]

Thus the coarse lock partition removes only a small fraction of the coupling.

Among

\[
272
\]

negative fixed-stratum rows,

only

\[
\boxed{
13/272
}
\]

satisfy

\[
H_{\rm lock}\ge\frac12|K_s|,
\]

and only

\[
\boxed{
6/272
}
\]

satisfy

\[
H_{\rm lock}\ge|K_s|.
\]

## 3. Stable conclusion

The \(|D|\le127\) scan gives the same conclusion:

\[
\operatorname{mean}H_{\rm lock}=0.000542,
\]

\[
\operatorname{mean}|K_{\rm within-lock}|=0.003035,
\]

\[
\operatorname{mean}|K_s|=0.003546.
\]

Only

\[
10/181
\]

negative rows have \(H_{\rm lock}\ge\frac12|K_s|\).

Therefore the failure is stable across both broad-family controls.

## 4. Negative result

The hypothesis

\[
\boxed{
\text{shared clock size and the three coarse lock classes explain most coupling}
}
\]

is false.

Neither:

- large shared-order fraction;
- \(pq\equiv+1\pmod g\);
- \(pq\equiv-1\pmod g\);
- nor the four-way lock partition

captures the dominant fixed-stratum synchronization.

## 5. What survives

For fixed world \(W\), prime \(p\), and character signs, the reciprocal
direction is controlled by

\[
y=x^q
\]

inside the cyclic subgroup

\[
\boxed{
H_{W,p}=\langle x\rangle\subset A_p^\times.
}
\]

The zero-mask conditions are coordinate conditions on \(y\).

For example, in the split local case \(\chi_p=+1\):

- \(z_1=1\) iff the \(x\)-coordinate of \(y\) equals \(\chi_q\);
- \(z_0=1\) iff the constant coordinate of \(y\) equals
  \[
  \frac{1-\chi_q}{2}B.
  \]

Thus each mask corresponds to incidence of the cyclic orbit

\[
\{x^m:m\in\mathbb Z/h_p\mathbb Z\}
\]

with one or two affine coordinate lines in the two-dimensional algebra.

The coarse order \(h_p\) records only orbit length.

It does **not** record how the orbit intersects those affine lines.

That incidence pattern is the missing observer geometry.

## 6. Revised mechanism

The coupling problem is therefore reduced to:

\[
\boxed{
\text{reciprocal incidence of two cyclic algebra orbits with mask-defining affine lines}.
}
\]

This is strictly finer than:

- quadratic character;
- clock length;
- shared clock gcd;
- plus/minus modular lock.

## 7. Next target

Construct for each local prime \(p\) the exact incidence code

\[
\mathcal I_{W,p}(m)
=
L_W(p\leftarrow m),
\qquad
m\in\mathbb Z/h_p\mathbb Z
\]

with the required character phase attached.

Then study reciprocal pairs

\[
m=q\bmod h_p,
\qquad
n=p\bmod h_q
\]

through the two incidence codes

\[
\mathcal I_{W,p}(m),
\qquad
\mathcal I_{W,q}(n).
\]

The next theorem target is an algebraic description of the mask phase sets as
intersections of the cyclic subgroup \(\langle x\rangle\) with affine lines,
followed by a reciprocal-incidence criterion for same-mask synchronization.
