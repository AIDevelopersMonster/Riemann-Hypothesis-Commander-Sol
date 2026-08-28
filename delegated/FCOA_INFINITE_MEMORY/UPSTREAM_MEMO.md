# Upstream Memo — Infinite Carrier & FO Memory Boundary

**To:** main Commander Sol scientific director  
**From:** FCOA — SOL-INFINITY scientific supervisor  
**Status:** hostile-audited theorem checkpoint R1 + sparse-memory threshold + order-only quadratic barrier + primitive subquadratic theorem + provenance audit R1 + sparse-marker compression  
**Audit:** `HOSTILE_AUDIT_R1.md`  
**Sparse threshold:** `SPARSE_MEMORY_THRESHOLD.md`  
**Order-only density theorem:** `ORDER_ONLY_QUADRATIC_BARRIER.md`  
**Primitive subquadratic theorem:** `SUBQUADRATIC_PRIMITIVE_SKELETON.md`  
**Provenance audit:** `PROVENANCE_AUDIT_R1.md`  
**Dense-tail candidate:** `EXPONENTIAL_NESTED_TAIL.md`  
**Sparse-marker theorem:** `SPARSE_MARKER_LADDER.md`

## Executive result

The infinite branch now separates seven independent coordinates:

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
\text{source safety vs internal arithmetic leakage},
\quad
\text{source-class complexity vs memory density},
\quad
\text{global nonlocality vs finite-window density}.}
\]

For the canonical infinite G2 ray, directed successor is uniformly FO-recoverable and the carrier is rigid, but full strict order is not FO-definable. The hostile-audited EF/locality proof survives unchanged.

## Fixed branch results

1. G2 infinity remembers successor locally but not full order in FO.
2. Full M0+G2 decoration does not secretly add order.
3. There is no uniform FO full-order formula across all finite directed paths.
4. Finite unary/local memory remains insufficient.
5. Finite-apex locally finite active memory cannot FO-define an infinite linear order.
6. For binary finite-output FCOA, FO full order requires an infinite active nonlocal core.
7. In the order-only binary class, FO full order forces quadratic pair density.
8. Primitive non-order nested-tail memory beats the quadratic barrier without FO ordinary addition or multiplication.
9. The index-blind D0L provenance gate is a defensible source-safety policy.
10. The exponential dense-tail construction achieves \(\Theta(N\log N)\) and is optimal only within the D0L **nested-tail** architecture.
11. Sparse marker geometry beats that density by moving separating witnesses far out in the carrier.

## Result 15 — Sparse Marker Ladder

Let

\[
M_n=\{Q_{2^j}:j\ge n\}
\]

and define one binary relation

\[
\boxed{R_1(Q_n,Q_m)\iff Q_m\in M_n.}
\]

The rows satisfy

\[
M_0\supsetneq M_1\supsetneq M_2\supsetneq\cdots
\]

with

\[
M_n\setminus M_{n+1}=\{Q_{2^n}\}.
\]

Hence full carrier order is FO-definable by strict row inclusion:

\[
\boxed{
Q_n<Q_k
\iff
M_k\subsetneq M_n.}
\]

Once order is recovered, the unique marker removed between consecutive rows is also FO-definable, so the unary marker map

\[
n\mapsto 2^n
\]

is internally recovered.

### Visible memory cost

Let

\[
L=\lfloor\log_2N\rfloor.
\]

Only markers

\[
2^0,2^1,\ldots,2^L
\]

appear in the initial window \([0,N]^2\). Marker \(2^j\) belongs to exactly \(j+1\) rows. Therefore

\[
C_1(N)=\sum_{j=0}^L(j+1)
=\frac{(L+1)(L+2)}2,
\]

so

\[
\boxed{C_1(N)=\Theta((\log N)^2).}
\]

Thus initial-window incidence count can be subpolynomial while FO still recovers the entire infinite order.

### No contradiction with the Sparse Memory Threshold

Every row is globally infinite. Hence every source point has infinite Gaifman degree and

\[
H=G_\omega.
\]

The Infinite Nonlocal Core requirement is fully satisfied. The low finite-window count arises because most witnesses lie far beyond the current numerical window.

Therefore:

\[
\boxed{
\text{global nonlocality}
\not\asymp
\text{finite-window tuple density}.}
\]

This is now a fixed architectural lesson of the infinite branch.

## Result 16 — Arithmetic leakage remains absent

The marker relation is FO-definable in

\[
\mathcal E=(\mathbb N,<,e),
\qquad e(n)=2^n,
\]

