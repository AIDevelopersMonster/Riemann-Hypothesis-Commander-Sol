# HATTER-SOL-04 · Finite-Future Indistinguishability

## 0. Why this strike matters

After the multiplicity-tower theorem, we looked for a weaker invariant that might separate the first Fermat-prime symmetry

\[
(3\ 5)
\]

without knowing exact predecessor-fiber cardinalities.

The natural candidates were finite rooted descendant configurations: triangles in the transitive closure, finite branching patterns, prescribed common descendants, finite colored neighborhoods, and similar local future data.

This strike shows that this entire class of attacks cannot work.

The reason is stronger than a computational failure:

\[
\boxed{
\text{finite future patterns over equal-predecessor vertices are universally reproducible.}
}
\]

For the Fermat primes in particular, \(3\) and \(5\) have the same finite future age.

The theorem is a rooted/pinned refinement of the CRT + Dirichlet universality mechanism already present in Gareth Jones's finite-acyclic universality result. We use it here specifically as an obstruction theorem for the automorphism problem.

---

# 1. The directed prime graph

Let

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1.
\]

Since \(D(q,p)\) implies \(q<p\), the graph is acyclic.

For a prime \(p\), write

\[
\operatorname{Pred}(p)=\{q\in\mathbb P:q\mid p-1\}.
\]

Every odd prime has \(2\in\operatorname{Pred}(p)\).

---

# 2. Finite forward extensions

Fix a finite induced subgraph on a set \(B\subset\mathbb P\).

A **finite forward extension** of \(B\) is a finite acyclic directed graph \(A\) containing \(B\) as an induced subgraph, together with an ordering of the new vertices

\[
v_1,\ldots,v_m
\]

such that every edge incident with a new vertex and directed toward that new vertex comes from either \(B\) or an earlier \(v_i\).

Equivalently, the new vertices are added in topological order and are intended to be realized by successively larger primes.

Because every new realized prime will be odd, admissibility also requires that the distinguished vertex corresponding to \(2\), when present in \(B\), points to every new vertex.

---

# 3. Pinned forward-extension theorem

## Theorem 3.1

Let \(B\subset\mathbb P\) be finite, and let \(A\) be any admissible finite forward extension of the induced graph \(\Pi\upharpoonright B\).

Then \(A\) can be realized inside \(\Pi\) by an embedding that fixes every vertex of \(B\) pointwise.

Moreover, at each stage the new prime may be chosen arbitrarily large, so there are infinitely many such realizations.

### Proof

We construct the new vertices in topological order.

Assume \(v_1,\ldots,v_{j-1}\) have already been realized by distinct primes

\[
p_1<\cdots<p_{j-1}
\]

all larger than every element of \(B\).

Let

\[
C=B\cup\{p_1,\ldots,p_{j-1}\}.
\]

Split \(C\) into two sets:

\[
U=\{q\in C:q\to v_j\text{ is required in }A\},
\]

and

\[
V=C\setminus U.
\]

Because the extension is admissible, if \(2\in C\) then \(2\in U\).

For every \(q\in U\), impose

\[
p\equiv1\pmod q.
\]

For every odd \(q\in V\), impose

\[
p\equiv-1\pmod q.
\]

If \(2\in V\), the pattern would be inadmissible, so this case does not occur.

The moduli are pairwise coprime. By the Chinese remainder theorem, the conditions combine into a single residue class

\[
p\equiv a\pmod M,
\qquad
M=\prod_{q\in C}q.
\]

The residue \(a\) is coprime to \(M\): for every \(q\in U\), \(a\equiv1\pmod q\), while for every odd \(q\in V\), \(a\equiv-1\pmod q\).

Hence Dirichlet's theorem gives infinitely many primes in this residue class. Choose one exceeding every prime already used.

Then, for \(q\in C\),

\[
D(q,p)
\iff
q\in U.
\]

Because \(p\) is chosen larger than every element of \(C\), we also automatically have

\[
D(p,q)=\text{false}
\qquad(q\in C),
\]

since \(p>q>q-1\).

Thus the new prime realizes exactly the required incidences between \(v_j\) and all previously realized vertices.

Induction completes the realization. \(\square\)

---

# 4. Rooted future age

For a finite base \(B\), define its **forward age** \(\operatorname{Age}^+(B)\) to be the class of all finite admissible forward extensions of \(B\), considered up to isomorphism fixing \(B\) pointwise.

Theorem 3.1 immediately gives:

## Corollary 4.1

For every finite induced base \(B\subset\Pi\),

\[
\boxed{
\operatorname{Age}^+(B)
\text{ is the full class of admissible finite acyclic forward extensions of }B.
}
\]

So once a finite base is fixed, the directed prime graph imposes no further finite restriction on its future beyond acyclicity and the universal edge from \(2\) to every odd new prime.

---

# 5. Equal-predecessor vertices have the same finite future

Suppose \(x,y\in\mathbb P\) satisfy

\[
\operatorname{Pred}(x)=\operatorname{Pred}(y)=S.
\]

Let

\[
B_x=S\cup\{x\},
\qquad
B_y=S\cup\{y\}.
\]

