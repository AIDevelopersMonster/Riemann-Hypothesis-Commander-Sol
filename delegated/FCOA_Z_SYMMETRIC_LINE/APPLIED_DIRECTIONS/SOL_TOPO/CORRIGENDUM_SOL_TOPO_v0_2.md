# Corrigendum to `SOL_TOPO_LC2_REFLECTION_BRAID_v0_2.md`

**Date:** 2026-09-01  
**Status:** REQUIRED INTERPRETATION CORRECTION  
**Superseding synthesis:** `SOL_TOPO_ARTICLE_EN_v1_0.md` / `SOL_TOPO_ARTICLE_RU_v1_0.md`

## 1. What remains valid

The following local algebraic statements in v0.2 remain valid for a fixed split terminal-output orbit

\[
Q_n^\alpha=\{E_n^\alpha,\bar E_n^\alpha\}:
\]

1. after free linearization, reflection defines a swap involution `J`;
2. retained legacy/reflected provenance defines a sign involution `S`;
3. `J^2=S^2=I` and `JS=-SJ`;
4. therefore `(JS)^2=-I`;
5. the unique normalized operator in `span_R{J,S}` exchanging these two local observables has Hadamard form `(J+S)/sqrt(2)`;
6. for an abstract two-dimensional Hadamard braid template with `R_t=diag(1,t)`, the braid relation is equivalent to `(t-1)(t^2+1)=0`, so the nontrivial projective ratios are `t=±i`.

These calculations are retained as statements about an internal **provenance fiber** and an abstract two-state braid template.

## 2. What is withdrawn

The following interpretation is withdrawn:

> the Hadamard generated from the split reflection/provenance orbit is already the Ising fusion-channel associator `F^{sigma sigma sigma}_sigma` for the channel encoding introduced in v0.1.

The reason is a typed-factor mismatch.

The v0.1 fusion dictionary identifies

\[
1\leftrightarrow E_n^+,
\qquad
\psi\leftrightarrow E_n^\times.
\]

Thus the `sigma x sigma` fusion-channel degree of freedom distinguishes **terminal types** `E^+` and `E^times`.

By contrast, split reflection distinguishes

\[
E_n^\alpha\leftrightarrow\bar E_n^\alpha
\]

inside a **fixed** terminal type `alpha`.

Hence the corrected space is

\[
H_n\cong H_{ch}\otimes H_{pr},
\]

with reflection/provenance acting on `H_pr` and the Ising associator acting on `H_ch`.

## 3. Consequence

The old reflection/provenance algebra is block diagonal with respect to the `E^+ / E^times` channel decomposition. Therefore it cannot generate the Ising channel Hadamard without at least one new cross-type channel-mixing morphism.

This is proved formally in `SOL_TOPO_COHERENCE_BARRIER_v0_3.md` and in the v1.0 unified articles.

## 4. Additional global correction

The v0.2 statement that an overall sign of the local Hadamard is merely gauge is valid only for the isolated two-dimensional matrix problem. In a full Ising fusion category, the two signs of the Tambara-Yamagami parameter distinguish the two inequivalent monoidal Ising categories. Therefore the sign cannot be globally discarded once pentagon coherence and the complete tensor structure are included.

## 5. Publication rule

`SOL_TOPO_LC2_REFLECTION_BRAID_v0_2.md` is retained for research history but must not be cited as the current programme verdict. Any public manuscript must cite the corrected v1.0 synthesis and may cite v0.2 only together with this corrigendum.
