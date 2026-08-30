# FCOA Hybrid Memory — Existential Pebble-Width Separation

**Status:** positive theorem in a standard finite-variable query model  
**Model:** static relational preprocessing + existential-positive finite-variable FO / conjunctive-query decoder  
**Significance:** first standard-model space separation between AL0 and AL1/AL2 in this branch

## 1. Why move from full FO^k to CQ^k

Full finite-variable FO permits negation, alternation and variable reuse. Establishing sharp storage lower bounds there immediately enters the hard general theory of finite-variable equivalence.

The existential-positive `k`-variable fragment is a standard and substantially cleaner intermediate model. It is equivalent, at query level, to conjunctive queries using at most `k` distinct variables, and its expressive comparison is characterized by existential `k`-pebble games / `k`-consistency methods.

This gives a genuine standard finite-model-theoretic width parameter rather than an FCOA-specific factorization convention.

---

## 2. Preprocessing/query model

For every `N`, let `X_N` be an `N`-element target sector of a finite relational structure `A_N` over one fixed finite relational signature of bounded arity.

Storage is

\[
S(A_N)=|A_N|+\sum_R |R^{A_N}|.
\]

A relation on `X_N` is decoded by one fixed conjunctive query (`CQ`) whose total number of distinct variables, free and existential together, is at most `k`.

Define the storage exponent

\[
\sigma_j^{CQ}(k)
=
\inf\limsup_{N\to\infty}
\frac{\log S(A_N)}{\log N},
\]

for the canonical AL benchmark of phase `j`.

Because `|X_N|=N`, every realizable phase has

\[
\sigma_j^{CQ}(k)\ge1.
\]

---

## 3. A three-variable linear-space order representation

### Construction HM-CQ-ORD

Let

\[
X_N=\{0,1,\ldots,N-1\}
\]

externally for construction purposes.

Build a balanced binary decomposition tree whose leaves, from left to right, are the target elements. For every internal tree node `w`, let `L_w` and `R_w` be the sets of leaves in its left and right subtrees.

Store two binary relations

\[
L(x,w)\iff x\in L_w,
\]

\[
R(y,w)\iff y\in R_w.
\]

Every leaf occurs in `O(log N)` left/right ancestor sets, so the total number of stored tuples is

\[
O(N\log N)=N^{1+o(1)}.
\]

Now define

\[
\boxed{
x<y\iff\exists w\,(L(x,w)\land R(y,w)).
}
\]

For distinct leaves `x,y`, their least common ancestor witnesses the formula exactly when `x` lies in the left subtree and `y` in the right subtree, i.e. exactly when `x<y` in the leaf order.

The query uses only three variables `x,y,w` and is conjunctive.

Hence

\[
\sigma_0^{CQ}(3)\le1.
\]

Together with the target-size lower bound,

\[
\boxed{
\sigma_0^{CQ}(3)=1.
}
\tag{1}
\]

---

## 4. Two variables are insufficient for compressed CQ order

A binary CQ using at most two variables `x,y` has no distinct existential helper variable once both free variables are present.

To define strict order, a conjunction containing only unary atoms cannot distinguish the orientation of a pair. Therefore at least one atom must involve both `x` and `y`.

That primitive relation must contain every ordered pair `(x,y)` with `x<y`, of which there are

\[
\frac{N(N-1)}2=Theta(N^2).
\]

Thus

\[
\sigma_0^{CQ}(2)\ge2.
\]

Storing `<` directly gives the matching upper bound:

\[
\boxed{
\sigma_0^{CQ}(2)=2.
}
\tag{2}
\]

So adding the third variable changes the optimal order-storage exponent from `2` to `1`.

---

## 5. Three-variable addition lower bound

Let

\[
Add_N(x,y,z)\iff x+y=z<N.
\]

Its number of true triples is

\[
|Add_N|
=\sum_{z=0}^{N-1}(z+1)
=\frac{N(N+1)}2
=Theta(N^2).
\tag{3}
\]

Consider any conjunctive query

\[
q(x,y,z)
\]

using at most three distinct variables total.

Since all three variable names are already free, `q` has no additional distinct existential helper variable. It is therefore a conjunction of atomic constraints whose variable support is contained in `{x,y,z}`.

### Lemma HM-CQ-ADD-SCOPE

If `q` defines `Add_N`, at least one atom of `q` must involve all three free variables.

### Proof

Assume every atom depends on at most two of the free variables.

Because every valid addition triple must satisfy every atom, the interpretation of each unary/binary atom must contain the corresponding projection of `Add_N` (with the appropriate variable permutation/repetition).

The principal pair projections are

\[
\pi_{xy}(Add_N)=\{(x,y):x+y<N\},
\]

\[
\pi_{xz}(Add_N)=\{(x,z):x\le z\},
\]

\[
\pi_{yz}(Add_N)=\{(y,z):y\le z\}.
\]

For every `N>=4`, the spurious triple

\[
(1,1,3)
\]

lies in all three pair projections and all unary projections, but

\[
1+1\ne3.
\]

Hence every atom with support of size at most two that is true on all valid addition triples is also true on `(1,1,3)`. Their conjunction therefore accepts this spurious triple, contradiction. `square`

### Theorem HM-CQ-ADD3

Any three-variable CQ preprocessing representation of exact truncated addition has

\[
S(A_N)=Omega(N^2).
\]

