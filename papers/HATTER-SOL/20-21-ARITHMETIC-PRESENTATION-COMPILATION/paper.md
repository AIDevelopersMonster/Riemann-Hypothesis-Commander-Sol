---
title: "HATTER-SOL 20-21: From Arithmetic Presentation Sensitivity to Semantics-Preserving World-Aware FPGA Compilation"
author:
  - "Author name to be inserted before archival release"
date: "2026-09-22"
bibliography: references.bib
link-citations: true
colorlinks: true
---

**Status:** first integrated manuscript draft  
**Scope:** architecture / compiler / arithmetic-observer paper  
**Publication claim:** conservative and device-bounded

---

## Abstract

Finite arithmetic functions admit many equivalent descriptions, but equivalent
semantics need not produce equivalent physical realizations.  HATTER-SOL 20
establishes this experimentally for the finite strict-next-prime function.
Three formally equivalent presentations—DIRECT lookup, a BALANCED threshold
tree, and a LINEAR threshold chain—remain structurally distinct after matched
Boolean synthesis for widths \(W=4,\dots,10\), and remain physically distinct
after place-and-route on both Intel/Altera Cyclone V and Gowin GW5A-25 devices.
The ordering of the logic-fabric implementations changes with width and backend,
showing that physical realization is an observer-dependent property of the
presentation rather than of the finite function alone.

HATTER-SOL 21 turns this observation into a constructive compilation rule.
For the quadratic arithmetic-world family

\[
A_n=(\mathbf Z/n\mathbf Z)[x]/(x^2-Bx-C),
\]

we prove that every canonical \(B=0\) descriptor collapses exactly to a scalar
Euler-Jacobi observer:

\[
x^n=C^{(n-1)/2}x.
\]

Consequently the generic quadratic defect is equivalent, including its
factor-gcd semantics, to the scalar congruence

\[
C^{(n-1)/2}
\equiv
\left(\frac Cn\right)
\pmod n.
\]

This gives a semantics-preserving compiler lowering from a generic quadratic
observer to a scalar modular-exponentiation datapath whenever the world
descriptor satisfies \(B=0\).

Matched sequential RTL using the same bit-serial modular multiplier confirms
bit-exact equivalence.  Generic synthesis yields a mean cycle ratio of about
\(4.98\times\) and a cell-count ratio of about \(1.99\times\) in favor of the
compiled scalar observer.  On Cyclone V 5CEFA7F23C6 under Quartus II 13.1, the
scalar implementation uses 215 ALMs and 251 registers at 157.33 MHz, versus
328 ALMs and 455 registers at 123.20 MHz for the matched quadratic
implementation.  Using the measured mean cycle counts, the corresponding mean
latencies are 1.112312 us and 6.988636 us, giving a \(9.5852\times\) advantage
in ALM-latency product for the tested architecture.

The paper does not introduce a new primality test, a new Euler-Jacobi
criterion, or a new Lucas/Frobenius algorithm.  Its contribution is the
end-to-end representation chain

\[
\boxed{
\text{presentation sensitivity}
\to
\text{exact arithmetic specialization}
\to
\text{compiler lowering}
\to
\text{measured FPGA consequence}.
}
\]

---

## 1. Introduction

Arithmetic hardware is usually specified from a mathematical function and then
optimized through a synthesis flow.  This hides two distinct questions.

First:

\[
\text{What function is computed?}
\]

Second:

\[
\text{How is that function presented to the implementation system?}
\]

The distinction is elementary, but it becomes operationally important whenever
multiple finite descriptions of the same arithmetic semantics induce different
Boolean or physical structures.

HATTER-SOL 20 was designed as a controlled test of this distinction.  The
arithmetic function was frozen, multiple presentations were proved equivalent,
and then the downstream structural and FPGA images were measured.  The result
was not a new prime theorem.  Instead, it was a reproducible observation that
the presentation remains visible to implementation observers after semantics
are fixed.

That result suggested a stronger question.  If presentation affects physical
geometry, can mathematics itself tell a compiler when one representation can
be replaced by a cheaper equivalent one?

HATTER-SOL 21 answers this constructively for one exact class of quadratic
arithmetic worlds.  The condition

\[
B=0
\]

is visible directly in the world descriptor.  It implies

