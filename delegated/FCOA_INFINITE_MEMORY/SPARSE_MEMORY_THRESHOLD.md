# Sparse Memory Threshold — Local Finiteness, Infinite Nonlocal Core, and FO Order

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Status:** theorem checkpoint after hostile audit R1  
**Scope:** infinite fixed-carrier/model-theoretic branch only; no change to finite M0-G4 status

## 1. Question

The previous checkpoint separated local successor memory from global FO order memory. The next question is sharper:

> How sparse can an infinite FCOA memory layer remain while still allowing first-order recovery of the full order?

A raw count of operation cells is not the right invariant. Reification can turn one dense relation into a sparse incidence presentation by adding infinitely many witness elements. The robust obstruction is instead **Gaifman nonlocality on the active carrier after finite boundary/terminal information has been traced out**.

The main result of this note is:

\[
\boxed{
\text{finite-apex local finiteness}
\Longrightarrow
\text{no FO-definable global linear order}.}
\]

For binary finite-output FCOA layers this strengthens to:

\[
\boxed{
\text{FO full order requires an infinite nonlocal core}.}
\]

That is, infinitely many active points must have infinitely many active interaction partners.

---

## 2. Gaifman background

For a relational structure \(\mathcal A\), its Gaifman graph has the same universe and joins two distinct elements whenever they occur together in a tuple of some basic relation.

A structure is **locally finite** if every vertex has finite Gaifman degree. No uniform degree bound is assumed.

Gaifman locality says that every FO formula is controlled by bounded neighborhoods together with finitely many global local-sentence components. The theorem used here is classical; the FCOA content is the placement of this locality obstruction inside the infinite-memory ladder.

---

## 3. Locally Finite Order Barrier

### Theorem SM-1

Let \(\mathcal A\) be an infinite structure in a finite relational signature. If its Gaifman graph is locally finite, then no first-order formula \(\varphi(x,y)\) defines a strict linear order on the whole universe of \(\mathcal A\).

### Proof

Assume \(\varphi(x,y)\) defines a strict linear order.

Put \(\varphi\) into Gaifman normal form. There is a finite locality radius \(r\) and only finitely many local formula components relevant to the truth of \(\varphi(x,y)\); the remaining basic local sentences have a fixed truth value in the single structure \(\mathcal A\).

For the finitely many local components, record at each point the corresponding finite rooted local FO-type needed by the normal form. Only finitely many such relevant types occur.

Since \(\mathcal A\) is infinite, one relevant type occurs on infinitely many points. Since \(\mathcal A\) is locally finite, every finite-radius ball is finite. Therefore choose two distinct points \(a,b\) of the same relevant local type with

\[
d(a,b)>2r.
\]

Their radius-\(r\) neighborhoods are disjoint. The local information of the pointed union around \((a,b)\) is the same as that around \((b,a)\): the two components have the same relevant rooted type and are merely exchanged. All global local-sentence components are unchanged.

Hence

\[
\varphi(a,b)\iff\varphi(b,a).
\]

But a strict linear order must satisfy exactly one of \(a<b\) and \(b<a\). Contradiction. \(\square\)

### Strength

The theorem does **not** require bounded degree. Degrees may grow without bound:

\[
1,2,3,4,\ldots
\]

or in any other way. Pointwise finite degree alone is enough to block FO global order.

---

## 4. Why finite terminal hubs must be traced out

A literal Gaifman graph of a one-sorted partial-operation graph can be misleading.

In infinite G2, the common terminal value \(\Omega\) occurs in infinitely many triples

\[
T(x,y,\Omega),
\]

so \(\Omega\) has infinite Gaifman degree. Nevertheless \(\Omega\) is only one pure terminal point and does not create global order memory.

Therefore the correct invariant must eliminate finite boundary/terminal apex sets while retaining every relation they induce among active points.

---

## 5. Finite-apex trace structure

Let \(\mathcal A\) be a finite-signature relational structure and let \(C\subseteq A\) be finite.

Define the **trace structure**

\[
\operatorname{Tr}_C(\mathcal A)
\]

on \(A\setminus C\) as follows. For every basic relation symbol \(R\) and every way of fixing some coordinates of \(R\) to elements of \(C\), include the resulting relation on the remaining coordinates as a basic trace relation.

Because the signature and \(C\) are finite, the trace signature is finite.

Example: if

\[
T(x,y,z)
\]

is an operation graph and \(\Omega\in C\), then plugging in \(z=\Omega\) produces the binary trace

