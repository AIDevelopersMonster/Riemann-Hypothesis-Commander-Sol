# FCOA-Z — Partition-Only Support Compression

Status: theorem package v0.1  
Date: 2026-08-31

This note follows `UNEQUAL_PARTITION_COHERENCE_SUPPORT.md`.

The full partition+phase target

\[
H_{\mathcal P}=A^{\mathcal P}\rtimes K_{\mathcal P}
\]

has exact support

\[
t\sum_j n_j(n_j-1),
\]

and does **not** admit complement compression, because every non-singleton block must still have its independent internal `A` actions collapsed to a diagonal `A`.

Here we remove that phase requirement and retain only the branch partition. The target becomes

\[
\boxed{J_{\mathcal P}=A^b\rtimes K_{\mathcal P}.}
\]

Now complement compression is real. The problem reduces exactly to a sparse directed-relation realization of the partition stabilizer on the branch labels.

---

## 1. Setup

Let

\[
A\le\operatorname{Sym}(\Lambda)
\]

be transitive of degree

\[
|\Lambda|=t\ge2,
\]

and let

\[
G=A\wr S_b=A^b\rtimes S_b
\]

act on

\[
X=[b]\times\Lambda.
\]

Fix a branch partition

\[
\mathcal P=\{B_1,\ldots,B_c\}
\]

with block sizes `n_j` and multiplicities

\[
m_d=|\{j:n_j=d\}|.
\]

Its branch-permutation stabilizer is

\[
K_{\mathcal P}
\cong
\prod_{d\ge1}(S_d\wr S_{m_d}).
\]

The partition-only residual group is

\[
\boxed{J_{\mathcal P}=A^b\rtimes K_{\mathcal P}.}
\]

The FCOA cell universe is the ordered cross-branch set

\[
S_\times
=
\{((r,i),(s,j)):r\neq s\}.
\]

Let

\[
\Omega_b=\{(r,s):r\neq s\}
\]

be the corresponding branch-level ordered-pair set.

---

## 2. Full-Fiber Lemma

### Lemma 2.1

If

\[
J_{\mathcal P}\le\operatorname{Stab}_G(F)
\]

for a subset

\[
F\subseteq S_\times,
\]

then for each ordered branch pair `(r,s)` either

\[
\{((r,i),(s,j)):i,j\in\Lambda\}\subseteq F
\]

or that whole `t^2`-fiber is disjoint from `F`.

#### Proof

The base subgroup `A^b` is contained in `J_P`. For fixed distinct branches `r,s`, the independent factors `A_r x A_s` act transitively on

\[
\Lambda\times\Lambda
\]

because `A` is transitive on each coordinate. Therefore an invariant subset of that fiber is either empty or the whole fiber. □

Thus every partition-only support is the full lift of a branch-level relation.

---

## 3. Exact branch-level reduction

For

\[
R\subseteq\Omega_b,
\]

define its full FCOA lift

\[
\widehat R
=
\{((r,i),(s,j)):(r,s)\in R,\ i,j\in\Lambda\}.
\]

Then

\[
|\widehat R|=t^2|R|.
\]

### Theorem 3.1 — Partition-Only Reduction Theorem

\[
\boxed{
\operatorname{Stab}_G(\widehat R)
=A^b\rtimes\operatorname{Aut}(R),
}
\]

where `Aut(R)` is the setwise stabilizer of the directed relation `R` in `S_b`.

Consequently, if

\[
d(\mathcal P)
=
\min\{|R|:R\subseteq\Omega_b,\ \operatorname{Aut}(R)=K_{\mathcal P}\},
\]

then

\[
\boxed{
m_G(J_{\mathcal P};S_\times)=t^2 d(\mathcal P).}
\]

#### Proof

Every element of `A^b` preserves each full internal fiber. A branch permutation `pi in S_b` preserves `\widehat R` exactly when it preserves the set of branch pairs `R`. Hence the stabilizer is the stated semidirect product.

By Lemma 2.1 every `J_P`-invariant support is some full lift `\widehat R`. Exact stabilizer `J_P` is therefore equivalent to `Aut(R)=K_P`, and support size is multiplied by `t^2`. □

This is the main structural simplification: the partition-only FCOA problem is exactly a sparse loopless digraph automorphism problem on the branch set.

---

## 4. Orbital Boolean reduction

Every candidate relation with automorphism group containing `K_P` is a union of `K_P`-orbits on `Omega_b`.

These orbitals are completely determined by block-size classes.

### 4.1 Within-block orbital

