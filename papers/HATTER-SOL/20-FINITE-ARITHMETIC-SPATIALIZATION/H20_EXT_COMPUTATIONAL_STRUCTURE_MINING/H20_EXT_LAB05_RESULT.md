# H20-EXT-LAB-05 · Fresh hold-out result

Status: **VALIDATION PASS / C1 EMPIRICAL CANDIDATE OPEN**

Run: GitHub Actions 35577464955.

## Frozen candidate

Before computing W=17,18,19, LAB-05 froze exactly one statement for testing:

[
L_W(4)_{m prime}
<
L_W(4)_{m stratified shuffle},
]

where

[
L_W(4)=sum_{k=1}^{4}e_{W,k}
]

and the baseline independently shuffles prime labels inside every joint stratum

[
(nmod210,lfloorlog_2 nfloor).
]

The five seeds remained frozen.

## Fresh validation

The predeclared validation widths were W=17,18.

| W | mean prime-minus-baseline low-4 mass | minimum | maximum | all five negative |
|---:|---:|---:|---:|---|
| 17 | -0.001050845161 | -0.001226598397 | -0.000873381272 | YES |
| 18 | -0.000790006574 | -0.000859932043 | -0.000680486672 | YES |

Thus on both fresh widths the prime low-degree mass through degree 4 is below **every** fixed-seed baseline sample.

The frozen validation criterion passes.

## Extrapolation

The predeclared extrapolation width W=19 gives

[
Delta L_{19}(4)_{m mean}
=
-0.000387021247
]

with five-seed range

[
[-0.000450737076,-0.000341650099].
]

No sign reversal occurs.

## Exact finite statement

For the exact prime indicator on the Boolean cubes of widths 17 and 18, and for each of the five declared joint wheel-210 + dyadic-shell preserving shuffles, the cumulative normalized Walsh energy on degrees 1 through 4 is strictly smaller for the prime indicator than for the shuffled baseline.

The same inequality holds on the predeclared W=19 extrapolation samples.

This is an exact statement about the finite generated functions and the frozen seeds.

## C1 empirical candidate

The branch now opens one empirical candidate:

[
oxed{
	ext{C1: primes exhibit a low-degree Walsh-energy deficit}
atop
	ext{relative to wheel-210 + dyadic-density preserving shuffles.}
}
]

Current evidence:

- emerged after LAB-04;
- hypothesis then frozen;
- independently validated at W=17,18;
- extrapolated successfully to W=19;
- survives control of exact prime counts by mod-210 residue and dyadic magnitude shell.

## Why this is not yet a publication result

The baseline is still sample-based.

A stronger object would compare the prime low-4 energy against the **exact expectation** (and preferably exact variance or concentration bounds) under uniform within-stratum permutations.

That removes dependence on five chosen seeds and creates a mathematical quantity suitable for theorem formulation.

## Literature status

The broad Fourier-Walsh interaction between primes and binary digits is known territory.

Relevant neighboring work includes:

- Jean Bourgain, *Prescribing the binary digits of primes*, arXiv:1105.3895;
- Jean Bourgain, *Monotone Boolean functions capture their primes*, arXiv:1211.6760 / Journal d'Analyse Mathématique;
- Bourgain's estimates for low-degree Fourier-Walsh coefficients of the von Mangoldt function used in that line of work;
- related Fourier-Walsh work on the Möbius function.

Therefore C1 is classified as:

[
oxed{	ext{apparently distinct finite empirical statistic; novelty unresolved}.}
]

No claim of new theorem is made.

## Non-claim

C1 does not imply:

- an asymptotic Walsh law for primes;
- contradiction or improvement of Bourgain's estimates;
- circuit lower bounds;
- a new prime-number theorem;
- any RH consequence.

## Next gate

Do not enlarge the width table merely for confidence.

The next serious target is:

[
oxed{
	ext{replace sampled stratified shuffles by an exact baseline expectation}
}
]

for degree-1--4 Walsh energy.

If the exact expected-baseline deficit persists and can be formulated cleanly, only then should C1 be considered for theorem-level development.
