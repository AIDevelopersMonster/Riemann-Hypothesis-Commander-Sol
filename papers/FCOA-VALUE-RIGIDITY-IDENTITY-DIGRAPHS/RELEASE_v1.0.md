# FCOA Value-Rigidity / Identity Digraphs — Release v1.0

**Release date:** 2026-08-29  
**Authors:** Alex Malachevsky · Commander Sol  
**Status:** mathematical content frozen; bilingual publication package built and QA-passed  
**Zenodo DOI:** pending assignment

## Publication titles

**EN:** *Reflections on Value-Rigidity with Commander Sol: Two Anonymous Outputs, Identity Digraphs, and Sparse Rigid Fibers*

**RU:** *Размышлизмы о ценностной жёсткости с Commander Sol: два анонимных выхода, identity-орграфы и разреженные жёсткие волокна*

## v1.0 mathematical core

1. One-Output Collapse: in the pure terminal-output category, `|O|=1` implies active-sort `VRI=1`.
2. Two-Output Maximum VRI: two anonymous terminal outputs suffice for the absolute maximum `VRI=n!` on `n` active points.
3. The sparsest maximally value-rigid two-output fiber is identified with the classical minimum-size identity-digraph extremal `m(n)`.
4. Exact finite threshold formula for `m(n)` in terms of identity oriented-tree counts.
5. Self-contained generating-function derivation of `a_k ~ c lambda^k k^(-5/2)`.
6. Second-order sparsity law with `L=log lambda=1.6580437722354153...`.
7. Explicit partial-layer phase oscillation; no universal bounded denominator constant `K_0` exists.
8. Reproducible exact calculator: `experiments/fcoa_identity_exact_m.py`.

## Publication discipline

Identity/asymmetric digraphs, minimum-size identity digraphs, identity oriented trees, distinguishing colorings, and the classical `Theta(n/log n)` scale are treated as prior art and are not claimed as discoveries of FCOA. Priority is not claimed for the historical precedence of the exact-threshold or phase-law refinements pending complete literature comparison.

## QA completed

- EN DOCX: 6 pages, rendered and visually inspected page-by-page.
- RU DOCX: 6 pages, rendered and visually inspected page-by-page.
- EN/RU PDFs: preflight PASS; openable, unencrypted, text PDFs.
- DOCX accessibility audit: zero high-severity findings.
- HTML exact calculator: JavaScript syntax PASS and exact values verified at `n=10`, `10^3`, `10^6`, `10^12`.
- Release ZIP: `unzip -t` PASS.
- SHA256 integrity manifest generated.

## Final artifact names

- `FCOA_Value_Rigidity_Identity_Digraphs_EN_v1.0.pdf`
- `FCOA_Value_Rigidity_Identity_Digraphs_EN_v1.0.docx`
- `FCOA_Value_Rigidity_Identity_Digraphs_RU_v1.0.pdf`
- `FCOA_Value_Rigidity_Identity_Digraphs_RU_v1.0.docx`
- `FCOA_Value_Rigidity_Demo_v1.0.html`
- `FCOA_Value_Rigidity_Identity_Digraphs_v1.0_release.zip`
- `ZENODO_METADATA_v1.0.txt`
- `SHA256SUMS.txt`

## Release gate

The only remaining external step is Zenodo deposit / DOI assignment. After the DOI is issued, insert it into both language versions, the HTML metadata, and this release note without changing theorem statements or proofs.
