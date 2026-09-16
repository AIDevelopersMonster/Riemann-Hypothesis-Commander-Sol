# HATTER-SOL-17 · NON-ABELIAN TOMOGRAPHY AND HARDWARE

## Research task

**Working title:** *Zero-Oracle Non-Abelian Tomography: Canonical Orbit Decoding, Erasure Robustness, and FPGA Port Processors*

**Status:** active application/hardware research branch.  
**Parents:** HATTER-SOL-15 and the closed finite-group theorem layers of HATTER-SOL-16.  
**Goal:** turn the proved observer architecture into an exact end-to-end reconstruction machine and then quantify its hardware and robustness costs.

---

## 1. Frozen H16 handoff

HATTER-SOL-16 is closed at the theorem layer relevant to H17.

For generating pairs in

\[
G=PSL(2,7),
\]

there are exactly 114 simultaneous-conjugacy orbits. The five oriented trace probes

\[
\boxed{A,\quad B,\quad AB,\quad AB^{-1},\quad[A,B]}
\]

separate all 114 orbits. Primitive trace depth four is necessary and sufficient, and no subfamily of at most four probes from the complete depth-at-most-four candidate family separates all 114 orbits.

The engineering interface handed to H17 is therefore frozen as

\[
\boxed{
\text{PORT WORD ENGINE}
\to
\text{ORIENTED 3D CHANNEL}
\to
\text{5-PROBE SIGNATURE}
\to
\text{114-ORBIT DECODER}.
}
\]

H17 must not re-prove this finite tomography theorem as its main task. It must implement it end to end.

---

## 2. Terminology discipline

**Zero-oracle tomography** means reconstruction from externally addressable port actions and externally measured response channels, with no direct read access to the hidden simultaneous-conjugacy orbit label.

It does not initially mean reconstruction of an arbitrary unknown network topology. Arbitrary topology recovery requires a separate identifiability theorem.

Likewise, injectivity of the full five-probe signature does not imply recovery after arbitrary probe/channel loss. Erasure robustness is a separate theorem layer.

---

## 3. H17-01 · canonical 114-orbit golden model

The first active strike is now the final H16 handoff, not the older H15-dihedral audit.

Construct a deterministic, reproducible software model that:

1. enumerates `PSL(2,7)` exactly;
2. enumerates all generating pairs `(A,B)`;
3. quotients by simultaneous conjugacy;
4. chooses the lexicographically minimal pair in each orbit as canonical representative;
5. sorts the 114 representatives and assigns canonical `orbit_id = 0..113`;
6. evaluates the five frozen probes;
7. emits a 15-bit class signature using the encoding

   `1A=000, 2A=001, 3A=010, 4A=011, 7A=100, 7B=101`;

8. verifies that all 114 signatures are distinct;
9. generates the complete 114-entry SystemVerilog orbit ROM and exhaustive test vectors.

The generator itself, not a hand-edited table, is the source of truth.

---

## 4. H17-02 · full port-word engine

The H16 HDL appendix accepted five class labels as inputs. H17 must remove that shortcut.

Input:

- exact representations of hidden ports `A,B` in `PSL(2,7)`.

Hardware computes:

\[
A,\quad B,\quad AB,\quad AB^{-1},\quad ABA^{-1}B^{-1}.
\]

Required sub-blocks:

- exact finite-field / permutation representation of group elements;
- multiplication/composition;
- inversion;
- depth-four word sequencer;
- deterministic probe scheduler.

The first implementation may use the faithful permutation action on `P^1(F_7)` because it is exact and compact. A finite-field matrix engine is a later optimization/alternative architecture.

---

## 5. H17-03 · oriented class/representation channel

Each of the five word values must be mapped to one of

\[
1A,2A,3A,4A,7A,7B.
\]

The split `7A/7B` orientation must be preserved. H16 proved that outer-invariant scalarization loses this distinction, while the oriented 3D channel retains it.

The hardware-facing real orientation code is

\[
Q_4=0\mapsto00,\qquad Q_4=+1\mapsto01,\qquad Q_4=-1\mapsto10.
\]

A design that merges `7A` and `7B` is not a valid H17 tomography implementation.

---

## 6. H17-04 · complete 114-orbit decoder

The five class labels form a 15-bit signature.

H17 must provide:

- all 114 canonical ROM entries;
- a `valid` output for signatures outside the admissible set;
- a 7-bit canonical orbit ID;
- orientation output;
- exhaustive simulation against all 114 golden vectors.

This replaces the two-entry demonstration LUT in the H16 appendix.

---

## 7. H17-05 · interface-cost experiment

H16 also proved a closed-loop-only alternative.

General oriented words:

\[
\boxed{5\text{ probes},\quad \text{maximum primitive depth }4.}
\]

Balanced closed-loop-only words:

\[
\boxed{8\text{ explicit sufficient probes},\quad \text{maximum depth }14,}
\]

and depth 14 is necessary and sufficient for the complete balanced-word family.

H17 should implement both interfaces and measure the actual cost of forbidding open/mixed probes:

- word-engine state;
- latency;
- ROM/control cost;
- switching/activity;
- total logic and memory resources.

This is the hardware analogue of the earlier HATTER-SOL structural cost laws.

---

## 8. H17-06 · erasure-resilient observer memory

Only after the exact 114-orbit processor is working should H17 return to redundancy and failure tolerance.

For a probe family `S`, compute:

- exact injectivity after deleting specified probes;
- minimum erasure count that produces a collision;
- redundant probe families maximizing erasure distance;
- post-erasure minimum separation / singular-value analogues where a linear embedding is used;
- fault-injection agreement between theory and RTL.

Do not claim “zero loss” or arbitrary fault tolerance before these conditions are proved.

---

## 9. FPGA architecture stages

### Stage 1 — exact finite core

`A,B -> word engine -> class/orientation -> five-probe signature -> 114-orbit decoder`.

No Mahler integral and no hardware logarithm.

### Stage 2 — robust core

Add redundant probes and fault injection after the exact erasure theorem is known.

### Stage 3 — spectral host extension

The FPGA may stream exact word/representation data to a host PC for eigenvalue, determinant, or Mahler analysis.

### Stage 4 — optional spectral FPGA

Only after the finite exact path is stable may fixed-point quadrature, CORDIC/log LUTs, or pipelined spectral channels be considered.

---

## 10. Common benchmark record

Every software/hardware experiment should emit a common record containing:

- group/action ID;
- canonical input port IDs or representatives;
- probe word;
- exact word value/class;
- orientation state;
- five-probe signature;
- expected orbit ID;
- observed orbit ID;
- pass/fail;
- cycles/latency;
- synthesis resource data when available.

This allows exact comparison among Python golden model, HDL simulation, and physical FPGA.

---

## 11. Claim boundary

At Stage 1 H17 may claim only:

- exact realization of noncommuting finite ports;
- exact evaluation of the frozen five-probe observer;
- exact recovery of the hidden generating-pair orbit within the proved 114-state laboratory.

Recovery of arbitrary graph topology, arbitrary hidden groups, noisy analog systems, or general arithmetic structure is outside the Stage-1 theorem.

---

## 12. Hardware publication threshold

H17 crosses its hardware publication threshold only after all of the following exist:

1. deterministic software golden model;
2. complete 114-entry decoder;
3. HDL simulation agreeing on every golden vector;
4. an end-to-end port-word engine rather than externally supplied class labels;
5. synthesis report for a real FPGA target;
6. timing/resource table;
7. at least one physical-board experiment;
8. reproducible source/test-vector package and hashes.

Until then the branch is active research/implementation, not a finished hardware article.
