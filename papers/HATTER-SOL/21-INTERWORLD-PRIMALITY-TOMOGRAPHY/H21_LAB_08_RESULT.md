# HATTER-SOL-21 · H21-LAB-08 RESULT

Status: **CI REPRODUCED / LUCAS COMPILER VALIDATED**

Run:

\`35649401208\`

Range:

\[
pq<2^{18},
\qquad
p\ne q
\]

with odd primes.

Distinct semiprimes:

\[
\boxed{46199}.
\]

## 1. Independent implementation equivalence

The local zero-mask was computed in two independent ways:

1. direct quadratic-algebra exponentiation;
2. Lucas-coordinate formulas from H21-LC1.

Mismatch count:

\[
\boxed{0}.
\]

Thus the Lucas representation is implementation-equivalent to the direct
quadratic defect observer on the complete finite validation set.

## 2. Local clock measurements

| world | eligible pq | exposure | mean log2(h) | unique orders | h<=6 fraction |
|---|---:|---:|---:|---:|---:|
| \(D=-7\) | 42237 | 39.415678% | 20.928661 | 8425 | 0% |
| \(D=5\) | 40846 | 34.466043% | 14.541480 | 7908 | 0% |
| \(D=-3\) | 37719 | 0% | 2.584963 | 1 | 100% |
| \(D=-11\) | 35071 | 27.355935% | 20.977777 | 8394 | 0.011794% |
| \(D=13\) | 35441 | 18.949804% | 20.943918 | 8409 | 0% |
| \(D=-19\) | 39218 | 30.577796% | 20.916352 | 8443 | 0.023588% |

## 3. Torsion-world signature

The \(D=-3\) world has exactly one clock order across all tested
nonexceptional primes:

\[
\boxed{h_{-3}(p)=6}.
\]

Its factor exposure is

\[
\boxed{0}.
\]

This independently reproduces the torsion-world no-go mechanism.

## 4. Clock length is not world quality

The four worlds

\[
D=-7,-11,13,-19
\]

have nearly indistinguishable mean clock lengths:

\[
\operatorname{mean}\log_2 h
\approx20.9,
\]

but their semiprime factor-exposure rates are

\[
39.42\%,\quad27.36\%,\quad18.95\%,\quad30.58\%.
\]

Therefore

\[
\boxed{
\text{large local multiplicative order is not sufficient to predict a good
factor world}.
}
\]

The \(D=5\) world provides a second counterexample: its mean clock order is much
smaller, yet its exposure rate remains high:

\[
\boxed{34.47\%}.
\]

Hence a scalar clock-length score is rejected.

## 5. Correct quality object

H21-SD1 and H21-LC1 show that factor exposure depends on the two-bit local
signature

\[
L_W(p\leftarrow q)
=
Z_{p\leftarrow q}(W),
\]

not merely on the clock period.

The world-quality object must therefore measure how the local clock is
**partitioned into zero-mask phases**.

For fixed \(p\), define the phase map

\[
\boxed{
\Lambda_{W,p}:
q\bmod\lambda_W(p)
\longmapsto
Z_{p\leftarrow q}(W).
}
\]

A useful world needs these maps to produce diverse and asymmetric masks across
prime pairs.

## 6. New compiler architecture

The world compiler becomes:

\[
\boxed{
(B,C,\Delta)
\to
\text{torsion elimination}
\to
h_W(p)
\to
\Lambda_{W,p}
\to
\text{mask diversity}
\to
\text{cross-prime asymmetry}
\to
\text{schedule}.
}
\]

Clock order is a support size / period bound.

Mask geometry on that clock is the actual observer content.

## 7. Hardware consequence

The direct quadratic exponentiation datapath is no longer mathematically
mandatory.

Because

\[
x^m=C U_{m-1}+U_mx,
\]

the factor observer can be realized by a Lucas/matrix recurrence engine that
produces exactly the required coordinates.

This creates a new H21 hardware comparison:

\[
\boxed{
\text{quadratic algebra exponentiation core}
\quad\text{vs}\quad
\text{Lucas recurrence core}.
}
\]

They are mathematically equivalent for the declared observer but may have
different FPGA images.

## 8. Claim boundary

Lucas sequences and Frobenius/Lucas probable-prime machinery are classical.

The exact H21 contribution under study is the observer composition

\[
\text{Lucas clock}
\to
\text{zero-mask phase}
\to
\text{cross-world factor asymmetry}
\to
\text{hardware scheduling}.
\]

Novelty remains unclaimed pending dedicated literature audit.
