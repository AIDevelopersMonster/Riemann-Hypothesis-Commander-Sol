# RH-SOL-02 · SHIFT — results log

This file is append-only in spirit: record negative, null, ambiguous, and positive findings.

## 2026-08-22 — bootstrap / geometry calibration

### Implemented

- Primary shifted-lattice observable `C_n(delta)`.
- Primary fill convention: non-zero winding number.
- Sensitivity fill convention: even-odd parity.
- Boundary points excluded with explicit tolerance.
- Translation grid uses cell midpoints to avoid systematic hits at `delta=(0,0)`.

### Synthetic validation

The implementation was tested before use on zeta data:

1. Unit square: generic shifted count = 1, area = 1.
2. 2x2 square: generic shifted count = 4, area = 4.
3. Self-intersecting bow-tie: both winding and even-odd paths execute and can be compared.
4. Polygonal approximation to a disk of radius 1.7:
   - polygon area approximately `9.07908785194`;
   - q=32 midpoint translation mean approximately `9.0703125`.

This is consistent with the exact translation-average identity and is only a numerical sanity check, not a zeta-specific result.

---

## 2026-08-23 — upstream reconstruction opened

### New reproducible pipeline

A direct upstream generator is now implemented:

`zero ordinates -> zeta(1/2+i t) samples -> ordered closed Argand polygon -> declared fill rule -> shifted lattice counts`.

Default zero source is `mpmath.zetazero`; an external CSV zero table may be supplied explicitly. The generator records zero source, precision, number of curve segments, adaptive-tolerance settings, number of vertices and zeta evaluations.

Relevant code:

- `src/zeta_argand.py`
- `src/shifted_lattice.py`
- `scripts/validate_upstream.py`
- `scripts/generate_shift_dataset.py`

### Reproduction test against RH-SOL-01

The regenerated unshifted integer-lattice incidences were compared with the archived RH-SOL-01 incidence CSV for loops 1–30.

At 30 decimal digits:

| Uniform segments per loop | Generated incidences | Archived incidences | Extra | Missing | Mismatching loops |
|---:|---:|---:|---:|---:|---:|
| 60 | 141 | 141 | 0 | 0 | 0 |
| 120 | 141 | 141 | 0 | 0 | 0 |
| 240 | 142 | 141 | 1 | 0 | 1 |

The only 240-segment discrepancy is loop 14, point `(4,1)`. Under a much more finely sampled polygon this point is classified inside, but its distance to the approximated boundary is only about `8.5e-4`. This is therefore treated as a **boundary/convergence ambiguity**, not evidence that one discretization is automatically correct.

Machine-readable record: `analysis/upstream_validation_1_30.json`.

### Interpretation of the reproduction test

This is an important methodological finding: the published incidence table is largely reproducible from a fresh direct zeta evaluation, but a coarse/fine sampling change can flip a point very close to the curve. Therefore RH-SOL-02 must classify loop geometry with an explicit convergence protocol, especially for lattice points near the boundary.

---

## 2026-08-23 — first real shifted-lattice pilot, loops 1–10

Using 60 uniform curve segments, 30 decimal digits and the winding fill rule, midpoint shift grids q=8,16,32 were evaluated directly on the first ten zeta Argand loops.

The translation-average identity provides the calibration target

`mean_delta C_n(delta) -> Area(D_n)`.

Across loops 1–10, the mean absolute discrepancy `|mean_delta C_n - Area(D_n)|` was:

- q=8: approximately `0.02733`
- q=16: approximately `0.00583`
- q=32: approximately `0.00240`

The corresponding RMS discrepancies were approximately:

- q=8: `0.03227`
- q=16: `0.00763`
- q=32: `0.00266`

Thus the empirical translation mean converges rapidly toward the filled area as q increases, as required by the exact translation-average identity.

For loops 1–10 the winding and even-odd rules produced identical pilot summaries. This is only a small-height observation and does not remove the need for the predeclared fill-rule sensitivity analysis.

Detailed table: `analysis/pilot_shift_1_10_summary.csv`.

### Computational optimization

