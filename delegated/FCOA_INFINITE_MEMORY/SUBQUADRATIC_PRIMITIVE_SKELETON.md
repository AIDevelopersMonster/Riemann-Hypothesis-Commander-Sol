# Subquadratic Primitive Skeleton

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Status:** theorem checkpoint + provenance candidate  
**Scope:** infinite fixed-carrier branch only

## 1. Question

Can a finite-signature primitive non-order skeleton on the same infinite carrier satisfy all three requirements simultaneously?

1. use only \(o(N^2)\) active incidences on the first \(N\) carrier points;
2. first-order recover the full strict order;
3. still fail to first-order recover ordinary external-index addition and multiplication.

The logical answer is **yes**.

Moreover, the required growth profile admits a finite substitution presentation, so the construction need not be specified by writing multiplication or squaring into the external-index rule. This improves the provenance status from an arithmetic calibration witness to a genuine finite-combinatorial primitive candidate.

---

## 2. Nested-tail template

Let

\[
G_\omega=\{Q_0,Q_1,Q_2,\ldots\}
\]

be the generic carrier in its external enumeration. Let

\[
f:\mathbb N\to\mathbb N
\]

be strictly increasing and cofinal. Define a binary relation

\[
\boxed{
R_f(Q_n,Q_m)\iff m\ge f(n).
}
\]

Equivalently, with one terminal output \(\Omega\), define one partial-operation layer

\[
Q_n\star_f Q_m=\Omega
\iff
R_f(Q_n,Q_m).
\]

The row of \(Q_n\) is the tail

\[
N_f(n)=\{Q_m:m\ge f(n)\}.
\]

Since \(f\) is strictly increasing, these rows form a strict descending chain under inclusion.

---

## 3. FO recovery of the full order

### Theorem PS-1 — row-inclusion order

The original strict order of the carrier is first-order definable from \(R_f\) alone:

\[
\boxed{
Q_n<Q_k
\iff
N_f(k)\subsetneq N_f(n).
}
\]

An explicit formula is

\[
\operatorname{Less}(x,y):=
\forall z\,(R_f(y,z)\to R_f(x,z))
\wedge
\exists z\,(R_f(x,z)\wedge\neg R_f(y,z)).
\]

### Proof

If \(n<k\), then \(f(n)<f(k)\), so every point in the tail beginning at \(f(k)\) also lies in the tail beginning at \(f(n)\), while points between the two thresholds witness proper inclusion.

Conversely, strict inclusion of the two tails forces \(f(n)<f(k)\), and strict monotonicity of \(f\) gives \(n<k\). \(\square\)

Thus one binary relation and one anonymous terminal output suffice for FO global-order recovery.

---

## 4. The jump map is internally recoverable

Once \(<\) is recovered, the minimum point in each row is definable:

\[
\operatorname{Jump}(x,y):=
R_f(x,y)
\wedge
\neg\exists z\,(\operatorname{Less}(z,y)\wedge R_f(x,z)).
\]

For every \(Q_n\) there is exactly one such \(Q_m\), namely

\[
m=f(n).
\]

Hence

\[
(G_\omega,R_f)
\]

is first-order interdefinable with

\[
(\mathbb N,<,f)
\]

under the external enumeration.

This observation is the key to both the decidability and arithmetic-leakage audits below.

---

## 5. First exact witness: quadratic nested tails

Take

\[
f_1(n)=(n+1)^2.
\]

Then

\[
R_1(Q_n,Q_m)\iff m\ge(n+1)^2.
\]

### Incidence count

On ranks \(0,\ldots,N\), let

\[
M=\lfloor\sqrt N\rfloor.
\]

The active rows whose threshold enters this initial segment correspond to

\[
j=1,\ldots,M.
\]

Hence

\[
C_1(N)
=\sum_{j=1}^{M}(N-j^2+1)
\]

and therefore

\[
\boxed{
C_1(N)=\frac23N^{3/2}+O(N).
}
\]

In particular,

\[
C_1(N)=o(N^2).
\]

Every source point has infinitely many outgoing partners, so the construction crosses the Infinite Nonlocal Core barrier despite its subquadratic initial-segment incidence count.

---

## 6. Finite substitution provenance

The same growth profile can be generated without using addition or multiplication as operations on the carrier indices.

Consider the finite word morphism

\[
\sigma(A)=ABBC,
\qquad
\sigma(B)=BC,
\qquad
\sigma(C)=C.
\]

Let

\[
a_n=|\sigma^n(A)|,
\qquad
b_n=|\sigma^n(B)|,
\qquad
c_n=|\sigma^n(C)|.
\]

Then

\[
c_n=1,
\qquad
b_n=n+1,
\]

and

\[
a_{n+1}=a_n+2b_n+c_n.
\]

With \(a_0=1\), induction gives

\[
\boxed{a_n=(n+1)^2.}
\]

Indeed,

\[
a_{n+1}
=(n+1)^2+2(n+1)+1
=(n+2)^2.
\]

Therefore the threshold sequence can be presented primitively as

\[
\boxed{f_1(n)=|\sigma^n(A)|.}
\]

