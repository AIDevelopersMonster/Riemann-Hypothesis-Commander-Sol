# RH-SOL-01 · LATTICE

## Integer-Lattice Encoding of Riemann-Zeta Argand Loops: Persistence of Dirichlet Frequencies under Binary Geometric Quantization

**Status:** Published / canonical starting point of the RH-SOL series  
**Author:** Alex Malachevsky  
**ORCID:** https://orcid.org/0009-0008-6009-3196  
**Version:** v0.1.1  
**Published:** 2026-08-22  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22060296  
**Article license:** CC BY 4.0  
**Code license:** MIT

Series subtitle: **Reflections on the Riemann Hypothesis with Commander Sol: a human-AI computational note**.

## Research question

How much arithmetic spectral structure survives when the complex trajectory

`zeta(1/2 + i t)`

is reduced to consecutive Argand-loop domains and then to the binary statement that a Cartesian integer-lattice point lies inside or outside a loop?

For consecutive critical-line zeros `gamma_n < gamma_(n+1)`, the article studies

`H_n = { zeta(1/2 + i t) : t in [gamma_n, gamma_(n+1)] }`

and the binary lattice observable

`I(n,a,b) = 1[(a,b) in Interior(H_n)]`.

## Main reported findings

Across 10,000 loops, the double-centered binary tensor preserves a pronounced physical-frequency comb near `omega = log(m)`. After removing the principal `log(m)` dictionary, leading residual structure is consistent with nonlinear combinations such as `log(m/k)`. An even/odd cross-fit removal of a predeclared log-integer plus small-ratio dictionary reduces out-of-sample variance by about 36.3%.

Several attractive static arithmetic hypotheses did **not** survive controls: parity/mod-3/mod-5 structure was null-like, and an apparent von-Mangoldt correlation was not robust after controlling the central geometric peak.

The article also develops a local sampling interpretation of

`T_m = 2*pi*m^2`

and the reciprocal first-fold label

`m* = T/(2*pi*m)`.

This is presented as an aliasing/identifiability interpretation, **not** as a proof mechanism for the Riemann Hypothesis and not as a necessary amplitude-onset law.

## Repository contents

- [`ABSTRACT.md`](ABSTRACT.md) — compact abstract and contribution statement
- [`CLAIMS_AND_LIMITATIONS.md`](CLAIMS_AND_LIMITATIONS.md) — what the publication does and does not claim
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — data/code provenance and reproducibility status
- [`DEMO.md`](DEMO.md) — interactive-demo provenance and Zenodo source
- [`manuscript/`](manuscript/) — LaTeX source and bibliography metadata
- [`analysis/`](analysis/) — selected scripts, tables and technical notes from the deposited package
- [`figures/`](figures/) — figure inventory and checksums; binary originals remain canonical on Zenodo
- [`release/`](release/) — citation, licensing, AI disclosure and final DOI metadata
- [`../../reviews/RH-SOL-01-review-summary.md`](../../reviews/RH-SOL-01-review-summary.md) — post-publication review takeaways feeding later RH-SOL branches

## Canonical archive policy

The immutable publication record is Zenodo DOI **10.5281/zenodo.22060296**. GitHub mirrors the human-readable source, selected analysis materials and programme context. Large/redundant binary assets and the full analysis archive remain canonical on Zenodo rather than being duplicated in Git history.

## Post-publication status

RH-SOL-01 is not being silently rewritten after publication. Questions raised by review — formal interior conventions, actual-zero timing, shifted lattices, geometry/phase nulls and full upstream regeneration — are routed into RH-SOL-02 · SHIFT, RH-SOL-03 · REALZERO and RH-SOL-04 · FIREWALL.
