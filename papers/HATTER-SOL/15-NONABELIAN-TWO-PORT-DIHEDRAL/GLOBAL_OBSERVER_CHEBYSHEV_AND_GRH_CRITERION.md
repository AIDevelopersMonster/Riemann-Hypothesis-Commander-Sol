# HATTER-SOL-15 · Global Observer-Chebyshev Signal and GRH Criterion

**Status:** exact bridge theorem; analytic number-theory machinery is classical, H15 contribution is the observer interpretation.

Let `K/Q` be the degree-`p` dihedral side field with Galois closure `L/Q`, and let

\[
\rho_X:G\to\operatorname{GL}(\mathbb C[X])
\]

be the permutation representation on the `p` arithmetic sectors.

For an unramified rational prime `q`, let `F_q` be a Frobenius element and define the `m`-th observer response

\[
O_m(q):=\operatorname{Tr}(\rho_X(F_q)^m)
      =\#\operatorname{Fix}(F_q^m\mid X).
\]

For ramified `q`, replace the permutation space by the inertia-invariant local Artin space so that the standard Artin local factor is used. The unramified formulas below are the geometric sector interpretation.

## Theorem H15.17 — logarithmic Euler reconstruction

For `Re(s)>1`,

\[
\boxed{
\log\zeta_K(s)
=
\sum_q\sum_{m\ge1}
\frac{O_m(q)}{m q^{ms}}
}
\]

with the understood inertia correction at the finitely many ramified primes.

Equivalently,

\[
\boxed{
-\frac{\zeta_K'}{\zeta_K}(s)
=
\sum_q\sum_{m\ge1}
\frac{O_m(q)\log q}{q^{ms}}.
}
\]

### Proof

For an unramified prime `q`, the local factor is

\[
\det(1-\rho_X(F_q)q^{-s})^{-1}.
\]

Using

\[
-\log\det(1-A T)
=
\sum_{m\ge1}\frac{\operatorname{Tr}(A^m)}mT^m
\]

gives the first formula prime by prime. Differentiation gives the second. QED.

## Theorem H15.18 — the global observer signal is the field Chebyshev function

Define

\[
\Psi_X(x)
:=
\sum_{q^m\le x}O_m(q)\log q,
\]

again with the standard inertia-corrected local coefficient at ramified primes.

Then

\[
\boxed{\Psi_X(x)=\psi_K(x),}
\]

where

\[
\psi_K(x)=\sum_{N\mathfrak a\le x}\Lambda_K(\mathfrak a)
\]

is the Chebyshev function of the number field `K`.

### Proof

If

\[
q\mathcal O_K=\prod_i\mathfrak q_i
\]

is unramified with residue degrees `f_i`, then `F_q` acts on the sector set with cycle lengths `f_i`. Hence

\[
O_m(q)=\sum_{f_i\mid m}f_i.
\]

At `m=r f_i`, the contribution `f_i log q` is exactly

\[
\log N\mathfrak q_i,
\]

the von Mangoldt weight of the prime-ideal power `\mathfrak q_i^r`. Summing over `q,m` gives `psi_K`. QED.

Thus the H15 observer signal is not merely analogous to the prime-ideal counting signal: it is exactly that signal.

## Corollary H15.19 — GRH implies square-root observer fluctuation

Under GRH for `zeta_K`, classical explicit prime-ideal theorems give a bound of square-root scale

\[
\Psi_X(x)
=
x+O\!\left(\sqrt{x}\,\operatorname{polylog}(D_K,x,[K:\mathbb Q])\right).
\]

More explicit versions are available in the literature; H15 uses only the scale.

## Theorem H15.20 — observer criterion for GRH

Assume that for every `epsilon>0`,

\[
\boxed{
\Psi_X(x)=x+O_\epsilon(x^{1/2+\epsilon}).
}
\]

Then every nontrivial zero of `zeta_K(s)` lies on

\[
\boxed{\operatorname{Re}s=1/2.}
\]

Hence this observer estimate implies GRH for `zeta_K`.

### Proof

For `Re(s)>1`, partial summation gives

\[
-\frac{\zeta_K'}{\zeta_K}(s)
=
s\int_1^\infty \Psi_X(x)x^{-s-1}\,dx.
\]

Write

\[
\Psi_X(x)=x+E(x).
\]

The main term gives the pole at `s=1`. The hypothesis

\[
E(x)=O_\epsilon(x^{1/2+\epsilon})
\]

for every `epsilon>0` makes the remaining integral analytic in every half-plane

\[
\operatorname{Re}s>1/2+\epsilon.
\]

Therefore `zeta_K` has no nontrivial zeros with real part greater than `1/2`. The functional equation reflects nontrivial zeros across `Re(s)=1/2`, so none can lie strictly to the left either. QED.

This is a classical prime-ideal/RH criterion rewritten exactly in observer language. It is not claimed as a new RH criterion.

## Theorem H15.21 — one fixed prime is analytically too small

Suppose the fixed prime `2` has reflection state in the degree-`p` dihedral field. Then

\[
O_m(2)=
\begin{cases}
1,&m\text{ odd},\\
p,&m\text{ even}.
\end{cases}
\]

Let `M=floor(log_2 x)`. Its entire contribution to `Psi_X(x)` is

\[
\Psi_{X,2}(x)
=
\log2\left(\left\lceil\frac M2\right\rceil
+p\left\lfloor\frac M2\right\rfloor\right).
\]

Hence

\[
\boxed{\Psi_{X,2}(x)=O(p\log x).}
\]

Therefore the fixed prime `2` can be a structural anchor, synchronizer, and local diagnostic carrier, but it cannot by itself produce the `x`-scale global signal whose fluctuation controls zero locations.

## Programme consequence

Any genuinely RH/GRH-relevant HATTER mechanism must couple observer responses across infinitely many rational primes. A theorem involving only the branch geometry of the single prime `2` is necessarily local and analytically lower-order.

Safe statement:

\[
\boxed{\text{local anchor at }2\;\neq\;\text{global zero-control mechanism}.}
\]