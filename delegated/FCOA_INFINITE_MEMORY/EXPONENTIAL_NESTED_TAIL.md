# Exponential Nested Tail — O(N log N) Arithmetic-Safe Primitive Memory

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Status:** theorem checkpoint, pending publication-hardening of the external QE citation  
**Scope:** infinite fixed-carrier branch only

## 1. Primitive source

Take the one-letter D0L morphism

\[
\sigma(A)=AA
\]

with seed word

\[
w=A.
\]

Then

\[
|\sigma^n(A)|=2^n.
\]

Let the generic carrier be

\[
G_\omega=\{Q_0,Q_1,Q_2,\ldots\}.
\]

Define one binary nested-tail relation

\[
\boxed{
R_\exp(Q_n,Q_m)
\iff
m\ge 2^n.
}
\]

Equivalently, with one terminal output \(\Omega\):

\[
Q_n\star Q_m=\Omega
\iff
R_\exp(Q_n,Q_m).
\]

The arithmetic expression \(2^n\) is used only to state the proved closed form. The primitive source rule is the index-blind morphism \(A\mapsto AA\).

---

## 2. FO recovery of the full order

For each source point define its row

\[
N(n)=\{Q_m:R_\exp(Q_n,Q_m)\}.
\]

Because

\[
2^n<2^k\iff n<k,
\]

we have

\[
n<k
\iff
N(k)\subsetneq N(n).
\]

Thus

\[
\boxed{
\operatorname{Less}(x,y):=
\forall z(R_\exp(y,z)\to R_\exp(x,z))
\wedge
\exists z(R_\exp(x,z)\wedge\neg R_\exp(y,z))
}
\]

defines the original strict carrier order.

Hence one binary relation and one terminal value already cross the FO order boundary.

---

## 3. Internal recovery of the exponential jump

Once \(<\) is available, the least element of the row of \(Q_n\) is definable:

\[
\operatorname{Jump}(x,y):=
R_\exp(x,y)
\wedge
\neg\exists z(\operatorname{Less}(z,y)\wedge R_\exp(x,z)).
\]

Therefore the structure is FO-interdefinable with

\[
(\mathbb N,<,e),
\qquad e(n)=2^n.
\]

under the external enumeration.

---

## 4. Exact incidence asymptotics

On the initial segment \(0,1,\ldots,N\), a row contributes iff

\[
2^n\le N.
\]

Let

\[
L=\lfloor\log_2 N\rfloor.
\]

Then

\[
C(N)
=\sum_{n=0}^{L}(N-2^n+1).
\]

Using

\[
\sum_{n=0}^{L}2^n=2^{L+1}-1,
\]

we obtain

\[
C(N)
=(L+1)(N+1)-(2^{L+1}-1).
\]

Hence

\[
\boxed{
C(N)=N\log_2N+O(N).
}
\]

In particular,

\[
\boxed{C(N)=\Theta(N\log N)=o(N^2).}
\]

This improves the previous certified quadratic-growth witness from \(\Theta(N^{3/2})\) to \(\Theta(N\log N)\).

---

## 5. Decidability / quantifier-elimination input

Published model-theoretic work on the structure

\[
(\mathbb N,<,e),
\qquad e(n)=2^n,
\]

gives a decidable complete theory and a quantifier-elimination analysis after the standard definitional expansion by successor/predecessor and the corresponding inverse-logarithm map.

The exact primary-source theorem and language conventions must be pinned down in the publication audit. The branch uses only the following consequence:

> unary definable sets in \((\mathbb N,<,2^x)\) have eventual behavior generated from finitely many order/exponential/logarithmic comparisons; in particular, the parity set is not definable.

This consequence is classical for this structure but remains an external theorem dependency, not a new FCOA theorem.

---

## 6. Addition does not leak

### Theorem EN-1

Ordinary external-index addition is not FO-definable in

\[
(G_\omega,R_\exp).
\]

### Proof

Assume addition were FO-definable. Then the unary parity predicate would be FO-definable by

