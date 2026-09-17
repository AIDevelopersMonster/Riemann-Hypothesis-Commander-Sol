# HATTER-SOL-15 · Centered Observer and Relative Zeta Signal

**Status:** exact analytic bridge; Artin formalism is classical, the HATTER observer interpretation is the programme contribution.

Let `K/Q` be the degree-`p` dihedral side field and let

\[
X=G/D
\]

be the `p`-sector permutation set. Its complex permutation representation decomposes as

\[
\mathbb C[X]=\mathbf 1\oplus V_0,
\]

where `V_0` is the augmentation representation of dimension `p-1`.

For an unramified rational prime `q`, define

\[
O_m(q)=\operatorname{Tr}(F_q^m\mid\mathbb C[X])
      =\#\operatorname{Fix}(F_q^m\mid X),
\]

and the centered response

\[
\boxed{\widetilde O_m(q):=O_m(q)-1
=\operatorname{Tr}(F_q^m\mid V_0).}
\]

## Theorem H15.22 — relative Artin factor

Artin formalism gives

\[
\boxed{L(s,V_0)=\frac{\zeta_K(s)}{\zeta(s)}.}
\]

### Proof

The permutation representation is `Ind_D^G 1`, whose Artin L-function is `zeta_K(s)`. The trivial summand has Artin L-function `zeta(s)`. Multiplicativity under direct sums gives the quotient formula. QED.

For dihedral `D_{2p}`, the augmentation representation splits over `C` into the `(p-1)/2` two-dimensional irreducible dihedral representations, so

\[
\frac{\zeta_K(s)}{\zeta(s)}
=\prod_{j=1}^{(p-1)/2}L(s,\rho_j).
\]

These `rho_j` are monomial/dihedral representations induced from characters of the cyclic index-two subgroup; their Artin L-functions are Hecke L-functions after induction from the quadratic field.

## Theorem H15.23 — exact centered character table

For the degree-`p` permutation action:

\[
\widetilde\chi(g)=
\begin{cases}
p-1,&g=1,\\
-1,&g\text{ a nonidentity rotation},\\
0,&g\text{ a reflection}.
\end{cases}
\]

### Proof

The full permutation character counts fixed sectors. The identity fixes `p` sectors, a nonidentity rotation fixes none, and a reflection fixes exactly one. Subtract the trivial character `1`. QED.

Thus the centered observer completely suppresses first-order reflection response:

\[
\boxed{\widetilde\chi(\text{reflection})=0.}
\]

This does not mean reflection primes are invisible at all powers: even powers of a reflection equal the identity.

## Corollary H15.24 — three relative local Euler factors

Put `T=q^{-s}`. For the three unramified Frobenius types:

### Identity

\[
\boxed{Z_q^{rel}(T)=(1-T)^{-(p-1)}.}
\]

### Nonidentity rotation

\[
\boxed{Z_q^{rel}(T)=\frac{1-T}{1-T^p}.}
\]

### Reflection

\[
\boxed{Z_q^{rel}(T)=(1-T^2)^{-(p-1)/2}.}
\]

These are exactly the local factors of `zeta_K/zeta`.

## Theorem H15.25 — centered global observer signal

Define

\[
\widetilde\Psi_X(x)
:=\sum_{q^m\le x}\widetilde O_m(q)\log q,
\]

with the standard inertia-corrected coefficients at ramified primes. Then

\[
\boxed{\widetilde\Psi_X(x)=\psi_K(x)-\psi(x).}
\]

### Proof

Subtract the logarithmic derivatives:

\[
-\frac{d}{ds}\log\frac{\zeta_K(s)}{\zeta(s)}
=
-\frac{\zeta_K'}{\zeta_K}(s)
+\frac{\zeta'}{\zeta}(s),
\]

and compare Dirichlet coefficients using H15.18. QED.

The `x` main terms cancel. Therefore the centered signal is a pure relative fluctuation signal rather than a prime-density signal with a leading term.

## Theorem H15.26 — relative GRH criterion

If for every `epsilon>0`,

\[
\boxed{\widetilde\Psi_X(x)=O_\epsilon(x^{1/2+\epsilon}),}
\]

then every nontrivial zero of the relative Artin/Hecke factor

\[
L(s,V_0)=\zeta_K(s)/\zeta(s)
\]

lies on `Re(s)=1/2`.

Conversely, GRH for these monomial Artin/Hecke factors yields square-root-scale bounds with the usual conductor/logarithmic losses.

This is the standard explicit-formula equivalence applied to the relative factor.

## 6. Exact relation to the Riemann hypothesis

The centered observer deliberately removes the trivial representation and therefore removes the Riemann zeta factor:

\[
\boxed{\zeta_K=\zeta\cdot L(s,V_0).}
\]

Consequently:

- controlling the centered signal can address the **relative/nontrivial dihedral factors**;
- it does **not by itself prove RH for `zeta(s)`**, because that factor has been divided out;
- controlling the uncentered field signal `Psi_X(x)-x` at square-root scale would imply GRH for `zeta_K`, and in the dihedral monomial case this includes the Riemann factor as one component.

Safe programme statement:

\[
\boxed{\text{RH-scale analysis naturally splits into universal background }\zeta(s)\text{ and world-relative signal }\zeta_K(s)/\zeta(s).}
\]

This separation may be useful even if it does not make either factor easier.

## 7. Fixed prime 2 after centering

For a reflection-state fixed prime `2`,

\[
\widetilde O_m(2)=
\begin{cases}
0,&m\text{ odd},\\
p-1,&m\text{ even}.
\end{cases}
\]

Thus the local relative factor is

\[
\boxed{Z_{2}^{rel}(T)=(1-T^2)^{-(p-1)/2}.}
\]

The fixed prime `2` remains a canonical local anchor, but its centered global contribution is still only `O(p log x)`, so global zero control necessarily requires infinitely many primes.