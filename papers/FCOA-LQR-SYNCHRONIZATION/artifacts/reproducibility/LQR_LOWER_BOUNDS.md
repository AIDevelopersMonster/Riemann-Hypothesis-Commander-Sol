# QGE3 LQR — Lower Bounds

## 1. Pair-union connectivity

Let `S` be synchronizing and let `Gamma_a` be the constraint graph for source color `a`.

### Theorem 1.1
For every two distinct colors `a,b`,

\[
\boxed{\Gamma_a\cup\Gamma_b\text{ is connected}.}
\]

### Proof
If the union is disconnected, let `X` be a nonempty proper union of its connected components. No constraint of color `a` or `b` crosses the cut `(X,[r]\\X)`. Let `sigma=(a\ b)` and put `pi_i=sigma` on `X`, `pi_i=id` outside `X`. Every crossing constraint has a source color fixed by `sigma`, while internal constraints compare equal permutations. Thus all constraints hold but the tuple is non-diagonal, contradiction. \(\square\)

After replacing each `Gamma_a` by a spanning forest of each connected component, write `m_a=|E(Gamma_a)|`. Pair-union connectivity gives

\[
m_a+m_b\ge r-1
\]

for every pair `a!=b`. Summing yields the older half-density bound

\[
\boxed{L_q(r)\ge \left\lceil\frac{q(r-1)}2\right\rceil.}
\]

This remains useful in small alphabets, but the stronger Mersenne defect inequality below is now the main general lower-bound engine.

---

## 2. Exact lower bound for q=3

For three colors,

\[
m_0+m_1\ge r-1,
\quad
m_0+m_2\ge r-1,
\quad
m_1+m_2\ge r-1.
\]

Therefore

\[
2(m_0+m_1+m_2)\ge3(r-1),
\]

so

\[
\boxed{L_3(r)\ge\left\lceil\frac{3(r-1)}2\right\rceil.}
\]

`LQR_CONSTRUCTIONS.md` gives equality.

---

## 3. Exact lower bounds for r=2 and r=3

For `r=2`, if two colors carried no edge, their union would be disconnected. Hence at least `q-1` colors contribute one edge and

\[
\boxed{L_q(2)\ge q-1.}
\]

For `r=3`, after forest reduction each `m_a in {0,1,2}`. If some `m_a=0`, all others must equal two. Otherwise, at most three colors can have `m_a=1`, because there are only three one-edge forests and two identical one-edge partitions are not pair-union connected. Thus

\[
\boxed{L_q(3)\ge2q-3.}
\]

Again the constructions are exact.

---

## 4. Universal cut-space dictionary

Let `P_a` be the partition of the `r` phase indices into connected components of `Gamma_a`, and let

\[
c_a=|P_a|.
\]

Since `Gamma_a` is a forest,

\[
m_a=r-c_a.
\]

Define the defect

\[
d_a=(r-1)-m_a=c_a-1.
\]

Hence

\[
\boxed{|S|=(r-1)q-\sum_a d_a.}
\]

Distinguish phase `0` and identify normalized binary cuts of the phase set with

\[
V=\mathbb F_2^{r-1}.
\]

For a partition `P`, define

\[
W(P)=\{x\in V:x\text{ is constant on every block of }P\}.
\]

If `P` has `c` blocks, then

\[
\boxed{\dim W(P)=c-1.}
\]

Moreover

\[
\boxed{W(P)\cap W(Q)=W(P\vee Q).}
\]

Therefore pair-union connectivity

\[
P_a\vee P_b=\mathbf 1
\]

is equivalent to

\[
\boxed{W(P_a)\cap W(P_b)=\{0\}.}
\]

This converts every synchronizing family into a family of pairwise trivially intersecting binary subspaces.

The full proof is recorded in `LQR_STABILIZATION_THEOREM.md`.

---

## 5. Mersenne defect inequality

A binary `d`-dimensional subspace has exactly `2^d-1` nonzero vectors. Since the nonzero parts of the spaces `W(P_a)` are pairwise disjoint inside `F_2^{r-1}`, every synchronizing system satisfies

\[
\boxed{
\sum_a(2^{d_a}-1)
\le
2^{r-1}-1.
}
\]

This is strictly stronger than merely summing pairwise rank inequalities.

Since

\[
d\le2^d-1
\qquad(d\ge0),
\]

we obtain the universal defect cap

\[
\boxed{
\sum_a d_a\le2^{r-1}-1.
}
\]

Substitution into the defect identity gives the new global lower bound

\[
\boxed{
L_q(r)
\ge
(r-1)q-(2^{r-1}-1).
}
\]

For small `q` this may be weaker than the half-density bound, but for fixed `r` and large `q` it is the decisive estimate.

---

## 6. Equality structure

Equality in

\[
\sum_a d_a\le2^{r-1}-1
\]

forces equality termwise in

\[
d_a\le2^{d_a}-1.
\]

Thus every positive defect must satisfy

\[
\boxed{d_a=1.}
\]

Hence an extremal family at the universal defect cap consists only of one-dimensional cut spaces, one for each nonzero binary vector. There are exactly

\[
2^{r-1}-1
\]

such vectors.

Therefore equality in the global lower bound is impossible when

\[
q<2^{r-1}-1.
\]

Combined with `LQR_BINARY_CUT_GADGET.md`, this proves the exact stabilization theorem

\[
\boxed{
L_q(r)=(r-1)q-(2^{r-1}-1)
\quad\text{iff in the large-alphabet regime }q\ge2^{r-1}-1.
}
\]

More precisely, the formula holds for every `q>=2^{r-1}-1`, and the same lower bound is strict below that threshold.

---

## 7. Finite-q packing interface

The stronger inequality suggests a finite optimization layer.

Define

\[
\mathcal D_r(q)
=
\max\left\{\sum_i \dim W_i:
W_i\le\mathbb F_2^{r-1},
\ W_i\cap W_j=\{0\}\ (i\ne j),
\text{ and each }W_i=W(P_i)\text{ for a partition }P_i
\right\}.
\]

Then

\[
\boxed{
L_q(r)\ge(r-1)q-\mathcal D_r(q).
}
\]

The ambient finite-geometry relaxation is a mixed-dimension partial-spread problem. The FCOA/LQR problem may be stricter because not every pairwise-compatible partition family is automatically a synchronizing system.

For `r<=4`, the previously constructed optimal gadgets show that the relevant defect optima are realizable.

---

## 8. Relation to classical mathematics

The pair-union condition is the LQR specialization of the classical fact that every two color classes of a uniquely colorable graph induce a connected subgraph.

The cut-space reduction meets classical finite geometry: pairwise trivially intersecting subspaces are partial-spread / vector-space-partition objects. No novelty is claimed for those notions themselves.

The FCOA-specific theorem is the canonical route from point-image synchronization constraints to partition defects, then to cut-space packing, and from there to the exact large-alphabet threshold.
