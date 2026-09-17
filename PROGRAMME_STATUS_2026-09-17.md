# Commander Sol Programme Status — 2026-09-17

**Canonical status:** FROZEN.

This file is the authoritative navigation/status layer for the repository at the freeze date. Older `STATUS.md`, `README.md`, `RESEARCH_TZ.md`, branch plans, publication candidates and roadmaps are preserved as historical records of the state at the time they were written. They may contain words such as `active`, `planned`, `next`, `in progress`, `future work` or `publication pending`; those words are **not current programme instructions after 2026-09-17**.

For repository-freeze mechanics and branch ancestry preservation, see [`PROJECT_FREEZE_2026-09-17.md`](PROJECT_FREEZE_2026-09-17.md).

## Status vocabulary

- **PUBLISHED** — a publication record/DOI was completed before the freeze.
- **RESEARCH COMPLETE / UNPUBLISHED AT FREEZE** — the research line reached its internal completion threshold, but publication synthesis/deposit was not completed before the freeze.
- **PARTIAL / UNFINISHED AT FREEZE** — substantive material exists, but the line was not completed.
- **SEED / PLANNED ONLY AT FREEZE** — a research direction was recorded, but no completed programme result is asserted.
- **FROZEN** — no continuation is currently authorized; preserved material remains archival.

## Programme-level map

| Direction | State at freeze | Canonical location | Notes |
|---|---|---|---|
| RH-SOL | **FROZEN** | `programme/`, `papers/RH-SOL-*` | RH-SOL-01 published; RH-SOL-02/03/04 research complete but manuscript synthesis not completed; RH-SOL-05 preserved as unfinished research; RH-SOL-06 contains partial exploratory material; RH-SOL-07..15 remain recorded future directions only. |
| PRIME-SUCCESSOR | **FROZEN** | `papers/PRIME-*`, related root/release metadata | Contains published, theorem-complete and unfinished lines. Local historical status files remain evidence, not current instructions. |
| FCOA | **FROZEN** | `papers/FCOA-*`, `delegated/FCOA_*`, `releases/` | Multiple publication and theorem layers were completed; remaining research directions are archival only. |
| HATTER-SOL | **FROZEN** | `papers/HATTER-SOL/` | HATTER-SOL 01–18 material is preserved in `main`; published and research-only items must be distinguished by their local publication metadata. HATTER-SOL-17 was unfinished at freeze; HATTER-SOL-18 is a future-work seed. |
| ALICE-RULER | **FROZEN** | `alice-ruler-incidence/`, `alice-ruler-edit-rigidity/` | Alice Ruler II and III publication material is preserved; no continuation is active. |

## RH-SOL status at freeze

| ID | Label | Freeze status |
|---|---|---|
| RH-SOL-01 | LATTICE | **PUBLISHED** — DOI `10.5281/zenodo.22060296` |
| RH-SOL-02 | SHIFT | **RESEARCH COMPLETE / UNPUBLISHED AT FREEZE** |
| RH-SOL-03 | REALZERO | **RESEARCH COMPLETE / UNPUBLISHED AT FREEZE** |
| RH-SOL-04 | FIREWALL | **RESEARCH COMPLETE / UNPUBLISHED AT FREEZE** |
| RH-SOL-05 | POISSON | **PARTIAL / UNFINISHED AT FREEZE** — preserved experiments and reproducibility scripts; no longer active |
| RH-SOL-06 | NYQUIST | **PARTIAL / UNFINISHED AT FREEZE** — exploratory analysis exists; manuscript/release layers were not completed |
| RH-SOL-07 | SURVIVAL | **SEED / PLANNED ONLY AT FREEZE** |
| RH-SOL-08 | RATE | **SEED / PLANNED ONLY AT FREEZE** |
| RH-SOL-09 | DECODE | **SEED / PLANNED ONLY AT FREEZE** |
| RH-SOL-10 | MINCODE | **SEED / PLANNED ONLY AT FREEZE** |
| RH-SOL-11 | LFUNCTIONS | **SEED / PLANNED ONLY AT FREEZE** |
| RH-SOL-12 | PRIMESET | **SEED / PLANNED ONLY AT FREEZE** |
| RH-SOL-13 | ENVELOPE | **SEED / PLANNED ONLY AT FREEZE** |
| RH-SOL-14 | RESIDUAL | **SEED / PLANNED ONLY AT FREEZE** |
| RH-SOL-15 | SYNTHESIS | **SEED / PLANNED ONLY AT FREEZE** |

## HATTER-SOL freeze note

The numbered folders are historical programme units, not active branches. HATTER-SOL 11–15 were consolidated into `main` from the cumulative research chain; late HATTER-SOL-13 and HATTER-SOL-14 corrections were separately preserved. HATTER-SOL-16 material was integrated before freeze. HATTER-SOL-17 is preserved at its unfinished hardware/research state. HATTER-SOL-18 is preserved as a future-work seed and must not be read as a completed article.

## Publication status precedence

Publication state must be read from, in this order:

1. an explicit DOI/publication record in the canonical `main` tree;
2. release metadata (`ZENODO_METADATA`, `CITATION.cff`, release manifest, DOI record);
3. this programme-status file;
4. historical local `STATUS`/`README` material only for reconstruction of the research timeline.

A historical line saying `planned`, `active`, `next`, `ready for deposit`, or `DOI pending` does not override a later publication record or the programme freeze.

## Restart rule

If the programme is ever reactivated, start from `main`, this file, and `PROJECT_FREEZE_2026-09-17.md`. Do not restart from an old branch name or from a historical `STATUS.md` without first reconciling it against the canonical publication index and current `main`.