There is an obvious base isomorphism

\[
\theta:B_x\to B_y
\]

fixing every element of \(S\) and sending

\[
x\mapsto y.
\]

## Theorem 5.1 — finite-future indistinguishability

The map \(\theta\) induces an equality of rooted forward ages:

\[
\boxed{
\operatorname{Age}^+(B_x)
\cong
\operatorname{Age}^+(B_y).
}
\]

In concrete terms, every finite descendant configuration realizable over \(x\) can be realized over \(y\) with the same finite directed pattern, while all common predecessors in \(S\) remain fixed.

### Proof

Take any finite admissible forward extension of \(B_x\). Transport its abstract incidence pattern along the base isomorphism \(\theta\), obtaining an admissible finite forward extension of \(B_y\). Theorem 3.1 realizes the transported extension inside \(\Pi\) while fixing \(B_y\) pointwise. The same argument in the opposite direction gives equality of the two rooted forward ages. \(\square\)

---

# 6. Fermat-prime consequence

For every Fermat prime \(f\),

\[
\operatorname{Pred}(f)=\{2\}.
\]

Therefore any two Fermat primes \(f,g\) satisfy

\[
\boxed{
\operatorname{Age}^+(\{2,f\})
\cong
\operatorname{Age}^+(\{2,g\}).
}
\]

In particular,

\[
\boxed{
\operatorname{Age}^+(\{2,3\})
\cong
\operatorname{Age}^+(\{2,5\}).
}
\]

So no finite rooted future pattern can distinguish \(3\) from \(5\).

This rules out, in one stroke, any attack based only on the existence or nonexistence of a finite forward configuration involving finitely many descendants.

Examples of doomed finite-future invariants include:

- existence of a common descendant with a prescribed finite adjacency pattern;
- existence of finite rooted trees of descendants;
- any finite acyclic motif attached above the root;
- any finite number of successive extension steps in which only incidences to previously chosen vertices are prescribed.

---

# 7. What this does NOT prove

The theorem does **not** imply that \(3\) and \(5\) are globally automorphic.

The missing requirement is exact control over **all** predecessors of every newly chosen prime, not merely its incidences to a finite previously named set.

A prime produced by CRT + Dirichlet may acquire extra predecessor primes outside the finite construction.

Those extra predecessors are exactly what the multiplicity fibers remember.

Thus the theorem establishes a sharp boundary:

\[
\boxed{
\text{finite relative incidence information is freely reproducible,}
}
\]

while

\[
\boxed{
\text{exact global support is the first place rigidity can hide.}
}
\]

---

# 8. Relation to Jones's finite universality theorem

Gareth A. Jones proved that every finite acyclic labelled directed graph occurs as one of the finite prime graphs \(\Pi_n\) (Proposition 13.1), using the same CRT + Dirichlet mechanism. He also showed that after deleting \(2\) and forgetting orientation, the odd-prime shadow is the Rado graph (Proposition 14.1).

Theorem 3.1 above should therefore be viewed as a **pinned forward-extension corollary/refinement for our research purpose**, not as a claim that finite prime-graph universality itself is new.

What matters here is its use as a no-go theorem:

> finite future patterns cannot supply the unconditional symmetry-killing invariant sought in HATTER-SOL-04.

---

# 9. Logical consequence for the research strategy

We had hoped to weaken exact multiplicity comparison

\[
\mu(S)\ne\mu(\tau S)
\]

into some easier finite descendant invariant.

The finite-future theorem closes that route.

Any unconditional separator of \(3\) and \(5\) must therefore depend on at least one of the following:

1. **exact predecessor support**, not merely finite relative incidences;
2. **cardinality/multiplicity data** of exact-support fibers;
3. **an infinite/global property** of the descendant structure;
4. a graph-theoretic invariant that quantifies over all possible external predecessors, rather than a finite named set.

This is a substantial narrowing of the problem.

---

# 10. A useful model-theoretic reading

Without making a claim about full first-order types, the theorem says the following safe statement:

> Any property whose witness is a finite forward extension over the pinned predecessor base has the same truth value for two vertices with the same exact predecessor set.

Thus the pair \((3,5)\) cannot be separated by a finite existential future witness of this form.

A stronger statement about unrestricted first-order equivalence would require a genuine back-and-forth theorem, and is **not** proved here.

---

# 11. Next strike

The search space is now much smaller.

The next plausible route is to construct a **global support obstruction** that does not require knowing exact fiber cardinalities.

The most promising candidates are:

- a hereditary condition on all exact-support descendants;
- an invariant of the infinite multiplicity tower weaker than exact \(\mu(S)\) but stronger than finite incidence age;
- a monotone arithmetic obstruction that forces one support family to contain an extra external predecessor infinitely/often/always;
- or a proof that no such obstruction can distinguish the Fermat fiber, pushing the branch toward a conditional/non-rigidity theorem instead.

The finite-pattern route is now closed rigorously.

## Status

This is a negative but useful theorem: it eliminates an entire class of possible symmetry-killing arguments and confirms that the genuine difficulty begins exactly at the transition from finite relative incidence to exact global support.
