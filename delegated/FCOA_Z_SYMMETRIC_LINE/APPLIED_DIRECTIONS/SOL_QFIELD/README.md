# SOL-QFIELD

**Scientific direction:** Pauli / particle-antiparticle / annihilation and scattering channels  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** FIRST TARGET COMPLETE  
**Verdict:** `ANALOGY ONLY`  
**Line status:** `1D-CLOSED` for unweighted typed channel incidence; genuine QFT modeling obstructed at the current structural level

## Main result

SOL-QFIELD separates three structures that must not be conflated:

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

The surviving structural match is narrower:

\[
\boxed{
\text{input geometry}
\longrightarrow
\text{typed output-channel class}
}
\]

FCOA base-valued versus terminal/new-sort outputs can encode an **unweighted reaction-channel incidence shadow** while remaining independent of local commutation status.

## Main obstruction

A single FCOA binary operation is a partial function. But one physical incoming pair may have several distinct allowed outgoing channels. For example, the same electron-positron input supports both elastic Bhabha scattering and annihilation into photons. Therefore one deterministic operation on only particle-type inputs cannot faithfully represent QED channel support.

Current FCOA-Z also lacks Hilbert/Fock space, field operators, CAR/CCR, amplitudes, unitarity, conservation laws, relativistic kinematics, phase space, and probabilistic channel weights.

## Files

- [`SOL_QFIELD_REPORT_v0_1.md`](./SOL_QFIELD_REPORT_v0_1.md) — full definitions, three-layer taxonomy, channel map, independence theorem, particle/antiparticle grading obstruction, deterministic-channel no-go, toy model, line-gate audit, and next target.

## Publication decision

`HOLD FOR APPLIED-DIRECTIONS SYNTHESIS`.

The branch provides a useful anti-overclaim theorem and abstract channel taxonomy, but no standalone QFT/FCOA physical model has been reached.

## Next strike

Test whether typed FCOA channel support admits a non-arbitrary **complex-amplitude lift** compatible with legacy exactness, reflection, normalization/unitarity, and an internally generated selection rule. If arbitrary amplitudes can be attached freely, stop the physical analogy. If a linear/Fock-like layer is forced, route the result toward `FCOA-QUANTIZED`.
