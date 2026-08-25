# RH-SOL-02 · EXP-03 RATE — results

Status: exploratory, post-confirmation.
Date: 2026-08-24.

## Primary four-model comparison

The target is the translation-dependent variance fraction

`F_res = residual_mean_square / (zero_mode_variance + residual_mean_square)`

across the 20 non-overlapping 1000-loop blocks from EXP-02 HEIGHT.

With `x = log(T_median/(2*pi))`, the primary models were fitted in log-space and ranked by AICc and leave-one-block-out log-RMSE.

### All 20 blocks

| Model | Parameters | AICc | delta AICc | LOO log-RMSE |
|---|---|---:|---:|---:|
| `A/x^p` | `A=0.2136813978`, `p=3.1377574489` | -135.609339 | 0 | 0.034611 |
| `A*(T/(2*pi))^-alpha` | `A=0.01429185767`, `alpha=0.4821582372` | -117.608635 | 18.000704 | 0.064619 |
| `A/x` | `A=0.003264919161` | -51.702102 | 83.907237 | 0.273401 |
| `A/sqrt(x)` | `A=0.001227871714` | -43.386768 | 92.222571 | 0.336576 |

The flexible inverse-log power law is decisively preferred within this candidate family on all 20 observed blocks:

`F_res approximately 0.213681 / [log(T/(2*pi))]^3.13776`.

This is an empirical finite-range fit, not an asymptotic theorem.

### Blocks 2..20 sensitivity

Removing the first low-height block gives:

| Model | Parameters | AICc | delta AICc | LOO log-RMSE |
|---|---|---:|---:|---:|
| `A/x^p` | `A=0.1835757007`, `p=3.0616304898` | -129.401369 | 0 | 0.032362 |
| `A*(T/(2*pi))^-alpha` | `A=0.01066405437`, `alpha=0.4425336399` | -125.938171 | 3.463198 | 0.036706 |
| `A/x` | `A=0.003125682892` | -62.565387 | 66.835982 | 0.191817 |
| `A/sqrt(x)` | `A=0.001163984029` | -54.488569 | 74.912800 | 0.237244 |

The fitted inverse-log exponent is stable near 3.1, but model separation from the power law in T becomes only moderate after removing block 1. Therefore the observed range does not yet uniquely establish the functional form.

## Component-exponent consistency

On all 20 blocks, separate descriptive power-law fits in `x` give:

- residual mean square exponent `r = 0.168147`;
- zero-mode variance exponent `z = 3.308081`;
- difference `z-r = 3.139934`;
- direct inverse-log exponent `p = 3.137757`.

On blocks 2..20:

- `r = 0.159214`;
- `z = 3.222423`;
- `z-r = 3.063210`;
- direct `p = 3.061630`.

Thus the direct rate exponent and the component-exponent difference agree to about 0.0022 on all 20 blocks and about 0.0016 on blocks 2..20.

This agreement is an important internal-consistency check but is not statistically independent evidence: for `F_res << 1`,

`F_res approximately residual_mean_square / zero_mode_variance`,

so if both numerator and denominator are themselves close to powers of `x`, the exponent difference is algebraically expected.

## Interpretation

The data support three increasingly conservative statements:

1. Fixed `1/log(T)` and `1/sqrt(log T)` decay are poor descriptions of the observed 20-block RATE sequence.
2. A free inverse-log power `1/[log(T/(2*pi))]^p` with `p` near 3.1 fits the observed range very well and cross-validates better than the tested alternatives.
3. The distinction between this inverse-log-power law and a power law in T is not yet independently established, because their AICc gap shrinks from 18.0 to 3.46 when the first block is removed.

The scientifically appropriate next test is out-of-sample prediction on new higher blocks with all RATE parameters frozen before generating those blocks.

## Guardrail

Do not report `p approximately 3.14` as a universal or asymptotic zeta law. It is a finite-height empirical exponent estimated after discovery on loops 1..20000. Independent higher-height validation is required.