The q x q midpoint family is now evaluated through a single grid of spacing `1/q`, with each fine-grid point tagged by its translation residue class. This is exactly the same midpoint family as q^2 separate shifted-lattice evaluations but avoids repeating the geometric classification q^2 times.

### Current status

**H1 (translation-average calibration): pilot passes on loops 1–10.**

No conclusion has yet been drawn for H2/H3, the persistence of the Dirichlet `log m` spectrum under shift. A ten-loop sample is far too short for that question.

---

## 2026-08-23 — EXP-01 scalar-count baseline frozen before the shift map

Before generating the full shifted dataset, the spectral observable was reduced to the scalar loop count

`C_n(0) = number of interior integer-lattice points in loop n`

using the published RH-SOL-01 10,000-loop incidence table. This checks that the spatial tensor is not required merely to recover the logarithmic temporal architecture.

The spectral score deliberately mirrors RH-SOL-01: 1000-loop blocks, linear detrending, median-normalized rFFT energy, smooth conversion from loop-index frequency to physical angular frequency, and block aggregation by mean `log1p` energy.

For `m = 2..13`:

- scalar comb score at the exact targets `omega = log(m)`: `2.0335818528`;
- independent ±0.2 per-target jitter null, `B=20000`, seed `20260822`;
- null median: `0.9264314803`;
- null 95th percentile: `1.1664037953`;
- null 99th percentile: `1.2870944662`;
- empirical upper-tail p-value: `4.99975e-05` (no surrogate exceeded the observed score);
- best common frequency shift: approximately `-0.0015`, with score `2.0446975953`.

The strongest scalar-count peaks remain near `log 2`, `log 3`, `log 4`, `log 5`, ... . Therefore EXP-01 can use the compact field `C_n(delta)` rather than reconstructing a full spatial occupancy tensor for every lattice translation.

Machine-readable baseline:

- `analysis/exp01_baseline_count_summary.json`
- `analysis/exp01_baseline_count_comb.csv`

This baseline was frozen **before** inspecting the full shift-persistence map.

### EXP-01 implementation status

The following are now fixed in the research branch:

- `src/dirichlet_spectrum.py` — frozen scalar spectral score;
- `scripts/fetch_lmfdb_zeros.py` — external zero-table acquisition;
- `scripts/exp01_build_chunk.py` — resumable chunk generator;
- `scripts/exp01_merge_chunks.py` — contiguous chunk merger;
- `scripts/exp01_analyze_shift_map.py` — q x q comb-score map, jitter null and Benjamini-Hochberg correction.

The published full-analysis archive does not contain ordered Argand-loop vertices, so the 10,000-loop SHIFT field cannot be recovered from the old binary incidence table alone; real loop boundaries must be regenerated.

---

## 2026-08-23 — EXP-01 full q=16 winding shift map

A full calibration cube was generated for loops 1–10000 from LMFDB zero ordinates 1–10001. The cube contains q=8,16,32 midpoint translation fields under both winding and even-odd fill conventions.

Canonical local cube fingerprint:

- artifact: `calibration_1_10000.npz`;
- size: `4,444,748` bytes;
- SHA-256: `229e4fe632bfa5cc6821c0edb93eaff982052e2d85378b489c2b7a1018ba473c`.

The primary q=16 winding map was evaluated over all 256 midpoint shifts using the zero-pair midpoint time proxy and the frozen Dirichlet-comb score.

Observed map summary:

- median comb score: `2.0413200073`;
- mean comb score: `2.0414418651`;
- minimum: `2.0332254345`;
- maximum: `2.0507165357`;
- fraction above the previously frozen unshifted scalar baseline `2.0335818528`: `255/256 = 0.99609375`;
- raw jitter `p < 0.05`: `256/256`;
- Benjamini-Hochberg `q < 0.05`: `256/256`.

Strongest midpoint shift: `delta = (0.09375, 0.65625)`, score `2.0507165357`.

Weakest midpoint shift: `delta = (0.15625, 0.28125)`, score `2.0332254345`.

### Primary interpretation

