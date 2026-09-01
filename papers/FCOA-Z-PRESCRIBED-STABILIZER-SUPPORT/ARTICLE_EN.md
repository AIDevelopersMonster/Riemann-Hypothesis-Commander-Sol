# Prescribed-Stabilizer Support in Fixed-Carrier Oriented Algebra
## Wreath Coherence, Partition Compression, and Exact Orbital Separation

**Author:** Alex Malachevsky  
**Series:** Commander Sol / Fixed-Carrier Oriented Algebra  
**Status:** publication manuscript draft v0.9  
**Date:** 2026-09-01

---

## Abstract

Fixed-Carrier Oriented Algebra (FCOA) studies how typed partial operations on a fixed active carrier can store structural information in their value geometry after auxiliary carrier structure has been erased. The framework used here is the FCOA Definition and canonical baseline of Malachevsky, Zenodo DOI **10.5281/zenodo.22164246**. We introduce the prescribed-stabilizer support quantity

\[
m_G(H;S)=\min\{|F|:F\subseteq S,\ \operatorname{Stab}_G(F)=H\},
\]

not as a claim of priority for the abstract group-action notion, but as a resource measure for exact residual symmetry in FCOA value memory. We solve a family of such problems for imprimitive wreath actions. If a transitive permutation group \(A\leq\operatorname{Sym}(\Lambda)\) of degree \(t\) acts independently on \(b\) isomorphic branches, then on the ordered cross-branch cell set \(S_\times\) the exact cost of imposing one common internal phase is

\[
m_{A\wr S_b}(\Delta A\times S_b;S_\times)=b(b-1)t.
\]

For an arbitrary branch partition \(\mathcal P\) with block sizes \(n_1,\ldots,n_c\), the exact cost of remembering both the partition and one common internal phase within each block is

\[
m_G(H_{\mathcal P};S_\times)=t\sum_{j=1}^c n_j(n_j-1).
\]

In contrast, if internal phases remain independent and only the partition must be remembered, every selected branch pair must carry a full \(t^2\)-fiber. The problem reduces exactly to minimizing the number of arcs in a loopless directed relation whose automorphism group is the concrete partition stabilizer \(K_{\mathcal P}\). We prove an overgroup dichotomy showing that exactness is characterized by breaking all forbidden cross-block point transpositions together with at most one singleton macro-swap. This yields an exact weighted Orbital XOR-Separation Program over \(O(k^2)\) variables, where \(k\) is the number of distinct block sizes. The resulting theory exhibits genuine complement compression and a resource non-monotonicity: a semantically stronger phase-coherent memory can require fewer FCOA cells than partition-only memory.

---

## 1. Introduction

A recurring problem in algebraic coding is to destroy unwanted symmetry while preserving a prescribed residual symmetry. Classical permutation-group theory contains several closely related themes: regular sets, distinguishing colorings, relation groups, 2-closures, orbital digraphs, point-determining graphs, and graph realizations with prescribed automorphism group. The present problem is narrower.

The active carrier and its ambient action are fixed. A value fiber of a typed partial operation is allowed to select some cells of a fixed \(G\)-set \(S\). We ask for the smallest support whose setwise stabilizer is exactly a prescribed subgroup \(H\leq G\).

This leads to the organizing quantity

\[
\boxed{
 m_G(H;S)=\min\{|F|:F\subseteq S,\ \operatorname{Stab}_G(F)=H\},
}
\tag{1}
\]

with \(m_G(H;S)=\infty\) if no such subset exists.

The primary FCOA interpretation is value memory. A hidden connection or branch partition is first used to choose values of a partial operation and is then erased from the carrier signature. What remains is a value geometry whose automorphism group should be exactly the intended residual symmetry.

The paper has three layers.

1. **Phase coherence.** A thin diagonal internal relation couples independent branch actions and gives exact support formulas.
2. **Partition-only memory.** If internal branch phases must remain independent, thin diagonal relations are forbidden; one must select whole internal fibers, reducing the problem to a sparse directed relation on branch labels.
3. **Exact orbital separation.** For arbitrary partition type, exact branch-level optimization is characterized by a finite list of forbidden transpositions plus one possible singleton macro-swap and becomes a weighted Boolean program.

The point is not that setwise stabilizers or orbital relations are new. They are classical. The contribution is the exact fixed-action support theory for this FCOA family and the resulting resource laws.

---

## 2. FCOA setting and the support invariant

### 2.1 Fixed carrier and terminal values

In the FCOA framework, the active carrier is a distinguished sort on which partial operations may be evaluated. Terminal output sorts contain values that, by default, are not legal inputs to further active operations.

For the present paper, only the following abstract structure is required.

Let \(X\) be a finite active carrier with an ambient automorphism group \(G\leq\operatorname{Sym}(X)\). Let \(S\subseteq X^2\) be a fixed operation-cell domain or a fixed \(G\)-orbit of candidate cells. A terminal-valued operation can distinguish a subset

\[
F\subseteq S
\]

by assigning it one output value and assigning the complement another output value.

If the terminal values are named, the active residual symmetry is the setwise stabilizer of \(F\). If the values are anonymous, an additional output-swap issue may occur; we treat this separately.

### 2.2 Prescribed-stabilizer support

