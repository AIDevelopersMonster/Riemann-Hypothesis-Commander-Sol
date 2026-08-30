# FCOA Hybrid Memory — Bounded-Depth Resource Separation

**Status:** conditional separation theorem in an explicit radix normal form  
**Scope:** post-Article-A resource theory; not an unrestricted FO lower bound

## 1. Motivation

Unrestricted linear-size encodings collapse the memory exponents of AL0, AL1 and AL2 because arithmetic can be factorized into more and more digit levels. The remaining question is whether a genuine separation appears once the amount of factorization is bounded.

The answer is yes in a natural **bottom-law radix normal form**.

The key distinction is simple:

- order on a bottom digit alphabet needs only a sparse unary/chain organization of the alphabet;
- addition or multiplication needs a total binary local law on all ordered pairs of bottom digits unless further factorization below that level is allowed.

This creates an exponent gap at every fixed factorization depth.

---

## 2. Depth-d binary radix normal form

Fix an integer

\[
d\ge1.
\]

Let

\[
k=2^d
\]

be the number of bottom digit positions.

For an `N`-point target sector choose a bottom alphabet `D_N` of size

\[
s_N\asymp N^{1/k}=N^{1/2^d}.
\]

Represent every target point by a fixed `k`-tuple of bottom digits. Thus

\[
|D_N|^k\asymp N.
\]

The target-to-digit attachment cost is

\[
Theta(kN)=Theta(N)
\]

because `d` and hence `k` are fixed.

### Bottom-law prohibition

The bottom alphabet is **primitive**: no further tuple/radix decomposition of elements of `D_N` is permitted.

A bottom binary law is represented extensionally by bounded-arity records. Therefore a total binary functional law on `D_N^2` uses one record per ordered input pair up to a fixed compilation factor.

This is the normal-form restriction that makes the theorem nontrivial.

---

## 3. Internal resource measure

Let

\[
M_{bot}
\]

denote the number of primitive records whose purpose is to organize the bottom digit alphabet and its local laws.

Target coordinate attachments are not counted in `M_bot`; they remain `Theta(N)` for every phase.

We compare the minimum asymptotic `M_bot` required for exact AL0, AL1 and AL2 within the depth-`d` normal form.

---

## 4. AL0 upper bound

Put a directed chain on the bottom alphabet:

\[
d_0\to d_1\to\cdots\to d_{s-1}.
\]

This uses

\[
Theta(s_N)
\]

bottom records.

The chain gives the bottom digit order uniformly. The target order is then lexicographic on the fixed `k` digit positions.

Since `k` is fixed, a single FO formula compares the first coordinate at which two target tuples differ.

Hence

\[
\boxed{
M_{bot}(AL0)=O(s_N)=O\left(N^{1/2^d}\right).
}
\]

---

## 5. AL0 lower bound inside the normal form

Suppose the bottom alphabet has `s_N` points but fewer than `c s_N` nontrivial bounded-arity bottom records, for sufficiently small fixed `c` depending only on the signature arity.

Each record touches only a bounded number of digit points. With `o(s_N)` bottom records, at least two bottom digits are untouched by any nontrivial bottom relation and remain exchangeable.

Because target coordinates range over all bottom digits in the radix representation, exchanging these two digit values induces a nontrivial symmetry of the target coordinate system and prevents a uniformly recovered strict lexicographic order.

Therefore

\[
\boxed{
M_{bot}(AL0)=Omega(s_N).
}
\]

Combining with the chain construction:

\[
\boxed{
M_{bot}(AL0)=Theta\left(N^{1/2^d}\right).
}
\]

This is a normal-form lower bound based on direct bottom-alphabet incidence; it is not claimed for arbitrary FO encodings outside the model.

---

## 6. AL1 upper bound

Store a complete bottom-digit add-with-carry law

\[
A(a,b;c,r),
\]

where `a,b,r in D_N` and `c` belongs to a fixed bounded carry set.

There is one output pair `(c,r)` for every ordered input pair `(a,b)`. Therefore

\[
|A|=Theta(s_N^2).
\]

School addition across the fixed `k=2^d` digit positions uses only `O(k)` carry witnesses and is uniformly FO definable.

Thus

\[
\boxed{
M_{bot}(AL1)=O(s_N^2)
=O\left(N^{2/2^d}\right).
}
\]

---

## 7. AL1 lower bound inside the extensional bottom-law model

In this normal form, the primitive bottom layer is required to supply the exact local result for **every ordered pair** of bottom digits, and no further decomposition of a bottom digit is allowed.

A deterministic total binary local law therefore has domain `D_N^2`, of cardinality

\[
s_N^2.
\]

Under extensional bounded-size record representation, each primitive record can certify only `O(1)` input pairs. Hence any complete bottom addition law requires

\[
Omega(s_N^2)
\]

records.

Therefore

\[
\boxed{
M_{bot}(AL1)=Theta\left(N^{2/2^d}\right).
}
\]

This is deliberately a normal-form theorem: intensional shortcuts, additional algebraic primitives, or another factorization level are outside the hypothesis.

---

## 8. AL2 upper bound