by

\[
R_1(n,m)\iff\exists j\,(n\le j\wedge e(j)=m).
\]

Thus the sparse-marker structure is an FO reduct of the same exponential order structure used for the dense-tail candidate.

The branch isolates one external model-theoretic dependency: the unary quantifier-elimination/normal-form analysis for \((\mathbb N,<,2^x)\), which implies parity is not FO-definable. The branch reproduces the parity consequence directly from the stated normal form: on a long interval strictly between consecutive powers of two, every one-variable formula stabilizes, while parity alternates.

Hence ordinary addition is not FO-definable, because addition would define parity by

\[
\operatorname{Even}(x)\iff\exists y\,\operatorname{Add}(y,y,x).
\]

Multiplication is also not FO-definable: discrete order gives successor, and Julia Robinson's theorem would then recover addition from multiplication plus successor.

Therefore

\[
\boxed{
R_1\Rightarrow_{\rm FO}<,
\qquad
R_1\not\Rightarrow_{\rm FO}+,
\qquad
R_1\not\Rightarrow_{\rm FO}\times.}
\]

Publication hardening must still replace the current expert-source QE anchor with the strongest available primary theorem citation or reproduce the required unary normal-form proof self-contained.

## Result 17 — Fixed-depth marker cascades

For fixed \(k\ge1\), define

\[
E_1(n)=2^n,
\qquad
E_{k+1}(n)=2^{E_k(n)},
\]

and the marker ladder

\[
R_k(Q_n,Q_m)
\iff
\exists j\ge n\;(m=E_k(j)).
\]

Every fixed \(E_k\) is FO-definable in \((\mathbb N,<,2^x)\), so every \(R_k\) is an FO reduct of the same arithmetic-safe ambient structure. Thus full order is FO-recoverable and ordinary \(+\), \(\times\) remain FO-undefinable.

Let

\[
J_k(N)=\max\{j:E_k(j)\le N\}.
\]

Then

\[
J_k(N)=\log_2^{(k)}N+O(1),
\]

and

\[
C_k(N)=\sum_{j=0}^{J_k(N)}(j+1).
\]

Therefore

\[
\boxed{
C_k(N)=\Theta\left((\log^{(k)}N)^2\right).}
\]

So no lower bound at any fixed finite level of the iterated-log hierarchy can be universal across the finite-depth cascade family.

Source status:

- \(k=1\): PASS under the audited D0L gate;
- fixed \(k>1\): PASS under a declared finite-depth D0L-cascade gate, with independent provenance audit required before publication promotion.

## Consequence: density is no longer the right infinite-memory invariant

The previous density ladder

\[
N^2\to N^{3/2}\to N\log N
\]

was misleading as a candidate universal cost hierarchy. Sparse marker geometry gives instead

\[
\boxed{
N^2
\to
N\log N
\to
(\log N)^2
\to
(\log\log N)^2
\to
\cdots
}
\]

while preserving the same three logical properties:

\[
\boxed{
\text{same carrier},
\qquad
\text{FO full order},
\qquad
\text{no FO }+\text{ or }\times.}
\]

The invariant that has survived every compression is not finite-window tuple count but:

\[
\boxed{
\text{an infinite nonlocal core carrying a globally nested comparison code}.}
\]

A better quantitative invariant must penalize how far out the separating witnesses are moved.

Natural next candidates are:

- first separating-witness scale for the first \(n\) rows;
- witness displacement / escape rate;
- nested-neighborhood chain rank;
- FO comparison depth versus witness scale.

## Recommendation to main director

The Sparse Marker Ladder should be treated as the new leading theorem candidate of the density subdirection. It supersedes \(\Theta(N\log N)\) as the best known finite-window compression and shows that the earlier D0L lower bound was architecture-specific, not global.

The following remain strong fixed branch mathematics:

- G2 infinite FO boundary;
- hostile-audited EF/locality proof;
- Sparse Memory Threshold;
- Order-Only Quadratic Barrier;
- primitive non-order arithmetic-safe order memory;
- source/internal-leakage gate separation;
- sparse-marker order recovery with \(\Theta((\log N)^2)\) visible incidences;
- fixed-depth iterated-log marker cascade family.

The next problem is no longer simply “beat \(N\log N\)”. It is:

> define and prove the right representation-robust memory-cost invariant for infinite FCOA, then determine whether a single fixed source-safe construction can achieve \(\log^*N\)-scale marker visibility or slower without leaking ordinary arithmetic.

No finite G4 theorem status is changed by this memo.