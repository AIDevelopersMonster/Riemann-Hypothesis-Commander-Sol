# RH-SOL-05 · POISSON-02 — complex stable-mode phase layer preregistration

Status: preregistered before inspection of phase-sensitive results.
Branch: `agent/rh-sol-05-poisson`.

## Motivation

POISSON-01B identified a frozen q-stable intersection consisting exactly of the complete shells `r^2=1` and `r^2=2`:

`(±1,0), (0,±1), (±1,±1)`.

Shell energies use only `|F(ell)|^2` and discard complex phase. Because each translation-count map is real, opposite Fourier modes are conjugate. The eight stable vectors therefore correspond to four independent complex coefficients.

POISSON-02 asks:

> Do the complex orientations of the resolved stable Fourier modes carry reproducible exact-`log(m)` temporal structure beyond scalar area and beyond shell-energy information?

## Frozen independent modes

No temporal selection is allowed. Use exactly these four representatives inherited from POISSON-01B:

- `(1,0)`;
- `(0,1)`;
- `(1,1)`;
- `(1,-1)`.

Their conjugates are redundant and are used only for numerical consistency checks.

## Midpoint-grid phase correction

The translation samples are taken at

`delta_ij = ((i+1/2)/q, (j+1/2)/q)`.

With

`F_q = fft2(C_q)/q^2`,

a resolved low mode carries the deterministic midpoint factor

`exp(pi i (a+b)/q)`

before alias contributions are considered.

Define the corrected discrete coefficient

`G_q(a,b) = F_q[a,b] * exp(-pi i (a+b)/q)`.

All q16/q32 phase-sensitive comparisons must use `G_q`, not the raw DFT coefficient.

For real count maps the corrected coefficients must satisfy

`G_q(-a,-b) = conjugate(G_q(a,b))`

up to floating precision.

## Complex q-stability diagnostics

For each of the four frozen representatives, separately on calibration and holdout, report:

1. power discrepancy inherited from POISSON-01B;
2. relative complex L2 error

`E_complex = ||G16-G32||_2 / (||G32||_2 + eps)`;

3. complex coherence

`rho_complex = |<G16,G32>| / (||G16||_2 ||G32||_2 + eps)`.

A representative is declared **complex-stable** if, on both calibration and holdout,

- `E_complex <= 0.10`, and
- `rho_complex >= 0.995`.

These thresholds are frozen before phase-sensitive temporal inspection.

If all four representatives pass, the full POISSON-01B stable layer is promoted to a phase-resolved layer. If only a subset passes, only that predeclared subset may be described as complex-stable; no replacement modes may be selected by temporal score.

## Complex temporal target statistic

For a complex vector observable `Y(t)` with one or more fixed spatial channels, evaluate each 1000-loop block as follows.

1. Detrend every complex channel against `[1,t]` by complex OLS.
2. At each target `omega=log(m)`, form the real temporal basis `[cos(omega t), sin(omega t)]`.
3. Orthogonally project every complex residual channel onto this two-dimensional temporal basis.
4. Define

`R2_complex = explained Frobenius energy / total residual Frobenius energy`.

5. Transform

`Q = -log(1-R2_complex+1e-15)`.

Average Q over targets and blocks.

This statistic is invariant under multiplying any fixed complex channel by a constant unit-modulus phase and is therefore not an artifact of an arbitrary real/imaginary axis choice.

Primary dictionary: `m=2..13`.
Sensitivity: `m=2..11`.

## Frozen channel groups

Compute phase-sensitive scores for q16 and q32 for:

1. each representative individually;
2. shell `r^2=1` vector: `(1,0),(0,1)`;
3. shell `r^2=2` vector: `(1,1),(1,-1)`;
4. combined stable vector: all four representatives.

No channel weighting is fitted to temporal targets.

## Area-residualized complex observables

For every frozen complex group, inside each 1000-loop block remove the complex OLS projection onto `[1,A]`, where `A` is winding-filled area:

`Y_perp = Y - alpha - beta A`.

Then apply the unchanged complex temporal target statistic.

This tests phase-sensitive structure beyond the scalar zero-mode/area layer.

## Power-only comparator

For each representative and group, also report the corresponding power-only scalar observable obtained from `|G|^2` (sum across group channels) and its existing scalar target score. This comparison is descriptive: it asks whether the complex vector statistic retains materially more or less temporal response than power alone.

## Frozen ranges

- calibration: loops `1..10000`;
- holdout: loops `10001..20000`.

Both q16 and q32 are analyzed independently.

## Success patterns

### Phase-resolved layer

A phase-resolved spatial layer is supported if:

1. at least one frozen representative is complex-stable by the q16/q32 criteria on both ranges;
2. its phase-sensitive exact-target score reproduces qualitatively on holdout;
3. its area-residualized complex score remains materially above zero on both ranges;
4. q16 and q32 temporal scores agree closely enough to exclude a purely resolution-specific phase artifact.

### Energy-dominated layer

If complex q-stability fails or phase-sensitive residualized scores add little beyond power-only behavior, conclude that the presently resolved information is primarily energy/magnitude based rather than demonstrably phase based.

## Guardrails

1. Midpoint phase correction removes only the deterministic sampling offset; aliasing can still contaminate complex coefficients.
2. Complex stability is empirical q16/q32 stability, not a proof of continuous-coefficient recovery.
3. No representative may be added or removed using temporal target scores.
4. No p-value threshold is introduced in this structural stage.
5. No Riemann-Hypothesis claim follows from any outcome.
