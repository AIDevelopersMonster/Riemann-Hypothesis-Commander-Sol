# HATTER-SOL-05 · Forward Cone, Causal Localization, and a Sharper Survival Criterion

## 0. Purpose

The first paper in the HATTER-SOL series asked how prime-renaming symmetry disappears when arithmetic structure is restored. HATTER-SOL-05 now studies the weakest unresolved reduct

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1.
\]

The previous strikes showed two things:

1. local arithmetic asymmetry between the \(3\)- and \(5\)-sides can be strong and hereditary;
2. the multiplicity tower forgets all such quantitative asymmetry once paired exact fibers are both countably infinite.

This note isolates the **causal region** in which a seed permutation can actually propagate. It then proves that this region already has relative prime density one, and that infinitude assumptions are only needed inside this region, not on every higher exact support.

The result strictly sharpens the Higher-Fiber Infinitude hypothesis introduced earlier.

---

# 1. Forward cones in the prime predecessor graph

Let

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1.
\]

For a set \(A\subseteq\mathbb P\), define its **forward cone** \(C^+(A)\) to be the smallest subset of \(\mathbb P\) such that

\[
A\subseteq C^+(A)
\]

and

\[
q\in C^+(A),\ D(q,p)
\Longrightarrow
p\in C^+(A).
\]

Equivalently,

\[
p\in C^+(A)
\]

iff there is a directed path

\[
a=q_0\to q_1\to\cdots\to q_m=p
\]

for some \(a\in A\), where each arrow means divisibility into the predecessor:

\[
q_j\mid q_{j+1}-1.
\]

For a single prime \(a\), write

\[
C^+(a)=C^+(\{a\}).
\]

---

# 2. First-layer arithmetic already generates a dense cone

For an odd prime \(a\), let

\[
N^+(a)
=
\{q\in\mathbb P:a\mid q-1\}.
\]

Then

\[
N^+(a)\subseteq C^+(a).
\]

By the prime number theorem in arithmetic progressions,

\[
d_{\mathbb P}(N^+(a))
=
\frac1{a-1}.
\]

More important for the next argument is the classical divergence

\[
\sum_{\substack{q\in\mathbb P\\q\equiv1\pmod a}}
\frac1q
=
\infty.
\]

Hence also

\[
\sum_{q\in N^+(a)}\frac1{q-1}
=
\infty.
\]

---

# 3. Forward-cone density theorem

## Theorem 3.1 — every odd prime has a density-one forward cone

Let \(a\) be any odd prime. Then

\[
\boxed{
d_{\mathbb P}(C^+(a))=1.
}
\]

Equivalently,

\[
\boxed{
d_{\mathbb P}(\mathbb P\setminus C^+(a))=0.
}
\]

### Proof

Let

\[
A=N^+(a)
=
\{q\in\mathbb P:q\equiv1\pmod a\}.
\]

Take a finite subset

\[
Q=\{q_1,\ldots,q_m\}\subset A.
\]

If a prime \(p\notin C^+(a)\), then for every \(q\in A\), and hence for every \(q\in Q\), we must have

\[
q\nmid p-1.
\]

Indeed, if \(q\in A\), then

\[
a\to q.
\]

If in addition \(q\mid p-1\), then

\[
a\to q\to p,
\]

which would imply \(p\in C^+(a)\).

Therefore

\[
\mathbb P\setminus C^+(a)
\subseteq
\{p\in\mathbb P:p\not\equiv1\pmod q\text{ for all }q\in Q\}.
\]

Put

\[
M=\prod_{q\in Q}q.
\]

Among the reduced residue classes modulo \(q\), exactly one of the \(q-1\) classes is forbidden, namely \(1\pmod q\). By the Chinese remainder theorem, among reduced residue classes modulo \(M\), the allowed proportion is

\[
\prod_{q\in Q}
\frac{q-2}{q-1}
=
\prod_{q\in Q}
\left(1-\frac1{q-1}\right).
\]

The prime number theorem in arithmetic progressions therefore gives

