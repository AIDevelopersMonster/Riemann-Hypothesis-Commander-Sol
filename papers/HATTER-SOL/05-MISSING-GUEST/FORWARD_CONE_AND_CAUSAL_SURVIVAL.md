# HATTER-SOL-05 · Forward Cone, Causal Localization, and a Sharper Survival Criterion

## 0. Status and purpose

We study the directed prime graph

\[
\Pi=(\mathbb P,D),\qquad D(q,p)\iff q\mid p-1.
\]

This note isolates the causal region in which a seed permutation can propagate. It proves that the causal future of every odd prime already has relative prime density one, and it localizes the infinitude hypothesis needed to extend a first-layer symmetry.

This is a **v1.0 canonical note**. The hostile proof audit found one scope defect in the former version of Lemma 5.1: forward-closedness alone does not imply that a vertex in the set entered through one of its predecessors, because it may have been inserted as a seed. The lemma below is stated for a **generated cone from lower Pratt levels**, which is exactly the situation used in the survival theorem. The theorem itself is unchanged.

The central question

\[
\operatorname{Aut}(\Pi)\stackrel?=\{\mathrm{id}\}
\]

remains open.

---

# 1. Forward cones

For \(A\subseteq\mathbb P\), let \(C^+(A)\) be the smallest set containing \(A\) and satisfying

\[
q\in C^+(A),\quad q\mid p-1
\Longrightarrow
p\in C^+(A).
\]

Equivalently, \(p\in C^+(A)\) iff a directed path

\[
a=q_0\to q_1\to\cdots\to q_m=p,
\qquad q_j\mid q_{j+1}-1,
\]

starts at some \(a\in A\). For a single prime \(a\), write \(C^+(a)\).

For a prime set \(B\), when the limit exists define relative prime density by

\[
d_{\mathbb P}(B)
=
\lim_{x\to\infty}
\frac{|B\cap[2,x]|}{\pi(x)}.
\]

For an odd prime \(a\), set

\[
N^+(a)=\{q\in\mathbb P:q\equiv1\pmod a\}.
\]

Then \(N^+(a)\subseteq C^+(a)\), and the classical prime number theorem in arithmetic progressions gives

\[
d_{\mathbb P}(N^+(a))=\frac1{a-1}.
\]

We shall also use the classical divergence

\[
\sum_{\substack{q\in\mathbb P\\q\equiv1\pmod a}}\frac1q=\infty,
\]

and therefore

\[
\sum_{q\in N^+(a)}\frac1{q-1}=\infty.
\]

---

# 2. Density-one forward cone

## Theorem 2.1 — forward-cone density theorem

For every odd prime \(a\),

\[
\boxed{d_{\mathbb P}(C^+(a))=1.}
\]

### Proof

Take a finite set

\[
Q\subset N^+(a)
\]

and put

\[
M=\prod_{q\in Q}q.
\]

If a prime \(p\notin C^+(a)\), then

\[
p\not\equiv1\pmod q
\qquad(q\in Q),
\]

because otherwise \(a\to q\to p\).

For each \(q\in Q\), exactly one of the \(q-1\) reduced residue classes modulo \(q\) is forbidden. By the Chinese remainder theorem the proportion of reduced classes modulo \(M\) that survive all these exclusions is

\[
\prod_{q\in Q}\frac{q-2}{q-1}
=
\prod_{q\in Q}\left(1-\frac1{q-1}\right).
\]

Applying the prime number theorem in arithmetic progressions to the finitely many reduced classes modulo \(M\),

\[
\overline d_{\mathbb P}(\mathbb P\setminus C^+(a))
\le
\prod_{q\in Q}\left(1-\frac1{q-1}\right).
\]

Now let \(Q\) exhaust finite subsets of \(N^+(a)\). Since

\[
\sum_{q\in N^+(a)}\frac1{q-1}=\infty,
\]

the finite products tend to zero. Hence

\[
\overline d_{\mathbb P}(\mathbb P\setminus C^+(a))=0,
\]

which proves the theorem. \(\square\)

## Corollary 2.2 — two directed steps already have density one

Let

