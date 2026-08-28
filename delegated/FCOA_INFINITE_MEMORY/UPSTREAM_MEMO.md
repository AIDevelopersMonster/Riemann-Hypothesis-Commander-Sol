# Upstream Memo — Infinite Carrier & FO Memory Boundary

**To:** main Commander Sol scientific director  
**From:** FCOA — SOL-INFINITY scientific supervisor  
**Status:** hostile-audited theorem checkpoint R1 + sparse-memory threshold + order-only quadratic barrier + primitive subquadratic theorem + provenance audit R1  
**Audit:** `HOSTILE_AUDIT_R1.md`  
**Sparse threshold:** `SPARSE_MEMORY_THRESHOLD.md`  
**Order-only density theorem:** `ORDER_ONLY_QUADRATIC_BARRIER.md`  
**Primitive subquadratic theorem:** `SUBQUADRATIC_PRIMITIVE_SKELETON.md`  
**Provenance audit:** `PROVENANCE_AUDIT_R1.md`  
**Best certified primitive candidate:** `EXPONENTIAL_NESTED_TAIL.md`

## Executive result

The infinite branch now separates six independent coordinates:

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
\text{source-class complexity vs memory density}.}
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

## Fixed branch results before provenance audit

1. G2 infinity remembers successor locally but not full order in FO.
2. Full M0+G2 decoration does not secretly add order.
3. There is no uniform FO full-order formula across all finite directed paths.
4. Finite unary/local memory remains insufficient.
5. Finite-apex locally finite active memory cannot FO-define an infinite linear order.
6. For binary finite-output FCOA, FO full order requires an infinite active nonlocal core.
7. In the order-only binary class, every basic relation has density either \(O(N)\) or \(\Theta(N^2)\); hence FO order forces quadratic density.
8. Primitive non-order nested-tail memory can beat the quadratic barrier while preserving nondefinability of ordinary \(+\) and \(\times\).

## Result 11 — Primitive Subquadratic Skeleton

For any strictly increasing cofinal jump map \(f\), define

\[
R_f(Q_n,Q_m)\iff m\ge f(n).
\]

Then row inclusion gives the full carrier order:

\[
Q_n<Q_k
\iff
N_f(k)\subsetneq N_f(n).
\]

The jump map itself is FO-recoverable as the least point in each row.

The earlier exact witness used

\[
f(n)=(n+1)^2
\]

and obtained

\[
C(N)=\frac23N^{3/2}+O(N).
\]

This already proved logical existence of subquadratic FO-order memory without FO ordinary addition or multiplication.

## Result 12 — Provenance audit repairs the source-safety criterion

The hostile provenance audit rejects two naive policies:

- “finite program = safe” is too weak, because finite programs can compute arbitrary arithmetic;
- “not arithmetically definable” is too strong, because effective combinatorial skeletons are arithmetically representable in sufficiently rich arithmetic.

The branch therefore adopts a conservative certified source class:

### Index-blind D0L source gate

A threshold sequence is source-certified when

\[
g(n)=|\sigma^n(w)|
\]

for a fixed finite alphabet, fixed seed word, and fixed deterministic morphism \(\sigma\) whose letter-replacement rules do not inspect the stage number, carrier indices, counters, parity, divisibility, BIT, addition, multiplication, or other numerical predicates.

This is materially stronger than a generic finite-program gate because D0L systems are a highly restricted parallel-rewriting formalism with tightly constrained growth functions.

Under this declared gate, the previous quadratic substitution passes provenance audit.

## Result 13 — Exponential Nested Tail: best certified primitive candidate

A much simpler D0L source improves the memory density:

\[
\boxed{A\mapsto AA.}
\]

With seed \(A\),

\[
|\sigma^n(A)|=2^n.
\]

Define

\[
\boxed{
R_{\exp}(Q_n,Q_m)
\iff
m\ge2^n.
}
\]

The closed form \(2^n\) is used only to describe the proved growth law; the primitive generator is the index-blind duplication morphism.

### FO recovery of order

Rows are strictly nested, so

