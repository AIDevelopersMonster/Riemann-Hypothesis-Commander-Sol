# HATTER-SOL-07 — continuity / handoff status

**Branch:** `research/hatter-sol-free-ports`  
**Path:** `papers/HATTER-SOL/07-FREE-PORT-FACTORIZATION/`  
**Status date:** 2026-09-12  
**Status:** **PUBLICATION THRESHOLD REACHED; RU PUBLICATION CANDIDATE ASSEMBLED AND PDF-QA PASSED**.

## Core model

Treat a factor `m` as a capacity-`m` node. For a connected simple graph `G=(V,E)` with factor capacities `a_v>=2`, define free boundary

\[
B(G,\mathbf a)=\sum_v(a_v-\deg_G v)=\sum_v a_v-2|E|.
\]

For a tree,

\[
B(T,\mathbf a)=2+\sum_v(a_v-2).
\]

Hence the original chain quantity `F=\sum(a_i-2)` is exactly the tree free boundary after designating two global terminals as input/output.

## Classical backbone / claim discipline

For a fixed capacity vector, minimizing free boundary is exactly maximum-cardinality simple `b`-matching / an `f`-bounded-subgraph problem on the complete host graph. This classical optimization layer is not claimed as new.

The literature audit also records classical vertex detachment/splitting and Matula-Goebel number/tree encodings. The publication must explicitly separate these from the candidate new theorem.

See `LITERATURE_AUDIT.md`.

## Result 1 — fixed-decomposition spectrum

For a fixed decomposition `\mathbf a=(a_1,...,a_k)`, let

\[
M_c(\mathbf a)=\max\{|E(G)|:\;G\text{ connected, simple, }\deg(v_i)\le a_i\}.
\]

Then

\[
\boxed{
\mathcal B(\mathbf a)
=\{\sum_i a_i-2e:\;k-1\le e\le M_c(\mathbf a)\}.
}
\]

Thus the boundary spectrum of one fixed factorization is a complete parity interval.

## Result 2 — refinement inversion

Multiplicative refinement need not improve topological saturation. For odd `q>=3` and `m>=2q`, replacing

\[
(2q,2^m)
\]

by

\[
(q,2^{m+1})
\]

gives

\[
\lambda(2q,2^m)=0,
\qquad
\lambda(q,2^{m+1})=1.
\]

See `REFINEMENT_INVERSION.md`.

## Main theorem — exact sharp one-step inversion amplitude

Let a capacity `ab` be refined to capacities `a,b`, with `a,b>=2`. Then for every ambient capacity vector,

\[
\boxed{
\lambda(\ldots,a,b,\ldots)
-
\lambda(\ldots,ab,\ldots)
\le
ab-a-b.
}
\]

Moreover this bound is sharp for every pair `a,b>=2`:

\[
\boxed{
\sup_{\text{ambient decompositions}}
\Bigl[
\lambda(\ldots,a,b,\ldots)
-
\lambda(\ldots,ab,\ldots)
\Bigr]
=ab-a-b.
}
\]

Hence refinement inversion is not bounded by any universal constant. The split `4->2*2` is the unique pair `a,b>=2` with zero worst-case inversion.

See `SHARP_REFINEMENT_BOUND.md`.

## Iterated corollary

If `\mathbf d` is obtained from `\mathbf c` by a sequence of multiplicative refinements and

\[
S(\mathbf c)=\sum_i c_i,
\]

then

\[
\boxed{
\lambda(\mathbf d)-\lambda(\mathbf c)
\le
S(\mathbf c)-S(\mathbf d)
}
\]

and hence

\[
\boxed{
\lambda(\mathbf d)+S(\mathbf d)
\le
\lambda(\mathbf c)+S(\mathbf c).
}
\]

## Literature-audit result

The hostile audit located classical maximum simple `b`-matching / `f`-bounded-subgraph theory, generalized Tutte-Berge deficiency formulas, one-vertex capacity sensitivity, vertex detachment/splitting, and Matula-Goebel encodings. It did **not** locate an explicit theorem equivalent to

\[
\Delta_{a,b}^{\max}=ab-a-b
\]

for the complete-host simple-network operation that replaces one capacity `ab` by two capacities `a,b` and re-optimizes all edges. This is a serious negative search, not an absolute priority guarantee.

Bibliographic audit on 2026-09-12 corrected several metadata details in the Drive publication candidate, notably:

- Qu **Z.** and West **D. B.**, *Journal of Graph Theory* 112(2) (2026), 145–150, DOI `10.1002/jgt.70019`;
- Fleiner, *SIAM Journal on Discrete Mathematics* 18(3) (2004), 581–591;
- Korte–Vygen, 6th ed. (2018), DOI `10.1007/978-3-662-56039-6`;
- Göbel DOI `10.1016/0095-8956(80)90049-0`.

## Publication assembly state

### Russian version

- `ARTICLE_RU_v0.9.md` assembled in this branch.
- Native Google Docs publication candidate assembled in project folder `03_Manuscript`.
- Seven Alice/Hatter illustrations inserted in the approved order.
- `03.png` is explicitly captioned as a schematic intuition for refinement inversion, not a proof diagram.
- `07.png` is explicitly captioned as a schematic sharpness-construction map; exact counts are in the theorem text.
- corrected `05.png` is used, with `12=[2]x[2]x[3]` visually unambiguous.
- PDF export visually inspected page-by-page: 14 pages, all seven figures present, no clipping/overlap.
- unsupported Unicode subscript `ₖ`, which rendered as a box in the first PDF pass, was replaced by `_k` in the Google Docs publication candidate.
- QA PDF saved in Drive as `HATTER-SOL-07_RU_v0.9_publication_candidate.pdf`.

### Important sync note

The Google Docs/PDF candidate contains the latest bibliography corrections listed above. Before tagging a GitHub v1.0 or publishing to Zenodo, synchronize those final bibliography edits back into the Markdown article and rerun the mandatory RU/EN publication audit.

## Publication framing

Recommended central formulation:

> We introduce a factor-capacity network viewpoint on multiplicative decompositions and isolate a sharp sensitivity law for minimum unused capacity under the arithmetic split `ab -> (a,b)`. For each fixed capacity vector the optimization is classical maximum simple b-matching; the contribution is the exact interaction between this deficiency and multiplicative refinement.

## Next actions

1. Perform one final hostile mathematical audit of Lemma 5.1 and the sharpness proof against edge cases.
2. Synchronize the corrected bibliography from the Drive candidate into GitHub Markdown.
3. Produce synchronized English article `ARTICLE_EN_v0.9.md`.
4. Audit numbering, DOI/date metadata, author line, ORCID, RU/EN consistency and figure captions.
5. Only then promote RU/EN files to final publication PDFs and prepare the Zenodo package.

Do not merge or publish automatically unless explicitly requested; this branch remains the canonical publication-working branch.
