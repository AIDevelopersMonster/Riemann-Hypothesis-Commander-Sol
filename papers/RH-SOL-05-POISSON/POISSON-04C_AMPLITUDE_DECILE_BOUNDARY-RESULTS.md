# RH-SOL-05 · POISSON-04C_AMPLITUDE_DECILE_BOUNDARY — results

Status: **strong exploratory boundary result; not confirmatory**.
Branch: `agent/rh-sol-05-poisson`.
Data: already inspected POISSON-04 OOS tensor, loops `20001..40000`.

POISSON-03 remains `statistical PASS / phase-stability FAIL`.
POISSON-04 remains frozen **full confirmation FAIL**.
POISSON-04B remains exploratory.

## Executive result

The ten-decile amplitude profile does **not** support a simple monotone law of the form

`lower spatial Fourier amplitude => stronger exact-frequency specificity`.

Instead it reveals a broad arithmetic-sensitive regime through approximately the first seven amplitude deciles, followed by a sharp attenuation in the upper three deciles and near-complete disappearance in the top decile.

The max-over-splits boundary scan selects

`D1..D7 | D8..D10`

with

- `T_exact_max_z = 11.840599709750434`;
- family-wise `p_max = 1/2001 = 0.0004997501249375312`;
- null q99 `4.022306278501032`;
- null maximum `6.422570532557473`.

Thus the observed best split exceeds every one of the 2000 max-over-nine-splits jitter surrogates.

Because the same data motivated the scan, this remains exploratory and must be validated on fresh loops before promotion.

## Amplitude coordinate

For each loop

`M_n = min_ell |G32_n(ell)|`

over the four frozen modes `(1,0),(0,1),(1,1),(1,-1)`.

The empirical decile edges were:

- q10 = `0.013469199036563101`;
- q20 = `0.02429746464506002`;
- q30 = `0.03666072938992199`;
- q40 = `0.049565162908478844`;
- q50 = `0.06233686786643069`;
- q60 = `0.07499116955069833`;
- q70 = `0.08898620569772585`;
- q80 = `0.12347616427691284`;
- q90 = `0.1743241145167231`.

The candidate regime boundary selected by the corrected scan is therefore the **empirical 70th percentile**, not an absolute amplitude constant.

## Decile profile

For each decile, `E = exact_score - matched_null_mean`.

| Decile | Exact score | Null mean | E | z | p_ge |
|---|---:|---:|---:|---:|---:|
| D1 | 0.02924897 | 0.02160707 | 0.00764189 | 9.7816 | 1/2001 |
| D2 | 0.02645129 | 0.02036182 | 0.00608947 | 9.2808 | 1/2001 |
| D3 | 0.02936986 | 0.02060453 | 0.00876533 | 11.5898 | 1/2001 |
| D4 | 0.02904293 | 0.02046942 | 0.00857351 | 11.2349 | 1/2001 |
| D5 | 0.03129287 | 0.02051426 | 0.01077860 | 11.7699 | 1/2001 |
| D6 | 0.04014887 | 0.02083721 | 0.01931166 | 12.0752 | 1/2001 |
| D7 | 0.03325048 | 0.02034821 | 0.01290227 | 10.9470 | 1/2001 |
| D8 | 0.02422565 | 0.02041918 | 0.00380647 | 7.0540 | 1/2001 |
| D9 | 0.02387407 | 0.02041381 | 0.00346025 | 6.8396 | 1/2001 |
| D10 | 0.02033865 | 0.02033012 | 0.00000853 | 0.0187 | 0.50075 |

### Structural reading

1. `D1..D7` all show very large exact-target excess.
2. The strongest decile is not the lowest-amplitude layer but `D6`, with excess `0.01931166` and z `12.0752`.
3. `D8` and `D9` still retain statistically strong exact-frequency localization, but their excess falls by roughly a factor of three to five relative to the D5-D7 peak.
4. `D10` has essentially no exact-target excess at all.

Therefore the profile is better described as

`strong regime -> attenuated shoulder -> null top layer`

than as a binary step or monotone singularity law.

## Adjacent changes

The largest downward adjacent change in exact-minus-null excess is

`D8 - D7 = -0.009095795627150665`.

The preceding peak occurs at D6:

`D6 - D5 = +0.008533058894702204`,

followed by

`D7 - D6 = -0.006409394020222517`.

This places the main attenuation zone around the D6-D8 neighborhood, while the family-wise best aggregate boundary is after D7.

## Boundary scan

The strongest corrected aggregate split is `k=7`:

`D1..D7` versus `D8..D10`.

For k=7:

- exact contrast: `0.008445106720237707`;
- null mean: `0.0002898014475564467`;
- null sd: `0.0006887577886756507`;
- z from null mean: `11.840599709750434`;
- unadjusted p: `1/2001`.

Nearby splits are also extreme:

- k=6: z `10.583105509529299`;
- k=8: z `11.520176251968746`;
- k=9: z `11.160638073764762`.

This breadth matters: the data do not identify a mathematically sharp one-decile discontinuity. They identify a robust **high-amplitude attenuation region** whose best empirical aggregate cut is the 70/30 split.

## Max-over-splits correction

The boundary was not chosen using an uncorrected best-pick p-value.

For each jitter draw, the same nine split statistics were computed and the maximum standardized split statistic was retained. The exact maximum

`11.840599709750434`

was then compared with that family-wise null distribution.

Results:

- null T q95: `2.646394132665853`;
- null T q99: `4.022306278501032`;
- null T max: `6.422570532557473`;
- family-wise p: `1/2001`.

Thus the amplitude-boundary signal survives the explicit nine-split search correction within the tested matched-jitter family.

## Non-monotonicity

Spearman correlation between decile rank and exact-minus-null-mean excess is only

`-0.35757575757575755`.

This confirms that a simple monotone amplitude gradient is the wrong model.

The decisive structure is regime-like:

- substantial specificity across low/intermediate amplitudes;
- a pronounced peak in D5-D7, especially D6;
- attenuation in D8-D9;
- disappearance in D10.

## Correct scientific statement

The strongest defensible exploratory statement is:

> **On loops 20001..40000, the phase-only exact-Dirichlet-frequency specificity of the frozen low spatial Fourier layer exhibits a strongly non-monotone amplitude profile. A max-over-nine-splits matched-jitter scan identifies the empirical 70th-percentile amplitude boundary as the strongest low/high regime separation, with family-wise Monte-Carlo p at the 1/2001 floor. The uppermost decile loses essentially all exact-target specificity, while the preceding two deciles retain a weaker but still significant signal.**

This is an exploratory finite-range statement.

## What is not established

POISSON-04C does not establish:

- a universal amplitude phase transition;
- an absolute threshold near `M=0.088986...`;
- monotonic decay with amplitude;
- asymptotic persistence of the 70/30 boundary;
- a theorem about zeta zeros or RH.

The absolute q70 value is range-specific and may drift with height. The natural confirmatory object is the **empirical amplitude rank split**, not the frozen numerical amplitude value.

## Next confirmatory target

The next independent experiment should freeze, before viewing new loops:

- fresh range beginning at loop `40001`;
- the same four q32 spatial modes;
- empirical amplitude rank `M_n = min |G32|`;
- a **single fixed 70/30 split** with no boundary scan;
- common-jitter matched contrast between lower 70% and upper 30%;
- primary success criterion: exact lower70-minus-upper30 contrast above matched-null q99 with `p<=0.01`;
- D10/top10 loss of specificity only as a secondary diagnostic unless an equivalence-style null criterion is preregistered.

A new zero table beyond index `40001` is required before this can be run independently.
