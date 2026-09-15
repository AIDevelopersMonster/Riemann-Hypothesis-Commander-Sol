# HATTER-SOL-15 · Mahler Response Orbit Code and Multiplicative Parseval Law

**Status:** exact theorem layer for prime dihedral worlds in the range `mu>=4` (`lambda<=0`).  
**Input:** `PRIMITIVE_MAHLER_CHANNEL_SEPARATION.md`.  
**Purpose:** assemble the distinct primitive Mahler values into a world/port response vector and determine exactly what geometry and harmonic information this vector carries.

The outcome is a continuous analogue of the earlier projective world-signature code, but with a different and richer symmetry: the response vectors form a regular orbit of the multiplicative group

\[
G_p=(\mathbf F_p^\times)/\{\pm1\},
\qquad |G_p|=m:=\frac{p-1}{2}.
\]

The associated Gram matrix is a group-circulant matrix diagonalized by the even Dirichlet characters modulo `p`.

---

## 1. Primitive Mahler profile

Fix an odd prime `p` and `mu>=4`. For a mirror class

\[
x=[k]\in G_p,
\]

put

\[
\vartheta_x=2\cos\frac{2\pi k}{p}
\]

and define the primitive Mahler profile

\[
\boxed{
f_\mu(x):=M_\mu(\vartheta_x).}
\]

By the strict separation theorem already proved,

\[
\boxed{x\ne y\Longrightarrow f_\mu(x)\ne f_\mu(y).}
\]

Thus `f_mu` is an injective real-valued function on `G_p`.

For an object reaction

\[
a\in G_p,
\]

define its full labelled Mahler response vector

\[
\boxed{
\mathbf M_a(x):=f_\mu(ax),
\qquad x\in G_p.
}
\]

Hence every object response is a multiplicative translate of one base profile.

---

## Theorem H15.98 — exact orbit-code structure

The family

\[
\mathcal M_{p,\mu}
:=\{\mathbf M_a:a\in G_p\}
\subset\mathbf R^m
\]

is the regular permutation orbit of the base vector `f_mu` under `G_p`.

In particular:

1. every codeword has the same Euclidean norm;
2. every coordinate multiset is the same;
3. the action of `G_p` on the codewords is free and transitive;
4. the map
   \[
   \boxed{a\longmapsto\mathbf M_a}
   \]
   is injective.

### Proof

Let `P_a` be the permutation matrix induced by multiplication `x -> ax` on `G_p`. Then

\[
\mathbf M_a=P_a f_\mu.
\]

The first three assertions follow from the regular action. If `M_a=M_b`, then evaluating at `x=1` gives

\[
f_\mu(a)=f_\mu(b),
\]

and injectivity of `f_mu` gives `a=b`. QED.

Thus the entire signless reaction coordinate is encoded equivariantly by the continuous Mahler response vector.

---

## 2. Exact distance geometry

For `g in G_p`, define

\[
D_\mu(g)^2
:=
\sum_{x\in G_p}
\bigl(f_\mu(x)-f_\mu(gx)\bigr)^2.
\]

## Theorem H15.99 — pairwise distances depend only on reaction ratio

For all `a,b in G_p`,

\[
\boxed{
\|\mathbf M_a-\mathbf M_b\|_2^2
=D_\mu(a^{-1}b)^2.
}
\]

Moreover,

\[
\boxed{
D_\mu(g)>0
\quad\text{for every }g\ne1.
}
\]

### Proof

Change variables `x -> ax` in the Euclidean sum. If `g ne 1`, the regular multiplication action has no fixed points, so `gx ne x` for every `x`. Since `f_mu` is injective, every summand is strictly positive. QED.

Let

\[
\Delta_{p,\mu}
:=
\min_{x\ne y}|f_\mu(x)-f_\mu(y)|>0.
\]

Because every nonidentity multiplier moves all `m` coordinates,

\[
\boxed{
D_\mu(g)^2
\ge m\,\Delta_{p,\mu}^2
\qquad(g\ne1).
}
\]

Thus the response orbit is not only injective: it has a strictly positive Euclidean minimum distance.

