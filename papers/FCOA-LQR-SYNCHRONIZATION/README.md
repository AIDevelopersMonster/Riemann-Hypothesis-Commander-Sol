# FCOA LQR Synchronization — publication package

**English title:** *Reflections on Point-Image Phase Synchronization with Commander Sol: Exact Costs, Cut-Space Packings, and a Sharp Stabilization Threshold in FCOA*  
**Russian title:** *Размышления о синхронизации фаз по образам точек с Commander Sol: Точные стоимости, упаковки пространств разрезов и точный порог стабилизации в FCOA*  
**Status:** complete release candidate / v1.0-rc1  
**Package date:** 2026-09-01  
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
- the complete exact four-phase column:

  `L_q(4)=3` for `q=2`, `2q-1` for `3<=q<=5`, `12` for `q=6`, and `3q-7` for `q>=7`;

- the universal binary-cut synchronization gadget;
- the cut-space packing lower bound;
- the exact stabilization theorem

  `L_q(r)=(r-1)q-(2^(r-1)-1)` for `q>=2^(r-1)-1`;

- exactness of the stabilization threshold `q_0(r)=2^(r-1)-1`.

The unresolved sector is explicitly restricted to

`4 <= q < 2^(r-1)-1`, `r>=5`.

## Human-authored package files

- `article_en.md` — English manuscript.
- `article_ru.md` — Russian manuscript with synchronized theorem/formula numbering.
- `CITATION.cff` — citation metadata; archival DOI intentionally omitted until Zenodo minting.
- `metadata.json` — canonical internal release metadata.
- `ZENODO_METADATA.json` — Zenodo-ready upload metadata.
- `RELEASE_NOTES.md` — archival release notes and theorem summary.
- `SOURCE_MAP.md` — theorem-to-source and verifier map.
- `PRE_RELEASE_AUDIT.md` — publication gate.

## Generated publication artifacts

GitHub Actions workflow `.github/workflows/fcoa-lqr-publication-build.yml` reproducibly generates under `artifacts/`:

- `article_en.docx`, `article_ru.docx`;
- `article_en.pdf`, `article_ru.pdf`;
- `article_en.html`, `article_ru.html`;
- `article_en.tex`, `article_ru.tex`;
- source Markdown copies;
- citation/Zenodo metadata and release notes;
- theorem provenance files;
- `verify_lqr.py`, `verify_lqr_cutspace.py`;
- `VERIFICATION_LOG.txt` containing fresh verifier output;
- PDF preflight information and first-page render smoke tests;
- `MANIFEST.sha256` covering generated package files.

The workflow also assembles:

`FCOA-LQR-SYNCHRONIZATION-v1.0-rc1.zip`

for one-file archival upload or local inspection.

## Reproducibility

The generated artifacts are not treated as hand-edited sources. They are rebuilt from the versioned Markdown manuscripts and theorem-source files. The exact finite verifiers are executed during every publication build before generated files are committed.

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

## Zenodo upload set

Recommended public files for the archival record:

1. `article_en.pdf` — primary English article;
2. `article_ru.pdf` — complete Russian version;
3. `article_en.docx` and `article_ru.docx` — editable publication copies;
4. `article_en.html` and `article_ru.html` — browser-readable copies;
5. `FCOA-LQR-SYNCHRONIZATION-v1.0-rc1.zip` — complete reproducibility bundle.

The `.tex`, source Markdown, theorem provenance, scripts, verification log and checksum manifest are included inside the ZIP and remain available in GitHub.

## Release gates

- [x] Mathematical hostile audit completed.
- [x] Literature/priority audit completed.
- [x] English manuscript assembled.
- [x] Russian manuscript assembled with matching theorem/formula structure.
- [x] Foundation DOI present in both abstracts and bibliographies.
- [x] Exact theorem/open-problem boundary stated.
- [x] Citation metadata prepared.
- [x] Zenodo-ready metadata prepared.
- [x] Release notes prepared.
- [x] Reproducible build workflow prepared.
- [x] Automated verifier execution included in release build.
- [x] SHA-256 manifest included in release build.
- [ ] Actual Zenodo DOI minted.
- [ ] New DOI propagated into `CITATION.cff`, metadata, manuscripts, README and upstream publication index after minting.

No DOI is to be guessed or prefilled before Zenodo assigns it.
