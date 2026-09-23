# H19-02 · Controlled Experiment Protocol

Status: **OPEN**

## Objective

Measure the mathematical-presentation effect without changing task semantics,
fault interface, I/O encoding, execution timing convention, or FPGA flow.

## Frozen semantic target

Use H18 restricted-12 LAB-04 semantics:

- same 197-state identify-or-REJECT domain;
- same static persistent erased-query identity;
- same registered-input / combinational-core / registered-output convention;
- same result encoding.

Every H19 presentation in the first family must be E0-equivalent on this exact
finite input contract.

## Presentation family

### P0 · DIRECT12

Compute all 12 query words as independent direct straight-line programmes.

Purpose: no word-prefix sharing.

### P1 · PREFIX19

Use the current H18-LAB-04 shared prefix DAG.

Frozen source fact:

\[
19
\]

shared permutation-composition prefixes, maximum word composition depth 3.

Purpose: measure ordinary common-subexpression sharing.

### P2 · NIELSEN12

Generate the same 12 observer functions through a frozen Nielsen/SLP basis.

Purpose: test whether a mathematically compressed generating basis yields a
different Boolean/physical image while semantics remains E0.

### P3 · FLAT

Flatten the same finite semantic map as aggressively as practical before
technology mapping.

Purpose: semantic control approximating a realization that forgets the source
mathematics.

## Fixed technology stacks

Initial targets:

1. Cyclone IV EP4CE115F29C7;
2. Cyclone V 5CEFA7F23C6.

Use the same Quartus II 13.1 timing-reference and reporting conventions already
frozen in H18.

No new device is added until the E0 four-presentation comparison is closed.

## Required measurements

Source structural profile:

\[
(Q,C_{\rm perm},D_{\rm perm},N_{\rm DAG},D_{\rm DAG},B_{\rm source}).
\]

Synthesis/physical profile:

\[
(ALM/LE,R,DSP,RAM,d_{\rm logic},t_{\rm cell},t_{\rm route},
F_{\max},N_{\rm cyc},T_{\rm tx}).
\]

## Interpretation rule

A change from P0→P1→P2 at fixed semantics is evidence about mathematical
factorization **only under the declared compiler discipline**.

P3 tests how much of that distinction survives when factorization is allowed to
collapse.

No measured ordering is called a theorem until it is supported by a proved
structural statement.
