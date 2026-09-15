# HATTER-SOL-17 · NON-ABELIAN TOMOGRAPHY AND HARDWARE

## Research task

**Working title:** *Zero-Oracle Non-Abelian Tomography: Algorithms, Erasure Robustness, and FPGA Port Processors*

**Status:** application/hardware research branch.  
**Parents:** HATTER-SOL-15 and the finite-group laboratories of HATTER-SOL-16.  
**Goal:** turn the observer architecture into explicit reconstruction algorithms and a hardware demonstrator without claiming more than the proved observer model supports.

---

## 1. Terminology discipline

The phrase **zero-oracle tomography** will mean:

> reconstruction from externally addressable port actions and externally measured response channels, with no direct read access to internal state labels.

It will **not** initially mean reconstruction of an arbitrary unknown network topology. H15 proves invertibility for a specific labelled reaction ensemble; arbitrary topology recovery requires a new identifiability theorem.

Likewise, invertibility of the full response matrix does **not** by itself imply lossless recovery after arbitrary channel failures. Erasure robustness must be proved from submatrix rank/singular-value conditions.

---

## 2. Article A: finite zero-oracle tomography

Start with a deliberately finite statement.

### Input

- a known port group/action family;
- an unknown reaction/state label from a finite set;
- a selectable family of port words / commutator probes;
- measured labelled observer responses.

### Output

- reaction class;
- confidence/residual;
- if sufficient probes exist, the exact hidden finite state.

### Main theorem target

Given an observer matrix `A`, characterize the smallest probe subset `S` for which

`A_S x = A_S y => x=y`

on the admissible reaction set, and separately on the full zero-sum linear span.

For linear tomography the basic quantities are:

- rank of `A_S`;
- smallest singular value;
- condition number;
- erasure distance: minimum number of observer rows whose removal destroys injectivity.

This is the correct route from H15 invertibility to fault tolerance.

---

## 3. Article B: erasure-resilient observer frames

Replace the phrase “topological memory with zero loss” by a theorem-driven formulation:

> **erasure-resilient non-Abelian observer memory**.

For an analysis operator `A:C^d -> C^m`, define exact `e`-erasure recovery by requiring every row-deleted operator `A_E`, `|E|<=e`, to remain injective.

Research goals:

1. compute exact erasure tolerance for the dihedral primitive Mahler frame;
2. bound the worst-case post-erasure singular value;
3. construct redundant probe sets maximizing robustness;
4. compare projective-code coarse observers with Mahler linear observers;
5. identify whether the H15 code distance and linear-frame erasure distance are related or genuinely different invariants.

Only after these are proved may the article claim recovery under channel failures.

---

## 4. FPGA demonstrator architecture

The first hardware should compute exact finite-group observables, not the full transcendental Mahler integral.

### FPGA block 1 — Port engine

Represent a permutation port as a LUT/memory map.

Operations:

- apply port `A` or `B`;
- compose words;
- inverse lookup;
- compute commutator `ABA^{-1}B^{-1}`;
- stream cycle/fixed-point statistics.

For matrix groups `PSL(2,q)`, use finite-field matrix multiplication and inversion.

### FPGA block 2 — Closed-word observer

Given a programmed list of words, evaluate:

- fixed-point counts;
- permutation traces;
- matrix traces;
- selected powers `Tr K^m`;
- compact fingerprints.

This block is exact over finite groups and is the most natural first prototype.

### FPGA block 3 — Character/representation projection

For small groups, store representation matrices or character-table values in ROM and accumulate class/trace channels.

### FPGA block 4 — Host-linked spectral observer

Initial version:

- FPGA generates exact port/word data and sample matrices;
- host PC evaluates eigenvalues, log determinants, and 2D Mahler quadrature.

Second-generation version may move fixed-point spectral quadrature onto FPGA using fixed-point arithmetic, CORDIC/log LUTs, and a pipelined torus grid.

Do not start with hardware logarithms before the exact finite core is validated.

---

## 5. Suggested first FPGA scale

Three progressively harder targets:

1. `D_{2p}` with small prime `p` — reproduce H15 commutator, traces, and labelled channels;
2. `A5` as permutations of five letters — first nonsolvable port processor;
3. `PSL(2,7)` — finite-field matrix engine and higher-dimensional representation channels.

The same serial command protocol should select the group, port pair, word, and observer.

---

## 6. Test-vector and benchmark format

Every software/hardware experiment should emit a common record containing:

- group ID;
- representation/action ID;
- port IDs `A,B`;
- word/probe ID;
- exact commutator/class result;
- exact trace/fixed-point response;
- optional floating spectral/Mahler response;
- expected reconstruction label;
- timing and resource data.

This allows bit-for-bit comparison between Python reference, FPGA simulation, and physical board.

---

## 7. What can be claimed at each stage

### Stage 1 — exact demonstrator

Claim only:

- correct realization of noncommuting ports;
- exact commutator/trace observer;
- finite-state reconstruction matching the proved software model.

### Stage 2 — robust tomography

Claim only after proof and fault injection:

- exact recovery under a specified number/pattern of erased channels;
- quantified condition number/noise tolerance.

### Stage 3 — hidden-network inference

Only after an identifiability theorem:

- recovery of unknown internal topology/parameters from external probes.

Until then, “zero-oracle” refers to hidden state, not arbitrary unknown graph reconstruction.

---

## 8. First active strike

The first H17 deliverable is a **reference observer matrix and erasure audit for the H15 prime-dihedral laboratory**, followed by a cycle-accurate FPGA architecture for the exact commutator/trace core.

Hardware article threshold:

- software golden model;
- HDL simulation agrees on all test vectors;
- synthesis report on a real FPGA target;
- at least one physical-board experiment;
- reproducible resource/timing table.
