# HATTER-SOL-21 · PUBLICATION GATE

Status: **ACTIVE MONITOR**

Updated after H21-LAB-27, PRIOR-ART AUDIT 03, and preparation of H21-LAB-28.

## Gate A — exact H21-specific mathematical core

\[
\boxed{\text{PASS FOR AN ARCHITECTURE PAPER CLAIM SET}}
\]

The claim set is deliberately narrow.

The central runtime-safe theorem is:

\[
\boxed{
B=0
\Longrightarrow
\delta_W(n)=
\left(
0,\,
C^{(n-1)/2}-\left(\frac Cn\right)
\right),
}
\]

so the canonical \(B=0\) quadratic-world observer lowers exactly to a scalar
Euler-Jacobi observer while preserving factor-gcd semantics.

Earlier projective/norm results remain supporting analysis, not novelty claims,
because Audits 01--02 found strong classical overlap.

## Gate B — independent reproducible validation

\[
\boxed{\text{PASS}}
\]

Evidence includes:

- H21-LAB-25:
  \[
  2,762,496
  \]
  quadratic/scalar equivalence checks and the same number of factor-gcd checks,
  with zero failures;

- H21-LAB-27:
  bit-exact Icarus simulation with zero mismatches;

- generic Yosys synthesis of both matched RTL cores.

## Gate C — broad-family / operational nontriviality

\[
\boxed{\text{PASS}}
\]

The \(B=0\) rule applies to the entire canonical even-discriminant world class,
not a hand-selected descriptor.

The broader world-compiler experiments also survive common-core and held-out
range controls, although their scheduling gain is modest.

## Gate D — novelty / prior-art audit

\[
\boxed{\text{PARTIAL / CLAIM NARROWED}}
\]

Established prior art includes:

- Solovay-Strassen / Euler-Jacobi;
- Lucas/Frobenius tests;
- norm-one / root-ratio Lucas structure;
- semiprime local Frobenius conditions;
- Lucas FPGA hardware.

The current potentially distinctive engineering claim is **not** any of those
ingredients.

It is the semantics-preserving compiler lowering inside a declared
parameterized quadratic-world observer family:

\[
\boxed{
B=0\to\text{scalar Euler-Jacobi datapath},
\qquad
B\ne0\to\text{quadratic datapath}.
}
\]

Audit 03 did not locate a direct published analogue of this exact lowering plus
matched hardware comparison, but absence from the search is not proof of
novelty.

A final literature check remains required before manuscript submission.

## Gate E — publication-level contribution

\[
\boxed{\text{CONDITIONAL PASS — PENDING DEVICE-SPECIFIC LAB-28}}
\]

H21-LAB-27 measured, using the same sequential base modular multiplier:

\[
\boxed{
4.981273\times
}
\]

mean cycle reduction and

\[
\boxed{
1.992297\times
}
\]

generic flattened-cell reduction for the compiled scalar \(B=0\) observer.

This is a material measured representation consequence.

The remaining condition is technology mapping on the matched Cyclone V flow:

- ALMs;
- registers;
- DSPs;
- Fmax;
- area×cycle metric.

LAB-28 is prepared for Quartus II 13.1 and target

\[
5CEFA7F23C6.
\]

## Gate F — manuscript architecture

\[
\boxed{\text{READY TO FREEZE}}
\]

Recommended paper spine:

1. H21 world-observer problem and claim boundary;
2. canonical quadratic world family;
3. exact \(B=0\) Euler-Jacobi collapse theorem;
4. semantics-preserving world compiler;
5. exhaustive software equivalence;
6. matched shared-modmult RTL architecture;
7. generic Yosys cycle/cell result;
8. Cyclone V matched result;
9. broader scheduling experiments as secondary evidence;
10. conservative prior-art and non-claims.

## Decision

\[
\boxed{\text{PUBLICATION THRESHOLD: HOLD FOR LAB-28}}
\]

This is no longer a request for another exploratory theorem.

If LAB-28 preserves a substantial device-level benefit without functional or
timing pathologies, the H21 architecture-paper publication threshold should be
considered crossed, subject only to final claim/bibliography audit.


## Immediate engineering trigger — LAB-28

The next decisive engineering gate is:

\[
\boxed{
\text{Cyclone V technology-mapped comparison of unchanged LAB-27 RTL}
}
\]

for target

\[
5CEFA7F23C6
\]

under Quartus II 13.1.

If both scalar and quadratic cores FIT and the compiled \(B=0\) path preserves a material advantage in:

- ALMs;
- measured latency
  \[
  \text{cycles}/F_{\max};
  \]
- and area-latency
  \[
  \text{ALM}\times\text{latency},
  \]

then Gate E must be re-evaluated immediately against PRIOR-ART AUDIT 03.

The strongest safe claim candidate would be:

\[
\boxed{
\text{semantics-preserving compiler lowering of canonical }B=0\text{ quadratic worlds to a scalar Euler-Jacobi datapath yields a measured device-specific implementation advantage.}
}
\]

This trigger does not authorize claims of a new Euler-Jacobi algorithm, a new
Lucas algorithm, or universal FPGA speedup.