\[
C^+_{\le2}(a)
=
\{a\}\cup N^+(a)
\cup
\{p\in\mathbb P:\exists q\in N^+(a),\ q\mid p-1\}.
\]

Then

\[
\boxed{d_{\mathbb P}(C^+_{\le2}(a))=1.}
\]

### Proof

The proof of Theorem 2.1 used only paths \(a\to q\to p\). Thus the same finite-class estimate applies to the complement of \(C^+_{\le2}(a)\). \(\square\)

This sharpening is conceptually useful: density one is obtained before any deeper Pratt iteration is used.

---

# 3. The seed transposition

Let

\[
\tau=(3\ 5)
\]

on the first Pratt layer and define

\[
C_\tau=C^+(\{3,5\}).
\]

Since \(C^+(3)\subseteq C_\tau\), Theorem 2.1 yields

\[
\boxed{d_{\mathbb P}(C_\tau)=1.}
\]

Thus the smallest generated forward region capable of carrying the consequences of the seed transposition already contains almost every prime in relative density.

This is distinct from the HATTER-SOL-04 theorem saying that the moved set of any nontrivial global automorphism has density one. Here density one belongs to the **potential causal future** before an automorphism has been constructed.

---

# 4. Correct causal localization lemma

Let \(P_{\le n}\) be the Pratt-height truncation, let \(L_{n+1}\) be the next layer, and let

\[
G_n=\operatorname{Aut}(\Pi\upharpoonright P_{\le n}).
\]

For a finite exact support \(S\), write

\[
X_S=\{p\in\mathbb P:\operatorname{Pred}(p)=S\}.
\]

## Lemma 4.1 — generated-cone localization

Let

\[
A\subseteq P_{\le n},
\qquad
C=C^+(A),
\]

and suppose \(g_n\in G_n\) fixes every vertex of \(P_{\le n}\setminus C\).

Let \(S\subseteq P_{\le n}\) be an exact predecessor support for vertices in \(L_{n+1}\). If

\[
S\cap C=\varnothing,
\]

then

\[
g_nS=S,
\]

and every \(p\in X_S\cap L_{n+1}\) lies outside \(C\).

### Proof

Every element of \(S\) lies outside \(C\), hence is fixed by \(g_n\), so \(g_nS=S\).

Now take \(p\in X_S\cap L_{n+1}\). Because \(A\subseteq P_{\le n}\), we have \(p\notin A\). If \(p\in C=C^+(A)\), some directed path from \(A\) reaches \(p\). Its last edge has the form

\[
q\to p
\]

with \(q\in C\) and \(q\in\operatorname{Pred}(p)=S\). Hence \(q\in S\cap C\), a contradiction. Therefore \(p\notin C\). \(\square\)

### Separate forward-closed contrapositive

For **every** forward-closed \(C\), without any generated-cone assumption,

\[
\boxed{p\notin C\Longrightarrow\operatorname{Pred}(p)\cap C=\varnothing.}
\]

Indeed, if \(q\in C\) and \(q\mid p-1\), forward-closedness would force \(p\in C\).

The converse direction is not valid for an arbitrary forward-closed set, because a vertex may belong to the set as an initially inserted seed. This is exactly the scope issue repaired above.

---

# 5. Cone-Fiber Infinitude

The earlier Higher-Fiber Infinitude hypothesis (HFI) required

\[
\mu(S)=\aleph_0
\]

for every higher finite exact support \(S\ni2\), \(S\ne\{2\}\), where

\[
\mu(S)=|X_S|.
\]

For a specified seed symmetry this is stronger than necessary.

## Definition 5.1 — CFI\((g_1)\)

Let \(g_1\in G_1\), let

\[
M_1=\operatorname{supp}(g_1),
\qquad
C=C^+(M_1).
\]

We say that **Cone-Fiber Infinitude**, CFI\((g_1)\), holds if

\[
\boxed{\mu(S)=\aleph_0}
\]

for every finite exact support \(S\) satisfying

\[
S\cap C\ne\varnothing.
\]

No assumption is imposed on supports disjoint from \(C\).

---

# 6. Causal Survival Theorem

## Theorem 6.1

