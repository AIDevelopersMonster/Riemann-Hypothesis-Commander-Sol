# HATTER-SOL-07 — continuity / handoff status

**Branch:** `research/hatter-sol-free-ports`  
**Path:** `papers/HATTER-SOL/07-FREE-PORT-FACTORIZATION/`  
**Status date:** 2026-09-12  
**Status:** **PUBLICATION THRESHOLD REACHED** — short RU/EN research note should now be assembled.

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

Multiplicative refinement need not improve topological saturation. There are infinite families with

\[
\lambda(\text{refined})>\lambda(\text{coarse}).
\]

In particular, for odd `q>=3` and `m>=2q`, replacing the coarse vector

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

Hence refinement inversion is not bounded by any universal constant.

Examples:

\[
6\to2\cdot3:\quad \Delta\lambda_{\max}=1,
\]

\[
8\to2\cdot4:\quad \Delta\lambda_{\max}=2,
\]

\[
9\to3\cdot3:\quad \Delta\lambda_{\max}=3.
\]

The split `4->2*2` is the unique pair `a,b>=2` with zero worst-case inversion.

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
S(\mathbf c)-S(\mathbf d).
}
\]

Equivalently,

\[
\boxed{
\lambda(\mathbf d)+S(\mathbf d)
\le
\lambda(\mathbf c)+S(\mathbf c).
}
\]

So `lambda+S` is refinement-nonincreasing in this model.

## Literature-audit result

The hostile audit located:

1. classical maximum simple `b`-matching / `f`-bounded-subgraph theory;
2. generalized Tutte-Berge deficiency formulas;
3. one-vertex capacity sensitivity results;
4. extensive vertex detachment/splitting theory;
5. Matula-Goebel factorization/tree encodings.

It did **not** locate an explicit theorem equivalent to the exact sharp response

\[
\Delta_{a,b}^{\max}=ab-a-b
\]

for the complete-host simple-network operation that replaces one capacity `ab` by two capacities `a,b` and re-optimizes all edges.

This is a serious negative search, not an absolute priority guarantee.

## Publication decision

\[
\boxed{\textbf{PUBLICATION THRESHOLD REACHED}.}
\]

A short standalone HATTER-SOL-07 research note is justified because:

- the classical layer has now been identified and fenced off;
- the central theorem is exact, sharp, and proved;
- sharpness holds for every local split `a,b`;
- the inversion amplitude is unbounded;
- there is a natural iterated monotone;
- the closest prior-art families found do not state the same multiplicative-split theorem.

## Publication framing

Recommended central formulation:

> We introduce a factor-capacity network viewpoint on multiplicative decompositions and isolate a sharp sensitivity law for minimum unused capacity under the arithmetic split `ab -> (a,b)`. For each fixed capacity vector the optimization is classical maximum simple b-matching; the contribution is the exact interaction between this deficiency and multiplicative refinement.

## Next actions

1. Assemble `article_ru.md` in the HATTER-SOL / Wonderland “Размышлизмы” style, with a visibly separate rigorous theorem section.
2. Produce synchronized `article_en.md`.
3. Include the hostile literature audit and conservative novelty statement.
4. Audit theorem numbering, proof completeness, bibliography, DOI metadata, author line, and ORCID.
5. Only after that produce publication PDF(s) and Zenodo package.

Do not merge or publish automatically unless explicitly requested; this branch is the canonical publication-working branch.
