# Ninth Strike — Binary Singleton as a Mod-3 Kernel Problem

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-29  
**Status:** proved reductions and conditional theorem; binary singleton itself remains open

## 1. Aim

The eighth strike solved the empty-skeleton finite-atom problem for arbitrary threshold depth by a depth firewall. The remaining hard case is binary depth:

\[
\kappa(r)\in\{0,1\}.
\tag{1}
\]

The reverse-divisor obstruction prevents the same greedy promotion argument.

This strike gives an exact graph-theoretic reduction of a concrete binary singleton construction to the existence of a kernel in one explicit arithmetic digraph. It also isolates a sharp sufficient condition via Richardson's kernel theorem and supplies exact finite evidence for the resulting odd-cycle problem.

No claim is made that the final kernel exists; that is the remaining arithmetic question.

---

## 2. Residual divisor digraph

For every prime \(p\), let

\[
N_p:=\tau(p)^2-p^{11}=\tau(p^2).
\tag{2}
\]

As before,

\[
N_p\ne0,
\tag{3}
\]

because \(N_p=0\) would imply

\[
2v_p(\tau(p))=11.
\tag{4}
\]

Define the loopless directed graph

\[
\Gamma_\Delta
\tag{5}
\]

on the set of rational primes by

\[
p\longrightarrow r
\iff
p\ne r\ \text{ and }\ r\mid N_p.
\tag{6}
\]

Every vertex has finite out-degree because \(N_p\) is a nonzero integer.

For a binary support \(S\), the active skeleton is empty exactly when \(S\) is independent in \(\Gamma_\Delta\), and

\[
\mu_S(\varnothing)
=
\left|
\{p\notin S:\operatorname{Out}(p)\cap S=\varnothing\}
\right|.
\tag{7}
\]

Thus the binary empty-trace problem is a directed-kernel problem.

---

## 3. Kernel reformulation

Recall that a subset \(K\) of a digraph is a **kernel** if

1. \(K\) is independent;
2. every vertex outside \(K\) has an outgoing edge to some vertex of \(K\).

Therefore a binary support with empty active skeleton and \(\mu_S(\varnothing)=0\) is exactly a kernel of \(\Gamma_\Delta\), while \(\mu_S(\varnothing)=1\) asks for a kernel with one prescribed absorption defect.

The mod-3 congruence of \(\tau\) produces a much cleaner corridor in which the single defect is forced automatically.

---

## 4. The mod-3 separator

We use the standard congruence

\[
\tau(n)\equiv n^2\sigma_1(n)\pmod3.
\tag{8}
\]

For a prime \(p\ne3\), this gives

\[
\tau(p)
\equiv
\begin{cases}
2\pmod3,&p\equiv1\pmod3,\\
0\pmod3,&p\equiv2\pmod3.
\end{cases}
\tag{9}
\]

Hence

\[
N_p
\equiv
\begin{cases}
0\pmod3,&p\equiv1\pmod3,\\
1\pmod3,&p\equiv2\pmod3.
\end{cases}
\tag{10}
\]

Therefore

\[
\boxed{
p\to3
\iff
p\equiv1\pmod3
}
\qquad(p\ne3).
\tag{11}
\]

Let

\[
C:=\{p\in\mathbb P:p\equiv2\pmod3\}.
\tag{12}
\]

Thus the marker \(3\) absorbs every prime outside \(C\cup\{3\}\), while no prime in \(C\) points to \(3\).

---

## 5. Three exact factorizations

The small coefficients needed for the corridor are

\[
N_2=\tau(4)=-1472=-2^6\cdot23,
\tag{13}
\]

\[
N_3=\tau(9)=-113643=-3^4\cdot23\cdot61,
\tag{14}
\]

and

\[
N_{11}=\tau(121)=498319933
=127\cdot3923779.
\tag{15}
\]

Both prime factors in (15) satisfy

\[
127\equiv3923779\equiv1\pmod3.
\tag{16}
\]

Consequently \(11\in C\) has **no outgoing edge to any other vertex of \(C\)**. Thus \(11\) is a sink of the induced digraph on \(C\).

Also

\[
N_{23}
=-605238167047943
=-11\cdot13\cdot4232434734601,
\tag{17}
\]

so in particular

\[
23\to11.
\tag{18}
\]

---

## 6. The corridor digraph

Let

\[
H:=\Gamma_\Delta[C\setminus\{2\}]
\tag{19}
\]

be the induced residual digraph on primes congruent to \(2\pmod3\), with the target prime \(2\) removed.

### Lemma 6.1 — Any kernel of \(H\) excludes \(23\)

If \(K\) is a kernel of \(H\), then

\[
11\in K
\qquad\text{and}\qquad
23\notin K.
\tag{20}
\]

