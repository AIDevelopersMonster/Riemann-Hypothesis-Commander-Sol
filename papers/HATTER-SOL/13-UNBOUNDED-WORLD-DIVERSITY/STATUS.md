# HATTER-SOL-13 · STATUS

**Date:** 2026-09-14  
**State:** active research; central scalar theorem spine established

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
- The intrinsic residue-degree observer already has unbounded range.
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

## Current theorem picture

The same fixed integer `2` exhibits three distinct levels of unboundedness:

1. **arithmetic support:** number of prime ideals above `2` is unbounded;
2. **observer response:** residue-degree support observer is unbounded;
3. **network response:** sparse carriers preserve unbounded scalar boundary diversity.

But carrier enrichment can also erase the same scalar memory completely, and the entire interpolation between the two extremes is known exactly.

## Remaining proof obligations

1. Lift the theorem from scalar residue-degree capacity to a richer HATTER ideal-typed response compatible with HATTER-SOL-10.
2. Determine whether the richer response has unbounded support size, polynomial diversity, or linear rank.
3. Run hostile prior-art/novelty audit of the final composed theorem.
4. Decide publication threshold only after the richer-response question is either solved or shown unnecessary by a strong no-go result.

## Claim discipline

Already proved: unbounded structural and scalar network-response diversity for one fixed rational integer across a natural world family.

Not proved: independent information, entropy, arbitrary payload capacity, cryptographic hardness, or unbounded rank of the full ideal-typed Pareto polynomial.

## Next action

Attack the HATTER-SOL-10-compatible ideal-typed lift. First try to prove that the prime ideals above `2` in the cyclotomic family carry a canonical typed state whose aggregate response retains more than the scalar residue degree. If conjugacy forces all typed states to coincide, record that as a symmetry no-go and identify the weakest richer observer that survives.