Equation (1) measures the smallest number of selected cells needed to obtain exactly \(H\) as the residual active group.

This is deliberately different from two nearby resources.

- A distinguishing number minimizes the number of colors.
- A regular set asks for trivial setwise stabilizer.

Here the output alphabet may already have cardinality two, while the support size remains a nontrivial optimization problem, and the target stabilizer may be nontrivial.

---

## 3. Two general reductions

### Proposition 3.1 — Orbit-union reduction

Let \(G\) act on a finite set \(S\), and let \(H\leq G\). If

\[
H\leq\operatorname{Stab}_G(F),
\]

then \(F\) is a union of \(H\)-orbits on \(S\).

#### Proof

For every \(x\in F\) and every \(h\in H\), setwise invariance gives \(hx\in F\). Hence \(Hx\subseteq F\), so \(F\) is a union of \(H\)-orbits. ∎

Therefore

\[
m_G(H;S)
=
\min
\left\{
\sum_{O\in\mathcal A}|O|:
\mathcal A\subseteq\operatorname{Orb}_H(S),
\operatorname{Stab}_G\!\left(\bigcup_{O\in\mathcal A}O\right)=H
\right\}.
\tag{2}
\]

### Proposition 3.2 — Normal-subgroup quotient reduction

Assume \(H\triangleleft G\), and put \(Q=G/H\). Let \(\Omega=H\backslash S\) be the set of \(H\)-orbits on \(S\), with weight \(w(O)=|O|\). Then

\[
\boxed{
 m_G(H;S)=
\min\left\{
\sum_{O\in A}w(O):
A\subseteq\Omega,
\operatorname{Stab}_Q(A)=1
\right\}.
}
\tag{3}
\]

#### Proof

An \(H\)-invariant subset of \(S\) is exactly a union of \(H\)-orbits, hence corresponds to a subset \(A\subseteq\Omega\). Because \(H\) is normal, \(G/H\) acts on \(\Omega\), and

\[
\operatorname{Stab}_G(F)/H
\cong
\operatorname{Stab}_Q(A).
\]

Exact stabilizer \(H\) is therefore equivalent to trivial stabilizer in \(Q\). ∎

### Corollary 3.3 — Index-two support formula

If \([G:H]=2\), let \(q\) denote the nontrivial element of \(G/H\). Then

\[
\boxed{
 m_G(H;S)=
\min\{|O|:O\in H\backslash S,\ qO\neq O\}.
}
\tag{4}
\]

#### Proof

A subset of the weighted quotient orbit set has trivial \(C_2\)-stabilizer exactly when it is not fixed by \(q\). A minimum such subset is a single quotient point moved by \(q\). ∎

The original seven-vertex branch-coherence example \(D_8\to V_4\) is an instance of (4).

---

## 4. Wreath branch geometry

Let \(\Lambda\) be a set of size

\[
|\Lambda|=t\geq2,
\]

and let

\[
A\leq\operatorname{Sym}(\Lambda)
\]

be transitive.

Take \(b\geq2\) isomorphic branches. The active imprimitive carrier is

\[
X=[b]\times\Lambda.
\tag{5}
\]

The ambient group is the natural wreath product

\[
G=A\wr S_b=A^b\rtimes S_b.
\tag{6}
\]

Write an element as

\[
g=(\sigma_1,\ldots,\sigma_b;\pi),
\]

where \(\sigma_r\in A\) and \(\pi\in S_b\).

The ordered cross-branch operation-cell set is

\[
S_\times
=
\left\{
((r,i),(s,j)):r\neq s
\right\},
\tag{7}
\]

with

\[
|S_\times|=b(b-1)t^2.
\tag{8}
\]

---

## 5. Global phase coherence

A global coherence identification declares the same internal coordinate on every branch to represent the same phase position.

Define the equality fiber

\[
F_=
=
\left\{
((r,i),(s,i)):r\neq s
\right\}.
\tag{9}
\]

Its size is

\[
|F_=|=b(b-1)t.
\tag{10}
\]

Define the diagonal internal subgroup

\[
\Delta A
=
\{(\sigma,\ldots,\sigma):\sigma\in A\}
\leq A^b
\tag{11}
\]

and

\[
H=\Delta A\times S_b.
\tag{12}
\]

### Theorem 5.1 — Global coherence stabilizer

\[
\boxed{
\operatorname{Stab}_G(F_=)=H.
}
\tag{13}
\]

#### Proof

Every element of \(H\) preserves equality of internal coordinates, so \(H\leq\operatorname{Stab}_G(F_=)\).

Conversely, let

\[
g=(\sigma_1,\ldots,\sigma_b;\pi)
\]

stabilize \(F_=\). For every pair \(r\neq s\) and every \(i\in\Lambda\), the cell

\[
((r,i),(s,i))
\]

must be sent to another equality cell. Hence

\[
\sigma_r(i)=\sigma_s(i)
\]

for all \(i\), so \(\sigma_r=\sigma_s\). Thus all internal components are equal, while \(\pi\) is arbitrary. Therefore \(g\in\Delta A\times S_b\). ∎

### Theorem 5.2 — Exact global coherence support

For every transitive \(A\) of degree \(t\) and every \(b\ge2\),

\[
\boxed{
 m_G(H;S_\times)=b(b-1)t.
}
\tag{14}
\]