\[
\overline d_{\mathbb P}(\mathbb P\setminus C^+(a))
\le
\prod_{q\in Q}
\left(1-\frac1{q-1}\right).
\]

Now enlarge \(Q\) through finite subsets of \(A\). Since

\[
\sum_{q\in A}\frac1{q-1}=\infty,
\]

we have

\[
\prod_{q\in Q}
\left(1-\frac1{q-1}\right)
\longrightarrow0.
\]

Hence

\[
\overline d_{\mathbb P}(\mathbb P\setminus C^+(a))=0.
\]

Thus the complement has relative prime density zero and

\[
d_{\mathbb P}(C^+(a))=1.
\]

\(\square\)

---

# 4. Consequence for the seed swap \(3\leftrightarrow5\)

Let

\[
\tau=(3\ 5)
\]

and define its causal cone

\[
C_\tau
=
C^+(\{3,5\}).
\]

Since

\[
C^+(3)\subseteq C_\tau,
\]

Theorem 3.1 gives immediately:

## Corollary 4.1

\[
\boxed{
d_{\mathbb P}(C_\tau)=1.
}
\]

Thus the smallest forward-closed region that can carry the consequences of the seed transposition already contains almost every prime in relative density.

This is fully consistent with the density-one movement theorem from HATTER-SOL-04: if \((3\ 5)\) extends nontrivially, its moved set must itself have density one.

The new point is different:

> density one is already built into the **causal geometry** of the directed prime graph, before an automorphism has been constructed.

---

# 5. Causal localization lemma

Let

\[
P_{\le n}
\]

be the Pratt-height truncation, and

\[
G_n=\operatorname{Aut}(\Pi\upharpoonright P_{\le n}).
\]

Suppose

\[
g_n\in G_n
\]

and let

\[
C\subseteq\mathbb P
\]

be forward closed.

## Lemma 5.1

Assume that

\[
g_n(p)=p
\qquad
\text{for every }p\in P_{\le n}\setminus C.
\]

Then every exact support

\[
S\subseteq P_{\le n}
\]

satisfying

\[
S\cap C=\varnothing
\]

is fixed pointwise by \(g_n\), hence

\[
g_nS=S.
\]

Moreover, every prime

\[
p\in X_S
\]

lies outside \(C\).

### Proof

If \(S\cap C=\varnothing\), every element of \(S\) lies outside \(C\), so every element is fixed by hypothesis. Thus \(g_nS=S\).

If some \(p\in X_S\) belonged to \(C\), then because \(C\) is forward closed and \(\operatorname{Pred}(p)=S\), the reason for membership of \(p\) in \(C\) would have to come from a directed path entering \(p\) through one of its predecessors. Hence some \(q\in S\) would lie in \(C\), contradicting \(S\cap C=\varnothing\). \(\square\)

### Equivalent contrapositive

If

\[
p\notin C,
\]

then

\[
\operatorname{Pred}(p)\cap C=\varnothing.
\]

Thus vertices outside a forward cone do not receive any incoming edge from the cone.

---

# 6. Cone-Fiber Infinitude

The earlier Higher-Fiber Infinitude hypothesis HFI required

\[
\mu(S)=\aleph_0
\]

for every finite exact support

\[
S\ni2,
\qquad
S\ne\{2\}.
\]

This is stronger than necessary for extending a specified seed symmetry.

## Definition 6.1 — Cone-Fiber Infinitude for a seed

Let

\[
g_1\in G_1
\]

be a first-layer permutation, and let

\[
M_1=\operatorname{supp}(g_1).
\]

Define its forward cone

\[
C=C^+(M_1).
\]

We say that **CFI\((g_1)\)** holds if

\[
\boxed{
\mu(S)=\aleph_0
}
\]

for every finite exact support \(S\) such that

\[
S\cap C\ne\varnothing.
\]

No assumption is made about exact fibers whose support is disjoint from \(C\).

---

# 7. Causal Survival Theorem

## Theorem 7.1

Let

\[
g_1\in G_1
\]

be any first-layer automorphism, and let

