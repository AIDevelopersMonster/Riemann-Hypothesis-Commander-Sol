# QGE3 LQR — Exact Four-Phase Theorem

**Branch:** `director/fcoa-rigidity-cost`  
**Problem:** determine `L_q(4)` for all alphabet sizes `q`.

## 1. Main theorem

### Theorem 1.1 — exact four-phase synchronization cost

For every `q>=2`,

\[
\boxed{
L_q(4)=
\begin{cases}
3, & q=2,\\
2q-1, & 3\le q\le5,\\
12, & q=6,\\
3q-7, & q\ge7.
\end{cases}
}
\]

The proof is completely combinatorial. Computation is used only as an independent hostile check.

---

## 2. Forest reduction and partition rank

For every source color `a`, replace the constraint graph `Gamma_a` by a spanning forest inside each of its connected components. This preserves the solution set.

For `r=4`, let `P_a` be the partition of `{0,1,2,3}` into connected components of `Gamma_a`, and put

\[
m_a=|E(\Gamma_a)|=4-|P_a|.
\]

Thus

\[
m_a\in\{0,1,2,3\}.
\]

By pair-union connectivity from `LQR_LOWER_BOUNDS.md`, every two distinct colors satisfy

\[
P_a\vee P_b=\mathbf 1,
\]

where `\mathbf 1` is the one-block partition. Equivalently, `Gamma_a\cup Gamma_b` is connected.

Call two partitions **compatible** when their join is the one-block partition.

---

## 3. Complete compatibility classification on four phase indices

### Lemma 3.1 — rank zero

The unique rank-zero partition is the discrete partition

\[
0|1|2|3.
\]

It is compatible only with the rank-three one-block partition.

### Proof

Joining the discrete partition with any partition leaves the latter unchanged. Hence the join is one block exactly when the other partition already has one block. \(\square\)

### Lemma 3.2 — rank one

Two rank-one partitions are never compatible.

### Proof

A rank-one partition is one pair plus two singletons. Its forest contains one edge. The union of two such forests contains at most two edges, while a connected graph on four vertices needs at least three. \(\square\)

### Lemma 3.3 — exactly four rank-two partners of a fixed rank-one partition

Fix a rank-one partition whose nontrivial block is `{u,v}`. Exactly four rank-two partitions are compatible with it.

### Proof

A rank-two partition has exactly two blocks. Adding the edge `{u,v}` makes the join one block iff `u` and `v` lie in different blocks of that rank-two partition. Once the block containing `u` and the block containing `v` are distinguished, each of the remaining two points may independently be assigned to either side. Hence there are exactly

\[
2^2=4
\]

compatible rank-two partitions. \(\square\)

### Lemma 3.4 — the seven rank-two partitions

There are exactly

\[
S(4,2)=7
\]

rank-two partitions. Any two distinct rank-two partitions are compatible. A rank-two partition is not compatible with itself.

### Proof

Rank two means exactly two blocks. If two distinct two-block partitions had a two-block join, that join would be a two-block partition coarser than each. A coarsening with the same number of blocks must equal the original partition, forcing the two partitions to coincide. Therefore the join of two distinct two-block partitions has one block.

The self-join is the same two-block partition, so it is not connected. \(\square\)

### Lemma 3.5 — rank three

The one-block partition is compatible with every partition and may occur for arbitrarily many colors.

This completes the compatibility classification relevant to the lower bound.

---

## 4. Lower bound for all q

Let `n_k` be the number of colors with `m_a=k`.

If `n_0>0`, Lemma 3.1 forces every other color to have rank three, so

\[
|S|\ge3(q-1).
\]

This is never smaller than the value claimed in Theorem 1.1 for `q>=3`.

Assume henceforth `n_0=0`. Then

\[
|S|=n_1+2n_2+3n_3
=3q-2n_1-n_2.
\]

By Lemma 3.2,

\[
n_1\le1.
\]

If `n_1=1`, Lemma 3.3 gives

\[
n_2\le4,
\]

and of course `n_2<=q-1`. Therefore

\[
2n_1+n_2\le 2+\min(4,q-1).
\]

If `n_1=0`, Lemma 3.4 gives

\[
n_2\le\min(7,q).
\]

Hence the maximum possible defect

\[
D:=2n_1+n_2
\]

is

\[
D_{\max}=
\begin{cases}
q+1,&3\le q\le5,\\
6,&q=6,\\
7,&q\ge7.
\end{cases}
\]

Indeed:

- for `3<=q<=5`, the rank-one option gives `D=q+1`, beating `D=q` from the all-rank-two option;
- for `q=6`, both options give at most `D=6`;
- for `q>=7`, the all-rank-two option gives `D=7`, while a rank-one color gives at most `D=6`.

Since `|S|=3q-D`, every synchronizing system satisfies

\[
L_q(4)\ge
\begin{cases}
2q-1,&3\le q\le5,\\
12,&q=6,\\
3q-7,&q\ge7.
\end{cases}
\]

For `q=2`, the previously proved binary theorem gives `L_2(4)=3`.

It remains to construct matching systems.

---

## 5. Matching gadgets for q=3,4,5

Use phase indices `{0,1,2,3}`.

Define the following component partitions, each realized by a spanning forest of the indicated rank:

\[
P_0=0|1|23 \qquad (m=1),
\]

\[
P_1=012|3,\qquad
P_2=013|2,\qquad
P_3=02|13,\qquad
P_4=03|12
\qquad (m=2).
\]

For `q=3`, use `P_0,P_1,P_2`; for `q=4`, add `P_3`; for `q=5`, add `P_4`.

The costs are respectively

\[
5,\qquad7,\qquad9.
\]

### Explicit constraints

A concrete forest realization is:

- color `0`: `(2,3)`;
- color `1`: `(0,1),(0,2)`;
- color `2`: `(0,1),(0,3)`;
- color `3`: `(0,2),(1,3)`;
- color `4`: `(0,3),(1,2)`.

Only the colors present for the chosen `q` are used.

### q=3

This has cost five and is already optimal by the exact theorem

\[
L_3(4)=5.
\]

### q=4 — direct proof

Normalize `pi_0=id` by global left composition.

The constraints imply:

\[
\pi_1(1)=\pi_1(2)=1,2,
\]

so `pi_1` fixes `1,2` and therefore either fixes or swaps `0,3`.

Likewise `pi_2` fixes `1,3`, so it either fixes or swaps `0,2`. Also

\[
\pi_2(0)=\pi_3(0),
\qquad
\pi_3(2)=2.
\]

If `pi_2` swapped `0,2`, then `pi_2(0)=2`, forcing `pi_3(0)=2`, impossible because `pi_3(2)=2` and `pi_3` is injective. Thus `pi_2=id`, so `pi_3(0)=0`.

The color-3 partition gives

\[
\pi_1(3)=\pi_3(3).
\]

If `pi_1` swapped `0,3`, then `pi_1(3)=0`, forcing `pi_3(3)=0`, impossible because `pi_3(0)=0`. Hence `pi_1=id`, so `pi_3(3)=3`.

Now `pi_3` fixes `0,2,3`, hence also `1`. Therefore all four phases are the identity after normalization. The system synchronizes, and

\[
L_4(4)=7.
\]

### q=5 — direct proof

Again normalize `pi_0=id`.

From colors `1,2,3,4`:

- `pi_1` fixes `1,2`, hence preserves `{0,3,4}`;
- `pi_2` fixes `1,3`, hence preserves `{0,2,4}`;
- `pi_3` fixes `2,4`, hence preserves `{0,1,3}`.

The color-0 constraint gives

\[
\pi_2(0)=\pi_3(0).
\]

The common value lies in

\[
\{0,2,4\}\cap\{0,1,3\}=\{0\},
\]

so both `pi_2` and `pi_3` fix `0`.

The color-3 constraint gives

\[
\pi_1(3)=\pi_3(3).
\]

The common value lies in `{0,3,4}\cap{0,1,3}={0,3}`. Since `pi_3(0)=0`, injectivity forces the common value to be `3`. Hence `pi_1,pi_3` fix `3`.

The color-4 constraint gives

\[
\pi_1(4)=\pi_2(4).
\]

The common value lies in `{0,3,4}\cap{0,2,4}={0,4}`. Since `pi_2(0)=0`, injectivity forces the common value to be `4`. Hence `pi_1,pi_2` fix `4`.

Now each of `pi_1,pi_2,pi_3` fixes four of the five colors and therefore is the identity. Thus

\[
L_5(4)=9.
\]

---

## 6. The exceptional q=6 value

Take the optimal `q=5` gadget above on colors `0,...,4` and make color `5` individually connected across all four phases, using a three-edge spanning tree.

The total cost is

\[
9+3=12.
\]

After normalizing `pi_0=id`, the connected color-5 graph forces every phase to fix color `5`. Hence all phases restrict to permutations of the remaining five colors, where the `q=5` gadget forces identity.

Therefore

\[
\boxed{L_6(4)=12.}
\]

---

## 7. Seven-cut gadget for q=7

