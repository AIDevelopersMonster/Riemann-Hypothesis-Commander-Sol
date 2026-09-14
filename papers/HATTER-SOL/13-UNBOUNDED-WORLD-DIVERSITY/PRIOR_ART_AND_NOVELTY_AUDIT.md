# HATTER-SOL-13 · Prior-Art and Novelty Audit

**Date:** 2026-09-14  
**Status:** claim-narrowing audit

## Standard background — not HATTER novelty

The following ingredients are classical and must not be claimed separately as new:

1. prime-ideal decomposition
   \[
   p\mathcal O_K=\prod_i\mathfrak p_i^{e_i};
   \]
2. residue degrees
   \[
   f_i=[\mathcal O_K/\mathfrak p_i:\mathbf F_p];
   \]
3. decomposition/splitting type recorded by triples `(e,f,g)` or equivalent multisets;
4. the cyclotomic splitting law relating residue degree to multiplicative order modulo the conductor;
5. the fact that Galois groups act transitively on primes above a rational prime within a fixed decomposition type;
6. graph degree-sum and free-boundary bookkeeping once a port-capacity model has been chosen.

Computational systems such as Sage and PARI/GP expose this standard decomposition data directly: prime decomposition records ramification index and residue degree, and Sage has a `decomposition_type` interface returning `(e,f,g)` data.

## HATTER-specific candidate contribution

The candidate contribution is the composed theorem package, not the individual ingredients:

- one fixed rational integer, `2`;
- one natural infinite world family
  \[
  K_k=\mathbb Q(\zeta_{2^k-1});
  \]
- exact unbounded prime-ideal support
  \[
  g_k=\frac{\varphi(2^k-1)}k\to\infty;
  \]
- canonical local ideal-type response
  \[
  A_k(E,F)=g_kEF^k;
  \]
- exact unbounded response rank
  \[
  \dim_Q\operatorname{span}\{A_2,\ldots,A_m\}=m-1;
  \]
- intrinsic residue-degree port lift on the same arithmetic state;
- exact connected-carrier boundary spectrum
  \[
  \mathcal B_k=\{0,2,\ldots,g_k(k-2)+2\};
  \]
- explicit survival and complete collapse on sparse and saturated carriers.

The novelty wording should therefore be:

> HATTER-SOL-13 composes classical local prime-decomposition data with a fixed-integer world family and a port-network observer to obtain an exact unbounded-rank world response together with a complete carrier survival/collapse spectrum.

## Claims to avoid

Do not claim:

- discovery of splitting types or residue degree;
- a new cyclotomic decomposition theorem;
- a new graph degree-sum identity;
- entropy or payload capacity equal to polynomial rank;
- cryptographic hardness;
- that `A_{K,p}` is a new invariant unless a literature audit establishes that exact packaging independently.

Treat `A_{K,p}` conservatively as a convenient canonical generating polynomial for standard local data.

## Publication-gate consequence

The current mathematical claims survive after removing all novelty from the standard number-theory ingredients. The publication candidate, if prepared, should center the exact composed fixed-integer theorem and the carrier response law.