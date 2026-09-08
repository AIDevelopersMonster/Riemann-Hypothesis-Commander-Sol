# FCOA Rigidity Cost — Actual Cell-Extension Cost

**Direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Status:** local theorem/optimization note for upstream hostile review  
**Scope:** sparse off-diagonal generic domains with two anonymous terminal outputs  
**Upstream boundary:** this note does not modify G4 or the published M0–G2 checkpoint.

Let

\[
D\subseteq G^2\setminus\Delta,
\qquad c:D\to\{0,1\}
\]

be the current sparse binary anonymous terminal layer, and let

\[
Q_D(x,y,z)\iff (x,y),(y,z)\in D\text{ and }c(x,y)=c(y,z).
\]

Write

\[
\Lambda(D)
\]

for the ordered-cell incidence graph from `SPARSE_DOMAIN_PHASE_THEOREM.md`, and

\[
r=\kappa(\Lambda(D)).
\]

---

## 1. Actual extension cost

An **admissible cell extension** is a pair

\[
(E,b)
\]

with

\[
E\subseteq (G^2\setminus\Delta)\setminus D,
\qquad
b:E\to\{0,1\}.
\]

It produces

\[
D'=D\cup E,
\qquad
c'=c\cup b.
\]

Define the **actual cell-extension cost**

\[
\boxed{
\alpha(D,c)
=
\min\{|E|:\operatorname{Aut}(G;D',Q_{D'})
=
\operatorname{Aut}^{\pm}(D',c')\}.
}
\]

Thus `alpha` counts real new operation cells, not abstract comparison links.

If the original reduct is already exact, then

\[
\alpha(D,c)=0.
\]

---

## 2. One-cell bridge lemma

### Lemma

Let C and C' be two distinct connected components of \(\Lambda(D)\). Then there exists one undefined non-loop cell

\[
e\notin D
\]

which, after being added, is adjacent in the enlarged cell-incidence graph to at least one cell of C and at least one cell of C'.

### Proof

Choose

\[
p=(a,b)\in C,
\qquad
q=(c,d)\in C'.
\]

The two natural bridge candidates are

\[
(b,c)
\qquad\text{and}\qquad
(d,a).
\]

If both were loops, then

\[
b=c,
\qquad d=a,
\]

so

\[
q=(b,a).
\]

But then p and q are already composable in both directions and lie in the same component, contradiction.

Hence at least one candidate is a non-loop cell. If such a candidate were already in D, it would itself be adjacent to p and q, again connecting C and C'. Therefore a non-loop undefined bridge exists. \(\square\)

The color assigned to the new bridge cell is irrelevant to connectivity.

---

## 3. Universal upper bound

Repeatedly apply the bridge lemma along a spanning tree on the r components.

After at most

\[
r-1
\]

new cells, the enlarged incidence graph is connected. By the Sparse-Domain Phase Theorem, connectedness implies exactness of the ternary reduct.

Therefore

\[
\boxed{
\alpha(D,c)\le r-1.
}
\]

This bound is unconditional for every sparse binary layer.

Define also the **connectivity repair number**

\[
\mu(D)=
\min\{|E|:\Lambda(D\cup E)\text{ is connected}\}.
\]

Then

\[
\boxed{
\alpha(D,c)\le\mu(D)\le r-1.
}
\]

The first inequality can be strict because exactness may occur while the cell-incidence graph remains disconnected.

---

## 4. Actual cost can be zero while connectivity repair is positive

If the sparse domain itself is carrier-rigid,

\[
\operatorname{Aut}(G,D)=1,
\]

then

\[
\operatorname{Aut}(G;D,Q_D)=1
\]

for every binary coloring c. Hence

\[
\boxed{
\alpha(D,c)=0
}
\]

regardless of the number of connected components of \(\Lambda(D)\).

So neither

\[
r-1
\]

nor

\[
\mu(D)
\]

is a lower bound for actual repair cost.

---

## 5. Unbounded gap between lambda and actual cell cost

The fixed-domain phase-link number \(\lambda(D,c)\) from `SPARSE_DOMAIN_PHASE_THEOREM.md` counts abstract component-equality constraints. It can be arbitrarily larger than actual operation-cell cost.

### Construction

Fix r>=2. Use carrier

\[
G=\{h,t\}\cup\{a_i,b_i:1\le i\le r\}.
\]

For each i define a domain component

\[
D_i=
\{(a_i,h),(b_i,h),(a_i,b_i),(b_i,a_i)\}.
\]

Set

\[
D=\bigsqcup_{i=1}^r D_i.
\]

The components are pairwise disconnected in \(\Lambda(D)\). Indeed, every cell of D_i that can continue composition has its other endpoint among \(a_i,b_i,h\), and there is no cell starting at h; private endpoints do not occur in another D_j.

Color each component by

\[
c(a_i,h)=0,
\qquad c(b_i,h)=1,
\]

\[
c(a_i,b_i)=0,
\qquad c(b_i,a_i)=1.
\]

The transposition

\[
s_i=(a_i\ b_i)
\]

preserves D, acts trivially outside the i-th private pair, and flips every color in D_i while fixing all other components.

Therefore the ternary reduct realizes all independent component phase flips:

\[
\boxed{
(C_2)^r\le\operatorname{Aut}(G;D,Q_D).
}
\]

The full anonymous layer permits only global simultaneous phase reversal. Thus the fixed-domain phase-link number is

\[
\boxed{
\lambda(D,c)=r-1.
}
\]

### One-cell repair

Now add the single cell

\[
e=(h,t)
\]

with either color.

It is adjacent to every cell

\[
(a_i,h),\quad(b_i,h),
\]

so the enlarged incidence graph becomes connected immediately.

Hence

\[
\boxed{
\alpha(D,c)=1.
}
\]

