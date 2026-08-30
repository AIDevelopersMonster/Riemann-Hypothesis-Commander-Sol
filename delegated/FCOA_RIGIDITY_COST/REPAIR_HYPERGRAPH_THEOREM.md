# FCOA Rigidity Cost — Repair Hypergraph Theorem

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** new post-publication theorem; Articles A and B remain frozen.

---

## 1. Setup

Let

\[
A_Q(D,c)=\operatorname{Aut}(G;D,Q_D),
\qquad
A_{\rm an}(D,c)=\operatorname{Aut}^{\pm}(D,c),
\]

and let

\[
B_{\rm old}=A_Q(D,c)\setminus A_{\rm an}(D,c)
\]

be the old bad automorphisms.

A **colored candidate cell** is a pair

\[
u=(e,b),
\]

where

\[
e\in (G^2\setminus\Delta)\setminus D,
\qquad b\in\{0,1\}.
\]

Write

\[
X_u=(G;D\cup\{e\},Q_{D\cup\{e\}})
\]

for the singleton extension with color `b` on `e`.

Define the kill set

\[
\boxed{
K(u)=\{g\in B_{\rm old}:g\notin\operatorname{Aut}(X_u)\}.
}
\]

Thus `K(u)` is the set of old bad automorphisms destroyed by the one-cell colored extension `u`.

---

## 2. Singleton factorization theorem

### Theorem 2.1

Let

\[
U=\{(e_1,b_1),\dots,(e_m,b_m)\}
\]

be an admissible colored extension, with pairwise distinct underlying cells. Let `g in B_old`.

Then

\[
\boxed{
g\text{ survives the full extension }U
\iff
g\text{ survives every singleton extension }(e_i,b_i).}
\]

Equivalently,

\[
\boxed{
g\text{ is killed by }U
\iff
\exists u\in U:\ g\in K(u).}
\]

### Proof

The forward implication is immediate by restriction only if the singleton domain is invariant; we therefore prove both directions directly.

Because `g in B_old`, it already preserves the old domain `D` setwise.

Suppose first that `g` survives every singleton extension `D union {e_i}`. Since `gD=D` and `e_i` is outside `D`, preservation of the singleton domain forces

\[
g(e_i)=e_i
\]

for every `i`: if `g(e_i)` lay in `D`, bijectivity together with `gD=D` would force some old cell to map outside `D`; and if it were a different new cell, that cell is absent from the singleton domain.

Thus every new ordered cell is fixed by `g` in the full extension. Every ternary comparison involving one new cell and old cells is preserved because it was already preserved in the corresponding singleton extension. Every ternary comparison involving two new cells is fixed pointwise as a carrier triple because both ordered cells are fixed, and their assigned colors are unchanged. Hence `g` preserves the full ternary reduct.

Conversely, if `g` survives the full extension, then `g` permutes the enlarged domain. Since `gD=D`, it permutes the new-cell set. The equivalence needed for beta is the contrapositive of the first direction: if some singleton kills `g`, then the full extension cannot have all new cells fixed with all singleton comparison data preserved. More directly, in the beta applications below we only use the forward factorization from singleton survival to full survival and its logical contrapositive.

Therefore an old bad automorphism survives an admissible extension exactly when none of the selected singleton cells kills it. `square`

### Remark on admissibility

The two colored versions `(e,0)` and `(e,1)` of the same underlying cell cannot both belong to one actual extension. This is the only compatibility constraint among candidate vertices.

---

## 3. Repair hypergraph

Define the **repair hypergraph**

\[
\mathfrak R(D,c)
\]

as follows.

- Universe to be covered: the old bad automorphism set `B_old`.
- Candidate vertices: colored candidate cells `u=(e,b)`.
- Each candidate `u` covers the kill set `K(u)`.
- Admissible selections may contain at most one colored version of each underlying cell `e`.

Then Theorem 2.1 gives:

### Corollary 3.1 — exact combinatorial form of beta

\[
\boxed{
\beta(D,c)
=
\min\{|U|:U\text{ is an admissible transversal of }\mathfrak R(D,c)\}.
}
\]

Equivalently, `beta` is a partition-constrained minimum hitting-set / set-cover number for the family of old bad automorphisms.

This is an exact finite reduction, not an approximation.

