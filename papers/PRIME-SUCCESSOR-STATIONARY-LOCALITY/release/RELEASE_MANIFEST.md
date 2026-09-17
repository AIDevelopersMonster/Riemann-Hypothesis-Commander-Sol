# Release Manifest - Stationary Locality v1.0

## Canonical publication files

The Zenodo package should contain:

1. `stationary_locality_en.pdf`
2. `stationary_locality_ru.pdf`
3. `stationary_locality_en.docx`
4. `stationary_locality_ru.docx`
5. `article_en.md`
6. `article_ru.md`
7. `FINITE_STATIONARY_LOCALITY_THEOREM.md`
8. `FINAL_LINE_BY_LINE_AUDIT.md`
9. `README.md`
10. `zenodo_metadata.md`
11. `zenodo_metadata.json`
12. `CITATION.cff`
13. `LICENSE.md` or the repository license copied verbatim into the package
14. `SHA256SUMS.txt`

Optional but useful:

15. `BUILD_NOTES.md` describing the reproducible document build.

## Shipping gates

Before any file is called final:

- incorporate all local repairs from `FINAL_LINE_BY_LINE_AUDIT.md` into both manuscripts;
- verify theorem numbering and cross-language section alignment;
- verify author spelling and ORCID;
- verify all DOIs and bibliographic metadata;
- generate DOCX from the final Markdown source;
- render every DOCX page to PNG and inspect every page;
- generate PDF from the verified source/document;
- render every PDF page to PNG and inspect every page;
- verify no clipped equations, missing glyphs, broken page breaks, or orphaned headings;
- verify that no internal tool citations, TODO markers, or research-status boilerplate remain in the publication files;
- compute SHA256 for every package file after the final render pass;
- generate the ZIP only after checksums are final;
- insert the Zenodo DOI only after the record is created.

## Claim gates

The release may state:

- Multi-Place Finite-Depth Normal Form for finite stationary atlases under the stated target language;
- Private-Place Exact Linear Separation;
- Reduced Affine-Fiber / bounded-anchor cylinder control;
- Fresh-Private-Place Avoidance;
- Formula-Relative Tail Symmetry;
- non-definability of the standard prime order and prime-successor relation;
- finite GIR for every fixed isolator;
- Ramanujan specialization for every finite stationary atlas;
- formula-by-formula compression for the infinite separately named Ramanujan atlas.

The release must not state:

- complete-theory decidability;
- NIP, stability, simplicity, or o-minimality;
- global non-interpretability of arithmetic;
- infinite GIR for the uniformly indexed atlas;
- a universal GIR bound independent of the isolator formula;
- a global automorphism theorem for the full two-sorted structure;
- historical priority without a dedicated literature audit.

## Current source branch

`research/stationary-locality`

## Current publication status

Mathematical proof audit: PASS after local repairs.  
Binary layout/render QA: pending.  
Zenodo record: not yet created.  
Version planned for first deposit: 1.0.
