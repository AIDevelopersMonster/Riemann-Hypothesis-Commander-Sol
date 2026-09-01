# Release Checklist — Prescribed-Stabilizer Support in FCOA

Status: pre-release  
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

## Proof audit

- [x] `PROOF_AUDIT_2026-09-01.md` completed.
- [x] Arbitrary-partition lower bound reread.
- [x] Overgroup proof reread.
- [x] Macro-swap proof expanded.
- [x] Anonymous-output exception checked against the global theorem.
- [ ] Final equation-number cross-check after LaTeX conversion.
- [ ] Final theorem-number cross-check after LaTeX conversion.

## Manuscripts

- [x] `ARTICLE_EN.md` created.
- [x] `ARTICLE_RU.md` created.
- [ ] English/Russian equation numbering synchronized after final edits.
- [ ] English/Russian bibliography synchronized after final edits.
- [ ] Convert final source to LaTeX.
- [ ] Build PDF.
- [ ] Render/inspect PDF page-by-page.
- [ ] Produce archival source package.

## Verification assets

Expected supporting files from research directory:

- `../FCOA-Z-RAY-AXIS/solve_partition_only_support.py`
- `../FCOA-Z-RAY-AXIS/verify_partition_only_exact_solver.py`
- `../FCOA-Z-RAY-AXIS/verify_branch_coherence_support.py`

Before release:

- [ ] Freeze verifier outputs in a text artifact with date/version.
- [ ] Record Python version / execution environment.
- [ ] Check examples in the article against frozen output.

## Bibliography audit

Included classical neighbors:

- Gluck — trivial set-stabilizers.
- Chan — wreath-product distinguishing number.
- Alikhani–Soltani — subgroup-relative distinguishing.
- Dalla Volta–Siemons — relation groups/orbit equivalence.
- Grech–Kisielewicz — orbit-closed/relation groups.
- Liebeck–Praeger–Saxl — 2-closure.
- Sumner — point-determining graphs.
- Entringer–Gassman — point distinguishing.
- Hell–Hernandez-Cruz — point-determining digraphs.
- McCarthy–Quintas; Babai–Goodman–Lovasz; Babai–Goodman; Deligeorgaki — minimum graph realization with given automorphism group.
- Sabatini — contemporary set-stabilizer work.

Before release:

- [ ] Verify final volume/page/year metadata against DOI landing pages.
- [ ] Normalize bibliography style.

## Release decision

### Research publication threshold

\[
\boxed{\text{PASSED}}
\]

### Immediate Zenodo upload threshold

\[
\boxed{\text{NOT YET: LaTeX/PDF/frozen-verifier editorial pass remains}}
\]

No further theorem discovery is required for the first paper. Complexity classification of the Orbital XOR-Separation Program should be treated as a separate follow-up branch unless it yields quickly during editorial work.
