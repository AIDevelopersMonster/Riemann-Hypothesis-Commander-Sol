# Branch Closure — Prime-Only Carrier Elimination / Active-Skeleton Complexity

**Branch:** `research/finite-subset-carrier-wall`  
**Date:** 2026-08-29  
**Research status:** mathematically closed at current scope  
**Publication status:** ready for manuscript assembly

## 1. Research question

How much source-side memory can be removed from the Support-Cardinality Valuation Wall while retaining, losing, or classifying the wild logical behavior?

## 2. Final answer of the branch

The progression is now fully resolved at the intended scope.

### Full multiplicative source

Infinite positive support implies residual graph universality and undecidability.

### Explicit finite-set carrier

Source multiplication is unnecessary. Prime atoms + genuine finite subsets + residual incidence still suffice for uniform finite-graph coding and undecidability.

### Prime-only reduct

The finite-set carrier can also be removed, but support cardinality no longer classifies the theory. Infinite-support prime-only structures can be decidable or undecidable.

### Exact normal form

The prime-only residual structure is parameter-free interdefinable with a locally finite incidence structure

\[
(P,S,R),
\]

where the positive support \(S\) is itself definable and every source has a finite active neighborhood.

The isomorphism type is exactly encoded by

\[
(G_\kappa,\mu_\kappa),
\]

where \(G_\kappa\) is the active skeleton and \(\mu_\kappa\) records the multiplicity of every finite external active neighborhood.

### Programmability

Every countable backward DAG can be realized as an active skeleton by a binary profile whose support has natural and Dirichlet density zero.

Hence support cardinality, density, threshold alphabet, and infinite regular-positive GIR are all insufficient as exact classifiers.

### Saturated canonical subfamily

The multiplicity channel can be frozen by requiring every finite active neighborhood to occur countably infinitely often.

For this canonical saturated family:

\[
\boxed{
\operatorname{Th}(\mathcal I_{\kappa_G})\text{ decidable}
\iff
\operatorname{WMSO}(G)\text{ decidable}.
}
\]

This gives a clean exact structural endpoint.

## 3. Why the branch closes here

A full decidability classification for arbitrary multiplicity spectra would require solving the combined problem of arbitrary active skeleton complexity together with arbitrary finite-neighborhood multiplicity spectra.

The current work proves that this is an independent larger classification problem rather than a missing step needed to answer the carrier-elimination question.

Accordingly, arbitrary multiplicity-spectrum classification is moved to Future Work / a separate branch.

## 4. Audit state

- Full proof reread: PASS after two formal repairs.
- Hostile counterexample campaign: PASS.
- Literature positioning audit: PASS for preprint/Zenodo scope.
- Novelty boundary corrected: WMSO and finite-set interpretation technology is treated as classical background; novelty is restricted to the Ramanujan residual arithmetic realization, carrier elimination, support recovery, skeleton programmability, and saturated classification package.

## 5. Required publication repairs

The final manuscript must incorporate two explicit formal corrections from `FINAL_PROOF_AUDIT_AND_REPAIRS.md`:

1. incidence-DAG graph adjacency must include \(x\ne y\) to prevent artificial loops;
2. the WMSO upper reduction must be written as the explicit active/external case translation rather than invoking an informal finite tag.

## 6. Publication recommendation

This branch now contains enough new, coherent material for a standalone sequel paper.

Suggested working title:

**Reflections on Carrier Elimination and Active-Skeleton Complexity with Commander Sol**  
*From the Support-Cardinality Wall to Prime-Only WMSO Classification*

The publication should present the result as a progression from full source memory to carrier-free prime-only structures, culminating in the exact saturated WMSO equivalence.

**Final branch verdict: CLOSE RESEARCH; BEGIN PUBLICATION ASSEMBLY.**
