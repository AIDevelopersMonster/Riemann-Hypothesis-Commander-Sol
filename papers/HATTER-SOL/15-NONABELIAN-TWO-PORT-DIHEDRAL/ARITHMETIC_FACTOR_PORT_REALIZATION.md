# HATTER-SOL-15 · Arithmetic Realization of Two-Port Sectors

Let `L/Q` be a finite Galois extension with

\[
\operatorname{Gal}(L/\mathbb Q)\cong D_{2p}
=\langle r,s\mid r^p=s^2=1,\ srs=r^{-1}\rangle,
\]

where `p` is an odd prime. Put

\[
D=\langle s\rangle,
\qquad
K=L^D.
\]

Then `[K:Q]=p`, and the embeddings/conjugate arithmetic sectors of `K` are indexed by the coset space `D\G`.

## Theorem H15.5 — reflection Frobenius gives one linear branch

Let `q` be a rational prime unramified in `L` whose Frobenius conjugacy class in `G` is the reflection class. Then the Frobenius permutation on

\[
D\backslash G\cong\mathbb F_p
\]

has cycle type

\[
\boxed{1\,2^{(p-1)/2}}.
\]

Consequently the factorization of `q` in the degree-`p` field `K` has residue-degree pattern

\[
\boxed{1,2,2,\ldots,2},
\]

with exactly one degree-one prime and `(p-1)/2` degree-two primes:

\[
q\mathcal O_K
=
\mathfrak q_0\mathfrak q_1\cdots\mathfrak q_{(p-1)/2},
\]

where

\[
f(\mathfrak q_0/q)=1,
\qquad
f(\mathfrak q_j/q)=2\quad(j\ge1).
\]

### Proof

All reflections in `D_{2p}` are conjugate when `p` is odd. On the coset model `F_p`, a reflection acts as

\[
i\mapsto-i+a
\]

for some `a`. Since `2` is invertible modulo `p`, this permutation has exactly one fixed point, and every other point is paired with its distinct reflected partner. Hence its cycle type is `1 2^{(p-1)/2}`.

For an unramified prime, the orbit lengths of Frobenius on the cosets of `D=Gal(L/K)` equal the residue degrees of the primes of `K` above `q`. Therefore the splitting pattern is exactly `1,2,...,2`. QED.

## Corollary H15.6 — density of reflection-factor primes

The reflection conjugacy class has `p` elements in a group of order `2p`. By Chebotarev, the set of unramified rational primes whose Frobenius lies in this class has density

\[
\boxed{\frac12}.
\]

Thus the H15 two-port arithmetic pattern occurs for a positive-density set of primes in every fixed dihedral extension of this form.

## Corollary H15.7 — factor ports

For a reflection Frobenius prime, the unique fixed Schreier sector is exactly the unique residue-degree-one factor branch of `q` in `K`; each two-cycle corresponds to one residue-degree-two branch.

Therefore the HATTER port abstraction can be read arithmetically:

\[
\boxed{
\text{Schreier sector orbit under Frobenius}
\longleftrightarrow
\text{prime-factor branch in }q\mathcal O_K.
}
\]

The non-abelian two-port action does not make ordinary integer multiplication noncommutative. Rather, it organizes the branches by which a rational prime decomposes in the surrounding number field.

## Relation to H15.3

For a chosen Frobenius reflection, the unique closure word identifies its unique fixed sector. Thus the same local closure event has two simultaneous descriptions:

1. group-theoretic: a unique fixed point of a reflection on `D\G`;
2. arithmetic: the unique degree-one prime above `q` in the degree-`p` subfield.

This is the first exact bridge in H15 from two-port non-abelian path order to literal prime factorization.