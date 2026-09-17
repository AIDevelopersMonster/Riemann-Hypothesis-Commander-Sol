# Article B — Publication Audit

## Identity and claim ceiling

Article B studies the whole-structure preprocessing-space / conjunctive-query-width tradeoff for canonical finite order and arithmetic on an N-element target sector. The central claim is the exact near-linear width threshold `k_+=9` for truncated addition in the single-CQ model.

## Resolved findings

| ID | Severity | Location | Problem | Minimal repair | Claim-set effect |
|---|---|---|---|---|---|
| B-C0-01 | C0 | former CF theorem | AL0 lower bound ignored target/factorisation attachments | quarantined theorem and removed from dependency chain | narrows |
| B-C0-02 | C0 | former bounded-depth result | successor chain was treated as FO-accessible total order | quarantined lower-bound claim | narrows |
| B-C2-01 | C2 | RTP line | presentation-level CRT profile risked being described as intrinsic | reclassified as normal-form calibration | clarifies |
| B-C2-02 | C2 | logical scope | one CQ was conflated with full existential-positive FO | claim restricted to single conjunctive queries | narrows |
| B-C0-03 | C0 | first CQ8 proof | boundary size >=2 did not justify two private positive helpers | replaced by zero-information conditioning and colored-closure proof | none after repair |
| B-C1-01 | C1 | colored closure | one connected component did not necessarily contain all adjacent helpers | closure redefined as union of all same-color components meeting A_F | clarifies |

## Final theorem dependency chain

canonical definitions -> FO preprocessing collapse -> CQ width-3 separation -> Latin slice -> boundary entropy -> zero-information conditioning -> unique information colors -> no singleton colored closure -> six-helper lower bound -> CRT width-9 upper bound.

No quarantined theorem is used.

## Bibliography

Principal DOI-checked references:

- Olteanu & Zavodny, ICDT 2012: `10.1145/2274576.2274607`
- Gogacz & Torunczyk, ICDT 2017: `10.4230/LIPIcs.ICDT.2017.15`
- Berkholz & Vinall-Smeeth, ICDT 2026: `10.4230/LIPIcs.ICDT.2026.11`

No prior-art source was found in the targeted search that directly states the specialized width-9 threshold proved here. The manuscript therefore presents it as an independent specialized theorem without claiming a theorem for all finite-variable logic.

## Build and rendering

- English XeLaTeX source: compiled, 13 pages.
- Russian XeLaTeX source: compiled, 11 pages.
- Both PDFs: openable, text PDFs, non-encrypted.
- Both PDFs rendered to page images and visually inspected.
- No clipping, overlap, black squares, or broken Cyrillic glyphs observed.
- Minor TeX overfull warnings remain in dense prose, with no visible page-boundary clipping in the render audit.

## Final audit block

- unresolved blocking issues: Zenodo DOI not yet reserved; no known mathematical blocker
- equations/theorems changed: yes, closure definition and proof wording repaired
- claim set changed: yes, narrowed during audit
- bibliography verified: yes, principal references
- metadata verified: partial (DOI pending)
- source compiled: yes
- PDF visually inspected: yes
- release status: `REVIEWED_CLEAN`

Final publication requires DOI insertion, rebuild, checksum refresh, and one final DOI/metadata consistency pass.