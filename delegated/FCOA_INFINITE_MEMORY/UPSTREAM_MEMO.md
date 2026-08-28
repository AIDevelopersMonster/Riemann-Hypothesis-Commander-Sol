# Upstream Memo — Infinite Carrier & FO Memory Boundary

**To:** main Commander Sol scientific director  
**From:** FCOA — SOL-INFINITY scientific supervisor  
**Status:** hostile-audited theorem checkpoint R1 + sparse-memory threshold + order-only quadratic barrier + primitive subquadratic existence theorem  
**Audit:** `HOSTILE_AUDIT_R1.md`  
**Sparse threshold:** `SPARSE_MEMORY_THRESHOLD.md`  
**Order-only density theorem:** `ORDER_ONLY_QUADRATIC_BARRIER.md`  
**Primitive subquadratic theorem:** `SUBQUADRATIC_PRIMITIVE_SKELETON.md`

## Executive result

The infinite branch now separates five independent coordinates:

\[
\boxed{
\text{local vs global memory},
\quad
\text{domain vs value-fiber memory},
\quad
\text{local finiteness vs infinite nonlocal core},
\quad
\text{order-only vs primitive non-order geometry},
\quad
\text{source safety vs internal arithmetic leakage}.}
\]

For the canonical infinite G2 ray

\[
P_2\to P_3\to P_4\to\cdots,
\]

directed successor is uniformly FO-recoverable from operation definedness and the carrier is rigid, but the full strict transitive order is not first-order definable.

Thus the primary boundary theorem remains

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

uniformly defines directed adjacency, but no FO formula defines

\[
x<y\iff \exists n\ge1\;S^n(x,y).
\]

## Result 2 — full M0+G2 does not secretly add order

The canonical infinite M0+G2 structure is FO-interpretable in the successor ray using finitely many tagged copies for the generic carrier, the \(E^\ast\)- and \(E^\times\)-families, the boundary points, and the terminal G2 output. Therefore any generic-sort FO definition of full order would pull back to one in the successor ray.

## Result 3 — no uniform finite-family formula

For each fixed finite \(N\), full order is definable by a finite disjunction of successor distances, but there is no single FO formula defining full order across all finite \(G_N\). Hence

\[
\boxed{
\text{per-size definability}
\not\Rightarrow
\text{uniform finite-family definability}
\not\Rightarrow
\text{infinite FO definability}.}
\]

## Result 4 — finite unary memory is still insufficient

Any finite number of arbitrary unary predicates on the infinite successor ray still fails to make the full strict order FO-definable. Thus finitely many named points, unary colors, predecessor, finitely many fixed-distance relations, and finitely many local G3-style anchors remain below the boundary.

## Result 5 — logical-strength separation

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

No unnecessary inclusion claim is made between the logical and algorithmic notions.

## Result 6 — two routes cross the FO boundary

### A. Order in the domain: one output

\[
x\diamond y=\Omega\iff x<y.
\]

Then \(x<y\) is exactly definedness.

### B. Complete domain, order in values: two outputs

\[
x\chi y=
\begin{cases}
\Omega_+,&x<y,\\
\Omega_-,&y<x.
\end{cases}
\]

On the one-ended \(\omega\)-carrier the positive output is intrinsically FO-definable because there is a least point but no greatest point. Hence full order is FO-definable.

The exact minimality split is

\[
\boxed{
|O|_{\min}=1\text{ for order in the domain},
\qquad
|O|_{\min}=2\text{ for orientation carried only in values with complete domain}.}
\]

## Result 7 — finite/infinite non-transfer

Finite G4-C retains reversal together with \(\Omega_+\leftrightarrow\Omega_-\). On the one-ended infinite \(\omega\)-carrier no order reversal exists. Thus anonymous output symmetry can disappear in the infinite limit.

## Result 8 — global order does not automatically leak arithmetic

The two canonical dense order-recovering constructions are FO-interpretable in \((\mathbb N,<)\) with finitely many tags/copies. Ordinary external-index addition and multiplication are not FO-definable there. Hence, for those exact constructions,

\[
\boxed{
\text{FO global order memory}
\not\Rightarrow
\text{FO ordinary arithmetic}.}
\]

## Result 9 — Sparse Memory Threshold

For a finite-signature structure, remove a finite boundary/terminal apex set but retain every induced relation in the finite trace structure. If the resulting trace is locally finite, no FO formula defines a strict linear order on the infinite target domain.

For finitely many binary finite-output FCOA layers, if

\[
H=\{x:\deg_\Gamma(x)=\infty\}
\]

is finite, then FO order is impossible. Therefore

\[
\boxed{
\text{FO full order}
\Longrightarrow
|H|=\infty.}
\]

Crossing the boundary requires an infinite active nonlocal core.

## Result 10 — Order-Only Quadratic Barrier

If every new binary domain/value-fiber relation is FO-generated from the pure external discrete order with only finitely many boundary parameters, then every such relation has asymptotic density either

\[
O(N)
\]

or

\[
\Theta(N^2).
\]

There is no genuinely intermediate binary density. Combining this with the Sparse Memory Threshold gives

\[
\boxed{
\text{order-only binary finite-output FCOA}
+\text{ FO full-order recovery}
\Longrightarrow
\Theta(N^2)\text{ generic interaction cells}.}
\]

