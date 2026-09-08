# HATTER-SOL-03 · RESEARCH STATE

## Working title

**«Чашка, которая задаёт вопросы сама: анонимные пробы, возвращение симметрии и рекурсивная жёсткость простых»**

English working title:

**“The Cup That Asks Its Own Questions: Anonymous Probes, Returning Symmetry, and Recursive Rigidity of the Primes.”**

## Starting point

HATTER-SOL-02 ended with the question

> Can a finite natural mechanism generate, from within the structure itself, a separating family rich enough to recover rigidity without externally naming an infinite family of probes?

The first strike shows that this question splits into three sharply different regimes:

1. **pure multiplication + finite seeds:** impossible;
2. **uniform but anonymous quadratic questions:** symmetry can return rather than disappear;
3. **a well-founded exact predecessor mechanism:** one finite binary relation can force full rigidity.

This gives HATTER-SOL-03 a new central theme:

\[
\boxed{
\text{self-generated individuality needs canonical asymmetry, not merely many questions.}
}
\]

---

# 1. Finite-seed barrier in pure multiplication

Let

\[
\mathcal M=(\mathbb N_{>0},\times).
\]

For a finite tuple

\[
\bar a=(a_1,\ldots,a_k)
\]

and a prime \(p\), define its valuation signature

\[
\nu_{\bar a}(p)
=
(v_p(a_1),\ldots,v_p(a_k))\in\mathbb N^k.
\]

## Main theorem candidate A

The orbits of the pointwise stabilizer

\[
\operatorname{Aut}(\mathcal M/\bar a)
\]

on the set of primes are exactly the fibers of \(\nu_{\bar a}\):

\[
\boxed{
p\sim_{\bar a}q
\iff
\nu_{\bar a}(p)=\nu_{\bar a}(q).}
\]

Consequently, all primes outside

\[
\operatorname{supp}(\bar a)
:=
\bigcup_i\{p:p\mid a_i\}
\]

have the zero signature and form one infinite orbit.

Therefore:

\[
\boxed{
\text{no finite tuple of multiplicative parameters can rigidify the primes.}
}
\]

More strongly,

\[
\operatorname{dcl}_{\mathcal M}(\bar a)\cap\mathbb P
\]

is finite: only singleton valuation-signature fibers can be definable over \(\bar a\).

Interpretation: the pure multiplicative cup cannot manufacture an infinite list of new prime questions from finitely many seeds. The symmetry group itself forbids such a canonical choice.

---

# 2. Anonymous-question paradox

HATTER-SOL-02 obtained rigidity by using separately named predicates \(Q_p\). The predicate name anchors the modulus \(p\): the question itself cannot move.

What happens if all those questions are merged into one uniform binary relation, so that the *questioner* can move together with the *answerer*?

A classical construction gives the warning.

Let

\[
\mathbb P_1=\{p\in\mathbb P:p\equiv1\pmod4\}
\]

and define a graph by

\[
p\sim q
\iff
\left(\frac pq\right)=1.
\]

Quadratic reciprocity makes the relation symmetric on \(\mathbb P_1\). Peter J. Cameron observed that this graph is the countable random/Rado graph; the extension property follows from CRT + Dirichlet.

Hence the uniform quadratic network is maximally homogeneous rather than rigid.

This is the conceptual reversal:

\[
\boxed{
\text{named probes can rigidify; anonymous probes can restore symmetry.}
}
\]

The HATTER-SOL interpretation is new framing only; the Rado-graph construction itself is classical.

Literature anchor:

- P. J. Cameron, *The Random Graph Revisited*, European Congress of Mathematics, Vol. II, 2001, pp. 267–274, DOI: **10.1007/978-3-0348-8268-2_15**.

---

# 3. A second warning from the \(p-1\) graph

There is an even closer bridge to the next positive mechanism.

Gareth A. Jones studies the directed graph on primes with

\[
q\to p
\iff
q\mid p-1,
\]

and labels an arc by \(r\) when

\[
q^r\parallel p-1.
\]

He proves that every finite acyclic positively labelled directed graph occurs in this way for a suitable finite prime set. He also proves that after deleting \(2\), forgetting directions and forgetting labels, the graph on odd primes with an edge whenever

\[
q\mid p-1\quad\text{or}\quad p\mid q-1
\]

is again the Rado graph.

Literature anchor:

- G. A. Jones, *Regular embeddings of complete bipartite graphs: classification and enumeration*, Proc. London Math. Soc. 101 (2010), 427–453, DOI: **10.1112/plms/pdp061**, especially Sections 13–14.

