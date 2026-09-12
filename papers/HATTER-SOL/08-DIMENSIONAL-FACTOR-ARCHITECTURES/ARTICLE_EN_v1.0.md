# HATTER-SOL-08 · From a Line to Space

## Dimensional suppression of factor-architecture sensitivity

**Malachevsky, A.A.**  
ORCID: `0009-0008-6009-3196`  
Commander Sol / Hatter Sol Research Series  
Version: `v1.0` · 2026-09-13  
Parent work: HATTER-SOL-07, DOI `10.5281/zenodo.22724185`

## Abstract

HATTER-SOL-07 interpreted factors as vertices with upper degree capacities, and used the free boundary of a network to measure unused aggregate capacity. Here we ask how the same arithmetic refinement responds when the admissible network is restricted to different geometric graph classes.

For a capacity vector `c=(c_1,...,c_k)` and a graph class `C`, define

\[
M_C(\mathbf c)=\max |E(G)|,
\qquad
\lambda_C(\mathbf c)=\sum_i c_i-2M_C(\mathbf c),
\]

where the maximum is taken over connected simple `C`-graphs satisfying `deg(v_i)<=c_i`.

Three distinct regimes appear. In strict one dimension, the admissible connected architecture is a path, and every multiplicative split `ab->(a,b)` strictly decreases the minimum free boundary:

\[
\lambda_{1D}(\mathbf c')-\lambda_{1D}(\mathbf c)
=-(ab-a-b+2)<0.
\]

Thus refinement inversion is impossible in 1D. Already in the outerplanar class there are explicit families in which the same arithmetic refinement reverses sign. For planar networks we prove a quantitative suppression bound for the split `2q->(2,q)`:

\[
\Delta_{Pl}^{\max}(2,q)
\le
2\left\lceil\frac{3(q-2)}4\right\rceil-(q-2).
\]

In the unrestricted / 3D class, HATTER-SOL-07 gives the exact value

\[
\Delta_{3D}^{\max}(2,q)=q-2.
\]

Hence for every `q>=6`, the planar worst-case amplitude is strictly smaller than the unrestricted one, and asymptotically the planar amplitude is bounded by roughly one half of the 3D amplitude. The paper carefully separates classical vertex splitting and splitting-off operations from the new sensitivity question: the response of minimum unused degree capacity to an arithmetically linked factor split under global re-optimization of the network.

**Keywords:** factorization, planar graphs, vertex splitting, splitting-off, degree constraints, free boundary, refinement inversion, dimensional sensitivity.

## 1. From a number to an architecture

The previous paper in the series introduced a factor-capacity network: a factor `m` is treated as a vertex with capacity `m`, and graph edges consume available ports. For a graph `G` with capacities `c_i`, the free boundary is

\[
B(G;\mathbf c)=\sum_i(c_i-\deg(v_i))
=\sum_i c_i-2|E(G)|.
\]

The minimum free boundary at fixed capacities is

\[
\lambda(\mathbf c)=\min_G B(G;\mathbf c).
\]

HATTER-SOL-07 proved that under the split

\[
ab\to(a,b)
\]

in the unrestricted simple-graph class,

\[
\lambda(\mathbf c')-\lambda(\mathbf c)\le ab-a-b,
\]

and that this bound is sharp for every pair `a,b>=2`.

The present paper changes the question: what happens if the same capacities must be realized inside a prescribed dimensional graph class?

## 2. Dimensional architecture classes

We consider

\[
P\subset O\subset Pl\subset A,
\]

where:

- `P` denotes strict 1D architectures, i.e. paths;
- `O` denotes outerplanar / one-page architectures;
- `Pl` denotes planar graphs;
- `A` denotes all finite simple graphs, corresponding to unrestricted crossing-free straight-line realizability in 3D.

For each class `C`, define

\[
M_C(\mathbf c)=
\max\{|E(G)|:G\in C,\;G\text{ connected},\;\deg(v_i)\le c_i\},
\]

\[
\lambda_C(\mathbf c)=\sum_i c_i-2M_C(\mathbf c).
\]

Class inclusion gives immediately

\[
\lambda_P\ge\lambda_O\ge\lambda_{Pl}\ge\lambda_A.
\]

### 2.1. Complete-capacity calibration staircase

For

\[
\mathbf c^{(k)}=(k-1,\ldots,k-1),\qquad k\ge4,
\]

the degree caps do not constrain the extremal graph in each architecture class. Classical edge bounds therefore give

\[
\lambda_{1D}=(k-1)(k-2),
\]

\[
\lambda_{outer}=(k-2)(k-3),
\]

\[
\lambda_{planar}=(k-3)(k-4),
\]

\[
\lambda_{3D}=0.
\]

This is a calibration family obtained from classical extremal graph theory and is not itself a novelty claim.

## 3. Exact law in 1D

### Theorem 3.1

Let `k>=2` and `c_i>=2`. Then

\[
\boxed{
\lambda_P(\mathbf c)=\sum_i c_i-2(k-1).
}
\]

**Proof.** A connected simple graph realized on a line without overlapping edge interiors is a path. Since every capacity is at least two, the path is feasible. Hence `M_P=k-1`, and the formula follows directly. □

### Corollary 3.2

Under one multiplicative refinement

\[
ab\to(a,b),
\]

we have

\[
\boxed{
\lambda_P(\mathbf c')-\lambda_P(\mathbf c)
=-(ab-a-b+2)<0.
}
\]

Thus refinement inversion is impossible in strict 1D.

## 4. Explicit sign reversal

Let `q>=3` be odd and `m>=2q`. Consider

\[
\mathbf A=(2q,2^m)
\]

and the refinement

\[
\mathbf A'=(q,2^{m+1}).
\]

The HATTER-SOL-07 construction for `A` is an outerplanar cactus of cycles sharing one hub and saturates all ports, so

\[
\lambda_O(\mathbf A)=0.
\]

For `A'`, a bouquet of triangles plus one tail is also outerplanar and has exactly one free port; odd total capacity supplies the matching lower bound. Therefore

\[
\lambda_O(\mathbf A')=1.
\]

Hence

\[
\Delta_O=\Delta_{Pl}=\Delta_A=+1.
\]

But Theorem 3.1 gives in strict 1D

\[
\Delta_P=-q.
\]

Thus the same arithmetic refinement reverses the sign of its response when one passes from a strict line to a richer topology.

For `q=3`,

\[
\boxed{
\Delta_O^{\max}(2,3)
=
\Delta_{Pl}^{\max}(2,3)
=
\Delta_A^{\max}(2,3)=1,
}
\]

while

\[
\Delta_P^{\max}(2,3)=-3.
\]

## 5. Connectivity of planar maxima

### Lemma 5.1

For capacities `c_i>=2`, the maximum number of edges among simple planar graphs satisfying `deg(v_i)<=c_i` is attained by a connected graph.

**Proof.** Choose a maximum-edge feasible planar graph with the minimum number of connected components. If two distinct components contain unsaturated vertices, connect them by a new edge through the common exterior face, increasing the edge count, a contradiction.

Hence at most one component contains an unsaturated vertex. Every saturated nontrivial component has minimum degree at least two and therefore contains a cycle and a nonbridge edge.

If another component contains an unsaturated vertex `z`, delete a nonbridge edge `xy` in a saturated component and add `xz`, choosing embeddings so the relevant faces are outer. Edge count and degree feasibility are preserved while the number of components decreases.

If both components are saturated, delete nonbridge edges `xy` and `uv`, then reconnect the two components by `xu` and `yv` in the exterior face, reflecting one component if necessary to avoid crossings. Degrees and edge count are preserved while the number of components decreases. Contradiction. □

## 6. The planar four-block reduction

### Lemma 6.1

Suppose that in a fixed plane embedding four consecutive edges around a vertex `x` lead to distinct neighbors `a,b,c,d`. Then one can lower the degree of `x` by four while losing at most three edges, preserving planarity, simplicity, and all upper degree bounds.

**Proof.** If all six pairs among `a,b,c,d` were edges, then together with `x` the graph would contain `K_5`, impossible in a planar graph. Thus choose a nonadjacent pair `u,v` among these four neighbors.

Delete the four spokes from `x` to this block. Since the incidences are consecutive, their deletion frees a local topological sector. Inside a sufficiently small disk around the deleted arcs `ux` and `xv` and the now-empty neighborhood of `x`, draw a new edge `uv`. It does not cross the remaining drawing. Because `uv` was absent, simplicity is preserved. At `u` and `v`, one deleted edge is replaced by one new edge, so their degrees do not increase. The degree of `x` drops by four and the total edge count drops by three. □

Repeating the operation on disjoint consecutive blocks and deleting any remainder of `0,1,2,3` incidences gives

\[
\boxed{
L_{Pl}(r)\le
3\left\lfloor\frac r4\right\rfloor+(r\bmod4)
=\left\lceil\frac{3r}{4}\right\rceil.
}
\]

## 7. Main theorem: planar suppression

Consider

\[
2q\to(2,q),\qquad q\ge3,
\]

and write

\[
\delta=q-2.
\]

### Theorem 7.1

For every ambient capacity vector,

\[
\boxed{
\lambda_{Pl}(\ldots,2,q,\ldots)
-
\lambda_{Pl}(\ldots,2q,\ldots)
\le
2\left\lceil\frac{3(q-2)}4\right\rceil-(q-2).
}
\]

Equivalently,

\[
\boxed{
\Delta_{Pl}^{\max}(2,q)
\le
U_{Pl}(q):=
2\left\lceil\frac{3(q-2)}4\right\rceil-(q-2).
}
\]

**Proof.** Take a maximum-edge planar graph before refinement and let `d` be the degree of the capacity-`2q` vertex.

If `d<=q+2`, split the vertex locally into capacities `2` and `q` by dividing the cyclic incidence order into two contiguous intervals; no edge loss is needed.

If `d>q+2`, set

\[
r=d-(q+2)\le q-2=\delta.
\]

Lemma 6.1 reduces the degree by `r` at a loss of at most `ceil(3r/4)` edges. Then perform the local vertex split. By Lemma 5.1 the maximum attainable edge count may be taken connected. Therefore

\[
M_{Pl}(\mathbf c')
\ge
M_{Pl}(\mathbf c)-\left\lceil\frac{3r}{4}\right\rceil.
\]

The total capacity decreases by `delta`, hence

\[
\lambda_{Pl}(\mathbf c')-\lambda_{Pl}(\mathbf c)
\le
-\delta+2\left\lceil\frac{3r}{4}\right\rceil
\le
-\delta+2\left\lceil\frac{3\delta}{4}\right\rceil.
\]

This is the claimed bound. □

## 8. Separating 2D from 3D

In the unrestricted / 3D class, HATTER-SOL-07 gives

\[
\boxed{
\Delta_A^{\max}(2,q)=q-2.
}
\]

For `q>=6`,

\[
U_{Pl}(q)<q-2.
\]

### Corollary 8.1

For every `q>=6`,

\[
\boxed{
\Delta_{Pl}^{\max}(2,q)
<
\Delta_A^{\max}(2,q).
}
\]

Hence there is an infinite family of arithmetic refinement operations for which planar geometry strictly suppresses the worst-case inversion amplitude relative to unrestricted 3D architecture.

Asymptotically,

\[
U_{Pl}(q)=\frac{q-2}{2}+O(1),
\]

whereas

\[
\Delta_A^{\max}(2,q)=q-2.
\]

Thus the planar amplitude is bounded by approximately one half of the unrestricted amplitude.

For odd `q>=7`, the explicit outerplanar family also yields

\[
1\le\Delta_{Pl}^{\max}(2,q)<q-2,
\]

so positive refinement inversion survives, but its worst-case amplitude is reduced.

## 9. Small cases

For `q=3,4,5,6,7`, the planar upper bound is respectively

\[
1,2,3,2,3.
\]

Thus strict planar/3D separation begins at `q=6` at the level of the proven bound:

\[
\Delta_{Pl}^{\max}(2,6)\le2<4=\Delta_A^{\max}(2,6).
\]

## 10. What is classical and what is claimed here

Classical ingredients include planar extremal bounds, `K_5` exclusion, vertex splitting, edge splitting / splitting-off, and planar or outerplanar degree-realization problems.

Relevant prior work includes Jordán on constrained edge-splitting, Nagamochi–Eades on planar edge-splitting, Gronemann–Nöllenburg–Villedieu on splitting plane graphs to outerplanarity, and Bar-Noy et al. on outerplanar degree realization.

Our claim is narrower: we do not introduce a new splitting operation. We study the **sensitivity of minimum unused degree capacity to the arithmetically linked split `2q->(2,q)` under global re-optimization inside a prescribed dimensional graph class**.

A targeted literature search did not locate an equivalent of Theorem 7.1. This is a negative search, not an absolute claim of historical priority.

## 11. Hostile audit and a retracted outerplanar conjecture

An earlier draft proposed a stronger outerplanar bound based on triples of neighbors and `K_4` exclusion. A hostile audit found a seven-vertex counterexample: after deleting three spokes, inserting a missing edge can create a subdivision of `K_{2,3}`. The stronger outerplanar formula and the resulting exact `q=5` claim were therefore withdrawn.

This negative result is methodologically useful: clique exclusion is sufficient for the local planar-disk argument but not for outerplanarity, whose one-page structure imposes additional global constraints.

## 12. Conclusion

The dimensional response law is now:

\[
\boxed{\text{1D: refinement inversion is impossible}}
\]

\[
\boxed{\text{2D planar: inversion is possible, but worst-case amplitude is suppressed}}
\]

\[
\boxed{\text{3D/unrestricted: the full amplitude }q-2\text{ is attainable}.}
\]

Dimension is therefore not merely a visual property of a representation; it becomes a parameter controlling the sensitivity of an optimized factor architecture to arithmetic refinement.

## AI role

This research was developed in dialogue with Commander Sol / Hatter Sol (OpenAI) for hypothesis generation, counterexample search, hostile proof audit, literature search, and proof structuring. Responsibility for the mathematical claims and publication version rests with the author.

## References

1. Malachevsky, A.A. *Alice in the Land of Free Threads: Factors as Nodes and the Exact Cost of Multiplicative Splitting*. HATTER-SOL-07, Zenodo (2026). DOI: `10.5281/zenodo.22724185`.
2. Jordán T. Constrained Edge-Splitting Problems. *SIAM Journal on Discrete Mathematics* 17(1) (2003), 88–102. DOI: `10.1137/S0895480199364483`.
3. Nagamochi H., Eades P. An Edge-Splitting Algorithm in Planar Graphs. *Journal of Combinatorial Optimization* 7(2) (2003), 137–159. DOI: `10.1023/A:1024470929537`.
4. Gronemann M., Nöllenburg M., Villedieu A. Splitting Plane Graphs to Outerplanarity. *Journal of Graph Algorithms and Applications* 28(3) (2024), 31–48. DOI: `10.7155/jgaa.v28i3.2970`.
5. Bar-Noy A., Böhnlein T., Peleg D., Ran Y., Rawitz D. Approximate realizations for outerplanaric degree sequences. *Journal of Computer and System Sciences* 148 (2025), 103588. DOI: `10.1016/j.jcss.2024.103588`.
6. Korte B., Vygen J. *Combinatorial Optimization: Theory and Algorithms*. 6th ed. Springer, 2018. DOI: `10.1007/978-3-662-56039-6`.

**Status:** `v1.0` · final publication edition · 2026-09-13. HATTER-SOL-08 DOI is assigned upon Zenodo deposit.
