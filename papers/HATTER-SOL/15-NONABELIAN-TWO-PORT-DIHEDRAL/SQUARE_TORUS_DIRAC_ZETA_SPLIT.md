# HATTER-SOL-15 · Square-Torus Laplacian / Twisted-Dirac Zeta Split

**Status:** exact classical bridge, useful as an observer architecture; not a new RH criterion.

This note records a precise spectral separation of the Riemann zeta factor from the square-torus spectral zeta function using a second, orientation-sensitive spectral observer.

## 1. Square torus Laplacian

Take the flat square torus

\[
T^2=\mathbb R^2/\mathbb Z^2
\]

with the standard metric. Its nonzero Laplace eigenvalues are

\[
\lambda_{m,n}=4\pi^2(m^2+n^2),
\qquad
(m,n)\in\mathbb Z^2\setminus\{(0,0)\}.
\]

Therefore its spectral zeta function is

\[
Z_{T^2}(s)
:=
\sum_{(m,n)\ne(0,0)}\lambda_{m,n}^{-s}
=(4\pi^2)^{-s}
\sum_{(m,n)\ne(0,0)}(m^2+n^2)^{-s}.
\]

For `Re(s)>1`, the classical square-lattice Epstein identity is

\[
\sum_{(m,n)\ne(0,0)}(m^2+n^2)^{-s}
=4\zeta(s)\beta(s),
\]

where

\[
\beta(s)=L(s,\chi_{-4})
\]

is the Dirichlet beta function. Hence

\[
\boxed{
Z_{T^2}(s)
=4(4\pi^2)^{-s}\zeta(s)\beta(s).
}
\]

Equivalently, up to the explicit archimedean scaling factor, the square-torus Laplacian sees the Dedekind zeta function of the Gaussian field `Q(i)`:

\[
\zeta_{\mathbb Q(i)}(s)=\zeta(s)\beta(s).
\]

## 2. Quarter-holonomy Dirac observer on the circle

Let

\[
D_a=-i\frac{d}{dx}
\]

act on sections of the unit circle with holonomy

\[
f(x+2\pi)=e^{2\pi i a}f(x),
\qquad
0<a<1.
\]

Its spectrum is

\[
\operatorname{spec}(D_a)=\{n+a:n\in\mathbb Z\}.
\]

The corresponding eta function is

\[
\eta_a(s)
:=
\sum_{n\in\mathbb Z}
\operatorname{sgn}(n+a)|n+a|^{-s}.
\]

For `Re(s)>1`, splitting positive and negative eigenvalues gives

\[
\boxed{
\eta_a(s)=\zeta(s,a)-\zeta(s,1-a).
}
\]

For the quarter-holonomy value

\[
a=\frac14,
\]

we obtain

\[
\eta_{1/4}(s)
=
\zeta\left(s,\frac14\right)
-
\zeta\left(s,\frac34\right).
\]

The standard Hurwitz-zeta expression for the Dirichlet beta function is

\[
\beta(s)
=4^{-s}
\left[
\zeta\left(s,\frac14\right)
-
\zeta\left(s,\frac34\right)
\right].
\]

Therefore

\[
\boxed{
\eta_{1/4}(s)=4^s\beta(s).
}
\]

Thus the orientation-sensitive Dirac eta observer isolates exactly the `\chi_{-4}` factor which is entangled with `\zeta(s)` in the orientation-blind square-torus Laplacian zeta.

## Theorem H15.49 — exact two-observer factor separation

The square-torus Laplacian zeta and quarter-holonomy Dirac eta satisfy the meromorphic identity

\[
\boxed{
Z_{T^2}(s)
=4(16\pi^2)^{-s}\zeta(s)\eta_{1/4}(s).
}
\]

Equivalently,

\[
\boxed{
\zeta(s)\eta_{1/4}(s)
=\frac{(16\pi^2)^s}{4}Z_{T^2}(s).
}
\]

Where division is legitimate after analytic continuation and cancellation of common zeros,

\[
\boxed{
\zeta(s)
=\frac{(16\pi^2)^s}{4}
\frac{Z_{T^2}(s)}{\eta_{1/4}(s)}.
}
\]

The product identity is the safer global formulation because it does not require discussing quotient values at zeros of `\beta(s)`.

## 3. Observer interpretation

The two spectral observers retain different information:

1. **Laplacian observer** — sees squared frequency magnitude and therefore the norm form

\[
m^2+n^2;
\]

2. **Dirac eta observer** — retains frequency orientation/sign and quarter-holonomy phase.

The first observer produces the product

\[
\zeta(s)\beta(s),
\]

while the second produces

\[
\beta(s).
\]

Hence their combination isolates

\[
\zeta(s).
\]

Safe conceptual statement:

\[
\boxed{
\text{Riemann zeta can be isolated by combining an orientation-blind square-torus spectral observer with an orientation-sensitive quarter-holonomy Dirac observer.}
}
\]

This is a factorization identity, not a proof of RH.

## 4. Relation to H15 port architecture

This fits the earlier observer ladder:

\[
\text{metric / Laplacian data}
<
\text{oriented / signed data}.
\]

The Laplacian forgets orientation and sees a product of arithmetic channels. The eta observer restores a signed channel and separates the `\chi_{-4}` contribution.

The natural H15 research question is now:

\[
\boxed{
\text{Can analogous signed/twisted observers separate the real-cyclotomic Dirichlet/Artin factors arising from the dihedral port determinant?}
}
\]

For the real cyclotomic field `F_p=Q(\zeta_p+\zeta_p^{-1})`, the relevant one-dimensional arithmetic channels are the even Dirichlet characters modulo `p`. A successful geometric realization would amount to a spectral projector onto those character channels.

## 5. RH boundary

The identity above puts the nontrivial zeros of `\zeta(s)` inside a geometric spectral-zeta factorization, but it does **not** constrain their real parts. Both `Z_{T^2}` and `\eta_{1/4}` are already built from classical zeta/L-functions.

To obtain genuinely new RH content, H15 would need an independent spectral or geometric theorem forcing a property of

\[
\frac{Z_{T^2}(s)}{\eta_{1/4}(s)}
\]

that is not merely a reformulation of known properties of `\zeta(s)`.

The strongest safe conclusion at present is architectural, not solution-level:

\[
\boxed{
\text{surface symmetry + observer choice can separate arithmetic L-channels.}
}
\]

That principle is now exact in the Gaussian/square-torus case and is the template for the dihedral/cyclotomic case.