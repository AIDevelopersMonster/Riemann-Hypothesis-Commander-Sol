# HATTER-SOL-05 · Finite-Fiber Compactness and Killing Certificates

## 0. Why this theorem matters

HATTER-SOL-01 began with the maximal multiplicative symmetry

\[
\operatorname{Aut}(\mathbb N_{>0},\times)
\cong
\operatorname{Sym}(\mathbb P),
\]

while the full additive-multiplicative arithmetic is rigid.

The HATTER-SOL programme asks how much intermediate structure must be restored before prime labels become fixed.

For the radical-predecessor graph

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1,
\]

HATTER-SOL-04 reduced this question to the multiplicity tower of exact predecessor fibers

\[
X_S=\{p:\operatorname{Pred}(p)=S\},
\qquad
\mu(S)=|X_S|.
\]

HATTER-SOL-05 now studies the first seed symmetry

\[
\tau=(3\ 5).
\]

This note proves a compactness principle: **if all exact fibers are finite, then every failure of a seed symmetry is witnessed at finite Pratt height**.

Thus the global automorphism problem has a clean finite-certificate form in the finite-fiber regime.

---

# 1. Height truncations and seed extensions

Let

\[
P_{\le n}=\{p\in\mathbb P:h(p)\le n\}
\]

and

\[
G_n=\operatorname{Aut}(\Pi\upharpoonright P_{\le n}).
\]

For \(m\le n\), write

\[
\rho_{m,n}:G_n\to G_m
\]

for restriction.

Fix a seed automorphism

\[
\tau\in G_m.
\]

Define the level-\(n\) extension set

\[
T_n(\tau)
=
\{g\in G_n:\rho_{m,n}(g)=\tau\},
\qquad n\ge m.
\]

So \(T_n(\tau)\ne\varnothing\) exactly when \(\tau\) survives to height \(n\).

For the HATTER-SOL-05 seed we take

\[
m=1,
\qquad
\tau=(3\ 5).
\]

---

# 2. Finite exact fibers force finite height truncations

## Definition 2.1 — finite-fiber condition

Say that \(\Pi\) satisfies **FFC** if

\[
\boxed{
\mu(S)<\infty
}
\]

for every finite exact predecessor support \(S\subset\mathbb P\) containing \(2\).

FFC is not asserted to hold. It is a structural regime to be analyzed.

## Lemma 2.2

Under FFC, every height truncation \(P_{\le n}\) is finite.

### Proof

We proceed by induction on \(n\).

For \(n=0\),

\[
P_{\le0}=\{2\}.
\]

Assume \(P_{\le n}\) finite.

Every prime \(p\in L_{n+1}\) has a finite predecessor set

\[
S=\operatorname{Pred}(p)\subseteq P_{\le n}
\]

with

\[
\max_{q\in S}h(q)=n.
\]

Since \(P_{\le n}\) is finite, there are only finitely many possible supports \(S\). For each such \(S\), FFC says that

\[
X_S
\]

is finite. Hence

\[
L_{n+1}
=
\bigsqcup_S X_S
\]

is finite. Therefore \(P_{\le n+1}\) is finite. \(\square\)

## Corollary 2.3

Under FFC every group \(G_n\) and every extension set \(T_n(\tau)\) is finite.

---

# 3. The extension tree

Construct a rooted tree \(\mathcal T(\tau)\) as follows.

The vertices at depth \(n-m\) are the elements of

\[
T_n(\tau).
\]

A node

\[
g_{n+1}\in T_{n+1}(\tau)
\]

is joined to

\[
g_n\in T_n(\tau)
\]

when

\[
\rho_n(g_{n+1})=g_n.
\]

A global automorphism extending \(\tau\) gives an infinite branch in this tree.

Conversely, an infinite compatible branch gives a global automorphism by the inverse-limit theorem of HATTER-SOL-04.

Under FFC the tree is finitely branching because each level is finite.

---

# 4. Finite-fiber compactness theorem

## Theorem 4.1 — finite-height survival is global survival under FFC

Assume FFC. Then for every seed \(\tau\in G_m\), the following are equivalent:

1. \(\tau\) extends to a global automorphism of \(\Pi\);
2. \(\tau\) extends to every finite Pratt height;
3. \(T_n(\tau)\ne\varnothing\) for every \(n\ge m\).

Equivalently,

\[
\boxed{
\tau\text{ fails globally}
\Longrightarrow
\tau\text{ dies at some finite height}.
}
\]

### Proof

The implication \((1)\Rightarrow(2)\Rightarrow(3)\) is immediate by restriction.

Assume \((3)\). Then \(\mathcal T(\tau)\) has a nonempty level at every depth. By Corollary 2.3 it is finitely branching. König's infinity lemma gives an infinite branch

\[
g_m,g_{m+1},g_{m+2},\ldots
\]

with

\[
\rho_n(g_{n+1})=g_n.
\]

The inverse-limit theorem then defines a global automorphism \(g\in\operatorname{Aut}(\Pi)\) restricting to \(\tau\). \(\square\)

---

# 5. Finite killing certificates

The previous theorem says more than mere compactness.

Suppose \(\tau\) does not extend globally under FFC. Choose the least \(N>m\) such that

\[
T_N(\tau)=\varnothing.
\]

Then

\[
T_{N-1}(\tau)\ne\varnothing.
\]

For every candidate extension

\[
g\in T_{N-1}(\tau),
\]

the multiplicity-tower theorem says that \(g\) fails to extend to level \(N\) exactly because there exists an exact support \(S_g\) at the next layer with

\[
\boxed{
\mu(S_g)\ne\mu(gS_g).
}
\]

Since \(T_{N-1}(\tau)\) is finite, only finitely many such witnesses are required.

## Theorem 5.1 — finite killing-certificate theorem

Assume FFC and suppose \(\tau\in G_m\) has no global extension.

Then there exist a finite height \(N\) and a finite family

\[
\mathcal W
=
\{(g,S_g):g\in T_{N-1}(\tau)\}
\]

such that

\[
\mu(S_g)\ne\mu(gS_g)
\]

for every surviving candidate \(g\) at height \(N-1\).

Thus the death of \(\tau\) is certifiable by finitely many exact-fiber cardinality mismatches.

### Important refinement

At height two, a single witness of the form

\[
\mu(S)\ne\mu(\tau S)
\]

kills the seed directly.

At later heights this need not be enough, because the earlier extension steps may have multiple choices. The correct global finite certificate is therefore generally a **finite obstruction tree**, not necessarily one support pair.

This corrects an overly narrow version of the initial HATTER-SOL-05 search target.

---

# 6. Phantom survival requires an infinite fiber

A logically possible pathology in a general inverse system is:

- the seed extends to every finite level;
- yet there is no compatible infinite branch.

The finite-fiber theorem excludes this completely under FFC.

## Corollary 6.1 — infinite-fiber necessity for noncompact failure

If a seed \(\tau\) extends to every finite Pratt height but does **not** extend globally, then FFC must fail.

Hence

\[
\boxed{
\exists S\quad \mu(S)=\aleph_0.
}
\]

In words: every genuinely noncompact failure of global extension requires at least one infinite exact predecessor fiber.

This gives infinite fibers a second role in the theory. They are not merely large local symmetry reservoirs; they are also the only possible source of failure of finite-height compactness.

---

# 7. The seed transposition \(3\leftrightarrow5\)

Take

\[
\tau=(3\ 5)\in G_1.
\]

Under FFC exactly one of two alternatives occurs.

## Alternative A — finite death

There is a least height \(N\) at which every surviving extension is blocked by a finite collection of exact-support multiplicity mismatches.

Then the first multiplicative symmetry from HATTER-SOL-01 has been killed by a finite amount of radical-predecessor information.

## Alternative B — global survival

The swap survives every finite height. Then Theorem 4.1 forces a global automorphism

\[
g\in\operatorname{Aut}(\Pi),
\qquad
 g(3)=5,
\quad
 g(5)=3.
\]

There is no third possibility under FFC.

Therefore

\[
\boxed{
\text{finite fibers turn the global }3\leftrightarrow5
\text{ problem into a finite-obstruction problem.}
}
\]

---

# 8. Relation with the Higher-Fiber Infinitude regime