\[
\operatorname{Even}(x)
\iff
\exists y\,(y+y=x).
\]

But by the published quantifier-elimination description of \((\mathbb N,<,2^x)\), parity is not definable in that structure. Since \((G_\omega,R_\exp)\) is FO-interdefinable with it, this is impossible. \(\square\)

Therefore

\[
\boxed{R_\exp\not\Rightarrow_{\rm FO}+.}
\]

---

## 7. Multiplication does not leak

### Theorem EN-2

Ordinary external-index multiplication is not FO-definable in

\[
(G_\omega,R_\exp).
\]

### Proof

The structure already defines discrete order and hence successor.

Julia Robinson proved that ordinary addition on the positive integers is first-order definable from multiplication together with successor.

Thus if multiplication were FO-definable in the exponential nested-tail structure, addition would also be FO-definable, contradicting Theorem EN-1. \(\square\)

Hence

\[
\boxed{
R_\exp\Rightarrow_{\rm FO}<,
\qquad
R_\exp\not\Rightarrow_{\rm FO}+,
\qquad
R_\exp\not\Rightarrow_{\rm FO}\times.
}
\]

---

## 8. Interaction with the previous barriers

The construction crosses every previously proved necessary boundary in exactly the expected way.

### Infinite nonlocal core

Each active row is an infinite tail. Hence every source point has infinitely many interaction partners and

\[
H=G_\omega.
\]

So the Sparse Memory Threshold is crossed.

### Order-only quadratic barrier

The relation is not FO-generated from pure order alone. Therefore the Order-Only Quadratic Barrier does not apply.

### Arithmetic leakage

Despite carrying more than pure order, the primitive skeleton remains below ordinary \(+\) and \(\times\) in FO expressive power.

Thus it occupies exactly the previously missing region:

\[
\boxed{
\text{subquadratic non-order global memory}
\quad+
\text{FO order}
\quad-
\text{FO arithmetic}.
}
\]

---

## 9. D0L optimality inside the nested-tail source class

Let a fixed D0L system have finite alphabet \(A\), seed \(w\), morphism \(\sigma\), and strictly increasing unbounded growth

\[
g(n)=|\sigma^n(w)|.
\]

Let

\[
B=\max_{a\in A}|\sigma(a)|.
\]

Then

\[
g(n)\le |w|B^n.
\]

Therefore for a constant \(c>0\), all

\[
0\le n\le c\log N
\]

have

\[
g(n)\le\sqrt N
\]

for sufficiently large \(N\). Each corresponding nested-tail row contributes at least

\[
N-\sqrt N
\]

incidences in the first \(N\) columns.

Consequently every unbounded strictly increasing D0L nested-tail skeleton satisfies

\[
\boxed{C(N)=\Omega(N\log N).}
\]

The duplication morphism attains

\[
\Theta(N\log N).
\]

Therefore:

### Theorem EN-3 — optimal D0L nested-tail density

\[
\boxed{\Theta(N\log N)}
\]

is asymptotically optimal among D0L-provenance nested-tail skeletons.

This is an internal theorem of the branch and does not depend on the external arithmetic-leakage citation.

---

## 10. Status

### Internal mathematics

- FO recovery of order: **proved**;
- incidence asymptotics \(\Theta(N\log N)\): **proved**;
- D0L-source provenance: **PASS under the declared gate**;
- D0L nested-tail \(\Omega(N\log N)\) lower bound: **proved**.

### External logical dependency

- addition nondefinability in \((\mathbb N,<,2^x)\): **supported by published QE/decidability theory, primary theorem citation to be publication-hardened**;
- multiplication nondefinability: follows from addition nondefinability plus Robinson once the former is locked.

Therefore the current branch classification is

\[
\boxed{
\text{EXPONENTIAL NESTED TAIL = theorem candidate with one literature-hardening obligation}.}
\]

It is already stronger asymptotically and cleaner in provenance than the quadratic substitution witness.