### Proof

By the scope lemma, some atom uses all three free variables. Since the conjunction is true on every addition triple, the primitive relation used by that atom must contain, up to a fixed permutation/repetition convention, all `Theta(N^2)` triples in (3). Therefore the preprocessed structure stores `Omega(N^2)` tuples. `square`

Direct materialization of `Add_N` gives the matching upper bound, so

\[
\boxed{
\sigma_1^{CQ}(3)=2.
}
\tag{4}
\]

---

## 6. AL2 inherits the same lower bound

The canonical AL2 benchmark contains the AL1 benchmark, in particular exact truncated addition.

Therefore every three-variable CQ realization of AL2 must also pay the addition lower bound:

\[
\boxed{
\sigma_2^{CQ}(3)=2.
}
\tag{5}
\]

The upper bound `2` follows by direct materialization of the canonical order/addition/multiplication relations; multiplication itself has only `N^{1+o(1)}` true triples, while addition and order dominate at quadratic storage under a three-variable direct representation.

---

## 7. Three-variable pebble-width phase separation

Combining (1), (4), and (5):

### Theorem HM-CQ3-SEPARATION

In static relational preprocessing with a three-variable conjunctive-query decoder,

\[
\boxed{
\sigma_0^{CQ}(3)=1,
\qquad
\sigma_1^{CQ}(3)=\sigma_2^{CQ}(3)=2.
}
\]

Thus at **exactly the same standard finite-variable width**, order admits near-linear preprocessing while additive and full arithmetic require quadratic preprocessing.

This is the first persistent asymptotic AL0-vs-AL1/AL2 resource separation obtained in the branch within a recognized finite-model-theory query fragment.

---

## 8. Width transition table

The currently proved endpoint values are

\[
\boxed{
\begin{array}{c|ccc}
\text{CQ variable width} & AL0 & AL1 & AL2\\
\hline
2 & 2 & \text{arity-impossible} & \text{arity-impossible}\\
3 & 1 & 2 & 2
\end{array}
}
\]

Here an exponent `a` means storage `N^{a+o(1)}`. “Arity-impossible” means a ternary benchmark relation cannot even have three distinct free variables in a two-variable formula.

The nontrivial row is `k=3`: all benchmark queries are syntactically admissible, but order compresses and arithmetic does not.

---

## 9. Why this is genuinely a pebble-width result

Existential-positive `k`-variable logic is characterized by the existential `k`-pebble game. The same game underlies strong `k`-consistency in CSP.

Therefore the parameter `k` is a standard semantic width parameter with an established game characterization, unlike the earlier FCOA-specific channel/depth measures.

The theorem should not be advertised as a lower bound for full `FO^3`; negation and general quantifier reuse may allow additional compression strategies not covered by the conjunctive-query argument.

---

## 10. Eventual linear upper bounds at larger fixed width

The previous digit constructions can be expressed by existential-positive formulas once enough variables are available simultaneously for:

- the three target arguments;
- their constant number of digit coordinates;
- the constant number of carry/product witnesses.

Thus there exists some absolute constant `K` such that

\[
\sigma_0^{CQ}(K)
=
\sigma_1^{CQ}(K)
=
\sigma_2^{CQ}(K)
=1.
\]

No claim of optimal `K` is made here.

Hence the CQ frontier has exactly the qualitative shape sought by the programme:

\[
\boxed{
\text{small width: arithmetic costs more space;}
\qquad
\text{sufficient width: all phases collapse to linear space.}
}
\]

The next sharp problem is to determine the minimum width at which AL1 and AL2 drop from exponent `2` to exponent `1`, and whether those two thresholds differ.

---

## 11. Relation to prior no-go results

This theorem explains why previous unrestricted models collapsed:

- unrestricted FO had enough logical coordination to exploit digit decompositions;
- increasing factorization depth supplied arbitrarily many effective helper coordinates;
- definitional expansion materialized difficult relations.

CQ^3 forbids exactly that escape route: the three free arithmetic arguments consume the entire variable budget, leaving no helper pebble for compressed joins.

Order uses only two free arguments, so its third pebble remains available as a shared witness and enables the dyadic biclique decomposition.

This is the conceptual source of the exponent gap.

---

## 12. Next target

Define

\[
k_+(N)
\]

and

\[
k_\times(N)
\]

as the minimum fixed CQ width allowing `N^{1+o(1)}` preprocessing for exact canonical addition and AL2 respectively.

The immediate finite question is whether the linear-space thresholds are

\[
4,5,6,\ldots
\]

and whether

\[
\boxed{k_+<k_\times}
\]

can be proved.

That would yield a genuine standard pebble-width hierarchy **inside arithmetic transport itself**, rather than only order versus arithmetic.

## 13. Literature calibration

The existential `k`-pebble game characterizes the existential-positive `k`-variable fragment and is equivalent to strong `k`-consistency phenomena in CSP. See, for example, Christoph Berkholz, *Lower Bounds for Existential Pebble Games and k-Consistency Tests*, Logical Methods in Computer Science 9(4), 2013, DOI 10.2168/LMCS-9(4:2)2013.

For the broader finite-variable setting and pebble-game methodology, see Martin Grohe, *Finite Variable Logics in Descriptive Complexity Theory*, Bulletin of Symbolic Logic 4(4), 1998, DOI 10.2307/420954.
