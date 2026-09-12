# Publication checklist — Alice Throws Away the Ruler II

Status: **mathematical proof audit passed; manuscript synchronization and release QA remain**  
Date: 2026-09-12

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

- Král anti-mitre `C_A` is configuration #4:
  `012,034,135,236,457`;
- mirror residual is configuration #7:
  `012,034,135,246,567`;
- they are non-isomorphic;
- classical five-line formulas imply exactly
  `c_A = 2 r_7`;
- therefore the completion coordinate remains valid as a zero-defect coordinate:
  `alpha = r_7/(6P(v)) = c_A/(12P(v))`;
- hence `alpha=0 iff c_A=0`.

Any future consolidated version of Article I must carry this correction explicitly.

## Main theorem to advertise

For an STS(v), phase each independent triple by the subsystem it generates:

- `P`: `S_7`;
- `H`: `S_9`;
- `D`: neither.

Let `rho_P,rho_H` be the two pure phase densities, let `c_A` be the anti-mitre count, and

`N=v(v-1)(v-3)/6`.

Then there is an absolute constant `C` such that

`min(rho_P,rho_H) <= C c_A/N`.

Equivalent completion-coordinate form:

`min(rho_P,rho_H) <= C_alpha alpha`.

**Claim discipline:** call this **phase-profile stability**. Do not call it edit-distance stability, structural reconstruction, removal lemma, or closeness of the full block set to a projective/Hall STS.

## Publication-core ingredients

New deductions to foreground:

1. independent-triple phase graph;
2. Laplacian gap `mu_2 >= v-3` from Johnson interlacing;
3. phase isoperimetry
   `(v-3)q(1-q/N) <= s+3(v-4)|D|`;
4. root-preserving anti-mitre witness;
5. bulk bound `|D|<=56 c_A`;
6. localized finite phase-interface witness;
7. interface bound `s<=C_I v|D|`;
8. quantitative Hall/projective phase stability.

Classical/source-derived ingredients must be identified as such.

## Mathematical proof audit — PASSED 2026-09-12

The publication-core proof note was line-by-line hardened in commit
`5c8fc288973fe77ca9ee1d8f65dc83e9a21815ab`.

The audit closed the following reviewer-sensitive points:

1. **Explicit anti-mitre identification.** The three representative five-block failure witnesses in the bulk-charging lemma now have explicit incidence-preserving relabellings to canonical
   `C_A = 012,034,135,236,457`.
2. **Fano two-colour lemma.** The claim that every red/blue colouring of the seven Fano lines has a monochromatic pencil is now proved directly rather than called merely elementary.
3. **No Fano subsystem in `S_9`.** A direct proof is included: a Steiner subsystem of `AG(2,3)` is, after translation, an additive subgroup of `F_3^2`, so its size is only `1,3,9`, never `7`.
4. **Localized use of the 2007 finite proof.** The single place where the source proof uses four-point independence is isolated. If the exceptional triple `d_A,d_B,d_C` is a block, `{A,B,d}` is immediately a `D` root; otherwise the source red-star argument proceeds unchanged. The blue-star branch needs no stronger assumption.
5. **Query-template audit.** All phase queries used by the finite proof fall into the four reconstruction classes
   `{d,u,v}`, `{d_x,u,v}`, `{u,d_x,d_y}`, `{d_x,d_y,d_z}`.
6. **Reverse multiplicity.** Each reconstruction class has `O(v)` reverse fiber; together with at most `84` `P/H` edges per mixed `(F,d)` pair this gives `s<=C_I v|D|`.
7. **Constant normalization.** The theorem is recorded consistently as
   `min(rho_P,rho_H) <= C c_A/N`, with `c_A/N=3 alpha`.
8. **Zero-defect conclusion.** The all-`P`/all-`H` phase conclusion is separated from the classical final identification as projective/Hall.

**Audit verdict:** no unresolved logical step remains in the proof chain currently used for the main theorem. This is a mathematical-proof verdict, not yet a release/layout verdict.

## Bibliography audit

Verified/anchored during the proof audit:

1. P. Danziger, E. Mendelsohn, M. J. Grannell, T. S. Griggs, *Five-Line Configurations in Steiner Triple Systems*, *Utilitas Mathematica* **49** (1996), 153–159. Primary PDF inspected for configurations #4 and #7 and their count formulas.
2. D. Král', E. Máčajová, A. Pór, J.-S. Sereni, *Characterisation Results for Steiner Triple Systems and Their Application to Edge-Colourings of Cubic Graphs*, *Canadian Journal of Mathematics* **62**(2) (2010), 355–381, DOI `10.4153/CJM-2010-021-9`.
3. D. Král', E. Máčajová, A. Pór, J.-S. Sereni, *Characterization Results for Steiner Triple Systems and Their Application to Edge-Colorings of Cubic Graphs*, technical report IUUK-CE-ITI 2007-352. Primary report inspected for the finite phase-purity proof and Figures 6–10.
4. D. Král', E. Máčajová, A. Pór, J.-S. Sereni, *Characterization of affine Steiner triple systems and Hall triple systems*, *Electronic Notes in Discrete Mathematics* **29** (2007), 17–21, DOI `10.1016/j.endm.2007.07.004`.
5. L. Teirlinck, *On linear spaces in which every plane is either projective or affine*, *Geometriae Dedicata* **4** (1975), 39–44, DOI `10.1007/BF00147400`.

Still to normalize against final publisher/catalogue metadata before release:

6. M. J. Grannell, T. S. Griggs, E. Mendelsohn, *A small basis for four-line configurations in Steiner triple systems*, *Journal of Combinatorial Designs* **3**(1) (1995), 51–59, DOI `10.1002/jcd.3180030107`.
7. D. R. Stinson, Y. J. Wei, *Some results on quadrilaterals in Steiner triple systems*, *Discrete Mathematics* **105** (1992), 207–219, DOI `10.1016/0012-365X(92)90143-4`.
8. C. J. Colbourn, A. Rosa, *Triple Systems*, Oxford University Press, New York, 1999.

## Priority-search boundary

Search through 2026-09-12 found no equivalent theorem under combinations of:

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
- [x] line-by-line theorem/proof audit against proof note.
- [x] explicit `C_A` witness isomorphisms added to proof note.
- [x] Fano two-colour pencil lemma proved.
- [x] `S_9` contains no `S_7` lemma proved.
- [x] localized source-proof dependency audited.
- [x] query-template/reverse-fiber audit completed.
- [ ] synchronize the strengthened proof text into EN manuscript.
- [ ] synchronize the strengthened proof text into RU manuscript.
- [ ] finish bibliography metadata normalization for refs. 6–8.
- [ ] normalize notation (`S_7/S_9`, `C_A`, `r_7`, `alpha`, `rho_*`) across EN/RU.
- [x] ensure no theorem-level claim of edit-distance stability remains in the proof core.
- [x] final version number chosen: `v1.0` for Article II.
- [ ] generate final EN PDF.
- [ ] generate final RU PDF.
- [ ] run PDF visual/layout audit.
- [ ] create final Zenodo release metadata.
- [ ] after DOI issuance, insert DOI into both manuscript metadata blocks and repository status.

## Publication threshold decision

**Mathematical threshold: crossed.** The main theorem is now sufficiently closed to proceed to publication hardening; I do not see a remaining proof obligation that should block preparation of the final preprint.

**Release threshold: not yet crossed.** Do not upload to Zenodo until the strengthened proof is mirrored into both language manuscripts, remaining bibliography metadata is normalized, and both final PDFs pass visual QA.

## Zenodo metadata draft

**Title:** Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects

**Creators:** Malachevsky, A.A. — ORCID 0009-0008-6009-3196

**Publication date:** 2026-09-12 (adjust to actual upload date if later)

**Resource type:** Preprint

**Language:** English primary; Russian parallel version included

**Keywords:**

- Steiner triple systems
- Hall triple systems
- projective Steiner triple systems
- anti-mitre
- stability
- phase rigidity
- Johnson graph
- spectral expansion
- forbidden configurations
- incidence geometry

**Description:**

We introduce a phase graph on noncollinear triples of a Steiner triple system, distinguishing projective `S_7`, Hall `S_9`, and defective local closure types. Spectral expansion of the independent-triple graph, combined with anti-mitre witness charging and a localized finite phase-interface argument, yields a quantitative Hall/projective phase-profile stability theorem: the minority pure phase is bounded linearly by the normalized anti-mitre count. The zero-defect case recovers the exact projective/Hall dichotomy. The result concerns phase-profile stability and does not assert edit-distance proximity of the full block set.