For every `d>=2` with `m_d>0`, let

\[
W_d
\]

be all ordered distinct vertex pairs lying in the same size-`d` partition block.

Its weight is

\[
\boxed{w(W_d)=m_d d(d-1).}
\]

### 4.2 Between unequal size classes

For distinct sizes `d,e`, let

\[
C_{d\to e}
\]

contain all ordered pairs from a size-`d` block to a size-`e` block.

Its weight is

\[
\boxed{w(C_{d\to e})=m_d m_e de.}
\]

The reverse direction is a distinct orbital.

### 4.3 Between distinct equal-size blocks

For `m_d>=2`, let

\[
C_{d\leftrightarrow d}
\]

contain all ordered pairs whose endpoints lie in two distinct size-`d` blocks.

Its weight is

\[
\boxed{w(C_{d\leftrightarrow d})=m_d(m_d-1)d^2.}
\]

Therefore `d(P)` is an exact finite 0/1 optimization over these orbitals: select a minimum-weight union whose full automorphism group is exactly `K_P`.

The number of orbitals depends on the number of distinct block sizes, not quadratically on `b`.

---

## 5. Complement compression is genuine

The full-coherence support encoded each non-singleton block internally by a complete equality matching across its ordered branch pairs. Partition-only support can instead mark only enough branch-level structure to identify the desired block system.

### Example 5.1 — Type `(q,1)`

Let one block have size `q>=2` and the remaining block be one singleton.

The directed star from the singleton to every point of the `q`-block has exactly

\[
q
\]

arcs and automorphism group

\[
S_q.
\]

Hence

\[
\boxed{d(q,1)=q,}
\]

whereas the same-block clique would cost

\[
q(q-1).
\]

Thus the compression factor is `q-1`.

---

## 6. Exact two-block theorem

Let the partition have exactly two blocks of sizes

\[
p\ge q\ge1.
\]

### Theorem 6.1 — Two-Block Minimum

If

\[
p>q\ge2,
\]

then

\[
\boxed{d(p,q)=q(q-1).}
\]

If

\[
p>q=1,
\]

then

\[
\boxed{d(p,1)=p.}
\]

If

\[
p=q=n\ge2,
\]

then

\[
\boxed{d(n,n)=2n(n-1).}
\]

#### Proof

For unequal blocks `p>q`, the `K=S_p x S_q` orbitals on ordered distinct pairs have sizes

\[
p(p-1),\quad q(q-1),\quad pq,\quad pq.
\]

Any nonempty `K`-invariant relation is a union of these orbitals. For `q>=2`, the smallest positive orbital is `W_q` of size `q(q-1)`, and `W_q` alone is the complete directed clique on the smaller block with the larger block isolated. Its automorphism group is exactly `S_q x S_p`. Hence the minimum is exact.

For `q=1`, the within-singleton orbital is empty. The smallest nonempty orbitals are the two directed complete bipartite stars of size `p`, either of which has automorphism group `S_p`, so `d(p,1)=p`.

For equal blocks `n,n`, the partition stabilizer is `S_n wr S_2`. There are two orbitals: within-block pairs, of size `2n(n-1)`, and cross-block pairs, of size `2n^2`. The within-block orbital alone has exactly the required wreath automorphism group and is smaller. □

### FCOA consequence

Multiply all formulas by `t^2`:

\[
\boxed{m_G(J_{(p,q)};S_\times)=t^2 d(p,q).}
\]

---

## 7. One non-singleton block plus singleton family

Consider partition type

\[
(n,1^m),
\qquad n\ge2,\ m\ge1.
\]

The target branch group is

\[
K\cong S_n\times S_m,
\]

because the `m` singleton blocks may be permuted arbitrarily.

There are three natural cheapest ways to distinguish the two vertex classes:

1. clique on the `n`-block: cost `n(n-1)`;
2. clique on the `m` singleton vertices, when `m>=2`: cost `m(m-1)`;
3. one directed complete bipartite relation between the two classes: cost `nm`.

### Theorem 7.1

Let

\[
\mu(n,m)
=
\min\Bigl(
 n(n-1),\ nm,\ m(m-1)\text{ if }m\ge2
\Bigr).
\]

Then

\[
\boxed{d(n,1^m)=\mu(n,m).}
\]

#### Proof

The group `S_n x S_m` has exactly the corresponding within-class and directed between-class orbitals, with the displayed weights. Every invariant relation is their union, so any nonempty exact relation has weight at least the minimum positive orbital weight. Each of the three candidate orbitals by itself distinguishes the two classes and has automorphism group exactly `S_n x S_m`. Therefore the minimum positive orbital is exact. □