#### Proof

The upper bound is attained by \(F_=\).

For the lower bound, let \(F\subseteq S_\times\) have stabilizer exactly \(H\). By Proposition 3.1, \(F\) is \(H\)-invariant. Restrict to one ordered pair of distinct branches. Because the internal action is diagonal \(A\), the selected internal cells form a union of diagonal-\(A\) orbitals in \(\Lambda^2\).

Every nonempty diagonal-\(A\) orbital has size at least \(t\): its projection to the first coordinate is a nonempty \(A\)-invariant subset of \(\Lambda\), hence all of \(\Lambda\), and every first-coordinate fiber has the same positive cardinality.

If the internal relation were empty or all of \(\Lambda^2\), independent branchwise actions would survive, producing a stabilizer larger than \(H\). Therefore a nonempty proper diagonal-\(A\)-invariant relation is required and costs at least \(t\) internal cells for every ordered branch pair. There are \(b(b-1)\) such pairs. Thus

\[
|F|\ge b(b-1)t.
\]

Equality is attained by the diagonal relation (9). ∎

### Corollary 5.3 — Coherence state count

\[
[G:H]=|A|^{b-1}.
\tag{15}
\]

Hence the semantic coherence information is

\[
I_{\rm coh}=(b-1)\log_2|A|.
\tag{16}
\]

The support cost and semantic information are therefore distinct resources.

---

## 6. Arbitrary partition coherence

Fix a partition

\[
\mathcal P=\{B_1,\ldots,B_c\}
\tag{17}
\]

of the branch set, with

\[
|B_j|=n_j,
\qquad
\sum_{j=1}^c n_j=b.
\tag{18}
\]

For every integer \(d\ge1\), write

\[
m_d=|\{j:n_j=d\}|.
\tag{19}
\]

The branch-permutation stabilizer is

\[
K_{\mathcal P}
\cong
\prod_{d\ge1}(S_d\wr S_{m_d}).
\tag{20}
\]

Define

\[
A^{\mathcal P}
=
\{(\sigma_1,\ldots,\sigma_b)\in A^b:
\sigma_r=\sigma_s\text{ whenever }r,s\in B_j\text{ for some }j\}
\cong A^c
\tag{21}
\]

and

\[
H_{\mathcal P}=A^{\mathcal P}\rtimes K_{\mathcal P}.
\tag{22}
\]

The canonical coherence fiber is

\[
F_{\mathcal P}
=
\left\{
((r,i),(s,i)):
 r\neq s,
\ r,s\text{ lie in the same }\mathcal P\text{-block}
\right\}.
\tag{23}
\]

### Theorem 6.1 — Exact arbitrary-partition phase-coherence support

\[
\boxed{
 m_G(H_{\mathcal P};S_\times)
=t\sum_{j=1}^c n_j(n_j-1).
}
\tag{24}
\]

#### Proof

**Upper bound.** The fiber (23) has cardinality

\[
|F_{\mathcal P}|=t\sum_jn_j(n_j-1).
\]

Its branch-pair projection is the disjoint union of complete loopless directed cliques on the partition blocks, whose automorphism group is exactly \(K_{\mathcal P}\). Within each non-singleton block, preservation of internal equality forces all branchwise internal permutations to coincide. Thus

\[
\operatorname{Stab}_G(F_{\mathcal P})=H_{\mathcal P}.
\]

**Lower bound.** Let \(F\) have stabilizer exactly \(H_{\mathcal P}\). Fix a size class \(d\ge2\) with \(m_d>0\). By \(K_{\mathcal P}\)-invariance, the restriction of \(F\) to any ordered pair of distinct branches lying in a size-\(d\) block is determined by one diagonal-\(A\)-invariant relation

\[
R_d\subseteq\Lambda^2.
\]

For branches lying in different partition blocks, the internal phase group contains independent \(A\times A\). Since \(A\) is transitive, \(A\times A\) is transitive on \(\Lambda^2\), so every cross-block internal fiber of an \(H_{\mathcal P}\)-invariant set is either empty or full.

If \(R_d\) were empty or full, one could apply a nonidentity element of \(A\) to a single branch inside one size-\(d\) block and fix all other branches. This extra base-group element would preserve all selected cells, contradicting exact residual group \(H_{\mathcal P}\). Hence \(R_d\) is nonempty and proper.

Every nonempty diagonal-\(A\) orbital has size at least \(t\), so \(|R_d|\ge t\). There are

\[
m_dd(d-1)
\]

ordered branch pairs inside size-\(d\) blocks. Summing over disjoint size classes gives

\[
|F|
\ge
 t\sum_{d\ge2}m_dd(d-1)
=
 t\sum_jn_j(n_j-1).
\]

The canonical fiber attains the bound. ∎

### Corollary 6.2 — Equal-block ladder

If \(b=cn\) and \(\mathcal P\) has \(c\) blocks of common size \(n\), then

\[
\boxed{
 m_G(H_{c,n};S_\times)=b(n-1)t.
}
\tag{25}
\]

The endpoints are

\[
n=1:\quad m=0,
\]

and

\[
n=b:\quad m=b(b-1)t.
\]

Thus global coherence is the top endpoint of an exact linear support hierarchy.

### Corollary 6.3 — Symmetry index

