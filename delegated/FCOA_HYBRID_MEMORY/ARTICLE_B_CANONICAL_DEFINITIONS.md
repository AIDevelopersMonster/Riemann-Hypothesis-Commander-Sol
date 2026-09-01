# Article B — Canonical Definitions and Scope

**Status:** CANONICAL PUBLICATION FRONT MATTER

## 1. Target sector and benchmark arithmetic

For each `N>=1`, the presentation contains a distinguished target sector `X_N` of cardinality `N`. For benchmark statements we fix an external rank bijection

\[
r_N:X_N\to [N]=\{0,1,\ldots,N-1\}.
\]

The benchmark relations on `X_N` are the pullbacks of:

\[
x<y,
\]

\[
Add_N(x,y,z)\iff x+y=z<N,
\]

\[
Mul_N(x,y,z)\iff xy=z<N.
\]

The rank bijection is used to specify the target relation; it is not available to the decoder unless encoded in the preprocessing structure.

## 2. Canonical benchmark hierarchy

Define

\[
B_0(N)=([N],<),
\]

\[
B_1(N)=([N],<,Add_N),
\]

\[
B_2(N)=([N],<,Add_N,Mul_N).
\]

Article B uses the labels `AL0`, `AL1`, `AL2` only for recovery of these **canonical target-sector benchmarks**:

- `AL0`: canonical target order is uniformly recoverable;
- `AL1`: canonical target order and canonical truncated addition are uniformly recoverable;
- `AL2`: canonical target order, truncated addition, and truncated multiplication are uniformly recoverable.

When the word **exact** is used, it means that the next canonical benchmark relation is not recoverable in the stated model. Exactness is model-relative and must be proved separately; reaching AL1 does not by itself prove exact AL1.

## 3. Two different notions must not be conflated

Article B distinguishes:

1. **target-benchmark recovery:** a formula defines `<`, `Add_N`, or `Mul_N` on the distinguished `X_N`;
2. **interpretability somewhere in the structure:** arithmetic may be interpretable on another definable set or quotient.

A theorem about target-benchmark recovery is not automatically a theorem excluding all arithmetic interpretations elsewhere.

## 4. Static relational preprocessing model

A preprocessing family is a sequence of finite relational structures `A_N` over one fixed finite signature of bounded arity, each containing the target sector `X_N`.

Total storage is

\[
S(A_N)=|A_N|+\sum_R|R^{A_N}|.
\]

All canonical Article B space exponents count the **whole preprocessing structure**, including target attachments and auxiliary relations.

This convention is deliberately chosen to avoid the target-hosting loophole that invalidated endpoint-based internal-memory measures.

## 5. FO decoder model

For the FO preprocessing collapse theorem, each benchmark relation is recovered by one fixed first-order formula independent of `N`. Quantifier rank is bounded by a fixed constant.

## 6. CQ decoder model

For the variable-width results, a decoder is one fixed conjunctive query

\[
q(\bar x)=\exists\bar u\;\bigwedge_i R_i(\bar t_i)
\]

over the preprocessing signature.

The CQ width is the number of **distinct variable names** occurring in the query, free and existential together.

A single CQ is a primitive-positive formula. Article B does not identify this class with the whole existential-positive fragment, which also permits finite disjunctions.

## 7. Storage exponents

For phase `j` and CQ width `k`,

\[
\sigma_j^{CQ}(k)
=
\inf\limsup_{N\to\infty}
\frac{\log S(A_N)}{\log N},
\]

where the infimum ranges over preprocessing families whose relevant canonical benchmark relations are decoded by fixed CQs of width at most `k`.

Near-linear means

\[
S(A_N)=N^{1+o(1)}.
\]

## 8. Width thresholds

Let `k_+` be the least fixed CQ width admitting near-linear preprocessing for exact canonical truncated addition.

For the AL2 benchmark, since AL2 includes AL1 by definition, let `k_{AL2}` be the least width at which all AL2 benchmark relations admit near-linear preprocessing.

The audited theorem proves

\[
\boxed{k_+=k_{AL2}=9.}
\]

The equality for AL2 uses the sparsity of the truncated multiplication graph, which has `Theta(N log N)` true triples and can be materialized near-linearly once the AL1 layer is available.

## 9. Claim ceiling

Article B does not claim:

- a width-9 theorem for arbitrary full `FO^k`;
- a width-9 theorem for arbitrary existential-positive formulas with disjunction;
- that RTP, internal-law memory, CF bottom memory, or radix depth are interpretation-invariant phase measures;
- that exact AL0/AL1 statements in one target model exclude arithmetic interpretations on unrelated definable quotients;
- any result about the Riemann hypothesis itself.
