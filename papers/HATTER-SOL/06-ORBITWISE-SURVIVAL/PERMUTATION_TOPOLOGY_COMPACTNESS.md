# HATTER-SOL-06 · Permutation-Topology Compactness

## 0. Purpose

The previous strike introduced the Eventual Bi-Finite Image property (EBFI) and proved, by a diagonal stabilization argument, that

\[
\text{arbitrarily deep finite survival}+\mathrm{EBFI}
\Longrightarrow
\text{global survival}.
\]

This note identifies the exact topology behind that argument.

The point is not cosmetic. It shows that EBFI is the natural compactness condition in the infinite symmetric group, and that noncompact death is literally escape from every compact set in the permutation topology.

This gives a conceptual form of the finite-image theorem and cleanly separates three regimes:

\[
\boxed{
\text{profinite compactness}
\;/\;
\text{permutation-topology precompactness}
\;/\;
\text{genuine image escape}.
}
\]

---

# 1. The permutation topology

Let

\[
\Omega=\mathbb P
\]

be the countable set of primes and let

\[
S_\infty=\operatorname{Sym}(\Omega).
\]

Give \(\Omega\) the discrete topology and \(S_\infty\) the topology of pointwise convergence.

A basic neighborhood of a permutation \(g\) is determined by finitely many values

\[
g(p_1),\dots,g(p_k).
\]

Equivalently, a sequence \((g_j)\) converges to \(g\) iff for every prime \(p\),

\[
g_j(p)=g(p)
\]

for all sufficiently large \(j\).

Inversion is continuous in this topology.

The graph automorphism group

\[
\operatorname{Aut}(\Pi)
\subseteq S_\infty
\]

is closed, because preservation of each edge and nonedge is a finite coordinate condition.

---

# 2. Why forward pointwise control alone is insufficient

A sequence of permutations can converge pointwise in \(\Omega^\Omega\) to an injective but non-surjective map.

For example, on \(\mathbb N\), let

\[
g_n=(1\ 2\ \cdots\ n).
\]

Then for each fixed \(k\),

\[
g_n(k)=k+1
\]

for all large \(n\). Thus \(g_n\) converges pointwise to the unilateral shift

\[
k\mapsto k+1,
\]

which is not a permutation.

The missing point is visible in the inverse maps:

\[
g_n^{-1}(1)=n
\]

escapes to infinity.

This is exactly why HATTER-SOL-06 required finite control of both possible images and possible preimages.

---

# 3. A compactness criterion for sets of permutations

For

\[
K\subseteq S_\infty
\]

and \(p\in\Omega\), define

\[
Kp=\{g(p):g\in K\},
\]

\[
K^{-1}p=\{g^{-1}(p):g\in K\}.
\]

## Theorem 3.1 — bi-finite orbit criterion

For a subset \(K\subseteq S_\infty\), the following are equivalent:

1. the closure of \(K\) in \(S_\infty\) is compact;
2. for every \(p\in\Omega\), both sets
   \[
   Kp
   \quad\text{and}\quad
   K^{-1}p
   \]
   are finite.

### Proof

Assume (1). Evaluation at a point,

\[
\operatorname{ev}_p:S_\infty\to\Omega,
\qquad
\operatorname{ev}_p(g)=g(p),
\]

is continuous. The image of a compact set under a continuous map is compact. Since \(\Omega\) is discrete, compact subsets of \(\Omega\) are finite. Therefore

\[
Kp
\]

is finite. Applying the same argument after the continuous inversion map gives finiteness of

\[
K^{-1}p.
\]

Now assume (2). Consider the embedding

\[
\iota:S_\infty\to\Omega^\Omega\times\Omega^\Omega,
\qquad
\iota(g)=(g,g^{-1}).
\]

For each \(p\), the first coordinate values lie in the finite set \(Kp\), and the inverse-coordinate values lie in the finite set \(K^{-1}p\). Hence