\[
x^2=C,
\]

which collapses the generic quadratic exponentiation to a scalar
Euler-Jacobi computation.  The replacement preserves not only pass/fail
semantics but also the declared factor-extraction gcd.

The contribution is therefore not a new probable-prime criterion.  It is a
semantics-preserving specialization rule embedded in a world-aware arithmetic
compiler and followed through matched RTL to a concrete FPGA target.

The combined HATTER-SOL 20–21 paper has two parts:

1. **H20:** equivalent arithmetic presentations remain distinguishable under
   Boolean and physical observers;
2. **H21:** an algebraic descriptor can trigger an exact implementation
   lowering whose physical benefit is measurable.

The central narrative is

\[
\boxed{
\text{H20: presentation matters physically}
\Longrightarrow
\text{H21: compile the mathematics into the right presentation}.
}
\]

---

## 2. Scope and non-claims

The paper is deliberately narrow.

It does **not** claim:

- a new primality test;
- a new theorem about the distribution of primes;
- a new Euler-Jacobi or Solovay-Strassen criterion;
- a new Lucas or Frobenius probable-prime algorithm;
- an optimal circuit for next-prime;
- universal FPGA performance ratios;
- a first-ever use of specialization or partial evaluation in hardware;
- an implication for the Riemann hypothesis.

The valid claim is instead:

> Within the declared H20/H21 finite arithmetic observer framework, equivalent
> arithmetic presentations can induce different measured FPGA realizations,
> and an exact algebraic condition on the H21 world descriptor can be used to
> perform a semantics-preserving lowering to a lower-cost datapath.

All numerical FPGA claims are restricted to the declared device, toolchain,
RTL family and timing observer.

---

# Part I. HATTER-SOL 20 — Presentation transport

## 3. Frozen finite arithmetic function

For each input width \(W\), define the strict next-prime map

\[
S_W(x)
=
\min\{p>x:p\text{ prime}\},
\qquad
0\le x<2^W.
\]

Three source presentations are generated:

- \(D_W\): DIRECT complete lookup;
- \(B_W\): BALANCED threshold decision tree;
- \(L_W\): LINEAR ordered threshold chain.

The research variable is the presentation.  The arithmetic function is frozen.

Independent software models were checked over the full input range for
\(W=4,\dots,10\).

## 4. Formal semantic equivalence

A Yosys SAT miter proved

\[
\boxed{
D_W\equiv B_W\equiv L_W
}
\]

for every

\[
W=4,\dots,10.
\]

Hence the semantic observer produces one equivalence class:

\[
\boxed{
\mathcal P_W^{\rm sem}
=
\{\{D,B,L\}\}.
}
\]

Any later separation is therefore a representation effect under the declared
implementation observer, not a difference in arithmetic semantics.

## 5. Boolean synthesis separation

For a fair Boolean comparison, the DIRECT memory representation was expanded
with memory mapping before matched technology mapping and ABC-fast.

The resulting cell counts were:

| \(W\) | DIRECT | BALANCED | LINEAR |
|---:|---:|---:|---:|
| 4 | 18 | 26 | 37 |
| 5 | 35 | 56 | 75 |
| 6 | 56 | 112 | 158 |
| 7 | 93 | 175 | 292 |
| 8 | 156 | 315 | 562 |
| 9 | 243 | 588 | 1128 |
| 10 | 407 | 1079 | 2226 |

For every tested width,

\[
\boxed{
\mathrm{cells}(D_W)
<
\mathrm{cells}(B_W)
<
\mathrm{cells}(L_W).
}
\]

Thus the synthesis observer separates all three presentations:

\[
\boxed{
\mathcal P_W^{\rm ABC}
=
\{\{D\},\{B\},\{L\}\}.
}
\]

The empirical H20 statement is therefore

\[
\boxed{
\mathcal P_W^{\rm sem}
\ne
\mathcal P_W^{\rm ABC}
}
\]

on the tested width family.

This is not an optimality theorem.  It establishes only that the chosen
presentations remain structurally distinguishable after the matched flow.

## 6. Cyclone V physical realization

The first physical backend used:

- Intel/Altera Cyclone V 5CEFA7F23C6;
- Quartus II 13.1;
- registered shell;
- 100 MHz declared core clock.

