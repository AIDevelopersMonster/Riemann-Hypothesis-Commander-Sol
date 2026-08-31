# FCOA-Z — Post-Publication Research State

Date: 2026-08-31  
Published anchor: DOI `10.5281/zenodo.22171473`

## Completed theorem chain after publication

1. `MIXED_RADIAL_CANCELLATION_GENERATOR.md`
   - natural non-tabular mixed generator;
   - exact mixed formula;
   - adjacent-output noncommutation;
   - complete five-status association realization.

2. `MIXED_GENERATOR_CLASSIFICATION.md`
   - all exact inward-covariant mixed maps factor through first-boundary normal form;
   - legacy boundary fixes the canonical extension uniquely.

3. `MIXED_FINITE_STATE_TRANSPORT.md`
   - first freedom beyond exact covariance is one `Z_2` phase bit;
   - finite-state phase clocks are exactly ultimately periodic;
   - unrestricted clocks give continuum many extensions;
   - old commutation/association statuses are blind to phase.

4. `PHASE_LOCALITY_COLLAPSE_THEOREMS.md`
   - local admissibility does not imply finite memory;
   - deterministic bounded locality does;
   - exact `r`-step covariance forces period dividing `r`;
   - twisted one-step covariance selects parity.

5. `OTIMES_TERMINAL_SYMMETRY_COLLAPSE.md`
   - `otimes`-only signed reduct has large terminal/source symmetry;
   - split fiber: `S_m wr C_2`;
   - shared fiber: `S_m x C_2`;
   - adding the `oplus` radial memory collapses full-axis symmetry to at most `C_2`;
   - terminal symmetry relative to a pointwise fixed source carrier is trivial.

6. `MINIMAL_BRANCHING_NONABELIAN_TRANSPORT.md` — v0.2 hostile-audit corrected
   - 4 vertices: first non-Abelian rooted ambient group `S_3`;
   - 7 vertices: first binary non-Abelian rooted group `D_8`;
   - correction: the root branch swap is canonical only on branch blocks, not at point level;
   - the lift set is a torsor over the subtree automorphism group;
   - minimal seven-vertex lift ambiguity is exactly `C_2`, hence one coherence bit.

7. `BRANCH_COHERENCE_VALUE_RECOVERY.md`
   - the one-bit connection is the choice between two cross-branch perfect matchings;
   - its stabilizer has index two in `D_8`;
   - one terminal output cannot encode the bit in values on a fixed domain;
   - two anonymous outputs plus a canonical root anchor recover the connection after erasure;
   - exact targeted `VRI=2`, reducing active group `D_8 -> V_4`.

8. `BRANCH_COHERENCE_SUPPORT_MINIMUM.md`
   - exact orbit/stabilizer search on `T^2`;
   - only the 8-cell directed cross-branch orbit supports a fiber with stabilizer exactly the connection `V_4`;
   - minimum connection-dependent fiber size = 4;
   - balanced `4+4` anonymous fibers permit output exchange;
   - adding the unique 1-cell root anchor breaks that exchange;
   - exact minimum anonymous-output domain size = 9.

9. `verify_branch_coherence_support.py`
   - reproducible exact enumeration of `D_8`, the ordered-pair orbits, the connection subgroup, minimum fiber support, and the 9-cell bound.

## Current exact resource passport for the first recoverable non-Abelian branch precursor

- active carrier: `7` vertices;
- ambient radial automorphism group: `D_8`;
- branch-lift ambiguity: `2` choices = `1 bit`;
- target connection stabilizer: `V_4`;
- anonymous terminal alphabet: `2` values, exactly minimal;
- connection-dependent special cells: `4`;
- canonical anti-output-swap anchor: `1`;
- total defined cells for value-only compilation: `9`, exactly minimal under connection-independent definedness;
- incremental Value-Rigidity Index: `2`.

## Important correction ledger

The earlier v0.1 branching note briefly claimed that the unlabeled seven-vertex tree canonically selected a pointwise root-branch swap. Hostile audit rejected that claim because a branch-block transposition has multiple pointwise lifts whenever the branch subtree has nontrivial automorphisms. The file was replaced by corrected v0.2.

No published Zenodo theorem is affected; the issue occurred only in post-publication research.

## Active frontier

The one-bit `D_8 -> V_4` problem is now fully solved at carrier, alphabet, and support levels.

The next programme-level invariant is

\[
\boxed{
m_G(H;S)=\min\{|F|:F\subseteq S,\ \operatorname{Stab}_G(F)=H\}.}
\]

The next strike is to solve or bound `m_G(H;S)` for natural pair orbits of wreath-product branch groups

\[
G=A\wr S_b,
\]

where `H` is the subgroup preserving a chosen inter-branch connection/coherence structure.

This would turn the seven-vertex calculation into a general theory of prescribed-stabilizer value support.