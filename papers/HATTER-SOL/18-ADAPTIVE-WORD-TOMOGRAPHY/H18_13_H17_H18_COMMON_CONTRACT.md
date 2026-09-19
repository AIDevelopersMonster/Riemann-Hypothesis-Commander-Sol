# H18-13 · Common abstract contract for H17/H18 comparison

Status: **FORMAL COMPARISON CONTRACT DRAFT**

Date: 19 September 2026.

## 1. Purpose

H17 and H18 are not compared by claiming that their fault-tolerant RTL modules
compute one identical bit-level function.  They expose different fault
interfaces and different internal observation strategies.

The comparison is instead factored through a common finite abstract problem.

Let

\[
X = PSL(2,7)^2 / \sim
\]

be the simultaneous-conjugacy quotient of ordered pairs.  The frozen quotient
contains 197 states:

\[
197=114\text{ generating}+83\text{ non-generating}.
\]

Let

\[
Y=\{0,\ldots,113\}\cup\{\mathrm{REJECT}\}.
\]

Define the fault-free semantic map

\[
\Phi_0:X\to Y
\]

by

\[
\Phi_0(x)=
\begin{cases}
\operatorname{orbitID}(x), & x\text{ generating},\\
\mathrm{REJECT}, & x\text{ non-generating}.
\end{cases}
\]

This is the common E0 layer.

---

## 2. H17 fault presentation

H17-LAB-02 forms a fixed eight-coordinate class fingerprint

\[
F_8(x)=(q_1(x),\ldots,q_8(x)).
\]

The fault datum is a known erased coordinate

\[
e\in\{0,\ldots,7\},
\]

or no erasure.

The H17 correctness relation is

\[
\mathcal R_{17}
\subseteq
X\times F_{17}\times Y,
\]

where the implementation must recover the correct orbit ID or REJECT under its
certified one-known-coordinate-erasure model.

The fault acts on a **fixed observation vector**.

---

## 3. H18 fault presentation

H18 does not expose a fixed observation vector.  It implements an adaptive
strategy

\[
w_1\to c_1\to w_2(c_1)\to c_2\to\cdots
\]

over the restricted 12-query alphabet.

The fault datum is the identity of at most one persistently unavailable query,

\[
e\in Q_{12}\cup\{\varnothing\}.
\]

Once an erased query is encountered it remains banned for the rest of the
transaction.

The H18 correctness relation is

\[
\mathcal R_{18}
\subseteq
X\times F_{18}\times Y.
\]

The fault acts on an **adaptive query language**, not on a fixed coordinate
vector.

---

## 4. E0: exact common fault-free semantics

With no erasure,

\[
\boxed{
\Phi_{17,0}(x)=\Phi_{18,0}(x)=\Phi_0(x)
}
\]

for every one of the 197 quotient states, after the common output encoding is
fixed.

This is the strongest direct semantic comparison presently available.

Consequently, fault-free H17 and H18 can be viewed as two mathematical
factorizations of the same finite function.

---

## 5. E1: common fault-tolerant correctness contract

The fault spaces are not identical:

\[
F_{17}\neq F_{18}.
\]

Therefore no pointwise identity

\[
\Phi_{17}(x,f)=\Phi_{18}(x,f)
\]

is asserted for raw fault inputs.

Instead both satisfy the same abstract requirement:

> identify the simultaneous-conjugacy orbit of a generating pair, or return
> REJECT for a non-generating pair, while tolerating one fault in the
> observation mechanism under the declared known-erasure semantics of the
> presentation.

This is the E1 common-contract layer.

It is sufficient for a controlled comparison of the cost of two mathematical
fault-tolerant presentations, provided their different fault interfaces are
reported explicitly.

---

## 6. Architecture normalization for the mathematics-effect experiment

To compare mathematical presentations rather than temporal architecture, use
the same execution discipline:

\[
\Pi_{\rm one-cycle}:
\quad
\text{registered input}
\to
\text{combinational mathematical core}
\to
\text{registered output}.
\]

Then compare

\[
H17\text{-LAB-02}
\quad\text{against}\quad
H18\text{-LAB-04}.
\]

This does not make their internal mathematics identical.  It removes the
largest architecture confound: one-cycle spatial versus multi-cycle temporal
execution.

---

## 7. Separate same-mathematics architecture control

For H18 itself, compare

\[
H18\text{-LAB-03}
\quad\text{against}\quad
H18\text{-LAB-04}.
\]

Both are generated from the same restricted-12 H18-11 decision certificate.

The difference is execution discipline:

- LAB-03: temporal reuse of word/class hardware;
- LAB-04: full spatialization of observers and decision DAG.

This is therefore the clean architecture-effect control.

---

## 8. What the H17/H18 FPGA comparison can support

A matched FPGA result may support statements of the form:

> Under the same device, speed grade, Quartus version, timing reference and
> one-cycle registered discipline, the H18 presentation maps to a different
> area/depth/routing resource vector than the H17 presentation.

It does **not** by itself support:

- absolute mathematical complexity ordering;
- global circuit-size optimality;
- equality of the two raw fault interfaces;
- technology-independent superiority;
- a proof that any measured area ratio is an invariant.

---

## 9. Experimental hierarchy

The current comparison program has three orthogonal controls:

\[
\boxed{
\begin{aligned}
\text{mathematics effect}:&
\quad H17\text{-LAB-02}\leftrightarrow H18\text{-LAB-04},\\
\text{architecture effect}:&
\quad H18\text{-LAB-03}\leftrightarrow H18\text{-LAB-04},\\
\text{technology effect}:&
\quad \Theta_{\rm C4}\leftrightarrow\Theta_{\rm C5}.
\end{aligned}
}
\]

This three-axis decomposition is the methodological basis of the H18-12
hardware-image program.
