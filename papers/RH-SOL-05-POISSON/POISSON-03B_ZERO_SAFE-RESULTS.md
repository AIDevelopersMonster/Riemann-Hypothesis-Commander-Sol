# RH-SOL-05 · POISSON-03B ZERO-SAFE — results

Status: exploratory structural diagnostic complete.
Branch: `agent/rh-sol-05-poisson`.

## Verdict lock

POISSON-03 remains exactly as preregistered:

**statistical PASS / phase-stability FAIL**.

POISSON-03B ZERO-SAFE does not relax or replace any frozen POISSON-03 threshold. It diagnoses why global phase stability failed and how phase-only temporal localization depends on spatial Fourier amplitude.

## Zero-safe correction

Exact-zero Fourier coefficients are now treated correctly: phase is undefined at `G=0`, so exact-zero rows are dropped from phase normalization and counted explicitly rather than producing NaNs.

### Exact-zero phase counts

Calibration, bottom 1% stratum:

- requested: `102` loops per mode;
- valid phase rows: `0`;
- invalid/undefined phase rows: `102`.

Holdout, bottom 1% stratum:

- requested: `131` loops per mode;
- valid phase rows: `0`;
- invalid/undefined phase rows: `131`.

Thus the entire bottom-1% amplitude stratum selected by the previous near-zero rule consists of loops for which all four frozen mode phases are undefined under the discrete q16/q32 representation.

## Common singular mask

The near-zero excluded masks are identical for all four frozen modes.

### Calibration

- four-way intersection count: `102`;
- four-way union count: `102`;
- intersection/union: `1.0`;
- every pairwise Jaccard index: `1.0`.

### Holdout

- four-way intersection count: `131`;
- four-way union count: `131`;
- intersection/union: `1.0`;
- every pairwise Jaccard index: `1.0`.

This identifies a common low-spatial-energy class rather than independent per-mode numerical accidents.

## Geometry of the singular class

Using q32 spatial Fourier energy:

### Calibration

Stable-shell energy `E12`:

- excluded mean: `3.334035178600191e-05`;
- included mean: `0.36628896826202906`;
- mean ratio excluded/included: `9.102199267478758e-05`.

Total nonzero energy / translation variance:

- excluded mean: `0.0012211893119064032`;
- included mean: `0.608450236333039`;
- mean ratio excluded/included: `0.002007048792134872`.

Exact zero fraction inside excluded class:

- `E12=0`: `0.4215686274509804`;
- `Enonzero=0`: `0.4215686274509804`.

### Holdout

Stable-shell energy `E12`:

- excluded mean: `1.8200812544657838e-05`;
- included mean: `0.37815116835279877`;
- mean ratio excluded/included: `4.813104934711523e-05`.

Total nonzero energy / translation variance:

- excluded mean: `0.000914602789260049`;
- included mean: `0.62818297079746`;
- mean ratio excluded/included: `0.0014559496703627406`.

Exact zero fraction inside excluded class:

- `E12=0`: `0.4580152671755725`;
- `Enonzero=0`: `0.4580152671755725`.

Hence the phase-instability class is genuinely close to a flat translation map.

## Amplitude-stratified q16/q32 phase stability

Phase stability improves monotonically with spatial Fourier amplitude.

For the top 50% amplitude stratum:

### Calibration

- `(1,0)`: RMS `0.035110726437770155`, rho `0.9993843489341911`;
- `(0,1)`: RMS `0.03243035010987341`, rho `0.9994745290550004`;
- `(1,1)`: RMS `0.060384971064792646`, rho `0.9981799406106023`;
- `(1,-1)`: RMS `0.06000746880755507`, rho `0.9982024450335332`.

### Holdout

- `(1,0)`: RMS `0.03707623565140844`, rho `0.9993143017918853`;
- `(0,1)`: RMS `0.03384394626516488`, rho `0.9994276860952718`;
- `(1,1)`: RMS `0.06171746241814347`, rho `0.9981019483037675`;
- `(1,-1)`: RMS `0.06006823917071941`, rho `0.998200144059887`.

By contrast, in the 1%-5% amplitude stratum the RMS phase discrepancies rise to roughly `0.49`-`0.80` rad on calibration and `0.52`-`0.73` rad on holdout.

This is consistent with the expected ill-conditioning of `arg G` near `G=0`.

## Zero-safe temporal amplitude strata

The unexpected result is that exact-`log(m)` temporal localization is **not weakest near the singular layer**. Among rows where all four q32 phases are defined, the bottom-amplitude decile gives the largest exploratory phase-only target score.

### Calibration

Bottom 10%:

- requested: `1000`;
- valid: `957`;
- undefined phase dropped: `43`;
- raw `m=2..13`: `0.03247080155945956`;
- area-residualized `m=2..13`: `0.029951778348488677`;
- area-residualized `m=2..11`: `0.030628565101364736`.

Middle 80%:

- valid: `8000`;
- area-residualized `m=2..13`: `0.010862938440845038`;
- area-residualized `m=2..11`: `0.012325651520344436`.

Top 10%:

- valid: `1000`;
- area-residualized `m=2..13`: `0.020461117108096793`;
- area-residualized `m=2..11`: `0.020921485883335346`.

### Holdout

Bottom 10%:

- requested: `1000`;
- valid: `940`;
- undefined phase dropped: `60`;
- raw `m=2..13`: `0.030975345567460132`;
- area-residualized `m=2..13`: `0.029123716323194722`;
- area-residualized `m=2..11`: `0.030188578620976875`.

Middle 80%:

- valid: `8000`;
- area-residualized `m=2..13`: `0.01050660158974002`;
- area-residualized `m=2..11`: `0.011982167048039755`.

Top 10%:

- valid: `1000`;
- area-residualized `m=2..13`: `0.020009052608702817`;
- area-residualized `m=2..11`: `0.019821195008216597`.

## Revised structural interpretation

The earlier working hypothesis that arithmetic phase information lives only in the regular high-amplitude layer is rejected by this diagnostic.

Instead the finite-range data support a more interesting two-property picture:

1. **resolution stability improves with amplitude** — high-amplitude spatial modes have much better q16/q32 phase agreement;
2. **exact-target temporal localization is amplified near the low-amplitude boundary** — after dropping rows where phase is mathematically undefined, the bottom amplitude decile has the strongest exploratory target score and reproduces closely on the second 10k-loop range.

Therefore spatial phase resolution and arithmetic temporal localization vary in opposite directions near Fourier zeros.

A useful descriptive phrase is:

> **phase-singularity amplification**: temporal Dirichlet-frequency localization becomes stronger as the resolved spatial Fourier amplitude approaches the phase-singular boundary, even while cross-resolution pointwise phase stability deteriorates.

This phrase is exploratory, not yet a theorem or confirmatory result.

## What remains unconfirmed

The amplitude strata were inspected on both available 10k ranges during POISSON-03B. They therefore cannot be promoted to a new independent confirmatory claim using the same data.

A fresh OOS range is required.

## Next experiment

`POISSON-04_PHASE_SINGULARITY_OOS` will use fresh loops `20001..40000` and will freeze before those translation tensors are analyzed:

- the same four spatial modes;
- the same q16/q32 midpoint correction;
- the same target-blind `min amplitude across four modes` stratification;
- bottom10 / middle80 / top10 groups;
- exact-zero rows dropped only where phase is mathematically undefined;
- primary q32 area-residualized `m=2..13` score;
- independent target-jitter null within each predeclared stratum;
- direct test of the ordered amplification pattern `bottom10 > top10 > middle80`;
- q16/q32 stability reported separately and not conflated with temporal localization.

No POISSON-03 threshold will be changed.
