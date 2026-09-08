# FCOA Branch Passport Laboratory — Closure Record

**Branch:** `director/fcoa-branch-passport-lab`  
**Closed:** 2026-08-29  
**Status:** **READY FOR ARCHIVAL CLOSURE**  
**Published mathematical successor:** Zenodo DOI `10.5281/zenodo.22160014`

## 1. Closure decision

The branch has completed its scientific purpose. No theorem-level question remains open inside the branch scope. The mathematical line that emerged from the audit work has been transferred to `main`, publication materials have been frozen, and the final result is published on Zenodo.

The branch should now be retained only as provenance for the audit/discovery path. It should not receive new mathematics or new tooling features.

## 2. File-by-file disposition

| File | Final disposition | Notes |
|---|---|---|
| `ROLE_AND_PROMPT.md` | ARCHIVAL / CLOSED | Governance frozen; reopening rule added. |
| `SOURCE_CONTEXT.md` | ARCHIVAL / UPDATED | Historical source chain separated from current publication boundary. |
| `PASSPORT_SCHEMA.md` | FROZEN METHOD SPEC | Reusable schema; no further implementation obligation. |
| `AUTOMATION_PLAN.md` | PARTIALLY IMPLEMENTED / DEFERRED | General serialization/diff tooling explicitly non-blocking. |
| `BRANCH_DIFFS.md` | FROZEN BENCHMARK REGISTER | M0/G1/G2/G3/G4 transition evidence retained. |
| `AUDIT_FINDINGS.md` | FINAL / RECONCILED | No theorem-level `OPEN` finding remains. |
| `ENUMERATION_REPORT_P1.md` | HISTORICAL EVIDENCE SNAPSHOT | Its contemporary `WORKING` wording is superseded by this closure record. |
| `TRANSLATION_ORBIT_AUDIT_P2.md` | HISTORICAL AUDIT SNAPSHOT | G4 scope issue subsequently superseded by P3-P5 pure constructions. |
| `PURE_TWO_OUTPUT_AMPLIFICATION_P3.md` | PROVED / PUBLISHED LINEAGE | Correct result; later strengthened by P5. |
| `ONE_OUTPUT_OBSTRUCTION_P4.md` | PROVED / PUBLISHED LINEAGE | Pure terminal-output scope retained. |
| `TWO_OUTPUT_EXTREMALITY_P5.md` | PROVED / PUBLISHED LINEAGE | Establishes maximal active-sort `VRI=n!`. |
| `SPARSE_RIGID_FIBER_P6.md` | PROVENANCE / CLASSICAL REDISCOVERY | `Theta(n/log n)` result later identified with classical identity-digraph extremal and strengthened on `main`. |
| `UPSTREAM_MEMO.md` | FINAL HANDOFF | Supersedes intermediate P4 memo and records publication transfer. |
| `passport_enumerator.py` | RETAINED EXECUTABLE EVIDENCE | Independent small-case automorphism checker; no formula substitution. |
| `CLOSURE.md` | FINAL INDEX | This file. |

## 3. Mathematical results transferred out of the branch

The following are no longer branch-local working claims. They belong to the published theorem package:

1. **One-Output Collapse**
   
   `|O|=1 => VRI=1`
   
   in the pure terminal-output active-sort setting.

2. **Two-Output Maximum VRI**
   
   exactly two anonymous terminal outputs can attain
   
   `VRI=n!`.

3. **Sparse rigid fiber / identity-digraph bridge**
   
   the minimum special fiber for maximal two-output value-rigidity is the minimum-size identity-digraph extremal `m(n)`.

4. **Exact finite structure**
   
   `m(n)` is evaluated by the threshold over cumulative identity oriented-tree counts.

5. **Asymptotic refinement**
   
   `n-m(n)=L n/[log n+(3/2)log log n+O(1)]`.

6. **Phase law**
   
   the bounded denominator term has a nontrivial partial-layer oscillation rather than a universal constant.

Canonical source: DOI `10.5281/zenodo.22160014` and `papers/FCOA-VALUE-RIGIDITY-IDENTITY-DIGRAPHS/` on `main`.

## 4. Prior-art reconciliation

The branch does **not** claim discovery of identity/asymmetric digraphs, minimum-size identity digraphs, identity oriented trees, distinguishing colorings, or the classical `Theta(n/log n)` scale. P6 is retained as an independent derivation that led the programme to the correct classical connection.

The published paper explicitly separates classical graph-theoretic material from the FCOA value-rigidity translation and its internally derived refinements.

## 5. Infrastructure deferred without blocking closure

The following ideas are intentionally left for a possible future tooling project:

- machine-readable universal passport serialization;
- generalized executable Carrier-Erasure and Value-Erasure predicates;
- universal automatic diff generation for arbitrary branches.

They are not unfinished scientific obligations of this branch.

## 6. Closure checklist

- [x] P0-P2 audit findings reconciled.
- [x] G4 bounded-output scope corrected.
- [x] Pure globally bounded two-output construction proved.
- [x] One-output lower boundary proved.
- [x] Two-output maximal VRI proved.
- [x] Sparse rigid fiber barrier resolved.
- [x] Classical identity-digraph connection recognized and credited.
- [x] Exact finite and asymptotic successor work moved to `main`.
- [x] Bilingual publication released.
- [x] Zenodo DOI assigned: `10.5281/zenodo.22160014`.
- [x] Root README / README_RU updated on `main`.
- [x] Remaining infrastructure classified as deferred/non-blocking.
- [x] Final branch synchronization with current `main` completed by merge commit `2611e148e6ae390503694d0947118319ed24bb02`.

## 7. Reopening policy

Do not reopen this branch for continuation of value-rigidity research. Reopen only to correct an archival factual error in the branch record. Any new theorem, computation, publication, or passport framework should start in a new branch from current `main`.
