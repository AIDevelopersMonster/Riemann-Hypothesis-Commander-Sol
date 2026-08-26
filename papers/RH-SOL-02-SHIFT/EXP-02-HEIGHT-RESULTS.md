# RH-SOL-02 · EXP-02 HEIGHT — results

Status: exploratory, post-confirmation.
Date: 2026-08-23.

## Primary 20-block HEIGHT result

Using 20 non-overlapping blocks of 1000 loops each over loops 1..20000, q=16 winding geometry, and the zero-pair midpoint time proxy for all blocks, the normalized Dirichlet-comb excess increased strongly with height while the best common frequency shift moved toward zero and the translation-dependent variance fraction decreased.

Primary m=2..13 trends versus `log(T/(2*pi))`:

- area E95: Pearson r = 0.976369, Spearman rho = 0.947368;
- translation-mean E95: Pearson r = 0.977544;
- |best common shift|: Pearson r = -0.851382;
- residual variance fraction: Pearson r = -0.938890, Spearman rho = -0.984962;
- residual-map median comb score: Pearson r = 0.771436.

These p-values are descriptive because EXP-02 was opened after EXP-01 confirmation.

The sequence is better described as formation -> alignment -> saturation than as an indefinitely linear height law. By roughly blocks 10..20, the area E95 values are concentrated in a narrow high band while alignment shifts are typically of order 1e-3 or smaller.

## Nyquist issue in the lowest block

At block 1, median height is approximately T=812.693. The asymptotic non-alias thresholds `T > 2*pi*m^2` for m=12 and m=13 are approximately 904.8 and 1061.9 respectively, so these two targets are not safely identifiable at the first block median.

A post-view sensitivity analysis therefore re-ran the height study with the common Nyquist-safe target dictionary m=2..11 for all 20 blocks. This sensitivity does not redefine the primary EXP-02 result.

## Nyquist-safe sensitivity, m=2..11

The principal height pattern survives removal of m=12 and m=13.

Across all 20 blocks:

- area E95: Pearson r = 0.973494, Spearman rho = 0.939850;
- translation-mean E95: Pearson r = 0.974211;
- |best common shift|: Pearson r = -0.879292;
- residual variance fraction: Pearson r = -0.938890, Spearman rho = -0.984962.

Excluding block 1 entirely still leaves strong trends over blocks 2..20:

- area E95: Pearson r = 0.962411, Spearman rho = 0.929825;
- residual variance fraction: Pearson r = -0.977782, Spearman rho = -0.982456;
- |best common shift|: Pearson r = -0.795090.

Therefore the principal height pattern is not explained by the low-block Nyquist boundary.

## Saturation regime

For blocks 10..20 in the common m=2..11 sensitivity:

- mean area E95 = 5.404845;
- standard deviation = 0.155522;
- minimum = 5.174423;
- maximum = 5.689417.

Within the high half, blocks 11..20, the area-E95 trend becomes much weaker:

- Pearson r = 0.594812;
- descriptive p = 0.0697.

The alignment-shift trend is no longer monotone in this high region:

- Pearson r = 0.390763;
- descriptive p = 0.264.

This supports the descriptive picture that the comb becomes well aligned and then enters a comparatively stable high-E95 regime rather than continuing to grow at the same rate indefinitely.

## Residual versus zero mode

A crucial decomposition result is that the residual variance fraction falls even though the absolute residual mean square does not fall.

Across all 20 blocks:

- residual mean square has Pearson r = +0.861129 with height;
- zero-mode variance has Pearson r = +0.982327 with height;
- residual variance fraction has Pearson r = -0.938890.

From the first to the last block, the residual variance fraction falls by a factor of approximately 4.6758.

Thus the correct interpretation is not that the translation-dependent residual disappears in absolute terms. Rather, the translation-invariant/area-like zero mode grows much faster and increasingly dominates the scalar count field.

This is consistent with the decomposition

`C_n(delta) = A_n + R_n(delta)`

at the scalar-count level, where the relative importance of the continuous carrier grows with height over the observed range.

## Scientific guardrail

EXP-02 is exploratory. The observed height dependence is an empirical regularity over the first 20,000 loops, not an asymptotic theorem and not evidence for the Riemann Hypothesis. The Nyquist-safe m=2..11 analysis was designed after viewing the primary m=2..13 result and is therefore a sensitivity analysis rather than an independent confirmation.

The strongest defensible statement is:

> Over the first 20,000 zeta Argand loops, the normalized log-integer spectral excess of the area/translation zero mode rises strongly with height, the frequency alignment approaches the predeclared log(m) targets, and the relative translation-dependent variance decreases; after an initial formation regime, the spectral excess appears to enter a high, comparatively stable plateau. The same qualitative pattern survives restriction to a common Nyquist-safe dictionary m=2..11.
