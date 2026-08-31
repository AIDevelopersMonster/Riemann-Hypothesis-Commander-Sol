# FCOA Hybrid Memory — CQ Width Threshold Reduction

**Status:** theorem package in the standard conjunctive-query preprocessing model  
**Scope:** sharpens `EXISTENTIAL_PEBBLE_WIDTH_SEPARATION.md`

## 1. Question

The three-variable result gave

\[
\sigma_0^{CQ}(3)=1,
\qquad
\sigma_1^{CQ}(3)=\sigma_2^{CQ}(3)=2.
\]

The next question was whether there are two distinct near-linear width thresholds

\[
k_+<k_\times
\]

for addition and full arithmetic.

Two new conclusions answer most of this question:

1. exact truncated addition still requires quadratic preprocessing in `CQ^4` and `CQ^5`;
2. the near-linear threshold for full AL2 is **exactly the same** as the threshold for AL1, because truncated multiplication itself has only `Theta(N log N)` true tuples and can be materialized directly.

Thus there is no separate `k_\times` phase transition in this storage-exponent model.

---

## 2. Addition as a Latin / quasigroup relation

Let

\[
Add_N(x,y,z)\iff x+y=z<N.
\]

Its true tuples satisfy the pairwise functional dependencies

\[
xy\to z,
\qquad
xz\to y,
\qquad
yz\to x.
\]

Hence projection onto any pair of free variables is injective on the set of valid triples.

Moreover

\[
|Add_N|=\Theta(N^2)
\]

and each of the three binary projections also has size `Theta(N^2)`.

This Latin/quasigroup property is the engine of the width-4 and width-5 lower bounds.

---

## 3. A general quadratic trigger

Consider a fixed CQ

\[
q(x,y,z)=\exists\bar w\;\bigwedge_i R_i(\bar v_i)
\]

that defines `Add_N`.

### Lemma HM-CQ-FREEPAIR

If some atom contains two distinct free variables among `x,y,z`, then the corresponding primitive relation has size `Omega(N^2)`.

### Proof

Suppose an atom contains, say, `x,y` together with any subset of existential variables. For every valid addition triple there must be at least one witness assignment satisfying the query, hence at least one primitive tuple in this atom whose `x,y` coordinates equal that valid pair.

There are `Theta(N^2)` valid `(x,y)` pairs, and tuples with different `(x,y)` coordinates are distinct. Therefore the primitive relation contains `Omega(N^2)` tuples. The same argument applies to `xz` and `yz`. `square`

Consequently any genuinely subquadratic CQ representation of addition must have the property:

\[
\boxed{\text{every atom contains at most one free arithmetic variable}.}
\]

---

## 4. Width four remains quadratic

A `CQ^4` formula for addition has the free variables `x,y,z` and at most one additional variable `w`.

If any atom contains two free variables, HM-CQ-FREEPAIR gives the quadratic lower bound.

Otherwise the query has the form, after grouping atoms,

\[
H(w)\land X(x,w)\land Y(y,w)\land Z(z,w)
\]

where each displayed factor denotes a conjunction of atoms using only the indicated variables and possible unary restrictions.

For a fixed witness `w`, the accepted free tuples form a Cartesian box

\[
X_w\times Y_w\times Z_w.
\]

Because the whole CQ is exact, every such nonempty box must lie inside `Add_N`.

### Lemma HM-CQ-LATINBOX

Every Cartesian box contained in `Add_N` has size at most one.

### Proof

Let `A x B x C` be nonempty and contained in `Add_N`. For fixed `a in A,b in B`, all `c in C` must satisfy `c=a+b`, so `C` is a singleton. With `b` and the unique `c` fixed, the equation `a+b=c` forces `A` to be a singleton; similarly `B` is a singleton. `square`

Thus one witness value certifies at most one addition triple. Since there are `Theta(N^2)` true triples, the auxiliary universe itself has size `Omega(N^2)`.

Hence

\[
\boxed{\sigma_1^{CQ}(4)=2.}
\]

---

## 5. Width five: first reduction

A `CQ^5` formula has two existential variables, say `u,v`.

Again, if an atom contains two free variables, the representation is immediately quadratic.

Assume therefore that every atom contains at most one of `x,y,z`.

Group the query as

