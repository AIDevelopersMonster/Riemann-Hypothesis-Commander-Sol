# FCOA-Z — Exact Twin-Separation Solver for Partition-Only Support

Status: theorem package v0.1  
Date: 2026-09-01

This note solves the finite recognition/optimization frontier left open in `PARTITION_ONLY_SUPPORT_COMPRESSION.md`.

The partition-only quantity is

\[
d(\mathcal P)=\min\{|R|:R\subseteq\Omega_b,\ \operatorname{Aut}(R)=K_{\mathcal P}\},
\]

where `Omega_b` is the loopless ordered-pair set on the `b` branch labels and `K_P` is the full set-partition stabilizer.

The main result is that **full automorphism computation is unnecessary**. Exactness is characterized by:

1. forbidding a finite list of cross-block point transpositions; and
2. at most one exceptional macro-swap involving the union of singleton blocks.

This yields an exact weighted Boolean optimization with `O(k^2)` variables and `O(k^2)` symmetry-breaking constraints, where `k` is the number of distinct block sizes.

Combined with the FCOA lift theorem,

\[
\boxed{m_G(J_{\mathcal P};S_\times)=t^2d(\mathcal P),}
\]

this gives an exact solver for arbitrary finite partition type `lambda`.

---

## 1. Setup

Let

\[
\mathcal P=\{B_1,\ldots,B_c\}
\]

be a partition of a finite branch set `Omega`, with

\[
|\Omega|=b.
\]

For each `d>=1`, let

\[
m_d=|\{B\in\mathcal P:|B|=d\}|.
\]

The partition stabilizer is

\[
\boxed{
K_{\mathcal P}
\cong
\prod_{d\ge1}(S_d\wr S_{m_d}).
}
\]

For `d=1`, this factor is simply

\[
S_{m_1},
\]

acting on the union `S` of all singleton blocks.

A relation `R subset Omega_b` is `K_P`-invariant iff it is a union of the following orbitals.

### Within one partition block

For `d>=2` with `m_d>0`:

\[
W_d
\]

contains all ordered distinct pairs inside one size-`d` block, over all such blocks.

Weight:

\[
\boxed{w(W_d)=m_dd(d-1).}
\]

### Between distinct equal-size blocks

For `m_d>=2`:

\[
E_d
\]

contains all ordered pairs whose endpoints lie in two different size-`d` blocks.

Weight:

\[
\boxed{w(E_d)=m_d(m_d-1)d^2.}
\]

### Between different size classes

For `d!=e`:

\[
C_{d\to e}
\]

contains all ordered pairs from a size-`d` block to a size-`e` block.

Weight:

\[
\boxed{w(C_{d\to e})=m_dm_e de.}
\]

Let `Q(P)` be this orbital set.

---

## 2. Which point transpositions already belong to `K_P`?

A transposition `(xy)` belongs to `K_P` exactly in the following cases:

1. `x,y` lie in the same partition block; or
2. `x,y` lie in two singleton blocks.

The second case occurs because all singleton blocks may be permuted arbitrarily, so their union carries the full symmetric group `S_{m_1}`.

Every other point transposition is forbidden by the target partition symmetry.

Call such a transposition a **cross-block forbidden transposition**.

---

## 3. Overgroup theorem

The crucial fact is that, apart from one explicit singleton phenomenon, every proper overgroup of a partition stabilizer already contains a forbidden point transposition.

### Theorem 3.1 — Partition-Overgroup Dichotomy

Let

\[
K_{\mathcal P}\le L\le S_\Omega.
\]

If

\[
L>K_{\mathcal P},
\]

then at least one of the following holds.

### A. Cross-block transposition

`L` contains a point transposition not belonging to `K_P`.

### B. Singleton macro-swap

Let `S` be the union of all singleton blocks. There exists a non-singleton block `B in P` such that

\[
|B|=|S|=m_1,
\]

and `L` contains an element moving the whole set `S` onto a size-`m_1` block.

Moreover every such macro-mover lies in the double coset

\[
K_{\mathcal P}\,s\,K_{\mathcal P},
\]

where `s` is any fixed bijective swap of `S` with one chosen size-`m_1` block.

