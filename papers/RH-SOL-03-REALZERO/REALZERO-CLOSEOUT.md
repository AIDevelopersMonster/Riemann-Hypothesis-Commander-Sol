# RH-SOL-03 · REALZERO — research closeout

Status: research phase complete.
Closeout date: 2026-08-25.

## Core question

Does the Dirichlet `log(m)` comb survive when physical time is taken directly from actual Riemann-zero ordinates rather than inferred through a smooth local `dt/dn` conversion?

## Answer

Yes, over the tested first 40,000 loops.

Using the winding filled area of each zeta Argand loop and the actual zero-pair midpoint

`t_n = (gamma_n + gamma_{n+1}) / 2`,

a direct irregular-time Lomb-Scargle / least-squares spectral analysis reproduces the `log(m)` comb without any smooth time warp.

## Frozen calibration

Loops `1..20000`:

Primary dictionary `m=2..13`:

- observed score `3.897458739496102`;
- null q99 `1.4598759255330063`;
- empirical p `4.999750012499375e-05`;
- best common shift `0.0`.

Conservative dictionary `m=2..11`:

- observed score `4.041270022452432`;
- null q99 `1.5220835678441076`;
- empirical p `4.999750012499375e-05`;
- best common shift `0.0`.

## Frozen holdout

Loops `20001..40000`:

Primary dictionary `m=2..13`:

- observed score `3.4659735801364495`;
- null q99 `1.367251639628815`;
- empirical p `4.999750012499375e-05`;
- best common shift `0.0`.

Conservative dictionary `m=2..11`:

- observed score `3.6056592132518253`;
- null q99 `1.4396563906942155`;
- empirical p `4.999750012499375e-05`;
- best common shift `0.0`.

Thus the exact declared target locations themselves maximize the common-shift scan on both disjoint ranges and both target dictionaries.

## Matched direct-vs-smooth comparison

On loops `1..20000` the direct actual-time score exceeds the smooth-warp score by about `48.73%` for `m=2..13` and `47.32%` for `m=2..11`.

On loops `20001..40000` the direct score exceeds the smooth score by about `8.34%` and `8.69%`, respectively.

On the holdout both methods have best common shift exactly `0.0`; on calibration the smooth method differs only by one scan grid step `+0.00025`, while the direct method remains exactly zero.

## Strongest defensible conclusion

> The dominant `log(m)` spectral structure in the continuous filled-area observable survives direct use of the actual zero ordinates and therefore does not require the smooth blockwise time conversion used in RH-SOL-01/02.

The earlier smooth warp is best interpreted as an approximation/convenience, not as a necessary generator of the observed frequency alignment.

## What REALZERO removes

REALZERO rules out one specific artifact mechanism: that the `log(m)` alignment is produced merely by converting loop-index frequency to physical frequency through a smooth local `dt/dn` map.

## What REALZERO does not remove

REALZERO does not determine the causal origin of the comb. In particular, it does not yet rule out:

- generic geometric regularity of the loop-area sequence;
- ordering effects unrelated to arithmetic phase;
- phase-coherent artifacts preserved by actual zero ordering;
- null processes that preserve marginal geometry while destroying arithmetic assignment.

Those are the task of RH-SOL-04 FIREWALL.

## Handoff

Next module:

**RH-SOL-04 · FIREWALL — Falsification Tests for Arithmetic Spectra in Quantized Zeta Geometry.**

The central goal is no longer to ask whether the comb survives another representation change. It is to attempt to destroy the comb with controls that preserve as much non-arithmetic structure as possible while breaking the specific correspondence between geometry and arithmetic time/phase.
