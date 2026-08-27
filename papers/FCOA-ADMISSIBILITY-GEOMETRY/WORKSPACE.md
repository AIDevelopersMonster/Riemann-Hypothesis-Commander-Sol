# FCOA Admissibility Geometry — workspace boundary

This file defines the maintenance boundary for this publication companion.

## Owned paths for this line of work

Only the following paths belong to the FCOA Admissibility Geometry publication companion:

- `papers/FCOA-ADMISSIBILITY-GEOMETRY/**`
- `demos/fcoa-domain-compilation/**`
- `experiments/fcoa-domain-compilation/**`

These paths may be updated when continuing this publication line.

## Paths explicitly outside this workspace

Do **not** modify other mathematical branches unless the user explicitly asks for that branch. In particular, this workspace does not own:

- `papers/PRIME-SUCCESSOR-*`
- `papers/RH-SOL-*`
- other directories under `papers/`
- other directories under `demos/`
- other directories under `experiments/`
- `programme/**`, `src/**`, `data/**`, `reviews/**`, or unrelated release folders

The repository contains other active research conversations and publication lines. Their files may be maintained by other concurrent work with Commander Sol and must be treated as independent.

## Root-file rule

Do not change root-level repository files (`README.md`, `README_RU.md`, `CITATION.cff`, `MANIFEST.md`, etc.) as part of routine FCOA maintenance. Root files should be edited only when the user explicitly asks for a repository-wide index/update.

The FCOA publication is already discoverable through its own folder and DOI. No further repository-wide edits are required for normal continuation.

## Canonical publication

Zenodo DOI:

**10.5281/zenodo.22129787**

Persistent URL:

https://doi.org/10.5281/zenodo.22129787

Zenodo is the canonical archival publication record. GitHub is the theorem/reproducibility/demonstration companion.

## Current frozen research chain

The published research chain is:

\[
M0\longrightarrow G1\longrightarrow G2.
\]

- **M0** — sparse baseline; generic multiplication symmetry \(S_{N-1}\).
- **G1** — external path/admissibility relation; external rigidity only.
- **G2** — directed adjacency compiled into partial-operation definedness using a single terminal output \(\Omega\); internal recoverable memory.

The audited G2 formulas are recorded in `MATHEMATICAL_CORE.md`.

## Continuation rule

Do not silently extend the published branch with G3 or new operation cells. A new rule is a new research branch/checkpoint and should be created only after an explicit research decision.

When continuing this work:

1. read `README.md`;
2. read `WORKSPACE.md`;
3. read `STATE.md`;
4. read `MATHEMATICAL_CORE.md`;
5. run/inspect `../../experiments/fcoa-domain-compilation/verify_formulas.py` if formulas are touched;
6. keep publication DOI metadata consistent in `release/`;
7. do not modify neighboring research branches.

## Claim discipline

Keep the following distinctions explicit:

- operation values vs operation definedness;
- external rigidity vs internal memory;
- role distinguishability vs structural rigidity;
- finite contextual recovery vs uniform directed-adjacency recovery vs uniform full-order recovery;
- typed Domain Compilation theorem vs one-sorted variants with extra hypotheses.

The terms FCOA, boundary-mediated order memory, external rigidity/internal memory, and domain compilation are working research terminology; do not turn them into priority claims without a dedicated prior-art audit.
