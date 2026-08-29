# Upstream Memo Addendum — Directedness Is Not Essential

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Date:** 2026-08-28  
**Status:** theorem checkpoint

The directedness question is resolved negatively.

There exists a single simple undirected graph relation \(G\) on the dimension-2 payload carrier \(U=\mathbb N^2\) such that:

\[
\boxed{
\begin{array}{l}
\operatorname{dim}_{\rm self}=2;\\
1\text{ primitive binary relation};\\
1\text{ partial-operation layer};\\
1\text{ terminal output};\\
\text{symmetric};\\
\text{irreflexive};\\
\text{commutative domain};\\
C_4\text{-free};\\
\lambda^{\rm atomic}=2;\\
\Theta(N)\text{ primitive cost};\\
\text{payload-preserving};\\
\text{FO full order of type }\omega;\\
\neg\text{FO }+;\\
\neg\text{FO }\times.
\end{array}}
\]

The graph uses, for each off-diagonal payload point \((i,j)\):

- an undirected row-coordinate edge to \(d_i=(i,i)\);
- an undirected transpose edge to \((j,i)\);
- when \(i<j\), one additional edge to \(d_j\).

Diagonal points are exactly the infinite-degree vertices. Upper points are exactly off-diagonal vertices with two diagonal neighbors. The transpose partner is the unique non-diagonal neighbor. From these facts the ordered coordinate pair \((i,j)\) is FO-recovered, then the diagonal order, and finally the full shell order of type \(\omega\).

The primitive graph is \(C_4\)-free because any two vertices have at most one common neighbor. Therefore no atomic half-graph of depth 3 exists, while depth 2 occurs. Hence atomic ladder depth is exactly 2.

Primitive edge count on the shell window \(W_m=[0,m]^2\) is

\[
2m(m+1)=\Theta(|W_m|),
\]

so the intrinsic recovered-order cost remains linear.

The graph is FO-interdefinable with the earlier three-trace payload structure, so the pure-order dimension-2 provenance and arithmetic non-leakage proofs transfer unchanged.

Therefore directedness, primitive orientation, loops, multiple relations, multiple operation layers, multiple terminal outputs, unbounded primitive ladder depth, and superlinear primitive cost are all nonessential resources in the current provenance class.

The remaining visible structural resources are:

\[
\boxed{
\text{interpretation dimension }2
\quad+
\text{an infinite nonlocal core of infinite-degree coordinate hubs}.}
\]

In the current shell enumeration the number of diagonal hubs among the first \(N\) payload points is \(\Theta(\sqrt N)\). The Sparse Memory Threshold only requires this number to tend to infinity.

Hence the next sharp problem is:

> How sparse can the infinite-degree hub set be while retaining one relation, symmetry, \(C_4\)-freeness, \(\Theta(N)\) cost, payload preservation, FO full order, and no FO ordinary arithmetic?

Primary theorem file: `UNDIRECTED_SINGLE_RELATION_MEMORY.md`.