#### Proof

Take

\[
g\in L\setminus K_{\mathcal P}.
\]

Suppose first that some non-singleton block `B` has image `g(B)` meeting more than one partition block.

Because `S_B<=K_P`, every transposition of two points of `B` belongs to `K_P`. Conjugating by `g` shows that every transposition between the corresponding two image points lies in `L`.

If two image points lie in distinct partition blocks and at least one of those blocks is non-singleton, this is a forbidden cross-block transposition and case A holds.

Therefore, if A fails, the only way `g(B)` can fail to be contained in one partition block is that

\[
g(B)\subseteq S.
\]

If this inclusion is proper, choose

\[
x\in g(B),\qquad y\in S\setminus g(B).
\]

The transposition `(xy)` belongs to `K_P` because both points lie in singleton blocks. Conjugating by `g^{-1}` produces a transposition between one point of `B` and one point outside `B`, hence a forbidden transposition. Contradiction.

Thus

\[
g(B)=S
\]

and consequently

\[
|B|=|S|=m_1.
\]

Now suppose `g(B)` is contained in one non-singleton partition block `C`. If it is a proper subset of `C`, choose one image point inside `g(B)` and one point of `C\setminus g(B)`. Their transposition is in `K_P`; conjugating back again gives a forbidden cross-block transposition. Therefore

\[
g(B)=C.
\]

Hence every non-singleton block not exchanged with `S` is mapped whole onto a same-size partition block.

Apply the same argument to `g^{-1}`. If no non-singleton block is exchanged with `S`, then `S` is preserved setwise and every non-singleton block is mapped to a same-size block. Since `K_P` already contains arbitrary bijections inside blocks, arbitrary permutations of equal-size blocks, and the full symmetric group on `S`, this implies

\[
g\in K_P,
\]

contrary to the choice of `g`.

Thus if case A fails, case B must occur.

Finally, on the macro-level consisting of `S` together with all blocks of size `m_1`, the subgroup induced by `K_P` fixes `S` and is symmetric on the equal-size non-singleton blocks. The point stabilizer in a symmetric action has exactly two double cosets: elements fixing the distinguished macro-point and elements moving it. Hence every macro-mover belongs to `K_P s K_P`. □

---

## 4. Exact recognition criterion

Let

\[
R\subseteq\Omega_b
\]

be `K_P`-invariant.

### Theorem 4.1 — Exact Partition-Stabilizer Recognition

\[
\boxed{
\operatorname{Aut}(R)=K_{\mathcal P}
}
\]

iff both conditions hold:

1. no forbidden cross-block point transposition preserves `R`;
2. if a singleton macro-swap is size-compatible, one fixed canonical macro-swap does not preserve `R`.

#### Proof

The forward direction is immediate.

Conversely suppose both tests pass but

\[
\operatorname{Aut}(R)>K_P.
\]

Apply Theorem 3.1 to

\[
L=\operatorname{Aut}(R).
\]

Case A contradicts test 1.

In case B, `L` contains some macro-mover `g`. By the double-coset statement,

\[
g=k_1sk_2
\]

for `k_1,k_2 in K_P`. Since `K_P<=Aut(R)`, this implies

\[
s=k_1^{-1}gk_2^{-1}\in\operatorname{Aut}(R),
\]

contradicting test 2. □

This is the central solver theorem.

---

## 5. Conjugacy reduction: only `O(k^2)` tests

Let

\[
D=\{d:m_d>0\},\qquad k=|D|.
\]

Because `K_P` is transitive on the relevant point-pair types, it suffices to test one representative transposition for each of the following types:

1. two points from distinct size-`d` blocks, for every `d>=2` with `m_d>=2`;
2. one point from a size-`d` block and one point from a size-`e` block for each unordered pair `d!=e`.

Transpositions between singleton blocks are omitted because they already lie in `K_P`.

There is at most one macro-swap size condition, namely

\[
d=m_1.
\]

Hence the number of forbidden symmetry tests is at most

\[
\boxed{
\binom{k}{2}
+|\{d>=2:m_d>=2\}|
+1.
}
\]

