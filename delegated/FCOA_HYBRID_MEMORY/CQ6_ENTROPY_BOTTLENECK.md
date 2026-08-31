# FCOA Hybrid Memory — CQ6 Entropy Bottleneck

**Status:** rigorous upper-bound improvement + exact reduction of the first unresolved lower-bound case  
**Scope:** standard static relational preprocessing with conjunctive-query decoders

## 1. Current threshold window

Let `k_+` be the minimum conjunctive-query variable width for which exact truncated addition on an `N`-point target sector admits preprocessing size `N^{1+o(1)}`.

The previous lower bounds give

\[
\sigma_1^{CQ}(3)=\sigma_1^{CQ}(4)=\sigma_1^{CQ}(5)=2,
\]

hence

\[
\boxed{k_+\ge 6.}
\]

The earlier digit construction gave `k_+<=10`. This note improves the upper bound to

\[
\boxed{k_+\le 9}
\]

using two residue channels.

Therefore

\[
\boxed{6\le k_+\le 9.}
\]

As proved in `CQ_WIDTH_THRESHOLD_REDUCTION.md`, the near-linear thresholds for AL1 and AL2 coincide because truncated multiplication itself has only `Theta(N log N)` true triples and may be materialized directly.

---

## 2. CQ9 linear-space addition via two CRT channels

Choose two coprime moduli

\[
p,q=\Theta(\sqrt N)
\]

with

\[
pq>2N.
\]

Introduce residue sorts `R_p,R_q`. Store four target-to-residue relations

\[
P(x,x_p),\quad P(y,y_p),\quad P(z,z_p),
\]

through one common relation symbol `P`, and analogously

\[
Q(x,x_q),\quad Q(y,y_q),\quad Q(z,z_q).
\]

Store complete modular addition tables

\[
A_p(a,b,c)\iff a+b\equiv c\pmod p,
\]

\[
A_q(a,b,c)\iff a+b\equiv c\pmod q.
\]

The preprocessing size is

\[
3N+3N+p^2+q^2=\Theta(N)
\]

up to harmless constant sharing of the residue-map relations.

Addition is decoded by

\[
\begin{aligned}
Add(x,y,z)\iff\exists x_p,y_p,z_p,x_q,y_q,z_q\;(&P(x,x_p)\land P(y,y_p)\land P(z,z_p)\\
&\land Q(x,x_q)\land Q(y,y_q)\land Q(z,z_q)\\
&\land A_p(x_p,y_p,z_p)\\
&\land A_q(x_q,y_q,z_q)).
\end{aligned}
\]

This formula uses exactly nine distinct variables:

\[
x,y,z,x_p,y_p,z_p,x_q,y_q,z_q.
\]

If it holds, then

\[
x+y-z\equiv0\pmod p,
\qquad
x+y-z\equiv0\pmod q,
\]

so `pq` divides `x+y-z`. Since

\[
|x+y-z|<2N<pq,
\]

we get

\[
\boxed{x+y=z.}
\]

Conversely ordinary equality implies both congruences.

Hence

\[
\boxed{\sigma_1^{CQ}(9)=1.}
\]

and therefore

\[
\boxed{k_+\le9.}
\]

---

## 3. Why CQ6 is the first genuinely new case

A `CQ^6` addition formula has free variables

\[
x,y,z
\]

and at most three helper variables

\[
u,v,w.
\]

The previous free-pair lemma remains valid:

> if any primitive atom contains two distinct variables among `x,y,z`, that primitive relation must contain `Omega(N^2)` tuples.

Thus every hypothetical near-linear `CQ^6` representation must satisfy:

\[
\boxed{\text{each primitive atom contains at most one free arithmetic variable}.}
\tag{C6.1}
\]

For every fixed helper assignment `(u,v,w)`, the conjunction of all `x`-branch atoms defines a set `X_{uvw}` of allowed `x` values; similarly `Y_{uvw}` and `Z_{uvw}`.

Because no atom contains two free variables, the free tuples accepted by one fixed helper assignment form the Cartesian box

\[
X_{uvw}\times Y_{uvw}\times Z_{uvw}.
\]

Exactness of addition and the Latin-box lemma imply every productive helper assignment has

\[
|X_{uvw}|=|Y_{uvw}|=|Z_{uvw}|=1.
\]

Therefore each productive helper assignment certifies exactly one addition triple.

Since `Add_N` contains `Theta(N^2)` triples, any exact `CQ^6` representation must have

\[
\boxed{Theta(N^2)\text{ productive helper assignments}.}
\tag{C6.2}
\]

This is the core reduction.

---

## 4. Why the CQ4/CQ5 rectangle argument stops here

With one helper, productive witnesses form a one-dimensional set; with two helpers, each free branch is rectangle-like in the hidden grid, and Latin fibers are matchings. This yields the previous quadratic lower bounds.

With three helpers, a branch may depend on all three helper variables through atoms such as

\[
R(x,u,v,w),
\]

or may use several pairwise helper scopes. The productive helper set can therefore have genuine three-way join structure.

The correct remaining problem is not a simple rectangle-cover problem. It is a **three-hidden-variable join/entropy problem**:

> Can a fixed join of total input size `N^{1+o(1)}` contain `Theta(N^2)` productive helper triples while three branch decoders map those triples bijectively onto the Latin relation `x+y=z`?

