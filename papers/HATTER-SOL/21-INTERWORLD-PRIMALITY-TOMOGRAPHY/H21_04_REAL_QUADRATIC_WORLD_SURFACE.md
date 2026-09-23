# HATTER-SOL-21 · REAL QUADRATIC WORLDS ON A SURFACE

Status: **EXPLORATORY COMPUTATIONAL LAYER**

## 1. Purpose

H21-LAB-02 proved the abstract surface-capacity law with independent linear
world channels.

H21-LAB-03 replaces those abstract channels by actual quadratic Frobenius
worlds.

The integer \(n\) is fixed during one observation. A genus-\(g\) surface
carries \(g\) declared world handles

\[
W_1,\ldots,W_g.
\]

For the first laboratory use the ordered world list

\[
\boxed{
\Delta=-7,\ 5,\ -3,\ -11,\ 13,\ -19.
}
\]

All are implemented by quadratic algebras

\[
(\mathbb Z/n\mathbb Z)[x]/(x^2-Bx-C)
\]

with \(B=1\) and \(C=(\Delta-1)/4\).

## 2. Local handle state

For each odd \(n\) and world \(W\), the handle observer emits one categorical
state:

- \(P+\): Frobenius law passes and Jacobi sign is \(+1\);
- \(P-\): Frobenius law passes and Jacobi sign is \(-1\);
- \(F+\): Frobenius law fails with Jacobi sign \(+1\);
- \(F-\): Frobenius law fails with Jacobi sign \(-1\);
- \(G\): the world precheck exposes a nontrivial gcd witness;
- \(E\): exceptional/degenerate for this world descriptor.

For a prime not exceptional for the selected world, only \(P+\) or \(P-\) can
occur.

The genus-\(g\) surface signature is

\[
\boxed{
\Sigma_g(n)
=
(s_1(n),\ldots,s_g(n)).
}
\]

## 3. Certification and ambiguity

A handle is a compositeness certificate when its state lies in

\[
\{F+,F-,G\}.
\]

Define the first revelation handle

\[
\boxed{
\tau(n)
=
\min\{i:s_i(n)\in\{F+,F-,G\}\},
}
\]

with \(\tau(n)=\infty\) when the declared world list never certifies
compositeness.

For a prefix of \(g\) handles define the survivor set

\[
S_g
=
\{n\text{ composite}:\tau(n)>g\}.
\]

## 4. Signature collisions

For each genus \(g\), let

\[
\mathcal P_g
=
\{\Sigma_g(p):p\text{ prime}\},
\]

\[
\mathcal C_g
=
\{\Sigma_g(n):n\text{ composite}\}.
\]

The overlap

\[
\boxed{
\mathcal M_g
=
\mathcal P_g\cap\mathcal C_g
}
\]

is the set of prime/composite signature collisions.

## 5. Discrete trajectory

Let odd integers be visited in order,

\[
3,5,7,\ldots.
\]

The full six-handle signature defines a finite response trajectory
\(\Sigma(n)\).

Use Hamming distance for first discrete speed:

\[
\boxed{
v(n)=d_H(\Sigma(n-2),\Sigma(n)).
}
\]

Encode each categorical state by a one-hot vector and define the second
difference diagnostic

\[
\boxed{
\kappa_2(n)
=
\|\mathbf e(\Sigma(n+2))
-2\mathbf e(\Sigma(n))
+\mathbf e(\Sigma(n-2))\|_2^2.
}
\]

This is a **curvature proxy**, not intrinsic geometric curvature.

## 6. Required stratification

H21-LAB-03 reports trajectory statistics separately for

- primes;
- prime squares;
- distinct-prime semiprimes;
- higher prime powers;
- other composites.

## 7. Claim boundary

The quadratic Frobenius laws are classical and finite-character sign patterns
are strongly controlled by congruence classes.

Therefore a visually striking trajectory or curvature-proxy pattern is not
accepted as arithmetic novelty.

The laboratory is useful only if it identifies a robust observer phenomenon
that survives stronger residue-periodicity and null-model controls.
