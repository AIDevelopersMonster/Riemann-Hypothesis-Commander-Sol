# Prime-Successor Fixed-Ball Interior

Research result in the Prime-Successor Algebra programme.

**Date:** 2026-08-25  
**Status:** proved programme result; Zenodo manuscript stage  
**Repository:** `AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol`

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

The purpose is to test whether one fixed 13-adic ball produces a genuine intermediate layer: stronger than pure prime-permutation symmetry, but still too weak to define the standard prime order, prime successor, or an infinite grid-isolation mechanism.

## Main result

The fixed-ball layer satisfies a **formula-relative tail symmetry theorem**.

For every mixed first-order formula \(\Phi\) there exist a finite 13-adic depth \(K_\Phi\) and a finite exceptional set \(F_\Phi\) such that, on the good-prime tail, \(\Phi\) is invariant under every permutation preserving the finite colors

\[
c_{K_\Phi}(p)=u_p+B_{K_\Phi}
\]

and fixing \(F_\Phi\) and the non-good primes.

The proof rests on four components:

1. **Target finite-depth normal form.** Formulas in \((\mathbb Q,+,0,B)\) reduce, after the definitional expansion by fixed \(B_m\), to Boolean combinations of rational-linear equalities and fixed-depth ball conditions.
2. **Private denominator / exact linear separation.** On the good-prime tail, fixed homogeneous linear relations among Frobenius labels are determined by equality patterns.
3. **Uniform affine-fiber bound.** Every non-structural exact affine fiber for a fixed linear scheme has uniformly bounded size, independently of the target value.
4. **Target-witness transport.** Alternating source/target quantifiers are handled by a formula-relative back-and-forth argument. Exact equations either pin a target witness through finitely many labels, or leave a non-empty fixed-depth coset cell in which a generic rational with sufficiently many fresh denominator primes avoids all unwanted affine incidences.

The full proof checkpoint is in [`MIXED_QUANTIFIER_COMPRESSION_PROOF.md`](MIXED_QUANTIFIER_COMPRESSION_PROOF.md).

## Consequences

The result yields:

\[
S_{\mathbb P}\notin\operatorname{Def}(\mathcal B_\Delta),
\qquad
<_{\mathbb P}\notin\operatorname{Def}(\mathcal B_\Delta),
\]

and for every fixed isolator formula \(I\),

\[
\operatorname{GIR}(I)<\infty.
\]

At the same time, the extension is strictly stronger than pure Skolem arithmetic because prime 13 is definable from the bridge and the fixed ball: for \(p\ne13\), \(u_p\in B\), while \(v_{13}(u_{13})=-11\).

Thus the programme now has a rigorous fixed-ball interior layer between pure prime-permutation symmetry and the previously established right-wall grid-amplification mechanisms.

## Audit history

The initial checkpoint was subjected to an adversarial deep-research review. That review supported the candidate but left a genuine gap at alternating source/target quantifiers. The programme therefore did **not** accept the review's direct `QE + finite colors` argument. The gap was closed instead by the formula-relative target-witness transport argument recorded in the proof file.

The same audit also motivated two corrections:

- the affine statement is a **uniform fiber bound**, not a claim that all far-tail affine fibers are empty;
- no universal numerical GIR bound such as \(13^{2K}\) is claimed without explicit bookkeeping of equality patterns and bounded exact exceptions.

## Claim discipline

This result does **not** claim:

- decidability of the complete theory \(\operatorname{Th}(\mathcal B_\Delta)\);
- non-interpretability of full arithmetic by every possible interpretation;
- historical priority for the general model-theoretic mechanisms.

Those are separate questions.

## Publication status

The mathematical threshold for a dedicated Zenodo manuscript has been reached on **2026-08-25**. The Zenodo release should follow after a manuscript-level audit of notation, proof dependencies, prior-art language, bibliography, and RU/EN consistency.