This is a continuous-response analogue of the finite projective incidence code, although no digital coding claim is intended.

---

## 3. Centering and the Mahler Gram kernel

Let

\[
\bar f_\mu
:=\frac1m\sum_{x\in G_p}f_\mu(x),
\]

and define

\[
f_\mu^\circ(x):=f_\mu(x)-\bar f_\mu.
\]

The centered response vector is

\[
\mathbf M_a^\circ(x)=f_\mu^\circ(ax).
\]

Define the multiplicative autocorrelation kernel

\[
\boxed{
C_\mu(g)
:=
\sum_{x\in G_p}
f_\mu^\circ(x)f_\mu^\circ(gx).
}
\]

## Theorem H15.100 — group-circulant Gram law

The centered Mahler response Gram matrix satisfies

\[
\boxed{
\langle\mathbf M_a^\circ,\mathbf M_b^\circ\rangle
=C_\mu(a^{-1}b).
}
\]

Hence the full Gram matrix is a `G_p`-circulant matrix.

Also

\[
\boxed{
\sum_{a\in G_p}\mathbf M_a^\circ=0.
}
\]

### Proof

The Gram identity follows by the same multiplicative change of variables as in H15.99. For the vector sum, each fixed coordinate sees every value of the centered base profile exactly once as `a` varies, and those values sum to zero. QED.

So the world/reaction orbit is automatically balanced around its barycenter.

---

## 4. Multiplicative Fourier diagonalization

The character group

\[
\widehat G_p
\]

is naturally the group of even Dirichlet characters modulo `p`:

\[
\chi(-1)=1.
\]

For `chi in \widehat G_p`, define the multiplicative Fourier coefficient

\[
\boxed{
\widehat f_\mu(\chi)
:=
\sum_{x\in G_p}
f_\mu^\circ(x)\overline{\chi(x)}.
}
\]

For the trivial character,

\[
\widehat f_\mu(1)=0.
\]

## Theorem H15.101 — exact Mahler Parseval spectrum

The character vectors diagonalize the centered response Gram matrix. Its eigenvalue in character channel `chi` is

\[
\boxed{
\Lambda_\chi
=|\widehat f_\mu(\chi)|^2.
}
\]

Consequently

\[
\boxed{
\operatorname{rank}G_{\rm Mahler}
=
\#\{\chi\in\widehat G_p:\widehat f_\mu(\chi)\ne0\}.
}
\]

The trivial channel has eigenvalue zero because of centering.

### Proof

Let `A` be the matrix with rows `M_a^circ`. Then

\[
A_{a,x}=f_\mu^\circ(ax).
\]

For a character vector `v_chi(x)=chi(x)`,

\[
(Av_\chi)(a)
=
\sum_x f_\mu^\circ(ax)\chi(x).
\]

Set `y=ax`. Then

\[
(Av_\chi)(a)
=\chi(a^{-1})
\sum_y f_\mu^\circ(y)\chi(y).
\]

Thus each multiplicative character is a singular direction of `A`, with singular value `|hat f_mu(chi)|`. Squaring gives the Gram eigenvalue. QED.

This is the exact continuous analogue of the earlier projective Gram/Parseval layer, but unlike the projective incidence transform the Mahler transform need not be isotropic: its nontrivial character eigenvalues can differ.

---

## Corollary H15.102 — exact energy decomposition

For every centered coefficient vector

\[
c=(c_a)_{a\in G_p},
\qquad
\sum_a c_a=0,
\]

one has the group-Fourier identity

\[
\boxed{
\left\|\sum_a c_a\mathbf M_a^\circ\right\|_2^2
=
\frac1m
\sum_{\chi\ne1}
|\widehat f_\mu(\chi)|^2
|\widehat c(\chi)|^2,
}
\]

with the unnormalized convention

\[
\widehat c(\chi)=\sum_a c_a\overline{\chi(a)}.
\]

Thus every even Dirichlet-character channel carries a precisely quantified amount of Mahler-response energy.

---

## 5. Linear tomography criterion

