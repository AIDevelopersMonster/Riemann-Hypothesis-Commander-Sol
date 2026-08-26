# Prime-Successor Stationary Locality

Research continuation of the Prime-Successor Algebra / Two Walls programme.

**Status:** published as version 1.0  
**Date:** 2026-08-26  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22110465

## Publication title

**English**  
*Reflections on Stationary Locality with Commander Sol: Private-Place Bridges, Finite Multi-adic Windows, and Formula-Relative Compression*

**Russian**  
*Размышлизмы о стационарной локальности с Commander Sol: Private-Place Bridges, конечные мульти-адические окна и формульно-локальное сжатие*

## Main theorem

For a finite set of stationary places

\[
S=\{\ell_1,\dots,\ell_s\}
\]

and a Private-Place Bridge satisfying S-integrality, injective private-place separation, finite exact defect classes, and a prime-only bridge condition, the two-sorted structure

\[
\mathcal B_{u,S}=\Bigl((\mathbb N_{>0},\times),(\mathbb Q,+,0,(B_\ell)_{\ell\in S}),U\Bigr)
\]

satisfies Formula-Relative Tail Symmetry.

For every parameter-free first-order formula \(\Phi\) there exist a finite exceptional prime set \(F_\Phi\) and a finite multi-place depth vector \(\mathbf K_\Phi\) such that \(\Phi\) is invariant on the prime tail under every admissible prime permutation preserving regular multi-place colors and exact defect classes.

Consequences:

\[
<_{\mathbb P},\operatorname{Succ}_{\mathbb P}\notin\operatorname{Def}(\mathcal B_{u,S}),
\]

and for every fixed isolator formula \(I\),

\[
\operatorname{GIR}(I)<\infty.
\]

## Proof architecture

1. Multi-Place Finite-Depth Normal Form.
2. Local Coverage Lemma for negative subcosets.
3. Multi-Place Generic Cell Lemma.
4. Private-Place Exact Linear Separation.
5. Reduced Affine-Fiber / Bounded-Anchor Cylinder Lemma.
6. Fresh-Private-Place Avoidance.
7. Pinned/Free Target-Witness Transport.
8. Full mixed-quantifier induction.

The theorem-level proof checkpoint is in [`FINITE_STATIONARY_LOCALITY_THEOREM.md`](FINITE_STATIONARY_LOCALITY_THEOREM.md).

## Ramanujan application

For

\[
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}},
\]

we may take \(\lambda(p)=p\) on the good-prime tail. For every finite stationary atlas \(S\), primes outside \(S\) are S-integral, private denominator separation holds, and zero primes, if any, form one exact common-label class \(u_p=-1\).

Hence every finite stationary multi-adic expansion \(\mathcal B_{\Delta,S}\) remains in the formula-relative compression regime.

## Stronger corollary: infinite named atlas

If the language contains one separately named predicate \(B_\ell\) for every prime \(\ell\), each ordinary first-order formula still mentions only finitely many places. Therefore the finite theorem applies formula-by-formula under local integrality.

Thus the real phase boundary is not

\[
|S|<\infty \quad\text{versus}\quad |S|=\infty,
\]

but rather

\[
(B_\ell)_{\ell\in\mathbb P}
\quad\Big|\quad
\mathsf B(\ell,x),
\]

where the place becomes a first-order variable.

## Claim discipline

This programme result does not assert complete-theory decidability, NIP/stability, global non-interpretability of arithmetic, or infinite GIR for the uniformly indexed atlas. Those remain separate questions.

## Publication

Version 1.0 was deposited on Zenodo on 2026-08-26.

DOI: **10.5281/zenodo.22110465**  
Persistent URL: https://doi.org/10.5281/zenodo.22110465

Canonical release metadata is in [`release/`](release/).
