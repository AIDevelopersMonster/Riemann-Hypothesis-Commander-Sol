# HATTER-SOL-21 · PRIOR-ART AUDIT 03

Status: **HARDWARE / COMPILER CLAIM AUDIT**

Date: 2026-09-22

## 1. Classical components confirmed

### Solovay-Strassen / Euler-Jacobi

Solovay and Strassen's classical test evaluates

\[
a^{(n-1)/2}
\]

and compares it with the Jacobi symbol

\[
\left(\frac an\right).
\]

Therefore H21-EJ1 is not a new primality test.

### Lucas hardware

Le Masle, Luk and Moritz,
"Parametrized hardware architectures for the Lucas primality test",
SAMOS 2011,
DOI 10.1109/SAMOS.2011.6045453,

gives a parameterized Lucas primality-test hardware architecture, including
Jacobi hardware, modular arithmetic, dependence analysis and scheduling.

Therefore H21 does not claim novelty for:

- Lucas hardware;
- Jacobi hardware;
- modular add/shift arithmetic;
- parameterized arithmetic controllers.

### Separate primality-test comparison

Existing engineering work compares implementations of multiple primality tests,
including Solovay-Strassen, quadratic Frobenius and Lucas tests.

Therefore simply placing several test implementations side by side is not a
novel architecture claim.

## 2. Search target

The specific H21 question is narrower:

> Given a single parameterized quadratic-world observer family
>
> \[
> A_n=(\mathbf Z/n\mathbf Z)[x]/(x^2-Bx-C),
> \]
>
> does an architecture/compiler automatically identify the descriptor class
> \(B=0\), prove semantic equivalence to an Euler-Jacobi observer, lower it to a
> scalar datapath, and retain the generic quadratic datapath only for the
> remaining descriptors?

The initial targeted search did not locate a direct published analogue of this
complete compiler lowering.

This absence is **not proof of novelty**.

## 3. H21 measured evidence

H21-LAB-27 supplies a concrete representation consequence using identical
base modular-multiplier RTL:

\[
\boxed{
4.981\times
}
\]

mean cycle reduction and

\[
\boxed{
1.992\times
}
\]

generic flattened-cell reduction for the compiled \(B=0\) path.

This is stronger evidence than a standalone operation-count argument.

## 4. Remaining prior-art risk

Potentially adjacent concepts still requiring examination include:

- algebraic compiler specialization / partial evaluation of arithmetic
  datapaths;
- mixed or heterogeneous primality-test accelerators;
- Lucas tests augmented by Euler-Jacobi congruences;
- parameter-specialized polynomial/Frobenius exponentiation hardware;
- common-subexpression specialization where a polynomial relation collapses
  algebra dimension.

## 5. Safe current claim

A conservative claim is:

\[
\boxed{
\text{H21 provides a semantics-preserving specialization rule for its declared
quadratic world family: canonical }B=0\text{ worlds lower exactly to scalar
Euler-Jacobi observers.}
}
\]

And experimentally:

\[
\boxed{
\text{the specialization substantially reduces cycles and generic RTL cells in
the declared shared-modmult architecture.}
}
\]

Unsafe without further audit:

- "first hardware architecture";
- "new Euler-Jacobi algorithm";
- "new quadratic Frobenius algorithm";
- "first heterogeneous primality accelerator";
- universal FPGA speed/area factors.

## 6. Publication gate consequence

This audit plus LAB-27 materially advances the engineering publication route.

The remaining evidence needed for a strong hardware claim is device-specific
technology mapping, preferably on the already-used Cyclone V flow:

- ALMs;
- registers;
- Fmax;
- latency/cycles;
- optional area×latency metric.

A device-specific result preserving the large generic RTL gap would justify a
publication re-evaluation.
