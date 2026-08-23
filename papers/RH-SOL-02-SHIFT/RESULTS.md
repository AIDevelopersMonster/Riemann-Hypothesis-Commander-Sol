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

### Next executable milestone

1. Run the upstream convergence audit on a larger calibration subset.
2. Freeze the curve-resolution/boundary ambiguity rule.
3. Generate the q=16 calibration tensor/count field over loops 1–10000, with q=8 and q=32 controls.
4. Apply a predeclared shift-persistence spectral score to `C_n(delta)` across loop index n.
5. Only after the score is frozen, open loops 10001–20000 as the first independent height holdout.
