# HATTER-SOL-06 · Explicit Noncompact Death Model

## 0. Purpose

HATTER-SOL-05 proved finite-fiber compactness. HATTER-SOL-06 then isolated the exact cone-localized extension tree

\[
\mathscr T_C(\tau)
\]

and its orbitwise survival kernel. The remaining structural question was whether the middle case

\[
\text{transfinite noncompact death}
\]

is merely a logical possibility or can actually occur in a multiplicity-tower system.

This note gives an explicit countable ranked directed graph in which

- a seed transposition extends to arbitrarily large finite heights;
- every particular first nontrivial extension dies after finitely many further levels;
- no global extension exists;
- the seed has obstruction rank exactly \(\omega\).

Therefore there is **no general compactness theorem beyond the finite-branching regime**. Any theorem excluding noncompact death for the actual prime graph must use arithmetic structure special to primes, not the abstract multiplicity-tower formalism alone.

---

# 1. The ranked graph

We construct a countable directed acyclic graph

\[
\Gamma=(V,E)
\]

with levels \(L_0,L_1,L_2,\dots\). Edges always point from lower to higher level, and each vertex is determined by its exact lower predecessor set in the same sense as the prime multiplicity tower.

## Level 0

Let

\[
L_0=\{r\}.
\]

## Level 1

Let

\[
L_1=\{s,t,d\}
\]

and give all three vertices exact predecessor set

\[
\{r\}.
\]

Fix the seed automorphism

\[
\tau=(s\ t),
\qquad
\tau(d)=d.
\]

## Level 2

Introduce two countably infinite fibers

\[
A=\{a_*\}\cup\{a_0,a_1,a_2,\dots\},
\]

\[
B=\{b_0,b_1,b_2,\dots\},
\]

with exact predecessor sets

\[
\operatorname{Pred}(a)=\{r,s\}
\qquad(a\in A),
\]

\[
\operatorname{Pred}(b)=\{r,t\}
\qquad(b\in B).
\]

Also introduce a fixed marker vertex

\[
c_0\in L_2
\]

with

\[
\operatorname{Pred}(c_0)=\{r,d\}.
\]

Thus every extension of \(\tau\) to level 2 must map \(A\) bijectively onto \(B\), map \(B\) bijectively onto \(A\), and fix \(c_0\).

## Marker chain

For \(n\ge0\), having defined

\[
c_n\in L_{n+2},
\]

define

\[
c_{n+1}\in L_{n+3}
\]

by the unique exact predecessor set

\[
\operatorname{Pred}(c_{n+1})=\{r,c_n\}.
\]

Hence every extension of \(\tau\) fixes every marker \(c_n\).

---

# 2. Future predicates on the two infinite fibers

For each \(n\ge0\), define a unary predicate \(P_n\) on \(A\cup B\) by

\[
P_n(a_*)=1,
\]

\[
P_n(a_k)=1
\iff
k>n,
\]

\[
P_n(b_k)=1
\iff
k>n.
\]

Thus the special point \(a_*\) satisfies every future predicate, while every ordinary indexed point eventually fails them:

\[
P_n(a_*)=1
\quad\forall n,
\]

but

\[
P_k(b_k)=0.
\]

The ordinary points \(a_k\) and \(b_k\) have identical predicate profiles.

---

# 3. Realizing the predicates as exact-support multiplicities

For every \(n\ge0\) and every \(x\in A\cup B\), consider the support

\[
S(x,n)=\{r,x,c_n\}.
\]

Since

\[
h(c_n)=n+2,
\]

this is a support for level \(n+3\).

Define its exact fiber multiplicity by

\[
\boxed{
\mu(S(x,n))=
\begin{cases}
1,&P_n(x)=1,\\
0,&P_n(x)=0.
\end{cases}
}
\]

When the multiplicity is one, denote the unique vertex by

\[
w_{x,n}.
\]

Thus

\[
\operatorname{Pred}(w_{x,n})=\{r,x,c_n\}.
\]

All other exact supports not explicitly used in this construction are declared empty, except the supports defining the already listed vertices.

In particular, no later descendants are attached to the witness vertices \(w_{x,n}\). They serve only as one-bit future tests.

---

# 4. Finite signatures

For \(N\ge0\), define the finite signature

\[
\sigma_N(x)
=
(P_0(x),P_1(x),\dots,P_N(x)).
\]

For \(0\le k\le N\), both \(a_k\) and \(b_k\) have the same threshold signature:

\[
P_n(a_k)=P_n(b_k)=1
\iff
n<k.
\]

All elements

