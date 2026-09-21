# HATTER-SOL-21 · MULTIWORLD SURFACE TOMOGRAPHY

Status: **EXPLORATORY EXACT THEOREM LAYER**

## 1. Why this is not H15 repeated

HATTER-SOL-15 already compared the same two-port algebra under different
surface laws (torus, Klein bottle, genus two), and already proved defect
storage/compensation.

H21 asks the orthogonal question:

\[
\boxed{
\text{Can one fixed surface carry several different arithmetic-world probes at once?}
}
\]

The handles of the surface are used as independent world-observer slots.

## 2. Arithmetic core inherited from H15

Let

\[
V=A/pA\cong\mathbf F_p^r
\]

for an odd prime \(p\), and let \(a\in V\) be the arithmetic class being
observed.

A calibrated world is represented by a linear functional

\[
\ell_i\in V^*.
\]

Its oriented Frobenius coordinate is

\[
\alpha_i(a)=\ell_i(a)\in\mathbf F_p.
\]

Use the dihedral port pair on handle \(i\)

\[
A_i(a)=R^{\ell_i(a)},
\qquad
B_i=S.
\]

H15 gives

\[
\boxed{
K_i(a):=[A_i(a),B_i]=R^{2\ell_i(a)}.
}
\]

Because \(p\) is odd, multiplication by \(2\) is invertible, so the oriented
handle holonomy carries exactly the same information as \(\ell_i(a)\).

## 3. Ready-made surfaces

Use the standard closed orientable genus-\(g\) surface

\[
\Sigma_g
\]

with fundamental-polygon law

\[
\boxed{
[a_1,b_1]\cdots[a_g,b_g]=1.
}
\]

Concrete realizations:

- \(g=0\): sphere;
- \(g=1\): torus;
- \(g=2\): standard hyperbolic regular-octagon model;
- \(g\ge2\): standard hyperbolic \(4g\)-gon model.

The metric realization is not the arithmetic datum. The arithmetic datum is
the connection/holonomy placed on the fixed surface.

## 4. Handle-resolved observer

Define

\[
\boxed{
H_g(a)
=
(K_1(a),\ldots,K_g(a)).
}
\]

Equivalently, after reading the rotation exponents,

\[
H_g(a)\leftrightarrow 2L_g(a),
\]

where

\[
L_g:V\to\mathbf F_p^g,
\qquad
L_g(a)
=
(\ell_1(a),\ldots,\ell_g(a)).
\]

### Theorem H21-S1 — exact surface tomography rank

The indistinguishability kernel of the handle-resolved surface observer is

\[
\boxed{
\ker H_g
=
\bigcap_{i=1}^{g}\ker\ell_i.
}
\]

Hence the number of oriented surface signatures is

\[
\boxed{
p^{\operatorname{rank}L_g}.
}
\]

The surface reconstructs \(a\) exactly iff

\[
\boxed{
\operatorname{span}\{\ell_1,\ldots,\ell_g\}=V^*.
}
\]

In particular, under the one-world-per-handle architecture, exact oriented
reconstruction requires

\[
\boxed{g\ge r,}
\]

and genus \(g=r\) suffices by choosing a basis of \(V^*\).

### Proof

The map from \(\ell_i(a)\) to \(K_i(a)=R^{2\ell_i(a)}\) is injective because
\(2\) is invertible modulo \(p\). Therefore two arithmetic states have the
same handle vector iff all \(\ell_i\) agree on their difference. The kernel is
the intersection of the kernels. Rank-nullity gives the signature count and
the reconstruction criterion. QED.

This theorem is elementary linear algebra once the H15 arithmetic transport is
fixed. The H21 content is the surface-multiplexing interpretation.

## 5. Global-only surface observer

A coarse observer may ignore individual handles and retain only the total
surface-relator defect:

\[
K_\Sigma(a)
=
\prod_{i=1}^{g}K_i(a).
\]

Because all \(K_i\) are rotations,

\[
\boxed{
K_\Sigma(a)
=
R^{2\sum_i\ell_i(a)}.
}
\]

### Theorem H21-S2 — genus does not increase global rank

For every \(g\ge1\), the global-only oriented observer factors through the
single functional

\[
\boxed{
\ell_\Sigma=\ell_1+\cdots+\ell_g.
}
\]

Therefore its rank is at most one, regardless of genus.

If \(\ell_\Sigma\ne0\), it has exactly \(p\) signatures and each signature has
fiber size \(p^{r-1}\).

Thus

\[
\boxed{
\text{more handles without handle-resolved observation do not create more tomographic rank.}
}
\]

This is the first negative control of the surface programme.

## 6. Global flatness can hide local curvature

The closed surface is globally flat for the total relator exactly when

\[
K_\Sigma(a)=1,
\]

equivalently

\[
\boxed{
\sum_i\ell_i(a)=0.
}
\]

This does not imply

\[
\ell_i(a)=0
\]

for every handle. Therefore a globally flat surface may contain nontrivial
local arithmetic holonomies that cancel.

For \(g=2\),

\[
\ell_2(a)=-\ell_1(a)\ne0
\]

is the simplest example.

This generalizes the H15 defect-compensation phenomenon from one repeated
dihedral port pair to independently calibrated arithmetic-world channels.

## 7. Coarse flat/curved handle observer

Define only the curvature bits

\[
b_i(a)
=
\mathbf 1_{\{\ell_i(a)\ne0\}}.
\]

Then

\[
B_g(a)=(b_1(a),\ldots,b_g(a))
\]

forgets each nonzero coordinate value but retains its support pattern.

For independent coordinate functionals and \(g\le r\),

\[
\boxed{
|B_g(V)|=2^g.
}
\]

## 8. Metric curvature is a negative control

Sphere, flat torus, and hyperbolic genus-\(g\) surfaces have different
intrinsic Gaussian-curvature regimes.

However, if arithmetic edge transports are assigned independently of the
metric, changing the metric alone cannot create arithmetic information.

Therefore H21 does **not** claim that negative Gaussian curvature reveals
primes by itself.

The first meaningful coupling is topological/connection-theoretic:

\[
\boxed{
\text{surface law}
+
\text{world-derived transport}
\to
\text{holonomy response}.
}
\]

A genuine metric-arithmetic coupling would require an additional rule and must
be tested separately.

## 9. Literature boundary

The following are classical and not novelty claims:

- surface-group presentations;
- flat connections and holonomy representations;
- lattice-gauge plaquette holonomy / Wilson-loop ideas;
- representation varieties;
- discrete differential geometry and intrinsic curvature of triangulated surfaces.

H21 novelty, if any, must come from a theorem about the composed object

\[
\boxed{
\text{arithmetic world channels}
\to
\text{surface-handle transport}
\to
\text{observer quotient}
\to
\text{tomographic rank / hardware cost}.
}
\]

## 10. Immediate experimental target

H21-LAB-02 uses

\[
p=7,\qquad V=\mathbf F_7^3
\]

with the first \(g\) coordinate functionals placed on the handles of
\(\Sigma_g\), for \(g=0,1,2,3\).

It exhaustively measures four observers:

1. global flatness;
2. global oriented holonomy;
3. handle-resolved flatness;
4. handle-resolved oriented holonomy.

Expected decisive contrast:

\[
\boxed{
1\to7\to49\to343
}
\]

for handle-resolved oriented signatures as genus increases from \(0\) to \(3\),
while the global oriented observer remains capped at \(7\) signatures for
every \(g\ge1\).