\[
\boxed{
[G:H_{\mathcal P}]
=
|A|^{b-c}
\frac{b!}{\prod_{d\ge1}(d!)^{m_d}m_d!}.
}
\tag{26}
\]

---

## 7. Why complement recovery fails for phase coherence

A tempting compression idea is to encode all but one partition block and recover the final block as a set-theoretic complement. Theorem 6.1 shows why this fails for full phase coherence.

Recovering a block as a **subset of branch labels** does not collapse its independent internal action

\[
A^{n_j}
\]

to the required diagonal copy

\[
\Delta A.
\]

Hence

\[
\boxed{
\text{block membership recovery}
\not\Rightarrow
\text{internal phase recovery}.
}
\tag{27}
\]

The distinction is crucial for the next section.

---

## 8. Partition-only memory

Now keep the same branch partition but remove the phase-coupling requirement. The target subgroup becomes

\[
J_{\mathcal P}=A^b\rtimes K_{\mathcal P}.
\tag{28}
\]

All branchwise internal actions remain independent.

Let

\[
\Omega_b=\{(r,s):r\neq s\}
\tag{29}
\]

be the branch-level ordered-pair set.

### Lemma 8.1 — Full-fiber lemma

If \(F\subseteq S_\times\) is \(J_{\mathcal P}\)-invariant, then for each ordered branch pair \((r,s)\), the entire internal fiber

\[
\{((r,i),(s,j)):i,j\in\Lambda\}
\]

is either contained in \(F\) or disjoint from \(F\).

#### Proof

The independent factors \(A_r\times A_s\le A^b\) act transitively on \(\Lambda^2\). ∎

Therefore every partition-only support is the full lift of a branch-level relation

\[
R\subseteq\Omega_b.
\]

Define

\[
\widehat R
=
\{((r,i),(s,j)):(r,s)\in R,\ i,j\in\Lambda\}.
\tag{30}
\]

Then

\[
|\widehat R|=t^2|R|.
\tag{31}
\]

### Theorem 8.2 — Exact partition-only reduction

\[
\boxed{
\operatorname{Stab}_G(\widehat R)
=A^b\rtimes\operatorname{Aut}(R).
}
\tag{32}
\]

Hence, with

\[
d(\mathcal P)
=
\min\{|R|:R\subseteq\Omega_b,\ \operatorname{Aut}(R)=K_{\mathcal P}\},
\tag{33}
\]

we have

\[
\boxed{
 m_G(J_{\mathcal P};S_\times)=t^2d(\mathcal P).
}
\tag{34}
\]

#### Proof

The base group \(A^b\) preserves every full fiber. A branch permutation \(\pi\in S_b\) preserves \(\widehat R\) exactly when it preserves the branch relation \(R\). The formula follows, and Lemma 8.1 proves that every admissible partition-only support arises in this way. ∎

This is where genuine complement compression becomes possible.

---

## 9. Exact special families for partition-only memory

### Theorem 9.1 — Two unequal blocks

For a partition into blocks of sizes \(p>q\ge2\),

\[
\boxed{d(p,q)=q(q-1).}
\tag{35}
\]

For \(p>1=q\),

\[
\boxed{d(p,1)=p.}
\tag{36}
\]

For two equal blocks \(n,n\),

\[
\boxed{d(n,n)=2n(n-1).}
\tag{37}
\]

#### Proof

For \(p>q\), the \(S_p\times S_q\)-orbitals on ordered distinct pairs have weights

\[
p(p-1),\quad q(q-1),\quad pq,\quad pq.
\]

When \(q\ge2\), the smallest positive orbital is the complete directed clique on the smaller block, with weight \(q(q-1)\), and its automorphism group is exactly \(S_p\times S_q\). When \(q=1\), the smallest available orbital is a directed star of weight \(p\). For equal blocks, the partition stabilizer is \(S_n\wr S_2\); the within-block orbital has weight \(2n(n-1)\) and is smaller than the cross-block orbital of weight \(2n^2\). ∎

### Theorem 9.2 — One non-singleton block and a singleton class

For partition type \((n,1^m)\), \(n\ge2\), \(m\ge1\),

\[
\boxed{
 d(n,1^m)
=
\min\{n(n-1),\ nm,\ m(m-1)\text{ if }m\ge2\}.
}
\tag{38}
\]

#### Proof

The target branch group is \(S_n\times S_m\). Its nonzero orbitals are precisely the within-\(n\) class, within-singleton-union class, and the two directed cross-class orbitals. Each orbital alone distinguishes the two classes and has the target automorphism group. Hence the cheapest positive orbital is optimal. ∎

### Theorem 9.3 — Three distinct blocks

Let

\[
p>q>r\ge1.
\]

Then

\[
\boxed{d(p,q,r)=qr.}
\tag{39}
\]

#### Proof

The directed complete bipartite relation from the \(q\)-block to the \(r\)-block has \(qr\) arcs. Its tail class, head class, and isolated complement have sizes \(q,r,p\), which are pairwise distinct, so its automorphism group is exactly

\[
S_p\times S_q\times S_r.
\]