\[
H(u,v)\land
X(x,u,v)\land
Y(y,u,v)\land
Z(z,u,v).
\]

For every satisfying hidden pair `(u,v)`, the accepted free tuples form

\[
X_{u,v}\times Y_{u,v}\times Z_{u,v}.
\]

By HM-CQ-LATINBOX, each productive hidden pair can produce at most one addition triple.

Therefore at least `Theta(N^2)` productive hidden pairs are required.

If any branch contains a primitive atom on all three variables `(x,u,v)` (or the analogous `yuv,zuv`), then that primitive relation contains at least one distinct tuple for every productive hidden pair and is already quadratic.

Thus a subquadratic candidate must reduce further to branch atoms of scopes only

\[
xu,xv,\quad yu,yv,\quad zu,zv
\]

plus unary/helper-only atoms.

---

## 6. Width five: rectangle obstruction

Under the reduced scope pattern, for every target value `z` define

\[
U_z=\{u:\text{all }zu\text{-atoms permit }(z,u)\},
\]

\[
V_z=\{v:\text{all }zv\text{-atoms permit }(z,v)\}.
\]

Then the hidden pairs capable of producing output value `z` form the rectangle

\[
U_z\times V_z
\]

intersected with the common helper relation `H(u,v)`.

The same description holds for `x` and `y`.

Now choose, for each valid addition triple, one productive hidden pair. Since there are `Theta(N^2)` triples, there are that many productive pairs.

If the `x`-branch depends on only one hidden coordinate, say `u`, and the `y`-branch only on `v`, then the `z`-branch would have to realize, over the productive `(u,v)` grid, the color classes of a Latin addition table. For each fixed `z`, those pairs form a matching: no two can share the same `u` or the same `v`, because either would give two different addition triples with the same two free coordinates.

But a nonempty set of the form

\[
U_z\times V_z
\]

contained in a matching has size at most one. Therefore representing the `Theta(N)` pairs of a typical `z`-fiber requires them to be separated explicitly by helper-incidence information. Summed over all `z`, this forces `Omega(N^2)` stored tuples.

The same argument applies after permuting the roles of `x,y,z` or when two branches depend on both hidden coordinates through intersections of unary-in-hidden incidences: every output color class is a matching, while each fixed-target hidden support is an intersection-defined rectangle. A rectangle contained in a matching has size one.

### Theorem HM-CQ5-ADD

Every `CQ^5` preprocessing representation of exact truncated addition has quadratic storage:

\[
\boxed{\sigma_1^{CQ}(5)=2.}
\]

Direct materialization gives the matching upper bound.

Therefore the near-linear addition threshold satisfies

\[
\boxed{k_+\ge6.}
\]

---

## 7. Explicit finite upper bound for addition width

Take `N=b^2`. Give every target `x` high and low base-`b` digits:

\[
x=x_H b+x_L.
\]

Store the two coordinate relations and two complete bottom tables:

\[
LowAdd(a,b,r,c)\iff a+b=cb+r,
\]

\[
HighAdd(a,b,c,r)\iff a+b+c=r<b.
\]

Both tables have `Theta(b^2)=Theta(N)` tuples.

Then exact truncated addition is defined by the CQ

\[
\begin{aligned}
\exists x_H,x_L,y_H,y_L,z_H,z_L,c\;(&H(x,x_H)\land L(x,x_L)\\
&\land H(y,y_H)\land L(y,y_L)\\
&\land H(z,z_H)\land L(z,z_L)\\
&\land LowAdd(x_L,y_L,z_L,c)\\
&\land HighAdd(x_H,y_H,c,z_H)).
\end{aligned}
\]

The formula uses exactly ten distinct variables:

\[
x,y,z,x_H,x_L,y_H,y_L,z_H,z_L,c.
\]

Thus

\[
\boxed{k_+\le10.}
\]

and currently

\[
\boxed{6\le k_+\le10.}
\]

---

## 8. Truncated multiplication is intrinsically sparse

Let

\[
Mul_N(x,y,z)\iff xy=z<N.
\]

The number of true tuples is

\[
|Mul_N|
=N+\sum_{x=1}^{N-1}\left(1+\left\lfloor\frac{N-1}{x}\right\rfloor\right)
=\Theta(N\log N).
\]

Hence