For \(W=8,9,10\):

| W | Presentation | Physical class | ALM | Fmax |
|---:|---|---|---:|---:|
| 8 | DIRECT | M10K ROM | 3 | 496.03 MHz |
| 8 | BALANCED | logic | 78 | 210.17 MHz |
| 8 | LINEAR | logic | 48 | 254.13 MHz |
| 9 | DIRECT | M10K ROM | 5 | 527.15 MHz |
| 9 | BALANCED | logic | 139 | 149.08 MHz |
| 9 | LINEAR | logic | 140 | 133.80 MHz |
| 10 | DIRECT | M10K ROM | 6 | 338.29 MHz |
| 10 | BALANCED | logic | 276 | 122.44 MHz |
| 10 | LINEAR | logic | 293 | 111.35 MHz |

Among the two logic-fabric implementations,

\[
L_8<B_8,
\]

but

\[
B_9<L_9,
\qquad
B_{10}<L_{10}.
\]

The finite-width crossover therefore occurs between \(W=8\) and \(W=9\) under
this backend.

## 7. Gowin replication and shifted crossover

The second backend used:

- Gowin GW5A-LV25MG121NC1/I0;
- Gowin Education 1.9.9Beta-4.

Measured results:

| W | Presentation | Physical class | LUT | CLS | Fmax |
|---:|---|---|---:|---:|---:|
| 8 | DIRECT | BSRAM | 0 | 0 | 455.463 MHz |
| 8 | BALANCED | logic | 108 | 58 | 150.775 MHz |
| 8 | LINEAR | logic | 92 | 48 | 165.180 MHz |
| 9 | DIRECT | BSRAM | 0 | 0 | 565.494 MHz |
| 9 | BALANCED | logic | 190 | 99 | 129.124 MHz |
| 9 | LINEAR | logic | 185 | 101 | 133.955 MHz |
| 10 | DIRECT | BSRAM | 0 | 0 | 493.494 MHz |
| 10 | BALANCED | logic | 309 | 166 | 105.619 MHz |
| 10 | LINEAR | logic | 313 | 165 | 103.719 MHz |

The Gowin logic-fabric crossover occurs later:

\[
L_8<B_8,
\qquad
L_9<B_9,
\qquad
B_{10}<L_{10}
\]

under the primary LUT/timing comparison.

The crossover location is therefore backend dependent.

## 8. H20 conclusion: the physical observer is vector-valued

A scalar ranking is insufficient.  A physical observer should include at least

\[
O_{\rm phys}
=
(
\text{resource class},
\text{logic area},
\text{hard memory},
F_{\max},
\text{worst delay},
\text{logic depth},
\text{register topology}
).
\]

The stable qualitative result is that semantically equivalent arithmetic
presentations can occupy different physical resource classes and can exchange
ordering as width or backend changes.

H20 therefore motivates a compiler objective more precise than
"implement the formula":

\[
\boxed{
\text{choose a semantics-preserving presentation appropriate to the observer
and target backend}.
}
\]

## 9. Negative H20 extension

H20-EXT searched for a stronger prime-specific structural invariant using
continuation quotients, Walsh spectra and conditioned null models.

Several finite effects survived substantial controls, but the strongest
Walsh-energy candidate changed sign under stronger sieve conditioning and a
proposed cross-width conditioning crossover failed fresh hold-out tests.

H20-EXT was therefore closed with

\[
\boxed{\text{NO PAPER}.}
\]

This negative branch is not used as a positive result in the present
manuscript.  Its role is methodological: it shows that the programme discarded
observer-dependent effects that failed their own falsification gates.

---

# Part II. HATTER-SOL 21 — World-aware lowering

## 10. Quadratic arithmetic worlds

H21 considers the quadratic algebra

\[
A_n
=
(\mathbf Z/n\mathbf Z)[x]/(x^2-Bx-C)
\]

with descriptor

\[
W=(B,C,\Delta),
\qquad
\Delta=B^2+4C.
\]

For prime \(p\nmid 2C\Delta\), the quadratic Frobenius response is governed by
the quadratic character of \(\Delta\).  In the H21 observer, failure of the
expected Frobenius relation certifies compositeness, while proper gcds of defect
coordinates can expose factors.

