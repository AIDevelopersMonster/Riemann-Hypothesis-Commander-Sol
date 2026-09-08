# FCOA-Z — Partition-Diagonal Prescribed-Support Hierarchy

Status: theorem package v0.1  
Date: 2026-08-31

This note continues `PRESCRIBED_STABILIZER_SUPPORT_TRANSITIVE.md`.

The global coherence target

\[
\Delta A\times S_b
\]

forces one common internal phase across all `b` branches. The present note interpolates between that target and the full wreath product by requiring common phase only inside blocks of branches.

The result is an exact support hierarchy.

---

## 1. Equal-block partition

Let `A<=Sym(Lambda)` be transitive of degree

\[
|\Lambda|=t\ge2.
\]

Let

\[
b=cn
\]

with `c>=1`, `n>=1`.

Partition the `b` branches into `c` unlabeled blocks

\[
\mathcal P=\{B_1,\ldots,B_c\}
\]

of equal size

\[
|B_j|=n.
\]

The ambient group is

\[
G=A\wr S_b=A^b\rtimes S_b.
\]

The branch-permutation stabilizer of the equal-block partition is

\[
K_{c,n}=S_n\wr S_c=(S_n)^c\rtimes S_c.
\]

The desired internal phase group consists of tuples constant on each partition block:

\[
A^{\mathcal P}
=
\{(\sigma_1,\ldots,\sigma_b):
\sigma_r=\sigma_s\text{ whenever }r,s\in B_j\text{ for some }j\}
\cong A^c.
\]

Define the target subgroup

\[
\boxed{
H_{c,n}=A^{\mathcal P}\rtimes K_{c,n}.
}
\]

This gives the endpoint checks:

- `n=1`, `c=b`: `H_{b,1}=G`;
- `c=1`, `n=b`: `H_{1,b}=Delta A x S_b`.

---

## 2. Partition-coherence fiber

On the ordered cross-branch cell set

\[
S_\times=\{((r,i),(s,j)):r\neq s\}
\]

define

\[
F_{\mathcal P}
=
\left\{
((r,i),(s,i)):
 r\neq s,\ r,s\text{ lie in the same block of }\mathcal P
\right\}.
\]

This stores two pieces simultaneously:

1. which branches belong to the same coherence block;
2. equality of their internal phase coordinates.

Its size is

\[
\boxed{
|F_{\mathcal P}|=c\,n(n-1)t=b(n-1)t.
}
\]

For `n=1`, the fiber is empty.

---

## 3. Exact stabilizer

### Theorem 3.1 — Partition-Coherence Stabilizer

\[
\boxed{
\operatorname{Stab}_G(F_{\mathcal P})=H_{c,n}.
}
\]

#### Proof

Every element of `H_{c,n}` preserves the partition and applies one common internal permutation to every branch in each block, so it preserves `F_P`.

Conversely let

\[
g=(\sigma_1,\ldots,\sigma_b;\pi)\in G
\]

stabilize `F_P`.

The projection of `F_P` to ordered branch pairs is exactly

\[
R_{\mathcal P}
=
\{(r,s):r\neq s,\ r,s\text{ are in the same }\mathcal P\text{-block}\}.
\]

Hence `pi` must stabilize this relation. For an equal-block partition this setwise stabilizer is precisely

\[
K_{c,n}=S_n\wr S_c.
\]

Now fix two distinct branches `r,s` in the same block. For every `i in Lambda`, the equality cell

\[
((r,i),(s,i))
\]

must be sent to another equality cell inside one target block. Therefore

\[
\sigma_r(i)=\sigma_s(i)
\]

for every `i`, so

\[
\sigma_r=\sigma_s.
\]

Thus the internal tuple is constant on each partition block, i.e. lies in `A^P`. Hence `g in H_{c,n}`. □

---

## 4. H-orbit structure and minimum

Assume first `n>=2`.

Under `H_{c,n}`, the fiber `F_P` is a single orbit:

- `K_{c,n}` is transitive on ordered distinct branch pairs lying in a common partition block;
- diagonal `A` inside that block is transitive on the equality coordinate `i`.

Therefore

\[
|F_P|=b(n-1)t
\]

is one `H`-orbit.

We compare it with all other `H`-orbits on `S_x`.

### Same-block, non-equality orbitals

Any nonempty diagonal-`A` orbital in `Lambda^2` has size at least `t`. Hence every same-block `H`-orbit has size at least

\[
b(n-1)t.
\]

### Different-block cells

For branches in distinct partition blocks, the internal phases are independent. Therefore `A x A` acts transitively on `Lambda^2` because `A` is transitive on each coordinate.

`K_{c,n}` is transitive on ordered pairs of distinct partition blocks and on the branch choices inside them. Hence all different-block cells form one orbit of size

\[
c(c-1)n^2t^2.
\]

For `c>=2`, `n>=2`, `t>=2`,

\[
c(c-1)n^2t^2>b(n-1)t.
\]

Indeed, after substituting `b=cn`, the ratio is

\[
\frac{(c-1)nt}{n-1}>1.
\]

Thus `F_P` is a minimum-size nonempty `H`-orbit.

### Theorem 4.1 — Exact Partition-Diagonal Support

For `n>=2`,

\[
\boxed{
m_G(H_{c,n};S_\times)=b(n-1)t.}
\]

For `n=1`, `H_{b,1}=G` and

\[
\boxed{m_G(G;S_\times)=0}
\]

via the empty subset.

#### Proof

Any subset with stabilizer exactly `H_{c,n}` is `H_{c,n}`-invariant, hence a union of `H_{c,n}`-orbits. If `H_{c,n}<G`, it is nonempty, so its size is at least the minimum nonempty orbit size `b(n-1)t`. The fiber `F_P` has exactly this size and Theorem 3.1 shows that its stabilizer is exactly `H_{c,n}`. □

