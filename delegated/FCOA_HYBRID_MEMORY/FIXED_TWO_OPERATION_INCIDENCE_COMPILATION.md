# FCOA Hybrid Memory — Fixed Two-Operation Incidence Compilation

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** theorem candidate; internally proved; hostile audit required  
**Priority discipline:** the abstract encoding of incidence structures by functions/operations is not claimed as novel. The FCOA-specific point is the exact fixed-two-operation partial-algebra realization, its automorphism transfer, and its role in hybrid value memory.

## 1. Goal

The previous scalable Carrier-Value Selection ladder used a growing number of operation symbols. The natural next question is whether a **fixed signature with exactly two binary partial operations** can exhibit unbounded value-driven rigidity while the operation domains remain maximally simple.

The answer is yes.

## 2. Input object: a finite bipartite graph

Let

\[
B=(L,R;E)
\]

be a finite simple bipartite graph with no isolated vertices. For each edge `e\in E`, write its two endpoints as

\[
\ell(e)\in L,
\qquad
r(e)\in R.
\]

Construct the one-sorted universe

\[
U_B=L\sqcup R\sqcup E,
\]

where every graph edge is represented by a new carrier element, disjoint from all graph vertices.

## 3. Two partial operations

Define exactly two binary partial operations `\oplus` and `\otimes`.

For every edge-element `e\in E`, set

\[
\boxed{e\oplus e=\ell(e),}
\]

\[
\boxed{e\otimes e=r(e).}
\]

Every other cell of both operations is undefined.

Thus

\[
D_\oplus=D_\otimes=\{(e,e):e\in E\}.
\]

The two operation domains are identical and consist only of the diagonal on the edge-elements.

## 4. Intrinsic role recovery

In the full joint one-sorted structure:

- `E` is exactly the set of elements `x` for which `x\oplus x` (equivalently `x\otimes x`) is defined;
- `L` is exactly the set of values of `\oplus`;
- `R` is exactly the set of values of `\otimes`.

Because the graph has no isolated vertices, every vertex in `L\cup R` occurs as an operation value.

The three sets `E,L,R` are pairwise disjoint by construction and are structurally separated by their operation roles. No external unary sort predicates are required.

## 5. Automorphism-transfer theorem

### Theorem HM-IC

Restriction to `L\sqcup R\sqcup E` in the obvious incidence interpretation gives a canonical isomorphism

\[
\boxed{
\operatorname{Aut}(U_B;\oplus,\otimes)
\cong
\operatorname{Aut}_{\mathrm{bip}}(B),
}
\]

where `\operatorname{Aut}_{\mathrm{bip}}(B)` denotes bipartition-preserving graph automorphisms.

### Proof

Let `g` be an automorphism of the partial algebra. Definedness preserves `E`. Values of `\oplus` preserve `L`, and values of `\otimes` preserve `R`. For every edge-element `e`,

\[
g(\ell(e))
=g(e\oplus e)
=g(e)\oplus g(e)
=\ell(g(e)),
\]

and similarly

\[
g(r(e))=r(g(e)).
\]

Hence the restriction of `g` to `L\sqcup R` preserves incidence, while its action on `E` is exactly the induced edge permutation.

Conversely, every bipartition-preserving graph automorphism permutes vertices and edges compatibly with the two endpoint maps, so it preserves both partial-operation tables.

The two constructions are inverse. `□`

Therefore every finite bipartite automorphism group can be realized as the joint automorphism group of this fixed two-operation template.

## 6. Definedness carries no incidence information

After Value-Erasure, both operation domains are the same diagonal on `E`. Hence the joint definedness reduct only recognizes the edge-elements as a set. All graph vertices become isolated from the definedness relation.

Therefore

\[
\boxed{
\operatorname{Aut}(U_B;D_\oplus,D_\otimes)
\cong
S_{|E|}\times S_{|L|+|R|}.
}
\]

Thus **all incidence geometry is carried by operation values**, not by operation definedness.

The value-induced rigidity index from definedness to the full pair is

\[
\boxed{
\frac{|E|!\,(|L|+|R|)!}
{|\operatorname{Aut}_{\mathrm{bip}}(B)|}.
}
\]

For rigid `B`, this is simply

\[
\boxed{|E|!\,(|L|+|R|)!.}
\]

## 7. Each reduct separately remains nonrigid

Consider `\oplus` alone. It is the one-sorted partial map from edge-elements to their left endpoints, represented on diagonal cells.

Let

\[
d_L(x)=|\{e\in E:\ell(e)=x\}|
\]

be the left degree. If some left vertex has degree at least `2`, then two edge-elements in that fiber may be permuted while preserving `\oplus`. Hence `\operatorname{Aut}(\oplus)\ne1`.

Likewise, if some right vertex has degree at least `2`, then `\operatorname{Aut}(\otimes)\ne1`.

More precisely, if `m_d^L` is the number of left vertices of degree `d`, then, ignoring the independent permutation of completely unused right-side elements, the map automorphism group contains the wreath-product factors

\[
S_d\wr S_{m_d^L}.
\]

In particular, the individual reducts can remain very large even when the joint structure is rigid.

