# HATTER-SOL-13 · STATUS

**Date:** 2026-09-14  
**State:** active research; publication-level theorem spine nearly closed

## Closed

- H12 finite-world structural-memory framework is published: DOI `10.5281/zenodo.22747698`.
- Fixed quadratic conductor towers do not yield unbounded fixed-integer factor/interface diversity. See `CONDUCTOR_TOWER_NO_GO.md`.
- For the fixed rational prime `2` and worlds
  \[
  K_k=\mathbb Q(\zeta_{2^k-1}),
  \]
  the prime-ideal support is unbounded:
  \[
  g_k=\frac{\varphi(2^k-1)}{k}\to\infty.
  \]
  See `CYCLOTOMIC_FIXED_PRIME_UNBOUNDED_SUPPORT.md`.
- The intrinsic residue-degree observer has unbounded range.
- Under the residue-degree port lift, a path/tree carrier preserves unbounded response:
  \[
  B_f(P_{g_k})=g_k(k-2)+2\to\infty.
  \]
- Explicit connected `k`-regular saturated carriers collapse the same response to
  \[
  B_f=0.
  \]
  See `RESIDUE_DEGREE_CARRIER_DICHOTOMY.md`.
- For all sufficiently large `k`, the full connected simple feasible scalar carrier spectrum is exactly
  \[
  \boxed{\mathcal B_k=\{0,2,4,\ldots,g_k(k-2)+2\}.}
  \]
  Hence
  \[
  |\mathcal B_k|=\frac{g_k(k-2)}2+2\to\infty.
  \]
  See `EXACT_CARRIER_BOUNDARY_SPECTRUM.md`.
- A canonical local ideal-type response is
  \[
  A_k(E,F)=g_kEF^k.
  \]
  The family is linearly independent over `Q`, with
  \[
  \dim_Q\operatorname{span}\{A_2,\ldots,A_m\}=m-1,
  \]
  and centered difference rank `m-2`. See `LOCAL_IDEAL_TYPE_POLYNOMIAL_RANK.md`.
- Galois transitivity gives a node-level symmetry no-go: individual prime ideals above `2` cannot be distinguished by any Galois-invariant observer depending only on local `(e,f)` type.
- Prior-art/novelty audit completed with claim narrowing. See `PRIOR_ART_AND_NOVELTY_AUDIT.md`.

## Current theorem picture

The same fixed integer `2` exhibits four exact forms of structural growth:

1. **arithmetic support:** the number `g_k` of prime ideals above `2` is unbounded;
2. **world-response rank:** the local ideal-type polynomial family has unbounded linear rank;
3. **network survival:** sparse carriers produce unbounded scalar boundary response;
4. **within-world carrier spectrum:** each sufficiently large world has the complete response interval
   \[
   \mathcal B_k=\{0,2,\ldots,g_k(k-2)+2\}.
   \]

At the same time, saturated carriers erase the scalar residue-degree boundary completely. This gives an exact infinite-world survival/collapse law.

## Remaining proof obligations

1. Run a hostile internal consistency audit across all H13 theorem files, especially the distinction between standard decomposition data and HATTER-specific response packaging.
2. Decide whether a stronger nonlocal ideal observer beyond `(e,f,g)` is mathematically necessary for H13, or should be deferred to H14.
3. Freeze article architecture and bibliography.
4. Signal publication threshold only if the hostile audit finds no hidden domain or novelty defect.

## Claim discipline

Already proved: one fixed rational integer supports a natural arithmetic-world response of unbounded symbolic rank and an exact unbounded carrier-response spectrum.

Not proved or claimed: independent information, Shannon entropy, arbitrary payload capacity, cryptographic hardness, or novelty of classical prime decomposition data itself.

## Next action

Perform the final hostile H13 consistency audit. If it passes, freeze the H13 article around the bounded/unbounded dichotomy, unbounded polynomial rank, and exact carrier survival/collapse spectrum rather than expanding into new machinery.