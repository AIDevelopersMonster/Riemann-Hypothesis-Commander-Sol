# FCOA Hybrid Memory — Sparse Order Wall

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** theorem candidate; proof complete modulo standard FO parity inexpressibility on finite linear orders; hostile audit required  
**Goal:** show that the linear-size coordinate construction reaches AL0 but does not leak to AL1.

## 1. Square-grid coordinate family

Fix `b>=2` and let

\[
N=b^2.
\]

Take two finite linearly ordered coordinate sets

\[
B_b=\{0_B<\cdots<(b-1)_B\},
\qquad
P_b=\{0_P<\cdots<(b-1)_P\}.
\]

Let the data sector be the Cartesian grid

\[
X_b=B_b\times P_b.
\]

Write its points as `x_{i,j}`.

The intended total order on `X_b` is lexicographic:

\[
x_{i,j}<_{lex}x_{k,l}
\iff
(i<k)\lor(i=k\land j<l).
\]

The sparse incidence realization from `ORDER_EMERGENCE_COST.md` adds block/position incidence and threshold-marker copies so that both coordinate orders and the lexicographic order are uniformly FO definable with `Theta(N)` incidences.

## 2. Logical upper bound: the scaffold is only two finite orders

Let

\[
\mathcal K_b=(B_b,<_{B};P_b,<_{P})
\]

be the two-sorted disjoint union of two `b`-element finite linear orders.

The entire coordinate scaffold is uniformly FO interpretable in `\mathcal K_b`:

- the data sort `X_b` is represented by ordered pairs `(i,j)\in B_b\times P_b`;
- block and position maps are coordinate projections;
- threshold-marker sorts are fixed tagged copies of `B_b` and `P_b`;
- threshold incidence is just the corresponding order relation.

Conversely the two coordinate orders are uniformly recoverable from the scaffold.

Therefore every relation uniformly FO definable on the sparse scaffold pulls back to a fixed FO relation over the pair of pure finite linear orders.

This is the key firewall.

## 3. Parity is not definable on equal pairs of finite orders

### Lemma HM-SOW-P

No FO sentence in the fixed two-sorted language

\[
\{<_{B},<_{P}\}
\]

defines the parity of `b` on the family `\mathcal K_b`.

### Proof

For every quantifier rank `q`, sufficiently long finite linear orders of adjacent lengths are `q`-equivalent; equivalently, Duplicator wins the `q`-round Ehrenfeucht-Fraisse game on two sufficiently long adjacent chains.

Choose an even `b` and odd `b+1` beyond that threshold. Duplicator plays the two-sorted game on

\[
\mathcal K_b
\quad\text{and}\quad
\mathcal K_{b+1}
\]

componentwise, using the winning strategy on the `B`-orders when Spoiler plays in sort `B` and independently on the `P`-orders when Spoiler plays in sort `P`.

Hence

\[
\mathcal K_b\equiv_q\mathcal K_{b+1}.
\]

So no rank-`q` sentence distinguishes even from odd `b`. Since `q` was arbitrary, parity is not uniformly FO definable. `□`

This is just the standard parity inexpressibility of finite linear order, lifted componentwise to two disjoint equal copies.

## 4. No uniform lexicographic rank addition

Let

\[
\operatorname{rk}(x_{i,j})=ib+j,
\qquad 0\le ib+j<N.
\]

Define externally the truncated rank-addition graph

\[
\operatorname{Add}_b(x,y,z)
\iff
\operatorname{rk}(z)=\operatorname{rk}(x)+\operatorname{rk}(y)<N.
\]

### Theorem HM-SOW-A

There is no parameter-free FO formula in the sparse coordinate scaffold uniformly defining `\operatorname{Add}_b` for all `b`.

### Proof

Assume such a formula exists. Pull it back through the interpretation to `\mathcal K_b`.

The lexicographic maximum

\[
M=x_{b-1,b-1}
\]

is uniformly definable from the recovered order. Its rank is

\[
N-1=b^2-1.
\]

Then the sentence

\[
\exists x\,\operatorname{Add}_b(x,x,M)
\]

holds exactly when `N-1` is even, equivalently exactly when `N` is odd. Since

\[
N=b^2,
\]

this holds exactly when `b` is odd.

Thus the hypothetical addition formula would define parity of `b` in `\mathcal K_b`, contradicting HM-SOW-P. `□`

Therefore the coordinate scaffold reaches order but not canonical rank addition.

## 5. No uniform EqGap

Let directed equal-gap geometry on the lexicographic data order be

\[
\operatorname{EqGap}(a,b;c,d)
\iff
\operatorname{rk}(b)-\operatorname{rk}(a)
=
\operatorname{rk}(d)-\operatorname{rk}(c),
\]

for forward intervals.

The main FCOA Arithmetic Leakage Boundary proved that, once the least point `0_X` and total order are definable,

\[
\operatorname{Add}(x,y,z)
\iff
\operatorname{EqGap}(0_X,y;x,z).
\]

Hence a uniform EqGap formula on the sparse scaffold would yield a uniform addition formula, contradicting HM-SOW-A.

Therefore

\[
\boxed{\operatorname{EqGap}\text{ is not uniformly FO definable}.}
\]

## 6. No uniform lexicographic rank multiplication

Define externally

\[
\operatorname{Mul}_b(x,y,z)
\iff
\operatorname{rk}(z)=\operatorname{rk}(x)\operatorname{rk}(y)<N.
\]

### Theorem HM-SOW-M

There is no parameter-free FO formula in the sparse coordinate scaffold uniformly defining `\operatorname{Mul}_b`.

### Proof

