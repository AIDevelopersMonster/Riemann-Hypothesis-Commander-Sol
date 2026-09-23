# HATTER-SOL-21 · PRIOR-ART AUDIT 01

Status: **INITIAL TARGETED AUDIT / CLAIM NARROWING**

Date: 2026-09-22

This audit is deliberately conservative.  Its purpose is to identify which H21
ingredients are classical or directly adjacent to known work before any
publication claim is made.

## 1. Quadratic Frobenius probable-prime testing — established prior art

### Jon Grantham

- J. Grantham, "A Probable Prime Test with High Confidence",
  Journal of Number Theory 72 (1998), 32--47.
  DOI: 10.1006/jnth.1998.2247.
- J. Grantham, "Frobenius pseudoprimes",
  Mathematics of Computation 70 (2001), 873--891.
  DOI: 10.1090/S0025-5718-00-01197-2.

These works establish the quadratic-polynomial/Frobenius probable-prime
framework and a general finite-field view of Frobenius pseudoprimes.

Therefore H21 does **not** claim novelty for:

- using quadratic quotient algebras for primality observation;
- the prime-law Frobenius congruence itself;
- Jacobi/Legendre split versus inert behavior;
- reduction of quadratic Frobenius conditions to Lucas-type recurrences.

## 2. Lucas/Frobenius equivalence and strengthening — established prior art

Relevant references include:

- R. Baillie and S. S. Wagstaff Jr., "Lucas Pseudoprimes",
  Mathematics of Computation 35 (1980), 1391--1417.
  DOI: 10.1090/S0025-5718-1980-0583518-6.
- A. Rotkiewicz, "Lucas and Frobenius pseudoprimes",
  Annales Mathematicae Silesianae (2003).
- D. Loebenberger, "A Simple Derivation for the Frobenius Pseudoprime Test",
  IACR ePrint 2008/124.
- I. Damgard and G. S. Frandsen,
  "An Extended Quadratic Frobenius Primality Test with Average- and Worst-Case
  Error Estimate", Journal of Cryptology 19 (2006), 489--520.
  DOI: 10.1007/s00145-006-0332-x.

Therefore the H21 Lucas local-clock representation is a **representation
layer**, not a claim of a new Lucas/Frobenius identity.

## 3. Semiprime factor-local Frobenius structure — direct neighboring prior art

S. Khashin:

- "Counterexamples for Frobenius primality test",
  arXiv:1307.7920.
- "Evaluation of the Effectiveness of the Frobenius Primality Test",
  arXiv:1807.07249.

Khashin explicitly studies properties of prime divisors of Frobenius
pseudoprimes.  In the semiprime setting he derives local congruence conditions
modulo one prime factor in terms of the other cofactor, gcd consequences for
quadratic-algebra coefficients, and split-case relations involving the two
roots.

This is close to the early H21 cross-prime/Frobenius-defect mechanism.

### Claim consequence

H21 must **not** present as novel, by itself:

\[
pq
\to
\text{local Frobenius relation modulo }p,q
\to
\gcd\text{ factor information}.
\]

The H21 semiprime zero-mask theorem may remain useful as an exact formulation
for the declared observer architecture, but priority/novelty cannot rest on
the existence of factor-local Frobenius congruences.

## 4. Multiplicative order with prescribed trace — established field

Examples include:

- A. Tuxanidy and Q. Wang,
  "On the number of N-free elements with prescribed trace",
  Journal of Number Theory 160 (2016), 536--565.
  DOI: 10.1016/j.jnt.2015.09.008.

This and related finite-field literature study elements of prescribed
multiplicative order together with trace constraints, often through Gaussian
periods/character sums.

Therefore H21 does not claim that the general problem

\[
\text{multiplicative subgroup}\cap\text{trace level}
\]

is new.

The scalar-coset incidence theorem should be presented as a particularly simple
exact specialization tailored to the H21 two-dimensional observer.

## 5. Hilbert 90 / norm-one quotient / projective quadratic torus — classical

For a quadratic finite-field extension,

\[
\mathbf F_{p^2}^\times/\mathbf F_p^\times
\]

