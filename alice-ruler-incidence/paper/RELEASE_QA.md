# Release QA — Alice Throws Away the Ruler II

Date: 2026-09-13  
Status: **RELEASE READY — awaiting Zenodo upload and DOI issuance**

## Mathematical gate

PASSED.

The publication-core proof has no recorded unresolved logical step. The strengthened proof is isolated in `proofs/PHASE_STABILITY_PROOF.md` and synchronized into both language manuscripts.

## Manuscript gate

PASSED.

- EN: `paper/PHASE_RIGIDITY_EN.md`
- RU: `paper/PHASE_RIGIDITY_RU.md`
- version: `v1.0`
- theorem numbering synchronized;
- anti-mitre terminology warning included;
- `C_A` relabelling audit included;
- Fano two-colour lemma included;
- `S_9` contains no `S_7` lemma included;
- zero-defect classical citation boundary explicit;
- no edit-distance overclaim remains.

## Bibliography gate

PASSED.

References 1–8 were normalized; DOI metadata is recorded where available. The OUP DOI for Colbourn–Rosa, *Triple Systems*, is `10.1093/oso/9780198535768.001.0001`.

## PDF gate

PASSED.

Final local artifacts:

- `Alice_Throws_Away_the_Ruler_II_Phase_Rigidity_EN_v1.0.pdf`
- `Alice_Throws_Away_the_Ruler_II_Phase_Rigidity_RU_v1.0.pdf`

Both PDFs:

- 12 pages;
- open successfully;
- are text PDFs, not scans;
- were rendered at 150 dpi for visual QA;
- show no clipped text, overlaps, broken mathematical glyphs, or broken Cyrillic;
- have no orphan trailing page after final pagination correction.

Representative visual checks included title/abstract page, proof-heavy middle pages, and final bibliography/author-note page in both languages.

## Remaining release actions

1. Upload both PDFs to Zenodo using `paper/ZENODO_METADATA.md`.
2. Obtain DOI.
3. Insert DOI into both manuscript metadata blocks and `STATUS.md` / repository publication index.
4. If desired, tag/archive the branch state as the v1.0 publication snapshot.

No scientific or typesetting blocker remains.