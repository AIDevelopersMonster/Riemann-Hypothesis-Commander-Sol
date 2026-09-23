# HATTER-SOL-21 · H21-LAB-27 RESULT

Status: **CI REPRODUCED / MEASURED RTL REPRESENTATION ADVANTAGE**

Run:

\`35741867585\`

Workflow:

\`H21 B0 RTL comparison\`

## 1. Functional equivalence

Two bit-exact sequential RTL implementations were compared:

1. compiled scalar Euler-Jacobi exponentiation
   \[
   C^{(n-1)/2}\bmod n;
   \]

2. uncompiled quadratic exponentiation
   \[
   x^n
   \]
   in
   \[
   x^2=C,
   \]
   implemented through a generic sequential quadratic multiplier.

Both use the same bit-serial modular multiplication design.

Test vectors:

\[
\boxed{9}.
\]

Functional mismatches:

\[
\boxed{0}.
\]

For every vector,

\[
q_0=0
\]

and

\[
q_1=\text{scalar result}.
\]

Thus the RTL preserves the exact H21-EJ1 observer equivalence.

## 2. Measured cycle result

Mean cycle ratio:

\[
\boxed{
\frac{C_{\rm quad}}{C_{\rm scalar}}
=
4.981273.
}
\]

Minimum:

\[
\boxed{4.666667}.
\]

Maximum:

\[
\boxed{5.400000}.
\]

Representative vectors:

| \(n\) | \(C\) | scalar cycles | quadratic cycles | ratio |
|---:|---:|---:|---:|---:|
| 101 | 3 | 105 | 567 | 5.4000 |
| 221 | 7 | 150 | 756 | 5.0400 |
| 899 | 5 | 165 | 819 | 4.9636 |
| 2047 | 3 | 270 | 1260 | 4.6667 |
| 3001 | 17 | 240 | 1134 | 4.7250 |

The measured controller-level ratio is somewhat larger than the idealized
base-modmul count ratio because every quadratic algebra multiplication incurs
additional sequential controller launch/wait overhead.

## 3. Generic Yosys synthesis

Flattened generic cell counts:

\[
\boxed{
N_{\rm scalar}=1428
}
\]

and

\[
\boxed{
N_{\rm quad}=2845.
}
\]

Therefore

\[
\boxed{
\frac{N_{\rm quad}}{N_{\rm scalar}}
=
1.992297.
}
\]

In this generic synthesis model the compiled scalar observer is therefore
approximately:

- \(5\times\) faster in cycle count;
- \(2\times\) smaller in flattened generic cell count.

## 4. What this establishes

H21 now has a measured end-to-end chain:

\[
\boxed{
B=0\text{ world descriptor}
\to
\text{exact Euler-Jacobi collapse}
\to
\text{compiler lowering}
\to
\text{bit-exact RTL}
\to
\text{measured cycle/cell reduction}.
}
\]

Unlike the factor-conditioned projective quantities \(e_p,d_p\), the compiler
predicate

\[
B=0
\]

is known before runtime and is directly synthesizable.

## 5. Claim boundary

This is **generic Yosys RTL evidence**, not yet a device-specific FPGA result.

No claim is made yet about:

- Cyclone V ALMs;
- FPGA Fmax;
- DSP/RAM use;
- actual dynamic power;
- energy.

Those require Quartus or equivalent technology mapping.

The base Euler-Jacobi/Solovay-Strassen arithmetic is classical.

The potentially distinctive engineering claim is the semantics-preserving
compiler lowering of a whole quadratic-world class inside the H21 multi-world
observer.
