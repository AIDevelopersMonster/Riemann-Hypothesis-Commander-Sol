# HATTER-SOL-15 · Local Euler-Factor Trichotomy

Let `L/Q`, `G=D_{2p}`, `D=<s>`, and `K=L^D` be as in the H15 dihedral setup, with `p` odd prime and `[K:Q]=p`.

Let `q` be a rational prime unramified in `L`.

## Theorem H15.11 — three Schreier splitting types

The permutation of the `p` sectors `D\G` induced by Frobenius has exactly one of the following cycle types.

### Type I — identity Frobenius

If `Frob_q=1`, the cycle type is

\[
\boxed{1^p}.
\]

Thus `q` splits completely in `K` into `p` degree-one prime factors.

### Type R — nontrivial rotation

If `Frob_q=r^a`, `a != 0`, then because `p` is prime the translation

\[
i\mapsto i+a
\]

is a single `p`-cycle. Hence the cycle type is

\[
\boxed{p}.
\]

Thus `q` is inert in the degree-`p` field `K`.

### Type S — reflection

If `Frob_q` is a reflection, its action is

\[
i\mapsto-i+b
\]

and has one fixed point and `(p-1)/2` transpositions. Hence the cycle type is

\[
\boxed{1\,2^{(p-1)/2}}.
\]

Thus the residue-degree pattern is `1,2,...,2`.

These are the only possibilities.

## Corollary H15.12 — local Euler factors from port sectors

The local Euler factor of the Dedekind zeta function `zeta_K(s)` is determined directly by the Schreier orbit lengths.

For `T=q^{-s}`:

\[
\boxed{
Z_q(T)=
\begin{cases}
(1-T)^{-p},&\text{identity type},\\
(1-T^p)^{-1},&\text{rotation type},\\
(1-T)^{-1}(1-T^2)^{-(p-1)/2},&\text{reflection type}.
\end{cases}}
\]

Thus the local `port/factor state` is literally a local Euler factor of an arithmetic zeta function.

## Corollary H15.13 — Chebotarev densities of the three coarse port states

In `D_{2p}`:

- the identity class has size `1`;
- the union of nonidentity rotations has size `p-1`;
- the reflection class has size `p`.

Therefore Chebotarev gives coarse densities

\[
\boxed{
\delta_I=\frac1{2p},\qquad
\delta_R=\frac{p-1}{2p},\qquad
\delta_S=\frac12.
}
\]

The rotation union consists of several conjugacy classes, but every nontrivial rotation has the same cycle type on the degree-`p` sector space.

## Structural interpretation

At this level a port is exactly a local factorization branch. The network state of a prime is not an externally attached label: it is the Frobenius action on the decomposition sectors, equivalently the multiset of residue degrees, equivalently the local Euler factor.

Hence H15 obtains the exact chain

\[
\boxed{
\text{two-port word action}
\to
\text{Schreier orbit structure}
\to
\text{prime splitting type}
\to
\text{local Euler factor}.
}
\]

This is the cleanest current bridge from the HATTER port abstraction back to classical analytic number theory.