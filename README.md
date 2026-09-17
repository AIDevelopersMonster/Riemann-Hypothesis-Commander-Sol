# Riemann Hypothesis / Commander Sol — frozen research archive

> **PROGRAMME FROZEN — 2026-09-17.** Scientific development in this repository is stopped. `main` is the canonical archival tree. Words such as `active`, `next`, `planned`, `in progress`, or `future work` inside older local files describe the historical state when those files were written; they are not current instructions.

For the authoritative programme state, read **[`PROGRAMME_STATUS_2026-09-17.md`](PROGRAMME_STATUS_2026-09-17.md)**. For the branch-consolidation and preservation record, read **[`PROJECT_FREEZE_2026-09-17.md`](PROJECT_FREEZE_2026-09-17.md)**.

Russian navigation: [`README_RU.md`](README_RU.md).

## What this repository preserves

This is the consolidated archive of the Commander Sol mathematical programme: RH-SOL, Prime-Successor Algebra and related prime-structure work, FCOA, HATTER-SOL, and the Alice/Ruler line. The freeze preserved theorem layers, research checkpoints, manuscripts, release metadata, reproducibility material, experiments, and relevant Git ancestry in `main`.

The repository is not itself a claim that every preserved theorem candidate, experiment, roadmap, or future-work note is proved or published. Publication status is determined by explicit DOI/release evidence; mathematical status remains the status stated in the corresponding audited theorem/manuscript layer.

## Canonical directions

| Direction | Freeze state | Main archive location |
|---|---|---|
| RH-SOL | **FROZEN** | `programme/`, `papers/RH-SOL-*` |
| PRIME-SUCCESSOR | **FROZEN** | `papers/PRIME-*` and related release material |
| FCOA | **FROZEN** | `papers/FCOA-*`, delegated/release material |
| HATTER-SOL | **FROZEN** | `papers/HATTER-SOL/` |
| ALICE-RULER | **FROZEN** | `alice-ruler-incidence/`, `alice-ruler-edit-rigidity/` |

Detailed per-line status: [`PROGRAMME_STATUS_2026-09-17.md`](PROGRAMME_STATUS_2026-09-17.md).

## Publication records already explicit in the canonical tree

This short table is navigation, not a substitute for release metadata. Only records whose DOI/title is explicit in the consolidated tree are listed here.

| Line | Publication | DOI |
|---|---|---|
| RH-SOL-01 · LATTICE | *Integer-Lattice Encoding of Riemann-Zeta Argand Loops: Persistence of Dirichlet Frequencies under Binary Geometric Quantization* | `10.5281/zenodo.22060296` |
| Alice Ruler II | *Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects* | `10.5281/zenodo.22722951` |
| Alice Ruler III | *From Local Fano Phase to Partial Projective Geometry: Sharp Obstructions and Rank-2 Boolean Fiberization* | `10.5281/zenodo.22737943` |
| FCOA · Admissibility Geometry | *Reflections on Admissibility Geometry with Commander Sol: How a Partial Operation Remembers an Oriented Carrier* | `10.5281/zenodo.22129787` |
| FCOA · Value-Rigidity / Identity Digraphs | *Reflections on Value-Rigidity with Commander Sol: Two Anonymous Outputs, Identity Digraphs, and Sparse Rigid Fibers* | `10.5281/zenodo.22160014` |
| FCOA-Z · Ray to Axis | *Reflections on How a Ray Becomes an Axis: And why old operations reveal new local laws after a second direction appears* | `10.5281/zenodo.22171473` |
| HATTER-SOL-01 | *A Tea Party in the Additive-Multiplicative World with Hatter Sol: The Number Line, the Observer, and Two Operations* | `10.5281/zenodo.22639237` |
| HATTER-SOL-02 | *Two Teapots, One Cup: “Who Are You?” Among the Primes* | `10.5281/zenodo.22656414` |
| HATTER-SOL-07 | *Alice in the Land of Free Threads: Factors as Nodes and the Exact Cost of Multiplicative Splitting* | `10.5281/zenodo.22724185` |
| HATTER-SOL-10 | *Ideal Factor Networks Beyond Unique Element Factorization* | `10.5281/zenodo.22734865` |

A DOI appearing in a historical candidate file does not by itself change the freeze status unless the canonical release/publication evidence supports it.

## RH-SOL at freeze

The old programme map is retained as intellectual history, but its former `Active` and `Planned` labels are no longer operational. At freeze: RH-SOL-01 was published; RH-SOL-02/03/04 had research completed without final publication synthesis; RH-SOL-05/06 were unfinished; RH-SOL-07..15 remained seeds/planned directions. See [`programme/SERIES_MAP.md`](programme/SERIES_MAP.md).

## HATTER-SOL at freeze

The numbered HATTER-SOL folders are archival programme units, not active branches. Material through HATTER-SOL-18 is preserved in `main`. HATTER-SOL-17 was unfinished at freeze; HATTER-SOL-18 is a future-work seed. Do not infer publication from a folder number alone.

## Historical files

Local `STATUS.md`, `RESEARCH_TZ.md`, `DIALOGUE_TZ.md`, `PUBLICATION_CANDIDATE.md`, roadmaps and older READMEs are intentionally preserved. They document how the programme evolved. When they conflict with current navigation, use this precedence:

1. explicit canonical DOI/publication record;
2. canonical release metadata and manifests;
3. [`PROGRAMME_STATUS_2026-09-17.md`](PROGRAMME_STATUS_2026-09-17.md);
4. local historical status files for chronology only.

## Repository layout

```text
programme/                 RH-SOL programme history and frozen series map
papers/                    mathematical programme and publication material
alice-ruler-incidence/     Alice/Ruler II archive
alice-ruler-edit-rigidity/ Alice/Ruler III and continuation archive
experiments/               preserved computational experiments
demos/                     preserved demonstrations
reviews/                   audit/review material
releases/                  release and Zenodo metadata
scripts/                   reproducibility and utility scripts
```

## Restart rule

If the programme is ever reactivated, begin from `main`, `PROGRAMME_STATUS_2026-09-17.md`, and `PROJECT_FREEZE_2026-09-17.md`. Do not resume from an old branch name or interpret an old `next step` as automatically current.

## Attribution

Author / programme owner: **Alex Malachevsky** · ORCID **0009-0008-6009-3196**. Commander Sol was used as an AI research collaborator for hypothesis generation, computational design, falsification planning, code assistance, literature triage, auditing, and manuscript drafting. Mathematical claims remain subject to their explicit proof/computational status.