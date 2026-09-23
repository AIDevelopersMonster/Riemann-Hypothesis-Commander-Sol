# HATTER-SOL-21 · FIXED-STRATUM CLOCK SYNCHRONIZATION TARGET

Status: **NEXT ACTIVE THEOREM STRIKE**

## 1. Frozen character regime

Fix

\[
(\chi_p,\chi_q)
\in
\{(+,+),(+,-),(-,+),(-,-)\}.
\]

After orientation symmetrization this reduces to

\[
++,\quad+-,\quad--.
\]

The character signs are now constants, so all zero-mask structure is generated
by Lucas congruences alone.

## 2. Phase sets

For every prime \(p\), world \(W\), and mask \(a\), define

\[
A_{W,p}^{(a,s)}
=
\left\{
r\bmod\lambda_W(p):
L_W(p\leftarrow r)=a
\text{ in stratum }s
\right\}.
\]

Then same-mask synchronization for a prime pair \((p,q)\) is exactly

\[
\boxed{
q\bmod\lambda_W(p)
\in
A_{W,p}^{(a,s)}
}
\]

and

\[
\boxed{
p\bmod\lambda_W(q)
\in
A_{W,q}^{(a,s)}.
}
\]

This is a reciprocal modular incidence problem.

## 3. Immediate finite objects

For each stratum build:

- local phase-set sizes;
- phase-set densities;
- clock gcd
  \[
  g_{pq}=\gcd(\lambda_W(p),\lambda_W(q));
  \]
- reciprocal compatibility counts;
- same-mask excess over independent phase density.

## 4. First theorem candidates

### Clock-coprime heuristic

If

\[
\gcd(\lambda_W(p),\lambda_W(q))=1,
\]

test whether reciprocal synchronization is closer to independence.

### Shared-clock hypothesis

Large

\[
\gcd(\lambda_W(p),\lambda_W(q))
\]

may force shared modular constraints and increase same-mask attraction.

### Phase-density criterion

For each mask compare observed reciprocal coincidence with

\[
\frac{|A_{W,p}^{(a,s)}|}{\lambda_W(p)}
\cdot
\frac{|A_{W,q}^{(a,s)}|}{\lambda_W(q)}.
\]

The discrepancy is the fixed-stratum analogue of \(c_a\).

## 5. Negative control

Do not assume shared clock gcd is sufficient.

Two worlds can have similar order statistics and very different exposure.

Any successful criterion must use both:

\[
\text{clock arithmetic}
\]

and

\[
\text{mask phase sets}.
\]

## 6. Hardware relevance

If reciprocal synchronization can be approximated from compact descriptors such
as

\[
(\lambda_W(p),|A_{W,p}^{(a,s)}|)
\]

plus a small compatibility table, then the world compiler can estimate
coupling without full pairwise semiprime training.