\[
a_*,a_{N+1},a_{N+2},\dots
\]

have the all-ones signature

\[
(1,1,\dots,1)
\]

of length \(N+1\). The same all-ones signature is realized in \(B\) by

\[
b_{N+1},b_{N+2},\dots.
\]

Therefore every finite signature class has the same cardinality in \(A\) and \(B\): the threshold classes have cardinality one, while the all-ones class is countably infinite on both sides.

## Lemma 4.1

For every \(N\ge0\), there exists a bijection

\[
f_N:A\to B
\]

preserving the predicates \(P_0,\dots,P_N\).

### Proof

Set

\[
f_N(a_k)=b_k
\qquad(0\le k\le N).
\]

The remaining source set

\[
\{a_*\}\cup\{a_{N+1},a_{N+2},\dots\}
\]

and remaining target set

\[
\{b_{N+1},b_{N+2},\dots\}
\]

are both countably infinite and consist entirely of points with the all-ones \(N\)-signature. Choose any bijection between them. \(\square\)

A particularly transparent choice is

\[
f_N(a_*)=b_{N+1},
\]

\[
f_N(a_{N+1+j})=b_{N+2+j}
\qquad(j\ge0).
\]

---

# 5. Arbitrarily deep finite survival

Choose \(N\ge0\). Extend \(\tau\) to level 2 by

\[
a\mapsto f_N(a),
\qquad
b\mapsto f_N^{-1}(b),
\]

and fix \(c_0\).

Because \(f_N\) preserves \(P_0,\dots,P_N\), for every \(n\le N\)

\[
\mu(S(x,n))
=
\mu(S(f_N(x),n)).
\]

Hence all witness fibers exposed through predicate \(P_N\) match exactly. Unique witness vertices are carried to unique witness vertices, and all zero fibers map to zero fibers.

The marker chain is fixed pointwise.

Therefore the seed admits a finite-height extension through every level on which only the predicates

\[
P_0,\dots,P_N
\]

have appeared.

Since \(N\) is arbitrary, we obtain:

## Theorem 5.1 — unbounded finite survival

For every finite height \(H\), there exists an automorphism of the truncation

\[
\Gamma\upharpoonright V_{\le H}
\]

extending the seed transposition \(\tau=(s\ t)\).

Equivalently, the seed extension tree has nodes at arbitrarily large finite depths.

---

# 6. No global extension

Now suppose for contradiction that there is a global automorphism

\[
g\in\operatorname{Aut}(\Gamma)
\]

extending \(\tau\).

Since \(g\) maps \(A\) bijectively to \(B\), there is some \(k\ge0\) with

\[
g(a_*)=b_k.
\]

Consider predicate level \(n=k\). By construction,

\[
P_k(a_*)=1,
\]

whereas

\[
P_k(b_k)=0.
\]

Thus

\[
\mu(\{r,a_*,c_k\})=1,
\]

while

\[
\mu(\{r,b_k,c_k\})=0.
\]

But \(r\) and \(c_k\) are fixed, so

\[
g\{r,a_*,c_k\}=\{r,b_k,c_k\}.
\]

An automorphism cannot map a nonempty exact fiber to an empty exact fiber. Contradiction.

Therefore:

## Theorem 6.1 — noncompact death

The seed \(\tau=(s\ t)\) extends to arbitrarily large finite heights but has no global extension.

Hence the extension tree is nonempty at every finite level but has no infinite branch.

---

# 7. Every individual first-stage choice dies finitely

The failure is stronger than mere absence of a global branch.

Take any level-2 extension, determined in particular by a bijection

\[
f:A\to B.
\]

There is a unique \(k\) such that

\[
f(a_*)=b_k.
\]

At predicate level \(k\), the exact-support mismatch

\[
\mu(\{r,a_*,c_k\})=1,
\qquad
\mu(\{r,b_k,c_k\})=0
\]

kills that chosen extension.

Thus every child of the seed dies at a finite stage, but the death heights are unbounded because we may choose

\[
f_N(a_*)=b_{N+1}.
\]

This is exactly the countdown-tree phenomenon.

---

# 8. Obstruction rank

Let rank zero mean an immediate leaf in the pruned extension tree, and recursively

\[
\operatorname{rk}(g)
=
\sup\{\operatorname{rk}(h)+1:h\succ g\}.
\]

For a child with

\[
f(a_*)=b_k,
\]

the branch survives only finitely many future predicate tests and is killed by \(P_k\). Thus every child has finite rank.

The ranks of children are unbounded in \(\mathbb N\), because choosing

\[
f_N(a_*)=b_{N+1}
\]

