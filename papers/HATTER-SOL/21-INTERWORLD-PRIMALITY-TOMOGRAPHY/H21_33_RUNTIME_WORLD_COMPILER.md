# HATTER-SOL-21 · RUNTIME-SAFE WORLD COMPILER

Status: **OPERATIONAL COMPILER / HARDWARE-SAFE EXPERIMENT**

## 1. Runtime-safe objective

The compiler may use an offline labeled population for optimization, but every
runtime world must operate only on

\[
n
\]

and its descriptor

\[
W=(B,C,\Delta).
\]

For a candidate input \(n\), compute the quadratic Frobenius defect

\[
\delta_W(n)=(d_0,d_1)
\]

in

\[
A_n=(\mathbf Z/n\mathbf Z)[x]/(x^2-Bx-C).
\]

A runtime factor is exposed when

\[
1<\gcd(n,d_j)<n
\]

for either coordinate \(j\).

This criterion requires no knowledge of the hidden prime factors.

## 2. Candidate world family

Use canonical quadratic worlds from fundamental discriminants

\[
|D|\le D_{\max},
\]

excluding the torsion-silent controls from the expensive schedule.

Exceptional factors found by

\[
\gcd(n,2C\Delta)
\]

are counted as cheap precheck exposures and recorded separately.

## 3. Offline greedy compiler

Let \(S\) be the declared training population of composites.

For each candidate world \(W\), define

\[
E_W\subseteq S
\]

as the inputs for which runtime execution exposes a proper factor.

Starting from uncovered set

\[
U_0=S,
\]

choose

\[
\boxed{
W_t
=
\arg\max_W
|E_W\cap U_{t-1}|.
}
\]

Then

\[
U_t
=
U_{t-1}\setminus E_{W_t}.
\]

This is the standard greedy maximum-coverage compiler under equal world cost.

A cost-weighted variant would maximize

\[
\frac{|E_W\cap U|}{\operatorname{cost}(W)}.
\]

## 4. Controls

Compare:

1. **greedy complementarity schedule**;
2. **individual ranking** by \(|E_W|\);
3. **original hand schedule**, beginning with
   \[
   D=-7,\ 5,\ -19,\ -11,\ 13;
   \]
4. optional random-order controls.

Report:

- cumulative factor coverage after each world;
- marginal new hits;
- average revelation index;
- median revelation index;
- uncovered count after \(k\) worlds;
- schedule overlap.

## 5. Why this is hardware-safe

The local projective/scalar theory is used only to understand and potentially
pre-screen worlds offline.

The runtime factor observer remains the declared quadratic defect + gcd engine.

Therefore any schedule advantage measured here is implementable without
knowing the factors \(p,q\).

## 6. Publication relevance

Greedy maximum coverage itself is classical.

The potentially publishable result would be a reproducible, nontrivial
reduction in runtime world count / cycles produced by the H21 arithmetic-world
family and observer, especially if accompanied by FPGA measurements.

No novelty claim is made for the greedy algorithm itself.
