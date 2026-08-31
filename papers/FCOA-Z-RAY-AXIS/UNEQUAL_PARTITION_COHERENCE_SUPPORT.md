# FCOA-Z — Exact Prescribed Support for Unequal Partition Coherence

Status: theorem package v0.1  
Date: 2026-08-31

This note continues `PARTITION_DIAGONAL_SUPPORT_HIERARCHY.md` and corrects the earlier working expectation that an unequal partition might permit support compression by leaving one coherence block implicit as a complement.

For the full target subgroup that remembers **both** the branch partition and one common internal `A`-phase inside each partition block, that compression does not occur.

The exact minimum remains the obvious within-block equality support:

\[
\boxed{
m_G(H_{\mathcal P};S_\times)=t\sum_{B\in\mathcal P}|B|(|B|-1).}
\]

The reason is structural: recovering a block as a set does not force the independent internal branch actions on that block to collapse to one diagonal `A`-action. That phase coupling must be witnessed by an internal-sensitive same-block relation for every non-singleton block-size class.

---

## 1. FCOA framework

The ambient framework is FCOA Definition 1.0:

A. Malachevsky, *Fixed-Carrier Oriented Algebra (FCOA): Definition, Typed Partial Operations, Carrier Erasure, and the Canonical M0 Baseline*, Zenodo, 2026, DOI `10.5281/zenodo.22164246`.

Let

\[
A\le\operatorname{Sym}(\Lambda)
\]

be transitive of degree

\[
|\Lambda|=t\ge2.
\]

Let the branch set be

\[
B=[b].
\]

The active imprimitive carrier is

\[
X=B\times\Lambda,
\]

with ambient group

\[
G=A\wr S_b=A^b\rtimes S_b.
\]

The operation-cell universe studied here is the ordered cross-branch set

\[
S_\times
=
\{((r,i),(s,j)):r\neq s\}.
\]

---

## 2. Arbitrary branch partition

Fix a set partition

\[
\mathcal P=\{B_1,\ldots,B_c\}
\]

of `B`, with block sizes

\[
|B_j|=n_j,
\qquad
n_1+\cdots+n_c=b.
\]

For each integer `d>=1`, let

\[
m_d=|\{j:n_j=d\}|
\]

be the multiplicity of block size `d`.

The branch-permutation stabilizer of the partition is

\[
K_{\mathcal P}
\cong
\prod_{d\ge1}\left(S_d\wr S_{m_d}\right),
\]

with factors of multiplicity zero omitted.

Define the internal phase subgroup

\[
A^{\mathcal P}
=
\{(\sigma_1,\ldots,\sigma_b)\in A^b:
\sigma_r=\sigma_s\text{ whenever }r,s\in B_j\text{ for some }j\}
\cong A^c.
\]

The target residual symmetry is

\[
\boxed{
H_{\mathcal P}
=A^{\mathcal P}\rtimes K_{\mathcal P}.
}
\]

Singleton blocks cause no internal restriction: on a one-element block, the diagonal copy of `A` is just the original independent `A` factor.

---

## 3. Canonical unequal-partition coherence fiber

Define

\[
F_{\mathcal P}
=
\left\{
((r,i),(s,i)):
 r\neq s,
\ r,s\text{ lie in the same }\mathcal P\text{-block}
\right\}.
\]

Its size is

\[
\boxed{
|F_{\mathcal P}|
=t\sum_{j=1}^c n_j(n_j-1)
=t\sum_{d\ge2}m_d d(d-1).
}
\]

This is the direct unequal-block analogue of the equal-block support from the preceding theorem package.

---

## 4. Exact stabilizer

### Theorem 4.1 — Unequal-Partition Coherence Stabilizer

\[
\boxed{
\operatorname{Stab}_G(F_{\mathcal P})=H_{\mathcal P}.
}
\]

#### Proof

Every element of `H_P` preserves the set partition and uses one common internal permutation on each block, so it preserves equality of internal coordinates inside every block. Hence

