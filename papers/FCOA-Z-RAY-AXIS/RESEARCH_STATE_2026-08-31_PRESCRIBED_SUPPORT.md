# FCOA-Z Research State — Prescribed-Stabilizer Support Milestone

Date: 2026-08-31

## Closed questions

The branch has moved from one exact seven-vertex compiler to a general prescribed-stabilizer support theory.

### General resource

For a finite permutation `G`-set `S` and `H<=G`, define

\[
m_G(H;S)=\min\{|F|:F\subseteq S,\operatorname{Stab}_G(F)=H\}.
\]

Orbit-union reduction is exact. For normal `H`, the problem becomes a weighted regular-set problem for `G/H` acting on the `H`-orbits of `S`. For index two this gives an exact minimum moved-orbit formula.

### Global wreath coherence

Let `A<=Sym(Lambda)` be any transitive group of degree `t`, let `G=A wr S_b`, and let

\[
H=\Delta A\times S_b.
\]

On ordered cross-branch cells,

\[
\boxed{m_G(H;S_x)=b(b-1)t.}
\]

The natural connection-independent cross domain has

\[
|S_x|=b(b-1)t^2,
\]

and

\[
[G:H]=|A|^{b-1}.
\]

The 2-transitive hypothesis initially used was proved unnecessary; transitivity alone is sharp for this theorem package.

### Equal-block partial coherence

Let `b=cn` and partition the branches into `c` equal unlabeled blocks of size `n`. Let

\[
H_{c,n}=A^{\mathcal P}\rtimes(S_n\wr S_c),
\]

where the internal phase is constant inside each block but independent between blocks.

Then

\[
\boxed{m_G(H_{c,n};S_x)=b(n-1)t.}
\]

The symmetry index is

\[
\boxed{[G:H_{c,n}]
=|A|^{b-c}\frac{b!}{(n!)^c c!}.}
\]

This gives the exact hierarchy

\[
0\le b(n-1)t\le b(b-1)t
\]

between no cross-branch coherence and full global coherence.

### Anonymous output anomaly

Across the full transitive wreath family, the balanced anonymous-output exchange anomaly is unique:

\[
A=S_2,\quad b=2,\quad t=2.
\]

This is precisely the minimal seven-vertex binary `D8 -> V4` compiler. It requires the extra canonical root anchor, giving the exact nine-cell FCOA realization.

## Current conceptual picture

The programme now separates four resources:

1. **domain cost** — how many operation cells must be opened;
2. **special support cost** — how many cells must carry the coherence-identifying value;
3. **semantic multiplicity** — the number `[G:H]` of distinguishable residual-symmetry states;
4. **output-cardinality / label anonymity cost** — whether terminal value exchange creates an extra automorphism.

These quantities can scale very differently.

## Active frontier

The next unsolved family is an unequal branch partition

\[
\lambda=(n_1,\ldots,n_c),\qquad \sum n_j=b.
\]

The naive within-block equality support has size

\[
t\sum_j n_j(n_j-1),
\]

but it is not generally minimal. If one partition block is uniquely determined as the complement of all marked blocks, its internal clique need not be stored explicitly. This creates the first genuine support-compression phenomenon in the partition hierarchy.

The next task is to determine the exact optimum and identify when complement recovery permits omitting one block or one block-size class without enlarging the stabilizer.