\[
C=C^+(\operatorname{supp}(g_1)).
\]

Assume CFI\((g_1)\).

Then \(g_1\) extends to a global automorphism

\[
g\in\operatorname{Aut}(\Pi)
\]

such that

\[
\boxed{
g(p)=p
\quad\text{for every }p\notin C.
}
\]

Thus all movement can be confined to the forward cone generated by the moved first-layer primes.

### Proof

We construct compatible automorphisms

\[
g_n\in G_n
\]

by induction, with the invariant

\[
g_n(p)=p
\qquad
(p\in P_{\le n}\setminus C).
\]

The case \(n=1\) holds by definition of \(C\): outside the support of \(g_1\), the first-layer automorphism is fixed, and \(2\) is fixed.

Assume \(g_n\) has been constructed.

Consider an exact predecessor support

\[
S\subseteq P_{\le n}
\]

for vertices of height \(n+1\).

### Case 1: \(S\cap C=\varnothing\)

By Lemma 5.1,

\[
g_nS=S,
\]

and every vertex of \(X_S\) lies outside \(C\). We choose the extension to fix \(X_S\) pointwise.

### Case 2: \(S\cap C\ne\varnothing\)

Because \(g_n\) fixes the complement of \(C\), it preserves \(C\cap P_{\le n}\) setwise. Hence

\[
g_nS\cap C\ne\varnothing.
\]

By CFI\((g_1)\),

\[
\mu(S)=\aleph_0
=
\mu(g_nS).
\]

Therefore the multiplicity-tower extension criterion from HATTER-SOL-04 is satisfied on every such support orbit. Choose bijections

\[
X_S\longrightarrow X_{g_nS}
\]

coherently around each orbit of supports under \(g_n\).

Combining the pointwise identity choices from Case 1 with these bijections yields

\[
g_{n+1}\in G_{n+1}
\]

extending \(g_n\).

Every newly moved vertex lies in some \(X_S\) with \(S\cap C\ne\varnothing\), and because \(C\) is forward closed, all such vertices lie in \(C\). Hence

\[
g_{n+1}(p)=p
\qquad
(p\in P_{\le n+1}\setminus C).
\]

This completes the induction.

The compatible sequence

\[
(g_n)_{n\ge1}
\]

defines an element of the inverse limit

\[
\varprojlim G_n
\cong
\operatorname{Aut}(\Pi).
\]

The resulting global automorphism fixes every prime outside \(C\). \(\square\)

---

# 8. The \(3\leftrightarrow5\) corollary

Let

\[
\tau=(3\ 5)
\]

on the first Pratt layer, fixing every other Fermat prime.

Define

\[
C_\tau=C^+(\{3,5\}).
\]

## Corollary 8.1

Assume

\[
\mu(S)=\aleph_0
\]

for every finite exact support satisfying

\[
S\cap C_\tau\ne\varnothing.
\]

Then

\[
\boxed{
(3\ 5)
\text{ extends to a global automorphism of }\Pi.
}
\]

Moreover, one can choose the extension so that it fixes every prime outside \(C_\tau\).

Because

\[
d_{\mathbb P}(C_\tau)=1,
\]

this localization does not contradict the density-one support theorem: the complement available for pointwise fixing is itself density zero.

---

# 9. Why CFI is strictly weaker than HFI

HFI requires infinitude for **every** higher exact support.

CFI\((\tau)\) requires infinitude only for supports that meet the forward cone generated by \(3\) or \(5\).

For example, supports built entirely from \(2\) and Fermat-layer primes outside \(C_\tau\), such as a hypothetical support involving \(17\) but no descendant of \(3\) or \(5\), are not constrained by CFI unless they also contain some prime from \(C_\tau\).

Thus

\[
\boxed{
\text{HFI}\Longrightarrow\text{CFI}(\tau),
}
\]

but CFI\((\tau)\) does not formally imply HFI.

The hypothesis is therefore genuinely more local to the seed symmetry.

---

# 10. Causal minimality of the cone

The forward cone has a conceptual meaning independent of infinitude assumptions.

