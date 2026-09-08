# Reflections on Point-Image Phase Synchronization with Commander Sol

## Exact Costs, Cut-Space Packings, and a Sharp Stabilization Threshold in FCOA

**Alex Malachevsky · Commander Sol**  
**Research manuscript · Version 1.0-rc1 · 31 August 2026**

---

## Abstract

This paper works in the Fixed-Carrier Oriented Algebra (FCOA) framework fixed by **FCOA Definition 1.0**, *Fixed-Carrier Oriented Algebra (FCOA): Definition, Typed Partial Operations, Carrier Erasure, and the Canonical M0 Baseline*, https://doi.org/10.5281/zenodo.22164246. We study an abstract full-support phase-synchronization problem that arises after sparse anonymous operation components admit well-defined local color phases. Given `r` permutations `pi_1,...,pi_r in S_q`, a primitive point-image constraint has the form `pi_i(a)=pi_j(a)` for one source color `a`. Let `L_q(r)` be the minimum number of such constraints that force every satisfying tuple to be diagonal.

We prove an exact graph-theoretic reformulation: a constraint system synchronizes exactly when a canonical transversal quotient is uniquely `q`-colorable up to global color relabeling. This yields the necessary pair-union connectivity of every two source-color constraint graphs. We then determine several infinite exact families,

\[
L_2(r)=r-1,
\qquad
L_3(r)=\left\lceil\frac{3(r-1)}2\right\rceil,
\qquad
L_q(2)=q-1,
\qquad
L_q(3)=2q-3,
\]

and close the entire four-phase column:

\[
L_q(4)=
\begin{cases}
3,&q=2,\\
2q-1,&3\le q\le5,\\
12,&q=6,\\
3q-7,&q\ge7.
\end{cases}
\]

The main structural result associates to every source color a normalized binary cut space `W(P_a) <= F_2^{r-1}` whose dimension equals the saved constraint cost of that color. Synchronization forces the nonzero parts of these cut spaces to be pairwise disjoint, so

\[
\sum_a(2^{d_a}-1)\le2^{r-1}-1.
\]

A matching binary-cut construction then gives the exact large-alphabet law

\[
\boxed{L_q(r)=(r-1)q-(2^{r-1}-1)}
\]

for every

\[
q\ge2^{r-1}-1,
\]

and we prove that this threshold is exact. Thus the unresolved part of the problem is finite for every fixed `r`. The finite-geometry ingredients themselves are classical; the contribution claimed here is the FCOA point-image synchronization model, its unique-coloring and cut-space reductions, the exact families above, and the sharp stabilization theorem.

**Keywords:** FCOA; anonymous values; permutation synchronization; unique colorability; set partitions; cut spaces; partial spreads; rigidity cost.

---

## 1. Introduction

Anonymous-output layers in FCOA naturally separate two questions. The first is whether an automorphism of a sparse relational reduct induces a local permutation of visible output names. The second begins only after such local phases exist: how much additional equality information is required to force all local phases to agree with one global anonymous relabeling?

The present paper isolates the second question as a finite extremal problem.

Let

\[
O=\{0,1,\ldots,q-1\}
\]

be an anonymous alphabet and let

\[
\pi_1,\ldots,\pi_r\in S_O.
\]

For `1<=i<j<=r` and `a in O`, a primitive **point-image constraint** is

\[
[i,j;a]:\qquad \pi_i(a)=\pi_j(a).
\tag{1}
\]

A set `S` of such constraints is **synchronizing** if every satisfying tuple is diagonal:

\[
\pi_1=\cdots=\pi_r.
\tag{2}
\]

We define

\[
\boxed{
L_q(r)=\min\{|S|:S\text{ is synchronizing}\}.
}
\tag{3}
\]

The old spanning-tree construction immediately gives

\[
L_q(r)\le(q-1)(r-1),
\tag{4}
\]

because equality of two permutations on `q-1` source points forces equality everywhere. For `q=2`, this is exact. For `q>=3`, however, bijectivity allows constraints on different component pairs to interact, and the tree bound is far from the whole story.

The main results of this paper are:

1. an exact reduction of synchronization to unique colorability of a special transversal quotient;
2. a universal pair-union connectivity condition and the lower bound
   \[
   L_q(r)\ge\left\lceil\frac{q(r-1)}2\right\rceil;
   \tag{5}
   \]