\[
H_{\mathcal P}\le\operatorname{Stab}_G(F_{\mathcal P}).
\]

Conversely let

\[
g=(\sigma_1,\ldots,\sigma_b;\pi)\in G
\]

stabilize `F_P`.

Projecting `F_P` to ordered branch pairs gives

\[
R_{\mathcal P}
=
\{(r,s):r\neq s,\ r,s\text{ are in the same }\mathcal P\text{-block}\}.
\]

This is the disjoint union of complete loopless directed cliques on the partition blocks. Its setwise stabilizer in `S_b` is exactly the automorphism group of the set partition:

\[
\operatorname{Stab}_{S_b}(R_{\mathcal P})=K_{\mathcal P}.
\]

Therefore

\[
\pi\in K_{\mathcal P}.
\]

Now let `r,s` be two distinct branches in the same non-singleton block. For every `i in Lambda`, the cell

\[
((r,i),(s,i))
\]

belongs to `F_P`, and its image must again be an equality cell. Hence

\[
\sigma_r(i)=\sigma_s(i)
\]

for every `i`, so

\[
\sigma_r=\sigma_s.
\]

Thus the internal tuple is constant on each non-singleton partition block. On singleton blocks there is no further condition, exactly as required by `A^P`. Therefore

\[
g\in A^{\mathcal P}\rtimes K_{\mathcal P}=H_{\mathcal P}.
\]

□

---

## 5. Structure of `H_P`-invariant subsets

Let

\[
F\subseteq S_\times
\]

satisfy

\[
H_{\mathcal P}\le\operatorname{Stab}_G(F).
\]

Fix a block size `d>=2` with `m_d>0`.

Because `K_P` is transitive on ordered pairs of distinct branches lying in blocks of size `d`, the restriction of `F` to those branch pairs is determined by one diagonal-`A`-invariant relation

\[
R_d\subseteq\Lambda^2.
\]

More precisely, for every ordered pair `(r,s)` of distinct branches in any size-`d` block,

\[
((r,i),(s,j))\in F
\quad\Longleftrightarrow\quad
(i,j)\in R_d.
\]

For branches lying in **different** `P`-blocks, the internal phases are independent. Therefore the corresponding internal action contains `A x A`, which is transitive on `Lambda^2` because `A` is transitive. Hence on every cross-block branch-pair orbit, an `H_P`-invariant subset is either empty on the whole internal `Lambda^2` fiber or contains the whole fiber.

Thus cross-block support cannot impose any relative internal phase equation between two branches of the same target block.

---

## 6. Phase-Coupling Necessity Lemma

### Lemma 6.1

Let `d>=2` with `m_d>0`. If

\[
\operatorname{Stab}_G(F)=H_{\mathcal P},
\]

then the same-block internal relation `R_d` is neither empty nor all of `Lambda^2`.

#### Proof

Suppose first

\[
R_d=\varnothing.
\]

Choose one branch `r` inside one size-`d` partition block and choose a nonidentity

\[
\alpha\in A.
\]

Apply `alpha` only to the internal coordinate of branch `r` and fix every other branch coordinate and every branch label.

This permutation lies in the ambient base group `A^b` but not in `A^P`, because the internal actions are no longer constant on the chosen block.

It nevertheless preserves `F`:

- on same-block size-`d` cells there are no selected cells;
- on cells between different partition blocks, every selected internal fiber is either empty or all of `Lambda^2`, hence is preserved by an independent action on one coordinate;
- all other size classes are untouched.

Thus the stabilizer is strictly larger than `H_P`, contradiction.

The same argument applies when

\[
R_d=\Lambda^2,
\]

because a full internal fiber is also invariant under independent branchwise `A` actions.

Hence `R_d` must be a nonempty proper diagonal-`A`-invariant relation. □

This is the obstruction to complement compression.

---

## 7. Minimum size of an internal-sensitive relation

The diagonal action of a transitive permutation group `A` on `Lambda^2` decomposes into orbitals.

