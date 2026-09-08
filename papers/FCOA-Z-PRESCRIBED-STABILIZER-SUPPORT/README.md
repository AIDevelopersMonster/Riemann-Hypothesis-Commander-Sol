# FCOA-Z — Prescribed-Stabilizer Support

## Publication

**English:** *Prescribed-Stabilizer Support in Fixed-Carrier Oriented Algebra: Wreath Coherence, Partition Compression, and Exact Orbital Separation*

**Russian:** *Предписанная стабилизаторная опора в фиксированно-носительной ориентированной алгебре: Wreath-когерентность, сжатие разбиений и точное орбитальное разделение*

**Author:** Alex Malachevsky  
**ORCID:** 0009-0008-6009-3196  
**Series:** Commander Sol / Fixed-Carrier Oriented Algebra / FCOA-Z  
**Release date:** 2026-09-01  
**Status:** publication package passed; ready for Zenodo deposit  
**Zenodo DOI:** pending deposit

## Required FCOA lineage

- FCOA Foundation — DOI [`10.5281/zenodo.22164246`](https://doi.org/10.5281/zenodo.22164246)
- Direct FCOA-Z predecessor, *Reflections on How a Ray Becomes an Axis* — DOI [`10.5281/zenodo.22171473`](https://doi.org/10.5281/zenodo.22171473)

The Foundation DOI is cited in both language abstracts and bibliographies, in accordance with the repository-wide FCOA publication rule.

## Main invariant

The paper uses the fixed-action prescribed-stabilizer support quantity

\[
m_G(H;S)=\min\{|F|:F\subseteq S,\ \operatorname{Stab}_G(F)=H\},
\]

as an FCOA resource measure for exact residual symmetry encoded in value geometry. No priority is claimed for the abstract group-action notions of setwise stabilizers, regular sets, relation groups, distinguishing theory, or wreath-product symmetry breaking.

## Main exact results

For a transitive branch action \(A\leq\operatorname{Sym}(\Lambda)\) of degree \(t\) on \(b\) isomorphic branches,

\[
\boxed{m_{A\wr S_b}(\Delta A\times S_b;S_\times)=b(b-1)t.}
\]

For an arbitrary branch partition \(\mathcal P=\{B_1,\ldots,B_c\}\) with block sizes \(n_1,\ldots,n_c\),

\[
\boxed{m_G(H_{\mathcal P};S_\times)=t\sum_{j=1}^c n_j(n_j-1).}
\]

If internal phases remain independent and only the partition is remembered, the problem reduces exactly to

\[
\boxed{m_G(J_{\mathcal P};S_\times)=t^2d(\mathcal P),}
\]

where \(d(\mathcal P)\) is the minimum loopless directed branch-level support whose automorphism group is exactly the concrete partition stabilizer \(K_{\mathcal P}\).

The paper then proves the Partition-Overgroup Dichotomy, the Macro-Mover Double-Coset Lemma, the exact recognition theorem, and the weighted Orbital XOR-Separation Program for arbitrary finite partition type.

A central resource phenomenon is non-monotonicity: a semantically stronger phase-coherent memory can require fewer FCOA cells than partition-only memory.

## Verification

The exact recognizer was checked by direct enumeration of the full symmetric group for every integer partition with

\[
2\le b\le7.
\]

Frozen verification state:

- 43 integer-partition types checked;
- 1468 invariant orbital unions checked;
- result: **ALL PASS**;
- seven-vertex \(D_8\to V_4\) support verifier: **PASS**;
- exact anonymous-output minimum in the binary seven-vertex compiler: **9**;
- frozen transcript: [`VERIFIER_OUTPUT_2026-09-01.txt`](VERIFIER_OUTPUT_2026-09-01.txt).

## Release files and reproducibility

Primary records:

- [`ARTICLE_EN.md`](ARTICLE_EN.md) — English manuscript source;
- [`ARTICLE_RU.md`](ARTICLE_RU.md) — Russian manuscript source;
- [`RELEASE_METADATA.md`](RELEASE_METADATA.md) — release metadata and Zenodo description seed;
- [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md) — proof, bibliography, build, and visual-QA gate;
- [`VERIFIER_OUTPUT_2026-09-01.txt`](VERIFIER_OUTPUT_2026-09-01.txt) — frozen exact-verifier output;
- [`prepare_release_sources.py`](prepare_release_sources.py) — deterministic release-source normalizer;
- [`publication-header.tex`](publication-header.tex) — publication typesetting header.

The repository contains a reproducible GitHub Actions Pandoc + XeLaTeX pipeline. The final audited package contains parallel English and Russian PDFs plus an archival source ZIP. PDF visual QA passed with no clipping or overlap observed.

## Publication decision

\[
\boxed{\text{research threshold — PASSED}}
\]

\[
\boxed{\text{PDF/source archival threshold — PASSED}}
\]

\[
\boxed{\text{Zenodo deposit threshold — PASSED}}
\]

The external Zenodo upload is the only remaining publication-platform step. After Zenodo assigns the DOI, this README, the root English/Russian README files, and `RELEASE_METADATA.md` must be updated with the permanent DOI.

## Next research branch

The first publication is closed mathematically at the current theorem layer. The computational complexity of the special Orbital XOR-Separation Program, higher-arity value fibers, restricted branch groups, and deeper iterated wreath products belong to separate follow-up branches rather than to this release.
