# HATTER-SOL-12 · OBSERVATION-DIRECTION PHASE DIAGRAM

**Status:** exact theorem layer assembled from the closed planar and toroidal `61^6` weighted-response formulas.  
**Probe:** `N=61^6`.  
**World laboratory:** `L={-4,-3,-19,-163}`.  
**Observer parameter:** `r=w_O/w_A>0`.

## 1. Resolving class count

For a carrier `C` and a one-parameter scalar response `F_R^C(r)`, define

\[
\boxed{
D_C(r):=\#\{F_R^C(r):R\in L\}.
}
\]

Thus `D_C(r)` is the number of arithmetic worlds distinguished by one observation in direction `r`. It is a partition count, not an entropy.

For four worlds,

\[
1\le D_C(r)\le4.
\]

---

## 2. Planar phase diagram

The exact planar signatures are

\[
F_{-4}^{Pl}(r)=
\begin{cases}
38,&r\le1,\\
38r,&r\ge1,
\end{cases}
\]

\[
F_{-3}^{Pl}(r)=
\begin{cases}
38,&r\le1,\\
12+26r,&r\ge1,
\end{cases}
\]

\[
F_{-19}^{Pl}(r)=38,
\]

\[
F_{-163}^{Pl}(r)=
\begin{cases}
26+12r,&r\le1,\\
38,&r\ge1.
\end{cases}
\]

### Theorem OD12.1 — exact planar resolution phases

\[
\boxed{
D_{Pl}(r)=
\begin{cases}
2,&0<r<1,\\
1,&r=1,\\
3,&r>1.
\end{cases}}
\]

### Proof

If `0<r<1`, the worlds `-4,-3,-19` all have value `38`, while `-163` has value `26+12r<38`. Hence there are exactly two classes.

At `r=1`, all four values equal `38`, so there is one class.

If `r>1`, the values are

\[
38r,\qquad12+26r,\qquad38,\qquad38.
\]

The first two differ because

\[
38r-(12+26r)=12(r-1)>0,
\]

and both exceed `38`. Thus the four worlds form exactly three classes. QED.

Hence the symmetric direction is a genuine resolution singularity:

\[
\boxed{2\to1\to3}
\]

when `r` crosses `1` from left to right.

---

## 3. Toroidal phase diagram

For the explicit triangular torus `T_12`, the exact signatures are

\[
F_{-4}^{T}(r)=
\begin{cases}
50,&r\le1,\\
12+38r,&r\ge1,
\end{cases}
\]

\[
F_{-3}^{T}(r)=
\begin{cases}
38+12r,&r\le1,\\
24+26r,&r\ge1,
\end{cases}
\]

\[
F_{-19}^{T}(r)=50,
\]

\[
F_{-163}^{T}(r)=
\begin{cases}
26+12r,&r\le1,\\
38,&r\ge1.
\end{cases}
\]

### Theorem OD12.2 — exact toroidal resolution phases

\[
\boxed{
D_T(r)=
\begin{cases}
3,&0<r<1,\\
2,&r=1,\\
4,&r>1.
\end{cases}}
\]

### Proof

For `0<r<1`, `-4` and `-19` both have value `50`. The remaining values are

\[
38+12r,
\qquad
26+12r,
\]

which differ by `12`. Both are strictly below `50`: the first because `r<1`, the second because `26+12r<38<50`. Hence exactly three classes occur.

At `r=1`, the values are

\[
50,50,50,38,
\]

so there are exactly two classes.

For `r>1`, the values are

\[
12+38r,
\qquad
24+26r,
\qquad
50,
\qquad
38.
\]

The first two differ by `12(r-1)>0`. The second exceeds `50` because `24+26r>50` iff `r>1`; therefore the first also exceeds `50`. Finally `50\ne38`. Hence all four values are pairwise distinct. QED.

Thus the toroidal phase sequence is

\[
\boxed{3\to2\to4.}
\]

---

## 4. Carrier resolution gain

Define the one-shot carrier resolution gain

\[
\Delta_D(r):=D_T(r)-D_{Pl}(r).
\]

### Corollary OD12.3

For every `r>0`,

\[
\boxed{\Delta_D(r)=1.}
\]

### Proof

Subtract the exact phase counts:

- `3-2=1` for `0<r<1`;
- `2-1=1` for `r=1`;
- `4-3=1` for `r>1`.

QED.

This is stronger than the previously noted transition `tdim_Pl=2 -> tdim_T=1`: in this laboratory, **the torus distinguishes exactly one additional world class at every observation direction**.

---

## 5. Normalized one-shot resolution

For a four-world laboratory define

\[
\rho_C(r):=\frac{D_C(r)-1}{3}.
\]

Then

\[
\rho_{Pl}(r)=
\begin{cases}
1/3,&0<r<1,\\
0,&r=1,\\
2/3,&r>1,
\end{cases}
\]

and

\[
\rho_T(r)=
\begin{cases}
2/3,&0<r<1,\\
1/3,&r=1,\\
1,&r>1.
\end{cases}
\]

The carrier therefore shifts the entire one-shot resolution profile upward by exactly `1/3`.

This normalized quantity is a finite distinguishability index only; it is not Shannon information.

---

## 6. Interpretation

The observer direction and the carrier act jointly. The same scalar measurement family has different partition structures on the same four arithmetic worlds:

\[
\boxed{
D_{Pl}:2\to1\to3,
\qquad
D_T:3\to2\to4.
}
\]

The singular direction `r=1` survives as a local resolution minimum on both carriers, but its severity changes:

- plane: complete blindness, one class;
- torus: partial blindness, two classes.

Thus carrier change can alter not merely numerical response values but the **partition-valued phase diagram of an observer family**.

This exact phase diagram is a natural central example for HATTER-SOL-12.