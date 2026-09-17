# HATTER-SOL-15 · Inter-World Gram Matrix and Arithmetic Parseval Law

**Status:** exact theorem layer. The finite-geometric spectral identities are classical consequences of the symmetric point-hyperplane design of projective space; H15 contributes the arithmetic observer interpretation.

Let

\[
V\cong \mathbb F_p^r,
\qquad
\mathcal P=\mathbb P(V),
\qquad
\mathcal W=\mathbb P(V^*),
\]

with

\[
N=|\mathcal P|=|\mathcal W|=\frac{p^r-1}{p-1}.
\]

For a projective class `A=[a] in P` and a world `H in W`, define the centered trace signature

\[
T_{A,H}:=
\begin{cases}
p-1,&a\in H,\\
-1,&a\notin H.
\end{cases}
\]

Equivalently, if `I` is the point-hyperplane incidence matrix, then

\[
T=pI-J.
\]

Every row and every column of `T` sums to `-1`.

## Theorem H15.34 — exact Gram matrix

The projective world transform satisfies

\[
\boxed{TT^{\!*}=T^{\!*}T=p^r I_N-(p-1)J_N.}
\]

In particular, for projective classes `A,B`,

\[
\boxed{
\langle T_A,T_B\rangle=
\begin{cases}
p^r-p+1,&A=B,\\
-(p-1),&A\ne B.
\end{cases}}
\]

### Proof

For a fixed point `A`, the number of hyperplanes containing it is

\[
k=\frac{p^{r-1}-1}{p-1},
\]

while the number not containing it is

\[
p^{r-1}.
\]

Hence

\[
\|T_A\|^2=k(p-1)^2+p^{r-1}=p^r-p+1.
\]

For distinct projective points `A,B`, the number of hyperplanes containing both is

\[
\lambda=\frac{p^{r-2}-1}{p-1},
\]

the number containing exactly one of them is `p^{r-2}` for each choice, and the number containing neither is `p^{r-2}(p-1)`. Therefore

\[
\langle T_A,T_B\rangle
=\lambda(p-1)^2-2p^{r-2}(p-1)+p^{r-2}(p-1)
=-(p-1).
\]

This gives the first Gram identity. Projective duality gives the column version, hence `T*T` has the same form. QED.

## Corollary H15.35 — spectral decomposition and exact inverse

The eigenvalues of the Gram matrix are

\[
\boxed{1}
\]

on the constant line and

\[
\boxed{p^r}
\]

on the zero-sum subspace.

Thus `T` is invertible and

\[
\boxed{
T^{-1}=\frac1{p^r}\bigl(T^{\!*}-(p-1)J\bigr).
}
\]

### Proof

Since

\[
(p-1)N=p^r-1,
\]

the matrix `p^r I-(p-1)J` has eigenvalue `1` on the all-one vector and `p^r` on its orthogonal complement. Also `TJ=-J`, so

\[
T\bigl(T^{\!*}-(p-1)J\bigr)
=TT^{\!*}+(p-1)J
=p^r I.
\]

QED.

## Theorem H15.36 — centered regular-simplex law

Let

\[
P_0=I_N-\frac1N J_N
\]

be orthogonal projection onto the zero-sum subspace and define

\[
U:=T+\frac1N J.
\]

Then every row and column of `U` has sum zero and

\[
\boxed{
UU^{\!*}=U^{\!*}U=p^r P_0.
}
\]

Hence the normalized projective-class signatures form a regular simplex / tight frame in the `(N-1)`-dimensional zero-sum space.

This is the exact spectral form of the inter-world redundancy.

## Theorem H15.37 — arithmetic Parseval identity

Restrict to unramified rational prime powers `q^m` for which `q` splits in the quadratic base field `E`, the class of a prime above `q` has nonzero image in `V=A/pA`, and `p` does not divide `m`.

For a projective class `A in P`, define the weighted prime-power count

\[
C_A(x)
:=
\sum_{\substack{q^m\le x\\ q\text{ split in }E\\ [\mathfrak q]\bmod pA\in A\\ p\nmid m}}
\log q,
\]

with the finitely many primes ramified in the class-field tower omitted.

Let `Y_H(x)` be the corresponding centered observer signal in world `H`, and remove its world-average:

\[
Y^\perp(x):=P_0Y(x).
\]

Then

\[
\boxed{
Y^\perp(x)=U^{\!*}C(x),
}
\]

and therefore

\[
\boxed{
\|Y^\perp(x)\|_2^2
=p^r\left(
\sum_A C_A(x)^2
-\frac1N\left(\sum_A C_A(x)\right)^2
\right).
}
\]

### Proof

For every admitted prime power, multiplication by `m` does not change its projective class in `V`, so its vector of centered traces across the worlds is exactly the corresponding row of `T`. Projecting away the world-constant direction replaces that row by the corresponding row of `U`. Summing the weighted contributions gives `Y^perp=U* C`. Applying `UU*=p^r P_0` yields the stated identity. QED.

Thus the inter-world second moment is exactly the variance of the projective prime-class counting vector, multiplied by `p^r`.

## Corollary H15.38 — exact recovery of relative prime-class counts

The deviations of the projective counts from their mean are reconstructed from the world deviations by

\[
\boxed{
P_0C(x)=\frac1{p^r}U Y^\perp(x).
}
\]

Hence the ensemble of degree-`p` worlds contains exactly the same zero-sum information as the projective distribution of prime classes, with no loss and no surplus.

## Corollary H15.39 — one-dimensional blind mode

World-difference data alone cannot recover the common scalar shift

\[
C_A(x)\mapsto C_A(x)+c
\qquad\text{for all }A.
\]

Its kernel is exactly the constant line.

Thus the inter-world comparison mechanism determines **relative distribution between arithmetic directions**, but it does not determine the universal scalar mode. An additional scalar observer is required to recover that mode.

This is the finite-geometric analogue of the earlier analytic split

\[
\zeta_K(s)=\zeta(s)\,L(s,V_0):
\]

relative world structure and universal rational background are different channels.

## Prior-art boundary

The point-hyperplane incidence structure of `PG(r-1,p)` is a classical symmetric design, and its incidence Gram spectrum is standard design theory. Projective incidence codes and simplex codes are also classical. H15 does not claim novelty for these finite-geometric identities.

The H15-specific arithmetic synthesis is that:

1. rows are projective ideal classes modulo `pA`;
2. columns are dihedral class-field worlds;
3. matrix entries are centered Frobenius observer responses;
4. the finite-design Gram identity becomes an exact Parseval law for arithmetic prime-class signals.