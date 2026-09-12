# HATTER-SOL-08 · Dimensional Factor Architectures

**Working title:** *From a Line to Space: Dimensional Release in Factor-Capacity Networks*  
**Series:** HATTER-SOL · Arithmetic Tea Party  
**Branch:** `research/hatter-sol-dimensional-factor-morphisms`  
**Status:** active research; first theorem layer obtained; publication threshold not yet declared.

## Question

HATTER-SOL-07 optimized the free boundary over abstract simple graphs. HATTER-SOL-08 asks what happens when the same factor-capacity network is restricted to progressively richer architecture classes:

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

and an admissible graph class `C`, define

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

Here `circle` means the outerplanar / one-page class, and `3D` means crossing-free straight-line realizability in three-dimensional space. Since every finite simple graph has such a 3D drawing, `lambda_3D` is exactly the unrestricted `lambda` of HATTER-SOL-07.

## First exact results

### 1D exact law

If `k>=2`, the only connected straight-line non-overlapping architecture on a line is a path. Hence

\[
\boxed{
\lambda_{1D}(\mathbf c)=\sum_i c_i-2(k-1).
}
\]

Under one multiplicative refinement

\[
ab\to(a,b),
\]

with

\[
\delta(a,b)=ab-a-b,
\]

we obtain

\[
\boxed{
\lambda_{1D}(\mathbf c')-\lambda_{1D}(\mathbf c)
=-(\delta+2)
=-(ab-a-b+2)<0.
}
\]

Thus **refinement inversion is impossible in 1D**.

### Complete-capacity staircase

For

\[
\mathbf c^{(k)}=(k-1,\ldots,k-1)
\]

on `k>=4` vertices, degree constraints do not bind before the architecture-class edge bound. Therefore

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

This follows from the classical edge maxima `k-1`, `2k-3`, `3k-6`, and `C(k,2)` for paths, outerplanar graphs, planar graphs, and unrestricted simple graphs, respectively.

The corresponding dimensional release gains are

\[
\lambda_{1D}-\lambda_{\circ}=2(k-2),
\]

\[
\lambda_{\circ}-\lambda_{2D}=2(k-3),
\]

\[
\lambda_{2D}-\lambda_{3D}=(k-3)(k-4).
\]

These formulas are a baseline consequence of classical extremal edge counts, not by themselves a novelty claim.

## Refinement across sparse architecture classes

A first new theorem candidate has been proved in `RESEARCH_KERNEL.md`:

for `C` equal to the outerplanar or planar class, one still has the one-step universal bound

\[
\boxed{
\lambda_C(\ldots,a,b,\ldots)
-
\lambda_C(\ldots,ab,\ldots)
\le ab-a-b.
}
\]

The proof uses local consecutive vertex splitting in an embedding plus a connectivity-recovery lemma for maximum-edge feasible planar/outerplanar graphs.

What is **not** yet proved is that this upper bound is sharp for every pair `a,b` in the outerplanar or planar classes.

## First dimensional phase transition

The HATTER-SOL-07 inversion construction for

\[
(2q,2^m)\to(q,2^{m+1}),
\qquad q\ge3\text{ odd},\;m\ge2q,
\]

is already outerplanar: the coarse saturated construction is a cactus of cycles sharing one hub, and the refined boundary-one construction is a bouquet of triangles plus one tail.

Hence

\[
\lambda_{\circ}(2q,2^m)=0,
\qquad
\lambda_{\circ}(q,2^{m+1})=1.
\]

So the sign of refinement response changes as soon as one leaves strict 1D.

For the smallest split `6 -> 2*3`, the general outerplanar/planar upper bound equals `1`, while the explicit outerplanar construction attains `1`. Therefore

\[
\boxed{
\Delta^{\max}_{\circ}(2,3)
=
\Delta^{\max}_{2D}(2,3)
=
\Delta^{\max}_{3D}(2,3)
=1,
}
\]

whereas in 1D the same split always gives

\[
\boxed{
\lambda_{1D}(\mathbf c')-\lambda_{1D}(\mathbf c)=-3.
}
\]

This is the first exact dimensional sign-reversal theorem in the programme.

## Prior-art boundary

The following are classical / known and must not be claimed as new:

- outerplanar graphs have at most `2n-3` edges;
- planar graphs have at most `3n-6` edges for `n>=3`;
- every finite graph has a crossing-free straight-line drawing in 3D (for example via the moment curve);
- vertex splitting is a classical graph operation;
- planar and outerplanar degree-realization problems have substantial prior literature, and full degree-sequence characterizations remain open in important cases.

The candidate contribution is narrower: **free-boundary sensitivity under the arithmetic split `ab -> (a,b)` compared across nested realization classes**.

## Next attack

Define

\[
\Delta_C(a,b)
:=
\sup_{\text{ambient capacity vectors}}
\left[
\lambda_C(\ldots,a,b,\ldots)
-
\lambda_C(\ldots,ab,\ldots)
\right].
\]

Known now:

\[
\Delta_{1D}(a,b)=-(ab-a-b+2),
\]

\[
\Delta_{3D}(a,b)=ab-a-b,
\]

and

\[
\Delta_{\circ}(a,b),\Delta_{2D}(a,b)\le ab-a-b.
\]

Also

\[
\Delta_{\circ}(2,3)=\Delta_{2D}(2,3)=1.
\]

The immediate open problem is to determine `Delta_circle(a,b)` and `Delta_2D(a,b)` exactly, or find the first pair for which either is strictly below `ab-a-b`.

See `RESEARCH_KERNEL.md` and `STATUS.md`.