For the lower bound, any nonempty invariant relation is a union of partition-stabilizer orbitals. The available orbital weights are within-block terms \(n(n-1)\) and cross-block terms \(n_in_j\). Since \(p>q>r\), the smallest orbital that can distinguish three classes has weight at least \(qr\); a smaller within-\(r\) orbital, when nonempty, isolates only the \(r\)-block and leaves the complement with full symmetric mixing between the \(p\)- and \(q\)-blocks, producing a larger automorphism group than the target. Thus \(qr\) is exact. ∎

This is the simplest infinite family exhibiting complement recovery: the largest block need not appear in the support at all.

---

## 10. Orbital structure for arbitrary partition type

A \(K_{\mathcal P}\)-invariant relation on \(\Omega_b\) is a union of explicit orbitals.

For every size \(d\ge2\) with \(m_d>0\), let

\[
W_d
\]

be all ordered distinct pairs inside one size-\(d\) partition block. Its weight is

\[
w(W_d)=m_dd(d-1).
\tag{40}
\]

For \(m_d\ge2\), let

\[
E_d
\]

be all ordered pairs between two distinct size-\(d\) blocks. Its weight is

\[
w(E_d)=m_d(m_d-1)d^2.
\tag{41}
\]

For distinct sizes \(d\neq e\), let

\[
C_{d\to e}
\]

be all ordered pairs from a size-\(d\) block to a size-\(e\) block. Its weight is

\[
w(C_{d\to e})=m_dm_e de.
\tag{42}
\]

Let the set of all such orbitals be

\[
Q(\mathcal P)=\{O_1,\ldots,O_q\}.
\tag{43}
\]

A candidate relation is encoded by bits

\[
y_i\in\{0,1\},
\qquad
R(y)=\bigcup_{y_i=1}O_i.
\tag{44}
\]

---

## 11. The partition-overgroup dichotomy

The main recognition theorem depends on an elementary but decisive structural fact about overgroups of a set-partition stabilizer.

Let \(S\) denote the union of all singleton blocks of \(\mathcal P\).

A point transposition lies in \(K_{\mathcal P}\) exactly when its two points lie in the same non-singleton block or both lie in \(S\). All other point transpositions are called **forbidden cross-block transpositions**.

### Theorem 11.1 — Partition-overgroup dichotomy

Let

\[
K_{\mathcal P}\le L\le S_b.
\]

If \(L>K_{\mathcal P}\), then at least one of the following holds.

1. \(L\) contains a forbidden cross-block point transposition.
2. The singleton union \(S\) has the same cardinality as a non-singleton partition block, and \(L\) contains a permutation moving \(S\) onto such a block.

#### Proof

Take \(g\in L\setminus K_{\mathcal P}\) and a non-singleton partition block \(B\).

Because \(\operatorname{Sym}(B)\le K_{\mathcal P}\), all point transpositions inside \(B\) lie in \(K_{\mathcal P}\). Conjugation by \(g\) therefore puts all transpositions inside \(g(B)\) into \(L\).

If \(g(B)\) meets two partition blocks and at least one is non-singleton, then one of these transpositions crosses target blocks and is forbidden. Thus, if no forbidden transposition occurs, any block image failing to lie in one non-singleton block must lie inside the singleton union \(S\).

If \(g(B)\subsetneq S\), choose \(x\in g(B)\) and \(y\in S\setminus g(B)\). The transposition \((xy)\) belongs to \(K_{\mathcal P}\), because \(K_{\mathcal P}\) induces the full symmetric group on \(S\). Conjugating by \(g^{-1}\) yields a forbidden transposition between one point of \(B\) and one point outside \(B\), contradiction. Hence

\[
g(B)=S,
\]

forcing \(|B|=|S|\).

If instead \(g(B)\) lies inside a non-singleton partition block \(C\), then a proper inclusion \(g(B)\subsetneq C\) similarly yields a forbidden transposition after conjugation. Hence \(g(B)=C\), necessarily with \(|B|=|C|\).

Apply the same argument to \(g^{-1}\). If no block is exchanged with \(S\), then \(S\) is preserved setwise and all non-singleton blocks are permuted within equal-size classes. Arbitrary bijections inside blocks and arbitrary permutations of equal-size blocks already lie in \(K_{\mathcal P}\), so \(g\in K_{\mathcal P}\), contradiction. Therefore alternative 2 must occur if alternative 1 does not. ∎

### Lemma 11.2 — Macro-mover double coset

Assume \(s=|S|\ge2\) and that \(\mathcal P\) has at least one non-singleton block of size \(s\). Let

\[
\mathcal M=\{S,B_1,\ldots,B_{m_s}\}
\]

be the macro-set consisting of \(S\) and all non-singleton size-\(s\) blocks. Fix one permutation \(\tau\) that swaps \(S\) and \(B_1\) by a bijection and fixes the remaining partition blocks setwise.

Every macro-mover satisfying the no-forbidden-transposition alternative lies in

\[
\boxed{K_{\mathcal P}\tau K_{\mathcal P}.}
\tag{45}
\]

#### Proof

On \(\mathcal M\), the group \(K_{\mathcal P}\) induces the full stabilizer of the distinguished macro-point \(S\), namely \(S_{m_s}\le S_{m_s+1}\). A point stabilizer in a full symmetric group has two double cosets: the stabilizer itself and the set of permutations moving the distinguished point. Hence any macro-permutation moving \(S\) can be written as