The scalar Dirichlet-frequency comb is **persistent rather than localized** on the q=16 translation torus. The total score range across all translations is only about `0.01749`, so the phenomenon is not concentrated near the original integer lattice placement.

However, the frozen unshifted scalar baseline used the RH-SOL-01 legacy `t_near` time proxy, whereas this q=16 map used the zero-pair midpoint proxy. Therefore the statement `255/256 above the frozen baseline` is descriptive rather than a strictly matched effect-size comparison. The within-map persistence conclusion does not depend on that mismatch.

---

## 2026-08-23 — EXP-01 translation zero-mode decomposition

The q=16 winding count field was decomposed as

`C_n(delta) = Cbar_n + R_n(delta)`,

where `Cbar_n` is the finite-q translation mean and `R_n(delta)` is the translation-dependent residual.

### Geometry calibration

The finite-q mean is an extremely accurate approximation to the filled loop area:

- mean absolute error `|Cbar_n - Area(D_n)|`: `0.0085078858`;
- RMS error: `0.0122167606`;
- maximum absolute error over 10,000 loops: `0.1080490658`;
- correlation between finite-q mean and filled area: `0.9999999306`.

### Variance decomposition

Across loop index and translation:

- translation-zero-mode variance: `1074.6317692218`;
- translation-residual mean square: `0.6023357590`;
- fraction assigned to the zero mode by this decomposition: `0.9994398097`.

Thus approximately `99.944%` of the scalar-count variance is translation-invariant at q=16, and only about `0.056%` lies in the translation-dependent residual.

### Spectral result for area and finite-q mean

Filled area itself carries the same predeclared log-integer comb:

- area comb score: `2.0415415257`;
- jitter-null median: `0.9284268041`;
- null 99th percentile: `1.2903242914`;
- empirical upper-tail p-value: `4.99975e-05`;
- best common frequency shift: `-0.0015`.

The finite-q translation mean gives essentially the same result:

- comb score: `2.0412438312`;
- empirical upper-tail p-value: `4.99975e-05`;
- best common frequency shift: `-0.0015`.

### Residual lattice component

After removing the translation zero mode, the residual score map is much weaker and heterogeneous:

- median residual comb score: `0.8827632779`;
- mean: `0.8985318642`;
- minimum: `0.7540767766`;
- maximum: `1.1520954487`;
- raw jitter `p < 0.05`: `154/256 = 0.6015625`;
- BH `q < 0.05`: `138/256 = 0.5390625`.

Strongest residual shift: `delta = (0.03125, 0.90625)`, residual score `1.1520954487`, BH `q = 0.00039998`.

Weakest residual shift: `delta = (0.65625, 0.78125)`, residual score `0.7540767766`, raw `p = 0.8700065`.

### Scientific interpretation

The dominant explanation of SHIFT persistence is now clear at the scalar-count level: the primary Dirichlet-frequency architecture is carried by the **translation zero mode**, numerically indistinguishable from the continuous filled area at q=16 resolution. The integer lattice is therefore not required for the dominant scalar spectral signal.

A weaker translation-dependent lattice residual remains detectable at a substantial subset of shifts, including `138/256` cells after BH correction under the present diagnostic jitter-null family. This residual must not yet be promoted to a separate arithmetic discovery: q=8/q=32 stability, fill-rule sensitivity, geometry/order/phase controls and a matched-time comparison are still required.

This result does **not** establish that the full RH-SOL-01 binary spatial tensor is reducible to area. It establishes the stronger and narrower statement that the scalar loop-count comb used for SHIFT is dominated by an area-like translation-invariant component.

### Revised status after EXP-01 primary run

- **H1 translation-average calibration: strongly supported at q=16.**
- **H2 shift persistence of the scalar log-integer comb: supported on the full q=16 midpoint torus.**
- **H3 translation-averaged persistence: supported in the calibration range, with the translation mean converging to area.**
- **H4 fill-rule robustness: not yet resolved on the full calibration range.**

The next controls are q=8/q=32, even-odd q=16, residual-map stability, and a matched time-proxy analysis before opening the 10001–20000 holdout.
