# RH-SOL-05 · POISSON-04_PHASE_SINGULARITY_OOS — results

Status: **full frozen confirmation FAIL; low-amplitude exact-target localization strongly replicated OOS**.
Branch: `agent/rh-sol-05-poisson`.
Fresh range: loops `20001..40000`.

## Frozen verdict

The preregistered phase-singularity-amplification package required all of the following on the fresh OOS range:

1. bottom10 exact score above its jitter q99 with `p<=0.01`;
2. top10 exact score above its jitter q99 with `p<=0.01`;
3. exact-score ordering `bottom10 > top10 > middle80`;
4. bottom/top and bottom/middle ratios above 1;
5. `m=2..11` sensitivity with bottom10 above middle80.

The observed result satisfies items 1, 3, 4 and 5 but **fails item 2**. Therefore the frozen primary claim is **not confirmed**.

No threshold is changed post hoc.

## Fresh OOS results

### bottom10

- requested rows: `2000`;
- valid defined-phase rows: `1884`;
- undefined phase dropped: `116`;
- q32 area-residualized `m=2..13`: `0.02924896590337709`;
- sensitivity `m=2..11`: `0.029846818093391365`.

Target-jitter null:

- median: `0.021537503576128`;
- q95: `0.023047265245448638`;
- q99: `0.023953429177698334`;
- max: `0.025645628642235234`;
- empirical `p_ge = 0.0004997501249375312 = 1/2001`.

The exact dictionary exceeds even the largest of the 2000 jitter surrogates.

Descriptive quantities:

- observed / q99 = approximately `1.2211`;
- observed / null median = approximately `1.3580`;
- observed - null median = approximately `0.00771146`.

### middle80

- requested/valid rows: `16000`;
- undefined phase dropped: `0`;
- q32 area-residualized `m=2..13`: `0.009956822800432821`;
- sensitivity `m=2..11`: `0.011286660923643119`.

Target-jitter null:

- median: `0.002341709666098999`;
- q99: `0.004663894674909145`;
- max: `0.006145271967424613`;
- empirical `p_ge = 1/2001`.

Descriptive quantities:

- observed / q99 = approximately `2.1349`;
- observed / null median = approximately `4.2519`;
- observed - null median = approximately `0.00761511`.

Thus the middle80 layer also has strong exact-target localization.

### top10

- requested/valid rows: `2000`;
- undefined phase dropped: `0`;
- q32 area-residualized `m=2..13`: `0.020338646838593502`;
- sensitivity `m=2..11`: `0.020081216032261425`.

Target-jitter null:

- median: `0.02031897844196505`;
- q99: `0.02135267015256859`;
- max: `0.021957929689199896`;
- empirical `p_ge = 0.4802598700649675`.

Descriptive quantities:

- observed / null median = approximately `1.00097`;
- observed - null median = approximately `0.00001967`.

Therefore the large raw top10 score is almost entirely reproduced by nearby jittered frequency dictionaries and is **not** evidence of exact-`log(m)` localization.

## Raw ordering

The preregistered raw ordering replicates exactly:

`bottom10 > top10 > middle80`.

Numerically:

- bottom/top = `1.4380979293015628`;
- bottom/middle = `2.9375802391607935`.

However POISSON-04 reveals that raw cross-stratum scores cannot be interpreted directly as comparable localization strengths because their jitter baselines differ dramatically with stratum size and geometry.

In particular:

- bottom10 null median is `~0.02154`;
- top10 null median is `~0.02032`;
- middle80 null median is only `~0.00234`.

Hence the raw relation `top10 > middle80` is largely a baseline effect rather than exact-target enrichment.

## Null-centered comparison

Subtracting each stratum's own jitter median gives:

- bottom10 excess: `~0.00771146`;
- middle80 excess: `~0.00761511`;
- top10 excess: `~0.00001967`.

Thus bottom10 and middle80 have almost equal absolute exact-target excess over their own null baselines, while top10 has essentially none.

This does **not** constitute a formal between-stratum test because the three POISSON-04 null ensembles were generated independently. A matched common-jitter contrast is required before making a cross-stratum inferential claim.

## q16/q32 phase-stability gradient

The descriptive phase-stability gradient is strongly reproduced.

### bottom10

RMS phase error:

- `(1,0)`: `0.3235071343310121`;
- `(0,1)`: `0.31787280644744803`;
- `(1,1)`: `0.5299593915008706`;
- `(1,-1)`: `0.5527118131591734`.

### top10

RMS phase error:

- `(1,0)`: `0.04095288048587093`;
- `(0,1)`: `0.042963319314054074`;
- `(1,1)`: `0.056521136651768236`;
- `(1,-1)`: `0.056382046434318246`.

Thus pointwise cross-resolution phase stability improves strongly with amplitude, while exact-target enrichment is strongest away from the highest-amplitude layer.

## Correct scientific interpretation

POISSON-04 does **not** confirm the originally frozen three-stratum phase-singularity-amplification package.

It does independently establish the following finite-range OOS facts under the frozen target-jitter family:

1. the low-amplitude bottom10 phase-only layer again shows very strong exact-`log(m)` localization after amplitude removal and area residualization;
2. the middle80 layer also shows strong exact-target localization;
3. the highest-amplitude top10 layer has a large raw temporal score but no exact-target specificity relative to its local-frequency jitter baseline;
4. q16/q32 phase stability improves monotonically toward the high-amplitude layer;
5. therefore cross-resolution geometric phase stability and exact-frequency specificity are not the same property and can move in opposite directions.

A conservative summary is:

> **Exact Dirichlet-frequency localization survives in the low and intermediate Fourier-amplitude phase layers, while the most phase-stable high-amplitude layer loses exact-target specificity under the frozen local-frequency jitter test.**

This statement is stronger and more precise than the failed raw-score amplification package.

## Methodological correction exposed by POISSON-04

Cross-stratum raw score comparisons are confounded by stratum-dependent null baselines. Future amplitude-layer comparisons must therefore use either:

- matched common-jitter contrasts; or
- a preregistered null-normalized statistic.

The already observed POISSON-04 data may be used only for an explicitly exploratory diagnostic of this issue.

## Next diagnostic

`POISSON-04B_MATCHED_NULL_CONTRAST` will use the already built fresh OOS tensor and a common target-jitter dictionary for all strata on every Monte-Carlo draw.

It will report exploratory matched contrasts:

- `Delta_BT = score(bottom10) - score(top10)`;
- `Delta_BM = score(bottom10) - score(middle80)`;
- `Delta_MT = score(middle80) - score(top10)`.

The exact-frequency contrast will be compared against the distribution of the same contrast under common jitter. This removes stratum-specific baseline score differences from the inferential comparison.

POISSON-04B is explicitly post hoc/exploratory and cannot retroactively change the POISSON-04 frozen FAIL verdict.

## Guardrails

1. POISSON-03 remains `statistical PASS / phase-stability FAIL`.
2. POISSON-04 remains full confirmation FAIL.
3. POISSON-04B cannot be called confirmatory on loops `20001..40000`.
4. Finite-range localization is not an asymptotic theorem.
5. No Riemann-Hypothesis claim follows.
