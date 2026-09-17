# Commander Sol project freeze — 2026-09-17

Status: **FROZEN / archival consolidation in progress**.

This repository is being frozen conservatively. `main` is the canonical archival entry point. The freeze preserves theorem layers, research status, publication metadata, reproducibility material and historical commit ancestry without allowing older branch trees to overwrite newer canonical state.

## Freeze rules

1. No branch is retired merely because its name looks obsolete.
2. A branch is retirement-safe only after `main...branch` reports `ahead_by = 0` or an explicit archival ancestry/salvage operation has made its head reachable from `main`.
3. Merge commits are preferred because they preserve ancestry.
4. Unfinished `STATUS` / `RESEARCH_TZ` material remains unfinished; archival inclusion does not promote conjectures, experiments or future-work seeds to theorems.
5. Conflicting historical branches are not wholesale-applied over newer canonical files. Where necessary, a topology-only merge records the historical head as a parent while leaving the `main` tree unchanged.
6. Scientific work is frozen: no new theorem layers, experiments, HATTER numbers, FCOA modules or RH-SOL branches during archival consolidation.

## Content integrated during freeze

- PR #19 — HATTER-SOL 11–15 cumulative chain.
- PR #20 — HATTER-SOL-13 late closure/README corrections.
- PR #21 — HATTER-SOL-14 Hecke/Zenodo publication tail.
- PR #22 — HATTER-SOL-16 nonsolvable-ports package.
- PR #23 — HATTER-SOL-17 current hardware state, including unfinished STATUS.
- PR #24 — HATTER-SOL-18 future-work seed.
- PR #25 — Alice Ruler III / edit-rigidity current state.
- PR #26 — Alice Ruler II / incidence late publication and QA tail.
- PR #28 — FCOA nesting atomicity package.
- PR #30 — RH-SOL-04/05 experimental chain and reproducibility scripts.
- PR #31 — PRIME-SUCCESSOR operator meta experiments.
- PR #32 — finite-subset carrier-wall late research layers.
- PR #34 — threshold-spectrum-rigidity proof/audit package.

The canonical FCOA PR #13 salvage was already integrated through PR #18.

## Conflict branches archived by ancestry

Direct historical merges were rejected where they would mix obsolete tree state with newer canonical material. Their complete commit histories are now made reachable from `main` through zero-diff topology-only merge commits:

- `research/stationary-locality` — source head `777b4d378e4dace0d5c7eda677f63caea02cde94`; direct content attempt PR #36 was rejected after showing 427 deletions; clean ancestry PR #37 merged. Post-merge verification: `ahead_by = 0`.
- `director/fcoa-selector` — source head `4de03fa7982fb8ed06003465b40d359ec9e30716`; historical direct PR #35 was not merged; clean ancestry PR #38 merged with 0 changed files. Post-merge verification: `ahead_by = 0`.
- `director/fcoa-z-symmetric-line` — source head `9e1d646f5a2dd1f4fee992e9a2410979485a314d`; historical direct PR #27 was not merged; clean ancestry PR #39 merged with 0 changed files. Post-merge verification: `ahead_by = 0`.
- `director/fcoa-hybrid-memory` — source head `963edac456faf1b930441c65c55616b31ba96130`; historical direct PR #29 was not merged because it overlaps newer canonical PR #13/#18 material; clean ancestry PR #40 merged with 0 changed files. Post-merge verification: `ahead_by = 0`.

These four original branch heads are now retirement-safe from the history-preservation perspective. Their old trees remain recoverable through Git history, while the current `main` tree remains authoritative.

## Recovery checkpoints

- `archive/freeze-2026-09-17-pre-final` — checkpoint before the final retirement/salvage pass.
- Additional temporary `archive/freeze-*` branches were created solely to carry ancestry merge commits. Once the final branch audit is complete and the corresponding commits are confirmed reachable from `main`, these temporary carrier branches are themselves retirement-safe.

## Historical lines already subsumed

The cumulative HATTER-SOL chain subsumes several intermediate HATTER heads, including the old `tmp-never-use` lineage and intermediate HATTER-SOL-11/12 work. HATTER-SOL-13 and HATTER-SOL-14 divergent late tails were separately integrated before retirement.

The integrated RH-SOL-05 chain is expected to subsume earlier RH-SOL agent heads; each must still pass the final `ahead_by = 0` verification before deletion.

## Remaining retirement gate

The final pass must compare every remaining branch against current `main`, especially remaining FCOA director/research heads and PRIME-SUCCESSOR research/publication branches. Any branch with `ahead_by > 0` remains protected until merged or archived by ancestry. Any branch with `ahead_by = 0` is safe to delete from the content/history perspective, except the intentionally retained recovery checkpoint.

## Canonical restart point

If the programme is ever resumed, start from `main` and this ledger. Do not resume from an old research branch without first comparing it with the then-current `main` and reading its branch-local `STATUS`, `RESEARCH_TZ`, publication audit and theorem-dependency records.
