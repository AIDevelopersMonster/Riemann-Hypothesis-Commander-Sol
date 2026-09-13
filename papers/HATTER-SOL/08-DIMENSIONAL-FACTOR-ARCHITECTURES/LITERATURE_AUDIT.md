# HATTER-SOL-08 · Literature audit

**Date:** 2026-09-12

## Classical layers that are not novelty claims

1. Planar graphs have at most `3n-6` edges and exclude `K_5`.
2. Outerplanar graphs have at most `2n-3` edges and exclude `K_4` and `K_{2,3}` minors.
3. Vertex splitting / detachment is classical.
4. Splitting-off / edge-splitting is classical, including variants constrained by connectivity and planarity.
5. Degree-realization problems for planar and outerplanar graph classes have a substantial literature.

## Closest prior art located

### Tibor Jordán — constrained edge-splitting

T. Jordán, *Constrained Edge-Splitting Problems*, SIAM Journal on Discrete Mathematics 17(1) (2003), 88–102. DOI `10.1137/S0895480199364483`.

The paper studies splitting-off operations under edge-connectivity constraints. This is relevant operational prior art but does not formulate the HATTER-SOL capacity-deficiency objective or an arithmetic split `ab -> (a,b)`.

### Nagamochi–Eades — planar edge splitting

H. Nagamochi, P. Eades, *An Edge-Splitting Algorithm in Planar Graphs*, Journal of Combinatorial Optimization 7 (2003), 137–159.

This is directly relevant to planarity-preserving edge-splitting as an established graph operation. HATTER-SOL-08 therefore must not claim novelty for preserving planarity under local splitting transformations.

### Gronemann–Nöllenburg–Villedieu — splitting plane graphs to outerplanarity

M. Gronemann, M. Nöllenburg, A. Villedieu, *Splitting Plane Graphs to Outerplanarity*, Journal of Graph Algorithms and Applications 28(3) (2024), 31–48. DOI `10.7155/jgaa.v28i3.2970`.

The paper treats vertex splitting as a graph-editing operation and minimizes the number of splits required to make a plane graph outerplane. This is important prior art for the geometry/topology side of the programme, but the objective differs from free-boundary sensitivity under multiplicative refinement.

### Bar-Noy et al. — outerplanar degree realization

A. Bar-Noy, T. Böhnlein, D. Peleg, Y. Ran, D. Rawitz, *Approximate realizations for outerplanaric degree sequences*, Journal of Computer and System Sciences 148 (2025), Article 103588. DOI `10.1016/j.jcss.2024.103588`.

This studies which degree sequences admit outerplanar realizations and supplies approximate realization criteria. It reinforces the point that outerplanar degree realization is nontrivial and that the exact outerplanar HATTER-SOL extremal function should remain open until proved.

## Negative search performed

Search terms included combinations of:

- planar graph vertex splitting consecutive rotation;
- planar splitting-off preserving planarity;
- edge splitting planar graphs;
- multiplicative refinement graph capacity;
- b-matching planar capacity split;
- degree-constrained planar graph sensitivity;
- outerplanar degree sequence realization;
- vertex split deficiency planar graph.

No explicit result was located equivalent to

\[
\Delta_{Pl}^{\max}(2,q)
\le
2\left\lceil\frac{3(q-2)}4\right\rceil-(q-2)
\]

for the HATTER-SOL free-boundary objective induced by replacing one arithmetic capacity `2q` by capacities `2,q` and re-optimizing the entire planar network.

This is a serious negative search, not an absolute priority guarantee.

## Publication-safe novelty framing

Recommended wording:

> Planarity-preserving splitting operations, vertex splitting, and degree-constrained graph realization are classical. We study a different sensitivity question: the change in minimum unused degree capacity when one arithmetic capacity `2q` is replaced by the multiplicatively linked pair `(2,q)` and the network is globally re-optimized. For planar networks we obtain a dimension-dependent upper bound that is asymptotically half of the unrestricted sharp amplitude.

## Hostile-audit note

An attempted stronger outerplanar bound based only on `K_4` exclusion failed. A seven-vertex counterexample shows that inserting a missing edge after deleting three spokes can create a `K_{2,3}` subdivision. The outerplanar strengthening is therefore explicitly retracted and must not be presented as a theorem.
