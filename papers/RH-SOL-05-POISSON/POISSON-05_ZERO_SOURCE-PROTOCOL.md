# RH-SOL-05 · POISSON-05 zero-source protocol

Status: frozen operational protocol **before acquisition of any zero with index > 40001**.

This document does not alter the mathematical preregistration in `POISSON-05_AMPLITUDE_70_30_OOS-PREREGISTRATION.md`. It fixes the external-data acquisition and validation procedure so that fresh-loop analysis cannot depend on post-acquisition source choices.

## Primary source

Use the official LMFDB Riemann-zeta-zero plain-text route:

`https://www.lmfdb.org/zeros/zeta/list?N=40001&limit=20001&format=plain&download=yes`

The expected response contains exactly 20,001 rows of the form

`index ordinate`

covering indices `40001..60001` inclusive.

The LMFDB application route itself allows up to 100,000 zeros in one request and emits the plain representation directly from the verified zeta-zero database.

## Why this source is frozen

The existing RH-SOL zero tables through index 40001 are LMFDB-derived. POISSON-05 therefore retains the same data family and avoids introducing a precision/source change at the OOS boundary.

No lower-precision fallback table is permitted for the primary POISSON-05 run.

If LMFDB acquisition fails, the run stops. It does not silently switch to Odlyzko or locally recomputed zeros.

## Required validation

Before any loop `40001..60000` is constructed, the acquisition script must verify:

1. row count exactly `20001`;
2. first index exactly `40001`;
3. final index exactly `60001`;
4. indices strictly contiguous with unit increment;
5. ordinates finite, positive, and strictly increasing;
6. overlap index `40001` agrees with the existing table `data/zeros/lmfdb_zeta_zeros_20001_40001.csv` to absolute tolerance `1e-27`;
7. SHA-256 of the raw LMFDB response is recorded;
8. SHA-256 of the normalized CSV is recorded.

Any failure aborts before tensor construction.

## Normalized output

Write

`data/zeros/lmfdb_zeta_zeros_40001_60001.csv`

with schema

`n,gamma`

and a provenance manifest

`data/zeros/lmfdb_zeta_zeros_40001_60001.manifest.json`.

The manifest records source URL, acquisition UTC timestamp, row count, first/last index, first/last ordinate strings, overlap delta, and both SHA-256 digests.

## Scientific guardrail

Source acquisition is operational, not inferential. No zero ordinate beyond 40001 may be inspected to choose or modify the frozen 70/30 boundary, target set, jitter width, seed, or success criterion.
