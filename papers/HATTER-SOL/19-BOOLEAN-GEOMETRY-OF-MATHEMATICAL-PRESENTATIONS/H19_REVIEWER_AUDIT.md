# H19 · Reviewer-style audit

Recommendation: ACCEPT AS PREPRINT / MINOR REVISION FOR FORMAL VENUE  
Scope: H19_MANUSCRIPT_EN.md and the frozen evidence package  
Date: 20 September 2026

## Summary

The manuscript studies three mathematically motivated, functionally equivalent presentations of a finite task and tracks how presentation distinctions appear under source, compiler, and physical FPGA observers.

The strongest result is experimental rather than foundational order theory:

\[
\mathcal P_{\rm ABC}
=
\{\{D\},\{P\},\{N\}\},
\]

while two independent FPGA vendor/toolchains yield

\[
\mathcal P_{\rm CV}^{\rm joint}
=
\mathcal P_{\rm GW}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
\]

The work is unusually careful about the distinction between observer equality and complete-state equality, and the SHA-256 manifests materially strengthen reproducibility.

## Major issues

### M1. Novelty must remain narrow

Resolved.

The manuscript no longer presents partition lattices, observational equivalence, branching-program/circuit comparisons, translation validation, or equality saturation as novel.

The claimed contribution is the controlled presentation family plus compiler/physical partition trajectory and two-vendor replication.

### M2. Re-separation must not be described as resurrection of destroyed information

Resolved.

The deterministic no-resurrection statement is used correctly. The manuscript describes intermediate equalities as coarse-observer hiding and later differences as re-exposure.

### M3. Cross-vendor language must not imply universal invariance

Resolved.

The manuscript uses two-vendor replication / partition-shape replication and explicitly limits the population to the two declared experiments.

### M4. Physical fit and timing closure must be separated

Resolved.

Gowin P&R completion is reported independently from failure of the 100 MHz timing constraint.

## Minor issues

### m1. Terminology is intentionally hybrid

The manuscript mixes mathematical English terms with Russian prose in the RU version. This is acceptable for the internal/preprint Russian edition because many terms are tool-native. The EN version should be the archival publication version.

### m2. Tool versions should remain in the methods section

Resolved in the manuscript and evidence map.

### m3. A third FPGA technology would strengthen persistence claims

Not required for the current claim. Recommended future work.

### m4. Seed sensitivity is not characterized

Not required for the present summary-coordinate experiment, but future P&R replication should include multiple seeds where supported.

## Reproducibility assessment

Strong for a finite hardware-comparison preprint.

Strengths:

- frozen semantic contract;
- common regression;
- matched family;
- explicit observer definitions;
- compact machine-readable summaries;
- raw-run SHA-256 manifests;
- two independent physical toolchains.

Limitations:

- heavy raw run directories are not archived directly;
- hashes certify local artifacts but do not prove deterministic rerouting;
- only one semantic family is tested.

## Mathematical correctness assessment

No inconsistency found in the final claim hierarchy.

The no-resurrection statement is a direct consequence of deterministic transport and is correctly scoped.

The partition refinement statements are elementary and correctly identified as background.

The latent-gap quantity is internally consistent for the finite family and is not overinterpreted.

## Empirical correctness assessment

The reported tables support the stated partitions.

DIRECT12 and PREFIX19 are equal on every coordinate of each declared joint physical observer.

NIELSEN12 differs in at least one physical coordinate on both technologies.

Therefore both declared joint physical observers induce exactly

\[
\{\{D,P\},\{N\}\}.
\]

## Final reviewer verdict

The work is suitable for preprint publication with the present conservative title and claim set.

For a formal conference/journal submission, the most valuable extension would be one of:

1. a second independent semantic presentation family;
2. a third FPGA technology;
3. multi-seed physical robustness;
4. a predictive theorem linking source invariants to observer-partition stability.

None is required to justify the present finite replicated result.