This framework belongs to the classical Frobenius/Lucas probable-prime
territory; H21 does not claim otherwise.  The engineering question is how the
world descriptor should control the implementation.

## 11. Canonical \(B=0\) world class

For canonical fundamental discriminants

\[
D\equiv0\pmod4,
\]

the world presentation is

\[
B=0,
\qquad
C=D/4,
\]

so

\[
A_n
=
(\mathbf Z/n\mathbf Z)[x]/(x^2-C).
\]

Assume \(n\) odd and

\[
\gcd(n,C)=1.
\]

The condition \(B=0\) is known directly from the runtime world descriptor.
Unlike factor-conditioned local invariants, it can therefore be used by a
compiler before executing the observer.

## 12. Exact \(B=0\) collapse theorem

### Theorem 1 — scalar collapse

For every odd \(n\),

\[
\boxed{
x^n=C^{(n-1)/2}x
}
\]

inside

\[
A_n=(\mathbf Z/n\mathbf Z)[x]/(x^2-C).
\]

#### Proof

Since \(n\) is odd,

\[
x^n
=
x(x^2)^{(n-1)/2}
=
C^{(n-1)/2}x.
\]

\(\square\)

The conjugation satisfies

\[
\tau(x)=-x.
\]

Also,

\[
\left(\frac Dn\right)
=
\left(\frac{4C}{n}\right)
=
\left(\frac Cn\right).
\]

Therefore the complete quadratic defect has identically zero constant
coordinate:

\[
\boxed{
\delta_W(n)
=
\left(
0,\,
C^{(n-1)/2}
-
\left(\frac Cn\right)
\right)
\pmod n.
}
\]

### Corollary 1 — Euler-Jacobi equivalence

The quadratic world passes exactly when

\[
\boxed{
C^{(n-1)/2}
\equiv
\left(\frac Cn\right)
\pmod n.
}
\]

This is the classical Euler-Jacobi congruence underlying the
Solovay-Strassen test.

The novelty claim is not the congruence.  The result identifies the entire
canonical \(B=0\) H21 world class as a scalar observer embedded in the generic
quadratic representation.

### Corollary 2 — factor-observer preservation

The only nontrivial gcd projection is

\[
\boxed{
g
=
\gcd\left(
n,\,
C^{(n-1)/2}
-
\left(\frac Cn\right)
\right).
}
\]

Thus the lowered scalar observer and the unlowered quadratic observer expose
the same proper factor whenever

\[
1<g<n.
\]

The lowering therefore preserves the declared factor-observer semantics.

## 13. Compiler rule

The theorem yields a descriptor-level specialization:

\[
\boxed{
B=0
\Rightarrow
\text{scalar Euler-Jacobi datapath}
}
\]

and

\[
\boxed{
B\ne0
\Rightarrow
\text{generic quadratic datapath}.
}
\]

The compiler does not predict the factors of \(n\).  It merely selects a
semantically equivalent implementation from the algebraic presentation.

This distinction is central.  The compiler rule is available before executing
the candidate input and before any hidden factor information is known.

## 14. Operation-model consequence

Assume both datapaths share the same sequential modular multiplication
primitive.

A generic quadratic multiplication can be reduced to four base modular
multiplications in the declared general-multiplier architecture.

The scalar \(B=0\) observer instead performs an ordinary binary modular
exponentiation

\[
C^{(n-1)/2}\bmod n.
\]

Under the common operation model, both costs remain \(O(\log n)\), but the
quadratic representation carries a constant-factor arithmetic overhead.

This operation model is predictive only.  The hardware claims below come from
cycle-accurate RTL and technology mapping.

## 15. Matched RTL experiment

Two sequential RTL implementations were constructed:

1. scalar:
   \[
   C^{(n-1)/2}\bmod n;
   \]

2. quadratic:
   \[
   x^n
   \]
   in
   \[
   x^2=C.
   \]

Both use the same bit-serial base modular multiplier.

Nine test vectors produced zero functional mismatches.  In every case, the
quadratic result satisfied

\[
q_0=0,
\qquad
q_1=\text{scalar result}.
\]

Thus the RTL experiment matches Theorem 1 exactly.

Measured controller-level cycle ratio:

\[
\boxed{
\frac{C_{\rm quad}}{C_{\rm scalar}}
=
4.981273
}
\]

on average.

The observed range was

\[
4.666667
\le
\frac{C_{\rm quad}}{C_{\rm scalar}}
\le
5.400000.
\]

Generic flattened Yosys cell counts were

\[
N_{\rm scalar}=1428,
\]

\[
N_{\rm quad}=2845,
\]

giving

\[
\boxed{
\frac{N_{\rm quad}}{N_{\rm scalar}}
=
1.992297.
}
\]

## 16. Cyclone V device result

The decisive physical comparison used:

- Cyclone V 5CEFA7F23C6;
- Quartus II 13.1.0 Build 162;
- identical LAB-27 RTL;
- matched sequential base multiplier;
- 100 MHz core clock constraint.

Both designs completed synthesis, fitting, assembly and TimeQuest.

### 16.1 Utilization

| metric | scalar | quadratic | ratio quadratic/scalar |
|---|---:|---:|---:|
| ALMs | 215 | 328 | 1.5256 |
| registers | 251 | 455 | 1.8127 |
| DSP | 0 | 0 | — |

The scalar design therefore uses approximately

\[
34.45\%
\]

fewer ALMs and

\[
44.84\%
\]

fewer registers.

### 16.2 Fmax

At Slow 1100 mV, 85 C:

\[
F_{\max,\rm scalar}=157.33\ \mathrm{MHz},
\]

\[
F_{\max,\rm quad}=123.20\ \mathrm{MHz}.
\]

Thus

\[
\boxed{
\frac{F_{\max,\rm scalar}}
{F_{\max,\rm quad}}
=
1.2770.
}
\]

Both implementations have positive register-to-register setup margin at the
declared 100 MHz clock.

### 16.3 Mean latency

Using authoritative LAB-27 mean cycle counts

\[
\bar C_{\rm scalar}=175,
\qquad
\bar C_{\rm quad}=861,
\]

the Fmax-derived mean latencies are

\[
\boxed{
T_{\rm scalar}=1.112312\ \mu s
}
\]

and

\[
\boxed{
T_{\rm quad}=6.988636\ \mu s.
}
\]

Hence

\[
\boxed{
\frac{T_{\rm quad}}
{T_{\rm scalar}}
=
6.2830.
}
\]

### 16.4 Area-latency product

\[
AT_{\rm scalar}
=
215\times1.112312
=
239.147016\ \mathrm{ALM}\cdot\mu s,
\]

\[
AT_{\rm quad}
=
328\times6.988636
=
2292.272727\ \mathrm{ALM}\cdot\mu s.
\]

Therefore

\[
\boxed{
\frac{AT_{\rm quad}}
{AT_{\rm scalar}}
=
9.5852.
}
\]

This is the strongest device-specific engineering result of H21.

It is valid for the declared matched architecture and target, not as a
universal FPGA ratio.

---

## 17. H20–H21 synthesis

H20 and H21 answer different levels of the same question.

### H20

Given fixed arithmetic semantics and several equivalent presentations:

\[
\boxed{
\text{does presentation remain visible downstream?}
}
\]

For the measured finite next-prime family, yes.

### H21

Given an algebraic world descriptor:

\[
\boxed{
\text{can mathematics select an equivalent cheaper presentation?}
}
\]

For canonical \(B=0\) quadratic worlds, yes.

The combined result is therefore stronger than either part alone.

H20 shows why presentation is worth treating as a first-class implementation
variable.

H21 shows that an exact algebraic theorem can drive the choice of that
presentation automatically.

The complete chain is

\[
\boxed{
\text{semantic object}
\to
\text{presentation}
\to
\text{observer geometry}
\to
\text{algebraic specialization}
\to
\text{compiler lowering}
\to
\text{physical image}.
}
\]

---

## 18. Related work and claim boundary

### 18.1 Euler-Jacobi / Solovay-Strassen

The scalar congruence used after the \(B=0\) lowering is classical.
Solovay and Strassen introduced the well-known Monte-Carlo primality test based [@solovay1977]
on comparing

\[
a^{(n-1)/2}
\]

with the Jacobi symbol.

H21 does not claim this criterion.

### 18.2 Frobenius and Lucas probable-prime tests

