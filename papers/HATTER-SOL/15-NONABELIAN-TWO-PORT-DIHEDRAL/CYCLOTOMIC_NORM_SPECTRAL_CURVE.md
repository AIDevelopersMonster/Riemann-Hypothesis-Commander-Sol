# HATTER-SOL-15 · Cyclotomic Norm Spectral Curve

**Status:** exact theorem layer. Cyclotomic fields, Chebyshev identities, and field norms are classical; H15 contributes the identification of the dihedral port Floquet determinant with a real-cyclotomic norm.

Let `p` be an odd prime, put

\[
m=\frac{p-1}{2},
\qquad
\omega=e^{2\pi i/p},
\qquad
\vartheta=\omega+\omega^{-1}=2\cos\frac{2\pi}{p},
\]

and let

\[
F_p=\mathbb Q(\vartheta)=\mathbb Q(\zeta_p+\zeta_p^{-1})
\]

be the maximal real subfield of the `p`-th cyclotomic field. Its degree is `m`.

Continue with the H15 square-lattice connection Laplacian

\[
L(z,w)=4I-zR-z^{-1}R^{-1}-(w+w^{-1})S.
\]

Set

\[
X=z+z^{-1},
\qquad
Y=w+w^{-1},
\qquad
\mu=4-\lambda.
\]

For the mirror-frequency pair indexed by `k`, put

\[
\vartheta_k=\omega^k+\omega^{-k}=2\cos\frac{2\pi k}{p}.
\]

The `2x2` block determinant is

\[
D_k(\mu;X,Y)
=
\det(L_k-\lambda I)
=
\mu^2-\mu X\vartheta_k+X^2+\vartheta_k^2-Y^2-4.
\]

## Theorem H15.45 — Chebyshev minimal polynomial of the frequency orbit

Define

\[
Q_p(u)
:=
\prod_{k=1}^{m}(u-\vartheta_k).
\]

Then

\[
\boxed{
Q_p(u)
=U_m(u/2)+U_{m-1}(u/2),
}
\]

where `U_j` is the Chebyshev polynomial of the second kind.

Equivalently,

\[
\boxed{
Q_p(u)^2
=\frac{2(T_p(u/2)-1)}{u-2},
}
\]

where `T_p` is the Chebyshev polynomial of the first kind.

For prime `p`, `Q_p` is the minimal polynomial of `vartheta` over `Q`.

### Proof

The roots of `T_p(u/2)-1` are

\[
u=2\cos\frac{2\pi j}{p},
\qquad j=0,\ldots,p-1.
\]

The root `u=2` occurs once, while every nontrivial cosine value occurs twice because `j` and `-j` give the same value. Hence

\[
2(T_p(u/2)-1)
=(u-2)Q_p(u)^2.
\]

For `p=2m+1`, the standard identity

\[
\frac{T_{2m+1}(x)-1}{x-1}
=(U_m(x)+U_{m-1}(x))^2
\]

gives the displayed formula. The numbers `vartheta_k`, `1<=k<=m`, are exactly the real Galois conjugates of `vartheta`, and `[F_p:Q]=m`, so this polynomial is minimal. QED.

## Theorem H15.46 — full dihedral determinant is a cyclotomic norm

The scalar `k=0` channel contributes

\[
\mu-X-Y.
\]

The product of all nontrivial mirror-frequency blocks is

\[
\boxed{
\prod_{k=1}^{m}D_k(\mu;X,Y)
=
N_{F_p/\mathbb Q}
\left(
\vartheta^2-\mu X\vartheta+\mu^2+X^2-Y^2-4
\right).
}
\]

Consequently the complete `p`-dimensional characteristic polynomial is

\[
\boxed{
\det(L(z,w)-\lambda I)
=(\mu-X-Y)
N_{F_p/\mathbb Q}
\left(
\vartheta^2-\mu X\vartheta+\mu^2+X^2-Y^2-4
\right).
}
\]

### Proof

Every embedding

\[
\sigma_k:F_p\hookrightarrow\mathbb R
\]

sends

\[
\vartheta\mapsto\vartheta_k.
\]

Applying all `m` embeddings to the element inside the norm gives exactly the `m` factors `D_k`. Multiplying them is the field norm. The invariant channel `e_0` contributes the remaining scalar factor. QED.

## Corollary H15.47 — resultant form of the spectral curve

The nontrivial determinant is also

\[
\boxed{
\operatorname{Res}_u
\left(
Q_p(u),
\,u^2-\mu Xu+\mu^2+X^2-Y^2-4
\right).
}
\]

Thus the complex Bloch spectral variety is defined over `Z` even though the individual mirror-frequency sheets live over the real cyclotomic field.

This gives an exact algebraic meaning to `frequency pairing -> rational observable`: the observer multiplies over the Galois orbit.

## Corollary H15.48 — arithmetic ramification of the frequency coordinates

For prime conductor `p`,

\[
\mathcal O_{F_p}=\mathbb Z[\vartheta]
\]

and

\[
\boxed{\operatorname{disc}(F_p)=p^{(p-3)/2}.}
\]

Hence the real frequency embeddings are arithmetically separable modulo every rational prime `ell != p`; the only rational prime that can ramify in the cyclotomic frequency field is `p`.

This statement concerns arithmetic reduction of the channel coordinates, not collisions of real Bloch eigenvalues.

## Galois action on frequency channels

The Galois group is

\[
\operatorname{Gal}(F_p/\mathbb Q)
\cong
(\mathbb Z/p\mathbb Z)^\times/\{\pm1\}.
\]

It acts on mirror-frequency labels by

\[
[k]\mapsto[ak].
\]

Thus the `k <-> -k` pairing found by the Floquet observer is exactly the quotient that produces the maximal real cyclotomic field.

Safe synthesis:

\[
\boxed{
\text{dihedral mirror-frequency channels}
=
\text{real cyclotomic embeddings},
\qquad
\text{spectral determinant}
=
\text{cyclotomic norm}.
}
\]

## Number-theory boundary

The same Galois group is Fourier-dual to the even Dirichlet characters modulo `p`, and the Dedekind zeta function of `F_p` factors through the corresponding Dirichlet `L`-functions. This gives a genuine common arithmetic symmetry between the Floquet channels and cyclotomic `L`-functions.

However, the zeros in the Bloch spectral variable `lambda` are **not** thereby identified with zeros of those Dirichlet `L`-functions in the complex variable `s`. Any such identification would require an additional trace/transfer theorem not proved here.