### Proof

The vertex \(11\) is a sink of \(H\). A sink cannot lie outside a kernel, because it would have no outgoing edge into the kernel. Hence \(11\in K\).

By (18), \(23\to11\). Independence of \(K\) therefore forces \(23\notin K\). ∎

---

## 7. Binary singleton from a kernel

### Theorem 7.1 — Exact corridor reduction

If \(H\) has a kernel \(K\), then the binary support

\[
S:=\{3\}\cup K
\tag{21}
\]

has all of the following properties:

1. the positive support is infinite;
2. the active skeleton is empty;
3. the complement is infinite;
4. the unique external source with empty active trace is \(2\):

\[
\boxed{\mu_S(\varnothing)=1.}
\tag{22}
\]

### Proof

**Independence.**

The set \(K\) is independent because it is a kernel. By (11), no vertex of \(K\subseteq C\) points to \(3\). Conversely, by (14), the only prime in \(C\) receiving an edge from \(3\) is \(23\), and Lemma 6.1 gives \(23\notin K\). Thus there is no edge in either direction between \(3\) and \(K\). Hence \(S\) is independent and the active skeleton is empty.

**The target \(2\).**

By (13), the only off-diagonal residual divisor of \(N_2\) is \(23\). Since \(23\notin K\) and \(3\nmid N_2\),

\[
\operatorname{Out}(2)\cap S=\varnothing.
\tag{23}
\]

Thus \(2\) has empty active trace.

**Every other external prime is absorbed.**

Let \(q\notin S\) and \(q\ne2\).

- If \(q\equiv1\pmod3\), then \(q\to3\) by (11).
- If \(q\in C\setminus(\{2\}\cup K)\), then the kernel property of \(K\) gives some \(r\in K\) with \(q\to r\).

Hence no external prime other than \(2\) has empty trace.

**Infinitude.**

The set \(C\setminus\{2\}\) is infinite. A finite kernel \(K\) would have only finitely many incoming constraints but would need to absorb every vertex of \(H\). For every fixed finite marker set, finite-pattern realization gives infinitely many primes of \(C\) avoiding all of them; hence no finite \(K\) can be a kernel. Thus \(K\), and therefore \(S\), is infinite.

The complement contains every prime \(q\equiv1\pmod3\), so it is infinite. ∎

### Remark 7.2

The only unresolved input in Theorem 7.1 is existence of a kernel of \(H\).

The binary singleton problem has therefore been reduced to one explicit directed graph.

---

## 8. Why this reduction is stronger than the earlier reverse-divisor formulation

The original binary obstruction mixed three tasks:

- preserving independence;
- absorbing all unwanted external primes;
- protecting the unique target.

The mod-3 corridor separates them:

- marker \(3\) absorbs all primes \(1\pmod3\);
- the target \(2\) can only see \(23\);
- the sink \(11\) forces every kernel to contain \(11\), which automatically excludes \(23\);
- all remaining work is exactly kernel existence inside \(H\).

Thus target protection is no longer an additional condition.

---

## 9. Compactness for outward-finite kernels

Because every vertex of \(H\) has finite out-degree, kernel existence can be written as a propositional theory with one Boolean variable \(X_v\) for each vertex:

\[
\neg X_u\lor\neg X_v
\qquad(u\to v),
\tag{24}
\]

and

\[
X_v\lor\bigvee_{v\to w}X_w
\qquad(v\in H).
\tag{25}
\]

The disjunction in (25) is finite.

### Lemma 9.1 — Finite-obstruction compactness

If every finite subset of the clauses (24)-(25) is satisfiable, then \(H\) has a kernel.

### Proof

Apply the compactness theorem for propositional logic. A satisfying assignment defines

\[
K:=\{v:X_v=\text{true}\}.
\]

Clauses (24) give independence, while (25) give absorption. ∎

This shows that nonexistence of a kernel must have a finite propositional obstruction.

---

## 10. Richardson corridor

A classical theorem of Richardson says that a finite digraph with no directed odd cycle has a kernel. For outward-finite infinite digraphs, the same conclusion follows here directly from finite Richardson plus Lemma 9.1.

### Theorem 10.1 — Odd-cycle sufficient criterion

If \(H\) contains no directed cycle of odd length, then \(H\) has a kernel. Consequently the binary singleton profile of Theorem 7.1 exists.

### Proof

Every finite induced subdigraph of \(H\) also contains no directed odd cycle, so finite Richardson gives it a kernel.

Take any finite subset of clauses (24)-(25), and let \(W\) be the finite set of variables occurring in them. A kernel of the finite induced digraph \(H[W]\) satisfies every independence clause in the finite set. It also satisfies each absorption clause in the finite set: if \(v\notin K\), kernel absorption inside \(H[W]\) supplies an outgoing neighbor in \(K\), which is also one of the disjuncts of the full clause (25).

