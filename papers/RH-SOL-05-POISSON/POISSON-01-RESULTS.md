# RH-SOL-05 · POISSON-01 — translation-mode decomposition results

Status: structural result obtained; low-shell interpretation requires the preregistered q-stability condition to be audited mode-by-mode before promotion.
Branch: `agent/rh-sol-05-poisson`.

## Data and exact identities

POISSON-01 used the existing RH-SOL-02 winding-fill translation tensors on two independent 10,000-loop ranges:

- calibration: loops `1..10000`;
- holdout: loops `10001..20000`.

For each q x q translation count map, the analyzer computed

`F_q = fft2(C_q)/q^2`.

The implementation verified the frozen zero-mode and Parseval identities. In particular, the discrete nonzero Fourier energy is numerically identical to translation variance:

`Enonzero_total = V_translation_variance`

at the reported precision on both ranges.

This realizes the exact torus principle underlying RH-SOL-05:

`Var_delta C_D(delta) = sum_{ell != 0} |hat 1_D(ell)|^2`

for the continuous periodization, with the q-grid version interpreted as an aliased discrete approximation.

## Zero mode = area layer

Using q=32, the translation zero mode tracks winding-filled area essentially perfectly.

Calibration:

- mean absolute `|Z-A|`: `0.0029675659873921417`;
- median absolute `|Z-A|`: `0.002047338280865202`;
- maximum absolute `|Z-A|`: `0.04859662437775114`;
- correlation `corr(Z,A)`: `0.999999991499581`.

Holdout:

- mean absolute `|Z-A|`: `0.0029271018258983624`;
- median absolute `|Z-A|`: `0.0019734948351814163`;
- maximum absolute `|Z-A|`: `0.037131583307541405`;
- correlation `corr(Z,A)`: `0.9999999948516985`.

The temporal exact-target scores are correspondingly indistinguishable:

Calibration, `m=2..13`:

- area: `0.05058665866662955`;
- translation zero mode: `0.05058665172038189`.

Holdout, `m=2..13`:

- area: `0.038677729776910974`;
- translation zero mode: `0.038677821253339746`.

Thus the SHIFT zero-mode/area identification is confirmed at substantially higher precision than needed for the conceptual argument.

## Nonzero spatial energies before area residualization

Primary `m=2..13` scores:

| Observable | Calibration | Holdout |
|---|---:|---:|
| `E1` (`r^2=1`) | `0.046877253649243354` | `0.04004020034093908` |
| `E1+E2` | `0.0541307817884026` | `0.04590347181515439` |
| `Elow` (`0<r^2<=4`) | `0.056315542240019015` | `0.04755173172676251` |
| `Ehigh` | `0.07115376813805535` | `0.05896236896716188` |
| `Enonzero_total` | `0.06451511553913392` | `0.05390687941443606` |

The same qualitative ordering reproduces under the `m=2..11` sensitivity dictionary.

The strongest raw scalar is `Ehigh`, not the zero mode.

## Area correlations

The nonzero-energy observables are strongly but not perfectly correlated with area:

Calibration:

- `corr(E1,A) = 0.732177702187731`;
- `corr(E1+E2,A) = 0.790190091076917`;
- `corr(Elow,A) = 0.8054296128936521`;
- `corr(Ehigh,A) = 0.9069382755011951`;
- `corr(Enonzero_total,A) = 0.862384234085346`.

Holdout:

- `0.7285880994885837`;
- `0.7899834862677348`;
- `0.8039221832640779`;
- `0.9013602668330287`;
- `0.8582863300665414`, respectively.

The near replication of these correlations across ranges indicates a stable geometric relationship rather than a calibration-only accident.

## Area-residualized temporal structure

After blockwise OLS removal of intercept plus area,

`X_perp = X - alpha - beta A`,

the exact-target scores remain positive and reproduce closely on holdout.

Primary `m=2..13`:

| Residualized observable | Calibration | Holdout | Residual/raw ratio (descriptive) |
|---|---:|---:|---:|
| `E1_perp` | `0.009500403716428898` | `0.01021567731946407` | `20.3% / 25.5%` |
| `(E1+E2)_perp` | `0.012860474345720069` | `0.013308005284241448` | `23.8% / 29.0%` |
| `Elow_perp` | `0.014237383317121297` | `0.014503339972136927` | `25.3% / 30.5%` |
| `Ehigh_perp` | `0.033837204101585465` | `0.030535294810883334` | `47.6% / 51.8%` |
| `Enonzero_total_perp` | `0.021749070838938664` | `0.02097806450252665` | `33.7% / 38.9%` |

The residual/raw ratios are descriptive only because the target score is nonlinear.

The most striking replication is that the residualized scores are of comparable magnitude on the independent holdout rather than collapsing toward zero.

## q-stability result

The analyzer reports `8` q-stable individual modes with `max(|a|,|b|)<=3` on calibration and again `8` on holdout under the frozen criterion

`R_16_32 <= 0.10`.

This is evidence that resolved nonzero spatial structure exists beyond the zero mode.

However, the current analyzer reports only the number of stable individual modes in its compact output and computes the declared shell energies from all q32 coefficients. The preregistration requires q-stability for a shell before that shell can be interpreted as a resolved continuous spatial layer.

Therefore the strong claim

> a specific low shell carries arithmetic information beyond area

is **not yet promoted** from POISSON-01 alone.

A short frozen audit, POISSON-01B, must first identify the exact stable vectors and test shell completeness / stable-subset scores without temporal mode selection.

## Structural conclusion already supported

Even before that audit, three conclusions are secure:

1. the translation zero mode is numerically the area observable;
2. translation variance is exactly the discrete nonzero Fourier energy by Parseval;
3. nonzero Fourier-energy observables retain reproducible exact-target temporal structure after linear area removal.

The third point is a descriptive incremental-information result. It is not yet a significance statement and not yet a shell-localized continuous-mode statement.

## Important caution about `Ehigh`

`Ehigh_perp` is the strongest area-residualized scalar in both ranges, but `Ehigh` contains unresolved and aliased q32 modes. Its strength is therefore a motivation for finer spatial analysis, not evidence that high continuous Fourier modes have already been identified.

## Next step

POISSON-01B will:

- print the exact q-stable vectors separately on calibration and holdout;
- identify their intersection;
- report completeness of the declared `r^2=1`, `2`, and `4` shells;
- compute energies using only the predeclared q-stable intersection, with no temporal-score-based selection;
- compare q16 and q32 temporal scores for the stable subset;
- area-residualize those stable-subset energies and report exact-target scores.

Only after this audit should RH-SOL-05 proceed to phase-sensitive complex Fourier coefficients.

## Guardrails

1. Positive target scores are not p-values; POISSON-01 is a structural decomposition stage.
2. Discrete q-grid Fourier coefficients are aliased approximations to continuous Poisson coefficients.
3. No shell is promoted as resolved until the q-stability audit is complete.
4. No Riemann-Hypothesis claim follows from this result.