Thus the dense order-in-domain and complete two-value comparison constructions are asymptotically optimal inside the order-only class.

## Result 11 — Primitive Subquadratic Skeleton exists

The previously open existence question now has a positive mathematical answer once one permits a primitive non-order global skeleton.

Let \(f\) be any strictly increasing cofinal jump map and define nested tails

\[
R_f(Q_n,Q_m)\iff m\ge f(n).
\]

The carrier order is FO-recoverable by strict inclusion of rows:

\[
Q_n<Q_k
\iff
N_f(k)\subsetneq N_f(n).
\]

The jump map itself is FO-recoverable as the least element of each row.

### Exact quadratic-growth witness

Take

\[
f_1(n)=(n+1)^2.
\]

Then the number of true incidences in the first \(N\) points is

\[
\boxed{
C_1(N)=\frac23N^{3/2}+O(N).
}
\]

So

\[
C_1(N)=o(N^2).
\]

Yet the full order is FO-definable.

### Internal arithmetic leakage is absent

The structure \((G_\omega,R_1)\) is FO-interdefinable with \((\mathbb N,<,(n+1)^2)\), hence with the classical quadratic expansion \((\mathbb N,<,n^2)\). Semenov proved that the latter has decidable elementary theory, while the corresponding expansion with addition is undecidable.

Therefore ordinary addition cannot be FO-definable from \(R_1\). Multiplication cannot be FO-definable either: in the presence of discrete order/successor, multiplication would give addition by the classical Julia Robinson definability result.

Thus

\[
\boxed{
R_1\Rightarrow_{\rm FO}<,
\qquad
R_1\not\Rightarrow_{\rm FO}+,
\qquad
R_1\not\Rightarrow_{\rm FO}\times.
}
\]

This closes the **logical existence** question positively.

### Finite-substitution provenance candidate

The same jump sequence can be generated by the finite morphism

\[
\sigma(A)=ABBC,
\qquad
\sigma(B)=BC,
\qquad
\sigma(C)=C,
\]

because

\[
|\sigma^n(A)|=(n+1)^2.
\]

So the primitive rule need not literally invoke external-index multiplication or squaring. Squaring appears as a theorem about the growth of a finite substitution system.

Current provenance status:

\[
\boxed{
\text{INTERNAL LEAKAGE: PASS},
\qquad
\text{SOURCE SAFETY: CANDIDATE PASS pending hostile provenance audit}.}
\]

No novelty claim is made for finite substitutions themselves.

### Arbitrarily near-linear family

Let \(F_k=f_1^{\circ k}\) and

\[
R_k(Q_n,Q_m)\iff m\ge F_k(n).
\]

Then \(F_k\) has degree \(2^k\), so

\[
\boxed{
C_k(N)=\Theta\!\left(N^{1+1/2^k}\right).
}
\]

For every fixed \(k\), the theory remains decidable as a reduct of the decidable quadratic expansion, while addition and multiplication remain FO-undefinable.

Therefore for every \(\varepsilon>0\) there exists a fixed finite-signature primitive skeleton with

\[
\boxed{
C(N)=O(N^{1+\varepsilon})
}
\]

that FO-recovers order but not ordinary \(+\) or \(\times\).

Hence there is no universal fixed superlinear-power lower bound once primitive non-order skeletons are admitted.

## Rejected comparison — binary tree/equal-level skeleton

A natural sparse candidate based on finite binary words, prefix, equal-level, and last-letter predicates is too expressive for the arithmetic-safe target: the standard universal automatic structure FO-defines exactly synchronous regular relations, and binary addition is synchronous regular. Thus hierarchical sparsity alone does not guarantee arithmetic safety.

## Corrected architectural principle

The branch now supports the stronger picture:

> **Infinite FCOA Memory Boundary.** Local successor memory can rigidify an infinite carrier without FO global order. Finite-apex local memory remains insufficient, and binary order-only compilation pays an unavoidable quadratic density cost. However, once a genuinely primitive non-order global skeleton is admitted, subquadratic arithmetic-safe order memory exists. A nested-tail skeleton generated by a finite substitution gives an exact \(\Theta(N^{3/2})\) candidate, and fixed iterates yield \(O(N^{1+\varepsilon})\) density for every prescribed \(\varepsilon>0\), while ordinary addition and multiplication remain FO-undefinable.

## Recommendation to main director

The following are strong enough to be treated as fixed branch mathematics:

- G2 infinite FO boundary;
- hostile-audited EF/locality proof;
- Sparse Memory Threshold;
- Order-Only Quadratic Barrier;
- logical existence of subquadratic nested-tail order memory with no FO \(+\) or \(\times\) leakage.

The finite-substitution provenance should remain a candidate until a dedicated hostile source-safety audit decides whether deriving the threshold sequence from substitution-growth lengths satisfies the programme's strongest interpretation of “do not import arithmetic on external indices”.

The remaining frontier is no longer existence. It is:

1. hostile provenance audit of the substitution-generated skeleton;
2. determine whether one can obtain a **single** \(O(N\log N)\), near-linear, or \(N^{1+o(1)}\) source-safe skeleton;
3. classify which natural sparse global skeletons cross into arithmetic and which do not.

Do not merge any infinite result into finite G4. No finite G4 theorem status is changed by this memo.