Hence every finite clause subset is satisfiable. Lemma 9.1 gives a kernel of \(H\), and Theorem 7.1 finishes the construction. ∎

### Claim boundary

The converse is not asserted. A digraph may have a kernel even when directed odd cycles are present.

---

## 11. Arithmetic edge constraint

### Lemma 11.1 — Quadratic-residue necessity

Let \(p\ne r\) be odd primes. If

\[
p\to r,
\]

then

\[
\boxed{\left(\frac{p}{r}\right)=1.}
\tag{26}
\]

### Proof

The edge condition is

\[
\tau(p)^2\equiv p^{11}\pmod r.
\tag{27}
\]

Since \(p\ne r\), the right side is nonzero. Because \(11\) is odd,

\[
p
\equiv
\bigl(\tau(p)p^{-5}\bigr)^2
\pmod r.
\tag{28}
\]

Thus \(p\) is a quadratic residue modulo \(r\). ∎

This is a genuine arithmetic restriction on every possible directed cycle in \(H\), although by itself it does not rule out odd cycles.

---

## 12. Exact finite computation

A finite computation was carried out as a **test only**, not as a proof of the infinite statement.

The coefficients were generated from the exact recurrence

\[
(n-1)\tau(n)
=
-24\sum_{k=1}^{n-1}\sigma_1(k)\tau(n-k),
\tag{29}
\]

and the induced graph on

\[
\{p\le30000:p\equiv2\pmod3\}
\tag{30}
\]

was constructed by exact integer divisibility tests.

Observed data:

- vertices: \(1634\);
- directed edges: \(1687\);
- directed cycles found: exactly one;
- that cycle has length \(4\):

\[
83\to71\to347\to443\to83;
\tag{31}
\]

- no directed odd cycle occurs in this range.

Each edge in (31) was verified directly by divisibility of the corresponding \(N_p\).

This evidence motivates, but does not prove, the following candidate statement.

### Conjecture 12.1 — Mod-3 Odd-Cycle Exclusion

The digraph

\[
\Gamma_\Delta[C]
\]

contains no directed cycle of odd length.

If this conjecture is true, Theorem 10.1 immediately settles the binary singleton problem positively.

---

## 13. Current frontier

The variable-depth compatibility problem is solved.

The binary problem has now been reduced to

\[
\boxed{
\text{Does }H=\Gamma_\Delta[C\setminus\{2\}]\text{ have a kernel?}
}
\tag{32}
\]

with the stronger sufficient question

\[
\boxed{
\text{Does }\Gamma_\Delta[C]\text{ contain a directed odd cycle?}
}
\tag{33}
\]

This is substantially narrower than the former reverse-divisor formulation.

The next attack should proceed in two parallel directions:

1. attempt an arithmetic proof or counterexample to Conjecture 12.1;
2. independently search for a direct kernel construction in \(H\), since odd-cycle exclusion is sufficient but not necessary.

---

## 14. Literature note

Richardson's kernel theorem and infinite/outward-finite extensions are standard in digraph kernel theory. A modern reference discussing the outward-finite version and extensions is:

M. Walicki, *Kernels of digraphs with finitely many ends*, Discrete Mathematics 342 (2019), 473–486, DOI 10.1016/j.disc.2018.10.026.

The mod-3 congruence used in Section 4 is a classical Ramanujan congruence.

---

## 15. Hostile audit

1. **Does marker 3 create an active edge into K?** No: every vertex of K is \(2\pmod3\), so (11) gives no edge to 3.
2. **Can 3 point to an active marker other than 23?** Inside C, no: (14) has only the C-prime factor 23 besides the diagonal prime 3.
3. **Why is 23 absent from every kernel?** Because 11 is a sink and therefore belongs to every kernel, while 23 points to 11.
4. **Why is 2 undominated?** Its only off-diagonal residual divisor is 23, which is absent from K; it also does not point to 3.
5. **Are primes 1 mod 3 absorbed?** Yes, uniformly by marker 3.
6. **Are the remaining 2 mod 3 primes absorbed?** Exactly by the kernel property in H.
7. **Is out-degree finite?** Yes, because each N_p is a nonzero integer.
8. **Is the computation a proof of Conjecture 12.1?** No. It is explicitly labelled finite evidence only.
9. **Is Richardson used beyond its valid scope?** The infinite conclusion is derived by propositional compactness from finite Richardson, using finite out-degree to keep every absorption clause finite.
10. **Does this solve the binary singleton unconditionally?** No. The only unresolved step is kernel existence for H.

**Audit verdict:** PASS for the exact reduction and conditional theorem. The binary singleton remains open.