Every nonempty orbital has size at least `t`.

### Lemma 7.1 — Orbital Lower Bound

If `O` is a nonempty orbit of diagonal `A` on `Lambda^2`, then

\[
|O|\ge t.
\]

#### Proof

The projection of `O` to the first coordinate is `A`-invariant and nonempty, hence is all of `Lambda`. Every first-coordinate fiber has the same positive size by transitivity. Therefore

\[
|O|=tq
\]

for some integer `q>=1`. □

The diagonal orbital

\[
\Delta_\Lambda=\{(i,i):i\in\Lambda\}
\]

has exactly size `t`, so the bound is sharp.

### Corollary 7.2

Every nonempty proper diagonal-`A`-invariant relation has size at least `t`.

---

## 8. Exact unequal-partition support theorem

### Theorem 8.1 — Exact Unequal-Partition Coherence Support

For every transitive `A` of degree `t>=2` and every partition

\[
\mathcal P=\{B_1,\ldots,B_c\}
\]

of `b` branches,

\[
\boxed{
m_G(H_{\mathcal P};S_\times)
=t\sum_{j=1}^c n_j(n_j-1).}
\]

Equivalently,

\[
\boxed{
m_G(H_{\mathcal P};S_\times)
=t\sum_{d\ge2}m_d d(d-1).}
\]

#### Proof

**Upper bound.** The canonical fiber `F_P` has exactly this size and Theorem 4.1 gives

\[
\operatorname{Stab}_G(F_P)=H_P.
\]

**Lower bound.** Let `F` have stabilizer exactly `H_P`. For every size class `d>=2`, Lemma 6.1 forces its same-block internal relation `R_d` to be nonempty and proper. By Corollary 7.2,

\[
|R_d|\ge t.
\]

There are

\[
m_d d(d-1)
\]

ordered branch pairs inside size-`d` blocks. Therefore the contribution of that size class to `F` is at least

\[
m_d d(d-1)t.
\]

Different size classes lie in disjoint cell sets, so these lower bounds add:

\[
|F|
\ge
 t\sum_{d\ge2}m_d d(d-1).
\]

This matches the canonical construction. □

---

## 9. The complement-recovery barrier

The preceding theorem disproves the earlier working guess that one non-singleton block might be omitted from the value support if its vertex set is recoverable as the complement of all explicitly marked blocks.

### Proposition 9.1 — Set Recovery Does Not Imply Phase Recovery

Let `B_0` be a non-singleton partition block. Even if the set `B_0` is definable from the remaining branch partition data, omitting every internal-sensitive same-block cell on `B_0` leaves an independent `A^{|B_0|}` action on its branches rather than the desired diagonal `A` action.

Hence recovering the **carrier subset** `B_0` does not recover its **coherence phase**.

Symbolically,

\[
\boxed{
\text{block membership recovery}
\not\Rightarrow
\text{internal phase coupling}.
}
\]

This is exactly why support compression by complement fails for the present target subgroup.

---

## 10. Exact symmetry index

The ambient group has size

\[
|G|=|A|^b b!.
\]

The internal target subgroup has size

\[
|A^{\mathcal P}|=|A|^c.
\]

The branch-partition stabilizer has size

\[
|K_{\mathcal P}|
=
\prod_{d\ge1}(d!)^{m_d}m_d!.
\]

Therefore

\[
\boxed{
[G:H_{\mathcal P}]
=
|A|^{b-c}
\frac{b!}{\prod_{d\ge1}(d!)^{m_d}m_d!}.
}
\]

The semantic information of the residual-symmetry choice is

\[
\boxed{
I_{\mathcal P}
=(b-c)\log_2|A|
+
\log_2\frac{b!}{\prod_d(d!)^{m_d}m_d!}.
}
\]

The first term measures phase identifications; the second counts set partitions of the declared block-size type.

---

## 11. Support density

The full ordered cross-branch domain has size

\[
|S_\times|=b(b-1)t^2.
\]

Hence the exact optimal support density is

