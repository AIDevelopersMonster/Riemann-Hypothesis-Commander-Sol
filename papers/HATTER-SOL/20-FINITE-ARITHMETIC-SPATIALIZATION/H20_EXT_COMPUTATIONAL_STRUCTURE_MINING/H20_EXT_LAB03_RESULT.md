# H20-EXT-LAB-03 · Exact Walsh degree-spectrum result

Status: **INITIAL SPECTRAL CANDIDATE PASSED LAB-03 / LATER SUBJECT TO LAB-04**

Run: GitHub Actions 35577146288.

## Observation

Against wheel-210 preserving shuffles, the prime sign-function Walsh degree spectrum showed two consistent validation-range deviations.

For W=12,13,14 the prime cumulative degree-1--2 energy exceeded every one of the five fixed-seed wheel-210 baseline samples.

The mean prime-minus-baseline differences were:

[
+0.001287079,quad +0.000770283,quad +0.000850010.
]

The five-seed ranges were strictly positive:

- W=12: [0.000642776, 0.001943588];
- W=13: [0.000242233, 0.001190424];
- W=14: [0.000539899, 0.001076460].

The same sign persisted at W=15 and W=16.

At the same time cumulative degree-1--4 energy was lower than every wheel-210 sample throughout W=12..16.

## Exact finite statement

Exact integer FWHT energies verify the above inequalities for the declared five seeds and widths.

## Interpretation

LAB-03 therefore crossed its own finite validation gate and justified a stronger falsification experiment.

## Non-claim

This was not promoted to a new prime theorem or publication result.

The wheel-210 shuffle does not preserve the large-scale density gradient of the primes, so LAB-04 was required before any structural interpretation.