\[
\iota(K)
\subseteq
\prod_{p\in\Omega}Kp
\times
\prod_{p\in\Omega}K^{-1}p.
\]

The right-hand side is compact by Tychonoff's theorem, since every factor is finite discrete.

Take a limit point

\[
(f,h)
\]

of \(\iota(K)\) in this product. For every \(p\), the identities

\[
h(g(p))=p,
\qquad
 g(h(p))=p
\]

hold coordinatewise for every \((g,g^{-1})\in\iota(K)\). Because all relevant coordinates are eventually constant along a convergent net, the identities pass to the limit:

\[
h(f(p))=p,
\qquad
 f(h(p))=p.
\]

Thus

\[
h=f^{-1},
\]

so \(f\in S_\infty\). Therefore the closure of \(\iota(K)\) stays inside \(\iota(S_\infty)\), and it is compact. Pulling back through \(\iota\), the closure of \(K\) in \(S_\infty\) is compact. \(\square\)

Thus **bi-finite coordinate orbits are exactly precompactness in the permutation topology**.

---

# 4. Finite-height extensions as full permutations

Fix a seed

\[
\tau\in G_m
\]

and its causal cone

\[
C=C^+(\operatorname{supp}\tau).
\]

Let

\[
g_n\in\mathcal T_n^C(\tau)
\]

be a cone-localized extension to Pratt height \(n\).

Extend \(g_n\) to a full permutation

\[
\widehat g_n\in S_\infty
\]

by setting

\[
\widehat g_n(p)=p
\qquad
\text{for }p\notin P_{\le n}.
\]

This completion is not asserted to be a graph automorphism above height \(n\). It is only a convenient representative in \(S_\infty\).

If

\[
n_1<n_2<\cdots\to\infty
\]

and \(g_{n_j}\in\mathcal T_{n_j}^C(\tau)\), then any permutation-topology cluster point of

\[
\widehat g_{n_j}
\]

is automatically a global graph automorphism.

## Lemma 4.1

Let

\[
\widehat g_{n_{j_k}}\to g\in S_\infty.
\]

Then

\[
g\in\operatorname{Aut}(\Pi),
\]

\[
g|_{P_{\le m}}=\tau,
\]

and

\[
g(p)=p
\qquad(p\notin C).
\]

### Proof

Fix primes \(p,q\). For all sufficiently large \(k\),

\[
p,q\in P_{\le n_{j_k}}.
\]

On that truncation, \(g_{n_{j_k}}\) preserves \(D\). Pointwise convergence means the values of \(p\) and \(q\) are eventually equal to \(g(p)\) and \(g(q)\). Hence

\[
D(p,q)
\iff
D(g(p),g(q)).
\]

Thus \(g\) is a graph automorphism. Seed agreement and complement fixing also pass to the pointwise limit. \(\square\)

---

# 5. EBFI is asymptotic precompactness

Recall the deep image sets

\[
I_H^+(p)
=
\left\{
q:\exists n\ge H,\ \exists g_n\in\mathcal T_n^C(\tau),\ g_n(p)=q
\right\},
\]

and

\[
I_H^-(p)
=
\left\{
q:\exists n\ge H,\ \exists g_n\in\mathcal T_n^C(\tau),\ g_n^{-1}(p)=q
\right\}.
\]

EBFI says that for every prime \(p\), both sets become finite after some horizon depending on \(p\).

## Theorem 5.1 — topological form of EBFI

Assume extensions exist to arbitrarily large finite heights. Then EBFI is equivalent to the following statement:

> For every sequence
> \[
> n_1<n_2<\cdots\to\infty
> \]
> and every choice
> \[
> g_{n_j}\in\mathcal T_{n_j}^C(\tau),
> \]
> the completed permutations \(\widehat g_{n_j}\) contain a subsequence whose closure in \(S_\infty\) is compact.

### Proof

Assume EBFI. Fix a sequence \(\widehat g_{n_j}\). For any prime \(p\), choose \(H(p)\) so that

