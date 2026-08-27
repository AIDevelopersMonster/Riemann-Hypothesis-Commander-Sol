# Release Manifest — FCOA Admissibility Geometry

**Publication date:** 2026-08-27  
**Zenodo DOI:** 10.5281/zenodo.22129787  
**Persistent URL:** https://doi.org/10.5281/zenodo.22129787

## Canonical archival record

The Zenodo record is the canonical publication archive for the bilingual paper package and publication binaries.

## GitHub recovery scope

This repository companion restores the source-level mathematical and reproducibility materials that were missing from GitHub at publication time:

- `../README.md` — publication summary, DOI, branch map and claim discipline;
- `../MATHEMATICAL_CORE.md` — theorem-level M0/G1/G2 checkpoint;
- `../CITATION.cff` — citation metadata;
- `../../../demos/fcoa-domain-compilation/index.html` — standalone interactive demonstrator;
- `../../../experiments/fcoa-domain-compilation/verify_formulas.py` — exact finite-spectrum verifier.

## Audited mathematical checkpoints

The recovered companion records the following final audited formulas.

### M0 multiplication

\[
\operatorname{Aut}(\mathfrak M_N^\times)\cong S_{N-1}.
\]

\[
(EQ,NEQ,LEFT,RIGHT,NONE)
=
\bigl(4(N-1),0,N^2+2N-2,N^2+N-2,N^3+N^2-4N+9\bigr).
\]

### G1

For every binary relation \(A\subseteq G_N^2\),

\[
\operatorname{Aut}(\mathfrak M_N^\times,A)
\cong
\operatorname{Aut}(G_N,A).
\]

For the path skeletons:

\[
S_{N-1}\to C_2\to1.
\]

### G2

\[
P_i\otimes_1P_{i+1}=\Omega,
\qquad 2\le i<N,
\]

with reverse/non-adjacent generic cells undefined.

Then

\[
\operatorname{Aut}(\otimes_1)=1
\]

and directed adjacency is recoverable from definedness after erasing the external relation.

The exact Association Spectrum is

\[
(EQ,NEQ,LEFT,RIGHT,NONE)
=
\bigl(5N-6,0,N^2+3N-4,N^2+2N-4,N^3+N^2-7N+15\bigr).
\]

The commutation locus remains unchanged from M0, of size

\[
3(N-1).
\]

## Typed Domain Compilation

The canonical theorem-level formulation uses a singleton output sort \(O=\{\Omega\}\). For any relation \(A\subseteq G^2\), define

\[
x\star_A y=\Omega\iff A(x,y).
\]

Then

\[
\operatorname{Aut}(G,O;\star_A)
\cong
\operatorname{Aut}(G;A).
\]

The typed form includes the empty relation. A one-sorted formulation requires extra hypotheses when the operation range is empty.

## Publication/repository consistency note

The publication DOI was assigned before this GitHub companion was restored. This manifest therefore documents a repository recovery, not a revision of the mathematical publication. If a later Zenodo version is issued, the release folder should record the new DOI/version explicitly rather than silently replacing this checkpoint.
