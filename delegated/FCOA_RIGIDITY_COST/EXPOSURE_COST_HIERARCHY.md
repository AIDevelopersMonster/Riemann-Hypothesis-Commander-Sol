# FCOA Rigidity Cost — Exposure Cost Hierarchy

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.  
**Status:** post-publication theorem ledger.

---

## 1. Why component count is still too coarse

Article B separated three costs:

\[
\lambda(D,c),\qquad \mu(D),\qquad \alpha(D,c).
\]

The post-publication disjoint-pair theorem shows that a fourth layer is needed. The relevant question is not only which phase components exist, but which carrier vertices allow a new operation cell to interact with a specific old bad automorphism.

---

## 2. Bad automorphisms and their exposure sets

Let

\[
A_Q=\operatorname{Aut}(G;D,Q_D)
\]

and let

\[
B(D,c)=A_Q\setminus\operatorname{Aut}^{\pm}(D,c)
\]

be the set of old bad automorphisms.

For \(g\in B(D,c)\), let

\[
\delta_g(p)=c(gp)\oplus c(p)
\]

on old defined cells.

Define the **exposure set**

\[
\boxed{
X(g)=\operatorname{supp}_G(g)
\cup
\bigcup_{\delta_g(p)=1}\operatorname{endpoints}(p).
}
\]

Thus `X(g)` contains

1. every carrier point moved by `g`; and
2. every carrier point occurring in an old cell on which `g` has phase discrepancy 1.

The second term is essential. In the hub family, the common hub `h` is fixed by each local flip but lies on phase-1 cells, and the single added cell `(h,t)` kills every local flip.

---

## 3. Exposure persistence lemma

### Lemma

Let \(g\in B(D,c)\). Let \((E,b)\) be an extension such that no endpoint of any cell of \(E\) lies in \(X(g)\). Then `g` remains a bad automorphism of the extended sparse ternary reduct.

### Proof

Because every endpoint of every new cell lies outside `supp_G(g)`, `g` fixes every new cell pointwise and hence preserves its assigned color.

A new cell cannot be composable with an old cell `p` having `delta_g(p)=1`, because any shared middle endpoint would be an endpoint of `p` and therefore lie in `X(g)`.

Thus every new-old ternary comparison visible to `Q` involves only old cells with discrepancy 0. Equality/non-equality is preserved there. New-new comparisons are fixed pointwise. Old-old comparisons were already preserved because `g in A_Q`.

Therefore `g` remains in the automorphism group of the extended reduct. Its restriction to the old colored layer is still non-global, so it is still bad. \(\square\)

---

## 4. Exposure-cover lower bound

For an undefined cell

\[
e=(x,y)\notin D
\]

let

\[
H(e)=\{g\in B(D,c):\{x,y\}\cap X(g)\ne\varnothing\}.
\]

Define the **exposure-cover number**

\[
\boxed{
\tau_{\rm exp}(D,c)
=
\min\{|E|:\bigcup_{e\in E}H(e)=B(D,c)\}.
}
\]

Only undefined non-loop cells are allowed in this cover.

### Theorem — Exposure lower bound

\[
\boxed{
\alpha(D,c)\ge\tau_{\rm exp}(D,c).
}
\]

Indeed, if an extension fails to hit the exposure set of some old bad automorphism, the Exposure Persistence Lemma says that this automorphism survives.

---

## 5. Old-obstruction cell cost beta

Define