\[
I_{H(p)}^+(p),\ I_{H(p)}^-(p)
\]

are finite. Since \(n_j\to\infty\), all but finitely many \(n_j\) exceed \(H(p)\). Therefore the total coordinate sets

\[
\{\widehat g_{n_j}(p):j\ge1\}
\]

and

\[
\{\widehat g_{n_j}^{-1}(p):j\ge1\}
\]

are finite: the early terms contribute only finitely many extra values, and the tail lies in the finite deep image sets.

By Theorem 3.1, the closure of the whole chosen sequence is already compact; a fortiori it has compactly convergent subsequences.

Conversely, suppose EBFI fails. Then for some prime \(p\), one of the nested sets

\[
I_H^+(p),\ I_H^-(p)
\]

is infinite for arbitrarily large \(H\), hence for every sufficiently large \(H\). Choose inductively increasing heights and extensions for which the corresponding image or preimage of \(p\) is new each time. The resulting sequence has an infinite coordinate orbit and therefore cannot have compact closure by Theorem 3.1. \(\square\)

---

# 6. Global survival as a compactness consequence

## Corollary 6.1

If cone-localized extensions of \(\tau\) exist to arbitrarily large finite heights and EBFI holds, then \(\tau\) has a global cone-localized extension.

### Proof

Choose one extension at each height in an increasing sequence. By Theorem 5.1 the completed permutations have compact closure in \(S_\infty\), hence a cluster point. Lemma 4.1 turns that cluster point into a global graph automorphism extending \(\tau\). \(\square\)

This recovers the earlier diagonal proof, but now as a direct compactness theorem in the natural ambient topological group.

---

# 7. Noncompact death is topological escape

## Theorem 7.1 — topological escape criterion

Assume \(\tau\) extends to arbitrarily large finite heights but has no global cone-localized extension.

Then every sufficiently deep family of finite-height extension approximants is non-precompact in \(S_\infty\).

Equivalently, there exists a prime \(p\) for which forward images or inverse images escape every finite set:

\[
\boxed{
|I_H^+(p)|=\infty\ \text{for all large }H
}
\]

or

\[
\boxed{
|I_H^-(p)|=\infty\ \text{for all large }H.
}
\]

### Proof

If some deep extension family were precompact, choose approximants at arbitrarily large heights inside it. Compactness would give a cluster point in \(S_\infty\), and Lemma 4.1 would yield a global extension, contradiction.

The coordinate-escape formulation follows from Theorem 3.1. \(\square\)

So **noncompact death is not merely a metaphor**: it is precisely failure of precompactness in the permutation topology.

---

# 8. FFC becomes profinite compactness

Under the finite-fiber condition (FFC), every Pratt truncation

\[
P_{\le n}
\]

is finite.

Hence

\[
G_n=\operatorname{Aut}(\Pi|P_{\le n})
\]

is a finite group.

The global automorphism group is the inverse limit

\[
\operatorname{Aut}(\Pi)
\cong
\varprojlim G_n.
\]

Therefore:

## Theorem 8.1 — profinite regime

Under FFC,

\[
\boxed{
\operatorname{Aut}(\Pi)
\text{ is a profinite compact group.}
}
\]

The finite-fiber compactness theorem from HATTER-SOL-05 is thus exactly the ordinary compactness of an inverse limit of finite discrete groups.

The transition to infinite exact fibers is a transition from an automatically profinite setting to a potentially non-precompact permutation-group setting.

---

# 9. The three compactness regimes

The previous results organize the survival problem into three distinct levels.

## Regime I — FFC / profinite

All relevant fibers are finite. Finite-height groups are finite and the inverse limit is compact automatically.

Arbitrarily deep finite survival forces a global branch.

## Regime II — infinite fibers but EBFI

Finite-height groups may be infinite, but future arithmetic eventually restricts the possible image and preimage of each prime to a finite set.

The approximating permutations are still precompact in \(S_\infty\), so global survival follows.