---

## 5. Exact symmetry index

The ambient group has size

\[
|G|=|A|^b b!.
\]

The target subgroup has size

\[
|H_{c,n}|=|A|^c (n!)^c c!.
\]

Hence

\[
\boxed{
[G:H_{c,n}]
=
|A|^{b-c}
\frac{b!}{(n!)^c c!}.
}
\]

The two factors have separate meanings:

\[
|A|^{b-c}
\]

counts the relative phase identifications imposed inside the `c` blocks, while

\[
\frac{b!}{(n!)^c c!}
\]

counts the number of equal-block partitions of the `b` branches.

Therefore the semantic information carried by the choice of partition-coherence state is

\[
\boxed{
I_{c,n}
=(b-c)\log_2|A|
+
\log_2\frac{b!}{(n!)^c c!}.
}
\]

---

## 6. Exact support ladder

For fixed ambient `b,t,A`, restrict to equal block sizes `n` dividing `b` and put

\[
c=b/n.
\]

Then

\[
\boxed{
m(n)=b(n-1)t.}
\]

Thus support grows linearly with coherence-block size:

\[
0,\ bt,\ 2bt,\ \ldots,\ b(b-1)t
\]

at the admissible divisors/intermediate block sizes.

The endpoints are:

### No cross-branch coherence

`n=1`:

\[
H=G,
\qquad
m=0.
\]

### Global coherence

`n=b`:

\[
H=\Delta A\times S_b,
\qquad
m=b(b-1)t.
\]

Hence the previously solved global coherence support is the top endpoint of an exact partition-coherence hierarchy.

---

## 7. Natural-domain fraction

The full connection-independent cross domain has size

\[
|S_x|=b(b-1)t^2.
\]

Therefore the optimal special-fiber density is

\[
\boxed{
\frac{m_G(H_{c,n};S_x)}{|S_x|}
=
\frac{n-1}{(b-1)t}.
}
\]

This separates two sparsity effects:

- increasing branch width `t` makes the value support sparser;
- decreasing coherence block size `n` makes the residual symmetry larger and the support cheaper.

---

## 8. Anonymous-output issue

With one terminal output there is no value-induced reduction on a fixed domain, so two outputs remain necessary whenever `H_{c,n}<G`.

With two named outputs, use `F_P` and its complement in the natural cross domain.

For anonymous outputs, a complete exchange of the two fibers requires equal cardinalities:

\[
b(n-1)t
=
b[(b-1)t^2-(n-1)t].
\]

Equivalently,

\[
2(n-1)=(b-1)t.
\]

If `c>=2`, then `b=cn>=2n`, so

\[
(b-1)t\ge2(2n-1)>2(n-1),
\]

and equality is impossible.

Thus every proper multi-block partition (`c>=2`, `n>=2`) automatically has unequal fiber sizes and no anonymous-output swap.

For `c=1`, this reduces to the global-coherence case. Equality of sizes forces `t=2`; the earlier theorem then shows actual fiber exchange occurs only when additionally `b=2`.

### Corollary 8.1

The unique anonymous-output anchor anomaly in the equal-block partition hierarchy is again

\[
\boxed{b=2,\ n=2,\ c=1,\ t=2.}
\]

All other nontrivial equal-block partition-coherence compilers need no extra anti-swap anchor.

---

## 9. Relation to the one-bit binary compiler

For

\[
A=S_2,
\quad
b=2,
\quad
n=2,
\quad
c=1,
\quad
t=2,
\]

we recover

\[
G\cong D_8,
\qquad
H\cong V_4,
\]

and

\[
m=2(1)2=4.
\]

The natural cross domain has size `8`; because this is the unique anonymous-output anomaly, one root anchor is required, giving total defined support `9` in the FCOA implementation.

---

## 10. New resource comparison

The support cost

\[
m=b(n-1)t
\]

and semantic information

\[
I_{c,n}
=(b-c)\log_2|A|
+
\log_2\frac{b!}{(n!)^c c!}
\]

are not proportional.

The support records an orbit-level equality relation, while the information count includes both internal phase identifications and the combinatorial choice of the branch partition.

This gives a richer version of the earlier principle

\[
\boxed{\text{support cost}\neq\text{semantic information}.}
\]

For large `t` and large `|A|`, a relatively sparse value fiber can distinguish a very large family of residual-symmetry states.

---

## 11. Current conclusion

The prescribed-support programme now contains two exact families:

### Global coherence

\[
A\wr S_b
\longrightarrow
\Delta A\times S_b,
\]

with

\[
m=b(b-1)t.
\]

### Equal-block partial coherence

\[
A\wr S_b
\longrightarrow
A^{\mathcal P}\rtimes(S_n\wr S_c),
\qquad b=cn,
\]

with

\[
\boxed{m=b(n-1)t.}
\]

Thus the global theorem is not isolated; it is the endpoint of a linear support hierarchy indexed by coherence-block size.

---

## 12. Next strike

The next natural refinement is to allow **unequal block sizes**

\[
n_1+\cdots+n_c=b.
\]

The obvious coherence fiber has size

\[
t\sum_{j=1}^c n_j(n_j-1),
\]

but unlike the equal-block case it need not be a single `H`-orbit, and minimum support may be able to omit redundant size classes while still recovering the entire partition.

Therefore the next question is genuinely extremal:

\[
\boxed{
\text{for a partition type }\lambda=(n_1,\ldots,n_c),
\text{ what is the exact minimum support needed to force }H_\lambda?
}
\]

This is the first point where partition combinatorics and prescribed stabilizer support interact nontrivially.