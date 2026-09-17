# TORUS OBSERVABILITY TRANSITION · RESEARCH SEED

**Status:** exact seed result; strong candidate for a separate article rather than absorption into HATTER-SOL-11.

**Probe:** `N=61^6` restricted to the four split class-number-one worlds

`Delta=-4,-3,-19,-163`

with typed states

`(6,5),(5,4),(7,1),(4,1)`.

**Question:** does changing host geometry from the sphere/plane to the torus change the number of weighted observations required to identify the arithmetic world?

The answer is yes.

---

## 1. Explicit 12-vertex toroidal host

Let

`V = Z_3 x Z_4`

and join each vertex `x` to

`x +/- e_1`, `x +/- e_2`, `x +/- (e_1+e_2)`.

The six neighbors are distinct, so this gives a simple 6-regular graph `T_12` on 12 vertices with 36 edges. It is the quotient of the triangular lattice by the translation sublattice `3Z x 4Z`, hence has the standard triangular embedding on the torus.

The three undirected generator directions are three edge-disjoint 2-factors, each with 12 edges.

Inside the `e_2` 2-factor choose

`M={(i,0)(i,1),(i,2)(i,3): i in Z_3}`.

Then `M` is a perfect matching with 6 edges.

These explicit decompositions will certify every weighted optimum below.

---

## 2. Weighted geometry gain

Let weights be `(a,o)>0`, with `a` applied to the `P` channel and `o` to the `Q` channel. Let

`G_R^T(a,o)`

be twice the increase in maximum weighted used incidence when the canonical strict path is replaced by the toroidal host `T_12`.

Equivalently it is the reduction in weighted free boundary from `1D` to the torus.

Put `r=o/a` and normalize by `a`:

`F_R^T(r)=G_R^T(a,ra)/a`.

---

## 3. Gaussian state `(6,5)`

On the path, both channel capacities exceed the maximum path degree, so all 11 edges may use the more valuable channel:

`U_1D=11 max(a,o)`.

On `T_12`:

- if `a>=o`, all 36 edges may be `P`, so `U_T=36a`;
- if `o>=a`, use `T_12-M` as `Q` (degree 5, 30 edges) and `M` as `P` (6 edges), so `U_T=30o+6a`.

Both are optimal by the degree caps.

Hence

`G_-4^T(a,o) = 50a` for `a>=o`,

and

`G_-4^T(a,o) = 12a+38o` for `o>=a`.

Thus

`F_-4^T(r)=50` for `r<=1`,

`F_-4^T(r)=12+38r` for `r>=1`.

---

## 4. Eisenstein state `(5,4)`

Again `U_1D=11 max(a,o)`.

If `a>=o`, every vertex of a 6-regular used support needs at least one `Q` incidence because `P<=5`. Thus at least 6 `Q` edges are necessary. The perfect matching `M` achieves this bound, giving

`U_T=30a+6o`.

If `o>=a`, the `Q` degree cap 4 gives at most 24 `Q` edges. Two complete generator 2-factors give an explicit 4-regular 24-edge `Q` subgraph; the remaining 12 edges are `P`. Hence

`U_T=12a+24o`.

Therefore

`G_-3^T(a,o)=38a+12o` for `a>=o`,

`G_-3^T(a,o)=24a+26o` for `o>=a`,

or

`F_-3^T(r)=38+12r` for `r<=1`,

`F_-3^T(r)=24+26r` for `r>=1`.

---

## 5. State `(7,1)`

On the path:

- if `a>=o`, use all 11 edges as `P`, so `U_1D=11a`;
- if `o>=a`, a `Q` matching has at most 6 edges and is attainable, giving `U_1D=5a+6o`.

On the torus:

- if `a>=o`, all 36 edges may be `P`;
- if `o>=a`, use `M` as the 6 `Q` edges and all remaining 30 edges as `P`.

Thus in both regimes

`G_-19^T(a,o)=50a`,

so

`F_-19^T(r)=50` for all `r>0`.

---

## 6. State `(4,1)`

Total node capacity is 5, so at most 30 edges can be used on 12 vertices.

Full saturation is explicitly attainable:

- use the perfect matching `M` as `Q` (degree 1);
- use two generator 2-factors disjoint from `M` as `P` (degree 4, 24 edges).

Thus every vertex has exact typed degree `(4,1)`.

The toroidal weighted optimum is therefore

`U_T=24a+6o`.

Subtracting the path optimum gives

`G_-163^T(a,o)=26a+12o` for `a>=o`,

`G_-163^T(a,o)=38a` for `o>=a`.

Hence

`F_-163^T(r)=26+12r` for `r<=1`,

`F_-163^T(r)=38` for `r>=1`.

---

## 7. Exact toroidal tomographic dimension

The four normalized signatures are therefore

`F_-4^T(r)=50` (`r<=1`), `12+38r` (`r>=1`);

`F_-3^T(r)=38+12r` (`r<=1`), `24+26r` (`r>=1`);

`F_-19^T(r)=50` for all `r`;

`F_-163^T(r)=26+12r` (`r<=1`), `38` (`r>=1`).

### Theorem TOS11.1 — toroidal one-shot identifiability

For every `r>1`, the four values are pairwise distinct. Therefore

`tdim_T2 = 1`.

### Proof

For `r>1`, the values are

`12+38r`, `24+26r`, `50`, `38`.

The first two are equal only at `r=1`; each equals 50 only at `r=1`; neither can equal 38 for `r>1`; and `50 != 38`. Thus any single observation with `r>1` identifies all four split worlds. QED.

By the previously proved planar result,

`tdim_Pl = 2`.

Hence

\[
\boxed{tdim_{Pl}(61^6)=2,\qquad tdim_{T^2}(61^6)=1.}
\]

This is a genuine geometry-induced observability transition.

---

## 8. The planar spectral blind direction disappears

In the planar laboratory, `r=1` gave

`F_R^Pl(1)=38`

for all four split worlds. Thus `r=1` was a fully world-blind direction.

On the torus,

`F_-4^T(1)=50`,

`F_-3^T(1)=50`,

`F_-19^T(1)=50`,

`F_-163^T(1)=38`.

So `r=1` is no longer fully blind.

For `r<1`, `-4` and `-19` collide at 50, but the four worlds are not all equal.

For `r>1`, all four values are distinct.

Therefore the toroidal fully blind set is empty:

\[
\boxed{B_*^{T^2}=\varnothing,}
\]

whereas the planar split-world laboratory had

\[
\boxed{B_*^{Pl}=\{r=1\}.}
\]

Thus topology/geometry of the admissible host can remove an arithmetic-world blind direction.

---

## 9. Why this should probably become a separate article

The result is not merely an extension of the planar balancing proof. It introduces a different question:

> how does host topology control the observability of arithmetic worlds?

For the same integer, same four worlds, same typed local states, and same weighted measurement family, changing only the host geometry changes

- the response signatures;
- the pair-collision complex;
- the fully blind set;
- and the exact tomographic dimension.

The sharp transition

`plane: tdim=2` -> `torus: tdim=1`

suggests a new programme in which genus or other host-topology parameters act on arithmetic-world identifiability.

**Recommendation:** retain this file as a seed inside HATTER-SOL-11, but if the phenomenon survives one additional prime or one general theorem, open a separate article/branch provisionally titled

`HATTER-SOL-12 · TOPOLOGICAL OBSERVABILITY OF ARITHMETIC WORLDS`.
