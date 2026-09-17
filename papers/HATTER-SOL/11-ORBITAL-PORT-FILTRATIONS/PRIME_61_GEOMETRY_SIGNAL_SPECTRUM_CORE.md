# HATTER-SOL-11 · PRIME 61 GEOMETRY-SIGNAL SPECTRUM CORE

**Status:** closed theorem layer.  
**Probe:** the same integer `N=61^6`.  
**World laboratory:** the nine imaginary-quadratic class-number-one UFD worlds.  
**Geometry comparison:** strict `1D -> planar`.  
**World graph:** the induced HATTER-SOL-09 star `K_{1,8}` centered at the Gaussian world.

## 1. Canonical host sizes

For `61^6`, split worlds have twelve irreducible factor nodes and inert worlds have six:

\[
\kappa_R(61^6)=\begin{cases}12,&61\text{ split in }R,\\6,&61\text{ inert in }R.\end{cases}
\]

The split worlds are `Delta=-4,-3,-19,-163`, with states `(6,5),(5,4),(7,1),(4,1)`. The inert worlds are `Delta=-8,-7,-11,-43,-67`, with rational-line state `(61,0)`.

## 2. Scalar geometry gain

Let `Lambda_C(R)` be the minimum scalar free boundary in geometry `C`, and define

\[
g_R:=\Lambda_{1D}(R)-\Lambda_{Pl}(R).
\]

### Theorem GS11.1 — splitting-character law

\[
\boxed{g_R=26+12\chi_R(61)},
\]

where `chi_R(61)=+1` for split and `-1` for inert. Equivalently,

\[
\boxed{g_R=38\text{ on split worlds},\qquad g_R=14\text{ on inert worlds}.}
\]

### Proof

In a split world, the canonical host has 12 vertices. The strict path has 11 edges and the exact icosahedral planar support has 30 edges, so the scalar boundary improvement is `2(30-11)=38`.

In an inert world, the canonical host has 6 vertices. The path has 5 edges and the octahedral planar support has 12 edges, so the improvement is `2(12-5)=14`. The displayed affine character formula is immediate. QED.

Thus this scalar observable forgets which of the four split interface states occurs; it remembers only split versus inert.

## 3. Exact star spectrum

For the unweighted star `K_{1,8}`, the standard Laplacian spectrum is

\[
0^{(1)},\qquad1^{(7)},\qquad9^{(1)}.
\]

The scalar signal has value 38 at the Gaussian center, value 38 on three split leaves, and value 14 on five inert leaves.

The leaf mean is

\[
\mu_L=(3\cdot38+5\cdot14)/8=23,
\]

and the global mean is

\[
\bar g=(38+8\cdot23)/9=74/3.
\]

Let

\[
v_*=(8,-1,-1,-1,-1,-1,-1,-1,-1),
\]

so `Lv_*=9v_*`. Then

\[
\boxed{g=\frac{74}{3}{\bf1}+\frac53v_*+h},
\]

where `Lh=h`, `h(center)=0`, `h=15` on each split leaf and `h=-9` on each inert leaf.

The scalar Dirichlet energy is

\[
\boxed{\mathcal E(g)=5\cdot24^2=2880}.
\]

The eigenvalue-nine contribution is `1800`, and the eigenvalue-one contribution is `1080`, hence

\[
\boxed{2880=1800+1080}.
\]

Thus exactly `5/8` of the scalar world energy is radial center-versus-leaves energy and `3/8` is leaf-contrast energy.

## 4. Rich typed signal detects hidden split-sector directions

Define the signed typed geometry signal

\[
\Gamma_R:=Z^{\Xi}_{Pl,\kappa_R(N)}(N)-Z^{\Xi}_{1D,\kappa_R(N)}(N)
\]

in the additive polynomial group.

For the four split worlds:

\[
\Gamma_{-4}=\sum_{j=0}^{30}X^{12+2j}Y^{60-2j}-\sum_{t=0}^{11}X^{50+2t}Y^{60-2t},
\]

\[
\Gamma_{-3}=\sum_{j=0}^{24}X^{2j}Y^{48-2j}-\sum_{t=0}^{11}X^{38+2t}Y^{48-2t},
\]

\[
\Gamma_{-19}=\sum_{j=0}^{6}X^{24+2j}Y^{12-2j}-\sum_{t=0}^{6}X^{62+2t}Y^{12-2t},
\]

\[
\Gamma_{-163}=1-\sum_{t=0}^{6}X^{26+2t}Y^{12-2t}.
\]

For every inert world,

\[
\Gamma_I=X^{342}-X^{356}.
\]

### Theorem GS11.2 — hidden split-sector sensitivity

Along each split leaf edge from Gaussian,

\[
[-1]\leftrightarrow[-3],\quad[-1]\leftrightarrow[-19],\quad[-1]\leftrightarrow[-163],
\]

one has

\[
\boxed{\Gamma_{leaf}-\Gamma_{-4}\ne0},
\]

while GS11.1 gives

\[
\boxed{g_{leaf}-g_{-4}=0}.
\]

### Proof

`Gamma_-4` has terms of `Y`-degree 60. `Gamma_-3` has `Y`-degree at most 48, `Gamma_-19` at most 12, and `Gamma_-163` contains the constant monomial `1`. Hence none equals `Gamma_-4`. The scalar derivative vanishes because all four worlds are split. QED.

Therefore scalarization kills genuine world directions that remain visible in the typed/Pareto response.

## 5. Polynomial star decomposition

Write `C=Gamma_-4`, `E=Gamma_-3`, `U=Gamma_-19`, `V=Gamma_-163`, `I=Gamma_I`. Define

\[
M=(E+U+V+5I)/8,
\qquad
A=(C+E+U+V+5I)/9,
\qquad
B=(C-M)/9.
\]

Then the full polynomial-valued world signal decomposes as

\[
\boxed{\Gamma=A{\bf1}+Bv_*+H},
\]

where `H(center)=0`, the leaf values are `E-M,U-M,V-M,I-M` (the last repeated five times), and

\[
LH=H,\qquad L(Bv_*)=9Bv_*.
\]

Both nonconstant sectors are nonzero. Hence the rich response has genuine support in both the eigenvalue-one and eigenvalue-nine world sectors.

## 6. Conclusion

For `61^6`, the scalar geometry observable collapses exactly to the quadratic splitting character, while the typed/Pareto observable resolves additional variation inside the split sector itself. This is the first exact spectral example in the programme of a coarse scalar symmetry hiding nontrivial world modes.
