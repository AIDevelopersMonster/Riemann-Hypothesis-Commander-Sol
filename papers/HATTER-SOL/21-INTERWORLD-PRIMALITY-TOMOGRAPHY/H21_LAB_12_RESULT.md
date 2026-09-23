# HATTER-SOL-21 · H21-LAB-12 RESULT

Status: **CI REPRODUCED / CHARACTER-MIXTURE MECHANISM TOO SMALL**

Run:

\`35704817620\`

## 1. Exact decomposition validated

For every scanned world,

\[
\boxed{
K
=
K_{\rm within}
-
H_{\rm char}
}
\]

with

\[
K_{\rm within}
=
\sum_s w_s K_s
\]

over the three split/inert strata

\[
s\in\{++, +-, --\},
\]

and

\[
\boxed{
H_{\rm char}
=
\sum_a
\operatorname{Var}_S(\pi_S(a))
\ge0.
}
\]

Maximum decomposition error:

\[
3.03\times10^{-16}.
\]

Thus the theorem is numerically verified to floating-point precision.

## 2. Character heterogeneity is always a negative contribution

As proved,

\[
-H_{\rm char}\le0.
\]

Therefore mixing split/split, split/inert, and inert/inert populations can only
push total coupling downward.

This is a genuine arithmetic source of negative \(K\).

## 3. But it is not the dominant source

For the broad scan

\[
|D|\le255,
\]

with

\[
156
\]

fundamental worlds and

\[
2162
\]

common-core semiprime pairs,

\[
\boxed{
\operatorname{mean} H_{\rm char}
=
0.000069
}
\]

while

\[
\boxed{
\operatorname{mean}|K_{\rm within}|
=
0.002505
}
\]

and

\[
\boxed{
\operatorname{mean}|K|
=
0.002572.
}
\]

Thus the split/inert-mixture penalty is only a small correction to the total
coupling.

Among the

\[
150
\]

non-torsion worlds with negative \(K\),

\[
\boxed{
0/150
}
\]

have

\[
H_{\rm char}\ge\frac12|K|,
\]

and likewise

\[
\boxed{
0/150
}
\]

have

\[
H_{\rm char}\ge|K|.
\]

Therefore the dominant negative coupling persists **inside** fixed
split/inert classes.

## 4. Strong examples

For

\[
D=5,
\]

\[
K=-0.008418,
\]

but

\[
H_{\rm char}=0.000112,
\]

so only about

\[
\boxed{1.3\%}
\]

of the negative coupling magnitude is explained by character-mixture
heterogeneity.

The residual is

\[
\boxed{
K_{\rm within}=-0.008306.
}
\]

Likewise for

\[
D=-84,
\]

\[
K=-0.008014,
\]

\[
H_{\rm char}=0.000209,
\]

so only about

\[
2.6\%
\]

is explained by the split/inert mixture.

## 5. Positive worlds obey the theorem sharply

For the small set of positive-coupling worlds, for example

\[
D=93,
\]

\[
K=+0.000125,
\]

\[
K_{\rm within}=+0.000192,
\]

\[
H_{\rm char}=0.000067.
\]

Thus positive total coupling occurs only because the within-stratum repulsion
is strong enough to overcome the universal negative heterogeneity penalty.

This exactly matches H21-CS3.

## 6. Negative conclusion

The hypothesis

\[
\boxed{
\text{most negative }K
\text{ is caused by mixing split/inert populations}
}
\]

is false on the broad finite family.

Quadratic-character type explains only a minor part of the observed
synchronization.

Therefore no further effort should be spent trying to explain coupling from
Legendre/Jacobi signs alone.

## 7. Surviving mechanism

The dominant object is

\[
\boxed{
K_s
}
\]

inside a fixed character stratum.

There, the signs

\[
\chi_p,\chi_q
\]

are already frozen.

The only remaining source of synchronization is the Lucas-clock geometry:

\[
q\bmod\lambda_W(p),
\qquad
p\bmod\lambda_W(q),
\]

together with the exact zero conditions on

\[
U_{q-1},U_q,U_{q+1}\pmod p
\]

and the reciprocal system modulo \(q\).

Hence the next H21 target is no longer quadratic reciprocity.

It is **reciprocal Lucas phase synchronization inside fixed split/inert
classes**.

## 8. Next theorem target

For each stratum

\[
s\in\{++, +-, --\},
\]

construct the local phase map

\[
\Lambda_{W,p}^{(s)}:
q\bmod\lambda_W(p)
\mapsto
Z_{p\leftarrow q}.
\]

Then study reciprocal prime pairs satisfying simultaneously

\[
q\bmod\lambda_W(p)
\in A_{p,a},
\]

\[
p\bmod\lambda_W(q)
\in A_{q,a}
\]

for the same mask \(a\).

The theorem target is a criterion or density estimate for these reciprocal
phase coincidences.

## 9. Current strongest H21 reduction

The coupling problem has now been reduced from

\[
\text{all semiprime arithmetic}
\]

to

\[
\boxed{
\text{reciprocal Lucas-clock synchronization inside fixed character strata}.
}
\]

This is the narrowest surviving mechanism after the sign-only and
character-mixture controls.
