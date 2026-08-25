# RH-SOL-02 · EXP-04 RATE-OOS — results

Status: frozen out-of-sample prediction test completed.
Prediction range: loops 20001..40000.
Training/fitting range: loops 1..20000 only.

## Artifact fingerprint

- OOS cube: `rate_oos_20001_40000_q16_winding.npz`
- size: `1,566,043` bytes
- SHA-256: `c5b87c0d42c29750988193fd337e1cab838261d4b1215edbd1f5fef3c52ce53d`

## Frozen competing models

No parameter was refit before the primary score.

### M1 — inverse log-power

`F1(T) = 0.21368139779723283 / [log(T/(2*pi))]^3.137757448939574`

### M2 — power in T/(2*pi)

`F2(T) = 0.014291857670165177 * (T/(2*pi))^(-0.48215823718583606)`

The preregistered primary criterion was log-space prediction RMSE over the 20 new 1000-loop blocks.

## Primary frozen OOS result

**Primary winner: M1 — inverse log-power.**

| Metric | M1 inverse log-power | M2 power in T |
|---|---:|---:|
| RMSE(log error) | 0.0514155365 | 0.0897821942 |
| MAE(log error) | 0.0392281707 | 0.0777829224 |
| mean signed log error | -0.0038996429 | -0.0712054718 |
| relative RMSE | 0.0519513399 | 0.0844404156 |
| median absolute relative error | 0.0309666958 | 0.0644159672 |
| cumulative log-SSE | 0.0528711479 | 0.1612168479 |
| block wins | 16 / 20 | 4 / 20 |

The frozen primary RMSE ratio is

`RMSE_log(M2) / RMSE_log(M1) = 1.7462074750`.

Thus M2's log-RMSE is about 74.6% larger than M1's. Equivalently, M1 reduces log-RMSE by about 42.7% relative to M2 and reduces cumulative log-SSE by about 67.2%.

## Calibration / bias

M1 is nearly unbiased over the new range:

- mean signed log error: `-0.00389964`;
- multiplicative geometric bias: `exp(-0.00389964) = 0.996108`, i.e. about `-0.39%`;
- mean ordinary relative error: about `-0.26%`.

M2 shows a systematic downward bias:

- mean signed log error: `-0.07120547`;
- multiplicative geometric bias: `exp(-0.07120547) = 0.931271`, i.e. about `-6.87%`;
- mean ordinary relative error: about `-6.73%`.

This is important because the OOS result is not only a lower aggregate RMSE for M1: the competing T-power law increasingly underpredicts the observed relative residual fraction over this range.

## Block-wise result

M1 has smaller absolute log error in 16 of the 20 frozen OOS blocks. M2 wins blocks 21, 29, 37 and 39; there are no ties.

Observed `F_res` on the OOS range fluctuates around the smooth rate law rather than decreasing monotonically block by block. This is expected for a block statistic and should not be confused with failure of the large-scale rate description.

## Post-primary exploratory refit

The following calculations were performed only after the frozen OOS winner had already been recorded and therefore do not alter the primary test.

Refitting the inverse-log-power model on the OOS blocks alone gives approximately

`F_res(T) = 0.19027 / [log(T/(2*pi))]^3.08108`.

The OOS-only exponent

`p_OOS approximately 3.081`

is close to the training estimate

`p_train = 3.137757`.

A descriptive combined 1..40000 refit gives approximately

`F_res(T) = 0.20888 / [log(T/(2*pi))]^3.12564`.

Thus the exponent inferred after extending the observed range to 40,000 loops remains near `3.1`.

For comparison, an OOS-only refit of the T-power family gives approximately

`alpha_OOS approximately 0.3722`,

substantially shifted from the frozen training value `alpha_train = 0.482158`. This is consistent with the systematic OOS underprediction of the frozen T-power model.

These post-OOS refits are descriptive and must not be substituted for the frozen prediction result.

## Scientific interpretation

EXP-04 independently supports the finite-range empirical rate law

`F_res(T) proportional to [log(T/(2*pi))]^(-p)`

with `p` near `3.1` over the first 40,000 zeta Argand loops.

The strongest defensible statement is:

> A two-parameter inverse-log-power rate fitted on loops 1..20000 predicted the relative translation-dependent variance on the completely unseen loops 20001..40000 substantially better than the strongest competing two-parameter power law in T, without any parameter refitting; its OOS-only fitted exponent remained close to the original estimate.

This strengthens the RATE finding from exploratory model selection to successful out-of-sample transfer.

## Guardrails

1. This is a finite-height empirical rate result, not an asymptotic theorem.
2. The result concerns the relative residual fraction `F_res`; it does not imply that the absolute residual mean square tends to zero.
3. The previously observed decrease of `F_res` is driven by increasingly dominant zero-mode variance relative to the residual component.
4. The value `p approximately 3.1` is empirically stable over the tested range but is not claimed as an exact constant.
5. No claim about the Riemann Hypothesis follows from this result.
6. Further extension in height should use the already-frozen M1 law as a prediction, not repeatedly refit before evaluation.
