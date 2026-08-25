# RH-SOL-02 · SHIFT — research closeout

Status: research phase closed; manuscript synthesis remains.
Closeout date: 2026-08-25.

## Core question

Does the Dirichlet-frequency structure reported in RH-SOL-01 survive arbitrary translation of the sampling lattice, or is it tied to the special placement of the integer grid?

## Answer

Yes at the scalar-count level tested here, and the dominant carrier is not the special integer-grid placement.

For midpoint translation grids q=8,16,32 and both winding and even-odd fill rules, the scalar count field

`C_n(delta)`

retains the predeclared log-integer spectral architecture across essentially the whole translation torus. The finite-q translation mean converges tightly to filled loop area.

The decomposition

`C_n(delta) = Cbar_n + R_n(delta)`

shows that the dominant scalar spectral signal is carried by the translation zero mode `Cbar_n`, numerically indistinguishable from continuous filled area at the tested resolutions. The translation-dependent residual is much smaller and heterogeneous.

## Confirmatory milestones

### EXP-01 SHIFT

Calibration loops 1..10000 followed by a frozen independent holdout on loops 10001..20000 supported:

- H1 translation-average calibration;
- H2 shift persistence;
- H3 translation-averaged persistence;
- H4 q/fill-rule robustness.

The independent holdout reproduced the qualitative result without tuning.

### EXP-02 HEIGHT

Exploratory 1000-loop blocks over loops 1..20000 showed:

- normalized area/zero-mode comb excess rises from a low-height formation regime and enters a high plateau;
- best common frequency shift approaches zero;
- relative translation-dependent variance decreases strongly with height.

Important refinement: absolute residual mean square does not vanish; the residual fraction falls because zero-mode variance grows substantially faster.

### EXP-03 RATE

Exploratory model comparison on loops 1..20000 found the best simple candidate among the frozen family to be

`F_res(T) = A / [log(T/(2*pi))]^p`

with

- `A = 0.21368139779723283`;
- `p = 3.137757448939574`.

The strongest competing two-parameter model was a power law in `T/(2*pi)`.

### EXP-04 RATE-OOS

A frozen out-of-sample test on completely unseen loops 20001..40000 selected the inverse-log-power model without refitting.

Primary frozen scores:

- M1 inverse-log-power RMSE(log error): `0.0514155365`;
- M2 power in T RMSE(log error): `0.0897821942`;
- ratio M2/M1: `1.7462074750`;
- block wins: M1 `16/20`, M2 `4/20`.

The frozen M1 mean signed log error was `-0.0038996429`, corresponding to only about `-0.39%` geometric multiplicative bias over the OOS range.

Post-primary OOS-only refitting gave `p approximately 3.081`, close to the training estimate `3.138`; a descriptive 1..40000 refit gives `p approximately 3.126`.

## Strongest defensible conclusions

1. The scalar Dirichlet-frequency structure is not tied to one placement of the integer lattice.
2. Translation persistence is dominated by the continuous filled-area / translation-zero mode.
3. The relative translation-dependent contribution decreases strongly with height because the zero-mode component grows faster, not because the absolute residual disappears.
4. Over the tested finite-height range, an inverse power of `log(T/(2*pi))` with exponent near `3.1` predicts the residual fraction substantially better out of sample than the strongest tested T-power competitor.

## Guardrails

- None of these results proves the Riemann Hypothesis.
- The RATE law is empirical and finite-height, not an asymptotic theorem.
- The residual component is not claimed to vanish.
- The jitter null tests target-frequency alignment; they are not a complete geometry-preserving firewall.
- Stronger causal/arithmetic claims are deferred to RH-SOL-04 FIREWALL.
- Direct use of actual zero ordinates, without smooth local time warping, is deferred to RH-SOL-03 REALZERO.

## Handoff

The next module on the series map is:

**RH-SOL-03 · REALZERO — Dirichlet Frequencies without Smooth Time.**

Its task is to test whether the comb survives a direct irregular-time spectral analysis on the actual zero-pair times, rather than the blockwise smooth `dt/dn` conversion used in RH-SOL-01/02.