The seven rank-two partitions of four phase indices admit a clean binary-vector parametrization.

Identify the seven source colors with

\[
V=\mathbb F_2^3\setminus\{0\}.
\]

For `v=(v_1,v_2,v_3) in V`, define a bipartition of the four phases by putting phase `0` on the zero side and phase `i` on the side `v_i`:

\[
B_v^0=\{0\}\cup\{i\in\{1,2,3\}:v_i=0\},
\]

\[
B_v^1=\{i\in\{1,2,3\}:v_i=1\}.
\]

Because `v!=0`, both blocks are nonempty. Connect each block by a spanning tree. The cost for color `v` is

\[
(|B_v^0|-1)+(|B_v^1|-1)=2.
\]

Using all seven nonzero vectors therefore costs

\[
14.
\]

### Lemma 7.1 — seven-cut synchronization

This 14-constraint system synchronizes four phases in `S_7`.

### Proof

Normalize `pi_0=id`.

For `i in {1,2,3}`, define

\[
H_i=\{v\in V:v_i=0\},
\qquad
A_i=\{v\in V:v_i=1\}.
\]

If `v_i=0`, phases `0` and `i` lie in the same block of the color-`v` partition, hence

\[
\pi_i(v)=\pi_0(v)=v.
\]

Thus `pi_i` fixes every element of `H_i` pointwise. Since `pi_i` is a permutation, it preserves the complementary four-set `A_i` setwise.

Now fix distinct `i,j in {1,2,3}`. For every

\[
v\in A_i\cap A_j,
\]

we have `v_i=v_j=1`, so phases `i,j` lie in the same block `B_v^1`. Therefore

\[
\pi_i(v)=\pi_j(v).
\]

The left side lies in `A_i` and the right side lies in `A_j`; hence the common value lies in `A_i\cap A_j`. Consequently `pi_i` preserves `A_i\cap A_j` setwise.

For fixed `i`, let `j,k` be the other two coordinates. On the four-set `A_i`, the two membership bits

\[
\mathbf 1_{A_i\cap A_j}(v),
\qquad
\mathbf 1_{A_i\cap A_k}(v)
\]

are exactly the coordinate pair `(v_j,v_k)`. The four elements of `A_i` have the four distinct patterns

\[
(0,0),(0,1),(1,0),(1,1).
\]

Since `pi_i` preserves both subsets `A_i\cap A_j` and `A_i\cap A_k`, it preserves both membership bits, hence fixes every element of `A_i` individually.

Thus `pi_i` fixes both `H_i` and `A_i`, so

\[
\pi_i=id.
\]

This holds for `i=1,2,3`. Therefore the tuple is diagonal before normalization and the seven-cut system synchronizes. \(\square\)

Hence

\[
\boxed{L_7(4)=14.}
\]

---

## 8. All q>=7

For every `q>7`, choose seven source colors and apply the seven-cut gadget. For each remaining source color, make its constraint graph connected on the four phase indices, at cost three.

After normalizing phase `0` to the identity, all extra connected colors are fixed pointwise by every phase. The remaining seven colors therefore carry an `S_7` action, which the seven-cut gadget kills by Lemma 7.1.

The total cost is

\[
14+3(q-7)=3q-7.
\]

Together with the lower bound,

\[
\boxed{L_q(4)=3q-7\qquad(q\ge7).}
\]

This completes the proof of Theorem 1.1. \(\square\)

---

## 9. Structural interpretation

The irregularity at `q=6` is now explained exactly.

- A rank-one color gives a defect saving of two relative to a connected color, but it can coexist with only four rank-two colors.
- Without a rank-one color, at most seven distinct rank-two colors can coexist.
- For `q<=5`, the `1+rank-two` architecture is optimal.
- At `q=6`, the best achievable defect is six in either architecture, producing the isolated value `12`.
- From `q=7` onward, the complete seven-cut family wins and every additional color costs exactly three constraints.

Thus the sequence

\[
5,7,9,12,14,17,20,\dots
\]

for `q=3,4,5,6,7,8,9,...` is not accidental finite behavior; it is the exact theorem-controlled four-phase column.

---

## 10. Scope and novelty firewall

The proof uses the already established classical necessary condition that every pair of canonical color classes in a uniquely colorable quotient must induce a connected subgraph; in LQR language this is pair-union connectivity.

What is new inside the present FCOA/LQR programme is the exact exploitation of the restricted four-phase partition geometry, including the seven-cut `F_2^3` gadget and the resulting exact formula for `L_q(4)`.

No broad claim is made about discovering unique colorability, Kempe connectivity, set partitions, or binary-vector cut systems themselves.
