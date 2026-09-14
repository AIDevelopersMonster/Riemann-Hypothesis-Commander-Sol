# HATTER-SOL-11 · Parent Series Metadata Audit

**Date:** 2026-09-14  
**Purpose:** freeze the citation status of HATTER-SOL-07--10 before HATTER-SOL-11 v0.9.

## HATTER-SOL-07

Repository cross-reference in the frozen HATTER-SOL-08 README identifies the parent work as HATTER-SOL-07 and records:

\[
\boxed{\text{DOI }10.5281/zenodo.22724185.}
\]

Use this DOI in the HATTER-SOL-11 bibliography.

The older HATTER-SOL-07 README predates publication metadata and still describes the project as exploratory; it should not override the later explicit DOI cross-reference.

## HATTER-SOL-08

Final repository metadata:

- title: *From a Line to Space: Dimensional Suppression of Factor-Architecture Sensitivity*;
- version: `v1.0`;
- publication/package date: `2026-09-13`;
- author: Malachevsky, A.A.;
- ORCID: `0009-0008-6009-3196`;
- repository status: `FROZEN FOR ZENODO DEPOSIT`;
- repository DOI field: **pending Zenodo deposit**.

The README explicitly states that the final EN/RU PDFs, metadata, checksums and source package were prepared, but the HATTER-SOL-08 DOI had not yet been assigned at the recorded state.

A focused current web/Zenodo-index search by exact title and author returned no reliable public record from which a later DOI could be verified. Therefore:

\[
\boxed{\text{Do not invent an HATTER-SOL-08 DOI.}}
\]

For HATTER-SOL-11 v0.9, cite HATTER-SOL-08 by title, author, version/date, and repository record, with `Zenodo DOI pending` only if a status note is useful.

## HATTER-SOL-09

Repository metadata currently exposes:

- title: *World-Dependent Factor Networks and a Prime-Toggle Response Operator*;
- author: Malachevsky, A.A.;
- ORCID: `0009-0008-6009-3196`;
- date: `2026-09-13`;
- status: `preprint candidate v0.9`.

The main-branch directory contains `HATTER-SOL-09_EN_preprint_candidate_v0.9.md` but no publication README or Zenodo metadata file in the directory listing inspected for this audit. A focused current web/Zenodo-index search by exact title and author returned no reliable DOI record.

Therefore:

\[
\boxed{\text{HATTER-SOL-09 DOI not verified; do not invent one.}}
\]

HATTER-SOL-11 should cite the v0.9 repository preprint unless a later publication record is supplied or added to the repository.

## HATTER-SOL-10

The main-branch publication README records:

- English title: *Ideal Factor Networks Beyond Unique Element Factorization*;
- author: Malachevsky, A.A.;
- ORCID: `0009-0008-6009-3196`;
- status: `published`;
- Zenodo DOI:

\[
\boxed{10.5281/zenodo.22734865.}
\]

Use this DOI in the HATTER-SOL-11 bibliography.

## Citation table for HATTER-SOL-11

| Work | Version/status to cite | DOI status |
|---|---|---|
| HATTER-SOL-07 | published parent work | `10.5281/zenodo.22724185` |
| HATTER-SOL-08 | v1.0, 2026-09-13, frozen deposit package | DOI not yet verified / repository says pending |
| HATTER-SOL-09 | EN preprint candidate v0.9, 2026-09-13 | DOI not verified |
| HATTER-SOL-10 | published | `10.5281/zenodo.22734865` |

## Publication-gate consequence

The parent-series metadata gate is now **resolved**, even though H08/H09 do not currently have verified DOI values. A missing DOI is not itself an inconsistency; an invented DOI would be.

For HATTER-SOL-11 v0.9:

1. use DOI citations for H07 and H10;
2. use explicit repository/version citations for H08 and H09;
3. do not write placeholder numeric DOI values;
4. if H08 or H09 receives a DOI before H11 deposit, update the bibliography during the final metadata audit.

With this rule, parent-series metadata no longer blocks freezing the HATTER-SOL-11 theorem manuscript.