---

## 6. Orbital-comparison graph of a forbidden permutation

Index the `K_P` orbitals by

\[
Q=\{O_1,\ldots,O_q\}.
\]

Write a candidate invariant relation as

\[
R(y)=\bigcup_{y_i=1}O_i,
\qquad
 y_i\in\{0,1\}.
\]

For a forbidden permutation `pi`, build a graph

\[
\Gamma_\pi
\]

on the orbital indices `1,...,q` by joining `i` and `j` whenever there exists an ordered pair `z in Omega_b` such that

\[
z\in O_i,
\qquad
\pi z\in O_j,
\qquad i\ne j.
\]

### Lemma 6.1

\[
\boxed{
\pi\in\operatorname{Aut}(R(y))
\iff
 y_i=y_j
\text{ for every edge }ij\in E(\Gamma_\pi).
}
\]

#### Proof

Membership in `R(y)` is constant on each `K_P` orbital. The permutation `pi` preserves `R(y)` exactly when every ordered pair and its image have the same membership bit. This is precisely equality of the orbital bits across every orbital transition created by `pi`. □

Therefore `pi` is broken iff

\[
\boxed{
\bigvee_{ij\in E(\Gamma_\pi)}(y_i\oplus y_j)=1.
}
\]

So each forbidden symmetry contributes one **OR-of-XOR witness constraint**.

---

## 7. Exact weighted Boolean program

The branch-level problem is now exactly:

\[
\boxed{
\begin{aligned}
\text{minimize }&\sum_{i=1}^q |O_i|y_i,\\
\text{subject to }&
\bigvee_{ij\in E(\Gamma_\pi)}(y_i\oplus y_j)=1
\quad\text{for every forbidden }\pi,\\
&y_i\in\{0,1\}.
\end{aligned}}
\]

Call this the **Orbital XOR-Separation Program**.

### Theorem 7.1

The optimum of this Boolean program is exactly

\[
\boxed{d(\mathcal P).}
\]

#### Proof

Every `K_P`-invariant relation corresponds uniquely to one orbital bit vector `y`. By Theorem 4.1 it has exact automorphism group `K_P` iff it breaks every listed forbidden symmetry. Lemma 6.1 translates each break condition into the displayed OR-of-XOR clause. The objective is exactly the number of selected ordered pairs. □

---

## 8. Number of variables

The orbital count is

\[
q
=
 k(k-1)
+|\{d>=2:m_d>0\}|
+|\{d:m_d>=2\}|.
\]

Hence

\[
\boxed{q\le k^2+k.}
\]

A naive exhaustive solver therefore runs in

\[
\boxed{O^*(2^{k^2+k})}
\]

time, where polynomial factors in `b` are suppressed.

Because distinct positive block sizes satisfy

\[
1+2+\cdots+k\le b,
\]

we have

\[
k=O(\sqrt b).
\]

Thus the exact compact formulation depends on the number of **distinct block sizes**, not on the total number of partition blocks.

---

## 9. Witness-branch exact search

Full enumeration of all `2^q` assignments is unnecessary.

Each forbidden symmetry clause only requires one orbital-comparison edge to receive unequal bits.

An exact recursive solver may therefore:

1. keep a partial orbital assignment;
2. choose an unsatisfied forbidden-symmetry clause;
3. choose one comparison edge `ij` from that clause;
4. branch on

\[
(y_i,y_j)=(0,1)
\quad\text{or}\quad
(1,0);
\]

5. propagate fixed bits;
6. prune whenever the current support cost already exceeds the best solution;
7. when all symmetry clauses are witnessed, set every still-unassigned positive-cost variable to zero.

This is exact because once a clause contains a fixed unequal pair, later assignments cannot make that witness disappear.

The repository implementation `solve_partition_only_support.py` uses precisely this witness-branch principle.

---

## 10. Immediate structural corollary for repeated non-singleton sizes

Let

\[
d>=2,\qquad m_d>=2.
\]

Take two points from two different size-`d` partition blocks.

Their forbidden transposition compares exactly the within-block orbital `W_d` with the distinct-block orbital `E_d`.

### Corollary 10.1

