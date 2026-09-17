# FCOA Nesting & Atomicity — Classical Comparison

## Purpose

Classical prime numbers are an example of sandbox-relative atomicity, not the definition of the general theory.

## Positive-integer multiplicative sandbox

Take

\[
X=\mathbb Z_{>0},\qquad \Omega=\{\cdot\},\qquad U=\{1\},
\]

with ordinary multiplication total on `X`.

For `n>1`, a two-sided nontrivial decomposition witness is exactly

\[
a\cdot b=n,
\qquad a>1,\ b>1.
\]

Therefore the bilateral U-atoms are precisely the ordinary primes.

So in this one sandbox,

\[
\boxed{
\text{prime number}
=
\text{bilateral }\{1\}\text{-atom}.
}
\]

This equivalence uses the declared operation and trivial class. It does not license importing divisibility into an unrelated partial FCOA signature.

## Why classical irreducibility collapses to atomicity here

In the positive integers under multiplication, `U={1}` behaves as an actual unit class: multiplication by `1` leaves every element fixed. Hence all decompositions of a prime necessarily have one factor `1`, and the nontrivial factor is the original element. Thus the branch notions of U-atom and U-irreducible coincide.

That coincidence is not formal in a general sandbox. It depends on the special transport behavior of the classical unit.

## Divisibility as reconstructed nesting

For this sandbox, the one-step nontrivial factor graph satisfies

\[
a\triangleleft n
\]

whenever there exists `b>1` with `ab=n` or `ba=n`. Since multiplication is commutative this is just proper nontrivial divisibility.

The transitive closure recovers the familiar divisibility nesting among positive integers after trivial factors are removed.

In FCOA, by contrast, the nesting graph should be reconstructed directly from allowed operation cells or labeled translations. Calling that graph `divisibility` would add an arithmetic interpretation not present in the signature.

## Unique factorization is extra structure

The statement that every integer greater than one factors uniquely into primes is much stronger than the existence of atoms. In sandbox language it requires, among other things, termination of nontrivial decompositions and a strong confluence/uniqueness property modulo the relevant symmetries.

None of these follow merely from the definition of a U-atom.

A finite partial sandbox can have:

- no atoms because of composition cycles;
- atoms but elements with no factorization into atoms;
- multiple incompatible atomic decompositions;
- left/right asymmetry;
- terminal outputs that stop nesting entirely.

Therefore classical prime factorization is a special theorem package of the multiplicative integer sandbox, not a template to be assumed in FCOA.

## Boundary reading of classical primes

The positive-integer nontrivial factor graph is acyclic under the ordinary magnitude function because any proper nontrivial factor of `n` is strictly smaller than `n`. Consequently the local definition "no incoming nontrivial factor edge" agrees with minimality in the induced divisibility order above `1`.

This explains why the slogan

\[
\text{atomicity is a boundary state of composition}
\]

looks especially natural in classical arithmetic: the sandbox possesses a built-in well-founded rank that removes cyclic nesting.

The FCOA theory should therefore treat **well-foundedness/acyclicity**, not arithmetic itself, as the structural hypothesis behind that classical coincidence.