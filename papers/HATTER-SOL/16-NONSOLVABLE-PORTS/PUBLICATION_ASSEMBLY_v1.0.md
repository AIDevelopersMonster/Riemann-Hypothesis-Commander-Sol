# HATTER-SOL-16 · Publication assembly v1.0

**Date:** 2026-09-16  
**Research status:** CLOSED  
**Publication status:** bilingual pre-Zenodo assembly complete  
**Installment DOI:** not yet assigned  
**Series DOI:** 10.5281/zenodo.17996774  
**ORCID:** 0009-0008-6009-3196

## Final assembly contents

The publication package has been typeset in English and Russian as both DOCX and PDF. The complete annotated HATTER-SOL-01…15 bibliography is included in both language editions and is also stored separately as `ANNOTATED_SERIES_BIBLIOGRAPHY_v1.0.md`.

The bibliography policy is conservative: a DOI is printed only where an installment DOI has already been assigned. HATTER-SOL-04, HATTER-SOL-06 and HATTER-SOL-15 are explicitly marked as non-DOI repository/publication-candidate layers rather than being assigned guessed identifiers.

## Authoritative mathematical correction

The publication uses

\[
S_4=28d+4\operatorname{Tr}\rho(K)+4\operatorname{Tr}\rho(K^{-1}),
\]

and therefore for the real three-dimensional `A5` channel

\[
\boxed{S_4=84+8\chi_3(K)}.
\]

Any older research note containing `48+8 chi_3(K)` is superseded by the final manuscript and `FINAL_CORRECTIONS_v1.0.md`.

## Built files

Local publication artifacts:

- `HATTER_SOL_16_EN_v1.0_publication.docx`
- `HATTER_SOL_16_EN_v1.0_publication.pdf`
- `HATTER_SOL_16_RU_v1.0_publication.docx`
- `HATTER_SOL_16_RU_v1.0_publication.pdf`
- `HATTER_SOL_ANNOTATED_SERIES_BIBLIOGRAPHY_v1.0.md`
- `HATTER_SOL_16_v1.0_publication_package.zip`
- PDF preflight reports and SHA-256 manifest.

## SHA-256

- EN PDF: `236921639d6042dec31731a65f9adef49dc116ed6e80ba529a5bb46cbbc14a55`
- RU PDF: `b38c7b7c17cdcc72fff42b1699efc831e618546200648fea6c7073ee6c15b26d`
- EN DOCX: `ba1a0ddca8e657d81ce2e5bf5499a92846c57a1064784ee40d15339dc1079b52`
- RU DOCX: `fd7070fb92a65319eb8565f918c925fc3ed3938941aadb67949de8696d0499ab`

## Visual and PDF QA

Both editions were rendered after final typesetting and all pages were visually inspected. The final builds contain seven pages each. No clipping, overlap, missing glyphs or broken tables were observed.

PDF preflight for both editions:

- openable: yes;
- encrypted: no;
- likely scanned: no;
- XFA: no.

## Remaining release step

After Zenodo assigns the HATTER-SOL-16 installment DOI:

1. insert that DOI into EN/RU sources and publication metadata;
2. rebuild both PDF/DOCX editions;
3. rerun visual QA and PDF preflight;
4. update GitHub bibliography/status;
5. merge/archive the research branch according to the HATTER-SOL release workflow.
