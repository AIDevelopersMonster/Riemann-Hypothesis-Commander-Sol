# HATTER-SOL-12 · PRIME 61 OBSERVER LADDER

**Status:** exact finite laboratory assembled from closed HATTER-SOL-11 theorem layers.  
**Probe:** `N=61^6`.  
**World laboratory:** the nine imaginary-quadratic class-number-one UFD worlds, with special attention to the four split worlds `Delta=-4,-3,-19,-163`.

## 1. Same integer, different world states

For `61^6`, the split worlds have twelve irreducible factor nodes and local folded states

\[
(6,5),\quad(5,4),\quad(7,1),\quad(4,1),
\]

while the five inert worlds have six nodes and rational-axis state `(61,0)`.

Thus the world itself already changes the structural state of the same rational integer.

## 2. Observer L0 — numerical observer

The coarsest observer sees only the rational integer

\[
O_{num}(W)=61^6.
\]

Hence all nine worlds collide:

\[
\boxed{|O_{num}(\mathcal W_9)|=1.}
\]

This is the baseline: numerical equality does not imply equality of world structure.

## 3. Observer L1 — scalar geometry-gain observer

Let

\[
g_W=\Lambda_{1D}(W)-\Lambda_{Pl}(W).
\]

The exact HATTER-SOL-11 splitting-character law gives

\[
\boxed{g_W=38\text{ on split worlds},\qquad g_W=14\text{ on inert worlds}.}
\]

Therefore

\[
\boxed{|g(\mathcal W_9)|=2.}
\]

This observer distinguishes split from inert but collapses all four distinct split interfaces.

Thus

\[
1\longrightarrow2
\]

is a strict observer refinement on the same integer.

## 4. Observer L2 — one weighted planar sample on the split sector

Restrict now to

\[
\mathcal W_{split}=\{-4,-3,-19,-163\}.
\]

For the normalized weighted planar geometry gain `G_W(r)`:

- if `0<r<1`, the worlds `-4,-3,-19` collide at `38`, while `-163` is strictly below;
- if `r=1`, all four collide at `38`;
- if `r>1`, `-19` and `-163` collide at `38`, while `-4` and `-3` are distinct and larger.

Hence a one-sample observer can have different resolving power depending on direction.

For any fixed `r>1`,

\[
\boxed{|G_r(\mathcal W_{split})|=3.}
\]

because the values are

\[
38r,\qquad12+26r,\qquad38,\qquad38.
\]

Thus on the split sector there is a strict ladder

\[
\boxed{1\xrightarrow{\text{symmetric }r=1}3}
\]

when the observation direction moves off the blind direction into `r>1`.

## 5. Observer L3 — two planar samples

Choose

\[
0<r_-<1<r_+.
\]

The exact tomographic theorem gives an injective map

\[
W\longmapsto\bigl(G_W(r_-),G_W(r_+)\bigr)
\]

on the four split worlds. Therefore

\[
\boxed{|O_{2sample}(\mathcal W_{split})|=4.}
\]

No single planar sample separates all four, so the planar tomographic dimension is exactly

\[
\boxed{\operatorname{tdim}_{Pl}=2.}
\]

Hence the planar observer ladder on the split sector is exactly

\[
\boxed{1\to2\text{ or }3\to4,}
\]

depending on the first chosen direction, with complete reconstruction requiring two scalar samples.

## 6. Rich typed/polynomial observer

Let

\[
\Gamma_W=Z^{\Xi}_{Pl}(W)-Z^{\Xi}_{1D}(W)
\]

be the signed typed geometry signal. HATTER-SOL-11 proves that the four split worlds have pairwise different rich responses. In particular their `Y`-degree/support behavior differs:

- Gaussian reaches `Y`-degree `60`;
- Eisenstein reaches `48`;
- `Delta=-19` reaches `12`;
- `Delta=-163` contains the constant monomial `1`.

Thus one polynomial-valued observation distinguishes all four split worlds:

\[
\boxed{|\Gamma(\mathcal W_{split})|=4.}
\]

The scalar projection can therefore be strictly weaker than the polynomial observer even when both are computed from the same underlying network response.

## 7. Carrier change: plane to torus

Keep the same integer `61^6`, the same four split worlds and the same one-parameter weighted measurement family, but change the carrier to the explicit 12-vertex triangular torus `T_12`.

The exact torus seed gives, for every `r>1`, four pairwise distinct values:

\[
12+38r,
\qquad24+26r,
\qquad50,
\qquad38.
\]

Therefore

\[
\boxed{\operatorname{tdim}_{T^2}=1,}
\]

whereas

\[
\boxed{\operatorname{tdim}_{Pl}=2.}
\]

Hence changing only the carrier changes the number of scalar observations required to identify the arithmetic world:

\[
\boxed{2\longrightarrow1.}
\]

## 8. Blind-set transition

In the planar laboratory, `r=1` is fully blind:

\[
G_W^{Pl}(1)=38
\]

for all four split worlds.

On the torus the same symmetric direction gives

\[
50,50,50,38,
\]

so it is no longer fully blind. The exact blind sets satisfy

\[
\boxed{B_*^{Pl}=\{1\},\qquad B_*^{T^2}=\varnothing.}
\]

Thus the carrier changes not only response values but the singular set of the observer family itself.

## 9. Exact observer/carrier diagram

The same integer therefore supports the following exact chain of distinctions:

\[
\boxed{
\text{integer value}
\;\Rightarrow\;1\text{ class on }\mathcal W_9,
}
\]

\[
\boxed{
\text{scalar 1D--planar gain}
\;\Rightarrow\;2\text{ classes on }\mathcal W_9,
}
\]

and, on the four split worlds,

\[
\boxed{
\text{one planar weighted sample }(r>1)
\;\Rightarrow\;3\text{ classes},
}
\]

\[
\boxed{
\text{two planar weighted samples}
\;\Rightarrow\;4\text{ classes},
}
\]

\[
\boxed{
\text{one rich polynomial observation}
\;\Rightarrow\;4\text{ classes},
}
\]

\[
\boxed{
\text{one toroidal weighted sample }(r>1)
\;\Rightarrow\;4\text{ classes}.
}
\]

This is the first exact multi-observer ladder for one rational integer in HATTER-SOL-12.

## 10. Interpretation

The key lesson is not that one observer is universally better. The resolving power depends jointly on

\[
(n,W,C,O).
\]

For the same integer:

- a numerical observer sees no world distinction;
- a scalar geometry observer sees only the quadratic splitting sector;
- a weighted directional observer reveals additional split-world structure;
- a polynomial observer resolves all four split worlds in one shot;
- a carrier change from plane to torus makes even a scalar one-shot observation sufficient for the same four-world laboratory.

This is an exact finite realization of the HATTER-SOL-12 thesis that world structure, carrier and observer are independent coordinates of structural visibility.
