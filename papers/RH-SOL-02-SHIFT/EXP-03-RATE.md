# RH-SOL-02 · EXP-03 RATE — exploratory decay law for relative lattice variance

Status: post-confirmation exploratory.
Opened: 2026-08-23, after EXP-01 confirmation and EXP-02 HEIGHT.

## Question

Let

`F_res(T) = residual_mean_square / (zero_mode_variance + residual_mean_square)`.

Over the observed height range, what simple rate law best describes the decrease of `F_res`?

This is not a confirmatory test and cannot be promoted to an asymptotic theorem from 20 blocks.

## Data

Use the 20 non-overlapping 1000-loop blocks already defined in EXP-02 HEIGHT, loops 1..20000. The RATE analysis consumes the saved EXP-02 JSON and does not regenerate zeta loops.

Define

`x = log(T_median / (2*pi))`.

## Primary candidate laws

The primary comparison uses four simple positive models:

1. `F = A / x`
2. `F = A / sqrt(x)`
3. `F = A * exp(-alpha*x)`  (equivalently `A*(T/(2*pi))^(-alpha)`)
4. `F = A / x^p`

The fourth model is the one-parameter exponent extension of the first two logarithmic laws.

## Fit scale and comparison

Primary residuals are fitted in log-space:

`log(F_pred) - log(F_obs)`.

This treats relative errors rather than absolute errors as the fitting scale.

For every candidate report:

- fitted parameters;
- log-RMSE;
- relative RMSE;
- AICc computed from log-residual RSS;
- leave-one-block-out log-RMSE;
- leave-one-block-out relative RMSE.

Model ranking is descriptive. AICc differences and cross-validation agreement matter more than nominal coefficient p-values.

## Sensitivity

Repeat the primary four-model comparison on blocks 2..20 to check whether the first low-height block determines the inferred law.

Floor-bearing models may be fitted only as an explicitly labeled post-view sensitivity:

- `F = c + A/x^p`
- `F = c + A*exp(-alpha*x)`.

They do not replace the primary four-model ranking.

## Mechanistic decomposition

Because `F_res` is a ratio, also fit separate descriptive power laws in `x`:

`residual_mean_square ~ C_R * x^r`

and

`zero_mode_variance ~ C_Z * x^z`.

When `F_res << 1`,

`F_res approximately residual_mean_square / zero_mode_variance`,

so the component fits predict

`F_res ~ x^(r-z)`.

Compare the implied exponent `z-r` with the directly fitted exponent `p` from `A/x^p`.

This exponent identity is descriptive evidence for a mechanism, not a proof of asymptotic scaling.

## Guardrails

- EXP-03 is exploratory and post-view.
- The first 20,000 loops cannot establish an asymptotic rate.
- No extrapolation to RH or to arbitrarily large T is licensed.
- A nonzero floor, if weakly supported, must not be asserted as a limiting constant.