\[
\boxed{
\beta(D,c)
}

as the minimum number of real new operation cells required to destroy **all old bad automorphisms** in `B(D,c)`, without requiring the enlarged reduct to be globally exact with respect to newly created automorphisms.

Thus beta deliberately ignores symmetry creation after extension.

### Theorem — Basic beta bounds

\[
\boxed{
\tau_{\rm exp}(D,c)\le\beta(D,c)\le\alpha(D,c).
}
\]

The left inequality is the exposure theorem. The right inequality holds because an exact extension cannot leave any old bad automorphism alive: its restriction to the old colored layer would remain non-global.

### Theorem — beta is bounded by lambda

\[
\boxed{
\beta(D,c)\le\lambda(D,c).
}
\]

### Proof

Take an optimal system of `lambda` abstract phase links. Realize each by one bridge cell as in the No-old-obstruction construction of Article B. That theorem proves that every automorphism of the enlarged reduct which preserves the old domain has diagonal old phase. Hence no old bad automorphism survives. New bad automorphisms may appear, but beta ignores them. Therefore at most `lambda` real cells are needed to kill every old obstruction. \(\square\)

---

## 6. Refined universal cost hierarchy

Combining the published and new bounds gives

\[
\boxed{
\tau_{\rm exp}\le\beta\le\alpha\le\mu\le r-1,
}
\]

and independently

\[
\boxed{
\beta\le\lambda\le r-1.
}
\]

There is still no proved universal ordering between `alpha` and `lambda`.

The key point is now sharper:

- `beta` measures the cost of removing the **old** obstruction;
- `alpha-beta` measures only the extra price forced by **new symmetry creation under extension**.

Define the **symmetry-creation surcharge**

\[
\boxed{
\sigma(D,c)=\alpha(D,c)-\beta(D,c)\ge0.
}
\]

Then Conjecture 14 of Article B is equivalent to

\[
\boxed{
\sigma(D,c)\le\lambda(D,c)-\beta(D,c).
}
\]

A counterexample must therefore have a symmetry-creation surcharge larger than all slack between the abstract phase-link cost and the old-obstruction real-cell cost.

---

## 7. Two infinite cost phases

### Hub family from Article B

For the `r`-component hub construction,

\[
\boxed{
\tau_{\rm exp}=\beta=\alpha=\mu=1,
\qquad
\lambda=r-1.
}
\]

Each local bad flip has an exposure set containing the common fixed hub `h`, because its phase-1 cells terminate at `h`. One cell `(h,t)` therefore hits every exposure set and connects the whole incidence geometry.

### Disjoint bidirected-pair family

For `r` disjoint oppositely colored bidirected pairs,

\[
\boxed{
\tau_{\rm exp}=\beta=\alpha=\left\lceil\frac r2\right\rceil,
}
\]

while

\[
\boxed{
\mu=\lambda=r-1.
}
\]

Explanation:

- each local flip has exposure set exactly the two carrier vertices of its own pair;
- one new cell can hit at most two such exposure sets, so `tau_exp>=ceil(r/2)`;
- the exact-cost construction from `DISJOINT_PAIR_EXACT_COST.md` attains this bound;
- connecting all `r` old incidence components requires at least `r-1` bridges because every candidate cell touches at most two old components.

Thus the two families exhibit genuinely different resource geometries:

\[
\text{hub concentration}
\quad\text{versus}\quad
\text{distributed endpoint exposure}.
\]

---

## 8. Stronger conjecture suggested by all current data

No audited example presently has a positive symmetry-creation surcharge.

In all complete audits through five carrier points, every nonexact state has `alpha=1`; hence necessarily `beta=alpha=1`.

For six carrier points with `|D|<=7`, the only states with `alpha=2` are the 60 normalized three-disjoint-bidirected-pair states:

- 15 perfect matchings on six carrier vertices;
- 4 opposite-color orientations modulo global complement for each matching;
- total `15*4=60`.

For these states the exact disjoint-pair theorem gives `beta=alpha=2`.

Hence every state in the currently exhaustive frontier satisfies

\[
\boxed{\alpha(D,c)=\beta(D,c).}
\]

This motivates the stronger conjecture:

### Strong Safe-Extension Conjecture

\[
\boxed{
\alpha(D,c)=\beta(D,c)
\quad\text{for every finite sparse binary anonymous layer.}
}
\]

If true, Article B Conjecture 14 follows immediately from `beta<=lambda`:

\[
\alpha=\beta\le\lambda.
\]

The strong conjecture states that although individual cell additions can create new symmetries, **there is always an old-obstruction-optimal extension that incurs no net symmetry-creation surcharge**.

This is now the preferred theoretical target.

---

## 9. Why the exposure theorem cannot by itself prove Conjecture 14

The exposure number sees only survival of old bad automorphisms. Since

\[
\tau_{\rm exp}\le\beta\le\lambda,
\]

no exposure-cover lower bound can by itself force

\[
\alpha>\lambda.
\]

Any counterexample to Article B Conjecture 14 must therefore exploit the part invisible to exposure geometry:

\[
\boxed{
\text{new bad automorphisms created by the extension.}
}
\]

This precisely confirms the deletion-symmetry localization obtained in Article B, now expressed as a cost decomposition.

---

## 10. Next theorem target

The next problem is the **Safe Minimum Extension Theorem**:

> Given an extension of size `beta` that kills all old bad automorphisms, can one choose an extension of the same size whose newly created automorphisms are all globally color-admissible?

A proof gives `alpha=beta` and settles Article B Conjecture 14.

A counterexample must have

\[
\sigma=\alpha-\beta>0
\]

and would constitute the first genuine example where symmetry creation has an unavoidable positive operation-cell cost.

---

## Claim firewall

1. `tau_exp` is a lower bound, not a general formula for `alpha` or `beta`.
2. `beta<=lambda` is theorem-level and uses the published No-old-obstruction bridge construction.
3. `alpha=beta` is a new conjecture, not a theorem.
4. The statement about the exhaustive frontier uses the previously recorded complete audits: all `|G|<=5` and `|G|=6, |D|<=7`.
5. Articles A and B remain frozen publications.
