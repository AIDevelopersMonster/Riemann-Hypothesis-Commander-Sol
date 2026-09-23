# HATTER-SOL-18 · FINAL PUBLICATION AUDIT

**Date:** 19 September 2026  
**Scope:** RU/EN publication-freeze manuscripts, theorem/claim discipline,
bibliography, hardware evidence, reproducibility, metadata.  
**Frozen manuscripts:**

- `HATTER_SOL_18_RU_FROZEN_v1.0-rc1.md`
- `HATTER_SOL_18_EN_FROZEN_v1.0-rc1.md`

## Claim ceiling

The manuscript may claim exact finite results only for the explicitly frozen
(PSL(2,7)) quotient/query models and may report FPGA results only as measured
realization witnesses under the declared Quartus/device/corner conditions.

H18-12 is a framework/methodology for technology-relative hardware images of
finite mathematical presentations.  It is not claimed to be a
technology-independent complexity invariant or a proof of globally optimal
circuits.

## Audit findings

| ID | Severity | Location | Problem | Why it matters | Minimal repair | Claim-set effect |
|---|---|---|---|---|---|---|
| F01 | C2 | §5, §19, title | `commutator-lift trace` and the classical Higman invariant were phrased too nearly as identical objects | McCullough–Wanderley distinguish the Higman invariant from commutator trace | Reworded (	au) as canonical determinant-one commutator-lift trace; Higman relation retained without identity claim; title tightened | narrows |
| F02 | C4 | References | Several bibliography entries lacked issue/page metadata; HATTER-SOL-17 was described as having unspecified “DOI materials” | Unverifiable metadata is not acceptable at freeze | Verified DOI/title/volume/page metadata; replaced unsupported H17 DOI implication with exact repository/branch reference | clarifies |
| F03 | C4 | §5–§6, §21 | Classical trace/Nielsen/Higman background lacked explicit in-text literature anchors | Readers could not distinguish classical ingredients from H18 finite results | Added [1,9] anchors; related PSL generating-pair context [2]; hardware-complexity context [3–8] | clarifies |
| F04 | C1 | H18-12 §13 | Pareto order did not explicitly state that (F_{max}) is maximized while area/delay coordinates are minimized | Without coordinate directions, the partial order is formally ambiguous | Declared optimization direction for every profile coordinate and allowed (1/F_{max}) as minimized substitute | clarifies |
| F05 | C2 | LAB-04 / §16 | EP4CE115F29C7 value 26,460 could be mistaken for final fitter utilization | Current extractor proves a MAP estimate, not a separately archived final-fit utilization line | Frozen manuscript labels 26,460 only as MAP estimate | narrows |
| F06 | C2 | LAB-03/LAB-04 fault comparison | 2,561 static erased-identity cases had earlier been described as “stronger” than the temporal schedule test | The raw fault representations are different and not ordered by set inclusion | Removed stronger/weaker language; retained semantic translation and E1 contract only | narrows |
| F07 | C2 | H17↔H18 comparison | Fault-tolerant H17/H18 could be read as identical Boolean functions | H17 erases a fixed fingerprint coordinate; H18 erases an adaptive query identity | Formalized E0 fault-free pointwise comparison and E1 common-contract comparison in H18-13 | clarifies |
| F08 | C5 | §8 vs §15 | 32-cycle H18-07 and 42-cycle H18-LAB-03 figures could be conflated | They belong to different RTL architectures | Explicitly separated the two architecture-specific cycle counts | clarifies |
| F09 | C5 | RU/EN status | Physical matrix closed after the previous “remaining gates” text was written | Stale gate text would make the freeze self-contradictory | Replaced with publication-freeze section and non-blocking future directions | none |
| F10 | C5 | Metadata | Drafts lacked explicit author/ORCID/collaborator metadata | Publication package should match repository citation metadata | Added Alex Malachevsky, ORCID 0009-0008-6009-3196, Commander Sol/Hatter Sol as AI research collaborator | none |
| F11 | C5 | Reproducibility | RU reproducibility section omitted the final one-command Cyclone-V LAB-03 control | Final physical matrix should be reproducible from the freeze text | Added `run_cyclonev_a7_full.ps1` and H18-13/audit references | none |

## Mathematical audit result

No C0 mathematical contradiction was found between the frozen manuscript
claims and the inspected exact certificates:

- H18-01: (D^*(W_4)=4), fixed minimum 5, path sum 382;
- H18-02/03: Nielsen component sizes (36,32,32,14) and trace fibers;
- H18-05: three-shadow reconstruction and (m_	au(W_4)=3);
- H18-06: (D_0=4,S_1=4,A_1=5) under one persistent known query erasure;
- H18-09/10/11: 26-query reduction, (9le M_1(W_4)le12),
  12-query witness, 305-node controller, 18,425-bit payload.

The unresolved exact value of (M_1(W_4)) is retained as an open problem and
is not a publication blocker.

## Physical-evidence audit result

The freeze preserves the following distinctions:

- failed fit = capacity evidence only, no routed timing;
- Quartus measurements = technology-relative realization witnesses, not
  globally optimal circuit complexity;
- Cyclone V = platform-level ALM+DSP comparison;
- LAB-03 ↔ LAB-04 = same-mathematics architecture control;
- H17-LAB-02 ↔ H18-LAB-04 = matched one-cycle mathematical-presentation
  comparison at E0/E1 claim levels.

The Cyclone-V same-mathematics control is closed:

[
1455 {m ALM}+26 {m DSP}, 42 {m cycles}
]

versus

[
10627 {m ALM}+48 {m DSP}, 1 {m cycle},
]

with approximately (7.30	imes) ALM spatialization cost and
(25.5	imes) reduction in worst transaction latency.

## Bibliography audit result

Bibliographic metadata and DOI identifiers were checked against publisher,
conference, author/institutional, or Dagstuhl/DBLP records.  The freeze includes
complete volume/issue/page data where available and adds Macbeath's primary
1969 source for the linear-fractional/trace context.

HATTER-SOL-17 has no publication DOI asserted in this freeze.  It is cited as
repository material by exact folder and branch.

## RU/EN synchronization

The frozen RU and EN files have matching section counts and the same numerical
claim set for:

- 197 = 114 + 83 states;
- (D^*=4), (191/57);
- (S_1=4,A_1=5);
- (9le M_1(W_4)le12);
- 18,425-bit payload;
- Cyclone-IV and Cyclone-V H17/H18 measurements;
- H18 temporal/spatial ratios;
- 26,460 as MAP estimate only;
- publication non-claims and H18-12/H18-13 boundaries.

## Final audit block

- unresolved blocking issues: **none in manuscript content**
- equations/theorems changed: **no numerical theorem result changed; one formal Pareto-definition clarification**
- claim set changed: **yes — narrowed/clarified only; no expansion**
- bibliography verified: **yes**
- metadata verified: **yes, against repository CITATION.cff / HATTER-SOL metadata**
- source compiled: **yes — final RU/EN PDFs built from frozen Markdown**
- PDF visually inspected: **yes — see `PDF_RENDER_AUDIT_2026-09-20.md`**
- release status: **PUBLICATION_READY**


## Render closure · 2026-09-20

Final RU/EN PDFs were rebuilt after status promotion and passed the page-by-page render audit recorded in `PDF_RENDER_AUDIT_2026-09-20.md`. No additional mathematical or bibliographic change was introduced at render closure.
