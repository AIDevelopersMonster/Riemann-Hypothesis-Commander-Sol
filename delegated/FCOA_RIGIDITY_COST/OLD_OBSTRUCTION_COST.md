# FCOA Rigidity Cost — Old-Obstruction Cost and Symmetry-Creation Overhead

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** new post-publication structural theorem; Articles A and B remain frozen.

---

## 1. Motivation

Article B defines:

- `lambda(D,c)` — fixed-domain abstract phase-link cost;
- `alpha(D,c)` — actual operation-cell extension cost needed to make the enlarged ternary reduct exact.

The No-old-obstruction theorem shows that a `lambda`-cell bridge realization kills every **old** non-global phase obstruction. If exactness still fails, the culprit is a carrier symmetry created by the extension and moving the old domain.

This suggests inserting a third quantity which measures exactly the cost of killing old bad automorphisms before asking whether new ones appear.

---

## 2. Old bad automorphisms

Let

\[
A_Q(D,c)=\operatorname{Aut}(G;D,Q_D)
\]

and

\[
A_{\rm an}(D,c)=\operatorname{Aut}^{\pm}(D,c).
\]

Define the old bad set

\[
\boxed{
B_{\rm old}(D,c)=A_Q(D,c)\setminus A_{\rm an}(D,c).
}
\]

These are exactly the carrier permutations responsible for nonexactness of the original ternary reduct.

For an admissible colored extension `(E,b)`, put

\[
D'=D\cup E,
\qquad
c'=c\cup b.
\]

An old bad automorphism `g` **survives** the extension when

\[
g\in\operatorname{Aut}(G;D',Q_{D'}).
\]

It need not preserve the colors globally; survival refers only to the enlarged ternary reduct.

---

## 3. Definition of beta

Define the **old-obstruction cell cost**

\[
\boxed{
\beta(D,c)
=
\min\{|E|:
B_{\rm old}(D,c)
\cap
\operatorname{Aut}(G;D\cup E,Q_{D\cup E})
=\varnothing
\},
}
\]

where the minimum ranges over admissible new cells and their binary terminal values.

Thus:

- `beta` asks only that every old bad symmetry be destroyed;
- `alpha` asks that the enlarged reduct contain **no** bad symmetry at all, including newly created symmetries.

This is the exact formal separation between phase repair and symmetry creation under extension.

---

## 4. Basic inequalities

### Theorem 4.1

For every finite sparse binary anonymous layer,

\[
\boxed{
0\le\beta(D,c)\le\alpha(D,c)
}
\]

and

\[
\boxed{
\beta(D,c)\le\lambda(D,c).
}
\]

Hence

\[
\boxed{
\beta(D,c)
\le
\min\{\alpha(D,c),\lambda(D,c)\}.
}
\]

### Proof

If an extension is exact, no old bad automorphism survives in its ternary reduct. Therefore every extension witnessing `alpha` also witnesses the defining condition for `beta`, giving

\[
\beta\le\alpha.
\]

For the second inequality, choose an optimal abstract link system of size `lambda` and realize each link by one actual bridge cell as in the One-Cell Bridge Lemma. The No-old-obstruction theorem of Article B implies that every automorphism of the enlarged ternary reduct which still preserves the old domain is globally admissible on the old layer. In particular no member of `B_old(D,c)` survives. Thus the `lambda` bridge cells witness

\[
\beta\le\lambda.
\]

\(\square\)

---

## 5. Symmetry-creation overhead

Define

\[
\boxed{
\eta(D,c)=\alpha(D,c)-\beta(D,c)\ge0.
}
\]

Call `eta` the **symmetry-creation overhead**.

It measures how many additional real cells are required, beyond the cheapest destruction of all old bad automorphisms, because the extension process may create new bad carrier symmetries.

The original conjecture

\[
\alpha(D,c)\le\lambda(D,c)
\]

can now fail only if

\[
\boxed{
\eta(D,c)>\lambda(D,c)-\beta(D,c).
}
\]

Thus the conjecture is not fundamentally about old phase synchronization: that part is already bounded by `lambda`. It is a quantitative statement about how much symmetry-creation overhead can be forced.