Suppose a first-layer prime \(x\) moves. A prime \(p\) can detect this movement through the relation \(D\) only if some directed path from \(x\) reaches \(p\). If no such path exists, then every predecessor of \(p\), every predecessor of those predecessors, and so on, avoids \(x\).

Thus

\[
C^+(x)
\]

is the smallest forward-closed region in which the consequences of moving \(x\) can be forced to propagate.

This gives a precise version of the narrative inherited from HATTER-SOL-01:

> a prime does not lose its multiplicative freedom everywhere at once; the loss of freedom propagates through the arithmetic dependency graph generated by the retained fragment of \(p-1\).

---

# 11. Relation to the density-one movement theorem

HATTER-SOL-04 proved:

\[
g\ne\mathrm{id}
\Longrightarrow
 d_{\mathbb P}(\operatorname{supp}(g))=1.
\]

Theorem 3.1 here proves a different density-one phenomenon:

\[
a\text{ odd prime}
\Longrightarrow
 d_{\mathbb P}(C^+(a))=1.
\]

The first statement concerns the **actual moved set of a hypothetical automorphism**.

The second concerns the **potential causal region generated by one moved prime**.

Together they produce a striking alignment:

\[
\boxed{
\text{one moved odd prime already has a density-one arithmetic future,}
}
\]

and any genuine nontrivial automorphism is forced to move a density-one set inside such a density-one future region.

This does not prove that a nontrivial automorphism exists.

---

# 12. A sharper survival frontier

The branch now has three nested sufficient hypotheses for survival:

\[
\text{FSI}
\Longrightarrow
\text{HFI}
\Longrightarrow
\text{CFI}(\tau).
\]

Where:

- FSI demanded every support fiber, including \(\{2\}\), be infinite;
- HFI removed the unnecessary Fermat-prime infinitude assumption;
- CFI\((\tau)\) removes every higher support that lies outside the causal future of the seed swap.

Hence the conditional non-rigidity theorem has been sharpened twice.

The remaining gap is now much more exact:

\[
\boxed{
\text{can CFI}(\tau)
\text{ be proved, disproved, or weakened further?}
}
\]

---

# 13. Next strike

There are now two high-value directions.

## Strike A — minimal orbitwise survival

Replace CFI by the exact set of support orbits that are **actually moved** by a minimally supported extension. This may yield a necessary-and-sufficient recursive survival condition strictly weaker than cone-wide infinitude.

## Strike B — arithmetic attack inside the cone

Search for one support

\[
S\cap C_\tau\ne\varnothing
\]

for which \(\mu(S)\) can be proved finite or zero. Such a support would directly attack CFI and could kill the seed swap.

Theorem 3.1 shows that this battleground is not sparse in the ordinary density sense: the causal cone itself already occupies density one of the primes.

---

# 14. Publication status

The mathematical package of HATTER-SOL-05 is now substantially stronger than its initial plan:

1. finite fixed-divisor coverings are impossible for every exact support;
2. the cyclotomic obstruction exhibits a one-dimensional Fermat collapse but positive-density survival in every higher support dimension;
3. the \(3\)- and \(5\)-branches have a persistent local sieve asymmetry;
4. exact descendants amplify that asymmetry but encounter a cardinality wall;
5. every moved odd prime has a density-one forward cone;
6. survival requires infinitude only inside the causal cone of the seed symmetry.

This is now a coherent structural theorem package. It is **close to publication threshold**, but one hostile proof/literature audit should be completed before freezing v1.0. The central yes/no problem

\[
\operatorname{Aut}(\Pi)\stackrel?=\{\mathrm{id}\}
\]

remains open and must not be presented as solved.

---

# Literature boundary

The proof of the density-one forward-cone theorem uses only classical ingredients: the prime number theorem in arithmetic progressions, divergence of reciprocal primes in a reduced arithmetic progression, and the Chinese remainder theorem. The cone formulation and its role in the HATTER-SOL multiplicity tower are used here as structural consequences for the present programme; no claim of literature-wide priority is made without a dedicated audit.
