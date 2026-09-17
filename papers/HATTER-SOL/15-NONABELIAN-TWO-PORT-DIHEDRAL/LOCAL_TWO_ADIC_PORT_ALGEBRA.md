# HATTER-SOL-15 · Local 2-adic Port Algebra

**Status:** exact theorem layer

Assume `K/Q` is one of the degree-`p` side fields from H15.9, so the fixed prime `2` is unramified with splitting type

\[
1\,2^{(p-1)/2}.
\]

Then

\[
2\mathcal O_K
=\mathfrak p_0\prod_{j=1}^{(p-1)/2}\mathfrak p_j,
\]

with residue degrees

\[
f(\mathfrak p_0/2)=1,
\qquad
f(\mathfrak p_j/2)=2.
\]

## Theorem H15.11 — exact local algebra decomposition

There is a `Q_2`-algebra isomorphism

\[
\boxed{
K\otimes_{\mathbb Q}\mathbb Q_2
\cong
\mathbb Q_2
\times
U_2^{(p-1)/2},
}
\]

where `U_2/Q_2` is the unique unramified quadratic extension.

### Proof

For every number field,

\[
K\otimes\mathbb Q_2
\cong
\prod_{\mathfrak p\mid2}K_{\mathfrak p}.
\]

Because `2` is unramified, each completion has ramification index `1` and degree equal to its residue degree. The unique degree-one prime gives

\[
K_{\mathfrak p_0}\cong\mathbb Q_2.
\]

Each degree-two prime gives an unramified quadratic extension of `Q_2`; such an extension is unique up to `Q_2`-isomorphism, so every remaining factor is `U_2`. QED.

## Corollary H15.12 — canonical local anchor

Among the local factors above `2`, there is exactly one factor isomorphic to the base local field `Q_2` itself. Thus the reflection world carries a unique degree-one local branch.

This branch is intrinsic to the factorization of `2` inside the chosen degree-`p` field `K`; it does not require an externally assigned vertex label.

The remaining `(p-1)/2` factors occur as quadratic unramified branches and are indistinguishable by residue degree alone.

Hence the fixed-prime observer hierarchy begins with a canonical split:

\[
\boxed{
\text{one base-field anchor}
\quad+\quad
\frac{p-1}{2}\text{ quadratic branches}.
}
\]

## Relation to the two-port Schreier picture

The unique `Q_2` factor corresponds to the unique fixed sector of the reflection action. Each transposition orbit of the reflection corresponds to one degree-two local branch.

Therefore the same structure is visible in three languages:

\[
\boxed{
\text{Schreier fixed point / pairs}
\Longleftrightarrow
\text{prime splitting }1\,2^{(p-1)/2}
\Longleftrightarrow
\mathbb Q_2\times U_2^{(p-1)/2}.
}
\]

## Claim boundary

The unique degree-one branch is canonical only after the degree-`p` side field `K` is fixed. Across conjugate degree-`p` subfields inside the Galois closure, the corresponding anchor is transported by the ambient Galois action.

Thus this is a local arithmetic anchor, not an absolute label on the unmarked Galois closure.