3. exact formulas on the complete `q=3` row and `r=2,3,4` columns;
4. a universal binary-cut construction using all nonzero vectors of `F_2^{r-1}`;
5. a cut-space packing inequality that matches that construction and yields the exact stabilization theorem
   \[
   L_q(r)=(r-1)q-(2^{r-1}-1)
   \quad(q\ge2^{r-1}-1),
   \tag{6}
   \]
   with exact threshold.

The finite pre-stabilization region remains open for `r>=5`; this is deliberately separated from the proved tail.

---

## 2. FCOA framework and scope

### 2.1 Framework statement

The canonical framework is FCOA Definition 1.0 [1]. The underlying FCOA motivation is a finite carrier `G` with a partial operation whose terminal outputs form anonymous value fibers. Sparse relational reducts can decompose the defined-cell geometry into comparison components. In the **full-support phase-admissible sector**, each relevant component carries a local permutation of the same anonymous terminal alphabet `O`.

This paper passes to the derived synchronization layer. The phase-index carrier is

\[
R=\{1,\ldots,r\},
\]

and the terminal sort is the anonymous set `O`. The primitive data studied here are not new operation values or new real FCOA cells; they are the abstract equality tests (1) between images of one source color under two local phases. Relative to the preceding sparse multicolor transport layer, the only added structure is a selected family of these point-image equalities.

### 2.2 Erasure and recovery

The **erasure convention** is that names of terminal values remain anonymous: simultaneous left composition

\[
\pi_i\mapsto\sigma\circ\pi_i
\qquad(\sigma\in S_q)
\tag{7}
\]

changes only the common output naming and preserves every constraint. Consequently one may normalize one phase to the identity.

The **recovery target** is not recovery of named colors. It is recovery of one global anonymous relabeling, equivalently diagonalization (2).

### 2.3 Firewall

The quantity `L_q(r)` is an abstract full-support phase-synchronization cost. It is not the minimum number of real operation cells needed to repair an FCOA carrier. No multicolor real-cell invariant `alpha_q` is defined here, and no inequality comparing such an invariant with `L_q(r)` is asserted. No arithmetic on the FCOA carrier is imported.

---

## 3. Constraint graphs and forest reduction

For each source color `a in O`, define a graph

\[
\Gamma_a=\Gamma_a(S)
\]

on vertex set `R` by

\[
\{i,j\}\in E(\Gamma_a)
\quad\Longleftrightarrow\quad
[i,j;a]\in S.
\tag{8}
\]

Equality propagates along paths. Hence only the connected-component partition of `Gamma_a` matters.

### Lemma 3.1 — forest reduction

Every constraint system can be replaced, without changing its satisfying tuples and without increasing its size, by one in which every `Gamma_a` is a forest.

**Proof.** Replace every connected component of `Gamma_a` by an arbitrary spanning tree. The new constraints impose exactly the same equality relation on the values `pi_i(a)`. Repeating independently for all `a` proves the claim. `square`

For a reduced system let

\[
m_a=|E(\Gamma_a)|,
\qquad
c_a=\kappa(\Gamma_a)=r-m_a.
\tag{9}
\]

Then

\[
|S|=\sum_a m_a.
\tag{10}
\]

---

## 4. Synchronization is a unique-coloring problem

Let `B_a` be the set of connected components of `Gamma_a`. Construct a graph `H(S)` as follows.

Its vertices are

\[
(a,B),\qquad a\in O,\ B\in B_a.
\tag{11}
\]

For every phase index `i`, let `B_a(i)` be the component of `Gamma_a` containing `i`. Join all `q` vertices

\[
(a,B_a(i)),\qquad a\in O,
\tag{12}
\]

pairwise. Thus every phase contributes a canonical `K_q` transversal. There is a canonical proper coloring

\[
\chi_0(a,B)=a.
\tag{13}
\]

### Theorem 4.1 — synchronization / unique-coloring equivalence

A constraint family `S` is synchronizing if and only if the canonical coloring `chi_0` of `H(S)` is the unique proper `q`-coloring up to permutation of the `q` color names.

**Proof.** Suppose first that `(pi_1,...,pi_r)` satisfies `S`. If `i,j` lie in the same component `B` of `Gamma_a`, path propagation gives `pi_i(a)=pi_j(a)`. Therefore

