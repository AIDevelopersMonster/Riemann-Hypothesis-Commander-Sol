# FCOA Rigidity - Article B

## Reflections on Sparse Anonymous Phase Geometry with Commander Sol
### Component Cocycles, Synchronization Costs, and Actual Cell-Extension Separation

Author: Alex Malachevsky  
ORCID: 0009-0008-6009-3196  
Version: 1.0  
Status: **PUBLICATION READY - Zenodo DOI pending**  
Date: 29 August 2026

Companion foundation: Article A, DOI **10.5281/zenodo.22157403**.

## Proved core

- Componentwise Phase Theorem on the ordered-cell incidence graph `Lambda(D)`.
- Exactness iff all realized component phase cocycle values are diagonal.
- Three distinct costs: fixed-domain `lambda(D,c)`, connectivity repair `mu(D)`, actual cell-extension `alpha(D,c)`.
- Universal bound `alpha <= mu <= kappa(Lambda)-1`.
- Explicit family with `lambda=r-1` and `alpha=1`; hence unbounded `lambda/alpha` separation.
- No-old-obstruction theorem: any failure of `alpha<=lambda` must be caused by a newly created bad symmetry moving the old domain.
- Deletion-symmetry reformulation and recognizable-bridge sufficient criterion.
- Complete audit on four carrier points: 523,250 surjective layers, only `(lambda,alpha)=(0,0),(1,1),(2,1)`.
- Five-point sector with at most five defined cells: 270,085 layers, no counterexample.

## Open boundary

`alpha(D,c) <= lambda(D,c)` remains Conjecture 14. It is explicitly not used as a premise of any theorem in the paper.

## Publication files

- `article_en.md`, `article_ru.md` - source manuscripts.
- `FCOA_Sparse_Phase_EN.docx`, `FCOA_Sparse_Phase_RU.docx` - editable publication versions.
- `FCOA_Sparse_Phase_EN.pdf`, `FCOA_Sparse_Phase_RU.pdf` - release PDFs.
- `demo_sparse_phase.html` - interactive explanatory companion.
- `verify_article_b.py` - finite witness and audit verifier.
- `CITATION.cff` - citation metadata; add Article B DOI after Zenodo deposit.

## QA completed

- hostile proof audit completed;
- bibliography corrected and publisher DOI records checked;
- Article A dependency frozen to DOI `10.5281/zenodo.22157403`;
- EN/RU synchronized;
- DOCX rendered page-by-page and visually inspected;
- PDFs independently rendered and visually inspected;
- interactive HTML browser-rendered in before/after states and visually inspected;
- core verifier reproduced the complete n=4 count exactly.

No mathematical revision is required before Zenodo deposit. The Article B DOI is the only missing archival metadata field.