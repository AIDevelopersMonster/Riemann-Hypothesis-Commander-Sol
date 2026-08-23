# RH-SOL-02 · SHIFT — EXP-01

## Full calibration 1–10000 + shift-persistence map

**Status:** executable / calibration not yet complete

## Objective

Measure whether the scalar shifted-lattice count

`C_n(delta) = sum_{k in Z^2} 1_{D_n}(k + delta)`

preserves the RH-SOL-01 Dirichlet-frequency architecture across the translation torus `delta in [0,1)^2`.

The primary map is q=16 under the non-zero winding rule. q=8 and q=32 are resolution controls. Even-odd fill is the predeclared sensitivity rule.

## Frozen spectral score

The scalar score is fixed before the full shift map is viewed:

1. 1000-loop blocks;
2. linear detrending within each block;
3. rFFT power;
4. normalization by median power over loop-frequency `0.01..0.48`;
5. smooth local mapping `f_loop = omega * (dt/dn)/(2*pi)`;
6. block aggregation by mean `log(1 + normalized_power)`;
7. comb targets `omega = log(m)`, `m=2..13`;
8. diagnostic null: independent uniform jitter ±0.2 for every target, default `B=20000`;
9. q x q map multiplicity: Benjamini-Hochberg correction over shift cells.

Implementation: `src/dirichlet_spectrum.py`.

The frozen unshifted scalar baseline is stored in:

- `analysis/exp01_baseline_count_summary.json`
- `analysis/exp01_baseline_count_comb.csv`

## Zero source

Preferred calibration source: LMFDB public Riemann-zeta zero table, indices 1–10001.

Acquisition helper:

```powershell
python scripts\fetch_lmfdb_zeros.py `
  --start 1 `
  --limit 10001 `
  --out data\zeros\lmfdb_zeta_zeros_1_10001.csv
```

The acquisition command prints the source URL and SHA-256 of the raw response. Preserve this output with the experiment notes.

## Chunk generation

Recommended chunking is independent of the mathematics; chunks are merged before spectral analysis. Example 500-loop chunks:

```powershell
python scripts\exp01_build_chunk.py `
  --start 1 --stop 500 `
  --zero-table data\zeros\lmfdb_zeta_zeros_1_10001.csv `
  --out data\derived\rh-sol-02-exp01\chunk_00001_00500.npz
```

Repeat contiguously through loop 10000. The default chunk generator computes q=8,16,32 and both `winding` and `even-odd` from each generated Argand polygon.

## Merge

```powershell
$chunks = Get-ChildItem data\derived\rh-sol-02-exp01\chunk_*.npz | `
  Sort-Object Name | ForEach-Object { $_.FullName }

python scripts\exp01_merge_chunks.py `
  @chunks `
  --out data\derived\rh-sol-02-exp01\calibration_1_10000.npz
```

The merger rejects duplicate loop indices and gaps.

## Primary q=16 shift map

To reproduce the calibration time convention as closely as possible to RH-SOL-01, use the archived `zeta_gaussian_phase_10000.csv` `t_near` values when available:

```powershell
python scripts\exp01_analyze_shift_map.py `
  --dataset data\derived\rh-sol-02-exp01\calibration_1_10000.npz `
  --rule winding `
  --q 16 `
  --legacy-time-csv data\rh-sol-01\zeta_gaussian_phase_10000.csv `
  --B 20000 `
  --out papers\RH-SOL-02-SHIFT\analysis\exp01_shift_map_winding_q16.csv
```

If the legacy time proxy is unavailable, the analyzer can use the zero-pair midpoint, but that run must be labelled separately because it changes both geometry and time proxy relative to RH-SOL-01.

## Required controls

Run the same analyzer for:

- winding q=8;
- winding q=32;
- even-odd q=16;
- optional even-odd q=8/q=32 if discrepancies appear.

## Primary reporting quantities

For q=16 winding report at minimum:

- distribution of comb scores over 256 shifts;
- median/min/max comb score;
- fraction of cells with raw jitter `p < 0.05`;
- fraction surviving BH `q < 0.05`;
- location and score of strongest/weakest shifts;
- comparison with the frozen unshifted baseline `2.0335818528`;
- translation-average geometry diagnostics;
- count and characterization of winding/even-odd disagreements.

## Interpretation rule

- **Persistent:** a substantial region of translation space retains elevated log-integer comb scores and the effect is not localized near a special grid placement.
- **Localized:** only a small exceptional region retains the comb; lattice placement is a material part of the phenomenon.
- **Destroyed:** generic translations remove the comb and the map is consistent with null behavior.

No result from EXP-01 is evidence for RH itself. The experiment tests robustness of information preservation under geometric translation.