Examples:

\[
d(3,1,1)=2,
\]

\[
d(2,1,1,1)=2,
\]

\[
d(q,1)=q.
\]

---

## 8. Strong compression examples

The following exact branch-level minima were independently checked by exhaustive orbital search:

\[
\begin{array}{c|c}
\lambda & d(\lambda)\\
\hline
(2,1) & 2\\
(3,1) & 3\\
(4,1) & 4\\
(2,2) & 4\\
(3,2) & 2\\
(3,3) & 12\\
(2,1,1) & 2\\
(3,1,1) & 2\\
(2,2,1) & 4\\
(3,2,1) & 2\\
(2,2,2) & 6\\
(4,2) & 2
\end{array}
\]

The striking cases

\[
d(3,2)=d(4,2)=2
\]

show that a tiny marked 2-block can define a much larger complementary block at no additional support cost.

Likewise `d(3,2,1)=2`: a two-arc orbital can identify two of the size classes and the remaining class is forced as the complement.

---

## 9. Memory-strength inversion

Partition-only memory is semantically weaker than partition+phase coherence:

\[
J_{\mathcal P}=A^b\rtimes K_{\mathcal P}
\supseteq
H_{\mathcal P}=A^{\mathcal P}\rtimes K_{\mathcal P}.
\]

Nevertheless it can cost **more FCOA cells**.

For two equal blocks of size `n>=2`,

### Partition only

\[
m_G(J;S_\times)
=
2n(n-1)t^2.
\]

### Partition + phase

\[
m_G(H;S_\times)
=
2n(n-1)t.
\]

Hence

\[
\boxed{
\frac{m_G(J;S_\times)}{m_G(H;S_\times)}=t.
}
\]

The stronger memory is `t` times cheaper in support.

This is not contradictory. Partition-only invariance contains independent `A x A` on each branch pair and therefore forces a selected branch pair to carry the whole `Lambda^2` fiber. Phase coherence removes that independent symmetry and permits the much thinner diagonal relation of size `t`.

Thus resource cost is not monotone under subgroup inclusion when the allowed support must itself be invariant under the target subgroup.

This gives a new FCOA principle:

\[
\boxed{
H_1\le H_2
\not\Rightarrow
m_G(H_1;S)\ge m_G(H_2;S)
\text{ or vice versa.}
}
\]

Exact symmetry reduction and support sparsity are partially independent resources.

---

## 10. Relation to classical permutation-group work

The branch-level quantity

\[
d(\mathcal P)
\]

asks for the minimum number of arcs in a loopless directed relation whose automorphism group is exactly the set-partition stabilizer `K_P`.

This is adjacent to the classical theory of relation groups and regular sets. Dalla Volta and Siemons study permutation groups representable as automorphism groups of relations, while later work on orbit-closed and relation groups emphasizes the connection between power-set orbits, regular sets, and invariant relations.

The present FCOA problem fixes a very specific imprimitive target group and minimizes **directed pair support** on a prescribed pair action. No broad novelty claim is made for the abstract minimization problem before a dedicated literature audit.

Useful literature boundary:

- F. Dalla Volta, J. Siemons, *Orbit equivalence and permutation groups defined by unordered relations*, Journal of Algebraic Combinatorics 35 (2012), DOI `10.1007/s10801-011-0313-5`.
- M. Grech, A. Kisielewicz, *Orbit closed permutation groups, relation groups, and simple groups*, Journal of Algebraic Combinatorics 57 (2023).

---

## 11. Current frontier

The partition-only problem has now been reduced exactly from FCOA cells to branch-level directed relation support:

\[
\boxed{
m_G(J_{\mathcal P};S_\times)=t^2 d(\mathcal P).}
\]

Closed formulas are established for:

- all two-block partition types;
- one non-singleton block plus any number of singleton blocks;
- several small mixed types by exact enumeration.

The remaining genuine problem is the branch-level extremal invariant

\[
\boxed{
d(\lambda)=\min\{|R|:\operatorname{Aut}(R)=K_\lambda\}}
\]

for arbitrary integer partition type `lambda`.

Because every candidate is a union of explicitly known `K_lambda` orbitals, this is now a finite weighted orbital-selection problem. The next strike should determine whether `d(lambda)` admits a closed formula in terms of a minimum-cost separating graph on the **block-size classes**, with complement recovery represented explicitly rather than handled case by case.
