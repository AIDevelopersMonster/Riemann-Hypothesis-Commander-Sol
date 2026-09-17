# RH-SOL-05 · POISSON-03 — phase-only unit-phasor test preregistration

Status: preregistered before inspection of phase-only results.
Branch: `agent/rh-sol-05-poisson`.

## Motivation

POISSON-02 established that the four resolved complex spatial coefficients

`(1,0), (0,1), (1,1), (1,-1)`

are highly stable across q16/q32 and retain reproducible phase-sensitive exact-`log(m)` temporal structure after removal of scalar area.

However the complex coefficient

`G = |G| exp(i phi)`

still mixes magnitude and phase. POISSON-03 removes magnitude completely and tests the unit phasor

`U = G / |G|`.

Core question:

> Does Fourier orientation alone, with amplitude removed, retain resolved and statistically localized exact-`log(m)` temporal structure?

## Frozen modes

Use exactly the four POISSON-02 representatives:

- `(1,0)`;
- `(0,1)`;
- `(1,1)`;
- `(1,-1)`.

No temporal selection or reweighting is permitted.

## Midpoint correction

Use the same midpoint-corrected coefficients as POISSON-02:

`G_q(a,b) = F_q[a,b] * exp(-pi i (a+b)/q)`.

## Near-zero amplitude guardrail

Unit phase is numerically unstable only when `|G|` is extremely small.

For each mode, range and q separately define

`tau_q = 1e-6 * median_n |G_q|`.

A sample is reliable for q16/q32 phase comparison only if

`|G16| > tau16` and `|G32| > tau32`.

The common reliable mask is used for both resolutions so that q16/q32 temporal scores use identical loop indices.

Report the excluded fraction for every mode and range.

Numerical reliability gate:

`excluded_fraction <= 0.001`

for every frozen mode on both calibration and holdout.

If this gate fails, phase-only scores are reported but no strong phase-only interpretation is promoted.

The threshold rule is frozen and depends only on coefficient amplitude, never on temporal target scores.

## Unit phasors

On reliable samples define

`U_q = G_q / |G_q|`.

Verify unit-modulus error is below `1e-12` at floating precision.

## q16/q32 phase-only stability

For each frozen representative on the common reliable mask define phase difference

`Delta phi = arg(U16 * conjugate(U32))`.

Report:

- RMS phase difference;
- median absolute phase difference;
- circular coherence

`rho_phase = |mean(U16 * conjugate(U32))|`.

A representative is phase-stable if on both calibration and holdout:

- `rms_phase_error <= 0.10` radians;
- `rho_phase >= 0.995`;
- the numerical reliability gate passes.

No channel can be replaced after temporal inspection.

## Frozen channel groups

As in POISSON-02:

1. each representative individually;
2. shell `r^2=1`: `(1,0),(0,1)`;
3. shell `r^2=2`: `(1,1),(1,-1)`;
4. combined stable layer: all four representatives.

For a group, use the intersection of the frozen reliable masks of its channels.

## Phase-only temporal score

Use the same phase-invariant complex Frobenius target statistic as POISSON-02, now applied to `U` rather than `G`:

1. within each original 1000-loop block, retain the group's reliable rows;
2. detrend each unit-phasor channel against `[1,t]` by complex OLS;
3. project onto `[cos(omega t), sin(omega t)]` at exact `omega=log(m)`;
4. form explained Frobenius energy divided by total residual Frobenius energy;
5. transform `R2 -> -log(1-R2+1e-15)`;
6. average over targets and blocks.

Primary dictionary: `m=2..13`.
Sensitivity: `m=2..11`.

## Area-residualized phase-only score

Within each block and on the same reliable rows remove complex OLS projection of `U` onto `[1,A]`, where `A` is winding-filled area, then apply the unchanged temporal score.

Because `U` contains no original Fourier magnitude, this residualized observable still depends only on spatial phase plus the explicit scalar-area nuisance removal.

## Confirmatory target-jitter null

The primary confirmatory statistic is the q32 area-residualized phase-only score of the combined four-channel group with `m=2..13`.

For each range generate `B=2000` jittered target dictionaries. For each target independently,

`omega_m^null = log(m) + eta_m`,

with

`eta_m ~ Uniform[-0.20, 0.20]`.

The exact dictionary is not included specially in the null; probability of exact equality is zero numerically.

Use fixed seeds:

- calibration: `20260906`;
- holdout: `20260907`.

For every jittered dictionary compute the identical block statistic on the already frozen phase-only observable.

Report null median, q95, q99, maximum and

`p_ge = (1 + count(null >= observed)) / (B + 1)`.

No frequency scan, common shift optimization or target deletion is permitted.

## Frozen ranges

- calibration: loops `1..10000`;
- holdout: loops `10001..20000`.

## Primary success pattern

A genuine phase-only arithmetic layer is supported if all of the following hold:

1. the numerical reliability gate passes for all four frozen channels on both ranges;
2. the four channels remain phase-stable across q16/q32 by the frozen phase criteria;
3. the combined q32 area-residualized unit-phasor exact score exceeds the q99 target-jitter null and has `p_ge <= 0.01` on calibration;
4. the same criterion independently holds on holdout;
5. q16 and q32 exact phase-only scores agree qualitatively, with no resolution-specific reversal;
6. the `m=2..11` sensitivity dictionary is directionally consistent.

## Negative / energy-dominated outcome

If unit-phasor target localization fails while POISSON-01B power and POISSON-02 complex results remain strong, conclude that the currently resolved arithmetic information is predominantly magnitude / energy carried; complex phase is geometrically stable but not independently demonstrated as an arithmetic carrier.

## Guardrails

1. Unit phasor removes Fourier amplitude exactly on reliable samples.
2. The near-zero mask is a numerical reliability device, not a temporal selection rule.
3. The target-jitter null tests exact-frequency localization, not every conceivable null model.
4. Finite-range phase-only localization is not an asymptotic theorem.
5. No Riemann-Hypothesis claim follows from any outcome.