Every exact relation satisfies

\[
\boxed{y(W_d)\ne y(E_d).}
\]

Thus one of these two orbitals is mandatory.

Since

\[
w(W_d)=m_dd(d-1),
\]

while

\[
w(E_d)=m_d(m_d-1)d^2,
\]

we always have

\[
w(W_d)<w(E_d).
\]

Therefore, except when the singleton macro-swap constraint makes the complementary choice globally useful, the cheapest local realization is

\[
W_d=1,\qquad E_d=0.
\]

This explains the repeated-block clique terms appearing in all earlier exact examples.

---

## 11. Small-case exhaustive validation

The recognition theorem and Boolean solver were checked against direct enumeration of the full symmetric group on all `K_P`-invariant orbital unions for the following partition types:

\[
(2,1),
(2,2),
(3,1),
(2,1,1),
(2,2,1),
(3,2).
\]

For every orbital bit vector in every listed case,

\[
\boxed{
\text{new criterion says exact}
\iff
\operatorname{Aut}(R)=K_P
}
\]

under full permutation enumeration.

The exact optimizer also reproduces all previously established minima, including

\[
\begin{array}{c|c}
\lambda&d(\lambda)\\
\hline
(2,1)&2\\
(3,1)&3\\
(3,2)&2\\
(3,2,1)&2\\
(3,3)&12\\
(2,2,1)&4\\
(4,2)&2\\
(3,1,1)&2\\
(3,1,1,1)&6\\
(4,3,2,1)&5.
\end{array}
\]

For example,

\[
d(4,3,2,1)=5
\]

is realized by

\[
W_2\cup C_{1\to3},
\]

with weights `2+3`.

---

## 12. FCOA consequence

For a transitive internal branch action `A` of degree `t`, the partition-only FCOA support is the full `Lambda^2` lift of the branch relation.

Therefore the arbitrary finite partition problem is now algorithmically exact:

\[
\boxed{
 m_G(J_{\mathcal P};S_\times)
=t^2\,\operatorname{OPT}(\text{Orbital XOR-Separation Program}).
}
\]

No graph-automorphism oracle is required.

---

## 13. Relation to point-determining / twin-free digraphs

The transposition part of the criterion is a weighted quotient version of the classical twin-free / point-determining condition: two vertices are forbidden to have identical in/out incidence behaviour when their interchange is not part of the target group.

Classical terminology and structure results include:

- D. P. Sumner, *Point determination in graphs*, Discrete Mathematics 5 (1973), 179–187, DOI `10.1016/0012-365X(73)90109-X`;
- R. C. Entringer and L. D. Gassman, *Line-critical point determining and point distinguishing graphs*, Discrete Mathematics 10 (1974), 43–55, DOI `10.1016/0012-365X(74)90019-3`;
- P. Hell and C. Hernández-Cruz, *Point determining digraphs, {0,1}-matrix partitions, and dualities in full homomorphisms*, Discrete Mathematics 338 (2015), 1755–1762, DOI `10.1016/j.disc.2014.12.001`.

The FCOA-specific object remains different: the digraph is constrained to be a union of orbitals of a prescribed partition stabilizer and the objective is weighted by the sizes of those orbital lifts.

No priority claim is made for the general twin-free terminology.

---

## 14. What is now solved

The previous frontier was:

\[
\text{compute }d(\lambda)\text{ for }4+\text{ size classes without ad hoc graph search.}
\]

This is now solved in the exact finite sense:

\[
\boxed{
\text{arbitrary }\lambda
\longrightarrow
\text{explicit }O(k^2)\text{-variable weighted Boolean program}
\longrightarrow
\text{exact }d(\lambda).
}
\]

The remaining question is no longer correctness or computability.

It is **complexity / closed-form compression**:

1. does the special Orbital XOR-Separation Program admit a polynomial-time algorithm;
2. or is computing `d(lambda)` NP-hard as a function of the compressed partition type;
3. which infinite partition families admit closed formulas beyond the already solved two-block, singleton-family, three-distinct-block, and equal-block cases?

That is now a clean secondary optimization frontier rather than an unresolved definition of the main invariant.