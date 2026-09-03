# FCOA / SOL-HYBRID — Article B

**English title:** *Reflections on Sparse Arithmetic Memory with Commander Sol: An Exact Conjunctive-Query Width Threshold for Finite Addition*

**Russian title:** *Размышлизмы о разреженной арифметической памяти с Commander Sol: точный порог ширины конъюнктивного запроса для конечного сложения*

- Author (EN): Alex Malachevsky
- Автор (RU): Алексей Малачевский
- ORCID: 0009-0008-6009-3196
- Version: 0.9.0-rc1
- Package date: 2026-09-03
- Intended resource type: Publication / Preprint
- License: CC BY 4.0
- Zenodo DOI: **pending reservation**

## Main theorem

For static relational preprocessing over a fixed finite bounded-arity signature, decoded by one fixed conjunctive query, the minimum variable width admitting near-linear preprocessing for exact canonical truncated addition is

\[
\boxed{k_+=9}.
\]

The lower bound requires at least six existential helper variables beyond the three free variables. The matching upper bound is a two-channel CRT construction with exactly six residue helpers.

Under the canonical AL2 benchmark that includes order and truncated addition, the near-linear width threshold is also 9 because the truncated multiplication graph has only `Theta(N log N)` true tuples and may be materialized directly.

## Claim ceiling

The release candidate does **not** claim the width-9 threshold for UCQs, the whole existential-positive fragment, full finite-variable FO, or arbitrary interpretation-equivalent encodings.

Earlier CF/bounded-depth/RTP/internal-memory claims are not dependencies of the main theorem; the invalid CF and bounded-depth lower bounds are quarantined in the research branch.

## Publication status

`REVIEWED_CLEAN — DOI reservation pending`

The bilingual RC PDFs and complete source package have been built and render-audited locally. The Russian manuscript uses the author form **Алексей Малачевский**; international citation and Zenodo creator metadata use **Alex Malachevsky**. After the Zenodo DOI is reserved, both PDFs must be rebuilt with the DOI inserted, checksums regenerated, and this README moved to v1.0.0 / PUBLISHED.