# HATTER-SOL-08 · Status

**Branch:** `research/hatter-sol-dimensional-factor-morphisms`  
**Path:** `papers/HATTER-SOL/08-DIMENSIONAL-FACTOR-ARCHITECTURES/`  
**Status date:** 2026-09-12  
**Status:** active research; first theorem layer obtained; publication threshold not yet reached.

## Proven in this branch

1. Exact 1D law:

\[
\lambda_{1D}(\mathbf c)=\sum_i c_i-2(k-1),
\]

and for `ab->(a,b)`

\[
\lambda_{1D}(\mathbf c')-\lambda_{1D}(\mathbf c)
=-(ab-a-b+2)<0.
\]

Hence refinement inversion is impossible in strict 1D.

2. Complete-capacity dimensional staircase for `c^(k)=(k-1,...,k-1)`:

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

3. Connectivity does not reduce the maximum feasible edge count for the planar and outerplanar capacity-constrained classes when all capacities are at least two.

4. The HATTER-SOL-07 one-step upper bound survives in the outerplanar and planar classes:

\[
\lambda_C(\ldots,a,b,\ldots)-\lambda_C(\ldots,ab,\ldots)
\le ab-a-b,
\quad C\in\{outer,planar\}.
\]

5. Explicit dimension-dependent sign reversal:

for odd `q>=3`, `m>=2q`, and

\[
(2q,2^m)\to(q,2^{m+1}),
\]

we have an outerplanar realization with

\[
\Delta_{outer}=\Delta_{planar}=\Delta_{3D}=+1,
\]

while the same refinement in strict 1D gives

\[
\Delta_{1D}=-q.
\]

6. Exact special case:

\[
\Delta_{outer}^{max}(2,3)
=\Delta_{planar}^{max}(2,3)
=\Delta_{3D}^{max}(2,3)=1,
\]

whereas every 1D ambient vector gives change `-3`.

## Open proof obligations

- Determine `Delta_outer^max(a,b)` exactly.
- Determine `Delta_planar^max(a,b)` exactly.
- For odd `q>3`, close the current gap

\[
1\le\Delta_{outer}^{max}(2,q),\Delta_{planar}^{max}(2,q)\le q-2.
\]

- Find the first pair `(a,b)` for which a restricted-class sharpness value is strictly smaller than the unrestricted value `ab-a-b`, or prove no such pair exists.
- Separate topological classes from intrinsic simplicial dimension; do not yet mix the flag-complex programme into the main theorem sequence.

## Prior-art status

Classical edge bounds, Fary straight-line planarity, 3D moment-curve drawings, vertex splitting/detachment, and degree-sequence theory are prior art and not novelty claims.

The novelty candidate is the arithmetic-split free-boundary response across nested architecture classes.

## Publication threshold

**Not yet reached.**

The branch has a real theorem layer, but the central 2D/outerplanar extremal function remains open. The next publication threshold would be crossed by either:

- an exact formula for `Delta_outer^max(a,b)` or `Delta_planar^max(a,b)` on a substantial family; or
- a strict dimensional-separation theorem showing an infinite family where restricted and unrestricted sharpness amplitudes differ.
