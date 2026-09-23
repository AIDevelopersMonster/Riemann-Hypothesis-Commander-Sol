# HATTER-SOL-21 · PRIOR-ART AUDIT 04

Status: **FINAL CONSERVATIVE ARCHITECTURE-CLAIM AUDIT**

Date: 2026-09-22

## 1. Prior art that must be acknowledged

### Lucas primality hardware

Le Masle, Luk and Moritz,
"Parametrized hardware architectures for the Lucas primality test",
SAMOS 2011,
DOI 10.1109/SAMOS.2011.6045453.

This work already establishes parameterized Lucas primality-test hardware,
including Jacobi hardware, modular arithmetic and scheduling.

Therefore H21 does not claim invention of Lucas/Jacobi hardware.

### Hardware specialization / partial evaluation

Özkan et al.,
"AnyHLS: High-Level Synthesis with Partial Evaluation",
IEEE TCAD 39(11), 2020,
DOI 10.1109/TCAD.2020.3012172.

More generally, partial evaluation and specialization of hardware descriptions
are established compiler techniques.

Therefore H21 does not claim invention of hardware specialization, partial
evaluation, or parameter-specialized FPGA datapaths.

### Classical Euler-Jacobi and Frobenius/Lucas arithmetic

Solovay-Strassen / Euler-Jacobi and quadratic Frobenius/Lucas probable-prime
machinery are classical.

Therefore H21 does not claim a new primality test.

## 2. Claim that remains specific to H21

The publication claim is deliberately narrower:

> Inside the declared H21 quadratic-world observer family
>
> \[
> A_n=(\mathbf Z/n\mathbf Z)[x]/(x^2-Bx-C),
> \]
>
> canonical \(B=0\) descriptors admit an exact semantics-preserving lowering
> from the generic quadratic observer to a scalar Euler-Jacobi datapath,
> while preserving the observer's factor-gcd semantics.

The contribution is the complete chain:

\[
\boxed{
\text{world descriptor}
\to
\text{exact specialization theorem}
\to
\text{compiler rule}
\to
\text{matched RTL}
\to
\text{measured Cyclone V consequence}.
}
\]

Targeted searches found adjacent work in Lucas hardware and generic hardware
partial evaluation, but no direct analogue of this exact H21 observer-family
specialization plus matched FPGA comparison.

Absence from targeted search is not proof of firstness.

## 3. LAB-28 strengthens the engineering claim

On Cyclone V 5CEFA7F23C6:

- scalar: 215 ALMs, 251 registers, 157.33 MHz;
- quadratic: 328 ALMs, 455 registers, 123.20 MHz;
- both use 0 DSP blocks;
- mean latency ratio quadratic/scalar:
  \[
  6.2830\times;
  \]
- ALM-latency ratio quadratic/scalar:
  \[
  9.5852\times.
  \]

Thus the specialization has a material technology-mapped consequence and is
not merely symbolic simplification.

## 4. Safe manuscript language

Safe:

\[
\boxed{
\text{We derive and validate a semantics-preserving specialization rule for
canonical }B=0\text{ descriptors in the H21 quadratic-world observer family,
and show a substantial matched Cyclone V implementation benefit.}
}
\]

Also safe:

- "in our matched architecture";
- "on the tested Cyclone V target";
- "our targeted literature audit did not identify a direct analogue".

Avoid:

- "first";
- "new Euler-Jacobi algorithm";
- "new Lucas/Frobenius test";
- "universal FPGA improvement";
- "optimal implementation".

## 5. Audit decision

For the conservative architecture-paper claim set:

\[
\boxed{\text{PRIOR-ART GATE: PASS WITH CLAIM NARROWING}}
\]

This is not a patent-style novelty opinion and not evidence of absolute
firstness.

It is sufficient for a carefully bounded research manuscript.
