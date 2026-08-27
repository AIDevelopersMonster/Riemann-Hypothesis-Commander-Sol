# Prime-Successor Exact Zero/One Valuation Boundary

Research continuation of the Prime-Successor Algebra / Two Walls programme.

**Status:** release candidate v1.0 — mathematical and claim audit passed  
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

For

\[
\mathcal V_{\Delta,0}
=
\bigl((\mathbb N_{>0},\times,1),(\mathbb Q,+,0),U_\Delta,B_0\bigr),
\]

with

\[
B_0(r,x)\iff\operatorname{Prime}(r)\land v_r(x)\ge0,
\]

every parameter-free first-order formula on free prime atoms admits a finite formula-relative coloring of the prime tail under which all admissible color-preserving prime permutations preserve the formula.

Consequences:

\[
<_{\mathbb P},\operatorname{Succ}_{\mathbb P}
\notin\operatorname{Def}(\mathcal V_{\Delta,0}),
\]

and for every fixed isolator \(I\),

\[
\operatorname{GIR}(I)<\infty.
\]

The preceding depth-one paper proves a fixed isolator \(I_1\) with

\[
\operatorname{GIR}(I_1)=\infty.
\]

Therefore

\[
B_1\notin\operatorname{Def}(\mathcal V_{\Delta,0}).
\]

## Critical proof repair

A naive global permutation of the Prüfer components is false because

\[
C_{p^\infty}\not\cong C_{q^\infty}
\quad(p\ne q).
\]

The final proof uses a **Finite-Fragment Generic Local Transfer Lemma**: outside finitely many coefficient primes, each relevant nonzero fixed scalar is an automorphism of every local Prüfer group, giving the same pinned/free one-witness geometry at every generic place.

## Immediate predecessors

- Stationary Locality: https://doi.org/10.5281/zenodo.22110465
- One-Step Valuation Jump: https://doi.org/10.5281/zenodo.22116714

## DOI gate

The new DOI is intentionally omitted until Zenodo assigns the record. After assignment, update `README.md`, `release/CITATION.cff`, Zenodo metadata, checksums and the final deposit ZIP.
