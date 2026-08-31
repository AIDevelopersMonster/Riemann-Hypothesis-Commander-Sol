# FCOA-Z Shadow Reconstruction — Zenodo Publication Package v1.0

**Canonical DOI:** [10.5281/zenodo.22179357](https://doi.org/10.5281/zenodo.22179357)  
**Publication date:** 2026-08-30  
**Package assembled and QA-checked:** 2026-08-31  
**Status:** READY FOR ZENODO ARCHIVAL / DOI-SYNCHRONIZED  
**Foundation DOI:** [10.5281/zenodo.22169264](https://doi.org/10.5281/zenodo.22169264)

## Canonical title

**EN:** *Classical Algebra as a Resolution-Dependent Shadow of a One-Dimensional Partial Geometry: Collapse, Matrix Units, and Reconstruction in FCOA-Z*

**RU:** «Классическая алгебра как тень одномерной частичной геометрии с переменным разрешением: схлопывание, матричные единицы и реконструкция в FCOA-Z»

Author: **Alex Malachevsky**  
ORCID: **0009-0008-6009-3196**

## Complete upload set

The assembled Zenodo package contains:

1. `FCOA_Z_Shadow_Reconstruction_EN_v1.0.pdf` — final English PDF, 11 pages.
2. `FCOA_Z_Shadow_Reconstruction_RU_v1.0.pdf` — final Russian PDF, 12 pages.
3. `FCOA_Z_Shadow_Reconstruction_EN_v1.0.md` — English source.
4. `FCOA_Z_Shadow_Reconstruction_RU_v1.0.md` — Russian source.
5. `FCOA_Z_Shadow_Reconstruction_EN_v1.0.html` — standalone English HTML using MathML.
6. `FCOA_Z_Shadow_Reconstruction_RU_v1.0.html` — standalone Russian HTML using MathML.
7. `zenodo.json` — Zenodo metadata template.
8. `CITATION.cff` — citation metadata.
9. `SOURCE_PROVENANCE.md` — theorem/repository provenance.
10. `PREPUBLICATION_AUDIT.md` — mathematical, bibliographic, dimensional, and format audit.
11. `ZENODO_UPLOAD_CHECKLIST.md` — upload checklist.
12. `SHA256SUMS.txt` — file-level checksum manifest.
13. `README.md` — package description and theorem scope.

Complete archive:

`FCOA_Z_Shadow_Reconstruction_Zenodo_v1_0.zip`

Archive SHA-256:

`5970c62ca538654309cd77bf0a35953d67f5a6dda7242e8e308a762826ffbb48`

## QA state

- EN PDF: 11 pages, text-based, openable, unencrypted, non-XFA.
- RU PDF: 12 pages, text-based, openable, unencrypted, non-XFA.
- XeLaTeX + Unicode fonts used.
- Render QA performed at 160 dpi; representative first/middle/final pages inspected in both languages.
- No clipping, overlap, black boxes, or broken Cyrillic observed.
- `zenodo.json` parses successfully as JSON.
- `CITATION.cff` parses successfully as YAML.
- Standalone HTML uses MathML and no external mathematics CDN.
- ZIP archive passes `unzip -t` with no errors.

## Bibliography completion

The incomplete bibliography in the initial publication drafts was replaced by exact references, including:

- H. Brandt, *Mathematische Annalen* 96 (1927), 360–366.
- G. Abrams and G. Aranda Pino, *Journal of Algebra* 293(2) (2005), 319–334, DOI `10.1016/j.jalgebra.2005.07.028`.
- M. C. Iovanov and A. Sistko, Contemporary Mathematics 688 (2017), 113–124, DOI `10.1090/conm/688/13830`.
- FCOA-Z foundation DOI `10.5281/zenodo.22169264`.

## Dimensional firewall

The package freezes a strictly one-dimensional theorem layer:

\[
\boxed{c_{\mathrm{coord}}=0.}
\]

Matrix indices label operator source/target points on one line and are not a two-dimensional carrier.

## License note

The package deliberately does not override or guess the license. The canonical license is the one selected on the Zenodo record for DOI `10.5281/zenodo.22179357`.

## Publication boundary

This package freezes the one-dimensional Shadow Reconstruction theorem layer. It does not introduce E-output re-entry, a second independently iterable coordinate, Tannakian reconstruction, or a group-cohomological classification theorem.