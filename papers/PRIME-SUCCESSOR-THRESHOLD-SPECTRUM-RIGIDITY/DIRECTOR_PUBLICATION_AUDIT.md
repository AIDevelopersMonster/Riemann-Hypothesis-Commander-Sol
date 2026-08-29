# Director Publication Audit — Threshold Spectrum Rigidity

**Branch:** `research/threshold-spectrum-rigidity`  
**Target:** `papers/PRIME-SUCCESSOR-THRESHOLD-SPECTRUM-RIGIDITY/`  
**Date:** 2026-08-29  
**Verdict:** **MATHEMATICAL CORE PASS / PUBLICATION PACKAGE NOT YET READY**

## 1. What passes

The central theorem package is mathematically coherent and, after checking the proof and hostile audit, no fatal defect was found in the following claims:

1. fixed source-prime calibration in the expanded threshold structure;
2. parameter-free calibration of target `1` from the single bridge value `u_2=-23/32`;
3. parameter-free definition of every fixed rational probe;
4. pointwise threshold recovery by the sentences `Sigma_{ell,m}`;
5. threshold-spectrum rigidity:
   `Th(V_{Delta,kappa}) = Th(V_{Delta,lambda}) iff kappa=lambda` in the standard family;
6. continuum many distinct complete theories at fixed full support and threshold alphabet `{1,2}`;
7. the unanchored finite-support rational-scaling gauge classification, subject to the exact language and standard-model scope stated in `FULL_PROOF.md`;
8. bridge gauge fixing.

The hostile audit correctly distinguishes theory-level pointwise recovery from the still-open problem of one uniform internal formula reconstructing the variable profile.

## 2. Why release is not yet authorized

The branch head is still the hostile-audit checkpoint. The hostile audit itself explicitly states that it does **not** authorize publication and that literature and claim audits remain required.

The paper directory currently contains only:

- `THRESHOLD_SPECTRUM_RIGIDITY.md`;
- `FULL_PROOF.md`;
- `HOSTILE_AUDIT.md`.

There is no final publication manuscript, bibliography/priority audit, citation metadata, release README, RU/EN synchronized publication pair, or rendered PDF/DOCX package.

Therefore the statement “publication ready” is premature if it means “ready to upload to Zenodo now.”

## 3. Required mathematical/editorial reconciliation

`THRESHOLD_SPECTRUM_RIGIDITY.md` retains the earlier two-prime Bezout calibration using `u_2,u_5`, whereas `FULL_PROOF.md` correctly simplifies target-unit calibration to the single bridge value `u_2=-23/32`.

Both paths are compatible, but the final paper must use one canonical proof path. Recommendation: use the one-prime calibration from `FULL_PROOF.md` and retain the Bezout construction only as a historical remark, if at all.

The final manuscript should also emphasize that individual fixed primes become parameter-free definable in the **expanded two-sorted threshold structure**; this should not be worded as a statement about pure Skolem arithmetic `(N_{>0},×,1)`, where prime permutations are a basic symmetry.

## 4. Literature / priority audit required

A preliminary external search confirms that the source sort belongs to the established model theory of Skolem arithmetic and that definability/automorphism questions in `(N,·)` are classical. Relevant starting points include:

- A. Stonestrom, *Some model theory of Th(N,·)*, Mathematical Logic Quarterly 68 (2022), 288–303, DOI `10.1002/malq.202100049`;
- A. Mostowski, *On direct products of theories*, Journal of Symbolic Logic 17 (1952), 1–31;
- the broader literature on definability of valuations and valued structures.

No exact prior theorem matching the present anchored threshold-profile rigidity statement was located in the preliminary search, but absence from a quick search is not a novelty proof.

A dedicated literature audit should therefore test at least:

1. expansions of Skolem arithmetic by valuation predicates indexed by primes;
2. multi-sorted structures coupling `(N,×)` to `(Q,+)` by valuation relations;
3. definability of individual primes after adding valuation/bridge predicates;
4. classification of additive-Q scaling automorphisms in such expansions;
5. continuum families of inequivalent complete theories obtained by predicate-profile coding.

Novelty should be claimed only for the exact combined structure and theorem package that survives this comparison.

## 5. Dependency audit

The statement that all `{1,2}` full-support profiles lie in the same GIR-infinite / finite-graph-universal / undecidable macroscopic phase depends on the previously published Support-Cardinality Valuation Wall result.

The final paper must cite that publication explicitly by title and DOI and clearly mark this as an imported theorem. Threshold Spectrum Rigidity itself is elementary and does not depend on the residual-Galois machinery of the wall theorem.

## 6. Publication recommendation

### Mathematical status

**PASS / publication-worthy.** There is enough original-looking, coherent material for a separate paper centered on:

- exact pointwise recovery of threshold profiles from complete theory;
- continuum spectral refinement inside one coarse support-cardinality phase;
- the contrast between unanchored finite-shift gauge equivalence and anchored bridge rigidity.

### Archival status

**NOT YET ZENODO-READY.** Before release:

1. perform a dedicated literature/novelty audit;
2. consolidate `THRESHOLD_SPECTRUM_RIGIDITY.md` and `FULL_PROOF.md` into one canonical manuscript;
3. add explicit references and dependency DOI(s);
4. carry out a claim-language audit, especially around “parameter-free definability of primes” and “continuum spectrum”;
5. prepare synchronized EN/RU manuscripts;
6. render and visually verify PDF/DOCX;
7. add `README.md`, `CITATION.cff`, publication metadata, and optionally an author-response/audit record.

After these steps, the result should be released unless the literature audit finds a direct prior theorem subsuming the central statement.
