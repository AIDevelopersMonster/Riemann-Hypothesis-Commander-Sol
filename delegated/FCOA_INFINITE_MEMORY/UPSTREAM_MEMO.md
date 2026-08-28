# Upstream Memo — Infinite Carrier & FO Memory Boundary

**To:** main Commander Sol scientific director  
**From:** FCOA — SOL-INFINITY scientific supervisor  
**Status:** hostile-audited theorem checkpoint R1 + sparse-memory threshold + order-only quadratic barrier  
**Audit:** `HOSTILE_AUDIT_R1.md`  
**Sparse threshold:** `SPARSE_MEMORY_THRESHOLD.md`  
**Order-only density theorem:** `ORDER_ONLY_QUADRATIC_BARRIER.md`

## Executive result

The infinite branch now separates four independent coordinates:

\[
\boxed{
\text{local vs global memory},
\qquad
\text{domain vs value-fiber memory},
\qquad
\text{local finiteness vs infinite nonlocal core},
\qquad
\text{order-only geometry vs primitive non-order global skeleton}.}
\]

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

This has been checked by an independent EF/locality proof.

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

## Result 4 — robustness under finite unary memory

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

The correct minimality statement is

\[
\boxed{
|O|_{\min}=1\text{ for global order carried in domain},
\qquad
|O|_{\min}=2\text{ for orientation carried only in values with complete domain}.}
\]

## Result 7 — finite/infinite non-transfer

Finite G4-C retains reversal together with

\[
\Omega_+\leftrightarrow\Omega_-.
\]

On the one-ended infinite \(\omega\)-carrier no order reversal exists. Therefore anonymous output symmetry disappears in the infinite construction.

This is a genuine finite-to-infinite non-transfer phenomenon and remains strictly separate from finite G4 publication/audit status.

## Result 8 — FO global order does not yet leak ordinary arithmetic

Both canonical order-recovering constructions are FO-interpretable in the discrete order \((\mathbb N,<)\) with only finitely many tags/copies. Ordinary external-index addition and multiplication are not FO-definable in pure \((\mathbb N,<)\), by the standard EF interval-length argument for linear orders.

Therefore, for these canonical constructions,

\[
\boxed{
\text{FO global order memory}
\quad\not\Rightarrow\quad
\text{FO definability of ordinary }+\text{ or }\times.
}
\]

## Result 9 — Sparse Memory Threshold

For a finite-signature structure, remove a finite set of boundary/terminal apex elements but retain every relation they induce on the remaining active carrier via the finite trace structure. If this trace structure is locally finite, then no FO formula defines a strict linear order on the infinite target domain.

For finitely many binary finite-output FCOA layers, if

\[
H=\{x:\deg_\Gamma(x)=\infty\}
\]

is finite, then after tracing out those finitely many hubs the residual active structure is locally finite. Therefore

\[
\boxed{
\text{FO full order in binary finite-output FCOA}
\Longrightarrow
|H|=\infty.}
\]

So finitely many universal hubs are not enough; crossing the FO boundary requires an **infinite active nonlocal core**.

## Result 10 — Order-Only Quadratic Barrier

The sparse-memory search is now closed for the natural **order-only** admissibility class.

Formalize “no imported arithmetic on external indices” conservatively by requiring every new binary domain/value-fiber relation to be FO-definable in the pure external discrete order \((G_\omega,<)\) with only finitely many boundary parameters.

For any such binary relation \(R(x,y)\), quantifier elimination for the discrete order gives a tail dichotomy:

\[
\boxed{
|R\cap[N]^2|=O(N)
\quad\text{or}\quad
|R\cap[N]^2|=\Theta(N^2).
}
\]

There is no genuinely intermediate binary density such as \(N\log N\) or \(N^{3/2}\) inside this order-only class. If all finitely many basic memory relations are in the linear regime, their finite union is finite-apex locally finite, so the Sparse Memory Threshold forbids FO order.

Therefore:

\[
\boxed{
\text{order-only binary finite-output FCOA}
+\text{ FO full-order recovery}
\Longrightarrow
\Theta(N^2)\text{ generic interaction cells}.}
\]

This makes the complete order-in-domain and complete two-value comparison constructions **asymptotically optimal** in the order-only binary class.

The result also clarifies the remaining search space: any genuine subquadratic candidate must introduce a primitive global skeleton that is not FO-generated from pure order. Such a skeleton is not automatically arithmetic, but it requires a separate source/admissibility audit and a separate Arithmetic Leakage audit.

## Calibration result — sparse arithmetic-derived thresholds exist, but are inadmissible as direct FCOA constructions

As a mathematical benchmark, a threshold relation of the form

\[
R_f(x,y)\iff f(x)\le y
\]

can compress pairwise comparison if one imports a rapidly growing external function \(f\). For example, using \(f(x)=x^2\) produces only \(\Theta(N^{3/2})\) true pairs on an initial segment while allowing order to be recovered through first-order comparison of threshold fibers.

Classical work of Semenov shows that adding such a function to pure order can remain decidable while adding it to Presburger arithmetic can make the theory undecidable; hence multiplication (and in the relevant formulations addition together with the function) is not simply forced by the ordered expansion. This is useful calibration, not an admissible FCOA construction: the square function itself was imported from external arithmetic and therefore violates the branch's source discipline.

## Corrected architectural principle

The branch now supports the following candidate principle for the main line:

> **Infinite FCOA Memory Boundary.** Local successor information can be fully compiled into operation definedness and can rigidify an infinite carrier without making its transitive global order first-order definable. Finite unary/local memory and, more generally, finite-apex locally-finite active memory do not remove this obstruction. In binary finite-output FCOA, FO recovery of full order requires infinitely many genuinely nonlocal active locations. If the new binary geometry is compiled only from the pure external order, then an even stronger barrier holds: quadratic pair density is asymptotically unavoidable. Any subquadratic solution must therefore import a new primitive global skeleton and undergo a separate arithmetic-leakage audit.

## Recommendation to main director

The G2 infinite boundary, hostile-audited EF/locality proof, Sparse Memory Threshold, and Order-Only Quadratic Barrier are strong enough to be treated as fixed branch results.

The order-only sparse-memory problem is now asymptotically closed. The remaining open problem is narrower and more interesting:

> find, or rule out, a natural primitive non-order global skeleton on the same carrier with subquadratic incidence, FO-definable full order, and provably no FO definition of ordinary addition or multiplication.

Do not merge any of these results into the finite G4 checkpoint. No finite G4 theorem status is changed by this memo.
