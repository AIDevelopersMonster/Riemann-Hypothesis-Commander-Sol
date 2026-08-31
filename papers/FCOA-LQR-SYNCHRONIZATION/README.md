# FCOA LQR Synchronization — publication package

**English title:** *Reflections on Point-Image Phase Synchronization with Commander Sol: Exact Costs, Cut-Space Packings, and a Sharp Stabilization Threshold in FCOA*  
**Russian title:** *Размышления о синхронизации фаз по образам точек с Commander Sol: Точные стоимости, упаковки пространств разрезов и точный порог стабилизации в FCOA*  
**Status:** release candidate / v1.0-rc1  
**Date:** 2026-08-31  
**Source line:** `delegated/FCOA_RIGIDITY_COST/QGE3/`

## Canonical FCOA foundation

This package follows the mandatory FCOA Foundation citation gate.

Foundation DOI: https://doi.org/10.5281/zenodo.22164246

Both language versions explicitly identify FCOA Definition 1.0 in the abstract and bibliography and state the carrier/sorts, derived primitive signature, erasure convention, recovery target, and arithmetic firewall.

## Main theorem package

The manuscript contains proofs of:

- `L_2(r)=r-1`;
- `L_3(r)=ceil(3(r-1)/2)`;
- `L_q(2)=q-1`;
- `L_q(3)=2q-3` for `q>=3`;
- the complete exact four-phase column

  `L_q(4)=3` for `q=2`, `2q-1` for `3<=q<=5`, `12` for `q=6`, and `3q-7` for `q>=7`;

- the universal binary-cut synchronization gadget;
- the cut-space packing lower bound;
- the exact stabilization theorem

  `L_q(r)=(r-1)q-(2^(r-1)-1)` for `q>=2^(r-1)-1`;

- exactness of the stabilization threshold `q_0(r)=2^(r-1)-1`.

The unresolved sector is explicitly restricted to

`4 <= q < 2^(r-1)-1`, `r>=5`.

## Files

- `article_en.md` — English release-candidate manuscript.
- `article_ru.md` — Russian release-candidate manuscript with synchronized theorem/formula numbering.
- `CITATION.cff` — citation metadata; DOI intentionally omitted until an actual Zenodo release is minted.
- `metadata.json` — release metadata for archival preparation.
- `SOURCE_MAP.md` — theorem-to-source and verifier map.
- `PRE_RELEASE_AUDIT.md` — publication gate and remaining release-only actions.

Research proofs and hostile-audit sources remain in `delegated/FCOA_RIGIDITY_COST/QGE3/`.

## Claim firewall

The package may claim the FCOA/LQR-specific chain

`point-image constraints -> transversal unique-coloring quotient -> component partitions -> canonical binary cut spaces -> sharp LQR stabilization`.

It must not claim discovery of:

- unique colorability or pairwise color-class connectivity;
- partial spreads, vector-space partitions, or pairwise trivially intersecting subspaces;
- the nonzero-vector packing count itself;
- general permutation synchronization.

The dedicated literature audit supports only a conservative claim that the exact extremal parameter `L_q(r)` in this same-source point-image form was not located in the searched literature.

## Release gates

- [x] Mathematical hostile audit completed.
- [x] Literature/priority audit completed.
- [x] English manuscript assembled.
- [x] Russian manuscript assembled with matching theorem/formula structure.
- [x] Foundation DOI present in both abstracts and bibliographies.
- [x] Exact theorem/open-problem boundary stated.
- [x] Reproducibility scripts identified.
- [x] Citation and release metadata prepared without inventing a DOI.
- [ ] Final PDF/DOCX render and visual QA.
- [ ] Actual Zenodo DOI minted.
- [ ] DOI propagated into `CITATION.cff`, metadata, manuscripts and repository README after release.

No DOI is to be guessed or prefilled before Zenodo assigns it.