\[
\bar k_1\bar\tau\bar k_2.
\]

Lift \(\bar k_1,\bar k_2\) to \(k_1,k_2\in K_{\mathcal P}\). After removing the macro action, the remaining permutation fixes every macro-block setwise up to block permutations already available in \(K_{\mathcal P}\). Since \(K_{\mathcal P}\) contains the full symmetric group inside each partition block and on \(S\), all remaining internal bijections are also absorbed into \(K_{\mathcal P}\). Therefore the original mover lies in \(K_{\mathcal P}\tau K_{\mathcal P}\). ∎

---

## 12. Exact recognition by forbidden symmetries

### Theorem 12.1 — Exact partition-stabilizer recognition

Let \(R\subseteq\Omega_b\) be \(K_{\mathcal P}\)-invariant. Then

\[
\boxed{
\operatorname{Aut}(R)=K_{\mathcal P}
}
\tag{46}
\]

if and only if:

1. no forbidden cross-block point transposition preserves \(R\); and
2. when a singleton macro-swap is size-compatible, one fixed canonical macro-swap \(\tau\) does not preserve \(R\).

#### Proof

The forward implication is immediate.

Conversely suppose the two tests hold but \(\operatorname{Aut}(R)>K_{\mathcal P}\). Apply Theorem 11.1 to

\[
L=\operatorname{Aut}(R).
\]

The first alternative contradicts test 1. Under the second alternative, \(L\) contains a macro-mover \(g\). By Lemma 11.2,

\[
g=k_1\tau k_2
\]

for some \(k_1,k_2\in K_{\mathcal P}\). Because \(K_{\mathcal P}\le\operatorname{Aut}(R)\), this implies \(\tau\in\operatorname{Aut}(R)\), contradicting test 2. ∎

This reduces exact automorphism recognition to a finite symmetry-separation problem.

---

## 13. Orbital XOR-Separation Program

For a forbidden permutation \(\pi\), define an orbital-comparison graph \(\Gamma_\pi\) on indices \(1,\ldots,q\). Join \(i\) and \(j\) if some ordered pair \(z\in O_i\) satisfies

\[
\pi z\in O_j,
\qquad i\neq j.
\tag{47}
\]

### Lemma 13.1

\[
\pi\in\operatorname{Aut}(R(y))
\iff
 y_i=y_j
\text{ for every }ij\in E(\Gamma_\pi).
\tag{48}
\]

#### Proof

Membership in \(R(y)\) is constant on each orbital. The permutation \(\pi\) preserves \(R(y)\) exactly when every cell and its image have the same membership bit, which is precisely equality across every orbital transition induced by \(\pi\). ∎

Therefore \(\pi\) is broken exactly when

\[
\bigvee_{ij\in E(\Gamma_\pi)}(y_i\oplus y_j)=1.
\tag{49}
\]

### Theorem 13.2 — Exact Orbital XOR-Separation Program

The branch-level minimum \(d(\mathcal P)\) is the optimum of

\[
\boxed{
\begin{aligned}
\text{minimize }&\sum_{i=1}^q |O_i|y_i,\\
\text{subject to }&
\bigvee_{ij\in E(\Gamma_\pi)}(y_i\oplus y_j)=1
\quad\text{for every representative forbidden }\pi,\\
&y_i\in\{0,1\}.
\end{aligned}
}
\tag{50}
\]

where the representative list consists of one forbidden transposition from every \(K_{\mathcal P}\)-conjugacy type plus, when applicable, one canonical singleton macro-swap.

#### Proof

Every \(K_{\mathcal P}\)-invariant relation is uniquely represented by an orbital bit vector. By Theorem 12.1, exact automorphism group is equivalent to breaking each representative forbidden symmetry. Lemma 13.1 translates each break condition to (49), while the objective is exactly the relation support size. ∎

---

## 14. Size of the compact exact program

Let

\[
D=\{d:m_d>0\},
\qquad
k=|D|.
\tag{51}
\]

The number of orbital variables is

\[
q
=
 k(k-1)
+|\{d\ge2:m_d>0\}|
+|\{d:m_d\ge2\}|,
\tag{52}
\]

hence

\[
q\le k^2+k.
\tag{53}
\]

The number of representative forbidden transposition types is at most

\[
\binom{k}{2}
+|\{d\ge2:m_d\ge2\}|,
\tag{54}
\]

plus at most one macro-swap.

Since distinct positive block sizes satisfy

\[
1+2+\cdots+k\le b,
\]

we have

\[
k=O(\sqrt b).
\tag{55}
\]

Thus arbitrary finite partition type admits an exact compact optimization depending primarily on the number of distinct block sizes.

The complexity classification of this special weighted OR-of-XOR program is left open. We make no NP-hardness claim.

---

## 15. Anonymous terminal values

The previous theorems describe named output fibers. If the two terminal outputs are anonymous, an automorphism may also exchange the two fibers.

For global coherence, the special fiber has size

\[
b(b-1)t,
\]

and its complement has size

\[
b(b-1)t(t-1).
\]

Equal cardinalities require \(t=2\). Actual exchange by a wreath element then occurs only for \(b=2\). Thus the seven-vertex binary coherence compiler is the unique anonymous-output anomaly in the global family.

