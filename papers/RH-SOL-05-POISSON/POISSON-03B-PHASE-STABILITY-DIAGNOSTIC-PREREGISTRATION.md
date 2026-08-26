# RH-SOL-05 · POISSON-03B — phase-stability failure diagnostic preregistration

Status: preregistered after POISSON-03 verdict and before inspection of diagnostic results.
Branch: `agent/rh-sol-05-poisson`.

## Fixed prior verdict

POISSON-03 remains permanently classified as:

**statistical PASS / phase-stability FAIL**.

This diagnostic does not alter its frozen thresholds and cannot retroactively promote POISSON-03 to a resolved phase-only layer.

## Motivation

POISSON-03 found that all four frozen phase channels

`(1,0), (0,1), (1,1), (1,-1)`

failed the frozen q16/q32 phase-stability rule. At the same time, the near-zero exclusion fraction was exactly identical across all four channels within each range:

- calibration: `0.0102`;
- holdout: `0.0131`.

The primary question is therefore structural:

> Is the phase-stability failure concentrated in a common low-amplitude / low-translation-structure subset of loops, while the bulk phase field is substantially more stable?

## Data and frozen coefficients

Use the same calibration and holdout datasets as POISSON-03 and the same midpoint-corrected complex coefficients

`G_q(a,b) = F_q[a,b] * exp(-pi i(a+b)/q)`

for q16 and q32.

No temporal target information is used for any selection or threshold.

## A. Exact mask-overlap diagnostic

For each mode construct the exact POISSON-03 reliable mask using

`tau_q = 1e-6 * median |G_q|`

and common reliability condition

`|G16| > tau16 and |G32| > tau32`.

Report:

- excluded loop count for each mode;
- pairwise Jaccard similarity of excluded sets;
- size of four-way excluded intersection;
- size of four-way excluded union;
- fraction `intersection/union`;
- whether the four masks are exactly identical.

This is purely diagnostic.

## B. Relation to translation structure

For each loop compute q32:

- stable shell energy `E12 = sum over r^2 in {1,2} |F32|^2`;
- total nonzero energy `Enz`;
- translation variance `V`.

Compare POISSON-03 four-way excluded-union loops against included loops using:

- mean and median E12;
- mean and median Enz;
- mean and median V;
- ratios excluded/included for each quantity;
- fraction of excluded loops with exactly zero E12;
- fraction with exactly zero Enz.

No significance threshold is preregistered; this section identifies conditioning geometry.

## C. Target-blind amplitude strata

For each frozen representative define a scalar conditioning amplitude

`A_mode = sqrt(|G16| |G32|)`.

Using the full range independently, partition loops by frozen empirical amplitude quantiles:

- Q0: bottom 1%;
- Q1: 1%–5%;
- Q2: 5%–20%;
- Q3: 20%–50%;
- Q4: top 50%.

Quantile boundaries depend only on amplitude and are target-blind.

For each stratum and mode report:

- sample count;
- RMS phase difference;
- median absolute phase difference;
- circular coherence.

Primary structural pattern of interest:

phase discrepancy decreases monotonically or nearly monotonically with amplitude, with the largest errors concentrated in Q0/Q1.

This is descriptive, not a new success criterion for POISSON-03.

## D. Trimmed stability sensitivity

Without changing the original verdict, report phase stability after removing the lowest amplitude fractions

`0%, 0.5%, 1%, 2%, 5%`

according to `A_mode` for each frozen mode, independently on calibration and holdout.

For each trim report RMS phase error and rho_phase.

No trim level is promoted as a replacement threshold. The purpose is to map the stability transition.

## E. Temporal localization by amplitude stratum

As an exploratory structural diagnostic only, compute the q32 phase-only exact-target score for the combined four-channel observable on three target-blind groups defined by the minimum conditioning amplitude across the four channels:

- bottom 10%;
- middle 80%;
- top 10%.

Use the same 1000-loop block assignment inherited from the full sequence and the same exact target dictionaries `m=2..13` and `m=2..11`.

Report raw and area-residualized scores.

No jitter null is required here because POISSON-03 already supplied the confirmatory exact-target null; this section asks only where in amplitude space the observed phase-only localization resides.

## Interpretation rules

### Common-degenerate-tail interpretation

Supported if:

- excluded masks have very high overlap;
- excluded loops have strongly reduced E12/Enz/V;
- phase error is sharply concentrated in low-amplitude strata;
- modest target-blind trimming substantially improves q16/q32 phase stability.

Then the correct statement is that POISSON-03 phase instability is concentrated in a common poorly conditioned translation-geometry tail.

This still does not retroactively satisfy POISSON-03.

### Distributed-instability interpretation

Supported if masks differ substantially, translation energies are not reduced, or phase error remains broad across amplitude strata.

Then phase non-resolution is an intrinsic q16/q32 limitation of the present lattice resolutions rather than a small degenerate tail.

## Guardrails

1. POISSON-03 remains statistical PASS / phase-stability FAIL regardless of this result.
2. No threshold relaxation, channel replacement or temporal selection is permitted.
3. All stratification is defined from spatial coefficient amplitude only.
4. Exploratory stratum temporal scores are not confirmatory p-values.
5. No Riemann-Hypothesis claim follows.