\[
Q_n<Q_k
\iff
N(k)\subsetneq N(n).
\]

Hence full carrier order is FO-definable.

### Exact memory density

Let

\[
L=\lfloor\log_2N\rfloor.
\]

Then

\[
C(N)=\sum_{n=0}^{L}(N-2^n+1)
\]

and therefore

\[
\boxed{
C(N)=N\log_2N+O(N)=\Theta(N\log N).
}
\]

This is the first source-certified nearly linear candidate in the branch.

### Arithmetic leakage status

The structure is FO-interdefinable with

\[
(\mathbb N,<,2^x).
\]

Published model-theoretic work gives decidability/quantifier-elimination analysis for this structure and, in particular, rules out definability of parity. Therefore ordinary addition cannot be FO-definable, since addition would define parity by

\[
\operatorname{Even}(x)\iff\exists y(y+y=x).
\]

Multiplication cannot be FO-definable either: discrete order gives successor, and Julia Robinson’s definability theorem would then recover addition from multiplication plus successor.

Thus, subject to publication-hardening of the exact primary QE citation,

\[
\boxed{
R_{\exp}\Rightarrow_{\rm FO}<,
\qquad
R_{\exp}\not\Rightarrow_{\rm FO}+,
\qquad
R_{\exp}\not\Rightarrow_{\rm FO}\times.
}
\]

Current status:

\[
\boxed{
\text{SOURCE GATE: PASS},
\qquad
\text{INTERNAL LEAKAGE: PASS with one external citation-hardening obligation}.}
\]

## Result 14 — D0L nested-tail optimality

Let

\[
g(n)=|\sigma^n(w)|
\]

be an unbounded strictly increasing D0L growth function and use the nested-tail relation

\[
R_g(n,m)\iff m\ge g(n).
\]

If

\[
B=\max_a|\sigma(a)|,
\]

then

\[
g(n)\le |w|B^n.
\]

Therefore at least \(c\log N\) initial rows have threshold at most \(\sqrt N\), and each contributes at least \(N-\sqrt N\) incidences inside the first \(N\) columns. Hence

\[
\boxed{
C(N)=\Omega(N\log N).
}
\]

The duplication morphism attains \(\Theta(N\log N)\). Therefore:

\[
\boxed{
\Theta(N\log N)
\text{ is asymptotically optimal inside the D0L-provenance nested-tail class}.}
\]

This density theorem is internal to the branch and does not depend on the external arithmetic-leakage citation.

## Architectural picture after provenance audit

The memory ladder is now:

\[
\boxed{
\begin{array}{c}
\text{G2 local successor: }\Theta(N),\ \text{no FO order}\\
\Downarrow\\
\text{finite-apex locally finite: no FO order}\\
\Downarrow\\
\text{order-only global binary memory: }\Theta(N^2)\text{ required}\\
\Downarrow\\
\text{primitive non-order D0L nested tails: }\Theta(N\log N)\\
\text{FO order, no FO ordinary }+\text{ or }\times.
\end{array}}
\]

Thus the original open question has a positive answer with a much stronger density than the first quadratic-growth witness.

## Recommendation to main director

The following may now be treated as fixed branch mathematics:

- G2 infinite FO boundary;
- hostile-audited EF/locality proof;
- Sparse Memory Threshold;
- Order-Only Quadratic Barrier;
- logical existence of arithmetic-safe subquadratic primitive order memory;
- repaired D0L provenance gate;
- \(\Theta(N\log N)\) D0L nested-tail upper/lower bound.

One obligation remains before publication-hardening the exponential candidate as a theorem package:

> pin down the exact primary-source quantifier-elimination/decidability theorem for \((\mathbb N,<,2^x)\) and reproduce the parity-nondefinability consequence at publication-proof level.

After that, the natural next frontier is no longer “does a sparse safe skeleton exist?” It is:

> can a comparably principled non-universal primitive source class beat the D0L floor \(N\log N\) while still passing the internal no-addition/no-multiplication leakage gate?

Do not merge any infinite result into finite G4. No finite G4 theorem status is changed by this memo.