Let \(g_1\in G_1\), and put

\[
C=C^+(\operatorname{supp}(g_1)).
\]

If CFI\((g_1)\) holds, then \(g_1\) extends to a global automorphism

\[
g\in\operatorname{Aut}(\Pi)
\]

such that

\[
\boxed{g(p)=p\qquad(p\notin C).}
\]

### Proof

Construct compatible \(g_n\in G_n\) by induction, maintaining

\[
g_n(p)=p
\qquad(p\in P_{\le n}\setminus C).
\]

The base case is immediate from the definition of \(C\).

Assume \(g_n\) has been constructed and consider an exact support \(S\subseteq P_{\le n}\) for a fiber in \(L_{n+1}\).

**Case 1: \(S\cap C=\varnothing\).**  Apply Lemma 4.1 with \(A=\operatorname{supp}(g_1)\subseteq P_{\le1}\subseteq P_{\le n}\). Then \(g_nS=S\), and every vertex of the relevant fiber lies outside \(C\). Choose the extension to fix that fiber pointwise.

**Case 2: \(S\cap C\ne\varnothing\).**  Since \(g_n\) is a permutation fixing the complement of \(C\) pointwise, it preserves \(C\cap P_{\le n}\) setwise. Hence

\[
g_nS\cap C\ne\varnothing.
\]

CFI gives

\[
\mu(S)=\aleph_0=\mu(g_nS).
\]

Thus the multiplicity-tower extension criterion from HATTER-SOL-04 is satisfied. On each orbit of supports under \(g_n\), choose coherent bijections

\[
X_S\longrightarrow X_{g_nS}.
\]

Every vertex in a fiber with \(S\cap C\ne\varnothing\) lies in \(C\): if \(q\in S\cap C\) and \(p\in X_S\), then \(q\to p\), so forward-closedness forces \(p\in C\). Therefore no new point outside \(C\) is moved.

The resulting \(g_{n+1}\) extends \(g_n\) and preserves the induction invariant. Passing to the inverse limit

\[
\varprojlim G_n\cong\operatorname{Aut}(\Pi)
\]

gives the required global automorphism. \(\square\)

---

# 7. Corollary for \(3\leftrightarrow5\)

Let

\[
\tau=(3\ 5),
\qquad
C_\tau=C^+(\{3,5\}).
\]

If

\[
\mu(S)=\aleph_0
\]

for every finite exact support with \(S\cap C_\tau\ne\varnothing\), then

\[
\boxed{(3\ 5)\text{ extends to a global automorphism of }\Pi,}
\]

and an extension can be chosen to fix every prime outside \(C_\tau\).

Since \(d_{\mathbb P}(C_\tau)=1\), this is compatible with the density-one movement theorem: the region available for pointwise fixing has density zero.

---

# 8. Position of CFI

For the seed transposition,

\[
\text{FSI}\Longrightarrow\text{HFI}\Longrightarrow\text{CFI}(\tau).
\]

CFI is formally weaker because it says nothing about exact supports disjoint from the causal cone. The fifth paper therefore narrows the conditional survival problem to the part of the multiplicity tower that can actually be causally reached from the moved first-layer primes.

The remaining unconditional problem is not removed:

\[
\boxed{\text{prove, refute, or weaken CFI}(\tau).}
\]

In particular, finding a support \(S\) meeting \(C_\tau\) for which \(\mu(S)\) is finite or zero could obstruct the seed swap, while proving the needed orbitwise equalities could sustain it.

---

# 9. Publication boundary and next research line

This note is frozen for HATTER-SOL-05 v1.0 after hostile proof audit.

The density-one theorem uses classical ingredients: the prime number theorem in arithmetic progressions, divergence of reciprocal primes in a reduced arithmetic progression, and the Chinese remainder theorem. The publication claim is the proved structural packaging inside the HATTER-SOL multiplicity-tower programme; no claim of literature-wide priority is made for the classical analytic ingredients.

The next refinement — replacing cone-wide CFI by the exact support orbits that are actually moved by a minimally supported extension — is **not required for HATTER-SOL-05 v1.0**. It belongs naturally to HATTER-SOL-06.