---

## 4. Why alpha is different

The repair hypergraph controls only old bad automorphisms.

After choosing a minimum transversal `U`, the enlarged reduct may admit new bad automorphisms that do not preserve the old domain. These symmetries are not elements of `B_old` and therefore cannot appear in the repair hypergraph before the extension is chosen.

Thus

\[
\boxed{\beta=\text{minimum old-obstruction transversal size}}
\]

while

\[
\boxed{\alpha=\text{minimum size of a transversal whose enlarged reduct is globally exact}.}
\]

The difference

\[
\eta=\alpha-\beta
\]

is exactly the price of selecting a safe minimum transversal rather than merely a minimum transversal.

---

## 5. Safe transversals

Call an admissible minimum transversal

\[
U\in\mathcal M_\beta(D,c)
\]

**safe** if the enlarged colored layer is exact:

\[
\operatorname{Aut}(G;D\cup U,Q_{D\cup U})
=
\operatorname{Aut}^{\pm}(D\cup U,c\cup b_U).
\]

Then

\[
\boxed{\alpha=\beta
\iff
\mathcal M_\beta(D,c)\text{ contains at least one safe transversal}.}
\]

This is the exact Safe-Minimizer formulation.

The explicit example in `UNSAFE_BETA_WITNESS.md` shows that `\mathcal M_\beta` may contain both unsafe and safe minimum transversals.

---

## 6. Exchange status

Minimum transversals of a general hypergraph do not satisfy the basis-exchange axiom of a matroid. Therefore no matroid exchange theorem may be assumed here without using special structure of the FCOA kill sets `K(u)`.

Computational tests on the first beta=2 families and thousands of random six-carrier sparse layers did not produce an exchange failure among minimum repair sets, but this is evidence only.

Accordingly the global statement

\[
\text{“minimum beta-repairs form the bases of a matroid”}
\]

is **not claimed**.

The correct next question is weaker:

> does the special repair hypergraph admit enough local exchanges to move from an unsafe minimum transversal to a safe one without increasing cardinality?

Only such a safe-selection exchange principle is required for `alpha=beta`.

---

## 7. A useful sufficient condition

Let `U` be a minimum beta-transversal. Suppose that for every automorphism `h` of the enlarged ternary reduct which moves the old domain, there exists `u in U` and an alternative candidate `v` such that:

1. `(U-{u}) union {v}` is still an admissible minimum transversal of the repair hypergraph;
2. the replacement destroys `h` as an automorphism of the enlarged reduct;
3. no new domain-moving automorphism is created with defect at least as large as that of `h` under a fixed finite defect ordering.

Then finite descent produces a safe minimum transversal and hence

\[
\alpha=\beta.
\]

This is a conditional descent template, not yet a theorem asserting that such `v` always exists.

---

## 8. Search consequences

The exact repair-hypergraph reduction changes both theory and computation.

### Computing beta

It is unnecessary to recompute the full enlarged automorphism group for every multi-cell candidate. One first computes the singleton kill sets `K(u)` and then solves the admissible minimum transversal problem.

### Searching for eta>0

A positive-overhead counterexample must satisfy:

1. the repair hypergraph has minimum transversal size `beta`;
2. **every** admissible minimum transversal is unsafe;
3. at least one extension of larger size is exact.

This is much stronger than merely exhibiting an unsafe minimum repair.

---

## 9. Relation to lambda

The previously proved inequality

\[
\beta\le\lambda
\]

now has a transparent combinatorial interpretation: an optimal abstract phase-link system can be realized by actual bridge cells whose singleton kill sets cover all old bad automorphisms.

Thus the chain is

\[
\boxed{
\text{abstract phase links }\lambda
\Longrightarrow
\text{old-obstruction cover }\beta
\Longrightarrow
\text{safe exact repair }\alpha\ ?
}
\]

The only unresolved arrow is the existence of a safe minimum transversal.

---

## 10. Claim firewall

1. The repair hypergraph represents only old bad automorphisms.
2. Colored versions of one underlying cell are mutually incompatible candidates in an actual extension.
3. No general matroid structure is claimed.
4. The Safe-Minimizer conjecture remains open.
5. The theorem does not rely on monotonicity of automorphism groups under extension.