pushes the first forced mismatch arbitrarily far out.

Therefore the seed has rank

\[
\boxed{
\operatorname{rk}(\tau)=\omega.
}
\]

This is an explicit realization of transfinite noncompact death of the smallest infinite ordinal rank.

---

# 9. What this proves structurally

The model proves the following no-go theorem.

## Theorem 9.1 — no abstract compactness beyond finite branching

There is no theorem based only on the multiplicity-tower axioms, countability, finite Pratt/rank height for individual vertices, and nonemptiness of every finite extension level that can force global survival.

### Reason

The graph \(\Gamma\) satisfies all of these structural properties, yet its seed transposition survives every finite target height and still has no global extension.

Therefore any stronger compactness theorem for the actual prime graph must exploit additional arithmetic properties of the exact-support multiplicities

\[
\mu(S),
\]

not merely the abstract extension-tree formalism.

---

# 10. The precise missing compactness

The mechanism of failure is now transparent.

At level 2 there is an infinite fiber-to-fiber bijection choice

\[
f:A\to B.
\]

Every finite future horizon sees only finitely many predicates

\[
P_0,\dots,P_N,
\]

and these finite signatures have matching cardinalities on \(A\) and \(B\). Hence a suitable \(f_N\) exists.

But one special point \(a_*\) has a complete infinite future signature

\[
(1,1,1,\dots)
\]

that no point of \(B\) realizes.

Thus finite signatures are indistinguishable while the complete future type differs.

The noncompactness is therefore a **failure of realization of an infinite future type**.

---

# 11. Future-type formulation

For vertices \(x,y\) inside corresponding equal-predecessor fibers, define finite future equivalence to depth \(N\) by

\[
x\equiv_N y
\]

if all exact-support multiplicity tests involving the already exposed future up to depth \(N\) agree under the proposed identification.

Define complete future equivalence by

\[
x\equiv_\infty y
\iff
x\equiv_N y
\quad\forall N.
\]

In the model,

\[
\forall N\ \exists b\in B:
\quad
 a_*\equiv_N b,
\]

but

\[
\nexists b\in B:
\quad
 a_*\equiv_\infty b.
\]

This is the exact local pattern that produces noncompact death.

It suggests the prime-specific next target:

\[
\boxed{
\text{does the actual prime graph realize every finitely realizable future type inside an infinite exact fiber?}
}
\]

A positive theorem of this kind would rule out the present pathology. A counterexample inside the prime graph would exhibit genuine noncompact death.

---

# 12. Relation to FFC and CFI

Under FFC, the first-stage fibers are finite, so the compactness failure above cannot occur. König's lemma recovers a global branch from unbounded finite survival.

Under CFI, every active exact fiber is countably infinite and only cardinal equality is used. CFI forces one-step extendability uniformly, so one can choose successors recursively and obtain a global branch.

The present example lives strictly between those two regimes:

- infinite fibers create noncompact choice;
- future tests progressively distinguish possible images;
- every finite set of tests is satisfiable;
- the complete infinite family is not.

Thus the mixed/infinite-fiber regime genuinely contains a new phenomenon rather than merely a proof-technical inconvenience.

---

# 13. Consequence for HATTER-SOL-06

The previous question

\[
\text{“can transfinite noncompact death really occur?”}
\]

is now answered at the abstract multiplicity-tower level:

\[
\boxed{\textbf{YES}.}
\]

More precisely, obstruction rank \(\omega\) occurs in an explicit countable ranked exact-fiber graph.

For the actual prime graph, however, the question remains open.

The next strike is no longer to seek a purely formal compactness theorem. That route is closed.

The prime-specific target is now:

\[
\boxed{
\text{prove or refute future-type compactness for exact prime fibers.}
}
\]

A useful concrete formulation is:

> Let \(X_S\) and \(X_T\) be corresponding infinite exact prime fibers under a partial automorphism. If every finite family of future multiplicity tests admits a matching point in \(X_T\) for a given \(p\in X_S\), must there exist one point of \(X_T\) matching all future tests simultaneously?

No such theorem is currently established here. It is the correct next barrier.

---

# 14. Status

This strike establishes:

1. an explicit countable ranked exact-fiber graph with unbounded finite survival and no global survival;
2. finite death of every individual first-stage choice;
3. exact obstruction rank \(\omega\) for the seed;
4. a no-go theorem against abstract compactness beyond finite branching;
5. identification of noncompact death with non-realization of a finitely realizable complete future type.

This materially advances HATTER-SOL-06, but does **not** yet cross the publication threshold. The next result must be prime-specific.
