# HATTER-SOL-21 · DEFECT-SURFACE FACTORIZATION LAB

Status: **ACTIVE EXACT FINITE LAB**

## 1. Observable

For each quadratic world \(W=(B,C,\Delta)\), compute

\[
x^n=(u_W,v_W)
\]

in

\[
(\mathbb Z/n\mathbb Z)[x]/(x^2-Bx-C).
\]

For Jacobi sign \(j=(\Delta/n)\in\{\pm1\}\), the expected prime response is

\[
E_W(n)=
\begin{cases}
(0,1),&j=+1,\\
(B,-1),&j=-1.
\end{cases}
\]

Define the Frobenius defect

\[
\delta_W(n)=(d_{0,W},d_{1,W})
=
(u_W,v_W)-E_W(n)\pmod n.
\]

The factor projections are

\[
g_{0,W}=\gcd(n,d_{0,W}),
\]

\[
g_{1,W}=\gcd(n,d_{1,W}),
\]

\[
g_{01,W}=\gcd(n,d_{0,W},d_{1,W}).
\]

Any value strictly between \(1\) and \(n\) is an explicit proper divisor.

Precheck gcd witnesses from \(2C\Delta\) are retained as part of the same world
response.

## 2. Surface fingerprint

For the six frozen real worlds

\[
\Delta=-7,\ 5,\ -3,\ -11,\ 13,\ -19,
\]

define the factor fingerprint

\[
\Phi(n)
=
(F_1(n),\ldots,F_6(n)),
\]

where \(F_i(n)\) is the set of proper divisors exposed by handle \(i\).

The primary finite observables are:

- any-factor coverage;
- number of distinct divisor witnesses;
- number of distinct prime divisors covered by those witnesses;
- coverage by factor-shape class;
- marginal factor yield per world;
- first-factor revelation time under an ordered world list.

## 3. Static world-order optimization

For a permutation

\[
\pi\in S_6
\]

define

\[
\tau_\pi^{\rm factor}(n)
=
\min\{k:F_{\pi_k}(n)\ne\varnothing\},
\]

with unresolved penalty \(7\).

Because there are only

\[
6!=720
\]

orders, H21-LAB-05 exhausts every order exactly.

Two costs are reported:

\[
C_{\rm all}(\pi)
=
\frac1{|C|}
\sum_{n\in C}
\min(\tau_\pi^{\rm factor}(n),7),
\]

over all composites in the finite range, and

\[
C_{\rm hit}(\pi)
=
\frac1{|C_{\rm hit}|}
\sum_{n\in C_{\rm hit}}
\tau_\pi^{\rm factor}(n),
\]

over composites for which at least one of the six worlds exposes a factor.

This separates world-family coverage from ordering efficiency.

## 4. Exact controls

The lab knows the true factorization only for post-hoc evaluation.

The world engine itself receives only \(n\) and the world descriptor.

Prime inputs must never produce a proper divisor witness.

For semiprimes \(pq\), one proper divisor completes the factorization because
the complementary factor is \(n/d\).

For numbers with more prime factors, the lab separately records whether the
union of world witnesses covers all distinct prime divisors.

## 5. Hardware interpretation

The FPGA datapath already computes \(d_0,d_1\).

H21-HW-01 therefore needs only:

- one or more binary gcd engines;
- proper-divisor comparators;
- a factor register;
- a world scheduler.

The exact finite order optimization supplies the first frozen scheduling
candidate for hardware.

## 6. Claim boundary

A high factor-exposure percentage is not a new factorization theorem.

The scientifically interesting outcomes are narrower:

- exact finite world-order optimality under the frozen family;
- a structural factor-exposure law by arithmetic class;
- a later theorem explaining why particular worlds split the composite
  population in complementary ways;
- or a hardware theorem comparing sequential/interleaved/parallel factor
  revelation.
