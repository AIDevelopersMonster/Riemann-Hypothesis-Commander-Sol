# Prime-Successor Fixed-Ball Interior

Research result in the Prime-Successor Algebra programme.

**Date:** 2026-08-25  
**Status:** proved programme result; manuscript audit passed; Zenodo package assembled  
**Repository:** `AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol`

## Publication manuscript

**English:** *Reflections on an Interior Layer between Two Walls with Commander Sol: A Fixed 13-adic Ball, Mixed Quantifier Compression, and Formula-Relative Tail Symmetry*  
**Russian:** *Размышлизмы о внутреннем слое между двумя стенами с Commander Sol: Один фиксированный 13-адический шар, Mixed Quantifier Compression и формульно-локальная симметрия*

Version 1.0, 2026-08-25. DOI pending Zenodo assignment.

## Object

We study the two-sorted structure

\[
\mathcal B_\Delta=
\Bigl(
(\mathbb N_{>0},\times),
(\mathbb Q,+,0,B),
U_\Delta
\Bigr),
\]

where

\[
B(x)\iff v_{13}(x)\ge0,
\qquad
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}}
\]

for prime atoms \(p\).

## Main result

The fixed-ball layer satisfies a **formula-relative tail symmetry theorem**.

For every mixed first-order formula \(\Phi\) there exist a finite 13-adic depth \(K_\Phi\) and a finite exceptional set \(F_\Phi\) such that \(\Phi\) is invariant on the prime tail under the formula-admissible permutations preserving the finite good-prime colors and the common-label zero-prime class.

The proof rests on four components:

1. **Target finite-depth normal form.** Formulas in \((\mathbb Q,+,0,B)\) reduce, after the definitional expansion by fixed \(B_m\), to Boolean combinations of rational-linear equalities and fixed-depth ball conditions.
2. **Private denominator / exact linear separation.** On the good-prime tail, fixed homogeneous linear relations among Frobenius labels are determined by equality patterns.
3. **Uniform affine-fiber bound.** Every non-structural exact affine fiber for a fixed linear scheme has uniformly bounded size, independently of the target value.
4. **Target-witness transport.** Alternating source/target quantifiers are handled by a formula-relative back-and-forth argument. Exact equations either pin a target witness through finitely many labels, or leave a non-empty fixed-depth coset cell in which a generic rational with sufficiently many fresh denominator primes avoids all unwanted affine incidences.

The proof checkpoint is in [`MIXED_QUANTIFIER_COMPRESSION_PROOF.md`](MIXED_QUANTIFIER_COMPRESSION_PROOF.md).

## Consequences

\[
S_{\mathbb P}\notin\operatorname{Def}(\mathcal B_\Delta),
\qquad
<_{\mathbb P}\notin\operatorname{Def}(\mathcal B_\Delta),
\]

and for every fixed isolator formula \(I\),

\[
\operatorname{GIR}(I)<\infty.
\]

At the same time prime 13 is definable from the bridge and the fixed ball: for \(p\ne13\), \(u_p\in B\), while \(v_{13}(u_{13})=-11\). Thus the programme has a rigorous fixed-ball interior layer between pure prime-permutation symmetry and the previously established right-wall grid-amplification mechanisms.

## Audit corrections incorporated

The final manuscript does not use the rejected shortcut `target QE + finite colors` across alternating source/target quantifiers. It uses direct target-witness transport. The affine theorem is stated as a uniform fiber bound, not eventual emptiness. The GIR theorem asserts a formula-dependent finite bound \(C(I)\), not an unsupported universal number such as \(13^{2K}\). Zero primes, if any, are treated as one exact common-label movable class \(u_p=-1\), so no Lehmer or density assumption is needed for the successor argument.

## Claim discipline

This result does **not** claim decidability of the complete theory, non-interpretability of full arithmetic by every possible interpretation, or historical priority for the general model-theoretic mechanisms.

## Publication status

The mathematical publication threshold was reached on **2026-08-25**. The bilingual manuscript has passed the manuscript-level consistency and visual-layout audit and the Zenodo v1.0 package has been assembled. The DOI remains pending until deposition.
