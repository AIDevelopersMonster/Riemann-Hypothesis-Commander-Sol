# Release Checklist — Prescribed-Stabilizer Support in FCOA

Status: **release candidate passed; ready for repository deposit**  
Date: 2026-09-01

## Research threshold

- [x] Exact global coherence theorem proved.
- [x] Exact arbitrary-partition phase-coherence theorem proved.
- [x] Partition-only full-fiber reduction proved.
- [x] Infinite special families solved exactly.
- [x] Arbitrary finite partition reduced to exact Orbital XOR-Separation Program.
- [x] Partition-Overgroup Dichotomy proved.
- [x] Singleton macro-swap double-coset lemma strengthened after hostile reread.
- [x] Exact recognition theorem proved.
- [x] Small-case verifier agrees with direct `S_b` enumeration for all tested integer partitions through `b<=7`.
- [x] Hostile literature audit completed.
- [x] No direct duplication of the combined theorem chain found.

## Mandatory FCOA publication requirements

- [x] Foundation DOI appears in English abstract: `10.5281/zenodo.22164246`.
- [x] Foundation DOI appears in Russian abstract: `10.5281/zenodo.22164246`.
- [x] Foundation paper included in bibliography.
- [x] Concrete FCOA structure described explicitly.
- [x] Direct predecessor FCOA-Z axis paper cited: `10.5281/zenodo.22171473`.

## Claim discipline

- [x] No claim that regular sets are new.
- [x] No claim that setwise stabilizers are new.
- [x] No claim that wreath-product symmetry breaking is new.
- [x] No claim that twin-free / point-determining graphs are new.
- [x] No claim that relation groups or 2-closure are new.
- [x] `m_G(H;S)` presented as an organizing invariant, not a universal priority claim.
- [x] Exact-vs-contained distinction from subgroup-relative distinguishing stated.
- [x] No NP-hardness claim.

## Proof and numbering audit

- [x] `PROOF_AUDIT_2026-09-01.md` completed.
- [x] Arbitrary-partition lower bound reread.
- [x] Overgroup proof reread.
- [x] Macro-swap proof expanded.
- [x] Anonymous-output exception checked against the global theorem.
- [x] Final equation-number sequence checked after Pandoc/XeLaTeX build.
- [x] Final theorem/lemma numbering checked after Pandoc/XeLaTeX build.
- [x] EN and RU versions checked for theorem-content alignment.

The English and Russian manuscripts are parallel publications, not literal line-by-line translations. Their equation numbering is intentionally internally consistent rather than artificially forced to be identical.

## Manuscripts and PDF build

- [x] `ARTICLE_EN.md` created.
- [x] `ARTICLE_RU.md` created.
- [x] Release-normalized sources produced by `prepare_release_sources.py`.
- [x] English/Russian bibliographies synchronized after final metadata audit.
- [x] Reproducible Pandoc + XeLaTeX build added in GitHub Actions.
- [x] Backslash-delimited TeX math enabled explicitly in the Pandoc reader.
- [x] English PDF built successfully.
- [x] Russian PDF built successfully.
- [x] PDFs rendered to PNG page images and visually inspected.
- [x] Title pages inspected.
- [x] Formula rendering inspected.
- [x] Exact-minima table inspected.
- [x] Cyrillic rendering inspected.
- [x] Bibliography pages inspected.
- [x] No clipping/overlap observed in page contact sheets.
- [x] Archival source package produced.

The publication workflow is `.github/workflows/build-fcoa-prescribed-stabilizer-paper.yml`; release assets are produced as the `fcoa-prescribed-stabilizer-publication` artifact. Build identifiers are intentionally not frozen in this checklist so editorial metadata updates do not make the checklist stale.

Final PDF geometry verified during QA:

- EN: 18 pages, A4, PDF 1.5
- RU: 15 pages, A4, PDF 1.5

## Verification assets

Supporting files:

- `../FCOA-Z-RAY-AXIS/solve_partition_only_support.py`
- `../FCOA-Z-RAY-AXIS/verify_partition_only_exact_solver.py`
- `../FCOA-Z-RAY-AXIS/verify_branch_coherence_support.py`

Release verification:

- [x] Verifier outputs frozen in `VERIFIER_OUTPUT_2026-09-01.txt`.
- [x] Python version recorded: `3.13.5`.
- [x] Verifier Git blob hashes recorded.
- [x] All integer partitions with `2 <= b <= 7` checked.
- [x] 43 partition types checked.
- [x] 1468 invariant orbital unions checked.
- [x] Exact recognizer result: `ALL PASS`.
- [x] Seven-vertex D8/V4 support verifier: `PASS`.
- [x] Frozen output SHA-256: `41fa2dcf71bfbd1939e9f5b4d47927110efcdd6a3b9733d0f28e798d41d86d97`.
- [x] Frozen transcript checksum is external to the transcript itself; no self-referential hash line remains.
- [x] Examples in the article checked against the frozen output.

## Bibliography audit

Included classical neighbors:

- Gluck — trivial set-stabilizers.
- Chan — wreath-product distinguishing number.
- Alikhani–Mirjalili–Soltani — subgroup-relative distinguishing.
- Dalla Volta–Siemons — relation groups/orbit equivalence.
- Grech–Kisielewicz — orbit-closed/relation groups.
- Liebeck–Praeger–Saxl — 2-closure.
- Sumner — point-determining graphs.
- Entringer–Gassman — point distinguishing.
- Hell–Hernández-Cruz — point-determining digraphs.
- McCarthy–Quintas; Babai–Goodman–Lovász; Babai–Goodman; Deligeorgaki — minimum graph realization with given automorphism group.
- Sabatini — contemporary set-stabilizer work.

Final hardening corrections:

- [x] Alikhani paper corrected to three authors: Saeid Alikhani, Ahmad Mirjalili, Samaneh Soltani.
- [x] Grech–Kisielewicz pages normalized to 1045–1072.
- [x] Sabatini normalized to *Bulletin of the London Mathematical Society* 58 (2026), e70201.
- [x] Bibliography style normalized consistently in both release PDFs.

## Release assets

- `FCOA_Prescribed_Stabilizer_Support_EN_2026-09-01.pdf`
- `FCOA_Prescribed_Stabilizer_Support_RU_2026-09-01.pdf`
- `FCOA_Prescribed_Stabilizer_Support_SOURCE_2026-09-01.zip`
- `VERIFIER_OUTPUT_2026-09-01.txt`

## Release decision

### Research publication threshold

\[
\boxed{\text{PASSED}}
\]

### PDF/source archival threshold

\[
\boxed{\text{PASSED}}
\]

### Zenodo deposit threshold

\[
\boxed{\text{PASSED — READY FOR DEPOSIT}}
\]

No further theorem discovery is required for this release. Complexity classification of the Orbital XOR-Separation Program belongs to a separate follow-up branch.

No Zenodo connector/plugin is currently available in this environment, so the external deposit itself is the remaining manual/platform step. Once a DOI is assigned, it should be written back to `RELEASE_METADATA.md`, both article source records if desired, and the relevant repository README/index files.