The substitution rule itself contains no external-index \(+\), \(\times\), divisibility, BIT, or prime predicate. Squaring appears only afterward as a theorem describing the combinatorial growth of a finite substitution system.

### Provenance status

This is materially different from defining the skeleton by the forbidden rule

\[
R(n,m)\iff n^2\le m
\]

using external multiplication.

The branch therefore records the substitution-generated presentation as a **source-admissibility candidate**. The mathematical theorems below do not depend on accepting any priority or novelty claim for this presentation.

---

## 7. Decidable FO theory

Let

\[
q(n)=n^2.
\]

A. L. Semenov proved that the elementary theory

\[
\operatorname{Th}(\mathbb N;<,q)
\]

is decidable, while

\[
\operatorname{Th}(\mathbb N;+,q)
\]

is undecidable.

Reference:

A. L. Semenov, “Logical theories of one-place functions on the set of natural numbers”, *Math. USSR-Izv.* **22** (1984), 587–618, DOI `10.1070/IM1984v022n03ABEH001456`.

In pure discrete order, successor and predecessor are FO-definable. Therefore

\[
f_1(n)=q(S(n))=(n+1)^2
\]

and, conversely, for \(n>0\),

\[
q(n)=f_1(\operatorname{pred}(n)),
\]

with \(q(0)=0\).

Hence

\[
(\mathbb N,<,f_1)
\]

and

\[
(\mathbb N,<,q)
\]

are first-order interdefinable.

By Section 4,

\[
(G_\omega,R_1)
\]

is interdefinable with \((\mathbb N,<,f_1)\). Consequently:

\[
\boxed{
\operatorname{Th}(G_\omega,R_1)\text{ is decidable}.}
\]

---

## 8. Addition does not leak

### Theorem PS-2

Ordinary external-index addition is not FO-definable in

\[
(G_\omega,R_1).
\]

### Proof

Assume addition were FO-definable in \((G_\omega,R_1)\). The jump function \(f_1\) is already FO-definable there, and \((G_\omega,R_1)\) has decidable complete theory.

Thus every sentence of

\[
(\mathbb N;+,f_1)
\]

could be effectively translated to a sentence of the decidable theory of \((G_\omega,R_1)\).

But \((\mathbb N;+,f_1)\) is interdefinable, up to the definable successor/predecessor shift, with the quadratic expansion \((\mathbb N;+,n^2)\), whose theory is undecidable by the result recorded by Semenov.

Contradiction. \(\square\)

Therefore

\[
\boxed{
<\text{ is FO-definable but }+\text{ is not}.}
\]

---

## 9. Multiplication does not leak

### Theorem PS-3

Ordinary external-index multiplication is not FO-definable in

\[
(G_\omega,R_1).
\]

### Proof

Assume multiplication were FO-definable.

The structure already FO-defines the discrete order, hence also the successor operation. Julia Robinson proved that addition on the positive integers is first-order definable from multiplication together with successor.

Therefore multiplication definability would imply addition definability, contradicting Theorem PS-2. \(\square\)

Reference:

Julia Robinson, “Definability and decision problems in arithmetic”, *J. Symbolic Logic* **14** (1949), 98–114, DOI `10.2307/2266510`.

Thus the exact leakage status is

\[
\boxed{
R_1\Rightarrow_{\rm FO}<,
\qquad
R_1\not\Rightarrow_{\rm FO}+,
\qquad
R_1\not\Rightarrow_{\rm FO}\times.
}
\]

---

## 10. Stronger family: arbitrarily close to linear density

The quadratic witness is not isolated.

Let

\[
f(t)=(t+1)^2
\]

be the substitution-generated jump map from Section 6. For a fixed integer \(k\ge1\), let

\[
F_k=f^{\circ k}
\]

be its \(k\)-fold composition, and define

\[
R_k(Q_n,Q_m)\iff m\ge F_k(n).
\]

### 10.1 Order recovery

Every \(F_k\) is strictly increasing, so the same strict row-inclusion formula defines the full carrier order.

### 10.2 Decidability

Because \(f\) is interdefinable with \(q(n)=n^2\), every fixed iterate \(F_k\) is FO-definable in the decidable structure

\[
(\mathbb N,<,q).
\]

Therefore \((G_\omega,R_k)\) is an FO reduct of a decidable structure, and

\[
\boxed{\operatorname{Th}(G_\omega,R_k)\text{ is decidable}.}
\]

### 10.3 Growth

The polynomial \(F_k\) has degree

\[
d_k=2^k
\]

with positive leading coefficient. Hence

\[
F_k(n)=\Theta(n^{2^k}).
\]

Therefore the number of incidences in the first \(N\) carrier points is

\[
\boxed{
C_k(N)=\Theta\!\left(N^{1+1/2^k}\right).
}
\]

### 10.4 Addition still cannot be defined

The jump map \(F_k\) is internally definable from \(R_k\).

