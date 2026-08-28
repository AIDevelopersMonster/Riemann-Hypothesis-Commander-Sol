# FCOA Hybrid Memory — Cost of Emerging Uniform Order

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** theorem candidate + constructive upper bound; hostile audit required  
**External calibration:** standard Gaifman locality is used as a classical ingredient.

## 1. Question

The Rigidity-without-Order theorem gives growing fixed-signature families with enormous joint value-memory and no uniform FO total order. The next question is the converse boundary:

> What structural resource must first become unbounded before a uniform FO order can appear, and how expensive can an explicit AL0 construction be?

Two answers emerge.

1. Any uniformly bounded-Gaifman-degree family is trapped below AL0.
2. Quadratic pairwise orientation is not necessary: with auxiliary coordinate nodes, AL0 can already be reached with linear total incidence size.

Thus the first cost is not density but **loss of locality**.

## 2. Bounded-degree Order Wall

### Theorem HM-BD0

Let `(A_n)` be an unbounded family of finite structures in a fixed finite relational signature of bounded arity. Suppose the Gaifman degree is bounded by a constant `Delta` independent of `n`.

Let `X_n` be a uniformly FO-definable subset with `|X_n|->infinity`.

Then no single parameter-free FO formula `phi(x,y)` can define a strict total order on every `X_n`.

### Proof

Fix `phi`. By Gaifman locality there is a finite radius `r` depending only on `phi`.

In a fixed finite signature and degree bound `Delta`, only finitely many rooted radius-`r` neighborhood types exist. Also every radius-`2r` ball has size bounded by a constant depending only on `Delta,r`.

For sufficiently large `X_n`, pigeonhole gives many points of one rooted `r`-type. Choose two such points `x,y` farther than `2r` apart. Their radius-`r` neighborhoods are disjoint and rooted-isomorphic. Hence the local neighborhood of `(x,y)` is isomorphic to that of `(y,x)` by exchanging the two components.

Gaifman normal form then gives

`phi(x,y) <=> phi(y,x)`.

A strict total order on distinct points requires exactly one orientation, contradiction. `square`

Therefore

\[
\boxed{\text{uniformly bounded Gaifman degree }\Longrightarrow\text{ below AL0}.}
\]

This strictly generalizes the homogeneous-corridor obstruction: the corridor was only an easy way to witness repeated local types.

## 3. Necessary structural transition

Any fixed-signature family that uniformly FO-defines a total order on an unbounded definable sector must violate the bounded-degree hypothesis.

Hence

\[
\boxed{\max\deg_G(A_n)\to\infty}
\]

is a necessary condition for crossing the order wall in this setting.

This does **not** mean dense `Theta(N^2)` operation tables are necessary. It means some elements must acquire increasingly nonlocal incidence reach.

Thus the first exact boundary is:

\[
\boxed{\text{AL0 requires unbounded Gaifman degree, not necessarily quadratic density}.}
\]

## 4. Why fixed local decorations cannot help

Any augmentation that adds only `O(1)` new local incidences per old element preserves bounded Gaifman degree. So none of the following can create uniform order on an unbounded family by themselves:

- finitely many periodic unary colors;
- a bounded number of short-range successor-like edges per point;
- fixed-radius marker gadgets repeated along a corridor;
- any constant-degree local orientation pattern.

They may destroy automorphisms globally, but HM-BD0 still blocks a uniform FO order.

This is the rigorous form of the statement that local symmetry-breaking is weaker than global coordinate recovery.

## 5. A linear-size AL0 construction with auxiliary coordinates

The quadratic G4-style tournament coloring is therefore an upper bound, not a lower bound.

We now give a sparse construction with only `Theta(N)` incidences.

For simplicity first take

\[
N=b^2.
\]

Let the data sector be

\[
X=\{x_{i,j}:0\le i,j<b\}.
\]

Introduce two coordinate sectors

\[
B=\{B_0,\ldots,B_{b-1}\},
\qquad
P=\{P_0,\ldots,P_{b-1}\}.
\]

Every data point has exactly one block coordinate and one position coordinate:

\[
\operatorname{Block}(x_{i,j},B_i),
\qquad
\operatorname{Pos}(x_{i,j},P_j).
\]

This costs exactly `2N` incidence pairs.

It remains only to make `B` and `P` uniformly ordered.

## 6. Threshold coding of the coordinate orders

Introduce marker sectors

\[
M_B=\{M^B_0,\ldots,M^B_{b-1}\},
\qquad
M_P=\{M^P_0,\ldots,M^P_{b-1}\}.
\]

Define threshold incidence

\[
R_B(B_i,M^B_k)\iff k\le i,
\]

and similarly

\[
R_P(P_j,M^P_k)\iff k\le j.
\]

Then coordinate order is first-order definable by strict neighborhood inclusion:

\[
B_i<B_{i'}
\iff
\forall m\,(R_B(B_i,m)\to R_B(B_{i'},m))
\land
\exists m\,(R_B(B_{i'},m)\land\neg R_B(B_i,m)).
\]

The same formula defines the order on `P`.

Each threshold relation uses

\[
1+2+\cdots+b=\frac{b(b+1)}2
\]

incidences. Both together cost

\[
b(b+1)=N+\sqrt N.
\]

Hence total incidence cost is

\[
2N+N+O(\sqrt N)=3N+O(\sqrt N).
\]

Fixed finite role gadgets can distinguish the four auxiliary sectors in a one-sorted presentation at only constant/additive-linear overhead, so the asymptotic remains `Theta(N)`.

## 7. Uniform recovery of the data order

Define lexicographic order on the data sector:

\[
x<y
\]

iff either

1. `Block(x)<Block(y)`, or
2. the block coordinates are equal and `Pos(x)<Pos(y)`.

Because each data point has unique block and position coordinates, this is uniformly FO definable from the fixed incidence signature.

Therefore the family reaches AL0:

\[
\boxed{\text{uniform total order on }N\text{ data points with }Theta(N)\text{ incidence size}.}
\]

For arbitrary `N`, take

\[
b=\lceil\sqrt N\rceil,
\qquad
p=\lceil N/b\rceil,
\]

use a `b x p` rectangle and omit unused final cells. The same asymptotic bound holds.

## 8. Compilation into fixed partial operations

The coordinate scaffold can be passed through the fixed-two-operation incidence compiler by representing each required incidence as an edge-element and using

\[
e\oplus e=\ell(e),
\qquad
e\otimes e=r(e).
\]

Finite role-separating marker gadgets distinguish the kinds of coordinate and threshold vertices.

Thus the AL0 upper bound is realizable in a fixed two-operation one-sorted FCOA signature with

\[
\boxed{Theta(N)\text{ defined cells per compiled incidence scale}.}
\]

The exact constant depends on the chosen role-gadget implementation and is not claimed optimal.

## 9. A linear lower bound under bounded arity

There is also a basic resource lower bound.

Suppose a one-sorted structure on an `N`-element target sector is built from a fixed finite collection of partial operation/relation cells of bounded arity, and assume target points not appearing in any nontrivial atomic tuple are structurally indistinguishable.

Each defined binary-operation cell

\[
f(a,b)=c
\]

mentions at most three carrier elements. If the total number of nontrivial cells is `M`, at most `3M` target elements can be directly incident to those cells.

If

\[
3M\le N-2,
\]

then at least two target elements remain completely untouched and can be transposed, preventing rigidity and therefore preventing a definable strict total order.

Hence in this basic cell model

\[
\boxed{M=\Omega(N).}
\]

is necessary.

Combined with the coordinate construction, this gives the asymptotic cell-cost window

\[
\boxed{\Theta(N)}
\]

for AL0 **when auxiliary carrier elements and fixed bounded-arity signatures are allowed**.

The lower bound is a coarse incidence-count bound; sharper constants and more permissive models may require separate analysis.

## 10. What actually crosses the wall

The transition below AL0 -> AL0 is therefore not best measured by automorphism collapse or by table density.

The decisive structural event is:

\[
\boxed{\text{bounded local reach }\longrightarrow\text{unbounded incidence degree / nonlocal coordinate access}.}
\]

The coordinate scaffold realizes this efficiently: only `O(sqrt N)` coordinate/marker nodes acquire degree `Theta(sqrt N)`, while total incidence remains linear.

Thus order can emerge from a sparse but nonlocal skeleton.

## 11. Leakage beyond AL0

The construction above proves uniform order but does **not** yet establish that it stops exactly at AL0.

The two-coordinate scaffold is richer than a bare linear order. In particular, its product/threshold representation may make additional relations uniformly definable.

Therefore its current classification is

\[
\boxed{\text{at least AL0; AL1/AL2 status requires hostile audit}.}
\]

It must not be advertised as a safe order-only construction until EqGap/addition and multiplication leakage are separately tested.

## 12. Exact contrast with Rigidity-without-Order

We now have two scalable fixed-signature regimes.

### Local rigid regime

- bounded Gaifman degree;
- finite members may be fully rigid;
- factorial value-memory amplification possible;
- uniform order impossible.

### Sparse nonlocal coordinate regime

- total incidence still linear;
- maximum Gaifman degree grows;
- a uniform coordinate comparison is available;
- total order becomes FO definable.

Hence

\[
\boxed{\text{rigidity is not the transition; nonlocality is}.}
\]

## 13. Current theorem package

The SOL-HYBRID order boundary now contains:

### HM-BD0

\[
\boxed{\text{bounded Gaifman degree }\Rightarrow\text{ no uniform FO total order}.}
\]

### Necessary AL0 condition

\[
\boxed{AL0\Rightarrow\max\deg_G\to\infty.}
\]

### Sparse upper bound

\[
\boxed{AL0\text{ is achievable with }Theta(N)\text{ total incidence/cell resources}.}
\]

Thus quadratic orientation tables are unnecessary once auxiliary coordinate carriers are allowed.

## 14. Next question

The remaining sharp question is no longer the asymptotic cost of obtaining order. It is:

> Can one achieve the `Theta(N)` AL0 bound while proving a genuine arithmetic firewall — no uniform EqGap/addition — or does every such compressed coordinate scheme inevitably leak at least AL1?

That is the next natural boundary between sparse order memory and additive leakage.
