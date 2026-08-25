# RH-SOL-02 · SHIFT — calibration freeze before independent holdout

Freeze date: 2026-08-23
Calibration range: loops 1–10000
Planned independent confirmation range: loops 10001–20000

## Frozen primary observable

`C_n(delta) = number of shifted-lattice points inside loop n`

Primary fill rule: non-zero winding number.
Primary translation grid: q=16 midpoint grid.
Resolution controls: q=8 and q=32.
Fill-rule control: even-odd.

## Frozen spectral pipeline

- 10 blocks of 1000 loops.
- Linear detrend within each block.
- rFFT power.
- Median normalization over loop-frequency f in [0.01, 0.48].
- Physical-frequency grid omega in [0.40, 3.50] with step 0.0005.
- Dirichlet-comb targets: log(m), m=2..13.
- Comb score: mean interpolated spectral score at the predeclared targets.
- Common-shift scan: [-0.25, 0.25], 2001 points.
- Diagnostic jitter null: independent uniform +/-0.20 per target, B=20000, seed 20260822.
- q=16 winding per-cell multiplicity correction: Benjamini-Hochberg over 256 cells.

## Frozen calibration findings

Matched RH-SOL-01 legacy `t_near` file SHA-256:

`1ca04cba2b57f0e7d899fa084ce823e657d2c6c5c8c60019855f1673cb8094bf`

Frozen unshifted scalar baseline:

`2.0335818527661713`

Matched-time q=16 winding shift map:

- median comb score: `2.0412147112689816`
- mean comb score: `2.0413472107313644`
- min: `2.0330933408382648`
- max: `2.050622900090961`
- 255/256 cells above frozen unshifted baseline
- 256/256 raw jitter p<0.05
- 256/256 BH q<0.05

Matched-time q=16 winding zero-mode decomposition:

- area comb score: `2.0414476429487487`
- finite-q translation-mean comb score: `2.0411500404477843`
- translation-mean / area correlation: `0.999999930586428`
- zero-mode variance fraction: `0.9994398096598852`
- residual-map median comb score: `0.8827840632312661`
- residual cells with BH q<0.05: `138/256`

Resolution and fill-rule controls support the same qualitative conclusion.

## Holdout interpretation rules

The holdout is confirmatory for the predeclared qualitative claims, not a search for new thresholds.

Primary confirmation questions:

1. Does the q=16 winding count map retain a log-integer comb across a substantial part of the translation torus?
2. Does the translation mean continue to approximate filled area closely?
3. Does the area / translation zero mode retain the comb with the same frozen spectral pipeline?
4. Is the translation-dependent residual still much weaker than the zero mode?

No metric, target set, q value, fill rule, null width, block size, frequency range or score definition may be changed after inspecting holdout results. Any such change must be labeled exploratory and versioned separately.

For loops 10001–20000 there is no RH-SOL-01 legacy `t_near` table. Therefore the predeclared holdout time proxy is the zero-pair midpoint `(gamma_n + gamma_{n+1})/2`. The calibration showed that replacing the midpoint proxy by matched legacy `t_near` on loops 1–10000 changes the q=16 scores only negligibly and does not alter the qualitative conclusions.

Negative or partial confirmation results must be recorded unchanged.
