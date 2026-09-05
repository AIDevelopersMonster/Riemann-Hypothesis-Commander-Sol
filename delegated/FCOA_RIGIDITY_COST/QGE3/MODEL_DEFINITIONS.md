# FCOA QGE3 — Model Definitions

**Branch:** `director/fcoa-rigidity-cost`  
**Delegated line:** sparse anonymous terminal alphabets `q>=3`  
**Status:** foundational definitions for the QGE3 research line

## 0. Frozen dependencies

This note treats the following publications as immutable inputs:

- Article A, DOI `10.5281/zenodo.22157403` — complete-domain anonymous equality reducts and the arity transition `q=2 -> k_exact=3`, `q>=3 -> k_exact=4` in the stated equality-pattern class.
- Article B, DOI `10.5281/zenodo.22159246` — sparse binary component phase theorem, binary component cocycle, and the costs `lambda`, `mu`, `alpha`.

Nothing below edits or weakens those papers.

---

## 1. Carrier, sparse domain, and anonymous alphabet

Let `G` be a finite carrier and let

\[
D\subseteq G^2\setminus\Delta_G
\]

be the set of defined off-diagonal operation cells. Let `O` be a finite set of terminal outputs with

\[
|O|=q\ge3,
\]

and let

\[
c:D\to O
\]

be surjective unless explicitly stated otherwise.

The elements of `O` are **anonymous**: `O` has no distinguished identity, order, addition, cyclic structure, or preferred labeling. Temporary names such as `0,1,2` are notation only.

A carrier permutation `g in S_G` acts on cells by

\[
g(x,y)=(gx,gy).
\]

The full anonymous carrier automorphism group of the sparse layer is

\[
\boxed{
\operatorname{Aut}^{\rm an}(D,c)
=
\{g\in S_G:\ gD=D,\ \exists\pi\in S_O\ \forall p\in D,\ c(gp)=\pi(c(p))\}.
}
\]

This is the target group that any exact anonymous reduct must recover.

---

## 2. Ordered-cell comparison graph

Define the undirected ordered-cell comparison graph

\[
\Lambda(D)
\]

with vertex set `D`. Distinct cells `p,q in D` are adjacent when they are composable in at least one direction. Thus, after possibly interchanging `p,q`,

\[
p=(x,y),\qquad q=(y,z)
\]

for some carrier points with both cells defined.

Write

\[
\mathcal C(D)=\pi_0(\Lambda(D))
\]

for the set of comparison components.

For a component `C`, define its visible color support

\[
O_C=c(C)\subseteq O.
\]

The support `O_C` is not assumed to equal `O`.

---

## 3. Model T — sparse ternary adjacent-cell equality

Define

\[
\boxed{
Q_D(x,y,z)
\iff
(x,y),(y,z)\in D
\text{ and }
c(x,y)=c(y,z).
}
\]

The ternary sparse reduct is

\[
\boxed{\mathcal T(D,c)=(G;D,Q_D)}.
\]

Its carrier automorphism group is

\[
A_T(D,c)=\operatorname{Aut}(G;D,Q_D).
\]

Because `D` is retained, every `g in A_T` induces an automorphism of `Lambda(D)`. Because `Q_D` is retained, it preserves which comparison edges join equal colors and which join unequal colors.

### 3.1 Equality-edge graph and equality atoms

Let

\[
\Lambda_{=}(D,c)
\]

be the spanning subgraph of `Lambda(D)` containing exactly those comparison edges `{p,q}` for which

\[
c(p)=c(q).
\]

Its connected components are called the **T-equality atoms**. Denote the set of atoms by

\[
\mathcal A_T(D,c).
\]

Each equality atom is monochromatic, but two distinct equality atoms may still carry the same color because Model T never compares arbitrary nonadjacent cells.

For a comparison component `C`, write `\mathcal A_C` for the equality atoms contained in `C`.

### 3.2 T-constraint quotient

For each comparison component `C`, define the simple graph

\[
\boxed{H_T(C)}
\]

whose vertices are the equality atoms `\mathcal A_C`, with two distinct atoms adjacent when at least one comparison edge of `Lambda(D)` joins them.

Any such inter-atom comparison edge is necessarily an inequality edge. Therefore the original coloring descends to a proper coloring

