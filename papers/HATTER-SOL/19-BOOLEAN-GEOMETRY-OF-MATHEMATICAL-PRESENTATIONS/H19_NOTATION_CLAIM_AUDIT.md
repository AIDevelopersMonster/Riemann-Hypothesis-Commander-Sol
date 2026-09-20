# H19 · Notation and claims audit

Status: PASSED WITH HARDENED CLAIM SET  
Date: 20 September 2026

## 1. Objects and notation

The publication manuscripts use the following roles consistently:

- \(M\): mathematical presentation.
- \(\mathcal F\): finite family of presentations.
- \(C_i(M)\): complete compiler state at stage \(i\).
- \(O\): observer on a compiler or physical state.
- \(\sim_{i,O}\): observer-induced equivalence.
- \(\mathcal P_{i,O}\): induced partition of \(\mathcal F\).
- \(\mathcal P_i^{\rm full}\): complete-state partition.
- \(Q(\mathcal P)\): number of indistinguishable unordered presentation pairs.
- \(L_i(O)\): latent partition gap.
- \(D,P,N\): DIRECT12, PREFIX19, NIELSEN12.

No symbol is used for two incompatible mathematical objects in the final RU/EN manuscripts.

## 2. Claim hierarchy

### Theoretical background statements

The following are retained as elementary lemmas/framework facts, not novelty claims:

- observer refinement induces partition refinement;
- joint observers combine distinctions coordinatewise;
- deterministic complete-state equality cannot later split;
- partition lattices and observational equivalence are classical.

### Construction-relative statements

The following are explicitly scoped to the declared compilation discipline:

- generated-DAG structural accounting;
- temporal/spatial accounting examples;
- source-operation counts for DIRECT12, PREFIX19, NIELSEN12.

No unrestricted circuit lower bound is claimed.

### Empirical compiler statements

The following are scoped to the frozen Yosys flow/version/options and the declared observers:

\[
\mathcal P_{\rm proc}
=
\mathcal P_{\rm techmap}
=
\{\{D,P\},\{N\}\},
\]

\[
\mathcal P_{\rm ABC}
=
\{\{D\},\{P\},\{N\}\}.
\]

The manuscript says observer hiding/re-exposure, not destruction/resurrection of complete state.

### Empirical physical statements

Cyclone V:

\[
\mathcal P_{\rm CV}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
\]

Gowin:

\[
\mathcal P_{\rm GW}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
\]

Cross-vendor claim:

\[
\boxed{
\mathcal P_{\rm CV}^{\rm joint}
=
\mathcal P_{\rm GW}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
}
\]

This is a two-experiment partition-shape replication only.

## 3. Prohibited overclaims checked

The final manuscripts do not claim:

- routed-netlist identity for D/P;
- bitstream identity;
- equality of complete physical states;
- universal technology-independent invariance;
- a universal scalar ranking of presentations;
- minimum Boolean-circuit complexity;
- statistical generalization over FPGA families;
- novelty of partition lattices, BDDs, observational equivalence, translation validation, or equality saturation.

## 4. Timing language checked

For Gowin all three designs completed P&R and bitstream generation but failed the declared 100 MHz timing target.

The manuscript keeps these logically separate:

\[
\text{P\&R PASS}\ne\text{timing closure}.
\]

Actual Fmax is reported as a measured post-route coordinate.

## 5. Cross-vendor comparison checked

Only partition shape is compared across vendors.

Cyclone ALM values are not numerically compared to Gowin Logic/LUT/CLS as if they were the same resource unit.

Timing direction is explicitly allowed to differ between technologies.

## 6. Evidence/provenance checked

The final claim set is backed by:

- Cyclone-V compact summary and physical partition atlas;
- Cyclone-V SHA-256 provenance manifest, 33 artifacts;
- Gowin synthesis summary;
- Gowin P&R summary;
- Gowin SHA-256 provenance manifest, 33 artifacts.

## 7. Editorial disposition

Result: PASS FOR PUBLICATION-CANDIDATE CLAIM SET.

Remaining caveat for future extensions: any claim stronger than two-vendor finite replication requires additional target families or a theorem connecting source invariants to physical partition stability.