\[
F(a,B):=\pi_i(a)\qquad(i\in B)
\tag{14}
\]

is well defined. On the transversal (12) contributed by index `i`, the `F`-values are

\[
\pi_i(0),\ldots,\pi_i(q-1),
\]

which are pairwise distinct. Hence `F` is a proper `q`-coloring of `H(S)`.

Conversely, let `F` be a proper `q`-coloring. Every canonical transversal is a `K_q`, so its vertices receive all `q` colors exactly once. Define

\[
\pi_i(a)=F(a,B_a(i)).
\tag{15}
\]

Then each `pi_i` is a permutation. If `[i,j;a] in S`, vertices `i,j` lie in the same `Gamma_a` component and (15) gives `pi_i(a)=pi_j(a)`. Thus proper colorings are in bijection with satisfying phase tuples.

The diagonal tuples are exactly the colorings obtained from `chi_0` by one global output-color permutation. Hence synchronization is equivalent to uniqueness of `chi_0` up to global relabeling. `square`

This theorem places the extremal problem next to classical unique colorability, while preserving a severe additional restriction: the quotient must arise from `r` canonical `K_q` transversals and identifications occur only within one source-color class.

---

## 5. Pair-union connectivity

### Theorem 5.1

If `S` is synchronizing, then for every two distinct source colors `a,b`,

\[
\boxed{\Gamma_a\cup\Gamma_b\text{ is connected}.}
\tag{16}
\]

**Proof.** Suppose `Gamma_a union Gamma_b` is disconnected. Let `X` be a nonempty proper union of its connected components. No constraint of source color `a` or `b` crosses the cut `(X,R\X)`. Put `sigma=(a b)` and define

\[
\pi_i=\sigma\quad(i\in X),
\qquad
\pi_i=id\quad(i\notin X).
\tag{17}
\]

Every internal constraint compares equal permutations. Every crossing constraint has a source color different from `a,b`, hence fixed by `sigma`. Thus all constraints are satisfied, but the tuple is non-diagonal. Contradiction. `square`

For a reduced system, (16) implies

\[
m_a+m_b\ge r-1.
\tag{18}
\]

Summing (18) over all unordered pairs gives

\[
(q-1)\sum_a m_a\ge\binom q2(r-1).
\]

### Corollary 5.2 — half-density bound

\[
\boxed{
L_q(r)\ge\left\lceil\frac{q(r-1)}2\right\rceil.
}
\tag{19}
\]

The connectivity statement is the LQR specialization of a classical property of uniquely colorable graphs [3]. Its role here is as the first lower-bound engine in the restricted transversal quotient.

---

## 6. Exact low-dimensional families

### 6.1 Binary alphabet

For `q=2`, agreement on one source color identifies two permutations of a two-element set. Therefore a connected graph on the `r` phase indices is necessary and sufficient.

### Theorem 6.1

\[
\boxed{L_2(r)=r-1.}
\tag{20}
\]

### 6.2 Two phases

Two permutations of a `q`-element set that agree on `q-1` source points agree on the final point. Fewer than `q-1` constraints leave at least two unconstrained source points and allow a transposition there.

### Theorem 6.2

\[
\boxed{L_q(2)=q-1.}
\tag{21}
\]

### 6.3 Three colors

For `q=3`, (18) gives

\[
m_0+m_1\ge r-1,
\quad
m_0+m_2\ge r-1,
\quad
m_1+m_2\ge r-1,
\]

and therefore

\[
L_3(r)\ge\left\lceil\frac{3(r-1)}2\right\rceil.
\tag{22}
\]

The matching construction is a three-constraint gadget. Suppose `rho` is already synchronized and `sigma,tau in S_3` are new. Impose

\[
[\rho,\sigma;0],
\qquad
[\rho,\tau;1],
\qquad
[\sigma,\tau;2].
\tag{23}
\]

After global normalization take `rho=id`. Then `sigma` fixes `0`, `tau` fixes `1`, and `sigma(2)=tau(2)`. If `sigma` were the nontrivial permutation fixing `0`, then `sigma(2)=1`, impossible for `tau(2)` because `tau(1)=1`. Hence `sigma=id`; then `tau(2)=2`, and `tau=id`.

Attaching two phases at a time gives the lower bound exactly.

