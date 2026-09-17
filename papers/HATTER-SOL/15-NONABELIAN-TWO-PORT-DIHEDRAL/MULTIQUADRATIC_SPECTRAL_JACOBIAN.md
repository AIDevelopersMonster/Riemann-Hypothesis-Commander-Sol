# HATTER-SOL-15 · Multiquadratic Spectral Jacobian Decomposition

**Status:** exact theorem layer under explicit genericity hypotheses. The general Jacobian decomposition mechanism is classical (Kani–Rosen / idempotent decomposition); H15 contributes the explicit decomposition of the dihedral Floquet spectral curve.

Fix an odd prime `p`, a nonzero mirror channel `k`, and write

\[
\vartheta=2\cos\frac{2\pi k}{p},
\qquad
\mu=4-\lambda.
\]

The H15 mirror block spectral curve is

\[
D_k(z,w;\lambda)=0,
\]

where

\[
D_k
=(\mu-z\omega^k-z^{-1}\omega^{-k})
 (\mu-z\omega^{-k}-z^{-1}\omega^k)
-(w+w^{-1})^2.
\]

Put

\[
u=z+z^{-1},
\qquad
v=w+w^{-1},
\]

and

\[
Q(u)=u^2-\mu\vartheta u+\mu^2+\vartheta^2-4.
\]

Then the spectral equation becomes

\[
\boxed{v^2=Q(u).}
\]

Moreover

\[
z=\frac{u+\sqrt{u^2-4}}2,
\qquad
v=\sqrt{Q(u)},
\qquad
w=\frac{v+\sqrt{v^2-4}}2.
\]

Therefore the function field is

\[
\boxed{
K(C_k)
=K(u)
\bigl(
\sqrt{a(u)},
\sqrt{b(u)},
\sqrt{c(u)}
\bigr),
}
\]

with

\[
a(u)=u^2-4,
\qquad
b(u)=Q(u),
\qquad
c(u)=Q(u)-4.
\]

Here `K` is any characteristic-zero coefficient field containing `vartheta` and `mu`.

## Genericity hypotheses

Assume:

1. `a,b,c` are squarefree;
2. their finite branch loci are pairwise disjoint.

Equivalently, the six roots of

\[
a(u)b(u)c(u)
\]

are distinct.

Useful explicit collision tests are

\[
Q(2)=(\mu-\vartheta)^2,
\qquad
Q(-2)=(\mu+\vartheta)^2.
\]

Thus overlap of `a` and `b` occurs exactly at

\[
\mu=\pm\vartheta.
\]

Overlap of `a` and `c` occurs when

\[
(\mu-\vartheta)^2=4
\quad\text{or}\quad
(\mu+\vartheta)^2=4.
\]

For nontrivial mirror channels `|vartheta|<2`, the polynomial `b` is squarefree unless

\[
\mu=\pm2,
\]

because

\[
\operatorname{disc} Q
=(\vartheta^2-4)(\mu^2-4).
\]

## Theorem H15.55 — genus five

Under the genericity hypotheses, the normalization of `C_k` is a smooth genus-five curve.

### Proof

The extension over `P^1_u` is a Galois multiquadratic cover with group

\[
G\cong(C_2)^3.
\]

There are six finite branch points, two from each of `a,b,c`. At each branch point the inertia group has order `2`, so above each branch value there are `4` points of ramification index `2`. Riemann–Hurwitz gives

\[
2g(C_k)-2
=8(-2)+6\cdot4
=8.
\]

Hence

\[
\boxed{g(C_k)=5.}
\]

QED.

## Theorem H15.56 — exact quotient curves

The seven nontrivial quadratic characters of `G` give the seven quadratic quotient curves

\[
C_a: y^2=a,
\qquad
C_b:y^2=b,
\qquad
C_c:y^2=c,
\]

\[
E_{ab}:y^2=ab,
\qquad
E_{ac}:y^2=ac,
\qquad
E_{bc}:y^2=bc,
\]

and

\[
C_{abc}:y^2=abc.
\]

Generically,

\[
g(C_a)=g(C_b)=g(C_c)=0,
\]

\[
\boxed{g(E_{ab})=g(E_{ac})=g(E_{bc})=1,}
\]

and

\[
\boxed{g(C_{abc})=2.}
\]

Explicitly,

\[
\boxed{
E_{ab}: y^2=(u^2-4)Q(u),
}
\]

\[
\boxed{
E_{ac}: y^2=(u^2-4)(Q(u)-4),
}
\]

\[
\boxed{
E_{bc}: y^2=Q(u)(Q(u)-4),
}
\]

and

\[
\boxed{
C_{abc}:y^2=(u^2-4)Q(u)(Q(u)-4).
}
\]

## Theorem H15.57 — Jacobian splitting

Under the same hypotheses,

\[
\boxed{
J(C_k)
\sim_K
E_{ab}\times E_{ac}\times E_{bc}\times J(C_{abc}),
}
\]

where `~_K` denotes isogeny over `K`.

### Proof sketch

The action of `G=(C_2)^3` on `C_k` decomposes the rational/complex representation on holomorphic differentials into character eigenspaces. Each nontrivial character corresponds to one quadratic quotient. The three single-radical quotients have genus zero and contribute no Jacobian factor. The remaining character quotients have genera `1,1,1,2`, whose sum is `5`, equal to `g(C_k)`. The standard Kani–Rosen/idempotent decomposition therefore yields the displayed isogeny. QED.

## Corollary H15.58 — Hasse–Weil L-factorization

When the curve and quotient maps are defined over a number field `K`, the isogeny implies equality of Hasse–Weil L-functions

\[
\boxed{
L(J(C_k)/K,s)
=
L(E_{ab}/K,s)
L(E_{ac}/K,s)
L(E_{bc}/K,s)
L(J(C_{abc})/K,s).
}
\]

Thus the genus-five spectral channel does **not** carry an analytically irreducible genus-five motive in general: it splits into three elliptic pieces and one genus-two piece.

## Why this matters for Mahler measure

Mahler measure of a two-variable polynomial can be interpreted, in suitable tempered/regulator settings, through regulator periods on the associated algebraic curve. H15 does **not** yet prove that the regulator class of `D_k` decomposes exactly into the four quotient factors above.

However, the Jacobian splitting gives a precise and testable mechanism for such a decomposition:

\[
\boxed{
\text{genus-5 spectral regulator}
\rightsquigarrow
3\times\text{elliptic regulator}
+\text{genus-2 regulator}.
}
\]

This is now the main arithmetic experiment rather than guessing a direct genus-five `L`-value.

## Prior-art boundary

Kani–Rosen decomposition and regulator/Mahler/L-value machinery are classical. H15 does not claim those general theories. The H15-specific content is the explicit multiquadratic structure of the dihedral Floquet spectral curve and the resulting concrete `1+1+1+2` Jacobian decomposition.