This means the support-only shadow is already known to carry enormous homogeneity. Any HATTER-SOL novelty must therefore concern the precise finite-language rigidity mechanism, not the existence of the prime-chain graph itself.

---

# 4. Exact predecessor-power relation

Define one binary relation \(H(a,p)\) on positive integers by

\[
H(a,p)
\iff
\begin{cases}
p\text{ is prime},\\
a=q^e\text{ for some prime }q,\\
q^e\parallel p-1.
\end{cases}
\]

Thus \(H(-,p)\) does not list all divisors of \(p-1\). It stores exactly one maximal prime power for each prime divisor of \(p-1\).

For example,

\[
12=2^2\cdot3
\]

means that for \(p=13\) the incoming exact-power data are

\[
H(4,13),\qquad H(3,13).
\]

Their product reconstructs

\[
13-1=12.
\]

Define

\[
\mathcal H
=(\mathbb N_{>0},\times,H).
\]

## Main theorem candidate B — self-generated rigidity

\[
\boxed{
\operatorname{Aut}(\mathcal H)=\{\mathrm{id}\}.
}
\]

Proof strategy: strong induction on the usual prime order.

- \(2\) is the unique prime with no \(H\)-predecessor.
- Suppose every prime below \(p\) is fixed.
- Every \(H\)-predecessor of \(p\) is a power of a prime \(q<p\), hence is fixed.
- Preservation of \(H\) forces \(p\) and its image to have the same finite set of exact predecessor powers.
- The product of those powers is exactly \(p-1\), hence the image has the same predecessor integer and must equal \(p\).
- Unique factorization then fixes every positive integer.

This is the first positive answer to the HATTER-SOL-03 question: **one finite relation symbol can generate enough internal recursive structure to destroy the full prime-permutation symmetry.**

---

# 5. Why this is not a trivial restatement of HATTER-SOL-02

HATTER-SOL-02 used infinitely many externally indexed predicates

\[
(Q_p)_{p\in F}.
\]

The present mechanism uses one relation symbol \(H\), and the relevant questions are generated from the target prime itself by recursively descending through the factorization of \(p-1\).

The difference is therefore not "finite language versus infinite language" alone. The key is that \(H\) has a **well-founded recursive anchor**:

\[
p
\longmapsto
\{q^{v_q(p-1)}:q\mid p-1\}
\longmapsto
\cdots
\longmapsto
2.
\]

This is closely related to the classical Pratt-tree / prime-chain hierarchy, so the hierarchy itself is not new. The exact HATTER-SOL question is whether this hierarchy, packaged as a single relation on the original multiplicative carrier, acts as a self-indexing rigidity mechanism.

---

# 6. Current conceptual law

The first two papers suggested that enough separation creates individuality. The third now forces a refinement:

\[
\boxed{
\text{separation without anchors can remain homogeneous.}
}
\]

The stronger candidate law is

\[
\boxed{
\text{self-generated individuality}
=
\text{separation}
+
\text{canonical indexing / well-founded anchoring}.
}
\]

Literary image:

- at the tea party everyone can "change places" and the table may look structurally unchanged — an automorphism;
- the \(p-1\) descent is the opposite image: going down the rabbit hole eventually reaches the unique anchor \(2\).

These are metaphors, not claims about Carroll's intended mathematics.

---

# 7. Immediate next strikes

1. Write the finite-seed theorem and self-generated rigidity theorem as formal proofs.
2. Check whether the exact relation \(H(a,p)\) can be weakened while preserving rigidity.
3. Primary minimality target:
   \[
   D(q,p)\iff q,p\in\mathbb P\text{ and }q\mid p-1.
   \]
   Is the **directed support-only prime graph** \((\mathbb P,D)\) rigid? Jones proves its undirected odd-prime shadow is Rado, but that does not settle the directed graph.
4. Intermediate target: retain direction but erase exponent depth. Determine whether depth is genuinely necessary for rigidity.
5. Literature audit: definable closure in Skolem arithmetic; Pratt trees/prime chains; Rado constructions from quadratic residues and from the \(p-1\) support graph.
6. Only after the directed-support question is resolved or sharply isolated should the publication article be assembled.

## Publication threshold

Not yet frozen. The branch already contains one negative theorem and one positive rigidity theorem, but the strongest version of HATTER-SOL-03 should determine how much of the \(p-1\) mechanism can be erased before rigidity fails.
