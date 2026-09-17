# HATTER-SOL-15 · Double Fourier Ladder and Even Dirichlet Channels

**Status:** exact representation-theoretic layer. Fourier decomposition of finite abelian groups and Dirichlet-character Artin factors are classical; H15 contributes the two-stage port/frequency interpretation.

Let `p` be an odd prime and let

\[
R(i)=i+1,
\qquad
S(i)=-i
\]

on `F_p`.

The additive Fourier transform diagonalizes `R`:

\[
R e_k=\omega^k e_k,
\qquad
\omega=e^{2\pi i/p},
\]

while

\[
S e_k=e_{-k}.
\]

Hence the nonzero frequencies are naturally grouped into mirror classes

\[
[k]=\{k,-k\}.
\]

Let

\[
G_p:=(\mathbb Z/p\mathbb Z)^\times/\{\pm1\}.
\]

Then the set of nonzero mirror classes is canonically a torsor for `G_p`.

## Theorem H15.50 — automorphism action on mirror-frequency channels

For every

\[
a\in(\mathbb Z/p\mathbb Z)^\times,
\]

the assignment

\[
R\mapsto R^a,
\qquad
S\mapsto S
\]

extends to an automorphism of the dihedral group `D_{2p}`. On mirror-frequency channels it acts by

\[
\boxed{[k]\mapsto[ak].}
\]

The action factors through `G_p`, and is free and transitive on the `(p-1)/2` nonzero mirror-frequency channels.

### Proof

Since `S R S^{-1}=R^{-1}`, replacing `R` by `R^a` preserves

\[
S R^a S^{-1}=R^{-a}=(R^a)^{-1}.
\]

In the additive Fourier basis, `R^a` has eigenvalue `omega^{ak}` on `e_k`, so the frequency label is multiplied by `a`. Quotienting by the reflection identification `k~-k` makes the action factor through `a~-a`. Since every nonzero mirror class is `[a]` applied to `[1]`, and the stabilizer modulo sign is trivial, the action is regular. QED.

## Theorem H15.51 — multiplicative Fourier projectors

Let

\[
\mathcal H_{mir}=\mathbb C[G_p]
\]

be the channel space. For `a in G_p`, let `U_a` be the permutation operator

\[
U_a\delta_{[k]}=\delta_{[ak]}.
\]

The character group of `G_p` is naturally the set of even Dirichlet characters modulo `p`:

\[
\boxed{
\widehat{G_p}
=\{\chi\bmod p:\chi(-1)=1\}.
}
\]

For each such character define

\[
\boxed{
P_\chi
=\frac1{|G_p|}
\sum_{a\in G_p}\overline{\chi(a)}U_a.
}
\]

Then:

1. `P_chi` is a rank-one orthogonal projector;
2. `P_chi P_psi=0` for `chi!=psi`;
3. `sum_chi P_chi=I`;
4. `U_a P_chi=chi(a)P_chi`.

Thus the multiplicative Fourier transform of the mirror-channel orbit diagonalizes the automorphism-permutation action into even Dirichlet-character channels.

### Proof

This is the standard character orthogonality decomposition of the regular representation of the finite abelian group `G_p`. QED.

## 3. Double Fourier ladder

The H15 two-port system therefore carries two distinct Fourier transforms:

### Stage A — additive Fourier transform

\[
\boxed{
\mathbb F_p
\longrightarrow
k\in\widehat{(\mathbb F_p,+)}.
}
\]

This diagonalizes the rotation port and turns the reflection port into the involution

\[
k\leftrightarrow-k.
\]

### Stage B — multiplicative Fourier transform

After quotienting by reflection,

\[
\boxed{
[k]\in(\mathbb F_p^\times/\{\pm1\})
\longrightarrow
\chi\in\widehat{G_p}.
}
\]

This diagonalizes the automorphism action `R -> R^a`.

Hence

\[
\boxed{
\text{sector}
\to
\text{additive frequency}
\to
\text{mirror orbit}
\to
\text{even Dirichlet character}.
}
\]

The two Fourier transforms are conceptually different: the first is on the additive sector group; the second is on the multiplicative automorphism group of nonzero frequency directions.

## 4. Cyclotomic arithmetic interpretation

The maximal real cyclotomic field

\[
F_p=\mathbb Q(\zeta_p+\zeta_p^{-1})
\]

has Galois group

\[
\operatorname{Gal}(F_p/\mathbb Q)\cong G_p.
\]

Thus the same group that permutes the nonzero H15 mirror-frequency channels is the Galois group of the real cyclotomic frequency field found in the norm theorem.

Its irreducible complex characters are precisely the even Dirichlet characters modulo `p`.

Consequently

\[
\boxed{
\zeta_{F_p}(s)
=
\prod_{\substack{\chi\bmod p\\\chi(-1)=1}}L(s,\chi),
}
\]

including the trivial character factor.

This is classical cyclotomic zeta factorization, but in H15 the characters acquire an explicit interpretation as multiplicative Fourier modes of the port-frequency channel permutation system.

## Theorem H15.52 — Frobenius eigenvalue in a channel

Let `ell != p` be a rational prime. Its Frobenius element in

\[
\operatorname{Gal}(F_p/\mathbb Q)\cong G_p
\]

is the class `[ell]`. On the `chi` projector channel,

\[
\boxed{
U_{[\ell]}P_\chi
=\chi(\ell)P_\chi.
}
\]

Therefore the local Euler factor attached to that one-dimensional arithmetic channel is

\[
\boxed{
(1-\chi(\ell)\ell^{-s})^{-1}.
}
\]

Multiplying over `ell != p` gives the corresponding Dirichlet `L(s,chi)` up to the standard conductor convention at `p`.

### Proof

The first formula is H15.51 with `a=[ell]`. The second is the standard one-dimensional Artin/Dirichlet Euler factor for the Frobenius eigenvalue `chi(ell)`. QED.

## 5. Observer meaning

A raw spectral observer sees mirror channels `[k]`. An automorphism-sensitive observer that can compare the marked worlds

\[
(R,S),\quad(R^a,S)
\]

and apply the character-weighted projector `P_chi` isolates one multiplicative arithmetic channel.

This yields the exact architecture

\[
\boxed{
\text{marked port automorphisms}
\to
\text{multiplicative channel projector}
\to
\chi(\ell)
\to
L(s,\chi).
}
\]

## RH / GRH boundary

The construction identifies the correct arithmetic channels but does not control the zeros of their `L`-functions. GRH for the real cyclotomic field `F_p` is equivalent to the critical-line statement for all even Dirichlet `L(s,chi)` appearing above.

Therefore the remaining analytic problem is now sharply separated from the finite port geometry:

\[
\boxed{
\text{channel decomposition is exact; zero-location control is not supplied by it.}
}
\]

Any genuinely new RH/GRH step would need an additional theorem that constrains the complex-`s` behavior of these character-projected observer transforms beyond classical Artin/Dirichlet formalism.