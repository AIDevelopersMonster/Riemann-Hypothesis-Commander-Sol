# RH-SOL-05 · POISSON-01B — q-stability audit results

Status: completed; preregistered q-stability requirement satisfied for two complete low spatial shells.
Branch: `agent/rh-sol-05-poisson`.

## Frozen audit question

POISSON-01B tested whether the nonzero spatial layer seen in POISSON-01 survives the preregistered q16/q32 resolution criterion without selecting modes by temporal target score.

A mode was declared q-stable using only

`R_16_32 <= 0.10`

for its spatial power. The final mode set was frozen as the intersection of the calibration-stable and holdout-stable sets.

## Stable intersection

The calibration/holdout intersection contains exactly eight vectors:

- `(-1,-1)`;
- `(-1,0)`;
- `(-1,1)`;
- `(0,-1)`;
- `(0,1)`;
- `(1,-1)`;
- `(1,0)`;
- `(1,1)`.

Thus the intersection is exactly the union of two complete shells:

### Shell r^2 = 1

`{(-1,0),(1,0),(0,-1),(0,1)}`

Status: **complete, 4/4 stable**.

### Shell r^2 = 2

`{(-1,-1),(-1,1),(1,-1),(1,1)}`

Status: **complete, 4/4 stable**.

### Shell r^2 = 4

`{(-2,0),(2,0),(0,-2),(0,2)}`

Status: **not stable, 0/4 stable**.

No mode was added or removed using temporal target scores.

## Stable-intersection energy: q16/q32 agreement

### Calibration, loops 1..10000

- q16/q32 energy discrepancy: `0.026573778917923396`;
- q16/q32 correlation: `0.998682717721041`.

q16:

- mean energy: `0.3638980979783968`;
- median: `0.17001338927787435`;
- correlation with area: `0.7899550597007969`;
- exact-target `m=2..13`: `0.05411110414116057`;
- exact-target `m=2..11`: `0.060954552694272676`;
- area-residualized `m=2..13`: `0.012813531947363645`;
- area-residualized `m=2..11`: `0.01316912715000349`.

q32:

- mean energy: `0.36255316085734457`;
- median: `0.1695937790703994`;
- correlation with area: `0.790190091076917`;
- exact-target `m=2..13`: `0.054130781788402596`;
- exact-target `m=2..11`: `0.060963329571335934`;
- area-residualized `m=2..13`: `0.012860474345720066`;
- area-residualized `m=2..11`: `0.013193818986739256`.

### Holdout, loops 10001..20000

- q16/q32 energy discrepancy: `0.027065968072447356`;
- q16/q32 correlation: `0.9987400244200697`.

q16:

- mean energy: `0.3743182781186485`;
- median: `0.16893884192603315`;
- correlation with area: `0.7912308566571704`;
- exact-target `m=2..13`: `0.04601481856546655`;
- exact-target `m=2..11`: `0.052037904624323714`;
- area-residualized `m=2..13`: `0.013336945614062226`;
- area-residualized `m=2..11`: `0.014265631333406697`.

q32:

- mean energy: `0.37319762647802146`;
- median: `0.1687080577057618`;
- correlation with area: `0.789983486267735`;
- exact-target `m=2..13`: `0.0459034718151544`;
- exact-target `m=2..11`: `0.05189590291343399`;
- area-residualized `m=2..13`: `0.013308005284241442`;
- area-residualized `m=2..11`: `0.014219632412030444`.

## Primary result

POISSON-01B satisfies the preregistered success pattern for a resolved nonzero spatial layer.

The two complete shells `r^2=1` and `r^2=2` are selected solely by q16/q32 spatial stability and reproduce on the independent holdout. Their combined energy is nearly resolution invariant between q16 and q32 and retains a reproducible exact-`log(m)` temporal score after blockwise linear removal of area.

The strongest defensible statement is therefore:

> The translated-lattice observable contains a resolved nonzero spatial Fourier layer, supported by the complete shells `r^2=1` and `r^2=2`, whose temporal exact-`log(m)` structure is not eliminated by linear removal of the scalar area / zero-mode component.

This is a descriptive incremental-information result, not a causal decomposition.

## Why this matters

RH-SOL-02 SHIFT showed that the translation mean is essentially area and that the residual translation structure is small relative to the zero mode.

POISSON-01/01B now identifies that residual structure spectrally:

- zero mode = area;
- first axial shell `r^2=1` = resolved;
- first diagonal shell `r^2=2` = resolved;
- next axial shell `r^2=4` = not resolved under the frozen q16/q32 criterion.

Thus the nonzero residual is not merely an undifferentiated translation variance. A concrete low-dimensional spatial Fourier layer survives resolution refinement.

## Limitation of shell energies

Shell energies use `|F(ell)|^2` and therefore discard the complex phases of the Fourier coefficients. For a real translation-count map, opposite modes satisfy conjugacy, so the eight stable vectors correspond to four independent complex coefficients.

The next stage should test those phase-sensitive coefficients directly, with the deterministic midpoint-grid phase corrected before q16/q32 comparison.

## Guardrails

1. q-stability is empirical resolution stability, not proof of zero alias contamination.
2. The exact-target scores are structural scores, not p-values.
3. Area residualization removes only a linear blockwise area component.
4. No Riemann-Hypothesis claim follows from this result.