For every fixed polynomial \(P\in\mathbb Z[t]\) of degree \(d\ge2\) with nonzero leading coefficient, the structure \((\mathbb N;+,P)\) defines multiplication. One convenient route is the fixed \(d\)-fold mixed finite-difference identity: the \(d\)-fold polarization of \(P\) isolates a nonzero constant multiple of

\[
x_1x_2\cdots x_d.
\]

Setting

\[
x_3=\cdots=x_d=1
\]

yields a fixed nonzero multiple of \(xy\), and multiplication by or division by a fixed integer is Presburger-definable. Thus ordinary multiplication is FO-definable from \(+\) and \(P\).

Since \(F_k\) is a fixed degree-\(2^k\) polynomial, the theory

\[
\operatorname{Th}(\mathbb N;+,F_k)
\]

is therefore undecidable.

If addition were FO-definable from \(R_k\), this undecidable theory would reduce to the decidable theory of \((G_\omega,R_k)\), a contradiction.

So for every fixed \(k\):

\[
\boxed{
R_k\Rightarrow_{\rm FO}<,
\qquad
R_k\not\Rightarrow_{\rm FO}+,
\qquad
R_k\not\Rightarrow_{\rm FO}\times.
}
\]

---

## 11. Near-linear consequence

For every real \(\varepsilon>0\), choose fixed \(k\) such that

\[
2^{-k}<\varepsilon.
\]

Then

\[
C_k(N)
=\Theta\!\left(N^{1+2^{-k}}\right)
=O(N^{1+\varepsilon}).
\]

Hence:

### Theorem PS-4 — no universal superlinear power barrier

For every \(\varepsilon>0\), there exists a single-binary-relation, one-terminal-output primitive nested-tail skeleton on the same carrier such that

\[
\boxed{
C(N)=O(N^{1+\varepsilon}),
}
\]

while

\[
\boxed{
<\text{ is FO-definable},
\qquad
+\text{ and }\times\text{ are not FO-definable}.}
\]

Therefore there is no universal lower bound

\[
\Omega(N^{1+\delta})
\]

with fixed \(\delta>0\) once primitive non-order skeletons beyond the order-only class are admitted.

This does **not** yet produce a single \(O(N\log N)\) or \(N^{1+o(1)}\) skeleton. The exponent is fixed for each chosen finite construction.

---

## 12. Why the obvious binary-tree candidate fails

A tempting natural sparse skeleton is the complete binary word tree equipped with prefix and equal-level structure. Such structures have only hierarchical/incidence complexity and their FO theories are decidable.

However, the standard structure

\[
\mathfrak U
=\langle\{0,1\}^*;\preceq,\operatorname{eqL},L_0,L_1\rangle
\]

is the **universal automatic structure**: its FO-definable relations are exactly the synchronous regular relations on finite words.

Binary addition is a synchronous regular relation — the usual least-significant-bit-first addition automaton only needs finite carry state. Therefore this natural tree/equal-level skeleton already FO-defines ordinary addition under the binary-word number coding.

So the binary-tree route is rejected for the present arithmetic-safe target.

This negative comparison is useful: hierarchical sparsity alone is not enough; the skeleton must also avoid becoming a universal automatic coding substrate.

---

## 13. Two independent safety notions

The investigation exposes a distinction that must remain explicit.

### Internal Leakage Safety

Ask whether the resulting structure FO-defines ordinary external-index \(+\) or \(\times\).

For \(R_k\):

\[
\boxed{\text{PASS}.}
\]

### Source / Provenance Safety

Ask whether the primitive skeleton itself was introduced by evaluating forbidden arithmetic operations on the external carrier indices.

- The arithmetic description
  \[
  R(n,m)\iff (n+1)^2\le m
  \]
  is **source-unsafe** if taken as the definition.
- The finite-substitution presentation
  \[
  A\mapsto ABBC,\quad B\mapsto BC,\quad C\mapsto C
  \]
  followed by nested-tail thresholds at the generated word lengths does not place \(+\) or \(\times\) into the carrier signature or operation rules.

The branch therefore classifies the substitution presentation as:

\[
\boxed{
\text{INTERNAL LEAKAGE: PASS}
\qquad
\text{SOURCE SAFETY: CANDIDATE PASS, pending hostile provenance audit}.
}
\]

No claim is made that finite substitutions or nested-tail encodings are new mathematical objects.

---

## 14. Main conclusion

The former open problem now has a positive mathematical answer:

\[
\boxed{
\begin{array}{c}
\text{finite-signature primitive non-order skeleton}\\
\text{with }o(N^2)\text{ incidences}\\
\Downarrow\\
\text{FO recovers the full carrier order}\\
\text{but does not FO recover }+\text{ or }\times
\end{array}
}
\]

The simplest exact witness has

\[
\Theta(N^{3/2})
\]

incidences and a three-letter finite substitution provenance.

The fixed-iterate family improves this to

\[
O(N^{1+\varepsilon})
\]

for every prescribed \(\varepsilon>0\).

The remaining scientific task is no longer existence. It is to determine the strongest admissibility notion for “no arithmetic import” under which this finite-substitution provenance survives, and then to look for a single nearly-linear or \(O(N\log N)\) arithmetic-safe skeleton.