Store a complete bottom multiply-and-split law

\[
P(a,b;h,r)
\iff
ab=hs_N+r.
\]

Again one record is needed per ordered bottom-digit pair, so

\[
|P|=Theta(s_N^2).
\]

Together with bottom add-with-carry, fixed-`k` school multiplication is uniformly FO definable using `O(k^2)` local products and a constant-size carry network relative to `N`.

Hence

\[
\boxed{
M_{bot}(AL2)=O(s_N^2)
=O\left(N^{2/2^d}\right).
}
\]

---

## 9. AL2 lower bound inside the extensional bottom-law model

The same extensional completeness argument applies. Exact school multiplication requires the primitive bottom layer to determine the split product for every ordered pair

\[
(a,b)\in D_N^2.
\]

With no lower factorization and bounded-size records, covering all input pairs requires

\[
Omega(s_N^2)
\]

primitive bottom-law records.

Therefore

\[
\boxed{
M_{bot}(AL2)=Theta\left(N^{2/2^d}\right).
}
\]

Within this normal form, AL1 and AL2 have the same bottom-memory exponent; their distinction is semantic/algebraic rather than asymptotic at fixed depth.

---

## 10. Bounded-Depth Separation Theorem

### Theorem HM-BDRS

In the depth-`d` binary radix normal form with primitive bottom alphabet, extensional bounded-arity bottom laws and no further bottom factorization,

\[
\boxed{
M_{bot}(AL0)
=Theta\left(N^{1/2^d}\right)
}
\]

while

\[
\boxed{
M_{bot}(AL1)
=M_{bot}(AL2)
=Theta\left(N^{2/2^d}\right).
}
\]

Hence for every fixed depth `d`, arithmetic transport has twice the bottom-memory exponent of pure order:

\[
\boxed{
\lambda_d(AL1)=\lambda_d(AL2)=2\lambda_d(AL0).
}
\]

This is the first positive resource separation in the SOL-HYBRID search that survives once the permitted amount of factorization is explicitly fixed.

---

## 11. Examples

### Depth d=1

Two bottom digits, each alphabet of size `N^{1/2}`:

\[
AL0:\Theta(N^{1/2}),
\qquad
AL1,AL2:\Theta(N).
\]

### Depth d=2

Four bottom digits, alphabet size `N^{1/4}`:

\[
AL0:\Theta(N^{1/4}),
\qquad
AL1,AL2:\Theta(N^{1/2}).
\]

### Depth d=3

Eight bottom digits, alphabet size `N^{1/8}`:

\[
AL0:\Theta(N^{1/8}),
\qquad
AL1,AL2:\Theta(N^{1/4}).
\]

As `d` grows, all exponents tend to zero, recovering the earlier no-go result that no positive exponent survives unbounded fixed-depth choice across presentations.

---

## 12. Depth versus quantifier complexity

The theorem is formulated in decomposition depth because a clean unrestricted lower bound purely in FO quantifier rank is not currently justified.

For the explicit constructions, however, recovery complexity grows with the radix width `k=2^d`:

- order comparison: `O(k)` coordinate tests;
- addition: `O(k)` carry witnesses;
- multiplication: `O(k^2)` local product/carry witnesses.

Thus one obtains constructive tradeoffs

\[
q_{AL0}=O(2^d),
\]

\[
q_{AL1}=O(2^d),
\]

\[
q_{AL2}=O(4^d)
\]

for straightforward formulas.

These are **upper bounds on formula complexity**, not lower bounds. Proving a theorem of the form

\[
q\le q_0\Longrightarrow M_{bot}(AL2)\ge N^{c(q_0)}
\]

for arbitrary FO presentations remains open and would require genuine finite-model/circuit lower-bound machinery.

---

## 13. Why the theorem is not vacuous

The separation is not merely the statement that a multiplication table has more rows than a chain. The important point is that it identifies exactly which previous compression mechanism destroyed each attempted invariant:

- increasing radix/decomposition depth decreases the alphabet size;
- once depth is frozen, that escape route disappears;
- order only needs sparse organization of the primitive alphabet;
- arithmetic needs binary transport over every pair of primitive symbols.

Thus the phase boundary is not “more total memory”, but

\[
\boxed{
\text{unary/comparison organization}
\quad\text{versus}\quad
\text{complete binary transport at the lowest unresolved scale}.
}
\]

---

## 14. Limits of the result

HM-BDRS does **not** claim:

1. an interpretation-invariant lower bound for all FO encodings;
2. an absolute quantifier-rank separation;
3. that AL2 costs more than AL1 in this normal form;
4. that every representation must expose a radix alphabet.

It does claim an exact asymptotic separation once the representation is normalized by a fixed factorization depth and an extensional primitive bottom law.

---

## 15. Next research target

The strongest unresolved question is now narrower and more realistic:

\[
\boxed{
\text{Can HM-BDRS be extended from radix normal forms to a representation class defined semantically,}
}
\]

for example bounded-fan-in FO transductions, bounded-depth incidence circuits, or interpretations with a bounded number of compositional factorization layers?

A successful extension would turn the current normal-form theorem into a genuine resource phase theorem.