## 8. Explicit infinite rigid family with fixed two operations

For every integer

\[
m\ge4,
\]

construct a tree `T_m` as follows.

Start with a path

\[
p_0-p_1-p_2-\cdots-p_m
\]

of length `m`. Attach an additional path of length `2` at `p_1`:

\[
p_1-q_1-q_2.
\]

This is a bipartite tree with

\[
|V(T_m)|=m+3,
\qquad
|E(T_m)|=m+2.
\]

### Proposition HM-IC-R

For every `m\ge4`, `T_m` is rigid.

### Proof

The vertex `p_1` is the unique vertex of degree `3`, so every automorphism fixes it. Removing `p_1` leaves three path branches of lengths

\[
1,
\qquad
2,
\qquad
m-1.
\]

For `m\ge4`, these three lengths are pairwise distinct. Hence every branch is fixed setwise. A finite path with one endpoint fixed has no nontrivial automorphism, so each branch is fixed pointwise. Therefore the whole tree is fixed pointwise. `□`

Applying the incidence compilation gives a two-operation one-sorted partial algebra `\mathcal H_m` with universe size

\[
|U_m|=(m+3)+(m+2)=2m+5
\]

and exactly

\[
m+2
\]

defined cells in each of the two operations.

The joint structure is rigid:

\[
\boxed{\operatorname{Aut}(\mathcal H_m)=1.}
\]

Yet both individual reducts are nonrigid: one bipartition side contains `p_1` of degree `3`, and the other contains an internal path vertex of degree `2`.

Therefore

\[
\boxed{
\operatorname{Aut}(\oplus)\ne1,
\qquad
\operatorname{Aut}(\otimes)\ne1,
\qquad
\operatorname{Aut}(\oplus,\otimes)=1
}
\]

for every `m\ge4` in a **fixed two-operation signature**.

## 9. Exact amplification in the rigid-tree family

For `T_m`, Value-Erasure gives

\[
S_{m+2}\times S_{m+3}.
\]

The full valued pair is rigid. Hence

\[
\boxed{
\operatorname{VRI}_{\mathrm{pair}}(\mathcal H_m)
=(m+2)!\,(m+3)!.
}
\]

Thus with only two operation symbols and `2(m+2)` total valued cells, the collapse from joint definedness symmetry to full joint rigidity grows as a product of two factorials.

The signature is fixed; only the finite tables grow.

## 10. Recovery of the graph from the operation pair

The original bipartite graph is first-order interpretable without parameters in the exact finite structure:

- edge-elements are the common loop-domain points;
- left vertices are `\oplus`-values;
- right vertices are `\otimes`-values;
- incidence is recovered by

\[
I_L(e,x)\iff e\oplus e=x,
\]

\[
I_R(e,y)\iff e\otimes e=y.
\]

Therefore the pair does not merely become rigid; it stores the entire bipartite incidence structure in its values.

This is the fixed-two-operation analogue of Domain Compilation, but the compiled object lives in **value incidence** rather than in definedness.

## 11. Association spectra and commutation

Every defined cell in either operation is diagonal. If graph vertices are not themselves edge-elements, no output is an argument of a defined cell. Hence every twice-nested product is undefined.

For either operation on `U_B^3`,

\[
\boxed{
(EQ,NEQ,LEFT,RIGHT,NONE)
=(0,0,0,0,|U_B|^3).
}
\]

The commutation locus of each operation is exactly

\[
\boxed{\{(e,e):e\in E\}.}
\]

Thus arbitrarily rich incidence memory and even complete rigidity coexist with a trivial Association Spectrum and purely diagonal commutation geometry.

## 12. Arithmetic Leakage firewall

The general incidence compiler can encode arbitrary finite bipartite graphs, so it is potentially far more expressive than the minimal two-cell VV witness. No blanket `below AL0` statement is therefore made for arbitrary compiled graph families.

For the explicit rigid-tree family, the operation pair uniformly recovers a finite tree with a distinguished branching geometry. This certainly carries more relational structure than the selector ladder. Whether it uniformly recovers a canonical total order on the growing family is a separate model-theoretic question and is **not** inferred from finite rigidity.

Accordingly:

\[
\boxed{
\text{fixed-two-operation incidence family: leakage status QUARANTINED.}
}
\]

No EqGap/addition/multiplication claim is made.

## 13. Structural consequence

The answer to the fixed-signature question is now decisive:

\[
\boxed{
\text{two fixed partial operations suffice for unbounded value-induced rigidity.}
}
\]

Indeed, they can compile an arbitrary finite bipartite incidence structure into values while their domains remain identical and maximally uninformative about incidence.

The scalable Carrier-Value Selection ladder is therefore not dependent on growing the operation signature. With two fixed operations, value memory can already carry an unbounded rigid combinatorial skeleton.

## 14. Current conclusion

For the rigid-tree family,

\[
\boxed{
S_{m+2}\times S_{m+3}
\longrightarrow
1
}
\]

under restoration of the two value tables, while each reduct remains nonrigid.

This establishes a fixed-two-operation value-amplification mechanism and identifies bipartite incidence as its natural general form.
