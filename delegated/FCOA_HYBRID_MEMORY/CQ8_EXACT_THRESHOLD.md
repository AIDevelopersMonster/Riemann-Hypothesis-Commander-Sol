# FCOA Hybrid Memory — Exact CQ Width Threshold (Audited Repair)

**Status:** CANONICAL ARTICLE-B THEOREM CANDIDATE AFTER HOSTILE AUDIT  
**Main result:** the minimum conjunctive-query variable width for `N^{1+o(1)}` preprocessing of exact canonical truncated addition is exactly `9`.

## 0. Scope and audit note

The target sector is canonically identified, for construction and benchmark purposes, with `[N]={0,...,N-1}` and

\[
Add_N(x,y,z)\iff x+y=z<N.
\]

The first version of the width-9 proof contained a gap: it proved that each free-coordinate information boundary had at least two helpers, but then incorrectly concluded that both had to be private non-negligible helpers. A shared `o(log N)` helper can still be topologically necessary.

The repaired proof conditions away all zero-normalized-entropy helpers first and works on the remaining positive-information core. In that core the three information-color components are disjoint, and no color component can be a singleton. This yields six helper variables, hence total width at least nine.

The theorem is only for one fixed **conjunctive query** over a fixed finite bounded-arity relational signature. It is not a theorem for arbitrary existential-positive FO with disjunction or for full finite-variable FO.

## 1. Model

A preprocessing representation consists of a finite structure `A_N` over one fixed finite bounded-arity relational signature, containing a distinguished target sector `X_N` of size `N`, and a fixed CQ

\[
q(x,y,z)=\exists\bar u\;\bigwedge_i R_i(\bar t_i)
\]

whose answer on `X_N` is exactly `Add_N`.

Assume

\[
S(A_N)=|A_N|+\sum_R|R^{A_N}|=N^{1+o(1)}.
\]

Let `h` be the number of helper variables in `\bar u`; total CQ width is `k=3+h`.

We prove `h>=6`.

## 2. Dense Latin slice

Let `m=floor(N/3)` and restrict to

\[
\mathcal T_m=\{(x,y,z):0\le x,y<m,\ z=x+y\}.
\]

Choose `(X,Y)` uniformly from `[m]^2` and set `Z=X+Y`. Then

\[
H(X)=H(Y)=\log m,
\]

\[
H(X,Y)=H(X,Z)=H(Y,Z)=2\log m,
\]

and `H(Z)=log m+O(1)`. Thus the three coordinates have one normalized entropy unit each, pairwise mutual information `o(log N)`, and joint entropy two units. Every two free coordinates determine the third.

Choose one satisfying helper tuple deterministically for each triple of `\mathcal T_m`.

## 3. No free-pair atom in a near-linear representation

If a primitive atom contains two distinct free variables among `X,Y,Z`, its projection on those positions contains `Theta(N^2)` distinct free pairs, so that primitive relation alone has quadratic size. Therefore every atom in a near-linear candidate contains at most one free arithmetic variable.

For a fixed complete helper assignment, all constraints on `X`, `Y`, `Z` therefore factor into a Cartesian box

\[
X_{\bar u}\times Y_{\bar u}\times Z_{\bar u}.
\]

A nonempty Cartesian box contained in `x+y=z` has size one. Hence every productive helper tuple determines a unique free triple. With deterministic witness selection, the helper tuple and the selected free triple determine each other on the selected support.

## 4. Helpers adjacent to a free coordinate

For `F in {X,Y,Z}`, let `A_F` be the set of helper variables that occur with `F` in at least one atom.

Every atom has at most `N^{1+o(1)}` tuples. If an atom contains `F` and helper tuple `S`, then

\[
H(F,S)\le\log N+o(\log N).
\]

Since `H(F)=log N+o(log N)`, we obtain

\[
H(S\mid F)=o(\log N).
\]

There are only constantly many atoms, so

\[
H(A_F\mid F)=o(\log N).
\tag{4.1}
\]

Conversely, if two productive witnesses agree on all helpers adjacent to `F`, then every atom involving `F` sees the same helper values. Replacing the `F`-part of one witness by that of the other while keeping the remaining helper assignment fixed would otherwise produce two accepted triples with the same other two free coordinates, contradicting the Latin functional dependency. Therefore

\[
H(F\mid A_F)=o(\log N).
\tag{4.2}
\]

Hence

\[
H(A_F)=\log N+o(\log N).
\tag{4.3}
\]

## 5. Conditioning away zero-information helpers

Call a helper `U` zero-information if `H(U)=o(log N)`. Since the query has only constantly many helpers, their joint entropy is `o(log N)`. A standard high-probability-set argument gives a joint value of these helpers whose fiber contains `N^{2-o(1)}` selected addition triples.

Condition on such a value and substitute those helpers by constants. On a Latin subrelation of size `N^{2-o(1)}`, each pair projection has the same cardinality, and each single-coordinate projection has size at least `N^{1-o(1)}` because every fixed coordinate value occurs in at most `N` triples. Therefore, under the uniform distribution on the surviving fiber,

\[
H(F)=\log N-o(\log N),
\]

\[
H(F,G)=2\log N-o(\log N)
\]

for distinct free coordinates.

