# HATTER-SOL-15 · Non-Abelian Floquet Pairing

**Status:** exact theorem layer. Bloch/Floquet analysis for periodic matrix-valued operators is classical; H15 contributes the explicit dihedral two-port specialization and its observer interpretation.

Let `p` be an odd prime and let

\[
R(i)=i+1,
\qquad
S(i)=-i
\]

act on the fibre `C^{F_p}`. Let

\[
\omega=e^{2\pi i/p}.
\]

Consider the square-lattice connection Laplacian symbol

\[
\boxed{
L(z,w)=4I-
\left(zR+z^{-1}R^{-1}+wS+w^{-1}S^{-1}\right),
}
\]

with `z,w in C*`. Since `S^{-1}=S`, this is

\[
L(z,w)=4I-zR-z^{-1}R^{-1}-(w+w^{-1})S.
\]

On the unit Bloch torus write

\[
z=e^{i\theta},
\qquad
w=e^{i\phi}.
\]

## Theorem H15.41 — exact Fourier pairing

Let `e_k`, `k in F_p`, be the Fourier basis for the rotation port:

\[
R e_k=\omega^k e_k.
\]

Then

\[
\boxed{S e_k=e_{-k}.}
\]

Hence the fibre decomposes as

\[
\mathbb C^{F_p}
=
\langle e_0\rangle
\oplus
\bigoplus_{k=1}^{(p-1)/2}
\langle e_k,e_{-k}\rangle.
\]

Thus the non-Abelian reflection port does not destroy Fourier analysis: it couples each frequency `k` exactly to its mirror `-k`.

### Proof

For `j in F_p`, take

\[
e_k(j)=p^{-1/2}\omega^{kj}.
\]

Then

\[
(S e_k)(j)=e_k(-j)=p^{-1/2}\omega^{-kj}=e_{-k}(j).
\]

QED.

## Theorem H15.42 — exact 2x2 Bloch blocks

The `k=0` channel is scalar:

\[
\boxed{
\lambda_0(\theta,\phi)
=4-2\cos\theta-2\cos\phi.
}
\]

For `1<=k<=(p-1)/2`, put

\[
\alpha_k=\frac{2\pi k}{p}.
\]

On `span(e_k,e_{-k})`, the symbol is

\[
\boxed{
L_k(\theta,\phi)
=
\begin{pmatrix}
4-2\cos(\theta+\alpha_k) & -2\cos\phi\\
-2\cos\phi & 4-2\cos(\theta-\alpha_k)
\end{pmatrix}.
}
\]

Therefore the two dispersion branches are

\[
\boxed{
\lambda_{k,\pm}(\theta,\phi)
=4-2\cos\theta\cos\alpha_k
\pm
2\sqrt{\sin^2\theta\sin^2\alpha_k+\cos^2\phi}.
}
\]

### Proof

`R` is diagonal in the Fourier basis while `S` swaps `k` and `-k`. This gives the block matrix directly. The displayed eigenvalues are the two eigenvalues of the real-symmetric 2x2 block. QED.

## Interpretation as an amplitude-frequency characteristic

For commuting scalar ports, each Fourier mode propagates independently. For the dihedral pair, the reflection port creates exact mode mixing

\[
\boxed{k\leftrightarrow-k.}
\]

Thus a spectral observer sees non-Abelian path structure as mirror-frequency coupling rather than as a loss of harmonic structure.

The quantity

\[
\sin^2\theta\sin^2\alpha_k+\cos^2\phi
\]

controls the splitting between the two branches. It vanishes only at special Bloch points, so the non-Abelian coupling is spectrally visible on a large set of frequencies.

## Complex-variable form

The spectral curve is the Laurent-polynomial equation

\[
\boxed{
P_k(z,w,\lambda)
:=\det(L_k(z,w)-\lambda I)=0,
}
\]

where

\[
L_k(z,w)=
\begin{pmatrix}
4-z\omega^k-z^{-1}\omega^{-k} & -(w+w^{-1})\\
-(w+w^{-1}) & 4-z\omega^{-k}-z^{-1}\omega^k
\end{pmatrix}.
\]

Thus each mirror-frequency pair defines an algebraic curve in `(C*)^2 x C`. The unit torus `|z|=|w|=1` is only the physical/Fourier slice of this complex spectral variety.

## Claim boundary

This symbol describes a periodic square-lattice operator with internal permutation-valued link variables. When `R` and `S` do not commute, it should not be interpreted as a flat vector bundle on the closed torus. Its elementary plaquette has nontrivial holonomy `[R,S]=R^2`; equivalently it is a non-flat connection / magnetic-type lattice operator.

The matrix-valued Bloch formalism and connection Laplacians are classical. H15 does not claim their invention.