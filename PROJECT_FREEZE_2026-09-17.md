# Commander Sol project freeze — 2026-09-17

Status: **FROZEN / archival consolidation in progress**.

This repository is being frozen conservatively. The objective is to make `main` the canonical archival entry point without losing unique theorem layers, research status, publication metadata, reproducibility scripts, certificates, or the ancestry of completed work.

## Freeze rules

1. No branch is to be deleted merely because its name looks obsolete.
2. A branch may be retired only after its unique content is present in `main` **and** its relevant history is reachable from `main`, or after an explicit archival salvage records the material that must survive.
3. Merge commits are preferred for freeze integration because they preserve branch ancestry.
4. Unfinished branches are archived with their current `STATUS`/`RESEARCH_TZ`; archival inclusion does not upgrade conjectures, open obligations, experiments, or seeds into proved results.
5. Historical branches that conflict with a newer canonical layer must not be wholesale-merged. They require path-level salvage.
6. Project is now scientifically frozen: no new theorem layers, experiments, HATTER, FCOA or RH-SOL research branches are to be started during archival consolidation.

## Integrated during freeze

- HATTER-SOL 11–15 cumulative research chain (PR #19).
- HATTER-SOL-13 late closure/README corrections (PR #20).
- HATTER-SOL-14 late Hecke/Zenodo publication tail (PR #21).
- HATTER-SOL-16 nonsolvable-ports package (PR #22).
- HATTER-SOL-17 current hardware research state, explicitly including unfinished status (PR #23).
- HATTER-SOL-18 future-work seed (PR #24).
- Alice Ruler III / edit-rigidity current state (PR #25).
- Alice Ruler II / incidence late publication and QA tail (PR #26).
- FCOA nesting atomicity research/publication package (PR #28).
- RH-SOL-04/05 experimental chain and reproducibility scripts (PR #30).
- PRIME-SUCCESSOR operator meta experiments (PR #31).
- PRIME-SUCCESSOR finite-subset carrier-wall late research layers (PR #32).
- PRIME-SUCCESSOR threshold-spectrum-rigidity proof/audit package (PR #34).

The earlier canonical FCOA PR #13 salvage is already in `main` through PR #18.

## Recovery checkpoint

`archive/freeze-2026-09-17-pre-final` records the canonical `main` state before the final retirement/salvage pass.

## Historical branches already subsumed by later ancestry

The HATTER-SOL cumulative chain makes several intermediate heads historically redundant once branch deletion is performed: `tmp-never-use`, the HATTER-SOL-11 orbital-port branch, and the HATTER-SOL-12 observer-world branch are ancestors of the integrated HATTER-SOL-15 chain. HATTER-SOL-13 and HATTER-SOL-14 had late divergent corrections; those tails were separately integrated before retirement.

Likewise, intermediate RH-SOL agent branches that are ancestors of the integrated RH-SOL-05 chain may be retired after final ancestry verification.

## Branches deliberately NOT wholesale-merged

The following freeze PRs were audited and closed without merge because a direct merge would mix historical state with newer canonical material:

- PR #27 — `director/fcoa-z-symmetric-line`.
- PR #29 — `director/fcoa-hybrid-memory`.
- PR #33 — `research/stationary-locality`.
- PR #35 — `director/fcoa-selector`.

These branches must remain until path-level archival salvage is complete. In particular, the hybrid-memory line overlaps the canonical PR #13 salvage; the selector and Z-symmetric lines contain large historical/applied trees whose root README state conflicts with current `main`; stationary-locality contains a self-contained publication package plus an RH-SOL-06 analysis note but no longer merges cleanly after later integrations.

## Remaining retirement gate

Audit every still-ahead branch against the current `main`. Priority salvage families include the four conflict sources above, remaining FCOA director/research heads, PRIME-SUCCESSOR research/publication tails, and any other branch for which `main...branch` still reports `ahead_by > 0`.

A branch with `ahead_by = 0` after this consolidation is safe to retire from the content/history perspective. A branch with `ahead_by > 0` is **not** safe to delete until its unique commits are merged or explicitly salvaged.

## Canonical restart point

If the programme is ever resumed, start from `main` and this freeze ledger. Do not resume from an old research branch without first comparing it against the then-current `main` and reading the branch-local `STATUS`, `RESEARCH_TZ`, publication audit, and theorem dependency records.
