# RH-SOL-05 · POISSON-02 — complex stable-mode phase-layer results

Status: completed on calibration and independent holdout.
Branch: `agent/rh-sol-05-poisson`.

## Frozen question

POISSON-02 tested the four independent complex representatives inherited from the fully q-stable POISSON-01B shells:

- `(1,0)`;
- `(0,1)`;
- `(1,1)`;
- `(1,-1)`.

The deterministic midpoint-grid phase was removed before q16/q32 comparison. No temporal target score entered mode selection.

## Complex q-stability

All four frozen channels satisfy the preregistered complex-stability criteria on both ranges:

`E_complex <= 0.10`

and

`rho_complex >= 0.995`.

### Calibration

| Mode | E_complex | rho_complex | Pass |
|---|---:|---:|---|
| `(1,0)` | `0.04976700046048635` | `0.9987646409972512` | yes |
| `(0,1)` | `0.050644731364794734` | `0.9987202534957366` | yes |
| `(1,1)` | `0.08593284203985006` | `0.9963256216073534` | yes |
| `(1,-1)` | `0.0853687058525731` | `0.9963745463277212` | yes |

### Holdout

| Mode | E_complex | rho_complex | Pass |
|---|---:|---:|---|
| `(1,0)` | `0.05075686883526162` | `0.9987129114675269` | yes |
| `(0,1)` | `0.051792934536804` | `0.9986607872243215` | yes |
| `(1,1)` | `0.08488922805109965` | `0.9964223303024073` | yes |
| `(1,-1)` | `0.08464431097900278` | `0.996432160726417` | yes |

Thus the entire POISSON-01B stable layer is promoted from power-resolved to empirically complex-resolved across q16/q32.

## Temporal complex scores

The phase-invariant complex Frobenius target statistic reproduces closely across q16 and q32. The combined four-channel q32 scores are:

Calibration:

- complex `m=2..13`: `0.0043850834807801905`;
- complex `m=2..11`: `0.0047770101578705915`;
- area-residualized complex `m=2..13`: `0.0038999336553959298`;
- area-residualized complex `m=2..11`: `0.0042387396896824674`.

Holdout:

- complex `m=2..13`: `0.00426154405301184`;
- complex `m=2..11`: `0.004604568993790836`;
- area-residualized complex `m=2..13`: `0.004009542907945907`;
- area-residualized complex `m=2..11`: `0.004345156737484117`.

The q16 values are nearly identical:

- calibration area-residualized `m=2..13`: `0.0038835059187925956`;
- holdout area-residualized `m=2..13`: `0.0039999024600223506`.

This excludes a simple q32-only phase artifact within the tested resolution pair.

## Per-channel replication

All four independent channels retain positive area-residualized complex target scores on both ranges. For q32, primary `m=2..13`:

| Mode | Calibration | Holdout |
|---|---:|---:|
| `(1,0)` | `0.002868759989104436` | `0.002718466511945234` |
| `(0,1)` | `0.005062880229436815` | `0.005645628483082704` |
| `(1,1)` | `0.00381535753130617` | `0.0037159745982554442` |
| `(1,-1)` | `0.0035058786998396936` | `0.0032702399977123904` |

The `(0,1)` channel is descriptively strongest, but no mode is promoted or discarded on that basis.

## Shell-level replication

q32 area-residualized primary complex score:

- shell `r^2=1`: calibration `0.003988032364544268`, holdout `0.004199027726117965`;
- shell `r^2=2`: calibration `0.0036556618780443895`, holdout `0.003493440270625551`.

Both complete resolved shells therefore retain phase-sensitive temporal structure beyond the scalar area layer.

## Power-only comparator

The corresponding q32 combined stable-layer power scores are much larger:

- calibration power `m=2..13`: `0.054130781788402596`;
- holdout power `m=2..13`: `0.0459034718151544`.

For comparison, the combined area-residualized complex scores are about `0.00390` and `0.00401`.

The two statistics are not a linear decomposition and their ratio must not be interpreted as a literal fraction of information. Nevertheless, the large scale difference is a strong descriptive indication that the currently resolved target structure is predominantly associated with magnitude / energy variation rather than being obviously dominated by complex orientation.

## Preregistered verdict

POISSON-02 satisfies the preregistered **phase-resolved layer** success pattern:

1. all four frozen representatives are complex-stable on both ranges;
2. complex exact-target scores reproduce on holdout;
3. area-residualized complex scores remain positive and of similar magnitude on both ranges;
4. q16 and q32 temporal results agree closely.

Therefore the strongest result supported by POISSON-02 is:

> The resolved nonzero spatial Fourier layer is not only stable in power. Its midpoint-corrected complex coefficients are themselves highly stable across q16/q32 and retain reproducible phase-sensitive exact-`log(m)` temporal structure after removal of the scalar area component.

## Critical distinction: phase-sensitive is not phase-only

The complex observable `G` contains both magnitude `|G|` and unit orientation `G/|G|`. A temporal statistic applied directly to `G` is phase-sensitive but does not mathematically isolate phase from magnitude.

Consequently POISSON-02 does **not** yet establish the stronger statement

> Fourier phase alone carries the temporal arithmetic structure.

That statement requires an amplitude-free observable.

The large power-only comparator scores make this distinction scientifically important rather than merely terminological.

## Next step

POISSON-03 should test a strictly phase-only representation of the same four frozen complex channels, without any temporal mode selection. The natural object is the unit phasor

`U_n(ell) = G_n(ell) / |G_n(ell)|`

where the coefficient is numerically nonzero, with a preregistered treatment of near-zero amplitudes and direct q16/q32 circular phase-consistency checks.

This next stage will distinguish:

- a genuinely phase-carried temporal layer;
- from an energy-dominated layer whose complex score in POISSON-02 is induced mainly by amplitude variation.

## Guardrails

1. Complex q-stability is empirical q16/q32 agreement, not exact recovery of the continuous Fourier coefficient.
2. Positive complex scores are structural statistics, not p-values.
3. POISSON-02 is phase-sensitive, not phase-only.
4. No Riemann-Hypothesis claim follows from this result.
