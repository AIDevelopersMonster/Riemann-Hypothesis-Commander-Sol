# SOL-QFIELD

**Scientific direction:** Pauli / particle-antiparticle / annihilation, scattering channels, amplitude and history structure  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** THIRD TARGET COMPLETE  
**Verdict:** `ANALOGY ONLY` with a proved native process-skeleton result  
**Line status:** typed support and native base evaluation diamonds are `1D-CLOSED`; genuine QFT modeling remains structurally obstructed

## Main separation

SOL-QFIELD permanently separates

\[
\boxed{
\text{exchange antisymmetry}
\ne
\text{field/operator anticommutation}
\ne
\text{scattering/annihilation channel structure}.
}
\]

The direct identifications

- “Pauli = FCOA noncommutativity”,
- “particle/antiparticle sign = boson/fermion parity”,
- “annihilation into bosons = operation became commutative”

all fail.

The surviving first-level structural match is

\[
\boxed{
\text{input geometry}
\longrightarrow
\text{typed output-channel class}.
}
\]

## Second target — amplitude lift

A normalized complex-amplitude decoration of terminal FCOA channels is not selected by the current structure: there is an uncountable family of compatible assignments.

More strongly, for terminal channels independent channel phases are operationally invisible under one-step readout. Modulo the phase action, normalized terminal complex amplitudes reduce to the classical probability simplex.

Thus

\[
\boxed{
\text{terminal complex weights}
\equiv_{\rm current\ observation}
\text{stochastic weights}.
}
\]

Relative phase becomes observable only after a stronger architecture exists:

\[
\boxed{
\text{branching}
+
\text{reconvergence}
+
\text{coherent path summation}.
}
\]

Deterministic re-entry alone is not interference.

## Third target — native diamonds

The existing legacy `oplus` already contains an infinite family of nondegenerate base-only evaluation diamonds. For every \(n\ge2\),

\[
\boxed{
(P_0\oplus P_n)\oplus P_0
=
P_0\oplus(P_n\oplus P_0)
=
P_{n-1},
}
\]

while the intermediate states are distinct:

\[
P_n\ne P_{n-1}.
\]

Reflection gives the corresponding negative-branch family.

Therefore native reconvergence does not require a second coordinate and is already present in the one-dimensional legacy structure.

However, current \(E^+,E^*,E^\times\) outputs are terminal, so there are no native typed re-entry diamonds.

The decisive new obstruction is semantic: the ordinary FCOA carrier remembers the common endpoint, not two independently surviving evaluation histories. To attach a relative phase to the two routes, the routes must first be promoted to distinct paths/morphisms.

Hence

\[
\boxed{
\text{associator equality}
\ne
\text{coherent superposition};
\qquad
\text{history retention is additionally necessary}.
}
\]

## Current QFIELD ladder

\[
\boxed{
QF0\;\text{typed support}
<
QF1\;\text{stochastic weights}
\equiv_{\rm terminal}
QF2\;\text{terminal complex weights}
<
QF2.5\;\text{native evaluation diamonds}
<
QF3a\;\text{history/morphism retention}
<
QF3b\;\text{coherent path algebra}
<
QF4\;\text{Hilbert-like dynamics}
<
QF5\;\text{Fock/CAR structure}.
}
\]

Current FCOA-Z reaches QF2.5 natively. QF3a and above are not yet derived.

## Files

- [`SOL_QFIELD_REPORT_v0_1.md`](./SOL_QFIELD_REPORT_v0_1.md) — three-layer separation, channel taxonomy, grading obstruction, deterministic-channel no-go, and negative QFT capability audit.
- [`SOL_QFIELD_AMPLITUDE_LIFT_v0_2.md`](./SOL_QFIELD_AMPLITUDE_LIFT_v0_2.md) — amplitude underdetermination, Terminal Phase Erasure, reconvergence threshold, re-entry/interference separation, and QF0–QF5 ladder.
- [`SOL_QFIELD_NATIVE_DIAMONDS_v0_3.md`](./SOL_QFIELD_NATIVE_DIAMONDS_v0_3.md) — native radial associator diamonds, typed-diamond no-go, extensionality/history obstruction, and the minimal-history frontier.

## Publication decision

`HOLD FOR APPLIED-DIRECTIONS SYNTHESIS`.

The branch now contains several theorem-level architectural results, but no standalone QFT/FCOA physical model has been reached. Publication should wait either for a canonical FCOA history category / coherent composition law or for the applied-directions synthesis.

## Next strike

Classify the **minimal FCOA history quotient**. Starting from legal evaluation paths, determine the coarsest natural congruence that preserves legacy values and reflection while keeping at least one radial associator pair distinct.

Three outcomes are targeted:

- `H0` — every natural congruence collapses the two histories;
- `H1` — a nontrivial finite/local history fiber survives and remains `1D-CLOSED`;
- `H2` — every nontrivial distinction propagates into unbounded compositional memory.

This H0/H1/H2 problem is now the sharp frontier of SOL-QFIELD.