Although the nonlinear orbit map `a -> M_a` is already injective, one can ask the stronger linear question: can an arbitrary zero-sum signal on reaction space be reconstructed from Mahler response superpositions?

## Theorem H15.103 — exact linear invertibility criterion

The centered Mahler response operator is invertible on the zero-sum subspace iff

\[
\boxed{
\widehat f_\mu(\chi)\ne0
\quad\text{for every nontrivial even character }\chi\bmod p.
}
\]

When this holds, Fourier inversion gives the exact inverse mode by mode by division through `hat f_mu(chi)`.

Thus possible blind directions of the continuous Mahler tomography are not mysterious: they are exactly the nontrivial even Dirichlet characters at which the multiplicative Fourier coefficient of the primitive Mahler profile vanishes.

No nonvanishing claim for all `p` is made here.

---

## 6. Exact low-prime geometry

The first prime worlds have especially rigid response geometry.

### `p=3`

Here `m=1`. There is only one nonzero signless reaction class, so the orbit is a single point.

### `p=5`

Here `m=2`. After centering, the two response vectors are negatives of each other:

\[
\boxed{
\mathbf M_{a_2}^\circ=-\mathbf M_{a_1}^\circ.
}
\]

Thus the response orbit is an exact one-dimensional regular simplex.

### `p=7`

Here `m=3`. The three centered vectors:

- have equal norm by permutation symmetry;
- sum to zero;
- have equal pairwise inner products because the cyclic action is transitive on nonidentity differences.

Therefore they form an exact equilateral triangle in the two-dimensional zero-sum plane:

\[
\boxed{
\langle\mathbf M_a^\circ,\mathbf M_b^\circ\rangle
=-\frac12\|\mathbf M_a^\circ\|^2
\qquad(a\ne b).
}
\]

So the first nontrivial Mahler response worlds literally reproduce regular-simplex geometry without any tuning of the Mahler values.

For larger `p`, exact simplex geometry is no longer forced; the character spectrum `|hat f_mu(chi)|^2` measures its anisotropy.

---

## 7. Relation to the earlier projective world transform

H15 now contains two different exact world-response geometries.

### Coarse Frobenius/projective layer

The projective incidence transform had the rigid Gram law

\[
TT^*=p^rI-(p-1)J,
\]

so every nonconstant direction had the same eigenvalue. It is an exact tight frame / regular simplex geometry.

### Primitive Mahler layer

The new response Gram spectrum is

\[
\Lambda_\chi=|\widehat f_\mu(\chi)|^2.
\]

Thus its geometry is generally anisotropic and resolves the multiplicative character channels unequally.

This distinction is structurally important:

\[
\boxed{
\text{binary projective observer}
\to
\text{universal isotropic geometry},
}
\]

while

\[
\boxed{
\text{primitive Mahler observer}
\to
\text{arithmetic character-weighted geometry}.
}
\]

The second observer therefore contains a new continuous spectral fingerprint even though both reconstruct the signless object reaction.

---

## 8. What has and has not been proved

**Proved:**

\[
\boxed{
\text{object reaction }a
\to
\text{Mahler response vector }\mathbf M_a
}
\]

is an equivariant injective embedding of `G_p` into Euclidean response space with positive minimum distance; its centered Gram matrix is exactly diagonalized by even Dirichlet characters.

**Not proved:** all nontrivial Fourier coefficients `hat f_mu(chi)` are nonzero for every prime `p`. Therefore a general linear-tomography theorem is not yet claimed.

**Not claimed:** Shannon capacity, cryptographic coding, or physical information storage.

---

## 9. Next attack

There is now one sharp arithmetic obstruction:

\[
\boxed{
\widehat f_\mu(\chi)\stackrel{?}{\ne}0
\quad\text{for every nontrivial even Dirichlet character }\chi.
}
\]

A proof would upgrade the orbit code to a full linear tomography theorem on the zero-sum reaction space.

A counterexample would be equally informative: it would exhibit an explicit multiplicative arithmetic mode invisible even to the complete primitive Mahler response ensemble.

This is the next natural point at which the analytic Mahler theory, the multiplicative character theory, and the non-Abelian port architecture genuinely meet.