Frobenius and Lucas tests provide an established framework in which polynomial
or recurrence behavior modulo \(n\) is compared with prime-field behavior.
Grantham's Frobenius-pseudoprime framework is part of this literature [@grantham2001].

H21's quadratic world observer lies in this established territory.

### 18.3 Lucas hardware

Le Masle, Luk and Moritz presented parameterized hardware for the Lucas primality test, including Jacobi computation, modular arithmetic and sequence scheduling [@lemasle2011].

Accordingly, the present paper does not claim the invention of Lucas/Jacobi
hardware.

### 18.4 Hardware specialization

Partial evaluation and parameter specialization are established hardware compiler techniques. AnyHLS, for example, uses partial evaluation to specialize high-level hardware descriptions before vendor-specific HLS code generation [@ozkan2020].

The present claim is narrower: the specialization predicate and replacement
datapath are derived from an exact arithmetic identity inside the declared H21
world family, and the complete semantic-to-device chain is validated.

### 18.5 Conservative novelty statement

Targeted literature review found adjacent work in primality-test hardware,
Frobenius/Lucas arithmetic and hardware specialization, but no direct analogue
of the exact chain

\[
\boxed{
B=0\text{ quadratic-world descriptor}
\to
\text{observer-preserving Euler-Jacobi lowering}
\to
\text{matched FPGA comparison}.
}
\]

Absence from a targeted search is not proof of firstness.  The manuscript
therefore avoids "first", "novel primality test", "optimal" and universal
hardware claims.

---

## 19. Limitations

### H20 limitations

The H20 presentation results are finite and flow-specific.

They do not establish:

- minimum circuit complexity;
- asymptotic ordering;
- universal crossover widths;
- backend invariants.

### H21 limitations

The Cyclone V experiment is a matched core comparison rather than complete
board-level timing sign-off.

The projects intentionally omit exact physical pin assignments and full
external I/O constraints.

The safe hardware claims are restricted to:

- mapped logic utilization;
- internal clock-domain timing;
- measured cycle counts;
- Fmax-derived latency;
- area-latency comparison.

No power or energy result is claimed.

### Mathematical limitations

The \(B=0\) lowering applies to the declared canonical world class.

It does not imply that all quadratic worlds admit scalar reductions.

The deeper H21 reciprocal-coupling programme remains an active research branch
and is not required for the present architecture/compiler paper.

---

## 20. Reproducibility

The repository contains:

### H20

- generated DIRECT/BALANCED/LINEAR RTL;
- Python reference models;
- formal Yosys SAT equivalence;
- matched Yosys synthesis scripts;
- Cyclone V Quartus scripts and reports;
- Gowin scripts and reports.

### H21

- exact theorem documents;
- software validation laboratories;
- matched scalar/quadratic RTL;
- LAB-27 simulation and generic synthesis workflow;
- LAB-28 Cyclone V scripts and reports;
- publication-gate and prior-art audits.

The decisive H21 physical target is

\[
\boxed{\text{5CEFA7F23C6}}
\]

under

\[
\boxed{\text{Quartus II 13.1.0 Build 162}}.
\]

The manuscript should be released with the exact repository commit used for
the final tables.

---

## 21. Conclusion

HATTER-SOL 20 established that presentation is experimentally visible after
arithmetic semantics are frozen.  The same strict-next-prime function, encoded
in three formally equivalent ways, produced distinct Boolean and FPGA
realizations; the physical ordering even changed with width and backend.

HATTER-SOL 21 converted that observation into a compiler action.  For canonical
quadratic worlds with \(B=0\), the algebra itself proves that the generic
quadratic observer is redundant and can be replaced by a scalar Euler-Jacobi
observer without changing the factor-gcd semantics.

The resulting specialization is not only symbolic.  It survives software
validation, matched RTL, generic synthesis and Cyclone V technology mapping.
On the tested device and architecture, the lowered implementation uses fewer
ALMs and registers, reaches higher Fmax, and reduces the ALM-latency product by
a factor of

\[
\boxed{9.5852}.
\]

The combined lesson is:

\[
\boxed{
\text{representation is a physical design variable, and exact arithmetic
structure can be used to compile that variable rather than merely observe it.}
}
\]

---

## References

::: {#refs}
:::
