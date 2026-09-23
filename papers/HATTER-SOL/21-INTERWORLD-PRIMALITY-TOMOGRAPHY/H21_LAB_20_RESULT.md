# HATTER-SOL-21 · H21-LAB-20 RESULT

Status: **CI REPRODUCED / NORM-LIFT DOUBLE-COVER THEOREM VALIDATED**

Run:

\`35738442661\`

Largest validation grid:

\[
p\le509,
\qquad
|D|\le127.
\]

## 1. Validation totals

World/prime rows:

\[
\boxed{7149}.
\]

Failures:

\[
\boxed{0}.
\]

Norm-phase checks:

\[
\boxed{45873}.
\]

Exact odd-fiber scalar reconstructions:

\[
\boxed{15313}.
\]

## 2. Exact scalar-fiber law

Let

\[
t_p=\operatorname{ord}_p(-C),
\qquad
s_p=\frac{t_p}{\gcd(t_p,e_p)}.
\]

Then every tested case satisfies

\[
\boxed{
\frac{d_p}{\gcd(d_p,2)}=s_p.
}
\]

Therefore

\[
\boxed{
d_p\in\{s_p,2s_p\}.
}
\]

If \(s_p\) is even, only the second alternative is possible.

All

\[
4541
\]

even-\(d_p\) cases satisfied

\[
\boxed{d_p=2s_p}.
\]

## 3. Norm determines the scalar coordinate up to at most one bit

For

\[
m=r+k e_p,
\]

put

\[
z_p=\lambda_p^k.
\]

Every tested phase satisfies

\[
\boxed{
z_p^2=(-C)^{m-r}.
}
\]

### Odd scalar fiber

Rows with odd \(d_p\):

\[
\boxed{2608}
\]

or

\[
\boxed{36.480627\%}.
\]

In this regime the squaring map on \(D_p\) is bijective and

\[
\boxed{
z_p=
\left((-C)^{m-r}\right)^{(d_p+1)/2}.
}
\]

Thus the scalar coordinate is completely norm-determined once the projective
phase is fixed.

### Even scalar fiber

Rows with even \(d_p\):

\[
\boxed{4541}
\]

or

\[
\boxed{63.519373\%}.
\]

In this regime the norm determines exactly two scalar lifts,

\[
z,\ -z.
\]

The only scalar information not visible from the norm is a binary sheet bit.

## 4. Structural reduction

The old local phase coordinate

\[
m\bmod h_p
\]

has now been reduced exactly to

\[
\boxed{
\text{projective phase }r
+
\text{norm datum}
+
\text{at most one binary lift bit}.
}
\]

Thus the unresolved reciprocal scalar mechanism is not a correlation between
large arbitrary cyclic coordinates.

It is, at worst, a correlation between two binary lift choices after
projective and norm data are fixed.

## 5. Compiler/hardware consequence

A compiled observer need not represent the scalar fiber as an arbitrary
\(d_p\)-state lookup.

For odd \(d_p\), the scalar target test can be expressed through base-field
norm arithmetic.

For even \(d_p\), one additional sign/lift bit suffices.

This is a concrete representation compression candidate for FPGA comparison.

## 6. Publication consequence

LAB-20 materially advances Gate A/E of the H21 publication monitor because the
remaining reciprocal mechanism has been reduced to a binary lift problem.

However publication is not declared until:

1. the reduction is audited against finite-field / Frobenius / Lucas prior art;
2. either the reciprocal lift bit is controlled arithmetically or the
   projective/norm representation yields a measured hardware advantage.