\[
D_\Omega(x,y)\iff T(x,y,\Omega).
\]

Thus a finite terminal output is removed as an apex, but the geometry of all input pairs mapping to it is retained.

### Translation lemma

Every FO formula of \(\mathcal A\) whose free variables range in \(A\setminus C\) translates to an FO formula of \(\operatorname{Tr}_C(\mathcal A)\).

Reason: each quantified variable is split into the finite cases in which it equals an element of \(C\), plus the remaining case in \(A\setminus C\). Atomic relations with coordinates fixed in \(C\) become trace relations.

---

## 6. Finite-Apex Locality Barrier

### Theorem SM-2

Let \(\mathcal A\) be an infinite finite-signature relational structure and let \(C\subseteq A\) be finite. If

\[
\operatorname{Tr}_C(\mathcal A)
\]

is locally finite on an infinite target domain \(U\subseteq A\setminus C\), then no FO formula of \(\mathcal A\) defines a strict linear order on \(U\).

### Proof

If such an order were definable in \(\mathcal A\), the translation lemma would make its restriction to \(U\) FO-definable in the finite trace structure. The relevant induced trace structure is locally finite, contradicting Theorem SM-1. \(\square\)

### Why the trace hypothesis is necessary

It is not enough merely to delete a finite apex set from the literal Gaifman graph.

A ternary relation could satisfy

\[
R(c,x,y)\iff x<y
\]

with a single apex \(c\). Deleting \(c\) erases all tuples, but the trace relation

\[
R_c(x,y)
\]

is exactly the full order and is maximally nonlocal. The trace construction prevents this false sparsity.

---

## 7. FCOA Finite-Fanout Barrier

Consider a fixed finite number of partial binary operation layers on the infinite generic carrier \(G_\omega\), each using a finite terminal output alphabet. Name all boundary points and all terminal outputs; naming only strengthens FO.

For every output value \(\Omega_j\), plugging it into the operation graph produces a binary value-fiber trace

\[
D_j(x,y)\iff x\star y=\Omega_j.
\]

Let \(\Gamma\) be the undirected active interaction graph on \(G_\omega\) obtained by joining \(x\ne y\) whenever some added operation layer has a defined cell on \((x,y)\) or \((y,x)\), irrespective of output value.

### Theorem SM-3 — finite-fanout barrier

If every generic point has finite degree in \(\Gamma\), then full strict order on \(G_\omega\) is not FO-definable in the enriched FCOA structure.

No uniform fanout bound is required.

### Corollary SM-3A

A finite union of locally finite binary-operation memory layers still cannot cross the FO global-order boundary.

Thus none of the following can suffice:

- successor edges;
- predecessor edges;
- arbitrary finite-distance jump families;
- arbitrary finite local G3-style value colorings;
- any finite number of pointwise-finite long-jump layers;
- unbounded but finite degree at every active point.

---

## 8. Infinite Nonlocal Core Necessity

The binary FCOA setting gives a stronger consequence.

Let

\[
H=\{x\in G_\omega:\deg_\Gamma(x)=\infty\}.
\]

### Theorem SM-4 — infinite nonlocal core

If full strict order is FO-definable from finitely many binary finite-output FCOA layers, then

\[
\boxed{|H|=\infty.}
\]

### Proof

Suppose \(H\) were finite. Add \(H\) to the finite boundary/terminal apex set. After tracing out those finitely many points, binary relations involving a named hub produce only unary traces on the remaining generic points; they do not create new edges between two remaining generic points.

By definition every remaining generic point then has finite active degree. The trace structure is locally finite, so Theorem SM-2 forbids a definable strict linear order. Contradiction. \(\square\)

Hence one universal hub is not enough. Nor are finitely many universal hubs.

Crossing the FO boundary requires **infinitely many genuinely nonlocal active locations**.

---

## 9. Placement of existing FCOA mechanisms

### G2 infinity

The active domain graph is the directed ray viewed undirected:

\[
P_2-P_3-P_4-\cdots
\]

Every generic degree is at most two.

Therefore SM-3 applies immediately.

The common terminal value \(\Omega\) is only a finite apex and disappears under the trace reduction, leaving exactly the successor-domain relation.

### Local G3 infinity

A finite output coloring of successor/reverse-successor cells changes value fibers but not active fanout. The trace remains locally finite.

Therefore local value memory cannot FO-recover global order.

### Complete comparison / infinite G4-C analogue

