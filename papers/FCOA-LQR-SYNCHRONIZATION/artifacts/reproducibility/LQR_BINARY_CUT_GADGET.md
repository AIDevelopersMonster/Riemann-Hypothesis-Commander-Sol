# QGE3 LQR — Universal Binary-Cut Synchronization Gadget

**Branch:** `director/fcoa-rigidity-cost`  
**Purpose:** generalize the four-phase seven-cut construction to arbitrary phase number.

## 1. Construction

Fix `r>=2` phase indices

\[
0,1,\dots,r-1.
\]

Let

\[
V=\mathbb F_2^{r-1}\setminus\{0\}.
\]

Use one source color for every `v=(v_1,\dots,v_{r-1}) in V`. Hence

\[
q_0=|V|=2^{r-1}-1.
\]

For color `v`, define the bipartition

\[
B_v^0=\{0\}\cup\{i\in\{1,\dots,r-1\}:v_i=0\},
\]

\[
B_v^1=\{i\in\{1,\dots,r-1\}:v_i=1\}.
\]

Because `v!=0`, both blocks are nonempty. Inside each block choose an arbitrary spanning tree and impose the corresponding point-image constraints of source color `v`.

The number of constraints contributed by color `v` is

\[
(|B_v^0|-1)+(|B_v^1|-1)=r-2.
\]

Therefore the whole gadget has cost

\[
\boxed{(r-2)(2^{r-1}-1).}
\]

---

## 2. Synchronization theorem

### Theorem 2.1 — binary-cut gadget

For every `r>=2`, the construction above synchronizes the `r` phases in

\[
S_{2^{r-1}-1}.
\]

Equivalently,

\[
\boxed{
L_{2^{r-1}-1}(r)
\le
(r-2)(2^{r-1}-1).
}
\]

### Proof

Let the phases be

\[
\pi_0,\pi_1,\dots,\pi_{r-1}.
\]

Global left composition preserves all point-image constraints, so normalize

\[
\pi_0=id.
\]

Fix `i in {1,...,r-1}` and define

\[
H_i=\{v\in V:v_i=0\},
\qquad
A_i=\{v\in V:v_i=1\}.
\]

If `v in H_i`, then phases `0` and `i` lie in the same block `B_v^0`. Since that block is connected by the color-`v` constraint tree,

\[
\pi_i(v)=\pi_0(v)=v.
\]

Thus `pi_i` fixes every color in `H_i` pointwise. Because `pi_i` is a permutation of `V`, it preserves the complementary set `A_i` setwise.

Now fix `j!=i`. If

\[
v\in A_i\cap A_j,
\]

then `v_i=v_j=1`, so phases `i` and `j` lie in the same block `B_v^1`. Hence

\[
\pi_i(v)=\pi_j(v).
\]

The left side belongs to `A_i`, because `pi_i` preserves `A_i`; the right side belongs to `A_j`, because `pi_j` preserves `A_j`. Therefore

\[
\pi_i(v)\in A_i\cap A_j.
\]

So `pi_i` preserves each subset

\[
A_i\cap A_j
\qquad(j!=i)
\]

setwise.

For a fixed `i`, every color `v in A_i` is uniquely determined by the membership vector

\[
\bigl(\mathbf 1_{A_i\cap A_j}(v)\bigr)_{j\ne i,\ 1\le j\le r-1}.
\]

Indeed these bits are exactly the remaining coordinates

\[
(v_j)_{j\ne i}.
\]

Since `pi_i` preserves every set `A_i\cap A_j`, it preserves all these membership bits. Therefore it fixes every element of `A_i` individually.

We already know that it fixes every element of `H_i`. Hence

\[
\pi_i=id.
\]

This holds for every `i=1,...,r-1`. Together with the normalization `pi_0=id`, all phases are equal. Thus the gadget synchronizes. \(\square\)

---

## 3. Large-alphabet corollary

### Corollary 3.1

For every `r>=2` and every

\[
q\ge2^{r-1}-1,
\]

\[
\boxed{
L_q(r)
\le
(r-1)q-(2^{r-1}-1).
}
\]

### Proof

Choose `q_0=2^{r-1}-1` source colors and apply Theorem 2.1. For each of the remaining `q-q_0` colors, make its constraint graph connected on all `r` phase indices using a spanning tree of `r-1` constraints.

After normalizing one phase to the identity, every extra connected color is fixed pointwise by every phase. Hence every phase preserves the `q_0` active colors setwise, and the binary-cut gadget forces identity on that active set.

The total cost is

\[
(r-2)q_0+(r-1)(q-q_0)
=(r-1)q-q_0,
\]

so

\[
L_q(r)\le(r-1)q-(2^{r-1}-1).
\]
\(\square\)

---

## 4. Unification of solved columns

The construction specializes exactly to already discovered optimal large-`q` formulas:

### r=2

\[
q_0=1,
\qquad
L_q(2)\le q-1,
\]

which is exact.

### r=3

\[
q_0=3,
\qquad
L_q(3)\le2q-3,
\]

which is exact for every `q>=3`.

### r=4

\[
q_0=7,
\qquad
L_q(4)\le3q-7,
\]

which `LQR_R4_THEOREM.md` proves exact for every `q>=7`.

Thus the formulas

\[
q-1,
\qquad
2q-3,
\qquad
3q-7
\]

are the first three instances of one general binary-cut law

\[
\boxed{
(r-1)q-(2^{r-1}-1).
}
\]

The open issue is whether this upper bound becomes exact for every fixed `r` once `q` is sufficiently large.

---

## 5. New asymptotic target

Define the large-alphabet defect

\[
C_r(q)=(r-1)q-L_q(r).
\]

The binary-cut theorem proves

\[
C_r(q)\ge2^{r-1}-1
\]

for every

\[
q\ge2^{r-1}-1.
\]

For `r=2,3,4`, the known exact formulas show eventual equality:

\[
C_2=1,
\qquad
C_3=3,
\qquad
C_4=7.
\]

This motivates the precise next conjectural target:

\[
\boxed{
L_q(r)=(r-1)q-(2^{r-1}-1)
\quad\text{for all sufficiently large }q.
}
\]

No general lower bound proving this is claimed here.

---

## 6. Partition-lattice interpretation

Each active color in the gadget uses a two-block partition of the phase set. Once phase `0` is distinguished, nontrivial bipartitions are in bijection with nonzero binary vectors of length `r-1`; hence there are exactly

\[
2^{r-1}-1
\]

of them.

Distinct two-block partitions have one-block join, so the entire family automatically satisfies the necessary pair-union connectivity condition.

The theorem shows more: the full family is not merely pairwise compatible; it is genuinely synchronizing. This upgrades a partition-lattice packing into an exact phase-recovery mechanism.

---

## 7. Scope firewall

1. This is an abstract full-support phase theorem for `L_q(r)`.
2. It does not define or bound a real-cell multicolor `alpha_q`.
3. The binary-vector parametrization is a proof device; no arithmetic structure is imposed on FCOA carrier labels.
4. No novelty claim is made for finite-vector spaces or cut families themselves. The programme-specific contribution is their use as a universal point-image synchronization gadget.
