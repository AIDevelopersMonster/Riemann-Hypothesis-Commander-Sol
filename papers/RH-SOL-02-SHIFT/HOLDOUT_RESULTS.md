# RH-SOL-02 · SHIFT — independent holdout results

Date: 2026-08-23
Holdout range: loops 10001–20000
Calibration freeze: `CALIBRATION_FREEZE.md`

## Status

**Independent confirmation: PASS for the predeclared qualitative claims.**

The holdout was evaluated after the calibration pipeline was frozen. No target set, q value, fill rule, block size, spectral frequency grid, jitter width, or primary score definition was changed after viewing the holdout.

Canonical local holdout cube:

- artifact: `holdout_10001_20000.npz`
- size: `4,488,218` bytes
- SHA-256: `e239db2ba8b50709f803aea3647783ab554534a59bd537fc03b137ec23da27fe`

## Primary q=16 winding shift map

Frozen observable: `C_n(delta)` on the q=16 midpoint translation grid, non-zero winding fill rule.

Observed holdout summary:

- median comb score: `3.1817637264`
- mean comb score: `3.1819244909`
- minimum: `3.1707919712`
- maximum: `3.1910624225`
- raw jitter `p < 0.05`: `256/256`
- BH `q < 0.05`: `256/256`
- strongest shift: `delta=(0.96875,0.84375)`, score `3.1910624225`
- weakest shift: `delta=(0.53125,0.28125)`, score `3.1707919712`

The map remains narrow and spatially persistent. The total q=16 score range is only about `0.02027` relative to a mean near `3.182`.

The absolute holdout score is larger than the calibration score. This is **not** interpreted by itself as evidence that the arithmetic signal grows with height, because the scalar score is not normalized to be directly comparable across disjoint height ranges. Height dependence is reserved for a separate post-confirmation analysis.

## Translation zero mode and filled area

For q=16 winding:

- `MAE(Cbar_n - Area(D_n)) = 0.0085198762`
- RMS error: `0.0124335252`
- maximum absolute error: `0.0923665844`
- correlation: `0.9999999559`
- zero-mode variance fraction: `0.9996456779`

Thus the finite translation mean again reproduces the filled area with extremely high accuracy, independently of the calibration range.

### Area spectrum

- area comb score: `3.1843117372`
- null median: `0.8909381523`
- null q99: `1.4670184066`
- empirical p-value: `4.99975e-05`
- best common shift: `+0.00025`

### Finite-q translation mean

- comb score: `3.1841341713`
- empirical p-value: `4.99975e-05`
- best common shift: `+0.00025`

The common-shift optimum remains extremely close to zero, supporting alignment with the predeclared `log(m)` targets rather than a displaced comb.

## Translation-dependent residual

After removing the q=16 translation zero mode:

- median residual comb score: `0.9272485106`
- mean: `0.9722291837`
- minimum: `0.7394658722`
- maximum: `1.4913024879`
- raw jitter `p < 0.05`: `194/256`
- BH `q < 0.05`: `186/256`

The residual remains much weaker than the area/zero-mode signal but is not null everywhere. Compared with calibration, the fraction of BH-significant residual cells increases from `138/256` to `186/256`. This is recorded as a secondary empirical feature, not promoted to the primary claim.

## Resolution controls

Winding-rule area MAE:

- q=8: `0.0235238363`
- q=16: `0.0085198762`
- q=32: `0.0029271018`

Winding translation-mean comb scores:

- q=8: `3.1848603119`
- q=16: `3.1841341713`
- q=32: `3.1841694675`

Winding count-map median scores:

- q=8: `3.1821235843`
- q=16: `3.1817637264`
- q=32: `3.1820076449`

Winding residual-map median scores:

- q=8: `0.9371605100`
- q=16: `0.9272485106`
- q=32: `0.9229612393`

The qualitative result is stable under q=8,16,32.

## Fill-rule control

Winding and even-odd remain nearly identical at the aggregate level:

- exact area equality fraction: `0.991`
- area correlation: `0.9999991370`
- q=16 exact cell equality fraction: `0.998237109375`
- q=16 loops with any rule disagreement: `0.0076`
- q=16 translation-mean correlation: `0.9999991351`

The largest individual cell-count difference between fill rules is 5 in the holdout, but the mean absolute cell difference remains only about `0.00278`.

## Confirmation verdict by preregistered hypothesis

- **H1 translation-average identity:** independently supported.
- **H2 shift persistence of the Dirichlet structure:** independently supported across the full q=16 translation torus.
- **H3 translation-averaged persistence:** independently supported; the area/translation-zero-mode comb remains strong relative to the frozen jitter null.
- **H4 fill-rule robustness:** independently supported at the aggregate level.

## Scientific conclusion after holdout

The calibration conclusion survives an independent height range:

`C_n(delta) = area-like translation zero mode + smaller translation-dependent residual`.

At the scalar-count level, the dominant `log(m)` frequency architecture is therefore not tied to a privileged placement of the integer lattice. The leading carrier is a continuous geometric observable closely represented by the filled Argand-loop area, while a smaller nonzero translation component remains as a secondary structure.

This remains an empirical statement about the chosen zeta-loop observable. It is not a proof of the Riemann hypothesis and does not imply that the full RH-SOL-01 spatial tensor is reducible to area.

## Next analysis boundary

EXP-01 confirmatory analysis is now closed. Any investigation of why the absolute comb score differs between calibration and holdout, or how signal strength evolves with height, is **post-confirmation exploratory work** and must be versioned and reported separately from the frozen holdout test.
