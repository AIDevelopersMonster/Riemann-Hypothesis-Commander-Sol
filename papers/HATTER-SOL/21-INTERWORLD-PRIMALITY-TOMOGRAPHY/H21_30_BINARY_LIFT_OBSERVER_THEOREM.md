# HATTER-SOL-21 · BINARY LIFT OBSERVER THEOREM

Status: **EXACT OBSERVER REDUCTION / PUBLICATION-GATE CRITICAL**

## 1. Even scalar fibers

Assume the nonexceptional local world has

\[
d_p=2s_p.
\]

By H21-NL1,

\[
\lambda_p^{s_p}=-1.
\]

Every scalar exponent

\[
k\in\mathbf Z/2s_p\mathbf Z
\]

has a unique decomposition

\[
\boxed{
k=k_0+\beta s_p,
\qquad
0\le k_0<s_p,
\quad
\beta\in\{0,1\}.
}
\]

Hence

\[
\boxed{
\lambda_p^k
=
(-1)^\beta\lambda_p^{k_0}.
}
\]

The norm-square datum determines \(k_0\) modulo \(s_p\); \(\beta\) is the only
remaining scalar ambiguity.

## Theorem H21-BL1 — binary lift form

Fix projective phase \(r\), incoming character sign, and an optional observer
target

\[
t_j(r)\in D_p.
\]

Suppose norm compatibility holds:

\[
\boxed{
t_j(r)^2
=
(-C)^{m-r}.
}
\]

Let \(z_0(r,m)\) be either one of the two norm-compatible scalar roots.
Then the selected scalar coordinate is

\[
z_p=(-1)^\beta z_0,
\]

while the observer target is

\[
t_j(r)=(-1)^{\beta_j^*}z_0
\]

for a uniquely determined target lift bit

\[
\beta_j^*\in\{0,1\}.
\]

Therefore

\[
\boxed{
j\in Z
\iff
\beta=\beta_j^*.
}
\]

If norm compatibility fails, the optional zero bit is impossible regardless of
the lift bit.

## Corollary H21-BL2 — no residual coordinate for odd fibers

If \(d_p\) is odd, the norm determines the scalar coordinate uniquely and no
lift bit exists.

Thus after projective phase and norm data are fixed, the local H21 observer has:

- zero residual scalar degrees of freedom when \(d_p\) is odd;
- exactly one binary residual degree of freedom when \(d_p\) is even.

## Corollary H21-BL3 — two optional bits share one lift

If two optional targets are simultaneously norm-compatible on the same
projective ray, their target lift bits satisfy

\[
\beta_0^*,\beta_1^*\in\{0,1\}
\]

and both are tested against the **same** actual lift bit \(\beta\).

Thus the two observer bits cannot carry independent scalar randomness.

Their joint state is one of:

- neither target matches the selected sheet;
- exactly one target matches;
- both match, only if the two targets coincide.

The last case is already restricted by H21-SF3 to the distinguished prime-law
projective ray.

## 2. Canonical lift coordinate

Let

\[
k=\frac{m-r}{e_p}\pmod{d_p}.
\]

For even \(d_p=2s_p\), define

\[
\boxed{
\beta_p(m)
=
\left\lfloor\frac{k}{s_p}\right\rfloor
\in\{0,1\},
}
\]

using the canonical representative \(0\le k<2s_p\).

Equivalently, \(\beta_p\) records which of the two points

\[
z,\ -z
\]

above the norm-square datum is selected.

This coordinate depends on the chosen generator \(\lambda_p\), but the
two-sheet structure itself is intrinsic.

## 3. Reciprocal semiprime reduction

For \(n=pq\), after fixing:

- the world;
- character stratum;
- projective phases;
- norm compatibility classes;

every even-fiber direction contributes at most one bit

\[
\beta_{p\leftarrow q},
\qquad
\beta_{q\leftarrow p}.
\]

Therefore the remaining reciprocal observer problem is a joint law on

\[
\boxed{
\{0,1\}\times\{0,1\}.
}
\]

For one optional norm-compatible target per direction, define target-match
events

\[
M_p=\mathbf1_{\{\beta_p=\beta_p^*\}},
\qquad
M_q=\mathbf1_{\{\beta_q=\beta_q^*\}}.
\]

Then the residual same-mask dependence is controlled by the Bernoulli pair

\[
(M_p,M_q).
\]

## 4. Exact binary covariance

For any conditioned arithmetic stratum in which the local mask difference is
determined solely by these two target-match events,

\[
\boxed{
\operatorname{Cov}(M_p,M_q)
=
\Pr[M_p=M_q=1]
-
\Pr[M_p=1]\Pr[M_q=1].
}
\]

This is the final scalar-level dependence after the exact projective and norm
reductions.

The next arithmetic question is whether reciprocal prime sampling imposes a
nontrivial law on

\[
(\beta_p,\beta_q)
\]

or on the target-adjusted bits

\[
\gamma_p=\beta_p\oplus\beta_p^*,
\qquad
\gamma_q=\beta_q\oplus\beta_q^*.
\]

Optional incidence is exactly

\[
\gamma=0.
\]

## 5. Publication significance

The double-cover itself is classical cyclic-group structure.

The H21-specific result is the observer reduction:

\[
\boxed{
\text{quadratic Frobenius local phase}
\to
\text{projective ray}
\to
\text{norm class}
\to
\text{at most one binary observer lift}.
}
\]

A publication-level arithmetic contribution would require a nontrivial theorem
for reciprocal lift sampling or a measured compiler/hardware advantage caused
by this reduction.