### Theorem 6.3

For every `r>=1`,

\[
\boxed{
L_3(r)=\left\lceil\frac{3(r-1)}2\right\rceil.
}
\tag{24}
\]

### 6.4 Three phases

For `r=3`, every reduced `Gamma_a` has `m_a in {0,1,2}`. If one color has `m_a=0`, every other color must be connected, giving cost at least `2(q-1)`. Otherwise each color has at least one edge. Two one-edge colors must use different edges of the phase triangle for their union to be connected. There are only three edges, so at most three colors have `m_a=1`; all remaining colors have `m_a=2`. Hence

\[
L_q(3)\ge3+2(q-3)=2q-3.
\tag{25}
\]

For the matching construction use the three-color triangle gadget

\[
[0,1;0],\quad[0,2;1],\quad[1,2;2]
\tag{26}
\]

and, for every extra source color `a>=3`, impose `[0,1;a]` and `[0,2;a]`. The extra colors are fixed across all phases, reducing the remaining action to `S_3`, where (26) synchronizes.

### Theorem 6.4

For every `q>=3`,

\[
\boxed{L_q(3)=2q-3.}
\tag{27}
\]

---

## 7. The exact four-phase column

For `r=4`, every source color determines a partition `P_a` of four phase indices. Under forest reduction its rank

\[
m_a=4-|P_a|
\]

lies in `{0,1,2,3}`.

The compatibility condition from Theorem 5.1 becomes

\[
P_a\vee P_b=\mathbf 1
\qquad(a\ne b),
\tag{28}
\]

where `mathbf 1` is the one-block partition.

The four-point partition lattice gives the complete low-rank classification:

- the discrete rank-zero partition is compatible only with the one-block rank-three partition;
- two rank-one partitions are never compatible;
- a fixed rank-one partition is compatible with exactly four rank-two partitions;
- there are exactly seven rank-two partitions, and any two distinct ones are compatible;
- a rank-three partition is compatible with all partitions.

Let `n_k` be the number of colors of rank `k`. If no rank-zero color occurs,

\[
|S|=n_1+2n_2+3n_3=3q-(2n_1+n_2).
\tag{29}
\]

The classification yields the maximal defect

\[
2n_1+n_2=\begin{cases}
q+1,&3\le q\le5,\\
6,&q=6,\\
7,&q\ge7.
\end{cases}
\tag{30}
\]

and therefore the corresponding lower bounds.

For `q=3`, the five-constraint construction is exactly an instance of the already proved `S_3` recursive gadget in Theorem 6.3, after phase/color relabeling. For `q=4,5`, one may use one rank-one partition plus respectively three or four of its compatible rank-two partners; direct normalization and injectivity force all phases to the identity. For `q=6`, extend an optimal `q=5` gadget by making the sixth source color connected. For `q=7`, use all seven bipartitions of four phase indices; this is the `r=4` instance of the binary-cut construction proved in Section 8. Extra colors for `q>7` are made connected.

### Theorem 7.1 — exact four-phase cost

\[
\boxed{
L_q(4)=
\begin{cases}
3,&q=2,\\
2q-1,&3\le q\le5,\\
12,&q=6,\\
3q-7,&q\ge7.
\end{cases}
}
\tag{31}
\]

The isolated value at `q=6` is therefore structural rather than numerical noise: the rank-one architecture can coexist with only four rank-two colors, whereas the all-bipartition architecture has capacity seven.

---

## 8. Universal binary-cut synchronization

Fix `r>=2` and put

\[
n=r-1,
\qquad
V=\mathbb F_2^n\setminus\{0\}.
\tag{32}
\]

Use one active source color for each vector

\[
v=(v_1,\ldots,v_n)\in V.
\]

Thus

\[
q_0=|V|=2^{r-1}-1.
\tag{33}
\]

For color `v`, partition the phases into

\[
B_v^0=\{0\}\cup\{i:v_i=0\},
\qquad
B_v^1=\{i:v_i=1\}.
\tag{34}
\]

Connect each block internally by a spanning tree. Since there are two nonempty blocks, color `v` costs `r-2` constraints.

### Theorem 8.1 — binary-cut gadget

The family (34) synchronizes the `r` phases in `S_{2^{r-1}-1}`.

**Proof.** Normalize `pi_0=id`. Fix `i>=1` and define

