# Commander Sol project freeze — 2026-09-17

Status: **FROZEN / final branch retirement audit in progress**.

`main` is the canonical archival entry point. Scientific development is stopped. This freeze preserves theorem layers, research status, publication metadata, reproducibility material, release artifacts and historical commit ancestry without allowing obsolete branch trees to overwrite newer canonical state.

## Freeze rules

1. No branch is retired merely because its name looks obsolete.
2. Retirement requires `main...branch` to report `ahead_by = 0`, or an explicit archival operation that makes the branch head reachable from `main`.
3. Clean content/release tails are physically merged. Conflicting historical lines are preserved by zero-diff ancestry merges.
4. Archival inclusion never promotes conjectures, experiments, incomplete STATUS material or future-work seeds to proved results.
5. No new HATTER, FCOA, RH-SOL or PRIME-SUCCESSOR research is started during the freeze.

## Content integrated during freeze

PRs #19–26 and #28 integrated the HATTER-SOL 11–18, Alice Ruler II/III and FCOA nesting-atomicity packages. PR #30 integrated RH-SOL-04/05. PR #31 integrated PRIME-SUCCESSOR operator meta experiments. PR #32 integrated finite-subset carrier-wall. PR #34 integrated threshold-spectrum-rigidity. The canonical FCOA PR #13 salvage was already integrated through PR #18.

Final publication/research pass:

- PR #41 — `paper/exact-zero-one-boundary-v1`: publication README/history physically integrated.
- PR #42 — `director/fcoa-rigidity-cost`: remaining FCOA-LQR-SYNCHRONIZATION RC1 release commit, including binary DOCX/PDF/ZIP artifacts, checksums and metadata, physically integrated.
- PR #43 — `research/fcoa-lqr-prestabilization`: 21-commit QGE3 prestabilization research line and verification scripts physically integrated.
- PR #45 — `research/fixed-ball-interior`: divergent research ancestry preserved with a zero-diff merge after direct PR #44 was rejected as conflicting.
- PR #46 — `paper/fixed-ball-v1.1`: later fixed-ball v1.1 publication state physically integrated and authoritative for its publication files.
- PR #48 — `research/prime-status-corridor`: 15-commit historical research/publication line preserved by zero-diff ancestry after direct PR #47 remained nonmergeable. The separate `paper/prime-status-corridor-v1.0` head is already an ancestor of main.
- PR #49 — `paper/support-cardinality-v1.1`: review response, release candidate and proof-audit publication tail physically integrated.

## Conflict branches archived by ancestry

- `research/stationary-locality` — source head `777b4d378e4dace0d5c7eda677f63caea02cde94`; dangerous direct content attempt rejected; ancestry preserved by PR #37.
- `director/fcoa-selector` — source head `4de03fa7982fb8ed06003465b40d359ec9e30716`; ancestry PR #38.
- `director/fcoa-z-symmetric-line` — source head `9e1d646f5a2dd1f4fee992e9a2410979485a314d`; ancestry PR #39.
- `director/fcoa-hybrid-memory` — source head `963edac456faf1b930441c65c55616b31ba96130`; ancestry PR #40.
- `research/fixed-ball-interior` — source head `d01ffe97ccecad10c4cf489d0555a94c9d58fbde`; ancestry PR #45.
- `research/prime-status-corridor` — source head `95e311bb01c0048585aa85c8b123aa2c3a6e7edc`; ancestry PR #48.

All of these lines remain recoverable from `main` history while the canonical tree remains authoritative.

## Verified retirement-safe branches in this pass

The following were explicitly checked against current `main` and returned `ahead_by = 0`:

- `agent/prime-successor-operator-meta`
- `agent/rh-sol-02-shift`
- `agent/rh-sol-03-realzero`
- `agent/rh-sol-04-firewall`
- `agent/rh-sol-05-poisson`
- `director/fcoa-nesting-atomicity`
- `paper/prime-status-corridor-v1.0`
- `paper/prime-successor-algebra`
- `paper/prime-successor-operator`
- `research/alice-ruler-edit-rigidity`
- `research/alice-ruler-incidence`
- `research/finite-subset-carrier-wall`
- `research/hatter-sol-dimensional-factor-morphisms`
- `research/hatter-sol-free-ports`
- `research/hatter-sol-ideal-factor-networks`
- `research/hatter-sol-world-interface-operators`
- `research/threshold-spectrum-rigidity`
- `tmp-never-use`

The newly integrated/ancestry-preserved heads listed above are also intended for retirement after the final mechanical verification sweep.

## Recovery branches

`archive/freeze-2026-09-17-pre-final` is the intentional pre-final recovery checkpoint. Temporary `archive/freeze-*` ancestry carrier branches exist only to transport topology-only merge commits; once their commits are reachable from `main`, they are themselves disposable. `archive/freeze-2026-09-17-prime-salvage` remains a recovery checkpoint until branch cleanup is completed.

## Canonical restart point

If the programme is ever reactivated, begin from `main` and this ledger. Do not resume an old research branch directly. First compare it with the then-current `main`, then read its STATUS/RESEARCH_TZ, publication audit and theorem dependency records. The freeze itself does not authorize new mathematical claims.