has order \(p+1\), and the map

\[
y\mapsto y/\tau(y)
\]

is the standard Hilbert-90/norm-one construction.

Therefore the following ingredients are classical consequences of finite-field
structure:

- projectivizing the multiplicative orbit modulo base-field scalars;
- the \(p+1\) norm-one/projective group in the inert case;
- norm identities;
- two-to-one behavior of squaring in even cyclic groups.

### Claim consequence

The theorem

\[
e_p=\operatorname{ord}(x/\tau(x))
\]

and the norm-square identity

\[
\lambda_p^2=(-C)^{e_p}
\]

are exact and useful, but should not be claimed as new finite-field theorems in
isolation.

The potentially H21-specific content is the way these identities compress the
declared zero-mask observer and world compiler.

## 6. Hardware prior art

A. Le Masle, W. Luk, C. A. Moritz,
"Parametrized hardware architectures for the Lucas primality test",
SAMOS 2011.
DOI: 10.1109/SAMOS.2011.6045453.

The paper reports parametrized Lucas-test hardware including Jacobi-symbol
hardware, pipelined modular arithmetic and scheduling.

Therefore H21 cannot claim novelty merely for putting Lucas/Frobenius
recurrences on FPGA.

A hardware publication claim must instead depend on a measured consequence of
the H21 mathematical representation, for example:

- eliminating provably silent worlds before synthesis/runtime;
- compiling world order from zero-mask information;
- replacing a full quadratic world datapath in the scheduler by
  projective/norm/lift metadata;
- demonstrating a nontrivial area-latency-energy advantage caused by that
  representation.

## 7. Current potentially distinctive H21 composition

The targeted audit did **not yet locate a direct prior analogue** of the complete
composition

\[
\boxed{
\text{multi-world arithmetic observer}
\to
\text{coordinate zero masks}
\to
\text{factor revelation}
\to
\text{world-quality compiler}
\to
\text{projective/scalar observer geometry}
\to
\text{norm-lift double cover}
\to
\text{adaptive/hardware world scheduling}.
}
\]

This absence from the current search is **not evidence of novelty by itself**.

It is only a justification for a deeper targeted audit of this combined
architecture.

## 8. Claims currently safe to make descriptively

Safe descriptive statements:

- H21 defines a specific multi-world observer architecture.
- Its local quadratic observer admits exact projective/scalar compression.
- In that representation, a local scalar coordinate is norm-determined up to
  at most one binary lift bit.
- The compiler heuristics and coupling decompositions have broad finite CI
  validation.
- The representation suggests concrete hardware pruning/compression
  experiments.

Unsafe at present:

- "new primality test";
- "new Frobenius factorization theorem" without qualification;
- "new finite-field trace/subgroup theorem";
- "new Lucas FPGA architecture";
- any claim that the full H21 composition is unprecedented.

## 9. Gate assessment after Audit 01

### Gate A — exact H21-specific mathematical core

\[
\boxed{\text{STRONG PARTIAL}}
\]

### Gate B — reproducibility

\[
\boxed{\text{PASS}}
\]

### Gate C — broad-family survival

\[
\boxed{\text{PASS}}
\]

### Gate D — prior-art audit

\[
\boxed{\text{PARTIAL / NOT PASSED}}
\]

The most important direct-overlap risk is Khashin's semiprime factor-local
Frobenius analysis.

### Gate E — publication-level contribution

\[
\boxed{\text{NOT YET}}
\]

The best remaining routes are:

1. a genuinely new theorem on reciprocal lift-bit sampling;
2. a nontrivial compiler theorem not reducible to generic probability;
3. a measured FPGA advantage caused specifically by H21 projective/norm
   compression.

## 10. Next audit targets

Search specifically for:

- factor extraction from individual Frobenius residual coordinates;
- projective quotient representations used to optimize Frobenius/Lucas tests;
- norm/square-root compression of quadratic Frobenius arithmetic;
- adaptive selection of multiple Frobenius/Lucas parameter worlds;
- hardware scheduling driven by algebraic world-quality statistics.