Assume such a formula exists. Let `T` be the uniformly definable data point of lexicographic rank `2`, i.e. the second successor of the minimum, for all sufficiently large `b`.

Then

\[
\exists x\,\operatorname{Mul}_b(T,x,M)
\]

holds exactly when `N-1=b^2-1` is even, equivalently exactly when `b` is odd.

Again this would define parity of `b` on `\mathcal K_b`, contradicting HM-SOW-P. `□`

## 7. Exact AL classification

The lexicographic order is uniformly FO definable, so the family is at least AL0.

By HM-SOW-A and the EqGap consequence, it does not reach AL1 in the main-line canonical-rank sense.

Therefore

\[
\boxed{
\text{sparse coordinate family is exactly AL0, not AL1.}
}
\]

The multiplication theorem independently confirms that the canonical rank multiplication graph is also absent.

This classification concerns the main-line AL hierarchy on the data sector; it does not claim that no unrelated arithmetic structure could ever be interpreted on some exotic quotient.

## 8. Resource count before compilation

For `N=b^2` data points:

- block incidence: `N`;
- position incidence: `N`;
- threshold incidence ordering `B`: `b(b+1)/2`;
- threshold incidence ordering `P`: `b(b+1)/2`.

Hence total incidence count is

\[
2N+b(b+1)
=3N+\sqrt N.
\]

Thus

\[
\boxed{M_{inc}=3N+O(\sqrt N)=\Theta(N).}
\]

The auxiliary coordinate and marker sectors contain only `O(\sqrt N)` elements beyond the data sort.

## 9. Resource count after fixed-two-operation compilation

Compile every incidence edge by an edge-element `e` with

\[
e\oplus e=\ell(e),
\qquad
e\otimes e=r(e).
\]

Each incidence contributes one defined cell to each of the two fixed operations. Therefore

\[
|D_\oplus|=|D_\otimes|=M_{inc},
\]

and total defined operation cells are

\[
\boxed{
2M_{inc}=6N+O(\sqrt N)=\Theta(N).
}
\]

Finite role gadgets distinguishing the finitely many incidence types change only the constant/lower-order overhead.

Hence exact AL0 is achieved in a **fixed two-operation one-sorted partial-algebra signature with linear cell cost**.

## 10. Optimal asymptotic cost

`ORDER_EMERGENCE_COST.md` gave the coarse bounded-arity lower bound

\[
M=\Omega(N)
\]

for any structure that must distinguish/order an `N`-point target sector using finitely many bounded-arity atomic cells, under the standard assumption that untouched target points remain exchangeable.

The construction above gives

\[
M=O(N).
\]

Therefore, in this auxiliary-carrier bounded-arity model,

\[
\boxed{
\text{exact AL0 cell cost}=\Theta(N).
}
\]

This is an asymptotic statement, not an optimal constant claim.

## 11. Why the construction does not secretly count

The coordinate decomposition

\[
\operatorname{rk}(x_{i,j})=ib+j
\]

exists only externally. Internally the structure sees:

- one finite order on block coordinates;
- one finite order on position coordinates;
- the Cartesian product pairing.

FO has no mechanism here to multiply the variable block index by the variable block size `b` and add the position index. If it did, parity of `b` would become definable, contradicting the two-order EF argument.

Thus the `sqrt N x sqrt N` representation supplies comparison of coordinates without supplying arithmetic conversion from coordinates to linear rank.

This is exactly the desired separation.

## 12. Comparison with G4-A

G4-A reaches AL0 with a dense orientation table on the generic sector, of quadratic scale.

The sparse coordinate family reaches the same main-line leakage level with only linear cell resources:

\[
\boxed{
\Theta(N^2)\text{-style pairwise orientation is not necessary for AL0.}
}
\]

The price is auxiliary coordinate carriers of unbounded degree.

So the correct resource tradeoff is not simply density versus leakage. It includes at least:

- number of operation cells;
- number of auxiliary carriers;
- maximum Gaifman degree;
- logical leakage level.

## 13. Sparse Order Wall Theorem

Combining the previous results gives the branch theorem package:

### Lower locality wall

\[
\boxed{\text{bounded Gaifman degree }\Rightarrow <AL0.}
\]

### Linear exact-order realization

There exists a fixed two-operation one-sorted family on an `N`-point data sector with

\[
\boxed{\Theta(N)\text{ defined cells}}
\]

such that

\[
\boxed{AL0\text{ holds but }AL1\text{ does not}.}
\]

### Asymptotic optimality

Under the bounded-arity cell-accounting model,

\[
\boxed{\Theta(N)}
\]

is the optimal asymptotic cost for exact AL0.

## 14. Boundary interpretation

The transition from the Rigidity-without-Order zone to exact AL0 can therefore be made without approaching quadratic density:

\[
\boxed{
\text{bounded local reach}
\longrightarrow
\text{sparse nonlocal coordinates}
\longrightarrow
\text{order without addition}.
}
\]

The first genuine arithmetic gateway remains variable displacement / EqGap, not coordinate comparison itself.

## 15. Status and next target

The mathematical core is now clean:

\[
\boxed{
\Theta(N)\text{ resources suffice for exact }AL0<AL1.
}
\]

The proof depends only on:

1. the explicit sparse coordinate interpretation;
2. standard FO parity inexpressibility on finite linear orders;
3. the previously proved EqGap/addition interdefinability.

The next sharp question is the corresponding cost of the next transition:

\[
\boxed{AL0\to AL1.}
\]

Can EqGap/addition also be compiled with `\Theta(N)` resources, or is there a genuine superlinear cost gap between order and additive memory?