This is precisely where AGM/fractional-cover bounds alone are insufficient: sparse three-variable joins can have superlinear output, and the Latin functional dependencies must be used.

---

## 5. Entropy formulation of CQ6

Choose one productive helper triple for every valid addition triple and sample uniformly from a large regular subtriangle of `Add_N` so that

\[
H(X,Y,Z)=2\log N-O(1)
\]

and any two of `X,Y,Z` determine the third.

Let `(U,V,W)` be the selected helper tuple. Since one productive helper tuple cannot certify two distinct valid addition triples,

\[
H(X,Y,Z\mid U,V,W)=0.
\]

Choosing one helper tuple deterministically per addition triple also gives

\[
H(U,V,W\mid X,Y,Z)=0.
\]

Hence, up to lower-order boundary effects,

\[
\boxed{H(U,V,W)=2\log N.}
\tag{E1}
\]

If total preprocessing is `N^{1+o(1)}`, then for every primitive relation atom `R(S)` used by the CQ,

\[
H(S)\le (1+o(1))\log N,
\tag{E2}
\]

under the induced witness distribution, because the support of that atom is contained in a relation of near-linear cardinality.

The CQ6 lower-bound problem therefore reduces to the following entropy feasibility question:

> Is there an entropy vector on
> \[
> X,Y,Z,U,V,W
> \]
> satisfying the addition functional dependencies
> \[
> H(Z\mid X,Y)=H(Y\mid X,Z)=H(X\mid Y,Z)=0,
> \]
> the helper equivalence (E1), the branch-singleton condition, and the near-linear atom constraints (E2) for some fixed CQ hypergraph obeying (C6.1)?

If no such entropy vector exists for every six-variable CQ hypergraph, then

\[
\boxed{\sigma_1^{CQ}(6)=2}
\]

and the threshold rises to `k_+>=7`.

---

## 6. Structural cases already eliminated

Several CQ6 hypergraph forms are immediately impossible at near-linear size.

### 6.1 A ternary helper atom carrying all productive triples

If the helper core contains an atom `H(u,v,w)` through which every productive assignment must pass, then `H` itself must contain all `Theta(N^2)` productive helper tuples by (C6.2). Hence storage is quadratic.

### 6.2 A free branch with one atom carrying all three helpers

If, for example, an atom `R(x,u,v,w)` must distinguish all productive helper assignments associated with the `x` branch and these assignments have `Theta(N^2)` distinct `(u,v,w)` projections, then `R` is quadratic. Therefore any near-linear candidate must reuse helper tuples heavily within each fixed free value and factor the branch into smaller scopes.

### 6.3 Pure triangle helper core

If all productive helper triples are constrained by three binary helper relations

\[
R_{UV}(u,v),\qquad R_{VW}(v,w),\qquad R_{WU}(w,u)
\]

whose total size is `M=N^{1+o(1)}`, the AGM bound gives at most

\[
O(M^{3/2})=N^{3/2+o(1)}
\]

helper triangles.

This is smaller than the required `Theta(N^2)`. Therefore a near-linear CQ6 candidate cannot obtain all productive witnesses from a triangle core alone.

These reductions leave only mixed hypergraphs in which at least one helper coordinate has substantial Cartesian freedom and the free branches jointly cut that freedom down to singleton Latin triples.

---

## 7. Literature calibration

The remaining CQ6 problem sits naturally at the intersection of:

- factorised representations of conjunctive-query answers;
- AGM/fractional-hypertree-width join bounds;
- entropy bounds for conjunctive queries under functional dependencies;
- rectangle/communication-complexity lower bounds.

In particular, entropy techniques for CQ size bounds under functional dependencies are standard and provide a natural language for the pairwise functional dependencies of the addition relation.

Relevant references include:

1. G. Gottlob, S. T. Lee, G. Valiant, *Size and Treewidth Bounds for Conjunctive Queries*, JACM 59(3), 2012, DOI 10.1145/2220357.2220363.
2. T. Gogacz, S. Toruńczyk, *Entropy Bounds for Conjunctive Queries with Functional Dependencies*, ICDT 2017, DOI 10.4230/LIPIcs.ICDT.2017.15.
3. D. Olteanu, J. Závodný, *Factorised Representations of Query Results: Size Bounds and Readability*, ICDT 2012, DOI 10.1145/2274576.2274607.
4. C. Berkholz, H. Vinall-Smeeth, *Factorised Representations of Join Queries: Tight Bounds and a New Dichotomy*, ICDT 2026, DOI 10.4230/LIPIcs.ICDT.2026.11.

---

## 8. Current exact status

The width frontier is now

\[
\boxed{
\begin{array}{c|ccc}
 k & AL0 & AL1 & AL2\\
\hline
3 & 1 & 2 & 2\\
4 & 1 & 2 & 2\\
5 & 1 & 2 & 2\\
6 & 1 & ? & ?\\
7 & 1 & ? & ?\\
8 & 1 & ? & ?\\
9 & 1 & 1 & 1
\end{array}
}
\]

and

\[
\boxed{6\le k_+=k_{AL1}=k_{AL2}\le9.}
\]

The next decisive strike is therefore the six-variable entropy/hypergraph classification. No stronger lower bound is claimed here until the mixed helper-core case is closed.