Therefore

\[
\boxed{
\lambda(D,c)-\alpha(D,c)=r-2,
}
\]

which is unbounded as r grows.

Equivalently,

\[
\boxed{
\frac{\lambda(D,c)}{\alpha(D,c)}=r-1
}
\]

for this family.

Thus one real operation cell can synchronize arbitrarily many abstract component phases at once.

---

## 6. Why one cell can beat many abstract links

An abstract phase link compares two pre-existing components.

A real operation cell is more powerful. The new cell becomes a new vertex of the incidence graph and may be adjacent simultaneously to cells in many old components.

For a candidate new cell

\[
e=(x,y),
\]

define its old-component touch set

\[
\boxed{
\mathcal T_D(e)
=
\{C\in\pi_0(\Lambda(D)):
\exists p\in C\text{ adjacent to }e\}.
}
\]

One cell can merge every component in \(\mathcal T_D(e)\) into one new component.

The hub construction above has

\[
|\mathcal T_D(h,t)|=r.
\]

This is the structural reason actual cell cost can be much smaller than lambda.

---

## 7. Connectivity-repair hypergraph viewpoint

The family of touch sets

\[
\mathcal H_D
=
\{\mathcal T_D(e):e\in(G^2\setminus\Delta)\setminus D\}
\]

forms a hypergraph on the component set of \(\Lambda(D)\).

Ignoring interactions among newly added cells, connectivity repair is a hypergraph-connection problem: choose as few candidate cells as possible so that their touch sets connect all old components.

This suggests a domain-only compression parameter

\[
\mu(D),
\]

with

\[
1\le\mu(D)\le r-1
\]

when r>1 and no single candidate cell touches every component.

But actual cost may satisfy

\[
\alpha(D,c)<\mu(D)
\]

because exactness needs only elimination of realized non-diagonal phase signatures, not full incidence connectivity.

---

## 8. Relation between alpha and lambda

The current theorem status is:

\[
\boxed{
0\le\alpha(D,c)\le r-1,
}
\]

\[
\boxed{
0\le\lambda(D,c)\le r-1,
}
\]

and there is an explicit family with

\[
\boxed{
\alpha(D,c)=1,
\qquad
\lambda(D,c)=r-1.
}
\]

Hence there is no lower bound of the form

\[
\alpha\ge f(\lambda)
\]

with f growing unboundedly.

### Opposite inequality

No example with

\[
\alpha(D,c)>\lambda(D,c)
\]

was found in exhaustive very-small cases or targeted finite searches, but a general proof of

\[
\alpha(D,c)\le\lambda(D,c)
\]

is **not accepted**.

The obstruction to an immediate proof is real: after adding a cell, the enlarged domain may acquire carrier automorphisms that did not preserve the original subdomain D. Therefore an abstract set of phase links for the old action does not automatically translate one-for-one into safe operation-cell additions.

Accordingly the statement

\[
\alpha\le\lambda
\]

is retained only as an open candidate, not as a theorem.

---

## 9. Exact optimization formulation

The actual cell cost has the exact but non-monotone optimization form

\[
\boxed{
\alpha(D,c)
=
\min_{E,b}
\left\{
|E|:
\Sigma(D\cup E,c\cup b)
\subseteq
\Delta_{\kappa(\Lambda(D\cup E))}
\right\},
}
\]

where \(\Sigma\) is the realized phase-signature set of the enlarged ternary reduct and \(\Delta\) is the corresponding diagonal phase set.

This formulation is exact because it recomputes the carrier action after extension; it does not assume that old automorphisms are the only candidates.

The optimization is non-monotone at the group level: adding cells can destroy old symmetries but can also make previously distinguishable domain cells structurally exchangeable. The safe universal route is therefore connectivity, which is why \(r-1\) survives as an unconditional upper bound.

---

## 10. Three distinct cost parameters

The sparse binary problem now has three genuinely different costs:

\[
\boxed{
\lambda(D,c)
=
\text{fixed-domain abstract phase-link cost},
}
\]

\[
\boxed{
\mu(D)
=
\text{domain-only incidence connectivity repair cost},
}
\]

\[
\boxed{
\alpha(D,c)
=
\text{actual operation-cell exactness repair cost}.
}
\]

Universally,

\[
\boxed{
\alpha(D,c)\le\mu(D)\le r-1.
}
\]

There is no universal ordering between lambda and mu, and the family in Section 5 proves that lambda can exceed alpha by an arbitrarily large amount.

Whether alpha can exceed lambda remains open.

---

## 11. FCOA passport

- **Carrier/signature:** sparse off-diagonal generic terminal layer.
- **Output alphabet:** exactly two anonymous terminal values.
- **Actual extension cost:** alpha(D,c).
- **Fixed-domain phase cost:** lambda(D,c).
- **Connectivity repair cost:** mu(D).
- **Universal bound:** alpha <= mu <= kappa(Lambda(D))-1.
- **Unbounded separation:** lambda=r-1 while alpha=1 for an explicit r-component family.
- **Mechanism of separation:** one new cell may touch and merge arbitrarily many old cell-incidence components.
- **Opposite separation alpha>lambda:** not established; no theorem claimed.
- **Ordinary arithmetic imported:** no.

---

## 12. Claim firewall

1. Alpha is defined relative to repair of the ternary anonymous equality reduct, not necessarily full rigidity `Aut=1`.
2. New cells use the same two anonymous terminal outputs; no new carrier points are added.
3. Lambda is not an operation-cell count and may overestimate actual repair by an unbounded factor.
4. The conjectural inequality `alpha<=lambda` is explicitly not claimed.
5. The upper bound `alpha<=r-1` is theorem-level via the one-cell bridge lemma and connectedness criterion.
6. Nothing here changes the status of G4 itself.