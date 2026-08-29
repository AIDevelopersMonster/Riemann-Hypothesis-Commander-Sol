# Hostile Provenance Audit R1

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Date:** 2026-08-28  
**Target:** `SUBQUADRATIC_PRIMITIVE_SKELETON.md`  
**Status:** provenance audit with repaired admissibility policy

## 1. Audit question

The previous checkpoint produced a finite-substitution presentation whose growth length is quadratic and used that length as a nested-tail threshold. The hostile question is:

> Does replacing the explicit arithmetic rule \(f(n)=(n+1)^2\) by a finite substitution genuinely avoid imported arithmetic, or does it merely hide the same arithmetic inside a finite generator?

The answer requires a provenance policy stronger than “the source description is finite” but weaker than the impossible demand that the induced relation not be arithmetically definable at all.

---

## 2. Two naive provenance tests both fail

### 2.1 Finite-program test is too weak

A finite Turing program can compute \(n^2\), multiplication, prime predicates, BIT, or any other computable arithmetic relation. Therefore

\[
\boxed{\text{finite description}\not\Rightarrow\text{source safety}.}
\]

Merely rewriting an arithmetic computation as a finite algorithm would be arithmetic laundering.

### 2.2 “Not arithmetically definable” is too strong

Any computable relation on \(\mathbb N\) is arithmetical in the ordinary sense and can be represented/defined in sufficiently rich first-order arithmetic with \(+\) and \(\times\).

Therefore a semantic policy of the form

\[
\text{reject every skeleton definable in ordinary arithmetic}
\]

would reject essentially every effective candidate, including purely combinatorial ones.

Hence provenance safety must be a **restricted generative-source criterion**, not absolute undefinability from arithmetic.

---

## 3. Repaired source gate: index-blind D0L provenance

For this branch, define a conservative certified source class.

A threshold sequence \(g(n)\) has **D0L provenance** if there exist:

1. a finite alphabet \(A\);
2. a fixed seed word \(w\in A^*\);
3. a fixed deterministic morphism
   \[
   \sigma:A^*\to A^*,
   \]
   determined solely by one replacement word \(\sigma(a)\) for each letter \(a\in A\);
4. no rule depending on the iteration number \(n\), carrier index, parity, divisibility, arithmetic comparison, stored counter, or external numerical predicate;
5. the threshold is the intrinsic word length
   \[
   g(n)=|\sigma^n(w)|.
   \]

The corresponding carrier relation is then

\[
R_g(Q_n,Q_m)\iff m\ge g(n).
\]

The external order is used only to identify the \(m\)-th carrier point and compare it with the intrinsically generated finite size \(|\sigma^n(w)|\). No binary \(+\) or \(\times\) operation on carrier indices is supplied to the generator.

### Why this is materially stronger than a finite-program gate

D0L systems are a highly restricted, index-blind parallel-rewriting class. Their growth functions are tightly constrained: classical D0L theory shows eventual polynomial/exponential behavior, and in particular no D0L growth can simulate an arbitrary computable growth law.

Relevant literature:

- G. Rozenberg and A. Salomaa, D0L/L-system growth theory;
- J. Cassaigne, C. Mauduit, F. Nicolas, “Asymptotic behavior of growth functions of D0L-systems”, arXiv:0804.1327;
- F. Nicolas and J. Cassaigne, “On polynomial growth functions of D0L-systems”, arXiv:0904.1752.

Thus the D0L gate is not merely syntactic concealment by a universal programming formalism.

---

## 4. Verdict on the previous quadratic substitution

The substitution

\[
A\mapsto ABBC,
\qquad
B\mapsto BC,
\qquad
C\mapsto C
\]

is a genuine D0L morphism, independent of stage/index values. Its quadratic length law

\[
|\sigma^n(A)|=(n+1)^2
\]

is a derived theorem about that morphism, not a primitive arithmetic test in the generation rule.

Therefore under the repaired D0L-source policy:

\[
\boxed{\text{quadratic substitution provenance: PASS}.}
\]

However, the audit finds a simpler and asymptotically stronger certified source, recorded separately in `EXPONENTIAL_NESTED_TAIL.md`.

---

