# HATTER-SOL-08 · Dimensional Factor Architectures

**Working title:** *From a Line to Space: Dimensional Release in Factor-Capacity Networks*  
**Series:** HATTER-SOL · Arithmetic Tea Party  
**Branch:** `research/hatter-sol-dimensional-factor-morphisms`  
**Status:** publication threshold reached for repaired planar/3D theorem layer; outerplanar strengthening retracted after hostile audit.

## Question

HATTER-SOL-07 optimized the free boundary over abstract simple graphs. HATTER-SOL-08 asks what changes when the same factor-capacity network is restricted to progressively richer architecture classes:

\[
\text{1D path}
\subset
\text{outerplanar/circular}
\subset
\text{planar 2D}
\subset
\text{unrestricted / 3D}.
\]

For a capacity vector

\[
\mathbf c=(c_1,\ldots,c_k),\qquad c_i\ge2,
\]

and admissible graph class `C`, define

\[
M_C(\mathbf c)
=
\max\{|E(G)|:\;G\in C,\;G\text{ connected},\;\deg(v_i)\le c_i\},
\]

and

\[
\lambda_C(\mathbf c)
=
\sum_i c_i-2M_C(\mathbf c).
\]

The immediate hierarchy is

\[
\lambda_{1D}\ge\lambda_{\circ}\ge\lambda_{2D}\ge\lambda_{3D}.
\]

Here `circle` means the outerplanar / one-page class, and `3D` means the unrestricted simple-graph class, which is realizable crossing-free by straight segments in three dimensions.

## Exact 1D law

For `k>=2`, strict 1D forces a path. Hence

\[
\boxed{
\lambda_{1D}(\mathbf c)=\sum_i c_i-2(k-1).
}
\]

Under

\[
ab\to(a,b),
\]

we obtain

\[
\boxed{
\lambda_{1D}(\mathbf c')-\lambda_{1D}(\mathbf c)
=-(ab-a-b+2)<0.
}
\]

Thus refinement inversion is impossible in 1D.

## Complete-capacity dimensional staircase

For

\[
\mathbf c^{(k)}=(k-1,\ldots,k-1)
\]

on `k>=4` vertices,

\[
\boxed{\lambda_{1D}=(k-1)(k-2)},
\]

\[
\boxed{\lambda_{\circ}=(k-2)(k-3)},
\]

\[
\boxed{\lambda_{2D}=(k-3)(k-4)},
\]

\[
\boxed{\lambda_{3D}=0}.
\]

These formulas are calibration consequences of classical extremal edge counts, not novelty claims.

## Exact sign reversal

For odd `q>=3`, `m>=2q`, consider

\[
(2q,2^m)\to(q,2^{m+1}).
\]

The HATTER-SOL-07 constructions are outerplanar and yield

\[
\Delta_{outer}=\Delta_{planar}=\Delta_{3D}=+1,
\]

while strict 1D gives

\[
\Delta_{1D}=-q.
\]

So the same arithmetic refinement changes sign solely because the admissible architecture class changes.

For `q=3`:

\[
\boxed{
\Delta_{outer}^{max}(2,3)
=\Delta_{planar}^{max}(2,3)
=\Delta_{3D}^{max}(2,3)=1,
}
\]

while strict 1D gives `-3`.

## Main audited theorem: planar suppression for `2q -> (2,q)`

Let

\[
\delta=q-2.
\]

The unrestricted / 3D theorem of HATTER-SOL-07 gives

\[
\boxed{
\Delta_{3D}^{max}(2,q)=q-2.
}
\]

In the planar class, a four-incidence local reduction gives

\[
\boxed{
\Delta_{planar}^{max}(2,q)
\le
U_{Pl}(q)
:=
2\left\lceil\frac{3(q-2)}4\right\rceil-(q-2).
}
\]

For every `q>=6`,

\[
\boxed{
\Delta_{planar}^{max}(2,q)
<
\Delta_{3D}^{max}(2,q)=q-2.
}
\]

Asymptotically,

\[
U_{Pl}(q)=\frac{q-2}{2}+O(1).
\]

Thus planar geometry suppresses the worst possible refinement inversion by an asymptotic factor of at least two relative to unrestricted/3D architecture.

For odd `q>=7`, the explicit inversion family gives the positive lower bound

\[
\boxed{
1\le\Delta_{planar}^{max}(2,q)
\le U_{Pl}(q)<q-2.
}
\]

This strict infinite-family planar-versus-3D separation is the central publication candidate of HATTER-SOL-08.

## Hostile-audit correction: outerplanar strengthening withdrawn

An earlier draft attempted to derive an outerplanar suppression bound from `K_4`-freeness by deleting three spokes at a vertex and inserting a missing edge among the three neighboring endpoints.

That local operation is **not** always outerplanar-preserving.

A seven-vertex counterexample is recorded in `DIMENSIONAL_SEPARATION.md`; the attempted inserted edge produces a `K_{2,3}` subdivision. Therefore the earlier proposed outerplanar bound and the claimed exact value for `10 -> 2*5` have been withdrawn.

Current safe outerplanar bounds for odd `q` are only

\[
\boxed{
1\le\Delta_{outer}^{max}(2,q)\le q-2,
}
\]

with equality known at `q=3` and the general exact function still open.

This correction is intentional: HATTER-SOL publication policy prefers a narrower theorem that survives hostile audit over a stronger but unproved claim.

## Claim discipline

Classical / not claimed as new:

- outerplanar edge bound `2n-3`;
- planar edge bound `3n-6`;
- Fary straight-line planarity;
- crossing-free straight-line realizability in `R^3`;
- vertex splitting / detachment / splitting-off;
- forbidden-minor facts for planar and outerplanar graphs;
- planar and outerplanar degree-realization theory.

Candidate contribution after audit:

> quantitative free-boundary sensitivity under the arithmetic split `2q -> (2,q)` across nested dimensional graph classes, including exact 1D monotonicity, architecture-dependent sign reversal, and an infinite-family strict planar-versus-unrestricted separation theorem.

## Next actions

1. Finish publication-level audit of the planar connectivity-recovery lemma.
2. Harden the four-incidence plane-local proof and small-`q` edge cases.
3. Run a targeted literature audit for an equivalent planar splitting-off sensitivity theorem.
4. Assemble the RU/EN manuscript around the audited planar/3D theorem layer.
5. Keep the outerplanar extremal function as an explicit open problem.

See `RESEARCH_KERNEL.md`, `DIMENSIONAL_SEPARATION.md`, and `STATUS.md`.
