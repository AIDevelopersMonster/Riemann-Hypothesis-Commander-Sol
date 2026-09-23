# HATTER-SOL 20–21 · CLAIM MATRIX

Status: **MANUSCRIPT CLAIM FREEZE v1**

## Central paper claim

\[
\boxed{
\text{Equivalent arithmetic presentations can produce measurably different
physical realizations, and exact algebraic structure can drive a
semantics-preserving compiler lowering to a lower-cost implementation.}
}
\]

## Claim inventory

| ID | Claim | Type | Evidence | Allowed? |
|---|---|---|---|---|
| H20-C1 | DIRECT/BALANCED/LINEAR implement the same strict-next-prime function for \(W=4..10\) | exact finite | SAT equivalence | yes |
| H20-C2 | The three presentations remain structurally distinct under the matched Boolean flow | finite empirical | Yosys/ABC \(W=4..10\) | yes |
| H20-C3 | DIRECT maps to hard memory while B/L remain logic on both tested FPGA families | finite cross-vendor | Cyclone V + Gowin | yes |
| H20-C4 | B/L crossover location is backend dependent on \(W=8..10\) | finite empirical | two-vendor P&R | yes |
| H20-C5 | H20 found a new prime invariant | unsupported | H20-EXT falsified | **no** |
| H21-C1 | Canonical \(B=0\) worlds satisfy \(x^n=C^{(n-1)/2}x\) | exact theorem | algebraic proof | yes |
| H21-C2 | The \(B=0\) H21 observer is exactly Euler-Jacobi in its nonzero defect coordinate | exact theorem | H21-EJ1/EJ2 | yes |
| H21-C3 | Scalar lowering preserves proper-factor gcd semantics | exact theorem | H21-EJ3 | yes |
| H21-C4 | Matched RTL is bit-exact on declared vectors | finite validation | LAB-27 | yes |
| H21-C5 | Scalar RTL has lower measured cycle count and generic cell count | finite implementation | LAB-27 | yes |
| H21-C6 | Scalar Cyclone V mapping uses 215 vs 328 ALMs, 251 vs 455 regs, and reaches 157.33 vs 123.20 MHz | device-specific | LAB-28 | yes |
| H21-C7 | ALM-latency ratio is 9.5852x in favor of scalar path for declared matched architecture | device-specific derived | LAB-27 + LAB-28 | yes |
| H21-C8 | The paper introduces a new Euler-Jacobi / Solovay-Strassen test | false claim | classical prior art | **no** |
| H21-C9 | The paper invents Lucas/Frobenius hardware | false claim | Le Masle et al. prior art | **no** |
| H21-C10 | 9.5852x is a universal FPGA advantage | unsupported | one target / matched core | **no** |
| H21-C11 | The H21 compiler is globally optimal | unsupported | no optimality theorem | **no** |
| H21-C12 | This is the first such architecture | unproved firstness | targeted audit only | **no** |

## Mandatory wording constraints

Use:

- "for the tested finite family";
- "under the declared matched flow";
- "on Cyclone V 5CEFA7F23C6";
- "semantics-preserving specialization/lowering";
- "targeted literature audit did not identify a direct analogue".

Avoid:

- "first";
- "optimal";
- "universal";
- "new primality test";
- "proves faster on FPGA in general";
- "prime structure invariant" for H20-EXT.

## H20-EXT rule

H20-EXT is cited only as a negative/falsification stage.

Its finite Walsh/continuation effects must not be promoted into the central
claim or abstract.

## Publication freeze

Further exploratory H21 coupling work must not change the central paper claim
unless it produces a separately audited theorem strong enough to justify a
new manuscript version.
