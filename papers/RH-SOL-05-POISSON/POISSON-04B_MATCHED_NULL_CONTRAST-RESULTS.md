# RH-SOL-05 · POISSON-04B_MATCHED_NULL_CONTRAST — results

Status: **post-hoc exploratory diagnostic complete**.

This analysis does not alter the frozen POISSON-04 verdict. POISSON-04 remains **full confirmation FAIL**.

## Purpose

POISSON-04 showed that raw scores are not directly comparable across amplitude strata because their local-frequency jitter baselines differ strongly. POISSON-04B therefore applies the **same jittered frequency dictionary** to `bottom10`, `middle80`, and `top10` on every Monte-Carlo draw and compares matched score differences.

Fresh tensor range inherited from POISSON-04: loops `20001..40000`.

Monte Carlo: `B=2000`, seed `20261004`.

## Exact scores and matched-null baselines

### bottom10

- exact score: `0.02924896590337709`;
- matched-null mean: `0.021629151479253768`;
- matched-null median: `0.02155537295135019`;
- exact-minus-null-mean excess: `0.007619814424123322`.

### middle80

- exact score: `0.009956822800432821`;
- matched-null mean: `0.0025602237495276864`;
- matched-null median: `0.0023495126630922996`;
- exact-minus-null-mean excess: `0.007396599050905135`.

### top10

- exact score: `0.020338646838593502`;
- matched-null mean: `0.020313953988079204`;
- matched-null median: `0.020312319638628278`;
- exact-minus-null-mean excess: `0.000024692850514298`.

Thus bottom10 and middle80 have nearly equal absolute exact-target excess over their matched local-frequency baselines, whereas top10 has essentially none.

## Matched contrasts

Define

- `Delta_BT = Q_bottom - Q_top`;
- `Delta_BM = Q_bottom - Q_middle`;
- `Delta_MT = Q_middle - Q_top`.

### Bottom versus top: Delta_BT

Observed exact contrast:

`0.008910319064783588`.

Matched-null distribution:

- mean: `0.0013151974911745615`;
- median: `0.0012676428260202845`;
- sd: `0.0008835154051994621`;
- q95: `0.002856579567980662`;
- q99: `0.003477314132542595`;
- maximum: `0.006024130898846149`;
- empirical `p_ge = 0.0004997501249375312 = 1/2001`;
- standardized displacement: `8.596478939599649` null SD.

The exact `log(m)` dictionary produces a bottom-over-top advantage larger than every one of the 2000 matched local-jitter realizations.

This is strong exploratory evidence that exact-frequency specificity differs between the low- and high-amplitude phase layers.

### Bottom versus middle: Delta_BM

Observed exact contrast:

`0.01929214310294427`.

Matched-null distribution:

- mean: `0.019068927729726078`;
- median: `0.019066800167191457`;
- sd: `0.0006020009177108831`;
- q95: `0.020080033353076492`;
- q99: `0.020464863178332387`;
- empirical `p_ge = 0.35582208895552225`;
- standardized displacement: `0.37078909126413107` null SD.

Therefore the large raw bottom-over-middle score difference is **not unusual** once both strata are subjected to the same frequency perturbation.

This directly rejects the stronger interpretation that the exact dictionary is specifically enriched in bottom10 relative to middle80.

### Middle versus top: Delta_MT

Observed exact contrast:

`-0.01038182403816068`.

Matched-null distribution:

- mean: `-0.017753730238551518`;
- median: `-0.017837072720263546`;
- sd: `0.0006720121284874231`;
- q99: `-0.015593884945601563`;
- maximum: `-0.013077602733390217`;
- empirical `p_ge = 0.0004997501249375312`;
- standardized displacement: `10.969900523943897` null SD.

The sign remains negative: top10 still has the larger raw score. But under the exact dictionary the top-over-middle advantage is dramatically **smaller** than under matched jitter.

Equivalently,

`Delta_TM = Q_top - Q_middle`

falls from a matched-null mean of approximately `0.017754` to an exact value of approximately `0.010382`.

Thus exact `log(m)` frequencies selectively lift middle80 toward top10, while top10 itself receives almost no exact-target excess.

## Matched-null score correlations

Order: `bottom10, middle80, top10`.

Correlation matrix:

```text
[[1.000000, 0.633775, 0.037128],
 [0.633775, 1.000000, 0.013782],
 [0.037128, 0.013782, 1.000000]]
```

The common jitter response of bottom10 and middle80 is moderately correlated (`~0.634`), whereas top10 is nearly decorrelated from both (`~0.04` and `~0.014`).

This is a new structural clue: the low/intermediate amplitude layers appear to share a common local-frequency response family that is largely absent from the highest-amplitude layer.

## Revised structural picture

POISSON-04B does **not** support a monotone statement of the form

`lower amplitude => stronger exact-target specificity`.

Instead it supports a two-regime picture:

### Arithmetic-sensitive low/intermediate regime

`bottom10` and `middle80` both show an exact-frequency excess of approximately `0.0074-0.0076` above their matched-null means.

Their responses to common target jitter are also substantially correlated.

### Phase-stable high-amplitude regime

`top10` is the most q16/q32 phase-stable layer, but its exact score is essentially equal to its local-jitter baseline:

`exact - matched-null mean ~ 2.47e-05`.

Its jitter response is almost decorrelated from the low/intermediate layers.

Therefore the strongest defensible exploratory statement is:

> **The highest-amplitude, most cross-resolution phase-stable spatial Fourier layer is spectrally distinct from the low/intermediate layers: it carries almost no exact-Dirichlet-frequency excess under the tested local-jitter family, whereas both low and intermediate amplitude layers carry comparable exact-target excess.**

This replaces the cruder exploratory phrase `phase-singularity amplification` as the preferred structural description.

## What was falsified

The stronger proposed monotone amplification law

`bottom exact specificity > middle exact specificity > top exact specificity`

is not supported.

In particular, the bottom-versus-middle matched contrast is ordinary (`p_ge ~ 0.356`).

The data instead point to a **regime boundary** separating top10 from the rest, not a continuous monotone amplitude law.

## What survives strongly

The matched bottom-versus-top contrast is extreme (`p=1/2001`, `z~8.60`) and the middle-versus-top contrast is also extreme relative to common jitter (`p=1/2001`, `z~10.97` in the upper-tail convention used here).

Thus the robust feature is not a singular enhancement at the lowest amplitudes. It is the **loss of exact-frequency specificity in the highest-amplitude layer**.

## Research consequence

The next experiment should no longer focus on `bottom10` versus all higher amplitudes. It should locate and test the apparent transition into the high-amplitude exact-specificity-poor regime.

A natural next diagnostic is an amplitude-decile profile with a matched common-jitter normalization, followed only later by a fresh-data preregistered threshold test if a stable transition boundary emerges.

Any amplitude-decile scan on loops `20001..40000` is necessarily exploratory because these data have already been inspected.

## Guardrails

1. POISSON-03 remains `statistical PASS / phase-stability FAIL`.
2. POISSON-04 remains frozen full-confirmation FAIL.
3. POISSON-04B is exploratory only.
4. No asymptotic theorem or RH claim follows.
