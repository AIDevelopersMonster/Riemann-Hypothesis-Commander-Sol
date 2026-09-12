# HATTER-SOL-08 · Status

**Branch:** `research/hatter-sol-dimensional-factor-morphisms`  
**Path:** `papers/HATTER-SOL/08-DIMENSIONAL-FACTOR-ARCHITECTURES/`  
**Status date:** 2026-09-12  
**Status:** **PUBLICATION THRESHOLD REACHED FOR A REPAIRED PLANAR/3D THEOREM LAYER; outerplanar suppression claim retracted after hostile audit.**

## Audited theorem layer

### 1. Exact 1D law

For a capacity vector `c=(c_1,...,c_k)`, `c_i>=2`, strict 1D forces a path and

\[
\lambda_{1D}(\mathbf c)=\sum_i c_i-2(k-1).
\]

For one multiplicative refinement `ab->(a,b)`,

\[
\boxed{
\lambda_{1D}(\mathbf c')-\lambda_{1D}(\mathbf c)
=-(ab-a-b+2)<0.
}
\]

Hence refinement inversion is impossible in strict 1D.

### 2. Complete-capacity dimensional staircase

For `c^(k)=(k-1,...,k-1)`:

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

This calibration family follows from classical extremal edge bounds and is not itself a novelty claim.

### 3. General one-step upper bound

The HATTER-SOL-07 one-step bound survives in the planar class, and the current branch also retains the previously established outerplanar class-preserving split bound:

\[
\lambda_C(\ldots,a,b,\ldots)-\lambda_C(\ldots,ab,\ldots)
\le ab-a-b,
\]

for the audited planar case and, subject to the separate connectivity/splitting formulation in `RESEARCH_KERNEL.md`, the outerplanar baseline case.

No stronger outerplanar bound is currently claimed.

### 4. Exact dimensional sign reversal

For odd `q>=3`, `m>=2q`, and

\[
(2q,2^m)\to(q,2^{m+1}),
\]

the HATTER-SOL-07 cactus/bouquet constructions are outerplanar and give

\[
\Delta_{outer}=\Delta_{planar}=\Delta_{3D}=+1,
\]

while strict 1D gives

\[
\Delta_{1D}=-q.
\]

For `q=3`:

\[
\boxed{
\Delta_{outer}^{max}(2,3)
=\Delta_{planar}^{max}(2,3)
=\Delta_{3D}^{max}(2,3)=1,
}
\]

while

\[
\boxed{\Delta_{1D}^{max}(2,3)=-3.}
\]

### 5. Audited planar suppression theorem for `2q -> (2,q)`

Let

\[
\delta=q-2.
\]

Using a four-incidence local reduction in a plane embedding, we obtain

\[
\boxed{
\Delta_{planar}^{max}(2,q)
\le
U_{Pl}(q)
:=
2\left\lceil\frac{3(q-2)}4\right\rceil-(q-2).
}
\]

HATTER-SOL-07 gives the unrestricted / 3D exact value

\[
\boxed{
\Delta_{3D}^{max}(2,q)=q-2.
}
\]

Hence for every `q>=6`,

\[
\boxed{
\Delta_{planar}^{max}(2,q)
<
\Delta_{3D}^{max}(2,q).
}
\]

Asymptotically,

\[
U_{Pl}(q)=\frac{q-2}{2}+O(1).
\]

Thus planar architecture suppresses the worst possible refinement-inversion amplitude by an asymptotic factor of at least two relative to unrestricted/3D architecture.

For odd `q>=7`, the explicit outerplanar family remains planar and supplies

\[
\boxed{
1\le\Delta_{planar}^{max}(2,q)
\le U_{Pl}(q)<q-2.
}
\]

This is the main publication-level result of HATTER-SOL-08 after audit.

## Retracted claim found by hostile audit

The first draft attempted to prove an outerplanar suppression bound by taking three consecutive neighbors of a vertex, deleting the three incident spokes, and inserting a missing edge among those neighbors.

This local operation does **not** always preserve outerplanarity.

A seven-vertex counterexample is recorded explicitly in `DIMENSIONAL_SEPARATION.md`. The added edge can create a subdivision of `K_{2,3}` even though it was absent before the operation.

Therefore the following earlier claims are withdrawn:

- the formula `U_O(q)=2 ceil(2(q-2)/3)-(q-2)` as a universal outerplanar bound;
- strict outerplanar/3D separation derived from that formula;
- the claimed exact value `Delta_outer^max(2,5)=1`.

These must not appear in a publication manuscript unless independently re-proved by a different argument.

## Computational hostile-search support

A finite regression check over all connected planar graphs in the NetworkX graph atlas up to seven vertices found no counterexample to the four-incidence planar local operation. This is **not** part of the proof; it is only a hostile-search sanity check.

The analogous hostile search is what exposed the outerplanar flaw.

## Prior-art boundary

Classical / not claimed as new:

- outerplanar edge bound `2n-3`;
- planar edge bound `3n-6`;
- Fary straight-line planarity;
- crossing-free straight-line drawings of finite graphs in `R^3`;
- vertex splitting / detachment / splitting-off;
- `K_4` and `K_{2,3}` exclusion for outerplanar graphs;
- `K_5` exclusion for planar graphs;
- planar and outerplanar degree-realization theory.

Candidate contribution after audit:

> quantitative free-boundary response to the arithmetic split `2q -> (2,q)` across dimensional architecture classes, including exact 1D monotonicity, explicit sign reversal, and an infinite-family strict planar-versus-unrestricted separation theorem.

## Remaining proof obligations before article assembly

1. Re-audit the planar connectivity-recovery lemma in publication-level detail.
2. Rewrite the planar four-block proof without relying on a particular drawing convention beyond a fixed plane embedding and contiguous incidence sector.
3. Verify the ceiling threshold `q>=6` and all small cases separately.
4. Run a targeted literature audit for planar splitting-off / detachment operations that might already imply the four-block inequality.
5. Treat the outerplanar exact extremal function as open; do not import the retracted bound.

## Publication threshold

**Reached for the repaired planar/3D theorem layer.**

The result is now narrower than the first draft but stronger in reliability: the branch contains an exact 1D law, an explicit sign reversal, and a strict infinite-family planar-versus-3D separation theorem. Manuscript assembly may begin after the remaining planar proof and literature audit items are closed.
