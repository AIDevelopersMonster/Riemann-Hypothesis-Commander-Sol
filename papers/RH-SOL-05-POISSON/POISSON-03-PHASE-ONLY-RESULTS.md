# RH-SOL-05 · POISSON-03 — phase-only unit-phasor results

Status: **statistical PASS / phase-stability FAIL** under the frozen preregistration.
Branch: `agent/rh-sol-05-poisson`.

## Frozen observable

POISSON-03 removes Fourier amplitude from the four POISSON-02 resolved complex modes

`(1,0), (0,1), (1,1), (1,-1)`

by replacing each midpoint-corrected coefficient

`G_q(a,b)`

with the unit phasor

`U_q(a,b) = G_q(a,b) / |G_q(a,b)|`

on the preregistered reliable mask.

The primary question is whether phase-only structure remains localized at the exact Dirichlet target dictionary `omega=log(m)` after scalar-area residualization.

## Frozen primary success rule

The preregistration required **all** of the following:

1. excluded fraction `<= 0.001` for every frozen mode on both ranges;
2. phase stability on q16/q32 with `rms_phase_error <= 0.10` rad and `rho_phase >= 0.995` for every mode on both ranges;
3. combined q32 area-residualized phase-only score above the target-jitter q99 with `p<=0.01` on calibration;
4. the same criterion independently on holdout;
5. qualitative q16/q32 agreement;
6. directionally consistent `m=2..11` sensitivity.

Because items 1 and 2 fail, POISSON-03 does **not** satisfy the full preregistered claim of a q-resolved phase-only arithmetic layer.

## Numerical reliability / phase-stability outcome

### Calibration 1..10000

All four frozen modes have excluded fraction

`0.0102`.

This exceeds the frozen reliability ceiling `0.001` by a factor of `10.2`.

Phase diagnostics:

| mode | RMS phase error | median abs phase error | rho_phase | frozen pass |
|---|---:|---:|---:|---|
| `(1,0)` | `0.1453217804350668` | `0.025751674736427765` | `0.9924003968976745` | no |
| `(0,1)` | `0.12440062429505401` | `0.02476349371864265` | `0.993564232081131` | no |
| `(1,1)` | `0.20710703869452202` | `0.047343315468854244` | `0.9826569493544074` | no |
| `(1,-1)` | `0.20397052027661802` | `0.04575004532177898` | `0.983499492830053` | no |

### Holdout 10001..20000

All four frozen modes have excluded fraction

`0.0131`.

This exceeds the frozen reliability ceiling by a factor of `13.1`.

Phase diagnostics:

| mode | RMS phase error | median abs phase error | rho_phase | frozen pass |
|---|---:|---:|---:|---|
| `(1,0)` | `0.13545414813349851` | `0.026153457938935937` | `0.9925238718429277` | no |
| `(0,1)` | `0.13904585471926964` | `0.02581991548634058` | `0.992278787201991` | no |
| `(1,1)` | `0.20184344626021036` | `0.04619313118757511` | `0.9836388299937517` | no |
| `(1,-1)` | `0.199389628924748` | `0.04587447930374787` | `0.9838644185210091` | no |

Thus none of the four individual channels satisfies the frozen joint phase-stability rule.

The contrast between relatively small median absolute phase errors and larger RMS errors suggests a non-Gaussian / tail-dominated phase discrepancy and motivates a separate diagnostic, but does not alter the frozen verdict.

## Phase-only temporal scores

Despite the stability-gate failure, the phase-only temporal scores reproduce strongly across calibration and holdout and agree extremely closely between q16 and q32.

For the combined four-channel observable `stable_all4`:

### Calibration

q16:

- phase-only `m=2..13`: `0.009977332094618251`;
- phase-only area-residualized `m=2..13`: `0.009008592549880042`;
- phase-only area-residualized `m=2..11`: `0.010202839002515958`.

q32:

- phase-only `m=2..13`: `0.00997922439682751`;
- phase-only area-residualized `m=2..13`: `0.009008319585884253`;
- phase-only area-residualized `m=2..11`: `0.010194035481730226`.

### Holdout

q16:

- phase-only `m=2..13`: `0.009699016236636365`;
- phase-only area-residualized `m=2..13`: `0.008885627917168246`;
- phase-only area-residualized `m=2..11`: `0.010092098219504252`.

