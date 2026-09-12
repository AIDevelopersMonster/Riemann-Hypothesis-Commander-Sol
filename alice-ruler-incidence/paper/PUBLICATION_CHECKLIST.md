# Publication checklist — Alice Throws Away the Ruler II

Status: **publication manuscript assembled; pre-release audit required**  
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

## Bibliography audit required before release

Verify final metadata and DOI formatting for:

1. Danziger–Mendelsohn–Grannell–Griggs, *Five-line configurations in Steiner triple systems*, Utilitas Mathematica 49 (1996), 153–159.
2. Král'–Máčajová–Pór–Sereni, Canadian Journal of Mathematics 62(2) (2010), 355–381, DOI `10.4153/CJM-2010-021-9`.
3. Král'–Máčajová–Pór–Sereni technical report IUUK-CE-ITI 2007-352.
4. Král'–Máčajová–Pór–Sereni, ENDM 29 (2007), 17–21, DOI `10.1016/j.endm.2007.07.004`.
5. Teirlinck, Geometriae Dedicata 4 (1975), 39–44, DOI `10.1007/BF00147400`.
6. Grannell–Griggs–Mendelsohn, JCD 3(1) (1995), 51–59, DOI `10.1002/jcd.3180030107`.
7. Stinson–Wei, Discrete Mathematics 105 (1992), 207–219, DOI `10.1016/0012-365X(92)90143-4`.
8. Colbourn–Rosa, *Triple Systems*, OUP, 1999.

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
- [ ] line-by-line theorem/proof audit against proof note.
- [ ] verify all bibliography metadata/DOIs against primary pages.
- [ ] normalize notation (`S_7/S_9`, `C_A`, `r_7`, `alpha`, `rho_*`).
- [ ] ensure no claim of edit-distance stability remains.
- [ ] decide final version number (`v1.0` recommended for Article II).
- [ ] generate final EN PDF.
- [ ] generate final RU PDF.
- [ ] run PDF visual/layout audit.
- [ ] create Zenodo release metadata.
- [ ] after DOI issuance, insert DOI into both manuscript metadata blocks and repository status.

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
