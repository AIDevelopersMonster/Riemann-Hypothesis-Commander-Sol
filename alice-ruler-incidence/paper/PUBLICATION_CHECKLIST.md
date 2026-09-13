# Publication checklist — Alice Throws Away the Ruler II

Status: **mathematical and manuscript audit passed; final PDF/Zenodo release QA remains**  
Date: 2026-09-13

## Canonical title

**EN:** *Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects*  
Series subtitle: *Alice Throws Away the Ruler II*

**RU:** *Фазовая жёсткость в системах троек Штейнера: количественная устойчивость Холл–проективной дихотомии через anti-mitre-дефекты*  
Серия: *Алиса выбрасывает линейку II*

## Author metadata

- EN/Zenodo: **Malachevsky, A.A.**
- RU: **Малачевский А.А.**
- ORCID: **0009-0008-6009-3196**

## Canonical manuscript files

- `paper/PHASE_RIGIDITY_EN.md`
- `paper/PHASE_RIGIDITY_RU.md`
- proof source: `proofs/PHASE_STABILITY_PROOF.md`
- research state: `STATUS.md`

## Mandatory correction to research seed v0.6

The following statement in v0.6 must **not** survive unchanged:

> the mirror-completion residual configuration `012,034,135,246,567` is the anti-mitre `C_A` of Král et al.

Correct statement:

- Král anti-mitre `C_A` is configuration #4: `012,034,135,236,457`;
- mirror residual is configuration #7: `012,034,135,246,567`;
- they are non-isomorphic;
- classical five-line formulas imply `c_A=2r_7`;
- `alpha=r_7/(6P(v))=c_A/(12P(v))`;
- hence `alpha=0 iff c_A=0`.

Any future consolidated version of Article I must carry this correction explicitly.

## Main theorem to advertise

For an `STS(v)`, phase each independent triple by the subsystem it generates:

- `P`: `S_7`;
- `H`: `S_9`;
- `D`: neither.

Let `rho_P,rho_H` be the pure phase densities, `c_A` the anti-mitre count, and `N=v(v-1)(v-3)/6`. Then there is an absolute constant `C` such that

`min(rho_P,rho_H) <= C c_A/N`.

Equivalent completion-coordinate form:

`min(rho_P,rho_H) <= C_alpha alpha`.

**Claim discipline:** call this **phase-profile stability**. Do not call it edit-distance stability, structural reconstruction, removal lemma, or closeness of the full block set to a projective/Hall STS.

## Publication-core ingredients

1. independent-triple phase graph;
2. Laplacian gap `mu_2>=v-3` from Johnson interlacing;
3. phase isoperimetry `(v-3)q(1-q/N)<=s+3(v-4)|D|`;
4. root-preserving anti-mitre witness;
5. bulk bound `|D|<=56c_A`;
6. localized finite phase-interface witness;
7. interface bound `s<=C_Iv|D|`;
8. quantitative Hall/projective phase stability.

Classical/source-derived ingredients are separated explicitly from the new quantitative layer.

## Mathematical proof audit — PASSED

The publication-core proof note was hardened in commit `5c8fc288973fe77ca9ee1d8f65dc83e9a21815ab`.

Closed reviewer-sensitive points:

1. explicit incidence-preserving relabellings of all three representative five-block failure witnesses to canonical `C_A=012,034,135,236,457`;
2. direct proof of the Fano two-colour monochromatic-pencil lemma;
3. direct proof that `S_9=AG(2,3)` contains no `S_7` subsystem;
4. localization of the only four-point-independence dependency in the 2007 finite proof;
5. exhaustive reduction of phase queries to four reconstruction classes;
6. `O(v)` reverse-fiber bound for every class;
7. consistent normalization of the final theorem and `c_A/N=3alpha`;
8. separation of the quantitative all-`P`/all-`H` phase conclusion from the classical projective/Hall identification.

**Verdict:** no unresolved logical step remains in the proof chain currently used for the main theorem.

## Manuscript synchronization — PASSED 2026-09-13

The strengthened proof has now been mirrored theorem-by-theorem into both publication manuscripts.

- EN hardened commit: `0776be3ba435e66ed467f4756a0380bdf93b2301`.
- RU hardened commit: `711447a056e1e15e94d9d8bbce49c7c076d502b4`.

Both versions now include:

- explicit `C_A` relabelling audit;
- Fano two-colour pencil lemma;
- `S_9`-contains-no-`S_7` lemma;
- localized interface proof with the four reconstruction classes;
- the same theorem numbering and constant normalization;
- explicit classical citation boundary in the zero-defect corollary;
- a terminology warning distinguishing the named configuration `C_A` from older usage of “anti-mitre STS” for a system containing no mitre;
- explicit statement that no edit-distance theorem is claimed.

## Bibliography audit — PASSED 2026-09-13

Final metadata used in both manuscripts:

1. P. Danziger, E. Mendelsohn, M. J. Grannell, T. S. Griggs, *Five-line configurations in Steiner triple systems*, *Utilitas Mathematica* **49** (1996), 153–159. Primary paper inspected for configurations #4/#7 and count formulas.
2. D. Král', E. Máčajová, A. Pór, J.-S. Sereni, *Characterisation Results for Steiner Triple Systems and Their Application to Edge-Colourings of Cubic Graphs*, *Canadian Journal of Mathematics* **62**(2) (2010), 355–381. DOI `10.4153/CJM-2010-021-9`.
3. D. Král', E. Máčajová, A. Pór, J.-S. Sereni, *Characterization Results for Steiner Triple Systems and Their Application to Edge-Colorings of Cubic Graphs*, technical report IUUK-CE-ITI 2007-352 (2007). Primary report inspected for the finite phase-purity proof.
4. D. Král', E. Máčajová, A. Pór, J.-S. Sereni, *Characterization of affine Steiner triple systems and Hall triple systems*, *Electronic Notes in Discrete Mathematics* **29** (2007), 17–21. DOI `10.1016/j.endm.2007.07.004`.
5. L. Teirlinck, *On linear spaces in which every plane is either projective or affine*, *Geometriae Dedicata* **4** (1975), 39–44. DOI `10.1007/BF00147400`.
6. M. J. Grannell, T. S. Griggs, E. Mendelsohn, *A small basis for four-line configurations in Steiner triple systems*, *Journal of Combinatorial Designs* **3**(1) (1995), 51–59. DOI `10.1002/jcd.3180030107`.
7. D. R. Stinson, Y. J. Wei, *Some results on quadrilaterals in Steiner triple systems*, *Discrete Mathematics* **105** (1992), 207–219. DOI `10.1016/0012-365X(92)90143-4`.
8. C. J. Colbourn, A. Rosa, *Triple Systems*, Oxford University Press, 1999. DOI `10.1093/oso/9780198535768.001.0001`. Print ISBN `9780198535768`.

## Priority-search boundary

Search updated through 2026-09-13 found no equivalent theorem under combinations of:

- Hall triple system stability;
- projective/Hall Steiner stability;
- anti-mitre supersaturation;
- Steiner quasigroup stability/removal;
- phase graph;
- quantitative Hall/projective dichotomy.

This is evidence only, not a formal guarantee of priority.

## Pre-Zenodo release checklist

- [x] EN manuscript assembled.
- [x] RU manuscript assembled.
- [x] proof note isolated.
- [x] v0.6 configuration-identification correction recorded.
- [x] novelty boundary recorded.
- [x] line-by-line theorem/proof audit.
- [x] explicit `C_A` witness isomorphisms.
- [x] Fano two-colour pencil lemma.
- [x] `S_9` contains no `S_7` lemma.
- [x] localized source-proof dependency audit.
- [x] query-template/reverse-fiber audit.
- [x] strengthened proof synchronized into EN manuscript.
- [x] strengthened proof synchronized into RU manuscript.
- [x] bibliography metadata normalized for refs. 1–8.
- [x] notation normalized (`S_7/S_9`, `C_A`, `r_7`, `alpha`, `rho_*`) across EN/RU.
- [x] no theorem-level edit-distance overclaim remains.
- [x] final version number chosen: `v1.0` for Article II.
- [ ] generate final EN PDF.
- [ ] generate final RU PDF.
- [ ] run PDF visual/layout audit.
- [ ] create final Zenodo release metadata/package.
- [ ] after DOI issuance, insert DOI into both manuscript metadata blocks and repository status.

## Publication threshold decision

**Mathematical threshold: crossed.**  
**Manuscript threshold: crossed.**  
**Release threshold:** only final PDF generation/visual QA and Zenodo packaging remain.

There is no longer a scientific reason to delay typesetting the final preprint.

## Zenodo metadata draft

**Title:** Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects

**Creator:** Malachevsky, A.A. — ORCID 0009-0008-6009-3196

**Publication date:** use actual upload date.

**Resource type:** Preprint

**Language:** English primary; Russian parallel version included

**Keywords:** Steiner triple systems; Hall triple systems; projective Steiner triple systems; anti-mitre; stability; phase rigidity; Johnson graph; spectral expansion; forbidden configurations; incidence geometry.

**Description:** We introduce a phase graph on noncollinear triples of a Steiner triple system, distinguishing projective `S_7`, Hall `S_9`, and defective local closure types. Spectral expansion of the independent-triple graph, combined with anti-mitre witness charging and a localized finite phase-interface argument, yields a quantitative Hall/projective phase-profile stability theorem: the minority pure phase is bounded linearly by the normalized anti-mitre count. The zero-defect case recovers the exact projective/Hall dichotomy. The result concerns phase-profile stability and does not assert edit-distance proximity of the full block set.