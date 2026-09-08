# Release Metadata — FCOA Prescribed-Stabilizer Support

**Release date:** 2026-09-01  
**Series:** Commander Sol / Fixed-Carrier Oriented Algebra  
**Author:** Alex Malachevsky  
**Publication status:** **release candidate passed; ready for Zenodo deposit**

## English title

**Prescribed-Stabilizer Support in Fixed-Carrier Oriented Algebra: Wreath Coherence, Partition Compression, and Exact Orbital Separation**

## Russian title

**Предписанная стабилизаторная опора в фиксированно-носительной ориентированной алгебре: Wreath-когерентность, сжатие разбиений и точное орбитальное разделение**

## Required FCOA linkage

- FCOA Foundation: DOI `10.5281/zenodo.22164246`
- Direct FCOA-Z predecessor: DOI `10.5281/zenodo.22171473`

The Foundation DOI is present in both article abstracts and both bibliographies.

## Final release assets

- `FCOA_Prescribed_Stabilizer_Support_EN_2026-09-01.pdf`
- `FCOA_Prescribed_Stabilizer_Support_RU_2026-09-01.pdf`
- `FCOA_Prescribed_Stabilizer_Support_SOURCE_2026-09-01.zip`
- `VERIFIER_OUTPUT_2026-09-01.txt`

PDF quality audit:

- English: 18 pages, A4; rendered and inspected page-by-page/contact-sheet.
- Russian: 15 pages, A4; rendered and inspected page-by-page/contact-sheet.
- title pages, displayed mathematics, exact-minima table, Cyrillic text, and bibliography inspected;
- no clipping or overlap observed.

## Frozen verifier state

- Python: `3.13.5`
- `verify_partition_only_exact_solver.py` Git blob: `d2357d683c925eae925c2e71558b15ee05312bc8`
- `verify_branch_coherence_support.py` Git blob: `f801a90232b8818c017065ceff115e4e228cd769`
- frozen verifier output SHA-256: `41fa2dcf71bfbd1939e9f5b4d47927110efcdd6a3b9733d0f28e798d41d86d97`
- partition verifier result: `ALL PASS`
- integer partitions checked: `43`
- orbital unions checked: `1468`
- verified range: all integer partitions with total branch count `2 <= b <= 7`
- seven-vertex branch-coherence verifier: `PASS`, exact anonymous-output minimum `9`

## Final bibliography hardening

The release-normalized manuscripts correct and synchronize the following metadata:

- Saeid Alikhani, Ahmad Mirjalili, Samaneh Soltani — three-author form for DOI `10.1080/02522667.2021.2003011`;
- Grech–Kisielewicz — Journal of Algebraic Combinatorics 57 (2023), 1045–1072;
- Sabatini — Bulletin of the London Mathematical Society 58 (2026), e70201.

## Claim discipline

The release must not claim priority for:

- regular sets or setwise stabilizers;
- distinguishing numbers;
- wreath-product symmetry breaking in general;
- relation groups or 2-closure;
- point-determining / twin-free graphs;
- minimum graph representations of abstract automorphism groups.

The release may claim the self-contained theorems proved in the manuscript for the declared fixed actions, including the exact wreath-coherence formulas, arbitrary partition phase-coherence formula, partition-only full-fiber reduction, Partition-Overgroup Dichotomy, Macro-Mover Double Coset Lemma, exact recognition theorem, and Orbital XOR-Separation formulation.

No NP-hardness claim is made.

## Zenodo description seed

This work develops a fixed-action support theory for exact residual symmetry in Fixed-Carrier Oriented Algebra (FCOA). It defines an organizing prescribed-stabilizer support quantity, proves exact support laws for global and partitioned wreath coherence, separates partition memory from phase-coherence memory, and reduces partition-only memory to a sparse directed-relation problem. A structural overgroup dichotomy and singleton macro-swap lemma yield an exact weighted Orbital XOR-Separation Program for arbitrary finite partition type. Exhaustive verification through all integer partitions with total branch count `b <= 7` agrees with the proved recognition criterion.

## Keywords

`Fixed-Carrier Oriented Algebra`, `FCOA`, `permutation groups`, `wreath products`, `setwise stabilizers`, `relation groups`, `2-closure`, `orbital digraphs`, `prescribed stabilizer`, `symmetry breaking`, `partition stabilizer`, `exact support`, `twin separation`

## Deposit note

No Zenodo connector/plugin is currently available in this environment. The external Zenodo upload is therefore the only remaining platform step. After a DOI is assigned, write it back to this file and the relevant repository README/index records.