\[
\boxed{
\frac{m_G(H_{\mathcal P};S_\times)}{|S_\times|}
=
\frac{\sum_j n_j(n_j-1)}{b(b-1)t}.
}
\]

This recovers the equal-block formula when all `n_j=n`:

\[
\frac{n-1}{(b-1)t}.
\]

---

## 12. Anonymous terminal outputs

Color `F_P` by one terminal value and its complement inside `S_x` by a second terminal value.

A necessary condition for a carrier automorphism to exchange the two anonymous output fibers is equality of fiber cardinalities:

\[
2|F_P|=|S_x|.
\]

Let

\[
L=\sum_j n_j(n_j-1).
\]

Then equality becomes

\[
2L=b(b-1)t.
\]

But

\[
L\le b(b-1),
\]

with equality iff the partition has one block of size `b`.

Since `t>=2`, fiber equality therefore forces

\[
t=2
\]

and one global partition block.

The global-coherence theorem already showed that an actual output-fiber exchange in this remaining case is possible only for

\[
b=2.
\]

### Corollary 12.1 — Unique Anonymous-Output Anomaly

For the entire unequal-partition coherence family, the only anonymous two-output case requiring an external anti-swap anchor remains

\[
\boxed{b=2,\quad t=2,\quad\mathcal P=\{B\},\ |B|=2.}
\]

This is exactly the seven-vertex binary branch-coherence compiler studied earlier.

---

## 13. Verification on small symmetric examples

Independent exhaustive checks for `A=S_2` reproduce the theorem on the following partition types:

\[
(2,1),\quad(3,1),\quad(2,2),\quad(3,2),\quad(2,1,1),\quad(3,1,1),\quad(4,1),\quad(2,2,1).
\]

In each tested case the exact minimum equals

\[
2\sum_j n_j(n_j-1).
\]

These checks are supporting verification only; the theorem is proved abstractly above and does not depend on enumeration.

---

## 14. Relation to nearby permutation-group theory

The prescribed-stabilizer problem is adjacent to several classical themes:

- regular sets and regular orbits in power-set actions;
- relation groups, where a permutation group is represented as the full automorphism group of a relation;
- distinguishing numbers and subgroup-relative distinguishing;
- set-stabilizers with controlled group-theoretic properties.

The current theorem differs in fixing a declared ambient `G`-set `S_x`, prescribing the **exact** residual subgroup `H_P`, and minimizing support cardinality.

A recent stabilizer paper emphasizes that setwise stabilizers and regular subsets are established objects in finite permutation-group theory, while relation-group work studies which groups can arise as automorphism groups of relations. The FCOA contribution here is the exact wreath-partition support formula and its interpretation as value-memory cost. No broad priority claim is made for the abstract notion `m_G(H;S)` without a dedicated literature audit.

---

## 15. Corrected frontier

The unequal-partition problem for **partition + phase coherence** is now solved exactly.

The initially anticipated complement compression does not occur:

\[
\boxed{
\text{full coherence target}
\Longrightarrow
m=t\sum_j n_j(n_j-1).
}
\]

However, complement compression can genuinely appear after removing the internal phase requirement.

Define the weaker partition-only target

\[
J_{\mathcal P}=A^b\rtimes K_{\mathcal P}.
\]

Here the operation only has to remember the branch partition, while every branch retains its independent internal `A` action.

For this weaker target, the internal-sensitive lower bound disappears and one may encode the partition through much sparser block-incidence relations. For example, a partition of type `(q,1)` can be recovered from a directed star using only `q` branch-level arcs rather than the `q(q-1)` arcs of a clique on the large block.

Therefore the next genuine compression problem is

\[
\boxed{
 m_G(J_{\mathcal P};S_\times),
}
\]

not the already solved full-coherence quantity `m_G(H_P;S_x)`.

This cleanly separates two resources:

\[
\boxed{
\text{partition memory}
\quad\text{vs}\quad
\text{phase-coherence memory}.
}
\]
