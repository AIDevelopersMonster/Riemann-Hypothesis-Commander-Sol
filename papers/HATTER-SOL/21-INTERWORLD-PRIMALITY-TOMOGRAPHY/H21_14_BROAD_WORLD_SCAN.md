# HATTER-SOL-21 · BROAD FUNDAMENTAL-DISCRIMINANT WORLD SCAN

Status: **BROAD COMPILER VALIDATION LAYER**

## 1. Purpose

H21-LAB-09 found a perfect six-world rank match between the cheap pooled
zero-mask diversity

\[
G_W=1-\sum_z\pi_W(z)^2
\]

and the exact nonexceptional semiprime factor-exposure rate

\[
Q_W.
\]

Six hand-selected worlds are not enough to trust this as a compiler rule.

H21-LAB-10 scans a canonical family of quadratic worlds generated from
fundamental discriminants.

## 2. Canonical quadratic world

For a fundamental discriminant \(D\), use

\[
x^2-Bx-C
\]

with

\[
(B,C)=
\begin{cases}
\left(1,\frac{D-1}{4}\right),&D\equiv1\pmod4,\\[2mm]
\left(0,\frac D4\right),&D\equiv0\pmod4.
\end{cases}
\]

Then

\[
B^2+4C=D.
\]

This gives one canonical presentation per scanned discriminant.

The special torsion controls

\[
D=-3,\qquad D=-4
\]

are retained and tagged separately.

## 3. Why fundamental discriminants

The scan is intended to test a world-quality heuristic, not to multiply
equivalent presentations arbitrarily.

Restricting to fundamental discriminants provides a simple canonical family of
quadratic fields/orders for the first broad test.

Observer dependence under alternative presentations remains a separate H21
question.

## 4. Two populations

### World-specific eligible population

For each world \(W\), use every distinct odd semiprime

\[
n=pq<N
\]

satisfying

\[
\gcd(pq,2C\Delta)=1.
\]

This measures operational quality of that world on its natural admissible
domain.

### Common-core population

For a discriminant bound

\[
|D|\le D_{\max},
\]

also restrict to

\[
\boxed{
p>D_{\max},\qquad q>D_{\max}.
}
\]

Then no scanned prime factor divides any nonzero \(C\) or \(D\), so every
canonical world sees the same semiprime population.

This is the principal ranking control.

## 5. Metrics

For each world and each population compute:

\[
Q_W
=
\Pr[
L_W(p\leftarrow q)\ne L_W(q\leftarrow p)
],
\]

\[
G_W
=
1-\sum_z\pi_W(z)^2,
\]

\[
H_W
=
-\sum_z\pi_W(z)\log_2\pi_W(z),
\]

and

\[
K_W=Q_W-G_W.
\]

Also report:

- partial-mask mass;
- empty/full mask masses;
- \(|K_W|/G_W\);
- rank by \(Q\), \(G\), and \(H\);
- rank displacement;
- pairwise ranking inversions;
- top-\(k\) overlap.

## 6. Broad compiler questions

The scan asks:

1. Does \(G_W\) remain strongly correlated with \(Q_W\) after expanding from
   six worlds to dozens or hundreds?
2. Does the correlation survive on the common-core population?
3. Are there explicit rank inversions
   \[
   G_{W_1}>G_{W_2}
   \quad\text{but}\quad
   Q_{W_1}<Q_{W_2}?
   \]
4. Which worlds are coupling-dominated:
   \[
   |K_W|/G_W
   \]
   large?
5. Are the torsion worlds automatically pushed to the bottom?

## 7. Decision rule

Three possible outcomes are distinguished.

### Strong heuristic survives

High rank correlation, small inversion rate, and stable top-\(k\) overlap on
the common core.

Then

\[
G_W
\]

is retained as a cheap world pre-screen.

### Heuristic only local

Good correlation on world-specific populations but poor common-core ranking.

Then eligibility structure, not intrinsic mask diversity, is driving part of
the effect.

### Heuristic breaks

Many rank inversions or large coupling corrections.

Then pairwise coupling is essential and no one-direction quality compiler is
adequate.

## 8. Claim boundary

Even a broad finite scan is not an asymptotic theorem.

Its role is to decide whether the diversity heuristic deserves a theorem search
or should be discarded before FPGA scheduling work.