\[
H_i=\{v:v_i=0\},
\qquad
A_i=\{v:v_i=1\}.
\tag{35}
\]

If `v in H_i`, phases `0` and `i` lie in the same connected block `B_v^0`, so

\[
\pi_i(v)=v.
\tag{36}
\]

Thus `pi_i` fixes `H_i` pointwise and preserves `A_i` setwise.

For `j!=i` and `v in A_i cap A_j`, phases `i,j` lie in the same block `B_v^1`, hence

\[
\pi_i(v)=\pi_j(v).
\tag{37}
\]

The left side belongs to `A_i` and the right side to `A_j`; therefore the common value lies in `A_i cap A_j`. Hence `pi_i` preserves every subset `A_i cap A_j` setwise.

On `A_i`, the membership bits in the sets `A_i cap A_j` for `j!=i` are precisely the remaining coordinates `(v_j)_{j!=i}`. They distinguish all vectors of `A_i`. Thus `pi_i` fixes every vector of `A_i`, and together with (36) this gives `pi_i=id`. This holds for all `i`, so all phases are diagonal before normalization. `square`

The gadget costs

\[
(r-2)(2^{r-1}-1).
\tag{38}
\]

For every `q>q_0`, make each extra source color connected on the `r` phases at cost `r-1`. Therefore

\[
L_q(r)\le(r-1)q-(2^{r-1}-1)
\quad(q\ge q_0).
\tag{39}
\]

---

## 9. Cut spaces and the packing bound

The matching lower bound comes from a canonical encoding of every source-color component partition.

Let `P` be a partition of the phase set

\[
R=\{0,1,\ldots,r-1\}.
\]

Normalize binary cuts by fixing the bit at phase `0` to zero and identify them with

\[
\mathbb F_2^{r-1}.
\]

Define

\[
W(P)=\{x\in\mathbb F_2^{r-1}:x\text{ is constant on every block of }P\},
\tag{40}
\]

with the understood extension `x_0=0`.

### Lemma 9.1

If `P` has `c` blocks, then

\[
\dim W(P)=c-1.
\tag{41}
\]

**Proof.** The block containing phase `0` is forced to bit zero. Every other block chooses its bit independently. Hence `|W(P)|=2^{c-1}`. `square`

For the component partition `P_a` of a forest-reduced `Gamma_a`, define the saved cost

\[
d_a=(r-1)-m_a.
\tag{42}
\]

Since `m_a=r-c_a`,

\[
d_a=c_a-1=\dim W(P_a).
\tag{43}
\]

### Lemma 9.2 — join/intersection identity

For any partitions `P,Q`,

\[
\boxed{W(P)\cap W(Q)=W(P\vee Q).}
\tag{44}
\]

**Proof.** A normalized binary cut belongs to both spaces exactly when it is constant on every block of `P` and every block of `Q`. This is equivalent to being constant on every equivalence class generated jointly by those blocks, namely the blocks of `P vee Q`. `square`

By Theorem 5.1,

\[
P_a\vee P_b=\mathbf 1
\quad(a\ne b),
\]

so

\[
W(P_a)\cap W(P_b)=\{0\}.
\tag{45}
\]

Thus the nonzero vectors of the cut spaces are pairwise disjoint. Since `F_2^{r-1}` has `2^{r-1}-1` nonzero vectors:

### Theorem 9.3 — defect packing inequality

Every synchronizing system satisfies

\[
\boxed{
\sum_a(2^{d_a}-1)\le2^{r-1}-1.
}
\tag{46}
\]

The counting step in (46) is standard finite-geometry packing once the cut-space reduction has been made; it is not claimed here as a new theorem about partial spreads or vector-space partitions [5,6].

Since

\[
d\le2^d-1
\qquad(d\ge0),
\tag{47}
\]

we get

\[
\sum_a d_a\le2^{r-1}-1.
\tag{48}
\]

But by (42),

\[
|S|=(r-1)q-\sum_a d_a.
\tag{49}
\]

Therefore:

### Corollary 9.4 — universal defect lower bound

\[
\boxed{
L_q(r)\ge(r-1)q-(2^{r-1}-1).
}
\tag{50}
\]

---

## 10. Exact large-alphabet stabilization

We now combine Sections 8 and 9.

### Theorem 10.1 — exact stabilization theorem

