# H20-EXT-LAB-02 · Wheel-conditioned continuation quotient

Status: **PROTOCOL FROZEN BEFORE EXECUTION**

## 1. Purpose

LAB-01 found that the exact continuation quotient of the finite prime indicator is smaller than density-matched random/shuffled baselines over much of the tested range.

That observation is not yet a prime-specific structural law because the characteristic function of the primes contains obvious low-modulus structure:

- all primes except 2 are odd;
- all primes except 2,3 avoid 0 mod 2 or 3;
- more generally primes above q avoid every non-coprime residue modulo a primorial wheel.

LAB-02 asks the falsification question:

[
\boxed{
\text{Does the continuation-quotient compression gap survive after}
\atop
\text{small-prime wheel structure is removed explicitly?}
}
]

No conjecture is assumed.

## 2. Frozen wheel family

Use the four wheels

[
M\in\{2,6,30,210\}
=
\{2, 2\cdot3, 2\cdot3\cdot5, 2\cdot3\cdot5\cdot7\}.
]

For each wheel define its reduced residue system

[
R_M=\{r:0\le r<M,\ \gcd(r,M)=1\}.
]

No larger wheel is used in the first run because at the declared widths it would shorten each residue-class sequence enough to make continuation-quotient comparisons much less informative.

## 3. Wheel-conditioned prime sequences

For fixed width (W), wheel (M), and admissible residue (r\in R_M), define the exact finite sequence

[
F_{W,M,r}(k)
=
\mathbf 1[r+Mk\text{ is prime}],
]

for all integers (k\ge0) such that

[
0\le r+Mk<2^W.
]

Thus every sequence lies entirely inside one admissible residue class.

The obvious wheel predicate

[
\gcd(n,M)=1
]

is therefore no longer something the Boolean quotient has to discover.

## 4. Exact continuation quotient on a non-power-of-two domain

Let

[
L_{W,M,r}
=
\#\{k:r+Mk<2^W\}.
]

Encode (k) using

[
D=\lceil\log_2 L_{W,M,r}\rceil
]

bits.

For codes (k\ge L_{W,M,r}), use a third terminal symbol

[
\bot
]

rather than silently assigning 0 or 1.

The quotient therefore has terminals

[
\{0,1,\bot\}.
]

This makes padding explicit and identical for every baseline having the same residue-class length.

For each sequence compute the exact residual-function quotient under:

- MSB-first order of the (k)-bits;
- LSB-first order of the (k)-bits.

The quotient is canonical relative to the declared variable order and terminal convention.

## 5. Primary observables

For each ((W,M,r,\sigma)), record:

- sequence length;
- number of prime ones;
- nonterminal quotient-node count;
- peak residual-class count;
- peak depth;
- exact quotient hash.

For each ((W,M,\sigma)), aggregate across all (r\in R_M):

- sum of node counts;
- mean and median node counts;
- normalized node count per sequence element;
- minimum and maximum class ratios;
- distribution of prime-vs-baseline node ratios.

The primary falsification statistic is

[
\rho_{W,M,\sigma}
=
\frac{
\sum_{r\in R_M}N_{\rm prime}(W,M,r,\sigma)
}{
\mathbb E[
\sum_{r\in R_M}N_{\rm fixed-count-random}(W,M,r,\sigma)
]
}.
]

## 6. Baselines

### B1 · fixed-count random within each residue class

For every ((W,M,r)), generate random binary sequences of exactly the same length and with exactly the same number of ones as the prime sequence.

This controls simultaneously for:

- sequence length;
- prime density;
- residue-class occupancy.

Fixed seeds:

[
1729,quad271828,quad314159,quad1618033,quad5772157.
]

### B2 · within-class shuffled prime labels

Shuffle the prime labels inside each residue class independently, preserving the exact number of ones in that class.

This is a second deterministic fixed-count baseline with separate seeds.

### B3 · arithmetic controls

On the same residue-class domain also compute:

- squarefree indicator;
- semiprime indicator.

These are not density-matched baselines; they are arithmetic comparison families.

## 7. Discovery / validation split

This LAB-02 split is frozen before execution:

### Discovery

[
W=8,9,10,11,12.
]

### Validation

[
W=13,14,15.
]

### Extrapolation gate

[
W=16.
]

A law formulated from discovery data may be tested unchanged on validation widths.

If it is altered after viewing (W=13,14,15), the altered law does not inherit that validation.

## 8. Predeclared falsification criteria

The LAB-01 compression observation is considered **explained by small-modulus structure** if either of the following occurs:

1. for (M=30) and (M=210), the prime/random ratio (ho) approaches 1 within baseline variation across validation widths; or
2. the apparent prime advantage is unstable between MSB-first and LSB-first orders; or
3. no coherent effect survives simultaneously across multiple residue classes.

A stronger candidate survives LAB-02 only if:

1. (ho<1) on discovery widths for (M=30) or (210);
2. the inequality persists without retuning on all validation widths;
3. it survives both variable orders;
4. it is not confined to a tiny exceptional subset of residue classes;
5. it remains materially separated from fixed-count baseline variation.

No asymptotic form is fitted in LAB-02.

## 9. Interpretation boundary

A surviving compression gap would establish only:

> after conditioning on divisibility by the primes (2,3,5,7), the exact finite prime-residue sequences remain more continuation-compressible than the declared fixed-count random baselines on the tested finite widths.

It would not by itself establish novelty, an asymptotic theorem, a circuit lower bound, or a connection to RH.

A vanishing gap is a successful negative result.

## 10. Required artifacts

The run must emit:

- `wheel_conditioned_quotient.csv`;
- `wheel_conditioned_summary.json`;
- `H20_EXT_LAB02_REPORT.md`.

No FPGA synthesis is used.

No exact circuit minimization is used.

No post-hoc wheel choice is allowed in the first run.
