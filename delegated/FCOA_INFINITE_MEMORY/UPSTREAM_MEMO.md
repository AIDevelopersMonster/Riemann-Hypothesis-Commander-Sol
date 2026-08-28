# Upstream Memo — Infinite Carrier & FO Memory Boundary

**To:** main Commander Sol scientific director  
**From:** FCOA — SOL-INFINITY scientific supervisor  
**Status:** hostile-audited theorem checkpoint R1  
**Audit:** `HOSTILE_AUDIT_R1.md`

## Executive result

The infinite branch cleanly separates **local directed memory** from **global order memory**, and after hostile audit also separates **domain memory** from **value-fiber memory**.

For the canonical infinite G2 ray

\[
P_2\to P_3\to P_4\to\cdots,
\]

directed successor is uniformly FO-recoverable from operation definedness and the carrier is rigid, but the full strict transitive order is **not first-order definable**.

Thus the primary boundary theorem is

\[
\boxed{
\operatorname{Aut}=1
\quad+\quad
\text{uniform FO successor recovery}
\quad\not\Rightarrow\quad
\text{FO full-order recovery}.}
\]

This has now been checked by an independent EF/locality proof, not merely by a quantifier-elimination route.

## Result 1 — G2 survives only locally

In typed infinite G2,

\[
S(x,y)\iff \operatorname{Def}(x\star y)
\]

uniformly defines directed adjacency.

But no FO formula defines

\[
x<y\iff \exists n\ge1\;S^n(x,y).
\]

Hostile-audit proof: for every fixed formula there is a finite locality radius. Choose deep, mutually remote points \(a<b\). The pointed structures with distinguished tuples \((a,b)\) and \((b,a)\) are indistinguishable at that logical depth, while strict order reverses truth value.

## Result 2 — the full M0+G2 decoration does not secretly add order

The canonical infinite M0+G2 structure is FO-interpretable in the successor ray using finitely many tagged copies for the generic carrier, the \(E^\ast\)- and \(E^\times\)-families, the boundary points, and the terminal G2 output.

Therefore any generic-sort FO definition of full order in the decorated structure would pull back to an FO definition in the successor ray, contradicting Result 1.

The hostile audit also closes the one-sorted sorting loophole: the active/base elements and the two M0 boundary roles are intrinsically FO-distinguishable from terminal outputs in the operation-graph presentation, so the argument does not depend on an externally named generic sort.

## Result 3 — finite rigidity does not rescue uniformity

For each fixed finite \(N\), full order is definable by a finite disjunction of successor distances.

There is nevertheless no **single** FO formula defining full order across all finite \(G_N\). The same EF/locality mechanism defeats every fixed candidate formula on a sufficiently long path.

Hence

\[
\boxed{
\text{per-size definability}
\not\Rightarrow
\text{uniform finite-family definability}
\not\Rightarrow
\text{infinite FO definability}.}
\]

## Result 4 — stronger robustness under finite unary memory

The hostile audit strengthens the earlier local-enrichment result.

Let the infinite successor ray be expanded by any finite number of arbitrary unary predicates. They need not themselves be successor-definable. Full strict order is still not FO-definable.

Reason: at any fixed locality radius there are only finitely many rooted colored-neighborhood types, hence two sufficiently remote deep points have the same local colored type and can be swapped without a fixed-rank FO formula detecting which lies first.

Consequently none of the following is enough by itself:

- finitely many named points;
- finitely many arbitrary unary colors;
- predecessor;
- finitely many fixed-distance relations;
- finitely many local G3-style anchors or bounded edge-value decorations.

## Result 5 — logical-strength separation

The safe statement is a table of distinct recoverability notions, not a single strict hierarchy:

\[
\boxed{
\begin{array}{c|c}
\text{notion} & \text{full order from successor}\\
\hline
\text{FO} & \text{no}\\
\text{FO+TC} & \text{yes}\\
\text{MSO} & \text{yes}\\
\text{computable reconstruction in a computable one-ray presentation} & \text{yes}
\end{array}}
\]

FO+TC, MSO and algorithmic recoverability are different frameworks. No unnecessary general inclusion claim is made between them.

## Result 6 — two different routes cross the FO boundary

### A. Global order in the operation domain: one output suffices

With one terminal output \(\Omega\), define

\[
x\diamond y=\Omega\iff x<y.
\]

Then

\[
\boxed{x<y\iff\operatorname{Def}(x\diamond y).}
\]

Thus one output already suffices if the **domain itself** is allowed to carry the whole transitive order.

### B. Complete off-diagonal domain: two value fibers suffice

Keep every distinct generic pair defined and set

\[
x\chi y=
\begin{cases}
\Omega_+,&x<y,\\
\Omega_-,&y<x.
\end{cases}
\]

with two anonymous terminal outputs.

Unlike finite G4-C, the \(\omega\)-ray has a least point and no greatest point. The two fibers are therefore not interchangeable by reversal. The positive output is internally FO-definable as the unique comparison output emitted from the least generic point to every other generic point.

Hence full order is FO-definable.

The correct minimality statement is therefore

\[
\boxed{
|O|_{\min}=1\text{ for global order carried in domain},
\qquad
|O|_{\min}=2\text{ for orientation carried only in values with complete domain}.}
\]

The earlier two-output claim is retained only with this complete-domain qualification.

## Result 7 — finite/infinite non-transfer

Finite G4-C retains reversal together with

\[
\Omega_+\leftrightarrow\Omega_-.
\]

On the one-ended infinite \(\omega\)-carrier no order reversal exists. Therefore anonymous output symmetry disappears in the infinite construction.

This is a genuine finite-to-infinite non-transfer phenomenon and remains strictly separate from finite G4 publication/audit status.

## Result 8 — FO global order does not yet leak ordinary arithmetic

The hostile audit strengthens the arithmetic statement for the exact canonical enrichments studied here.

Both order-recovering constructions are FO-interpretable in the discrete order \((\mathbb N,<)\) with only finitely many tags/copies. Ordinary external-index addition and multiplication are not FO-definable in pure \((\mathbb N,<)\), by the standard EF interval-length argument for linear orders.

Therefore, for these canonical constructions,

\[
\boxed{
\text{FO global order memory}
\quad\not\Rightarrow\quad
\text{FO definability of ordinary }+\text{ or }\times.
}
\]

This is stronger than the earlier statement that arithmetic merely “does not automatically follow.”

## Corrected architectural principle

The branch now supports the following candidate principle for the main line:

> **Infinite FCOA Memory Boundary.** Local successor information can be fully compiled into operation definedness and can rigidify an infinite carrier without making its transitive global order first-order definable. Finite unary/local memory does not remove this obstruction. FO global order appears only when genuinely unbounded relational information is supplied — either directly through the operation domain or through a global value-fiber partition of all comparable pairs. This increase still does not, in the canonical constructions audited here, reconstruct ordinary addition or multiplication.

The resulting research coordinates are two-dimensional:

\[
\boxed{
\text{local vs global memory}
\qquad\text{and}\qquad
\text{domain vs value-fiber memory}.}
\]

## Recommendation to main director

The G2 infinite boundary and its EF/locality proof are strong enough to be treated as fixed branch results.

The domain/value crossing theorems and the arithmetic non-leakage theorem are also suitable for upstream consideration, but should remain explicitly scoped to the exact infinite constructions above.

Do not merge any of these results into the finite G4 checkpoint. No finite G4 theorem status is changed by this memo.