## Regime III — genuine noncompact escape

Some prime keeps infinitely many possible images or preimages arbitrarily deep into the extension tower.

Only here can arbitrarily deep finite survival coexist with global death.

Thus:

\[
\boxed{
\text{the real compactness wall is not “finite versus infinite fibers”}
}
\]

but rather

\[
\boxed{
\text{precompact versus escaping coordinate orbits in }S_\infty.
}
\]

---

# 10. Consequence for the first escape channel

For the seed

\[
\tau=(3\ 5),
\]

suppose the first genuine image escape occurs at

\[
p=7\in X_{\{2,3\}}.
\]

Then its possible images lie in

\[
X_{\{2,5\}}.
\]

The topological theorem says that noncompact death through this channel requires more than the existence of many candidates. It requires an infinite set of candidates that remains visible arbitrarily far into the extension tower:

\[
\forall H\gg1,
\qquad
|I_H^+(7)\cap X_{\{2,5\}}|=\infty.
\]

Equivalently, no finite subset of \(X_{\{2,5\}}\) may eventually capture all sufficiently deep possible images of \(7\).

This is the precise object that the next arithmetic strike must attack.

---

# 11. Why the direct arithmetic attack is hard

A candidate image

\[
q\in X_{\{2,5\}}
\]

has the form

\[
q=1+2^a5^b
\]

with \(a,b\ge1\).

Already one level deeper, mapping

\[
7\mapsto q
\]

requires matching the pure exact fiber

\[
X_{\{2,7\}}
\]

with

\[
X_{\{2,q\}}.
\]

Thus even the first fixed-parameter descendant test contains the generalized Pierpont-prime cardinality problem

\[
\left|\{r:r=1+2^u7^v\text{ prime},\ u,v\ge1\}\right|
\stackrel?=
\left|\{r:r=1+2^cq^d\text{ prime},\ c,d\ge1\}\right|.
\]

No finiteness or infinitude theorem sufficient to resolve this comparison is established here.

Moreover, HATTER-SOL-05 already proved that finite fixed-divisor coverings cannot annihilate these candidate exponent lattices. Therefore a finite congruence-cover argument cannot by itself close the channel.

The topological reformulation is useful precisely because it tells us what weaker statement would suffice: we do **not** need to determine the full cardinality of every such fiber. It is enough to show that sufficiently deep future constraints leave only finitely many possible root images.

---

# 12. New target: precompactness without fiber finiteness

The next prime-specific problem can now be stated cleanly.

For \(p=7\), define

\[
J_H(7)
=
I_H^+(7)\cap X_{\{2,5\}}.
\]

Prove either:

\[
\boxed{
\exists H\quad |J_H(7)|<\infty,
}
\]

which closes the first forward escape channel, or construct an explicit sequence

\[
q_1,q_2,q_3,\dots\in X_{\{2,5\}}
\]

with

\[
q_j\in J_{H_j}(7),
\qquad
H_j\to\infty,
\]

which would be the first genuine arithmetic evidence for noncompact death.

This is strictly weaker than deciding whether \(X_{\{2,5\}}\) itself is finite or infinite.

---

# 13. Status

This strike establishes:

1. the exact compactness criterion for subsets of the infinite symmetric group in terms of finite forward and inverse coordinate orbits;
2. the identification of EBFI with asymptotic precompactness of finite-height extension approximants;
3. a topological proof of the EBFI global-survival theorem;
4. the equivalence of noncompact death with genuine coordinate escape;
5. the interpretation of FFC as the profinite compact regime;
6. a three-regime compactness taxonomy for the multiplicity tower;
7. a precise topological formulation of the first escape channel \(7\to X_{\{2,5\}}\).

The next strike remains arithmetic:

\[
\boxed{
\text{prove eventual finiteness of }J_H(7)
\text{ or produce a certified escaping sequence.}
}
\]

HATTER-SOL-06 remains active research.