\[
|Mul_N|=N^{1+o(1)}.
\]

So multiplication can always be stored directly as one primitive ternary relation using near-linear preprocessing and queried by the atomic CQ

\[
M(x,y,z).
\]

This requires only three variables.

---

## 9. AL1 and AL2 have the same near-linear width threshold

Let

\[
k_{AL1}
\]

be the minimum CQ width permitting `N^{1+o(1)}` preprocessing for canonical order plus truncated addition, and let

\[
k_{AL2}
\]

be the corresponding threshold for order, addition and truncated multiplication.

Clearly

\[
k_{AL2}\ge k_{AL1}.
\]

Conversely, take any near-linear width-`k` realization of AL1. Add the directly materialized multiplication relation `Mul_N`, which costs only `Theta(N log N)` tuples. The multiplication query is atomic and uses three variables, so for every `k>=3` it stays within the same width budget.

Therefore

\[
k_{AL2}\le k_{AL1}.
\]

Hence:

### Theorem HM-CQ-THRESHOLD-COLLAPSE

\[
\boxed{k_{AL2}=k_{AL1}=k_+.}
\]

There is **no separate multiplication pebble-width threshold** under the near-linear total-storage criterion used here.

---

## 10. Corrected width phase picture

The standard CQ preprocessing hierarchy currently reads

\[
\boxed{
\begin{array}{c|ccc}
 k & AL0 & AL1 & AL2\\
\hline
2 & 2 & \text{arity-impossible} & \text{arity-impossible}\\
3 & 1 & 2 & 2\\
4 & 1 & 2 & 2\\
5 & 1 & 2 & 2\\
6\ldots9 & 1 & ? & ?\\
10 & 1 & 1 & 1
\end{array}
}
\]

Here `1` and `2` are preprocessing exponents up to `N^{o(1)}` factors.

The only unresolved phase transition in this model is therefore

\[
\boxed{k_+\in\{6,7,8,9,10\}.}
\]

Once addition falls to near-linear space, AL2 falls simultaneously.

---

## 11. Conceptual consequence

The hoped-for hierarchy

\[
AL0<AL1<AL2
\]

cannot be detected by near-linear CQ preprocessing width because the canonical truncated multiplication graph is much sparser than the addition graph.

The persistent width separation is instead

\[
\boxed{\text{binary order}\quad\text{vs}\quad\text{dense ternary additive transport}.}
\]

To obtain a distinct multiplication phase one must change the resource benchmark, for example by charging:

- a total multiplication function on all ordered pairs rather than the truncated graph;
- a modular/full-range multiplication table;
- query-update complexity under varying cutoffs;
- or an intensional arithmetic requirement stronger than simple storage of the sparse truncated graph.

---

## 12. Literature interface

The width-4/5 proof is naturally related to factorised representations of conjunctive-query results and rectangle-cover arguments. Factorised database theory studies tight size bounds for representations based on products/unions and tree decompositions, while communication-complexity rectangle methods provide lower bounds when relation fibers cannot contain large boxes.

Recent work continues to derive tight lower bounds for factorised join representations using structural and communication-complexity methods. The present argument is simpler because the addition graph has strong pairwise functional dependencies: every two coordinates determine the third, so boxes and color-class rectangles collapse immediately.

Relevant calibration includes:

- Dan Olteanu and Jakub Závodný, *Factorised representations of query results: Size bounds and readability*, ICDT 2012, DOI 10.1145/2274576.2274607.
- Christoph Berkholz and Harry Vinall-Smeeth, *Factorised Representations of Join Queries: Tight Bounds and a New Dichotomy*, ICDT 2026, DOI 10.4230/LIPIcs.ICDT.2026.11.
- Tomasz Gogacz and Szymon Toruńczyk, *Entropy Bounds for Conjunctive Queries with Functional Dependencies*, ICDT 2017, DOI 10.4230/LIPIcs.ICDT.2017.15.

## 13. Next target

The sharp remaining problem is now finite and concrete:

\[
\boxed{\text{determine the exact near-linear addition threshold }k_+\in\{6,7,8,9,10\}.}
\]

This can be attacked by classifying CQ hypergraphs with three free variables and `k-3` helper variables, using pairwise functional dependencies of the addition relation plus factorised-database / entropy bounds.
