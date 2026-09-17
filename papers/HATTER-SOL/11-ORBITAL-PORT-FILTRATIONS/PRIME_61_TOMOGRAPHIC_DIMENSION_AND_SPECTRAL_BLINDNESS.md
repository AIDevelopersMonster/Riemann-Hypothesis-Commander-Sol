# HATTER-SOL-11 · PRIME 61 TOMOGRAPHIC DIMENSION AND SPECTRAL BLINDNESS

**Status:** closed theorem layer.  
**Probe:** `61^6`.  
**Laboratory:** the four split class-number-one UFD worlds `Delta=-4,-3,-19,-163`.  
**Observable:** normalized weighted geometry gain `G_R(r)`, where `r=w_O/w_A>0`.

---

## 1. Exact signatures

From `PRIME_61_WEIGHTED_GEOMETRY_TOMOGRAPHY.md`,

\[
G_{-4}(r)=\begin{cases}38,&r\le1,\\38r,&r\ge1,\end{cases}
\]

\[
G_{-3}(r)=\begin{cases}38,&r\le1,\\12+26r,&r\ge1,\end{cases}
\]

\[
G_{-19}(r)=38,
\]

\[
G_{-163}(r)=\begin{cases}26+12r,&r\le1,\\38,&r\ge1.\end{cases}
\]

All four meet at `(r,G)=(1,38)`.

---

## 2. Tomographic dimension

For a finite world laboratory `L` and a family of scalar probes `G_R(r)`, define the **tomographic dimension** `tdim(L;G)` to be the smallest integer `m` for which there exist admissible directions

\[
r_1,\ldots,r_m>0
\]

such that the evaluation map

\[
R\longmapsto (G_R(r_1),\ldots,G_R(r_m))
\]

is injective on `L`.

If no finite family separates the worlds, set `tdim=infinity`.

### Theorem TD11.1 — exact tomographic dimension of the split 61 laboratory

For

\[
L_{61}^{split}=\{-4,-3,-19,-163\},
\]

\[
\boxed{\operatorname{tdim}(L_{61}^{split};G)=2.}
\]

### Proof

**Upper bound.** Choose any `r_- in (0,1)` and any `r_+>1`. At `r_-`, world `-163` is the unique world below 38. At `r_+`, the remaining three take the strictly ordered values

\[
38r_+>12+26r_+>38.
\]

Thus two samples separate all four worlds, so `tdim<=2`.

**Lower bound.** No one sample suffices:

- if `0<r<1`, then
  \[
  G_{-4}(r)=G_{-3}(r)=G_{-19}(r)=38;
  \]
- if `r=1`, all four values equal 38;
- if `r>1`, then
  \[
  G_{-19}(r)=G_{-163}(r)=38.
  \]

Hence every single weight direction identifies at least two distinct worlds. Therefore `tdim>=2`. QED.

This is the first exact tomographic-dimension computation in the HATTER-SOL world-response programme.

---

## 3. Split-world graph and spectral blindness

The induced split-world prime-toggle graph is the star `K_{1,3}` centered at the Gaussian world `-4`, with leaves `-3,-19,-163`.

Its standard Laplacian spectrum is

\[
\boxed{0,1,1,4.}
\]

For each weight ratio `r`, regard

\[
G(r)=(G_{-4}(r),G_{-3}(r),G_{-19}(r),G_{-163}(r))
\]

as a scalar signal on this star.

### Theorem TD11.2 — the symmetric weight is a complete nonconstant spectral blind direction

At

\[
r=1,
\]

\[
\boxed{G(1)=38\mathbf1.}
\]

Hence

\[
\boxed{L_WG(1)=0}
\]

and every nonconstant world-Laplacian mode has zero coefficient.

For every `r!=1`, `G(r)` is nonconstant, so at least one positive-eigenvalue world mode is nonzero.

### Proof

At `r=1`, the four explicit formulas all equal 38, so the signal lies entirely in the constant eigenspace.

If `r<1`, the `-163` value is `26+12r<38`, while the other three equal 38. If `r>1`, the Gaussian value is `38r>38`. Thus the signal is nonconstant whenever `r!=1`. A signal on a connected graph has no positive-eigenvalue component iff it is constant. QED.

Thus `(1,1)` is not merely an unfortunate coarse choice; it is an exact spectral blind direction for this laboratory.

---

## 4. Exact spectrum for `0<r<1`

Put

\[
d:=12(1-r)>0.
\]

Then, relative to the constant value 38,

\[
G(r)=38\mathbf1+(0,0,0,-d).
\]

Let

\[
v_*=(3,-1,-1,-1),
\]

so `Lv_*=4v_*`.

The leaf mean is

\[
38-d/3,
\]

while the center is 38, so the radial coefficient is

\[
b=\frac{d/3}{4}=\frac d{12}=1-r.
\]

Therefore the eigenvalue-four component is

\[
(1-r)v_*.
\]

The remaining nonconstant component lies in the eigenvalue-one leaf-contrast space. Thus both positive spectral sectors are activated for every `0<r<1`.

The Dirichlet energy can be read directly from the star edges: only the edge to `-163` changes, with jump `d`. Hence

\[
\boxed{\mathcal E(G(r))=144(1-r)^2,\qquad0<r<1.}
\]

---

## 5. Exact edge energy for `r>1`

Put

\[
s:=r-1>0.
\]

Then the four values are

\[
38+38s,
\quad38+26s,
\quad38,
\quad38.
\]

The three center-to-leaf jumps are therefore

\[
12s,
\quad38s,
\quad38s.
\]

Hence the exact Dirichlet energy is

\[
\boxed{
\mathcal E(G(r))
=(12^2+38^2+38^2)(r-1)^2
=3032(r-1)^2,
\qquad r>1.
}
\]

Thus the spectral response is strongly asymmetric across the blind direction:

\[
\boxed{
\mathcal E(G(r))=
\begin{cases}
144(1-r)^2,&0<r<1,\\
0,&r=1,\\
3032(r-1)^2,&r>1.
\end{cases}}
\]

The weight direction therefore controls not only whether world information is visible, but how strongly it is expressed in the world spectrum.

---

## 6. Interpretation

The symmetric scalar `(1,1)` lies exactly at a tomographic singularity:

- all four split worlds collide;
- tomographic rank drops to one class;
- all nonconstant world spectral energy vanishes.

Moving to either side activates hidden modes, but the two sides reveal different information:

- `r<1` first isolates `Delta=-163`;
- `r>1` separates Gaussian and Eisenstein from the low-tail pair;
- combining one direction from each side gives complete reconstruction within the four-world laboratory.

Thus the response field has an experimentally meaningful notion of **blind directions** and a finite **tomographic dimension**. These are properties of the chosen observable family, not of the abstract world graph alone.