If conditioning makes another helper zero-information, repeat. Since the number of helpers is fixed, the process terminates. In the final reduced query every remaining helper satisfies

\[
H(U)=\Omega(\log N).
\tag{5.1}
\]

and the dense Latin entropy relations above remain valid.

## 6. Information colors are disjoint

A remaining helper `U` is `F`-colored if

\[
H(U\mid F)=o(\log N).
\]

Every helper adjacent to `F` is `F`-colored by Section 4.

If `U` were both `F`- and `G`-colored for distinct free coordinates, then

\[
H(U)\le I(F;G)+H(U\mid F)+H(U\mid G)=o(\log N),
\]

contradicting (5.1). Thus every positive-information helper has at most one free-coordinate color.

## 7. Maximal colored components

For each free coordinate `F`, let `C_F` be the maximal connected set of positive-information `F`-colored helpers reachable from the atoms containing `F` through helper-only atoms while remaining inside the `F`-colored set.

By (4.3), `C_F` is nonempty and carries one entropy unit. By Section 6,

\[
C_X,C_Y,C_Z
\]

are pairwise disjoint.

## 8. No colored component is a singleton

### Lemma HM-CQ-COLOR2

For every `F in {X,Y,Z}`,

\[
|C_F|\ge2.
\]

### Proof

Assume `C_F={U}`. Since the component carries the information of `F`,

\[
H(U)=\log N-o(\log N).
\tag{8.1}
\]

If no helper-only atom connects `U` to a positive-information helper outside `C_F`, then after the zero-information helpers have been fixed, the CQ factor graph separates the `F` branch from the other two free branches. The answer relation factors as a Cartesian product in `F` versus the other two coordinates. A dense Latin subrelation with `N^{1-o(1)}` possible values of `F` cannot factor this way because the other two coordinates determine `F` uniquely.

Hence some helper-only atom contains `U` and a nonempty tuple `T` of positive-information helpers outside `C_F`. Since the primitive relation is near-linear,

\[
H(U,T)\le\log N+o(\log N).
\]

Together with (8.1),

\[
H(T\mid U)=o(\log N).
\]

Because `H(U|F)=o(log N)`, the chain rule gives

\[
H(T\mid F)=o(\log N).
\]

Thus every component of `T` is `F`-colored and connected to `U`, contradicting maximality of the singleton component. `square`

## 9. Six-helper lower bound

The three colored components are pairwise disjoint and each contains at least two helpers. Therefore the positive-information core has at least six helpers. Conditioning only removed variables, so the original CQ also had at least six helper variables:

\[
h\ge6.
\]

Hence

\[
\boxed{k\ge9.}
\]

## 10. Matching width-9 CRT construction

Choose coprime `p,q=Theta(sqrt N)` with `pq>2N`. Store target residue maps modulo `p,q` and complete modular addition tables. The total number of stored tuples is `Theta(N)`.

Use six helper variables

\[
x_p,y_p,z_p,x_q,y_q,z_q
\]

and the CQ asserting the three residue maps and modular addition in both channels. If both congruences hold, then `pq` divides `x+y-z`, while `|x+y-z|<2N<pq`; hence `x+y=z`. Conversely exact addition satisfies both modular equations.

Thus width `3+6=9` suffices with linear storage.

### Theorem HM-CQ-EXACT

\[
\boxed{k_+=9.}
\]

## 11. AL2 under the canonical benchmark convention

For Article B we define the AL2 benchmark to include the AL1 benchmark. The truncated multiplication graph

\[
Mul_N(x,y,z)\iff xy=z<N
\]

has `Theta(N log N)=N^{1+o(1)}` true triples and may be materialized directly as a ternary relation without changing the near-linear storage exponent. Therefore adding multiplication to an optimal near-linear AL1 presentation does not require additional CQ variables beyond the three free variables already used by the multiplication atom.

Consequently, under this benchmark convention,

\[
\boxed{k_{AL2}=k_{AL1}=9.}
\]

## 12. Claim ceiling

Proved:

- near-linear exact canonical addition in the static relational CQ-preprocessing model requires six helper variables and six suffice;
- the exact near-linear width threshold is `9`;
- under the benchmark convention that AL2 includes AL1, the AL2 threshold is also `9`.

Not proved:

- the same threshold for full existential-positive FO with disjunction;
- the same threshold for arbitrary `FO^k`;
- exact storage exponents at widths `6,7,8`;
- an interpretation-invariant statement outside this preprocessing model.

## 13. Literature calibration

Entropy methods for CQ bounds under functional dependencies and factorised-representation lower bounds provide the standard background language. The proof above is specialized to the exact finite addition relation and its Latin functional dependencies; it is not claimed as an immediate corollary of a published general theorem.

Relevant references for the bibliography include Tomasz Gogacz and Szymon Torunczyk, *Entropy Bounds for Conjunctive Queries with Functional Dependencies*, ICDT 2017, DOI 10.4230/LIPIcs.ICDT.2017.15; Dan Olteanu and Jakub Zavodny, *Factorised Representations of Query Results: Size Bounds and Readability*, ICDT 2012; and Christoph Berkholz and Harry Vinall-Smeeth, *Factorised Representations of Join Queries: Tight Bounds and a New Dichotomy*, ICDT 2026.
