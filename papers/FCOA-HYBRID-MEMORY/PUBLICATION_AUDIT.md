# Publication audit — FCOA Hybrid Memory Article A

**Audit method:** BC Publication Auditor protocol.

**Document type:** bilingual mathematical preprint / Zenodo publication package.

**Claim ceiling:** exact finite automorphism/minimality theorems for hybrid memory of partial operations, plus one scalable selector family. No claim of general novelty for stabilizers, distinguishing theory, partial algebra, or group actions. No arithmetic-recovery claims.

## Findings

| ID | Severity | Location | Problem | Why it matters | Minimal repair | Claim-set effect |
|---|---|---|---|---|---|---|
| A-01 | C1 | historical minimum statements | Earlier notes treated the 3-cell typed JFS bound as absolute. | One-sorted outputs carry carrier-role information and admit a 2-cell VV witness. | Separate typed/common-terminal and unrestricted one-sorted semantics. | Replaced one global threshold by a semantics-indexed hierarchy. |
| A-02 | C1 | Lift-Compatibility | Full group isomorphism needs all output points used. | Unused pure outputs create a kernel. | State global surjectivity for the isomorphism; retain lift-set formula for active projection without it. | Hypothesis made explicit. |
| A-03 | C2 | novelty language | Stabilizer/equalizer/fiber-product ideas could be read as new. | Those are standard group-action constructions. | State prior-art boundary and restrict novelty to the tagged partial-operation formulation and exact thresholds. | Claim ceiling lowered to defensible FCOA-specific contribution. |
| A-04 | C2 | VV=6 | The old `3+3=6` phrase was too broad. | CVS gives an unrestricted one-sorted 2-cell VV witness. | Label 6-cell result as independent-output and separately value-sensitive. | Repaired. |
| A-05 | C0/C4 | finite counts `24/1`, `48/8` | Counts were previously recorded without a release artifact. | An unshipped enumeration is not reproducible evidence. | Release dependency-free exhaustive verifier with hard assertions and captured output. | Counts retained as computer-assisted propositions. |
| A-06 | C1 | DD threshold in summary table | `DD=2` was previously summarized without a dedicated proof in the article draft. | The publication rule forbids theorem claims without proof. | Add sharp DD proposition and proof. | Claim retained with proof. |
| A-07 | C2 | rigidity language | Finite rigidity can be mistaken for order/arithmetic recovery. | This would inflate the result beyond evidence. | Add arithmetic-leakage firewall and exclude AL0+ work. | Prevents cross-paper claim leakage. |
| A-08 | C4 | bibliography | Initial internal notes had little external prior-art calibration. | Novelty cannot be assessed only inside FCOA. | Add standard partial-algebra, distinguishing-number and base-size references; cite prior FCOA admissibility paper. | Novelty claims narrowed. |
| A-09 | C5 | DOI/metadata | DOI was initially unreserved. | A fabricated or inconsistent DOI is publication-blocking metadata. | Reserve and publish DOI, then synchronize README/CFF/metadata/state. | **Repaired: DOI 10.5281/zenodo.22165651.** |
| A-10 | C5 | bilingual rendering | RU/EN sources need visual PDF verification. | Broken glyphs/overflow would make archival files defective. | Build with XeLaTeX, render every PDF to images, inspect title/middle/final pages; eliminate overfull boxes. | Repaired in publication build. |

## Verification results

The released verifier reproduces:

```text
ONE_SORTED n=2: labeled=0, isomorphism_classes=0
ONE_SORTED n=3: labeled=0, isomorphism_classes=0
ONE_SORTED n=4: labeled=24, isomorphism_classes=1
TYPED_JFS3: labeled=48, isomorphism_classes=8
ALL CHECKS PASSED
```

## Bibliographic/novelty audit

The manuscript explicitly acknowledges established foundations:

- P. Burmeister, *A Model Theoretic Oriented Approach to Partial Algebras* (1986), DOI 10.1515/9783112720875.
- R. F. Bailey and P. J. Cameron, “Base size, metric dimension and other invariants of groups and graphs” (2011), DOI 10.1112/blms/bdq096.
- C. Laflamme, L. Nguyen Van Thé and N. W. Sauer, “Distinguishing Number of Countable Homogeneous Relational Structures” (2010), DOI 10.37236/292.
- A. Malachevsky, prior FCOA admissibility-geometry publication, DOI 10.5281/zenodo.22129787.

The release does not claim that symmetry breaking, base size, color stabilizers or the abstract pullback principle are new. The publication contribution is the exact joint-memory formulation for partial operations, its output-semantics dependence, sharp minima, JFS/CVS separation, and the released finite classifications.

## Render audit

- English edition: 13 pages in the audited RC build, XeLaTeX, visually inspected after raster render; no overfull boxes in final log.
- Russian edition: 14 pages in the audited RC build, XeLaTeX, Cyrillic/math glyphs inspected; no overfull boxes in final log.
- No missing references or undefined labels in final audited build logs.

## Final release status

**PUBLISHED / AUDIT CLOSED**

- Version: **1.0.0**
- Publication date: **2026-08-29**
- Zenodo DOI: **10.5281/zenodo.22165651**
- Persistent URL: https://doi.org/10.5281/zenodo.22165651

No publication-blocking audit item remains in Article A. Further arithmetic-leakage and resource-theory results belong to Article B rather than amendments to this theorem set.