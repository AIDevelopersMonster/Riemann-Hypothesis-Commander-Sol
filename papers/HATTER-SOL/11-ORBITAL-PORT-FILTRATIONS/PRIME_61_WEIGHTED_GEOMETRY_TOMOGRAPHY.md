# HATTER-SOL-11 · PRIME 61 WEIGHTED GEOMETRY TOMOGRAPHY

**Status:** closed theorem layer.  
**Probe:** `N=61^6`.  
**Scope:** the four split class-number-one UFD worlds, canonical host `n=12`, strict 1D versus planar Xi responses.

---

## 1. Weighted geometry gain

Let

\[
a=w_A>0,\qquad o=w_O>0.
\]

For a finite response support `S`, define

\[
m_S(a,o)=\min_{(B_A,B_O)\in S}(aB_A+oB_O).
\]

For a world `R`, define the weighted geometry gain

\[
\boxed{
g_R(a,o)=m_{1D,R}(a,o)-m_{Pl,R}(a,o).}
\]

Positive homogeneity allows one to reduce to the ratio `r=o/a`, but the symmetric two-weight formulas are retained below.

The four split states of 61 are

\[
\Delta=-4:(6,5),\quad
\Delta=-3:(5,4),\quad
\Delta=-19:(7,1),\quad
\Delta=-163:(4,1).
\]

---

## 2. Gaussian world

The exact 1D front is the segment of step-two lattice points from

\[
(50,60)\quad\text{to}\quad(72,38),
\]

and the exact planar front is the segment from

\[
(12,60)\quad\text{to}\quad(72,0).
\]

Both have direction `(2,-2)`, so the active endpoint changes at `a=o`.

Hence

\[
\boxed{
g_{-4}(a,o)=
\begin{cases}
38a,&a\ge o,\\
38o,&a\le o.
\end{cases}}
\]

Equivalently,

\[
\boxed{g_{-4}(a,o)=38\max(a,o).}
\]

---

## 3. Eisenstein world

The 1D front runs from

\[
(38,48)\quad\text{to}\quad(60,26),
\]

whereas the planar front runs from

\[
(0,48)\quad\text{to}\quad(48,0).
\]

Again the switch occurs at `a=o`. Thus

\[
\boxed{
g_{-3}(a,o)=
\begin{cases}
38a,&a\ge o,\\
12a+26o,&a\le o.
\end{cases}}
\]

At `a=o`, both branches equal `38a`.

---

## 4. Delta = -19

For state `(7,1)`, the 1D front runs from

\[
(62,12)\quad\text{to}\quad(74,0),
\]

and the planar front from

\[
(24,12)\quad\text{to}\quad(36,0).
\]

The two fronts differ by the constant translation `(38,0)` pointwise along their common six-step parameter.

Therefore

\[
\boxed{g_{-19}(a,o)=38a\qquad\text{for every }a,o>0.}
\]

This world is geometrically anisotropic in the strongest possible sense for this observable: the planar improvement is entirely axial and independent of the oblique weight.

---

## 5. Delta = -163

For state `(4,1)`, the 1D front runs from

\[
(26,12)\quad\text{to}\quad(38,0),
\]

while the planar response is the saturated singleton

\[
(0,0).
\]

Hence

\[
\boxed{
g_{-163}(a,o)=
\begin{cases}
26a+12o,&a\ge o,\\
38a,&a\le o.
\end{cases}}
\]

Again the branches agree at `a=o`.

---

## 6. Exact four-world tomography theorem

### Theorem WT11.1 — all four split worlds are separated by weighted geometry gain

The four functions

\[
g_{-4},\quad g_{-3},\quad g_{-19},\quad g_{-163}
\]

are pairwise distinct on the positive weight cone.

Yet at the symmetric weight they all coincide:

\[
\boxed{g_R(1,1)=38}
\]

for every split world `R`.

### Proof

The equality at `(1,1)` follows directly from the formulas.

For pairwise separation:

- if `o>a`, then
  \[
  g_{-4}=38o,
  \quad g_{-3}=12a+26o,
  \quad g_{-19}=38a,
  \quad g_{-163}=38a;
  \]
  here Gaussian and Eisenstein are distinct from each other and from the latter pair;
- if `a>o`, then
  \[
  g_{-4}=g_{-3}=g_{-19}=38a,
  \quad g_{-163}=26a+12o<38a;
  \]
  so `-163` separates from the other three;
- to distinguish `-19` from `-163`, choose `a>o`;
- to distinguish `-3` from `-19`, choose `o>a`, where
  \[
  (12a+26o)-38a=26(o-a)>0;
  \]
- to distinguish `-4` from `-3`, choose `o>a`, where
  \[
  38o-(12a+26o)=12(o-a)>0.
  \]

Thus every pair differs for some positive weight. QED.

---

## 7. One-parameter normalized signatures

Set `a=1` and `r=o/a>0`. Then

\[
\boxed{
G_{-4}(r)=
\begin{cases}38,&r\le1,\\38r,&r\ge1,
\end{cases}}
\]

\[
\boxed{
G_{-3}(r)=
\begin{cases}38,&r\le1,\\12+26r,&r\ge1,
\end{cases}}
\]

\[
\boxed{G_{-19}(r)=38,}
\]

\[
\boxed{
G_{-163}(r)=
\begin{cases}26+12r,&r\le1,\\38,&r\ge1.
\end{cases}}
\]

All four meet at the single symmetric point

\[
(r,G)=(1,38).
\]

Away from that point, the slopes encode which channel is responsible for the geometry gain.

For `r>1`, the slopes are

\[
38,\quad26,\quad0,\quad0
\]

for `-4,-3,-19,-163`.

For `r<1`, the slopes with respect to `r` are

\[
0,\quad0,\quad0,\quad12.
\]

Thus the two sides of the symmetric weight probe complementary interface information.

---

## 8. Two generic weight samples suffice for this four-world laboratory

Choose any

\[
r_-\in(0,1),\qquad r_+>1.
\]

Consider the ordered measurement pair

\[
\boxed{\mathcal T_R=(G_R(r_-),G_R(r_+)).}
\]

### Corollary WT11.1a

For the four split worlds of `61^6`, the map

\[
R\mapsto\mathcal T_R
\]

is injective.

### Proof

At `r_-<1`, `-163` is the unique world with value below 38; the other three equal 38.

At `r_+>1`, the remaining three have respectively

\[
38r_+,
\quad12+26r_+,
\quad38,
\]

which are strictly ordered for `r_+>1`:

\[
38r_+>12+26r_+>38.
\]

Hence all four signatures are distinct. QED.

So although the symmetric scalar observable collapses all split worlds, **two asymmetric weighted scalar measurements reconstruct the world within this finite split laboratory**.

---

## 9. Interpretation

This is a stronger conclusion than merely saying that the full polynomial contains more information.

For this exact laboratory:

1. the single total-boundary scalar `(1,1)` loses all split-sector distinction;
2. the complete weighted family separates all four split worlds;
3. in fact two generic asymmetric samples already suffice;
4. the full polynomial remains richer, because tropical tomography in general loses discrete support information by TP11.3.

Thus the information hierarchy is experimentally strict but not uniformly expensive: some world information destroyed by one coarse scalar can be recovered by a very small number of directional scalar probes.

This suggests a new quantitative invariant: the **tomographic dimension** of a finite world laboratory — the minimum number of admissible weight directions needed to separate its world responses.