For arbitrary partition coherence, let

\[
L=\sum_jn_j(n_j-1).
\]

Fiber equality requires

\[
2L=b(b-1)t.
\tag{56}
\]

Since \(L\le b(b-1)\), equality forces \(t=2\) and a single global partition block; the previous argument then forces \(b=2\).

Hence the unique anti-swap exception remains

\[
\boxed{b=2,\ t=2,\ \mathcal P=\{[2]\}.}
\tag{57}
\]

In that minimal binary case, one canonical fixed cell such as a root anchor changes fiber sizes from \(4+4\) to \(5+4\), giving the previously established exact nine-cell anonymous-output compiler.

---

## 16. Resource non-monotonicity

Partition+phase memory is semantically stronger than partition-only memory because

\[
H_{\mathcal P}\le J_{\mathcal P}.
\tag{58}
\]

Yet stronger symmetry reduction can be cheaper in support.

For two equal blocks of size \(n\ge2\), partition-only memory costs

\[
m_G(J_{\mathcal P};S_\times)=2n(n-1)t^2,
\tag{59}
\]

while partition+phase memory costs

\[
m_G(H_{\mathcal P};S_\times)=2n(n-1)t.
\tag{60}
\]

Therefore

\[
\boxed{
\frac{m_G(J_{\mathcal P};S_\times)}{m_G(H_{\mathcal P};S_\times)}=t.
}
\tag{61}
\]

The explanation is structural. Partition-only invariance contains independent \(A\times A\) on a branch pair and therefore forces a whole \(t^2\)-fiber. Phase coherence removes that independent symmetry and permits the thinner diagonal relation of size \(t\).

Thus support cost is not monotone under subgroup inclusion:

\[
\boxed{
H_1\le H_2
\not\Rightarrow
m_G(H_1;S)\ge m_G(H_2;S),
}
\tag{62}
\]

nor the reverse inequality in general.

---

## 17. Computational verification

The repository contains an exact solver implementing the witness-branch form of (50) and an independent verifier.

For every integer partition with total branch count

\[
2\le b\le7,
\]

all \(K_{\mathcal P}\)-invariant orbital unions were checked against direct enumeration of the full symmetric group \(S_b\). In every tested case,

\[
\boxed{
\text{recognition criterion says exact}
\iff
\operatorname{Aut}(R)=K_{\mathcal P}.
}
\tag{63}
\]

The computation is supporting verification, not a substitute for the proofs above.

Selected exact minima include

\[
\begin{array}{c|c}
\lambda & d(\lambda)\\
\hline
(2,1)&2\\
(3,2)&2\\
(3,3)&12\\
(3,2,1)&2\\
(2,2,1)&4\\
(4,2)&2\\
(4,3,2,1)&5.
\end{array}
\tag{64}
\]

---

## 18. Relation to classical literature

The closest classical lines are important and should delimit the claims.

### 18.1 Regular sets and setwise stabilizers

A subset with trivial setwise stabilizer is a classical regular set. Gluck studied trivial set-stabilizers in finite permutation groups, and recent work of Sabatini studies nontrivial set-stabilizers with controlled structure. The present quantity (1) contains the regular-set case \(H=1\), but prescribes an exact nontrivial subgroup and minimizes support on a fixed action.

### 18.2 Distinguishing number

Chan studied distinguishing numbers for direct and wreath product actions. Alikhani and Soltani introduced a subgroup-relative distinguishing number requiring the label-preserving group to lie inside a prescribed subgroup. Their resource is the number of labels and their target condition is containment, while here the resource is support weight and the target is exact equality.

### 18.3 Relation groups and 2-closure

Dalla Volta and Siemons, Grech and Kisielewicz, and the broader theory of relation groups study when a permutation group is the full automorphism group of a relation. The theory of 2-closure and orbital digraphs provides the natural language for binary relational representations. Our partition-only problem is a fixed-action, directed, loopless, weighted orbital-subselection problem inside this classical setting.

### 18.4 Point-determining graphs and twins

The forbidden-transposition criterion is a quotient-weighted analogue of classical point-determining or twin-free graph ideas. The novelty claim is not the concept of separating twins. What is specific here is the exact partition-stabilizer recognition theorem with the singleton macro-swap completion and the induced FCOA support optimization.

### 18.5 Minimum graphs with prescribed abstract automorphism group

There is also a literature minimizing graph size or edge count for a prescribed abstract automorphism group. Those problems usually allow the representation itself to vary. Here the concrete permutation action and carrier are fixed.

---

## 19. Discussion

Three structural lessons emerge.

First, **support cost and information cardinality are different resources**. A coherence state space can grow like \(|A|^{b-1}\) while the thin equality support grows only linearly in the branch degree \(t\) per ordered branch pair.

Second, **set recovery and phase recovery are distinct**. Complement compression is valid for partition-only memory but fails for full phase coherence because an unmarked block retains independent internal actions.

Third, **stronger memory may be cheaper**. The allowed invariant support geometry changes with the target subgroup. A stronger target can permit a thinner relation.

These effects are natural in FCOA because the resource being measured is not logical information alone but the geometry of a typed partial operation under a fixed automorphism action.

---

## 20. Open problems

The main finite correctness problem for partition-only memory is solved by the exact program (50). The next questions are secondary but mathematically natural.

