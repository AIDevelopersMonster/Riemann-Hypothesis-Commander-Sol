# Prime-Successor Fixed-Ball Interior

Research result in the Prime-Successor Algebra programme.

**Date:** 2026-08-25  
**Current GitHub version:** 1.1  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22101603  
**Status:** proved programme result; post-publication adversarial-review clarifications incorporated

## Publication manuscript

**English:** *Reflections on an Interior Layer between Two Walls with Commander Sol: A Fixed 13-adic Ball, Mixed Quantifier Compression, and Formula-Relative Tail Symmetry*  
**Russian:** *Размышлизмы о внутреннем слое между двумя стенами с Commander Sol: Один фиксированный 13-адический шар, Mixed Quantifier Compression и формульно-локальная симметрия*

The DOI record corresponds to the published v1.0 release. GitHub v1.1 is a clarification revision: the principal theorems and conclusions are unchanged.

## Object

We study

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
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}}.
\]

## Main result

For every mixed first-order formula \(\Phi\), there is a finite formula-relative partition of the prime tail such that \(\Phi\) is invariant under every admissible permutation preserving the relevant good-prime colors, the common-label zero-prime class, and a finite exceptional set.

Consequently,

\[
S_{\mathbb P}\notin\operatorname{Def}(\mathcal B_\Delta),
\qquad
<_{\mathbb P}\notin\operatorname{Def}(\mathcal B_\Delta),
\]

and for every fixed isolator formula \(I\),

\[
\operatorname{GIR}(I)<\infty.
\]

Prime 13 is nevertheless parameter-free definable, so the fixed-ball layer breaks the pure prime-permutation symmetry of Skolem arithmetic without reaching the previously exhibited infinite-grid amplification mechanisms.

## Version 1.1 clarifications

The post-publication adversarial review was accepted with local corrections. GitHub v1.1 adds:

1. an explicit proof that every fixed depth predicate \(B_m\) is definable in the original target language;
2. the full private-denominator valuation calculation and a separate injectivity corollary for good labels;
3. an explicit compatibility calculation for several simultaneous pinning equations in Target-Witness Transport;
4. a separate **Multiplicity-Blind Bridge Principle**;
5. treatment of zero primes \(\tau(p)=0\) as one exact common-label movable class \(u_p=-1\), so the prime-successor proof does not depend on Lehmer nonvanishing or on Serre's density theorem;
6. clarification that the comparison with the "right wall" is a programme-level comparison of grid-amplification behaviour, not a claim that a global interpretability preorder has been established.

The strengthened proof is in [`MIXED_QUANTIFIER_COMPRESSION_PROOF.md`](MIXED_QUANTIFIER_COMPRESSION_PROOF.md). See [`VERSION_1.1_NOTES.md`](VERSION_1.1_NOTES.md) for the change log.

## Claim discipline

Version 1.1 does **not** add claims of:

- decidability of \(\operatorname{Th}(\mathcal B_\Delta)\);
- non-interpretability of full arithmetic by every possible interpretation;
- an explicit effective map \(\Phi\mapsto K_\Phi\);
- historical priority for the general model-theoretic mechanisms.

## Publication record

Published record: **10.5281/zenodo.22101603**.  
GitHub v1.1 preserves the published mathematical result and makes the proof dependencies more explicit after adversarial review.