---

## 6. Stronger target

A strictly stronger statement than Conjecture 14 is

\[
\boxed{
\alpha(D,c)=\beta(D,c)
\qquad\text{for all sparse binary layers.}
}
\]

Equivalently,

\[
\boxed{
\eta(D,c)=0.
}
\]

This says that old bad symmetries can always be killed by an extension of minimum old-obstruction size **without paying any extra cells for newly created symmetries**.

No proof is currently claimed. It is a sharper research target because it isolates the only remaining mechanism identified by the deletion-symmetry analysis.

Even if `alpha=beta` is false, a uniform bound on `eta` would immediately sharpen the original cost theory.

---

## 7. Immediate counterexample constraints

If Conjecture 14 fails, then necessarily

\[
\beta\le\lambda<\alpha.
\]

Therefore every counterexample has strictly positive overhead

\[
\boxed{\eta>0.}
\]

and no counterexample can arise solely from failure to kill the old realized phase cocycle.

A minimal counterexample must exhibit the following phenomenon:

> every extension of size at most `lambda` which destroys all old bad automorphisms creates at least one new bad automorphism of the enlarged ternary reduct.

This is stronger than the earlier statement that one particular bridge realization may create symmetry.

---

## 8. Full phase-capacity corollary

If the realized component phase set is the full binary cube

\[
\Sigma(D,c)=\mathbf F_2^r,
\]

then

\[
\lambda(D,c)=r-1.
\]

Article B already gives

\[
\alpha(D,c)\le r-1.
\]

Hence

\[
\boxed{
\Sigma(D,c)=\mathbf F_2^r
\Longrightarrow
\alpha(D,c)\le\lambda(D,c).
}
\]

Therefore any counterexample to Conjecture 14 must have **restricted realized phase capacity**:

\[
\boxed{
\Sigma(D,c)\subsetneq\mathbf F_2^r.
}
\]

This removes the maximally independent phase families from the search entirely, including the disjoint-pair and independent-flip models.

More generally, a counterexample must satisfy

\[
\lambda(D,c)<r-1
\]

or else the universal `alpha<=r-1` bound already proves the conjectured inequality.

---

## 9. Relation to the disjoint-pair exact theorem

For the disjoint oppositely colored bidirected-pair family,

\[
\lambda_r=r-1,
\qquad
\alpha_r=\left\lceil\frac r2\right\rceil.
\]

The lower-bound argument shows that every untouched pair retains an old local bad transposition. The explicit `a-a` bridge construction simultaneously destroys all old bad symmetries and yields an exact extension. Consequently

\[
\boxed{
\beta_r=\alpha_r=\left\lceil\frac r2\right\rceil,
\qquad
\eta_r=0.
}
\]

Thus this infinite family has genuine `alpha>1` but zero symmetry-creation overhead.

The hub family of Article B likewise has

\[
\beta=\alpha=1,
\qquad
\eta=0.
\]

So all currently understood extremal families have zero overhead.

---

## 10. New search strategy

Future computational searches for `alpha>lambda` should no longer spend equal effort on all nonexact layers.

Priority filters are now:

1. disconnected `Lambda(D)`;
2. nontrivial old bad set;
3. restricted phase capacity `Sigma != F_2^r`;
4. `lambda < r-1`;
5. compute `beta` before computing full `alpha`;
6. search specifically for positive overhead `eta=alpha-beta`.

The first decisive new object is therefore not merely a layer with large `alpha`, but a layer with

\[
\boxed{\eta>0.}
\]

Such a layer would be the first genuine example of unavoidable symmetry-creation cost.

---

## 11. Claim firewall

1. `beta` is an operation-cell count, but it only controls survival of automorphisms that were already bad in the original reduct.
2. `eta` is defined from minima and need not be realized by nesting an optimal beta-extension inside an optimal alpha-extension.
3. `alpha=beta` is a new conjectural strengthening, not a theorem.
4. The full-phase-capacity corollary is theorem-level and follows immediately from the published universal bound.
5. Articles A and B are immutable foundations; this note is post-publication research.