Every generic point interacts with infinitely many generic points. The active trace is not locally finite, and in fact

\[
H=G_\omega.
\]

The locality obstruction is therefore crossed.

### Global-order domain compilation

For

\[
x\diamond y=\Omega\iff x<y,
\]

every point has infinite active degree. Again

\[
H=G_\omega.
\]

Thus the two canonical order-recovering constructions cross exactly the necessary nonlocality barrier.

---

## 10. Raw cell density is not the invariant

The theorem above is deliberately phrased in terms of locality rather than the number of relation tuples.

There are two reasons.

### 10.1 Arithmetic coding can be subquadratic

The classical BIT predicate has only

\[
\Theta(N\log N)
\]

true incidences on the first \(N\) natural numbers, because each number contributes its set bits.

Nevertheless FO with BIT can recover order, and the standard descriptive-complexity results show that BIT is strong enough to define ordinary addition and multiplication as well.

Thus

\[
\boxed{
\Theta(N^2)\text{ pairwise comparison cells are not necessary for FO order if Arithmetic Leakage is allowed}.}
\]

BIT does not contradict SM-4: each bit-position element is incident with infinitely many numbers, and in the standard one-sorted BIT relation every natural number also serves as a bit position. The active nonlocal core is infinite.

### 10.2 Reification can make a dense relation incidence-sparse

If one is allowed a new witness element \(e_{xy}\) for every ordered pair \(x<y\), the order relation can be replaced by two incidence relations

\[
\operatorname{Src}(e_{xy},x),
\qquad
\operatorname{Tgt}(e_{xy},y).
\]

Then

\[
x<y\iff\exists e\,(
\operatorname{Src}(e,x)\wedge\operatorname{Tgt}(e,y)).
\]

Relative to the expanded universe, the number of incidence tuples is linear in the number of witness elements even though the represented order is dense.

This construction is only an **auxiliary-sort benchmark**. It is not a solution to the fixed-carrier FCOA problem because it adds an infinite pair-witness sort.

Its purpose is conceptual: raw tuple count is representation-dependent, whereas the trace/locality obstruction survives faithful treatment of the active relation.

---

## 11. Arithmetic Leakage comparison

The sparse-memory question has two distinct axes:

\[
\boxed{
\text{locality cost}
\qquad\text{and}\qquad
\text{arithmetic leakage}.}
\]

Current benchmark points are:

| enrichment | active nonlocal core | FO order | ordinary +,× leakage |
|---|---:|---:|---:|
| G2 successor domain | none | no | no |
| finite/local G3 coloring | none | no | no |
| complete order in domain | all generic points | yes | no in the canonical order-only construction |
| complete two-value comparison | all generic points | yes | no in the canonical order-only construction |
| BIT-style coding | infinite | yes | yes |

Therefore compressing pairwise order memory is possible, but a natural compressed coding may cross directly into arithmetic.

This makes the next fixed-carrier question precise:

> Does there exist a direct finite-signature FCOA enrichment on the same generic carrier with an infinite but structurally sparse nonlocal core, FO-definable full order, and provably no FO definition of ordinary addition or multiplication?

This is now the main open problem of the sparse-memory subdirection.

---

## 12. Exact threshold reached so far

The current theorem boundary is:

\[
\boxed{
\begin{array}{c}
\text{finite-apex trace locally finite}\\
\Downarrow\\
\text{FO full order impossible}\\
\Downarrow\\
\text{for binary finite-output FCOA: finitely many infinite-degree hubs still impossible}\\
\Downarrow\\
\text{FO full order requires an infinite nonlocal core}.
\end{array}}
\]

This is stronger than a bounded-degree obstruction and stronger than the previous “bounded local enrichment” statement.

The theorem gives a necessary threshold, not a complete characterization: an infinite nonlocal core is necessary but not automatically sufficient.

---

## 13. Literature boundary

No novelty claim is made for Gaifman locality itself or for classical BIT/arithmetic definability.

Relevant classical background:

- H. Gaifman, locality of first-order logic;
- L. Libkin, *Elements of Finite Model Theory*, locality and ordered-structure chapters;
- classical descriptive-complexity results showing the strength of BIT and its relation to first-order arithmetic on finite initial segments.

The research contribution claimed inside this branch is only the FCOA-specific synthesis:

\[
\boxed{
\text{finite terminal/value hubs are finite apices; after tracing them out, local finiteness is the obstruction, and fixed-carrier FO order forces an infinite active nonlocal core}.}
\]
