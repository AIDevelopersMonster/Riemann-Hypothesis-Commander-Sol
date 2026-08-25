# RH-SOL-04 · FIREWALL-03 — phase-randomized surrogate preregistration

Status: preregistered before phase-randomized surrogate inspection.
Branch: `agent/rh-sol-04-firewall`.

## Core question

FIREWALL-01/02 showed that the exact `log(m)` alignment depends on the correct geometry-to-zero-time assignment more strongly than can be explained by within-block circular shifts or whole-block reassignment.

FIREWALL-03 asks a stricter alternative:

> Can the observed exact-target score be reproduced by surrogates that preserve the full blockwise loop-index Fourier power spectrum of the area series while destroying its Fourier phases?

If yes, second-order temporal structure of the area sequence may already be sufficient. If no, phase information beyond the preserved power spectrum is required.

## Observable and block structure

- observable: winding filled area `A_n = Area(D_n)`;
- time coordinate for scoring: actual zero-pair midpoint `t_n = (gamma_n + gamma_{n+1})/2`;
- block size: 1000 loops;
- ranges tested independently:
  - loops `1..20000`;
  - loops `20001..40000`.

## Surrogate construction

For each 1000-loop area block independently:

1. subtract the block mean;
2. compute the real FFT in loop-index order;
3. preserve the magnitude of every Fourier coefficient exactly;
4. keep the DC component fixed at zero after centering;
5. for all non-DC/non-Nyquist positive-frequency bins, replace the phase by an independent uniform random phase in `[0,2*pi)`;
6. if the Nyquist bin exists, preserve its real value up to an independent random sign;
7. inverse real FFT;
8. restore the original block mean.

Thus each surrogate block preserves exactly, up to floating-point roundoff:

- the block mean;
- the block variance;
- the complete loop-index Fourier magnitude spectrum;
- therefore the circular autocovariance function / second-order periodic structure implied by that spectrum.

It destroys the original Fourier phase relations and the original pointwise sequence.

## Primary FIREWALL statistic

Use exactly the frozen target-only statistic introduced before FIREWALL-01/02:

For each block and each target `omega=log(m)`:

- detrend area linearly against actual time;
- fit `a cos(omega t) + b sin(omega t)`;
- compute `R2(omega) = 1 - SSE/SST`;
- transform by `-log(1-R2+1e-15)`.

The range-level score is the mean across targets and blocks.

Primary dictionary:

- `m=2..13`.

Predeclared sensitivity:

- `m=2..11`.

No common-shift scan, target deletion, frequency optimization or refitting enters the primary score.

## Monte Carlo design

- surrogate realizations per range: `B=5000`;
- calibration-range seed: `20260827`;
- holdout-range seed: `20260828`.

For each range and dictionary report:

- observed score;
- surrogate median;
- surrogate q95;
- surrogate q99;
- surrogate maximum;
- empirical upper-tail p-value `(1 + #surrogates >= observed)/(B+1)`.

## Primary success criterion

FIREWALL-03 passes on a range if

- observed score > surrogate q99;
- empirical p <= 0.01.

The result is strongest if no surrogate reaches observed, but that is not required beyond the preregistered q99/p criterion.

## Interpretation

### If FIREWALL-03 fails strongly

Then preserving the full blockwise loop-index power spectrum is insufficient to reproduce the exact `log(m)` alignment. The relevant information must depend on phase structure or on higher-order/nonlinear temporal organization coupled to the true zero times.

### If FIREWALL-03 reproduces observed

Then the present interpretation must be weakened: second-order blockwise area-spectrum structure may already be sufficient to account for much or all of the exact-target score.

### Intermediate result

If calibration rejects but holdout does not, or vice versa, report the asymmetry without retuning the surrogate family.

## Guardrails

1. Phase randomization preserves second-order loop-index structure, not polygon-level geometry.
2. It does not preserve the empirical amplitude distribution exactly; a later IAAFT-type surrogate may test simultaneous spectrum+distribution preservation if needed.
3. The test does not prove arithmetic causation even if surrogates fail.
4. No post-view tuning may be reclassified as confirmatory.
5. No Riemann-Hypothesis claim follows from any outcome.