## 5. Stronger certified primitive source

Use the one-letter D0L system

\[
A\mapsto AA,
\qquad w=A.
\]

Then

\[
|\sigma^n(A)|=2^n.
\]

This rule is as index-blind as possible: every existing symbol is simply duplicated at each parallel rewriting step.

The induced nested-tail relation

\[
R_{\exp}(Q_n,Q_m)
\iff
m\ge |\sigma^n(A)|
\]

therefore has a D0L-certified primitive origin.

No addition, multiplication, parity, divisibility, BIT, or arithmetic predicate occurs in the source rule.

---

## 6. Source safety versus internal leakage safety

The audit now enforces two independent gates.

### Gate S — source/provenance

Was the skeleton generated inside an accepted restricted primitive class without querying arithmetic operations/predicates on carrier indices?

For \(A\mapsto AA\):

\[
\boxed{\text{Gate S: PASS}.}
\]

### Gate L — internal arithmetic leakage

After the skeleton is installed, can FO reconstruct ordinary carrier-index addition or multiplication?

For the exponential nested-tail skeleton, `EXPONENTIAL_NESTED_TAIL.md` proves, using the known first-order structure of \((\mathbb N,<,2^x)\), that addition is not FO-definable. Multiplication would imply addition via Julia Robinson’s 1949 definability theorem, hence multiplication is not FO-definable either.

Thus:

\[
\boxed{\text{Gate L: PASS, with an explicit external QE theorem dependency}.}
\]

The QE dependency must be reproduced or replaced by a primary-source proof before publication-hardening, but it is not an unproved branch conjecture.

---

## 7. D0L nested-tail density floor

The provenance restriction itself yields an informative optimality result.

Let

\[
g(n)=|\sigma^n(w)|
\]

be an unbounded strictly increasing D0L growth function and define

\[
R_g(n,m)\iff m\ge g(n).
\]

Let

\[
B=\max_{a\in A}|\sigma(a)|.
\]

Then for every \(n\),

\[
g(n)\le |w|B^n.
\]

Therefore for all sufficiently large \(N\), at least

\[
c\log N
\]

initial rows satisfy

\[
g(n)\le \sqrt N
\]

for a constant \(c>0\) depending only on the fixed D0L system.

Each such row contributes at least

\[
N-\sqrt N
\]

incidences inside the first \(N\) columns. Consequently

\[
\boxed{
|R_g\cap[0,N]^2|=\Omega(N\log N).
}
\]

The duplication system \(A\mapsto AA\) achieves

\[
\Theta(N\log N),
\]

so:

### Theorem PA-1 — D0L nested-tail optimum

Within the D0L-provenance nested-tail class,

\[
\boxed{\Theta(N\log N)}
\]

is asymptotically optimal.

Thus the provenance repair does not merely certify the source. It also produces a natural, nontrivial memory-cost boundary.

---

## 8. What the audit does not certify

The audit does **not** claim:

- that every finite substitution is philosophically non-arithmetic under every imaginable definition;
- that D0L is the unique correct provenance class;
- that a more permissive but still source-safe primitive formalism cannot achieve \(o(N\log N)\);
- that the external quantifier-elimination theorem used in the leakage proof is a novelty of this programme.

It certifies only the explicit governance rule:

\[
\boxed{
\text{index-blind D0L source}
+\text{separate internal leakage audit}
}
\]

as a defensible conservative interpretation of the branch prohibition against silently importing \(+\) or \(\times\) on external indices.

---

## 9. Audit verdict

The previous status

\[
\text{SOURCE SAFETY: CANDIDATE PASS}
\]

is repaired as follows.

For the declared D0L provenance class:

\[
\boxed{
\text{SOURCE SAFETY: PASS}
}
\]

for both the quadratic morphism and the simpler duplication morphism.

The duplication morphism supersedes the quadratic one as the best certified primitive candidate because it lowers memory from

\[
\Theta(N^{3/2})
\]

to

\[
\boxed{\Theta(N\log N)}.
\]

The remaining frontier is now sharply separated:

> Can a comparably principled non-universal primitive source class, still passing the internal non-leakage gate, beat the D0L floor \(N\log N\)?