For every `r>=2` and every

\[
q\ge2^{r-1}-1,
\]

\[
\boxed{
L_q(r)=(r-1)q-(2^{r-1}-1).
}
\tag{51}
\]

Moreover the threshold is exact: if

\[
q<2^{r-1}-1,
\]

then

\[
L_q(r)>(r-1)q-(2^{r-1}-1).
\tag{52}
\]

**Proof.** The lower bound is Corollary 9.4. The binary-cut construction gives equality when `q>=2^{r-1}-1`.

Suppose equality held in (50). Then

\[
\sum_a d_a=2^{r-1}-1.
\tag{53}
\]

From (46) and (47),

\[
\sum_a d_a
\le
\sum_a(2^{d_a}-1)
\le
2^{r-1}-1.
\tag{54}
\]

Equality in (53) forces equality termwise in (47), which for nonnegative integers occurs only for `d_a in {0,1}`. Hence every positive-defect color contributes exactly one nonzero cut vector. To obtain total defect `2^{r-1}-1`, at least that many positive-defect colors are necessary. Therefore

\[
q\ge2^{r-1}-1.
\]

So equality is impossible below that threshold. `square`

### Corollary 10.2

The stabilization threshold is

\[
\boxed{q_0(r)=2^{r-1}-1.}
\tag{55}
\]

For example,

\[
L_q(5)=4q-15\qquad(q\ge15),
\tag{56}
\]

and

\[
L_q(6)=5q-31\qquad(q\ge31).
\tag{57}
\]

Thus for every fixed `r`, only finitely many alphabet sizes remain outside the exact linear tail.

---

## 11. The finite pre-stabilization problem

The proof of Theorem 10.1 gives a stronger interface for the unresolved sector. Define

\[
\mathcal D_r(q)
=
\max\left\{
\sum_{i=1}^q\dim W(P_i):
W(P_i)\cap W(P_j)=\{0\}\ (i\ne j)
\right\},
\tag{58}
\]

where zero-dimensional spaces may pad the family.

Then necessarily

\[
L_q(r)\ge(r-1)q-\mathcal D_r(q).
\tag{59}
\]

This is only a lower-bound interface: pairwise trivial intersection is necessary for synchronization but need not by itself imply unique colorability of the transversal quotient.

The genuinely unresolved regime is

\[
\boxed{
4\le q<2^{r-1}-1,
\qquad r\ge5.
}
\tag{60}
\]

For `r=5`, only `4<=q<=14` remain. Exact weighted packing computations provide a useful hostile check, but no unproved packing optimum is promoted to an LQR theorem here.

---

## 12. Finite verification

Two independent verification scripts accompany the theorem development in the repository.

`verify_lqr.py` checks:

- the exact `q=3` constructions for small `r` by normalized exhaustive enumeration;
- the exact `r=3` constructions for small `q`;
- the first exact `r=4` values using the partition quotient.

`verify_lqr_cutspace.py` independently checks:

- Bell-number enumeration of phase partitions through `r=6`;
- `|W(P)|=2^{|P|-1}`;
- `W(P) cap W(Q)=W(P vee Q)` for all partition pairs through `r=6`;
- the weighted partition-packing capacity for `r=5` through the stabilization threshold `q=15`.

The proofs of the infinite formulas do not depend on these computations.

---

## 13. Literature position and novelty boundary

The graph-theoretic and finite-geometric surroundings of the result are classical.

Harary, Hedetniemi and Robinson [3] established foundational properties of uniquely colorable graphs, including connectivity of the graph induced by every pair of color classes. Bollobas [4] developed further structural results on unique colorability. Our Theorem 5.1 is therefore not claimed as a new general unique-colorability theorem; its role is the specialized form induced by the LQR transversal quotient.

Pairwise trivially intersecting subspaces, partial spreads and vector-space partitions are also classical [5,6]. Once (45) has been obtained, counting their nonzero vectors is standard. The novelty claim is therefore deliberately restricted to the following chain inside the FCOA phase-synchronization problem:

\[
\text{point-image constraints}
\longrightarrow
\text{transversal unique-coloring quotient}
\longrightarrow
\text{component partitions}
\longrightarrow
\text{canonical binary cut spaces}
\longrightarrow
\text{sharp LQR stabilization}.
\tag{61}
\]

