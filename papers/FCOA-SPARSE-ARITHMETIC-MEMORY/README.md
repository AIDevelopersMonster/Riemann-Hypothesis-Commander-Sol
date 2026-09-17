# FCOA / SOL-HYBRID — Article B

**English title:** *Reflections on Sparse Arithmetic Memory with Commander Sol: An Exact Conjunctive-Query Width Threshold for Finite Addition*

**Russian title:** *Размышлизмы о разреженной арифметической памяти с Commander Sol: точный порог ширины конъюнктивного запроса для конечного сложения*

- Author (EN): Alex Malachevsky
- Автор (RU): Алексей Малачевский
- ORCID: 0009-0008-6009-3196
- Version: 1.0.0
- Publication date: 2026-09-03
- Resource type: Publication / Preprint
- License: CC BY 4.0
- Zenodo DOI: **10.5281/zenodo.22286064**
- Persistent URL: https://doi.org/10.5281/zenodo.22286064

## Main theorem

For static relational preprocessing over a fixed finite bounded-arity signature, decoded by one fixed conjunctive query, the minimum variable width admitting near-linear preprocessing for exact canonical truncated addition is

\[
\boxed{k_+=9}.
\]

The lower bound requires at least six existential helper variables beyond the three free variables. The matching upper bound is a two-channel CRT construction with exactly six residue helpers.

Under the canonical AL2 benchmark that includes order and truncated addition, the near-linear width threshold is also 9 because the truncated multiplication graph has only `Theta(N log N)` true tuples and may be materialized directly.

## Claim ceiling

The paper does **not** claim the width-9 threshold for UCQs, the whole existential-positive fragment, full finite-variable FO, or arbitrary interpretation-equivalent encodings.

Earlier CF/bounded-depth/RTP/internal-memory claims are not dependencies of the main theorem; invalid CF and bounded-depth lower bounds remain quarantined in the research branch.

## Publication package

Final bilingual PDFs are v1.0.0 and include the Zenodo DOI. The Russian manuscript uses **Алексей Малачевский**; international citation and Zenodo creator metadata use **Alex Malachevsky**.

Final SHA-256:

- EN PDF: `401935136c656b88ce9944f9137d5efe839e0b240b709344b0768d21c60455ed`
- RU PDF: `df1f2fdfbef9ac962d5a6d02245ad2741d5698c713421197ab303526b792db5f`

## Publication status

\[
\boxed{\text{PUBLISHED / v1.0.0 / DOI 10.5281/zenodo.22286064}}
\]