The previous HATTER-SOL-05 strike introduced HFI:

\[
\mu(S)=\aleph_0
\qquad
(2\in S,\ S\ne\{2\}).
\]

Under HFI the seed swap survives globally.

FFC is the opposite structural regime:

\[
\mu(S)<\infty
\qquad
\text{for every exact support }S.
\]

Thus the branch now has two clean endpoints.

### Infinite-fiber endpoint

\[
\boxed{
\text{HFI}
\Longrightarrow
3\leftrightarrow5\text{ survives globally.}
}
\]

### Finite-fiber endpoint

\[
\boxed{
\text{FFC}
\Longrightarrow
\bigl(
3\leftrightarrow5\text{ dies at finite height}
\ \text{or}\
\text{survives globally}
\bigr).
}
\]

So the genuinely difficult regime is mixed:

\[
\boxed{
\text{some exact fibers finite, others infinite.}
}
\]

That mixed regime is precisely where the cardinality wall and noncompact branching interact.

---

# 9. Why this reconnects directly to HATTER-SOL-01

The first article established

\[
\operatorname{Aut}(\mathbb N_{>0},\times)
\cong
\operatorname{Sym}(\mathbb P).
\]

The fifth article is not an unrelated study of exponential prime families. It is analyzing how one specific generator of that huge symmetry group,

\[
(3\ 5),
\]

is filtered when we restore only the weak additive shadow

\[
q\mid p-1.
\]

The continuity chain is therefore

\[
\operatorname{Sym}(\mathbb P)
\supseteq
\operatorname{Aut}(\Pi)
\supseteq
\{\mathrm{id}\}.
\]

HATTER-SOL-03 showed that a stronger predecessor relation already reaches the right endpoint.

HATTER-SOL-04 and HATTER-SOL-05 study whether the much weaker radical-predecessor relation already suffices.

The exact-fiber multiplicities

\[
\mu(S)
\]

are therefore not a side topic: they are the arithmetic mechanism by which a prime permutation from the pure multiplicative world may be killed while crossing toward rigid arithmetic.

---

# 10. Literature boundary

The abstract compactness mechanism in Theorem 4.1 is an application of König's infinity lemma to a finitely branching extension tree, and is not claimed as a new general graph-theoretic theorem.

The contribution here is its exact formulation for the radical-predecessor multiplicity tower and the resulting finite-killing-certificate interpretation of the prime-automorphism problem.

A recent paper of Languasco, Luca, Moree and Togbé, *Sequences of integers generated by two fixed primes* (Abh. Math. Semin. Univ. Hambg. 95 (2025), 123–148, DOI 10.1007/s12188-025-00293-9), studies the distribution and gaps of two-prime S-units \(p^a q^b\). It does not, in the material checked for this note, resolve infinitude of primes of the form \(p^a q^b+1\). In particular the classical Pierpont-prime infinitude problem for \(2^a3^b+1\) remains unresolved.

This matters because even the first higher exact fiber

\[
X_{\{2,3\}}
\]

already sits beyond currently known unconditional infinitude theory.

---

# 11. Revised research target

The branch should no longer insist that a single support pair must kill \((3\ 5)\).

The correct target is:

\[
\boxed{
\text{construct a finite obstruction tree for }(3\ 5)
}
\]

or prove that every finite obstruction tree can be escaped.

A successful finite obstruction tree would be enough to establish finite-height death under any regime where the relevant fibers have rigorously known finite cardinalities.

Conversely, proving systematic escape from every finite obstruction tree would move the branch toward a global survival theorem weaker than HFI.

---

# 12. Current status

This strike changes the shape of HATTER-SOL-05.

The branch now contains four logically distinct layers:

1. finite fixed-divisor coverings cannot empty an exact-support family;
2. cyclotomic factorization creates a genuine dimension jump between \(|S|=1\) and \(|S|\ge2\);
3. local sieve asymmetry between the 3-side and 5-side persists and amplifies down descendant chains, but is erased by the cardinality wall when both fibers are infinite;
4. in the all-finite regime, every global failure has a finite exact-support killing certificate.

This is now a coherent theorem package, but publication should wait for a dedicated hostile proof/literature audit of the combined fifth-paper manuscript.
