# Prime-Successor Exact Zero/One Valuation Boundary

Research continuation of the Prime-Successor Algebra / Two Walls programme.

**Status:** release candidate v1.0 — mathematical, adversarial, DOCX and PDF QA passed  
**Date:** 2026-08-27  
**Zenodo DOI:** pending assignment

## Publication title

**English**  
*Reflections on the Exact Zero/One Valuation Boundary with Commander Sol: Uniform Zero-Depth Compression versus Residual-Cubic Grid Amplification*

**Russian**  
*Размышлизмы о точной границе нулевой и единичной валюационной глубины с Commander Sol: Uniform Zero-Depth Compression против Residual-Cubic Grid Amplification*

**Author:** Alex Malachevsky  
**ORCID:** 0009-0008-6009-3196

## Main theorem

For the Ramanujan bridge

\[
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}},
\]

consider the uniformly indexed zero-depth predicate

\[
B_0(r,x)\iff \operatorname{Prime}(r)\land v_r(x)\ge0.
\]

For every parameter-free first-order formula with free source variables restricted to prime atoms, there is a finite formula-relative exceptional set and a finite color partition of the regular prime tail such that every admissible color-preserving prime permutation preserves the formula.

Consequences:

\[
<_{\mathbb P},\operatorname{Succ}_{\mathbb P}
\notin\operatorname{Def}(\mathcal V_{\Delta,0}),
\]

and for every fixed ternary isolator \(I\),

\[
\operatorname{GIR}(I)<\infty.
\]

The immediately preceding depth-one paper proves that for

\[
B_1(r,x)\iff \operatorname{Prime}(r)\land v_r(x)\ge1,
\]

there exists a fixed isolator \(I_1\) with

\[
\operatorname{GIR}(I_1)=\infty.
\]

Therefore

\[
\boxed{
B_0:\forall I\,\operatorname{GIR}(I)<\infty
\quad\Big|\quad
B_1:\exists I_1\,\operatorname{GIR}(I_1)=\infty,
}
\]

and \(B_1\) is not definable in the depth-zero structure.

## Proof architecture

1. Private denominator geometry of regular Ramanujan labels.
2. Primary decomposition \(\mathbb Q/\mathbb Z\cong\bigoplus_p C_{p^\infty}\).
3. Finite-Fragment Generic Local Transfer outside a formula-relative coefficient-prime set.
4. Finite stationary exceptional atlas.
5. External-support exact anchoring and bounded-anchor affine traces.
6. Integer-translation kernel blindness of \(B_0\).
7. Bridge-pinned / exact-scheme-pinned / free target witness transport.
8. Full finite-fragment source/target back-and-forth.
9. Formula-Relative Tail Symmetry, non-definability of order/successor, finite GIR.
10. Strict separation from the published depth-one infinite-GIR theorem.

The theorem-level checkpoint is [`THEOREM_ZERO_DEPTH_COMPRESSION.md`](THEOREM_ZERO_DEPTH_COMPRESSION.md).

## Immediate predecessor

*Reflections on a One-Step Valuation Jump with Commander Sol: From Private Denominator Support to Residual-Cubic Grid Amplification*  
Zenodo DOI: **10.5281/zenodo.22116714**  
https://doi.org/10.5281/zenodo.22116714

The earlier Stationary Locality theorem is published at DOI **10.5281/zenodo.22110465**.

## Package contents

- `manuscript/article_en.md` — English canonical manuscript.
- `manuscript/article_ru.md` — Russian canonical manuscript.
- `THEOREM_ZERO_DEPTH_COMPRESSION.md` — theorem-level proof checkpoint.
- `CLAIM_AUDIT.md` — publication claim audit.
- `FINAL_LINE_BY_LINE_AUDIT.md` — adversarial proof and release audit.
- `LITERATURE_AUDIT.md` — literature and priority-discipline note.
- `references.bib` — bibliography data.
- `verification/` — finite sanity checks.
- `demo/index.html` — standalone conceptual comparison page.
- `release/` — publication metadata, manifest and checksums; DOCX/PDF binaries are carried in the Zenodo deposit package.

## DOI gate

The new DOI is intentionally omitted until Zenodo assigns it. After assignment, update README, `release/CITATION.cff`, Zenodo metadata, checksums and the deposit archive. No mathematical content needs to be changed merely to insert the DOI.