\[
\boxed{
\kappa_C:\mathcal A_C\to O_C,
\qquad
\kappa_C(A)=c(p)\quad(p\in A).
}
\]

Thus Model T remembers the graph `H_T(C)` but, in general, forgets which nonadjacent equality atoms belong to the same global terminal fiber.

This quotient is the central object of the QGE3 line.

---

## 4. Local phase: definition and existence condition

Let `g in A_T(D,c)` and let `C in \mathcal C(D)`. Then `gC` is another comparison component.

A **local anonymous phase** for `(g,C)` is a bijection

\[
\boxed{
\phi_{g,C}:O_C\to O_{gC}
}
\]

such that

\[
\boxed{
c(gp)=\phi_{g,C}(c(p))\qquad\forall p\in C.}
\]

If it exists, this bijection is unique on the visible support `O_C`.

Equivalently, if `\bar g_C:H_T(C)\to H_T(gC)` is the graph isomorphism induced on equality atoms, then a local phase exists exactly when

\[
\kappa_{gC}(\bar g_C A)
\]

depends only on `\kappa_C(A)` and different source colors are sent to different target colors.

### Important point

For `q>=3`, **a local phase need not exist even when `C` is connected**. Preservation of ternary equality constrains only adjacent atoms in `H_T(C)`. It need not preserve the global partition of all atoms into terminal fibers.

Therefore the binary phrase “one phase per connected component” is not valid without an additional hypothesis.

If a local phase exists but `O_C` is a proper subset of `O`, it is naturally a bijection between visible supports, not a canonically chosen element of `S_q`. Any extension to all of `O` is extra, non-intrinsic data.

---

## 5. Model E — four-ary arbitrary-cell equality

Define

\[
\boxed{
E_D(x,y,u,v)
\iff
(x,y),(u,v)\in D
\text{ and }
c(x,y)=c(u,v).
}
\]

The four-ary sparse equality reduct is

\[
\boxed{\mathcal E(D,c)=(G;D,E_D)}.
\]

Unlike Model T, Model E directly records the full equality partition of **all** defined cells, including disjoint and noncomposable cells.

Consequently, for surjective `c`,

\[
\boxed{
\operatorname{Aut}(G;D,E_D)=\operatorname{Aut}^{\rm an}(D,c).
}
\]

Indeed, any carrier permutation preserving `E_D` sends each terminal fiber to a terminal fiber and therefore induces one global permutation of `O`.

This statement is independent of connectedness or sparsity of `D`.

---

## 6. Proper-coloring state of a T-component

The data lost by Model T can be expressed intrinsically.

The proper coloring `\kappa_C` induces a partition

\[
\mathcal P_C
=
\{\kappa_C^{-1}(a):a\in O_C\}
\]

of the vertices of `H_T(C)` into independent sets.

Model T remembers `H_T(C)` but not, in general, `\mathcal P_C`.

Thus the correct local hidden state is not automatically an `S_q` phase. It is the proper-coloring partition of the constraint quotient. A carrier symmetry of the ternary reduct may transport `\mathcal P_C` to a different proper-coloring partition that is not obtainable from the first by relabeling colors.

The phrase **proper-coloring transport** will refer to this action.

---

## 7. Separation of the two models

The following distinction is mandatory throughout QGE3.

### Model T

- arity 3;
- compares only composable cells;
- exact data = equality/inequality pattern on comparison edges;
- hidden freedom = proper colorings of `H_T(C)`;
- local color permutation may fail to exist.

### Model E

- arity 4;
- compares arbitrary defined cells;
- exact data = full anonymous equality partition of `D`;
- hidden freedom = none beyond one global permutation of anonymous fibers;
- exact for every finite `q` and every sparse `D`.

A theorem about Model E is never to be reported as a theorem about Model T.

---

## 8. Research firewall

1. No `Z_q` or additive structure is attached to anonymous colors.
2. `UNDEF` is not an output value.
3. Carrier labels are notation only.
4. Connectivity of `Lambda(D)` is not assumed to imply phase existence for `q>=3`.
5. A local visible-support bijection is not silently promoted to a canonical element of `S_q`.
6. Articles A and B remain frozen dependencies.
7. Novelty claims require a separate literature audit.