q32:

- phase-only `m=2..13`: `0.009692590318928326`;
- phase-only area-residualized `m=2..13`: `0.008882093504839652`;
- phase-only area-residualized `m=2..11`: `0.010089209179402387`.

The q16/q32 agreement of the final area-residualized score is effectively exact at the scale of the statistic, even though per-sample q16/q32 phase stability does not meet the frozen threshold.

## Confirmatory target-jitter null

The primary confirmatory statistic is the q32 combined four-channel area-residualized phase-only `m=2..13` score.

### Calibration

- observed: `0.009008319585884253`;
- null median: `0.0019199937499810374`;
- null q95: `0.0031439964508839196`;
- null q99: `0.0041306808471196`;
- null max: `0.00516497284912114`;
- empirical `p_ge = 0.0004997501249375312`.

Derived descriptive ratios:

- observed / q99 = approximately `2.181`;
- observed / null max = approximately `1.744`.

### Holdout

- observed: `0.008882093504839652`;
- null median: `0.0019126755599677913`;
- null q95: `0.0031264450885041626`;
- null q99: `0.0038798438852725194`;
- null max: `0.005327228042895833`;
- empirical `p_ge = 0.0004997501249375312`.

Derived descriptive ratios:

- observed / q99 = approximately `2.289`;
- observed / null max = approximately `1.667`.

Both ranges therefore hit the Monte-Carlo floor `1/(2000+1)` and exceed even the largest generated target-jitter surrogate.

## Scientific interpretation

The correct POISSON-03 verdict is deliberately two-part.

### What is supported

1. Fourier amplitude can be removed completely on the reliable samples while a strong exact-`log(m)` temporal localization remains.
2. This localization survives blockwise residualization against scalar filled area.
3. It reproduces independently on loops `10001..20000` with nearly identical score.
4. q16 and q32 phase-only temporal scores agree extremely closely.
5. The exact target dictionary beats the preregistered independent target-jitter null by a large margin on both ranges.

Thus phase-only geometry contains a reproducible finite-range Dirichlet-frequency signature under the tested statistic.

### What is not yet supported

The frozen claim of a **q-resolved phase-only arithmetic layer** is not established because:

- the numerical reliability gate fails (`~1.0%` to `~1.3%` excluded vs frozen `0.1%` ceiling);
- every frozen mode fails at least one q16/q32 phase-stability threshold;
- diagonal modes in particular have RMS phase discrepancy around `0.20` rad and coherence around `0.983`.

The statistical target localization may therefore be robust to a minority of phase-unstable samples even though individual phase values are not uniformly q-stable enough for the stronger resolved-coefficient interpretation.

## Structural clue

The excluded fraction is exactly the same across all four frozen modes within each range:

- calibration: `0.0102` for every mode;
- holdout: `0.0131` for every mode.

This is unlikely to be ignored as a generic per-mode numerical accident. It motivates a diagnostic of mask overlap, stable-layer energy and translation variance on the excluded loops.

In particular, a natural hypothesis is that these loops form a common low/nonzero-spatial-energy class where unit phase is intrinsically undefined or poorly conditioned. This hypothesis is **not established by POISSON-03** and must be tested without changing the frozen POISSON-03 verdict.

## Next step

POISSON-03B will diagnose the phase-stability failure without weakening the preregistered thresholds:

- compare the four near-zero masks and their Jaccard overlap;
- test whether excluded loops coincide with zero or very low stable-shell energy / translation variance;
- stratify q16/q32 phase discrepancy by amplitude using target-blind amplitude quantiles;
- report whether RMS instability is concentrated in a small low-amplitude tail;
- recompute temporal target localization by predeclared amplitude strata only as an exploratory structural diagnostic, not as a replacement primary test.

## Guardrails

1. POISSON-03 remains a frozen **statistical PASS / phase-stability FAIL** regardless of POISSON-03B.
2. No post-hoc threshold relaxation is permitted.
3. The target-jitter null addresses exact-frequency localization, not all conceivable null models.
4. Finite-range phase-only localization is not an asymptotic theorem.
5. No Riemann-Hypothesis claim follows from this result.
