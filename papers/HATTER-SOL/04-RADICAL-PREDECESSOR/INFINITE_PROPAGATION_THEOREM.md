# HATTER-SOL-04 · Infinite Propagation Theorem

## 0. Motivation

The finite-future indistinguishability theorem shows that no finite forward motif can kill the first Fermat-prime symmetry. We now ask a different unconditional question:

> If a nontrivial automorphism of the directed prime graph exists at all, how local can it be?

The answer is: **not local in any finite sense**.

A single moved prime forces infinitely many moved successors, and this propagation continues to arbitrarily large Pratt height.

This gives a strong unconditional constraint on every hypothetical nontrivial automorphism.

---

# 1. Directed prime graph

Let

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1.
\]

Let \(g\in\operatorname{Aut}(\Pi)\).

Write

\[
\operatorname{supp}(g)
=
\{p\in\mathbb P:g(p)\ne p\}.
\]

Since \(2\) is the unique vertex of indegree zero, every automorphism fixes \(2\).

---

# 2. Asymmetric successor sets are infinite

For distinct odd primes \(x\ne y\), define

\[
A(x,y)
=
\{p\in\mathbb P:
 x\mid p-1,
\ y\nmid p-1
\}.
\]

## Lemma 2.1

For all distinct odd primes \(x\ne y\), the set \(A(x,y)\) is infinite.

### Proof

Impose

\[
p\equiv1\pmod x
\]

and

\[
p\equiv-1\pmod y.
\]

By the Chinese remainder theorem these conditions combine into a reduced residue class modulo \(xy\). Dirichlet's theorem gives infinitely many primes in that class. Every such prime lies in \(A(x,y)\). \(\square\)

By symmetry, the reverse asymmetric set

\[
A(y,x)
\]

is also infinite.

Therefore the successor neighborhoods of two distinct odd primes have infinite symmetric difference.

---

# 3. One moved prime forces infinitely many moved successors

## Theorem 3.1 — local propagation

Let \(g\in\operatorname{Aut}(\Pi)\), and suppose

\[
g(x)=y\ne x.
\]

Then every prime

\[
p\in A(x,y)
\]

is moved by \(g\).

Consequently, \(x\) has infinitely many moved immediate successors.

### Proof

Take \(p\in A(x,y)\). Then

\[
D(x,p)
\]

holds, while

\[
D(y,p)
\]

fails.

Assume for contradiction that \(g(p)=p\). Since \(g\) is an automorphism,

\[
D(x,p)
\iff
D(g(x),g(p))
=
D(y,p),
\]

contradicting the choice of \(p\).

Thus \(g(p)\ne p\). Since \(A(x,y)\) is infinite, there are infinitely many moved immediate successors of \(x\). \(\square\)

---

# 4. Every moved vertex generates an infinite moved future

The previous theorem can be iterated.

## Theorem 4.1 — infinite propagation

If \(g\ne\mathrm{id}\), then there exists a sequence of moved primes

\[
x_0,x_1,x_2,\ldots
\]

such that

\[
D(x_n,x_{n+1})
\]

for every \(n\), and

\[
h(x_0)<h(x_1)<h(x_2)<\cdots.
\]

### Proof

Choose any moved prime \(x_0\), and write

\[
y_0=g(x_0)\ne x_0.
\]

Because \(2\) is fixed, \(x_0,y_0\) are odd.

By Lemma 2.1 choose

\[
x_1\in A(x_0,y_0).
\]

Then \(D(x_0,x_1)\), and Theorem 3.1 implies that \(x_1\) is moved.

Now set

\[
y_1=g(x_1)\ne x_1
\]

and repeat. At stage \(n\), choose

\[
x_{n+1}\in A(x_n,y_n).
\]

Then \(x_{n+1}\) is moved and satisfies

\[
D(x_n,x_{n+1}).
\]

Every directed edge strictly increases Pratt height, so

\[
h(x_{n+1})>h(x_n).
\]

Thus the heights tend to infinity. \(\square\)

---

# 5. Stronger branching form

The propagation is not merely a single infinite chain.

## Theorem 5.1 — infinite branching

Let \(g(x)=y\ne x\). Then \(x\) has infinitely many immediate successors contained in \(\operatorname{supp}(g)\).

Moreover, each of those moved successors itself has infinitely many moved immediate successors.

Hence every moved vertex lies at the root of an infinitely branching forward tree contained in the moved set, after recursively choosing distinct witnesses.

### Proof

The first statement is Theorem 3.1.

If \(p\) is any moved successor, then

\[
g(p)\ne p,
\]

