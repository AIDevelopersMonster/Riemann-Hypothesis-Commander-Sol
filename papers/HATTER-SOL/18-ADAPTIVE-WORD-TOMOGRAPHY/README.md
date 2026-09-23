# HATTER-SOL-18

## Adaptive Word Tomography and Nielsen Dynamics

This branch continues HATTER-SOL-17 on the theoretical side.

Core question:

\[
\boxed{
\text{Can a non-Abelian observer choose its next word from previous class results?}
}
\]

The project studies exact adaptive decision trees on the 114 canonical \(PSL(2,7)\) generating-pair orbits, then connects them to Nielsen dynamics on orbit space and finally to a sequential hardware architecture.

See:

- RESEARCH_TZ.md

Parent:

- papers/HATTER-SOL/17-NONABELIAN-TOMOGRAPHY-HARDWARE/


## Current theorem / publication spine

Closed theorem layers now include:

- H18-01 — exact adaptive depth four;
- H18-02 — Nielsen dynamics on 114 orbit states;
- H18-03 — canonical lift trace / Higman identification;
- H18-04 — explicit \(\tau\) query does not improve adaptive depth;
- H18-05 — three-shadow reconstruction of \(\tau\);
- H18-06 — exact one-persistent-erasure tomography;
- H18-07 — first adaptive RTL and generic hardware-cost layer;
- H18-08 — canonical 24-query microcoded dual-RTL baseline (CI closure still required);
- H18-09 — Nielsen-normal \(50\to26\) query reduction;
- H18-10 — global query-alphabet bound \(9\le M_1(W_4)\le12\);
- H18-11 — restricted 12-query controller: 305 query nodes and 18,425 explicit program bits.

Clean publication working drafts:

- \`HATTER_SOL_18_RU_DRAFT_v0.2.md\`
- \`HATTER_SOL_18_EN_DRAFT_v0.2.md\`

The old v0.1 drafts are historical working files and should not be used for
publication because their TeX escaping was damaged during an earlier API
write.

Current theorem target:

\[
\boxed{M_1(W_4)\in\{9,10,11,12\}}
\]

with exact closure required before replacing the certified interval.
