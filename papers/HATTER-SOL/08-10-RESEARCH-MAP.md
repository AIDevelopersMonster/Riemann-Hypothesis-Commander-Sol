# HATTER-SOL 08–10 — research map after Free-Port Factorization

**Branch:** `research/hatter-sol-dimensional-factor-morphisms`  
**Base:** `research/hatter-sol-free-ports`  
**Status:** research seeds / no publication claims yet

This map preserves three distinct continuations of HATTER-SOL-07 instead of forcing them prematurely into one article.

## HATTER-SOL-08 — Dimensional Factor Architectures

Question: what changes when factor-capacity networks are not abstract graphs, but must live in a prescribed architecture class such as 1D, outerplanar/circular, 2D planar, or 3D unrestricted space?

Core candidates:

\[
M_{\mathcal C}(\mathbf c)=\max\{|E(G)|:G\in\mathcal C,\;\deg(v_i)\le c_i\},
\]

\[
\lambda_{\mathcal C}(\mathbf c)=\sum_i c_i-2M_{\mathcal C}(\mathbf c).
\]

Expected hierarchy for nested classes

\[
\text{1D path}\subseteq\text{outerplanar}\subseteq\text{planar}\subseteq\text{all finite graphs}
\]

gives

\[
\lambda_{1D}\ge\lambda_{\circ}\ge\lambda_{2D}\ge\lambda_{3D}=\lambda.
\]

A second, intrinsic notion of dimension uses clique/flag complexes and asks for architectures of bounded simplicial dimension.

## HATTER-SOL-09 — The Integer as a Factorization State Space

Question: treat one integer not as one factorization but as the entire state space of all its multiplicative decompositions.

For

\[
n=\prod_{j=1}^r p_j^{e_j}
\]

write its exponent vector

\[
e(n)=(e_1,\ldots,e_r)\in\mathbb N^r.
\]

An unordered factorization

\[
n=a_1\cdots a_k
\]

corresponds to a vector partition

\[
e(n)=\alpha_1+\cdots+\alpha_k,
\qquad \alpha_i\in\mathbb N^r\setminus\{0\},
\]

modulo permutation of the summands. A refinement is exactly a local split

\[
\alpha\mapsto\beta+\gamma.
\]

The classical factorization structure is known; the proposed new layer enriches every factorization state by its capacity-network fiber, boundary spectrum, dimensional realizations, and geometry-transfer data.

## HATTER-SOL-10 — Square, Triangle, Circle: Geometry-Transfer Morphisms

Question: given the same abstract factor architecture, which transformations between geometric realizations preserve arithmetic labels, adjacency, cycles, faces, boundary, metric data, or refinement?

Key warning: `bijection` alone is not a novelty claim. The research target is classification of **structure-preserving** maps and invariants under those maps.

The first distinction is crucial:

1. If square/triangle/disk are merely 2D containers and edges may be arbitrary noncrossing arcs, they are topologically equivalent (all are disks).
2. If all vertices are constrained to one boundary, the natural class is outerplanar; the exact convex boundary shape is topologically irrelevant.
3. If straightness, nearest-neighbour rules, Euclidean metric, or a square/triangular lattice are part of the structure, square and triangle/circle cease to be equivalent.

This is where a genuine morphism spectrum can arise.

## Publication discipline

- HATTER-SOL-07 remains a self-contained publication candidate and is not to be rewritten around these new ideas.
- 08, 09, and 10 stay as research seeds until each has its own theorem not reducible to standard graph embedding, factorization-monoid, divisor-lattice, or geometric-topology facts.
- Prior art to audit explicitly: factorization monoids/categories, divisor graphs/posets, graph embeddings and planarity, outerplanar graphs, Turan extremality, clique complexes, lattice transformations, and geometric/topological equivalence of planar domains.
