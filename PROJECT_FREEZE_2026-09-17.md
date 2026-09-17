# Commander Sol project freeze — 2026-09-17

Status: **FROZEN / conservative archival mode**.

This repository is being frozen conservatively. `main` is the canonical archival entry point. No unfinished research is promoted to a proved result by archival inclusion.

## Freeze rules

1. Never delete a branch because its name looks obsolete.
2. Retire a branch only when its unique content/history is reachable from `main`, or when an explicit archival salvage preserves what must survive.
3. Prefer merge commits for clean freeze integrations so branch ancestry remains reachable.
4. Preserve `STATUS`, `RESEARCH_TZ`, audits, manuscripts, publication metadata, scripts and certificates for unfinished work.
5. Never wholesale-merge a historical branch that conflicts with a newer canonical layer; use path-level salvage instead.

## Integrated during freeze

- PR #19 — HATTER-SOL 11–15 cumulative chain.
- PR #20 — HATTER-SOL-13 late corrections.
- PR #21 — HATTER-SOL-14 publication tail.
- PR #22 — HATTER-SOL-16.
- PR #23 — HATTER-SOL-17 current state.
- PR #24 — HATTER-SOL-18 research seed.
- PR #25 — Alice Ruler III current state.
- PR #26 — Alice Ruler II publication/QA tail.
- PR #28 — FCOA nesting atomicity.
- PR #30 — RH-SOL-04/05 firewall/Poisson experimental chain and reproducibility scripts.
- PR #31 — PRIME-SUCCESSOR-OPERATOR meta experiments.
- PR #32 — finite-subset carrier-wall remaining theorem/research layers.
- PR #34 — threshold-spectrum-rigidity proof/audit package.

The earlier canonical FCOA PR #13 salvage is present through PR #18.

## Safety checkpoints

Before the second consolidation pass, `archive/freeze-2026-09-17-pre-final` was created from the then-current `main` as a recovery point. `archive/freeze-2026-09-17-prime-salvage` is an additional checkpoint from the same consolidation era.

## Subsumed HATTER history

The cumulative HATTER chain makes intermediate HATTER-11/HATTER-12 heads and `tmp-never-use` redundant from a content/history perspective. HATTER-13 and HATTER-14 had late divergent corrections, so their tails were separately integrated before retirement.

## Deliberately NOT wholesale-merged

The following freeze PRs were closed without merge because current canonical `main` and the historical branch conflict or overlap in ways that make a wholesale merge unsafe:

- PR #27 — `director/fcoa-z-symmetric-line`.
- PR #29 — `director/fcoa-hybrid-memory`.
- PR #33 — `research/stationary-locality`.
- PR #35 — `director/fcoa-selector`.

These branches are **archival sources and must not be deleted yet**. FCOA selector contains substantial unique `delegated/FCOA_SELECTOR` and accumulated Z-symmetric material; hybrid-memory overlaps the canonical PR #13 salvage; stationary-locality contains a unique theorem/manuscript/release package but no longer merges cleanly after later integrations.

## Remaining retirement gate

Branch deletion is intentionally deferred until every remaining branch has been re-compared with the final `main`. Cleanly integrated branches should report no unique commits relative to `main`; conflicting archival-source branches above are exceptions and must remain until path-level salvage is completed.

The project is scientifically frozen: do not start new theorem layers, experiments, HATTER numbers, FCOA modules, or RH-SOL branches during this freeze. The only permitted repository work is archival consolidation, provenance repair, metadata correction, or later explicit reactivation.

## Canonical restart point

If the programme is resumed, start from `main` and this ledger. Do not resume directly from an old research branch without comparing it against the then-current `main` and reading its branch-local status/audit records.
