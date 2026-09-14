# HATTER-SOL-13 · STATUS

**Date:** 2026-09-14  
**State:** active research

## Closed

- H12 finite-world structural-memory framework is published: DOI `10.5281/zenodo.22747698`.
- Fixed quadratic conductor towers do not yield unbounded fixed-integer factor/interface diversity. See `CONDUCTOR_TOWER_NO_GO.md`.

## Current main target

Prove a positive fixed-integer unbounded-diversity theorem using a natural higher-degree family.

Primary probe:

\[
n=2.
\]

Primary world family:

\[
K_k=\mathbb Q(\zeta_{2^k-1}),\qquad k\ge2.
\]

Target arithmetic branching count:

\[
g_k=\#\{\mathfrak p\subset\mathcal O_{K_k}:\mathfrak p\mid2\mathcal O_{K_k}\}
=\frac{\varphi(2^k-1)}{k}.
\]

## Proof obligations

1. Prove `ord_{2^k-1}(2)=k` exactly.
2. Prove the cyclotomic decomposition formula for `2` in `K_k` applies because `2` is unramified.
3. Prove `g_k` is unbounded; prefer an elementary lower bound strong enough for the result.
4. Define the weakest intrinsic HATTER observer whose output already detects `g_k`.
5. Separate unbounded ideal support from unbounded network-response diversity.
6. Determine whether a canonical carrier response preserves an unbounded subsequence or collapses it.
7. Run prior-art/novelty audit before publication claims.

## Current conjectural theorem shape

There exists one fixed rational integer `n=2` and a natural sequence of number fields `K_k` for which the number of prime-ideal directions above `2` is unbounded.

This would establish unbounded **arithmetic structural diversity**. It does not yet establish unbounded entropy, message capacity, or an unbounded HATTER network response.

## Next action

Close obligations 1-3 in a self-contained theorem note, then attack observer survival.