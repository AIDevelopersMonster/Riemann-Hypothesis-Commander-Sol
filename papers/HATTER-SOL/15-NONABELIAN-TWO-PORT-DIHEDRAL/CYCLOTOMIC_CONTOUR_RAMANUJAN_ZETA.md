# HATTER-SOL-15 · Cyclotomic Contour Jump, Ramanujan Observer, and Zeta Factor

**Status:** exact theorem layer. Ramanujan sums, cyclotomic logarithmic derivatives, and their Dirichlet series are classical; H15 contributes the contour-observer interpretation inside the port/frequency architecture.

Let `p` be an odd prime and

\[
\zeta_p=e^{2\pi i/p},
\qquad
\Phi_p(z)=\frac{z^p-1}{z-1}=\prod_{a=1}^{p-1}(z-\zeta_p^a).
\]

Then

\[
\frac{\Phi_p'(z)}{\Phi_p(z)}
=\sum_{a=1}^{p-1}\frac1{z-\zeta_p^a}.
\]

For an integer `m>=1` and a radius `rho!=1`, define the contour response

\[
I_{p,m}(\rho)
:=\frac1{2\pi i}
\oint_{|z|=\rho}
z^m\frac{\Phi_p'(z)}{\Phi_p(z)}\,dz.
\]

## Theorem H15.49 — exact contour jump

For `0<rho<1`,

\[
\boxed{I_{p,m}(\rho)=0.}
\]

For `rho>1`,

\[
\boxed{
I_{p,m}(\rho)
=\sum_{a=1}^{p-1}\zeta_p^{am}
=c_p(m),
}
\]

where `c_p(m)` is the Ramanujan sum

\[
\boxed{
c_p(m)=
\begin{cases}
p-1,&p\mid m,\\
-1,&p\nmid m.
\end{cases}}
\]

### Proof

For `rho<1`, the contour encloses none of the zeros of `Phi_p`, so the integrand is holomorphic inside and the integral vanishes.

For `rho>1`, all nontrivial `p`-th roots of unity lie inside. Each is a simple pole of `Phi_p'/Phi_p` with residue `1`, so the residue theorem gives

\[
I_{p,m}=\sum_{a=1}^{p-1}(\zeta_p^a)^m.
\]

Adding the missing trivial root gives

\[
1+I_{p,m}
=\sum_{a=0}^{p-1}\zeta_p^{am}
=
\begin{cases}
p,&p\mid m,\\
0,&p\nmid m.
\end{cases}
\]

Hence the formula. QED.

Thus crossing the unit frequency circle produces a discontinuous observer jump

\[
\boxed{0\longrightarrow c_p(m).}
\]

The contour itself is singular at `rho=1`; the statement is about the inside and outside limits.

## Corollary H15.50 — full-root cancellation versus centered residue

Let

\[
J_{p,m}(\rho)
:=\frac1{2\pi i}\oint_{|z|=\rho}
z^m\frac{p z^{p-1}}{z^p-1}\,dz.
\]

For `rho>1`,

\[
\boxed{
J_{p,m}=\sum_{a=0}^{p-1}\zeta_p^{am}
=
\begin{cases}
p,&p\mid m,\\0,&p\nmid m.
\end{cases}}
\]

and

\[
\boxed{I_{p,m}=J_{p,m}-1.}
\]

Therefore for `p\nmid m` the complete root orbit cancels exactly to zero, while deleting the single trivial root leaves the residual value `-1`.

This is the precise complex-contour version of

\[
\boxed{\text{complete symmetry cancels; centered observation leaves a residual trace}.}
\]

## Corollary H15.51 — mirror-frequency form

Pairing complex-conjugate roots gives

\[
\boxed{
c_p(m)
=2\sum_{k=1}^{(p-1)/2}
\cos\frac{2\pi km}{p}.}
\]

Hence the Ramanujan contour jump is exactly the sum over the real mirror-frequency channels `k<->-k` from the H15 Floquet decomposition.

## Theorem H15.52 — the contour jump is the centered rotation character

Let `R` be the regular rotation on `F_p` and let

\[
V_0=\mathbb C[\mathbb F_p]\ominus\mathbf1
\]

be the augmentation representation. Then

\[
\boxed{
\operatorname{Tr}(R^m\mid V_0)=c_p(m).
}
\]

### Proof

The eigenvalues of `R` on the regular representation are all `p`-th roots `1,zeta_p,...,zeta_p^{p-1}`. Removing the invariant eigenline removes the eigenvalue `1`, so the trace on `V_0` is the sum of the nontrivial roots raised to the `m`-th power. QED.

Thus three previously separate H15 objects are literally the same function:

\[
\boxed{
\text{cyclotomic contour jump}
=
\text{Ramanujan sum}
=
\text{centered port character}.
}
\]

## Theorem H15.53 — exact Riemann-zeta generating function

For `Re(s)>1`,

\[
\boxed{
\mathcal C_p(s)
:=\sum_{m=1}^\infty\frac{I_{p,m}(\rho>1)}{m^s}
=\sum_{m=1}^\infty\frac{c_p(m)}{m^s}
=(p^{1-s}-1)\zeta(s).
}
\]

### Proof

Using `c_p(m)=p 1_{p|m}-1`,

\[
\sum_{m\ge1}\frac{c_p(m)}{m^s}
=p\sum_{p|m}\frac1{m^s}-\sum_{m\ge1}\frac1{m^s}
=p^{1-s}\zeta(s)-\zeta(s).
\]

QED.

The pole of `zeta(s)` at `s=1` is canceled by the zero of `p^{1-s}-1`, so `C_p(s)` extends holomorphically through `s=1` with

\[
\boxed{\mathcal C_p(1)=-\log p.}
\]

## Corollary H15.54 — zero set and RH reformulation

The factor

\[
p^{1-s}-1
\]

has the explicit zeros

\[
\boxed{
s=1-\frac{2\pi i k}{\log p},
\qquad k\in\mathbb Z\setminus\{0\},
}
\]

after the `k=0` zero is canceled by the pole of `zeta` at `1`.

Apart from those explicit zeros and the trivial zeros inherited from `zeta`, the remaining zeros of `C_p` in the critical strip are exactly the nontrivial zeros of `zeta`.

Therefore RH is equivalent to the statement that every non-explicit zero of `C_p(s)` in `0<Re(s)<1` lies on

\[
\boxed{Re(s)=1/2.}
\]

This is a classical reformulation, not a proof of RH.

## Claim discipline

Ramanujan sums and the Dirichlet-series identity are classical. The H15 contribution is to identify the same arithmetic function simultaneously as:

1. a residue jump across the complete cyclotomic frequency contour;
2. the centered trace of the rotation port;
3. the sum of all mirror-frequency channels;
4. a Dirichlet series carrying the Riemann-zeta zero set up to an explicit factor.