1. Determine the computational complexity of the special Orbital XOR-Separation Program generated by partition-stabilizer orbitals.
2. Find closed formulas for broader infinite families of integer partitions.
3. Extend the support theory from pair relations to higher-arity FCOA value fibers.
4. Replace symmetric branch permutation \(S_b\) by restricted branch groups and determine how the overgroup dichotomy changes.
5. Study deeper iterated wreath products, where coherence constraints live at several tree levels simultaneously.

---

## 21. Conclusion

The FCOA branch-coherence problem leads to a concrete theory of prescribed residual symmetry on fixed pair actions.

For transitive branch action \(A\) of degree \(t\), global coherence has exact support

\[
\boxed{b(b-1)t.}
\]

For an arbitrary partition \(\mathcal P\), partition+phase coherence has exact support

\[
\boxed{t\sum_jn_j(n_j-1).}
\]

Partition-only memory reduces exactly to

\[
\boxed{t^2d(\mathcal P),}
\]

where \(d(\mathcal P)\) is the minimum branch-level directed support with automorphism group exactly \(K_{\mathcal P}\). The Partition-Overgroup Dichotomy and Macro-Mover Lemma reduce exact recognition to a finite list of forbidden transpositions plus at most one singleton macro-swap, yielding the exact Orbital XOR-Separation Program.

The resulting framework separates three resources that are often conflated:

\[
\boxed{
\text{output alphabet}
\quad\neq\quad
\text{support cost}
\quad\neq\quad
\text{semantic state count}.
}
\]

That separation is the central contribution of the present FCOA-Z continuation.

---

## References

1. A. Malachevsky, *Fixed-Carrier Oriented Algebra (FCOA): Definition, Typed Partial Operations, Carrier Erasure, and the Canonical M0 Baseline*, Zenodo, 2026. DOI: `10.5281/zenodo.22164246`.
2. A. Malachevsky, *Reflections on How a Ray Becomes an Axis: And why old operations reveal new local laws after a second direction appears*, Zenodo, 2026. DOI: `10.5281/zenodo.22171473`.
3. D. Gluck, *Trivial Set-Stabilizers in Finite Permutation Groups*, Canadian Journal of Mathematics 35 (1983), 59–67. DOI: `10.4153/CJM-1983-005-2`.
4. M. Chan, *The distinguishing number of the direct product and wreath product action*, Journal of Algebraic Combinatorics 24 (2006), 331–345. DOI: `10.1007/s10801-006-0006-7`.
5. S. Alikhani, S. Soltani, *The distinguishing number of groups based on the distinguishing number of subgroups*, Journal of Information and Optimization Sciences 43 (2022), 311–321. DOI: `10.1080/02522667.2021.2003011`; preprint arXiv:1701.00141.
6. F. Dalla Volta, J. Siemons, *Orbit equivalence and permutation groups defined by unordered relations*, Journal of Algebraic Combinatorics 35 (2012), 547–564. DOI: `10.1007/s10801-011-0313-5`.
7. M. Grech, A. Kisielewicz, *Orbit closed permutation groups, relation groups, and simple groups*, Journal of Algebraic Combinatorics 57 (2023). DOI: `10.1007/s10801-022-01214-2`.
8. M. W. Liebeck, C. E. Praeger, J. Saxl, *On the 2-Closures of Finite Permutation Groups*, Journal of the London Mathematical Society 37 (1988), 241–252. DOI: `10.1112/jlms/s2-37.2.241`.
9. D. P. Sumner, *Point determination in graphs*, Discrete Mathematics 5 (1973), 179–187. DOI: `10.1016/0012-365X(73)90109-X`.
10. R. C. Entringer, L. D. Gassman, *Line-critical point determining and point distinguishing graphs*, Discrete Mathematics 10 (1974), 43–55. DOI: `10.1016/0012-365X(74)90019-3`.
11. P. Hell, C. Hernández-Cruz, *Point determining digraphs, {0,1}-matrix partitions, and dualities in full homomorphisms*, Discrete Mathematics 338 (2015), 1755–1762. DOI: `10.1016/j.disc.2014.12.001`.
12. D. J. McCarthy, L. V. Quintas, *A stability theorem for minimum edge graphs with given abstract automorphism group*, Transactions of the American Mathematical Society 208 (1975), 27–39. DOI: `10.1090/S0002-9947-1975-0369148-4`.
13. L. Babai, A. J. Goodman, L. Lovász, *Graphs with Given Automorphism Group and Few Edge Orbits*, European Journal of Combinatorics 12 (1991), 185–203. DOI: `10.1016/S0195-6698(13)80085-6`.
14. L. Babai, A. J. Goodman, *Subdirectly Reducible Groups and Edge-Minimal Graphs with Given Automorphism Group*, Journal of the London Mathematical Society 47 (1993), 417–432. DOI: `10.1112/jlms/s2-47.3.417`.
15. D. Deligeorgaki, *Smallest graphs with given automorphism group*, Journal of Algebraic Combinatorics 56 (2022), 609–633. DOI: `10.1007/s10801-022-01125-2`.
16. L. Sabatini, *On stabilizers in finite permutation groups*, Bulletin of the London Mathematical Society, 2026. DOI: `10.1112/blms.70201`.
