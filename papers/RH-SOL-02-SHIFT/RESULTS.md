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

### Current limitation

RH-SOL-01's published incidence table contains occupancy information on the unshifted integer grid, but shifted-lattice analysis requires sampled loop boundaries (ordered `x,y` vertices) or a reproducible upstream generator for `zeta(1/2+it)` between consecutive zeros. Therefore no claim about SHIFT persistence has yet been made.

### Next executable milestone

Generate or recover ordered loop-boundary samples for loops 1–10000 and run q=8,16,32 under both fill conventions. Freeze scoring rules before opening the 10001–20000 confirmation range.
