# FCOA-Z — Exact Partition-Only Support for Three Distinct Blocks

Status: theorem package v0.1  
Date: 2026-08-31

This note sharpens `PARTITION_ONLY_SUPPORT_COMPRESSION.md` for the first genuinely unequal multi-block family.

Let a branch partition have exactly three blocks of pairwise distinct sizes

\[
p>q>r\ge1.
\]

Then the minimum branch-level directed relation support is

\[
\boxed{d(p,q,r)=qr,}
\]

and therefore the minimum FCOA partition-only support is

\[
\boxed{m_G(J_{(p,q,r)};S_\times)=t^2qr.}
\]

The largest block is completely implicit: it is recovered as the isolated complement of a single directed complete bipartite relation between the two smaller blocks.

---

## 1. Setup

Let `A<=Sym(Lambda)` be transitive of degree `t>=2`, and let

\[
G=A\wr S_b,
\qquad b=p+q+r.
\]

For three distinct partition blocks `P,Q,R` of sizes `p,q,r`, the partition-only residual group is

\[
J=A^b\rtimes(S_p\times S_q\times S_r).
\]

By the Partition-Only Reduction Theorem,

\[
m_G(J;S_\times)=t^2 d(p,q,r),
\]

where `d(p,q,r)` is the minimum number of arcs in a loopless directed relation on the `b` branch labels whose automorphism group is exactly

\[
S_p\times S_q\times S_r.
\]

---

## 2. Construction

Take the directed complete bipartite relation

\[
C_{Q\to R}=Q\times R.
\]

It has exactly

\[
|C_{Q\to R}|=qr
\]

arcs.

Its branch vertices fall into three intrinsically distinct classes:

- vertices of `Q` have positive out-degree and zero in-degree;
- vertices of `R` have positive in-degree and zero out-degree;
- vertices of `P` are isolated.

Therefore every automorphism preserves `P,Q,R` setwise, while arbitrary permutations inside each class are allowed. Hence

\[
\operatorname{Aut}(C_{Q\to R})
=S_p\times S_q\times S_r.
\]

Thus

\[
d(p,q,r)\le qr.
\]

---

## 3. Orbital lower bound

The target branch group

\[
K=S_p\times S_q\times S_r
\]

has the following orbitals on ordered distinct pairs:

### Within-block orbitals

\[
W_P,\quad W_Q,\quad W_R
\]

of respective sizes

\[
p(p-1),\quad q(q-1),\quad r(r-1),
\]

with `W_R` empty when `r=1`.

### Cross-block orbitals

For each ordered pair of distinct blocks there is one complete directed bipartite orbital. Their sizes are

\[
pq,\quad pr,\quad qr,
\]

in each of the two orientations.

Since

\[
p>q>r,
\]

the smallest cross-block orbital has size exactly

\[
qr.
\]

Suppose a `K`-invariant relation `F` has

\[
|F|<qr.
\]

Then `F` contains no cross-block orbital. Hence it is a union only of within-block orbitals.

To have automorphism group exactly `K`, at least two of the three blocks must be marked by nonempty within-block orbitals. If only one block is marked, the vertices in the other two blocks are all isolated and may be permuted together, producing a strictly larger symmetric group on their union.

For `r>=2`, the two cheapest nonempty within-block orbitals have total size

\[
r(r-1)+q(q-1).
\]

Because `q>r`,

\[
r(r-1)+q(q-1)\ge qr.
\]

Indeed, writing `q=r+s` with `s>=1`, the difference is

\[
r(r-1)+q(q-1)-qr
=(q-r)(q-1)+r(r-2)\ge0.
\]

For `r=1`, `W_R` is empty, so two marked blocks require at least `W_Q` together with `W_P`; this cost is strictly larger than

\[
q=qr.
\]

Therefore no exact relation has fewer than `qr` arcs.

Combining with the construction gives the theorem.

---

## 4. Theorem

### Theorem 4.1 — Three-Distinct-Block Minimum

For every

\[
p>q>r\ge1,
\]

\[
\boxed{d(p,q,r)=qr.}
\]

Consequently, for every transitive internal branch action `A` of degree `t`,

\[
\boxed{m_G(J_{(p,q,r)};S_\times)=t^2qr.}
\]

□

---

## 5. Exact complement compression

The naive same-block clique encoding would use

\[
p(p-1)+q(q-1)+r(r-1)
\]

branch-level arcs.

The optimum uses only

\[
qr.
\]

arcs.

Thus the compression ratio is

\[
\boxed{
\frac{p(p-1)+q(q-1)+r(r-1)}{qr}.
}
\]

For fixed `q,r`, this ratio grows quadratically with `p`.

The large block carries no explicit support at all. Its membership is reconstructed as

\[
P=B\setminus(Q\cup R),
\]

where `Q` and `R` are distinguished by out-degree versus in-degree in the single cross relation.

This is genuine complement recovery.

---

## 6. Comparison with full phase coherence

For the stronger partition+phase target, the exact support is

\[
m_{\rm coh}
=t\,[p(p-1)+q(q-1)+r(r-1)].
\]

For partition-only memory,

\[
m_{\rm part}=t^2qr.
\]

Neither quantity uniformly dominates the other.

Their ratio is

\[
\boxed{
\frac{m_{\rm part}}{m_{\rm coh}}
=
\frac{tqr}{p(p-1)+q(q-1)+r(r-1)}.
}
\]

Thus there are parameter regimes where weaker partition-only memory is cheaper, and regimes where the stronger phase-coherent representation is cheaper because it exploits a sparse internal diagonal.

This strengthens the resource non-monotonicity phenomenon identified in the preceding note.

---

## 7. Next barrier: four or more distinct size classes

For three distinct blocks one directed cross orbital is enough because its source, target, and isolated complement provide exactly three branch signatures.

For four or more distinct block sizes, one cross orbital leaves at least two untouched classes with identical empty incidence, causing them to merge into one larger symmetric class.

Therefore the problem becomes a **signature separation problem**.

At branch-size-class level, each selected orbital contributes an in/out incidence bit. The selected orbitals must give distinct structural signatures to every unmerged class, while their weights are products of class sizes for cross orbitals and `n(n-1)` for within-class clique orbitals.

A naive star need not work: if several leaf classes have identical incidence to the same center, their vertices become one larger twin class.

Hence the next general invariant is a weighted directed twin-separation problem on the distinct block-size classes.

This is the first place where the arbitrary-partition support problem no longer collapses to one orbital or one obvious complement argument.