so applying Theorem 3.1 again to the pair \((p,g(p))\) yields infinitely many moved immediate successors of \(p\).

Recursive selection gives the desired branching tree. \(\square\)

The selected tree need not be induced: additional directed edges may occur between chosen vertices. What is guaranteed is the existence of infinitely many moved forward branches with strictly increasing height.

---

# 6. Immediate corollaries

## Corollary 6.1 — no finitary automorphisms

\[
\boxed{
 g\ne\mathrm{id}
 \Longrightarrow
 |\operatorname{supp}(g)|=\aleph_0.
}
\]

In particular, the directed prime graph has no nontrivial automorphism of finite support.

## Corollary 6.2 — no bounded-height support

If \(g\ne\mathrm{id}\), then for every \(N\) there exists a moved prime \(p\) with

\[
h(p)>N.
\]

Equivalently,

\[
\boxed{
\sup\{h(p):g(p)\ne p\}=\infty.
}
\]

## Corollary 6.3 — eventual identity implies identity

If an automorphism fixes every prime above some Pratt height, then it is the identity.

Likewise, if it fixes every sufficiently large prime in the ordinary numerical order, then it is the identity.

### Proof

A nontrivial automorphism would force moved vertices of arbitrarily large Pratt height and therefore arbitrarily large numerical size. \(\square\)

---

# 7. Minimal moved level

Let \(g\ne\mathrm{id}\), and let \(n\) be the least Pratt height at which \(g\) moves a vertex.

Then \(g\) fixes \(P_{<n}\) pointwise.

If \(x\in L_n\) is moved, then

\[
\operatorname{Pred}(g(x))
=
 g(\operatorname{Pred}(x))
=
\operatorname{Pred}(x),
\]

because all predecessors of \(x\) have smaller height and are fixed.

Therefore the first motion of every nontrivial automorphism is born inside an exact predecessor fiber:

\[
\boxed{
 x,g(x)\in X_S
\text{ for some }S.
}
\]

This matches the kernel term in the multiplicity-tower theorem.

Combining both results gives a precise birth-and-propagation law:

\[
\boxed{
\text{first motion is born inside one equal-predecessor fiber,}
}
\]

then

\[
\boxed{
\text{it must propagate through infinitely many successors to unbounded height.}
}
\]

---

# 8. Consequence for the Fermat swap

Suppose the transposition \((3\ 5)\) extends to a global automorphism \(g\).

Then every prime \(p\) satisfying

\[
3\mid p-1,
\qquad
5\nmid p-1
\]

must be moved.

There are infinitely many such primes by Dirichlet.

Likewise, every prime with

\[
5\mid p-1,
\qquad
3\nmid p-1
\]

must be moved.

Therefore any hypothetical global realization of the Fermat swap immediately forces an infinite cascade through the graph. It can never remain a local permutation of the height-one fiber.

This gives an unconditional structural statement even though the existence of such a global automorphism remains unresolved.

---

# 9. Why this is useful

The original MathOverflow question asked, after the possibility of many automorphisms was raised, what can be said unconditionally about hypothetical nontrivial automorphisms.

The propagation theorem gives a clean answer:

> A hypothetical nontrivial automorphism cannot be finitary, cannot be confined to finitely many Pratt levels, and cannot move only an isolated family of equal-predecessor vertices. Every moved prime forces infinitely many moved immediate successors, and the moved set reaches arbitrarily high Pratt height.

Thus nontrivial symmetry, if it exists, is necessarily a genuinely global phenomenon.

---

# 10. Interaction with finite-future indistinguishability

The previous strike showed

\[
\text{finite future patterns cannot distinguish }3\text{ from }5.
\]

The present strike shows the complementary fact:

\[
\text{a global swap, if it exists, must alter infinitely much of the future.}
\]

Together:

\[
\boxed{
\text{finite future is too flexible to kill symmetry,}
}

while

\[
\boxed{
\text{global symmetry is too expensive to remain local.}
}
\]

This sharply localizes the unresolved difficulty to the infinite compatibility problem encoded by the multiplicity tower.

---

# 11. Next strike

The next question is whether the moved-set propagation itself can be upgraded into a contradiction by imposing **coherent two-sided constraints** along an infinite branch.

A natural target is:

> Can one force an infinite sequence of asymmetric-successor choices whose images eventually violate an exact predecessor requirement or a Pratt-height multiplicity constraint?

If yes, this would convert propagation into rigidity.

If no, the propagation theorem becomes evidence that any nontrivial automorphism must look like an infinite back-and-forth cascade rather than a finite permutation.

For now the theorem is unconditional and does not decide existence.