Permutation synchronization also has an established algorithmic literature, typically concerned with recovering globally consistent matchings from noisy pairwise permutation estimates [7]. The present parameter differs: it asks for the minimum number of exact same-source point-image equalities sufficient to force an arbitrary tuple in `S_q^r` to be diagonal.

A dedicated search performed for this project did not locate the exact extremal parameter `L_q(r)` in this form. This is a conservative literature statement, not an absolute priority claim.

---

## 14. Limitations and open problems

The main limitations are structural and explicit.

1. `L_q(r)` measures abstract phase-link constraints, not real FCOA operation-cell additions.
2. The pre-stabilization sector (60) is not solved in general.
3. Pairwise cut-space packing is necessary but may fail to capture all unique-coloring obstructions.
4. The present paper does not define a multicolor analogue of the binary actual-cell repair parameter.
5. The local existence of permutation-valued phases is assumed; sparse ternary reducts with `q>=3` can fail before the synchronization problem is even defined, as shown in the companion sparse multicolor transport manuscript [2].

Natural next problems are to determine `L_4(r)` for general `r`, solve `L_q(5)` for `4<=q<=14`, and characterize when an optimal partition-subspace packing is realized by a synchronizing transversal quotient.

---

## 15. Conclusion

The point-image synchronization cost has a sharper structure than the naive spanning-tree estimate suggests. The correct lower-bound objects are not merely graphs on the phase indices. They are component partitions, and after normalization those partitions produce binary cut spaces whose nonzero vectors must pack disjointly.

This leads to three layers of exact structure:

\[
L_3(r)=\left\lceil\frac{3(r-1)}2\right\rceil,
\]

an exact four-phase transition,

\[
L_q(4)=3,\ 2q-1,\ 12,\ 3q-7
\]

in its respective ranges, and the general stabilization theorem

\[
\boxed{
L_q(r)=(r-1)q-(2^{r-1}-1)
\quad\text{iff the linear lower bound is attainable, with attainment beginning exactly at }q=2^{r-1}-1.
}
\]

For each fixed number of phases, the unsolved problem is therefore finite. In FCOA terms, the result provides an exact capacity theorem for synchronizing already-existing anonymous full-support phases, while keeping distinct the harder problem of realizing such synchronization by genuine operation-cell extensions.

---

## References

[1] A. Malachevsky and Commander Sol, **Fixed-Carrier Oriented Algebra (FCOA): Definition, Typed Partial Operations, Carrier Erasure, and the Canonical M0 Baseline**, 2026. DOI: `10.5281/zenodo.22164246`. https://doi.org/10.5281/zenodo.22164246.

[2] A. Malachevsky and Commander Sol, **Reflections on Sparse Multicolor Transport with Commander Sol: Proper-Coloring Obstructions, Local Phase Groupoids, and Exact Gluing in FCOA**, companion manuscript, 2026, repository package `papers/FCOA-SPARSE-MULTICOLOR-TRANSPORT/`.

[3] F. Harary, S. T. Hedetniemi, R. W. Robinson, **Uniquely colorable graphs**, *Journal of Combinatorial Theory* 6(3) (1969), 264–270. DOI: `10.1016/S0021-9800(69)80086-4`.

[4] B. Bollobas, **Uniquely colorable graphs**, *Journal of Combinatorial Theory, Series B* 25 (1978), 54–61. DOI: `10.1016/S0095-8956(78)80010-0`.

[5] O. Heden, **A survey of the different types of vector space partitions**, *Discrete Mathematics, Algorithms and Applications* 4(1) (2012), 1250001. DOI: `10.1142/S1793830912500012`.

[6] T. Honold, M. Kiermaier, S. Kurz, **Partial spreads and vector space partitions**, in *Network Coding and Subspace Designs*, Springer, 2018, 131–170. DOI: `10.1007/978-3-319-70293-3_7`.

[7] D. Pachauri, T. Kondor, V. Singh, **Solving the multi-way matching problem by permutation synchronization**, *Advances in Neural Information Processing Systems 26*, 2013.

---

## Reproducibility note

The theorem-source files and independent finite verifiers are maintained under

`delegated/FCOA_RIGIDITY_COST/QGE3/`

in the repository

`https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol`

on the research branch `director/fcoa-rigidity-cost` at manuscript assembly time.
