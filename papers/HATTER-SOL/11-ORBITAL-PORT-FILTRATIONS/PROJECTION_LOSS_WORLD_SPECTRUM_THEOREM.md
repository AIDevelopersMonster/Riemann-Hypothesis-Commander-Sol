# HATTER-SOL-11 · PROJECTION-LOSS WORLD-SPECTRUM THEOREM

**Status:** closed theorem layer.  
**Purpose:** characterize exactly when a linear coarse projection of a vector-valued world response preserves or annihilates world-Laplacian modes, and separate this from nonlinear scalar minimization.

---

## 1. Setup

Let `W` be a finite weighted world graph with Laplacian `L_W`. Let `V` and `U` be finite-dimensional vector spaces over a field of characteristic zero. A rich world response is a function

\[
F:V(W)\to V.
\]

Equivalently `F` lies in

\[
\mathbb K^{V(W)}\otimes V.
\]

Let

\[
P:V\to U
\]

be a linear response projection, applied pointwise to the signal. Then

\[
PF:V(W)\to U.
\]

The world Laplacian acts only on the world coordinate:

\[
L_W\otimes I_V.
\]

---

## 2. Projection commutes with the world Laplacian

### Theorem PL11.1

For every linear projection `P:V->U`,

\[
\boxed{
P(L_WF)=L_W(PF).
}
\]

More precisely,

\[
(I\otimes P)(L_W\otimes I_V)
=
(L_W\otimes I_U)(I\otimes P).
\]

### Proof

The two operators act on different tensor factors, hence commute. Pointwise, both sides equal the weighted sum of projected edge differences. QED.

Thus linear coarse-graining never moves information between distinct world eigenvalues. It can only preserve or annihilate components already present in each eigenspace.

---

## 3. Exact mode-preservation criterion

Let `E_lambda` be the world-Laplacian eigenspace for eigenvalue `lambda`, and let

\[
F=\sum_\lambda F_\lambda,
\qquad
F_\lambda\in E_\lambda\otimes V
\]

be the spectral decomposition.

### Theorem PL11.2 — eigenspacewise loss law

For every eigenvalue `lambda`,

\[
\boxed{
(PF)_\lambda=(I\otimes P)F_\lambda.
}
\]

Therefore:

1. the `lambda`-mode is preserved iff `(I\otimes P)F_\lambda != 0`;
2. the `lambda`-mode is annihilated iff
   \[
   \boxed{F_\lambda\in E_\lambda\otimes\ker P};
   \]
3. no linear projection can convert a nonzero `lambda`-mode into a different eigenvalue `mu != lambda`.

### Proof

Apply PL11.1 to the spectral projector of `L_W`; since `P` commutes with `L_W`, it commutes with every polynomial in `L_W`, hence with every spectral projector. QED.

---

## 4. Injectivity criterion on occupied response directions

Let

\[
S_F:=\operatorname{span}\{v\in V:\text{some coefficient of }F\text{ uses }v\}
\]

be the occupied response subspace.

### Corollary PL11.2a

If `P` is injective on `S_F`, then the set of occupied world eigenvalues is preserved exactly.

Conversely, if `ker P` intersects an occupied spectral coefficient subspace nontrivially, spectral loss is possible, and occurs exactly on the part lying in that intersection.

Thus the correct object for linear projection loss is not merely `ker P`, but

\[
\boxed{
(E_\lambda\otimes V)\cap\ker(I\otimes P)
=E_\lambda\otimes\ker P.
}
\]

---

## 5. Edge-derivative version

For an oriented world edge `e=(R,R')`, write

\[
D_eF=F(R')-F(R).
\]

Then linearity gives

\[
\boxed{D_e(PF)=P(D_eF).}
\]

Hence a rich world edge is invisible after projection exactly when

\[
\boxed{D_eF\in\ker P.}
\]

This is the local counterpart of PL11.2.

---

## 6. Geometry-coupling version

Let `Gamma_R` be any linearized geometry difference, for example

\[
\Gamma_R=Z_{Pl}(R)-Z_{1D}(R)
\]

in an additive response group. Then along a world edge `e`,

\[
H_{e,G}=D_e\Gamma.
\]

For every linear projection `P`,

\[
\boxed{P(H_{e,G})=D_e(P\Gamma).}
\]

Therefore a nonzero rich mixed world-geometry mode can disappear after coarse projection precisely when the corresponding mixed response lies in `ker P`.

---

## 7. Important boundary: scalar minimum is nonlinear

The map taking a Pareto response to its minimum scalar boundary is not linear. Schematically,

\[
M(Z)=\min\{B_A+B_O:(B_A,B_O)\in\operatorname{supp}Z\}.
\]

In general,

\[
M(Z_1-Z_2)
\]

is not meaningful as a linear response projection, and

\[
M(L_WZ)\ne L_W(MZ)
\]

need not hold.

Therefore the exact scalar collapse found for `61^6` is a **nonlinear coarse-graining phenomenon**, not an instance of PL11.1.

This distinction is essential:

- linear projections admit exact eigenspacewise loss theory;
- tropical/minimum-type summaries require a separate nonlinear theory.

---

## 8. First nonlinear loss invariant

For a rich world signal `F` and a nonlinear coarse map `M`, define the edge loss indicator

\[
\boxed{
\ell_e(F;M)=
\begin{cases}
1,&D_eF\ne0\text{ but }D_e(MF)=0,\\
0,&\text{otherwise}.
\end{cases}}
\]

This records whether the coarse observable erases a genuine world distinction on an edge.

For a set of edges `E_0`, define the hidden-edge count

\[
\boxed{
N_{hidden}(F;M,E_0)=\sum_{e\in E_0}\ell_e(F;M).
}
\]

No claim of universality is attached to this simplest statistic; it is the first exact discrete observable for nonlinear projection loss.

---

## 9. Application to the `61^6` geometry signal

Take the rich typed geometry signal `Gamma_R` from `PRIME_61_GEOMETRY_SIGNAL_SPECTRUM_CORE.md` and let `M` be minimum scalar boundary gain.

On the three split leaf edges from Gaussian,

\[
[-1]\leftrightarrow[-3],
\quad
[-1]\leftrightarrow[-19],
\quad
[-1]\leftrightarrow[-163],
\]

we have

\[
D_e\Gamma\ne0
\]

by GS11.2, while

\[
D_e(M\Gamma)=0
\]

because all four split worlds have scalar geometry gain 38.

Therefore

\[
\boxed{
\ell_e(\Gamma;M)=1
}
\]

for all three split edges, and

\[
\boxed{
N_{hidden}=3
}
\]

on the split substar.

This is the first exact nonlinear projection-loss count in the programme.

---

## 10. Research consequence

The response programme now has two distinct information-loss theories:

### Linear spectral loss

Controlled exactly by

\[
E_\lambda\otimes\ker P.
\]

### Nonlinear coarse loss

Detected operationally by world or mixed derivatives that vanish only after a nonlinear summary such as scalar minimum.

The next natural theorem target is to determine conditions under which a nonlinear tropical projection preserves enough edge data to reconstruct a rich response up to a controlled equivalence class.
