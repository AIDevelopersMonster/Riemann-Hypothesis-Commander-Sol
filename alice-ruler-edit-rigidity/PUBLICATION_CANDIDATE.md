# Alice Throws Away the Ruler III — PUBLICATION CANDIDATE

**Branch:** `research/alice-ruler-edit-rigidity`  
**Date:** 2026-09-13  
**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196

## Publication decision

**STATUS: PUBLICATION CANDIDATE — MATHEMATICS FROZEN FOR v1.0**

The branch has crossed the publication threshold. Article III should now be typeset from the two master manuscripts without expanding the theorem set.

### Master manuscripts

- English: `paper/ALICE_RULER_III_EN.md`
  - commit: `ec4cae091e82d57cbc1b42f48b96d89c31647943`
- Russian: `paper/ALICE_RULER_III_RU.md`
  - commit: `7fcfb1247e7079555374d940d4f4ac096a566c80`

### Publication-audited constructive theorem

The rank-2 Fano fiberization note was re-audited before manuscript assembly.

Corrected note:

`notes/PROJECTIVE_RANK2_FANO_FIBERIZATION.md`

Audit commit:

`6edd9b419283b18243d6a587bac77496e324dd28`

The first draft used a one-sided contamination definition in the proof of the fiber-affine law. The publication version symmetrizes the two input orientations. The theorem survives unchanged in form and linear scale, but the safe explicit bound is

```math
\boxed{|Z|<40(1-\rho_P)v^2}
```

rather than the preliminary constant `20`.

All publication text uses `40`.

## Frozen v1.0 theorem set

The publication may claim the following proved results.

1. Exact three-associator certificate for a P-phase root.
2. Explicit D-phase counterexample with all six root permutations associative.
3. Quantitative equivalence between P-phase impurity and Steiner-loop associativity defect.
4. Ultra-low same-carrier projective edit rigidity from Drápal's theorem.
5. Robust Boolean recovery from sufficiently close group tables.
6. Explicit Add-4 wrong-order sequence with `rho_P -> 1`.
7. Sharp `Theta(1/v)` scale for exact projective order rigidity, up to absolute constants.
8. Exact blockwise Pasch-deficit localization of associator failure.
9. Exact relation `s=4c14` with the classical `C14` configuration count.
10. Impossibility of vanishing-error reconstruction on the same carrier and on `(1+o(1))` supercarriers for all points.
11. Cross-order partial-core projective cost `D_pc` extending same-order block edit distance.
12. Universal linear converse `D_pc >= (1-rho_P)/(12+o(1))` in the small-distance regime.
13. Exact Add-4 partial-core cost.
14. Exact direct-product associator and partial-core benchmark formulas.
15. Exact Fano count `F(S)=rho_P N/28`.
16. Exact global Fano-extension defect sum.
17. Exact translation commutator identity.
18. Rank-2 Fano fiberization after deleting at most `2(1-rho_P)(v-3)` points.
19. Exact `H`-affine multiplication on every clean fiber pair.
20. Publication-audited contamination bound `<40(1-rho_P)v^2`.
21. Almost-medial bound `M_med <= 5(v+1)s`.

## Explicitly OPEN — do not state as theorem

The following remains conjectural and must be labelled as such:

```math
D_{pc}(S,\mathcal P)
\le C(1-\rho_P)
```

for sufficiently small phase impurity, with `C` absolute.

Equivalent research bottleneck: uniform quotient completion/repair for the almost-Steiner multiplication induced on the Fano-fiber quotient.

No claim should be made that current Latin-square removal or almost-commuting-permutation stability literature closes this step.

## Article architecture for v1.0

1. Motivation from Article II.
2. Steiner-loop associator bridge.
3. Ultra-low exact rigidity.
4. Wrong-order obstruction and sharp `1/v` scale.
5. Pasch / `C14` defect geometry.
6. Failure of same-carrier and near-supercarrier reconstruction.
7. Partial-core cost and universal linear converse.
8. Add-4 and direct-product benchmarks.
9. Fano-extension defect.
10. Rank-2 Boolean fiberization.
11. Exact affine fiber interactions.
12. Quotient-completion barrier and linear conjecture.
13. Discussion and conclusion.

## Source discipline

External references used in v1.0 have been checked for the roles assigned to them:

- Drápal 1983 — almost-associative quasigroup estimates in the ultra-low regime;
- Grannell--Lovegrove 2013 — Add-4 / near-maxi-Pasch construction;
- Kozlik 2020 — associative triples and Pasch counts in Steiner loops;
- Gowers--Long 2020 — context for partial associativity, not used as the missing same-carrier theorem;
- Arzhantseva--Păunescu 2015 — fixed finite tuple permutation stability;
- Becker--Mosheiff 2021 — polynomial stability for abelian groups;
- Garbe--Hancock--Hladký--Sharifzadeh 2023 — Latin-square limits/removal boundary;
- Aryapoor 2013 — Steiner quasigroup direct products / Pasch context.

## Next publication operations

No new mathematics should be added before v1.0 unless an error is discovered in audit.

Next operations:

1. typeset English and Russian publication PDFs;
2. run numbering/equation/bibliography/DOI audit on both rendered versions;
3. ensure EN/RU theorem numbering matches;
4. add final repository README links;
5. prepare Zenodo metadata only after the rendered PDFs pass audit;
6. record the Zenodo DOI back into the branch and repository documentation.
