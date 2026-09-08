# FCOA-Z Research State — Partition Support Frontier

Date: 2026-08-31

## Closed results

### Full partition + phase coherence

For arbitrary partition

\[
\lambda=(n_1,\ldots,n_c),
\qquad \sum_j n_j=b,
\]

with transitive internal branch group `A` of degree `t`, the exact prescribed support is

\[
\boxed{
m_G(H_{\mathcal P};S_\times)
=t\sum_j n_j(n_j-1).}
\]

Complement recovery does not reduce this cost because block-set recovery does not force diagonal phase coupling inside an omitted non-singleton block.

File:

- `UNEQUAL_PARTITION_COHERENCE_SUPPORT.md`

### Partition-only reduction

For the weaker target

\[
J_{\mathcal P}=A^b\rtimes K_{\mathcal P},
\]

partition-only invariant support must be a union of full `Lambda^2` fibers over branch pairs. Hence

\[
\boxed{
m_G(J_{\mathcal P};S_\times)=t^2 d(\mathcal P),}
\]

where

\[
d(\mathcal P)
=
\min\{|R|:R\subseteq\Omega_b,\ \operatorname{Aut}(R)=K_{\mathcal P}\}.
\]

This reduces the FCOA problem exactly to minimum directed-relation support for the partition stabilizer.

File:

- `PARTITION_ONLY_SUPPORT_COMPRESSION.md`

### Exact two-block family

For two blocks `p>=q`:

\[
d(p,q)=
\begin{cases}
p,&p>q=1,\\
q(q-1),&p>q\ge2,\\
2q(q-1),&p=q=q\ge2.
\end{cases}
\]

### One non-singleton block plus singleton family

For type `(n,1^m)`,

\[
\boxed{
d(n,1^m)
=
\min\{n(n-1),\ nm,\ m(m-1)\text{ when }m\ge2\}.}
\]

### Three distinct blocks

For

\[
p>q>r\ge1,
\]

\[
\boxed{d(p,q,r)=qr.}
\]

Thus

\[
\boxed{m_G(J_{(p,q,r)};S_\times)=t^2qr.}
\]

The largest block is recovered entirely as the isolated complement of one directed complete bipartite relation between the two smaller blocks.

File:

- `PARTITION_ONLY_THREE_DISTINCT_BLOCKS.md`

## Resource non-monotonicity

The stronger target

\[
H_{\mathcal P}\le J_{\mathcal P}
\]

does not have a uniformly larger support cost.

Partition-only invariance retains independent `A x A` actions and therefore selected branch pairs cost full `t^2` fibers. Phase coherence allows thin diagonal fibers of size `t`.

Consequently subgroup inclusion does not impose monotonicity on prescribed support cost.

This is now a stable FCOA principle:

\[
\boxed{
H_1\le H_2
\not\Rightarrow
m_G(H_1;S)\ge m_G(H_2;S)
\text{ or }m_G(H_1;S)\le m_G(H_2;S).
}
\]

## Active frontier

For four or more distinct block-size classes, one selected cross orbital is insufficient because at least two untouched classes receive identical empty incidence and merge into a larger twin class.

The remaining invariant is therefore a weighted directed twin-separation problem on block-size classes.

Each possible marker has cost:

- within-class clique marker on class size `n`: `n(n-1)`;
- directed cross marker between class sizes `n_i,n_j`: `n_i n_j`.

The selected markers must prevent any unwanted fusion of size classes after blow-up.

The next target is to characterize

\[
\boxed{d(\lambda)}
\]

as a minimum-cost separating digraph/code problem on the distinct size classes, and then determine whether this optimization has a closed formula or a polynomial-time dynamic program.

## Publication threshold

The post-publication branch now contains a substantial body of exact theorems, but a new Zenodo paper is not yet recommended. The strongest publication package would combine:

1. prescribed-stabilizer support `m_G(H;S)`;
2. wreath coherence exact formulas;
3. full unequal-partition coherence theorem;
4. partition-only reduction;
5. exact complement-compression families;
6. a general solution or complexity theorem for the weighted twin-separation frontier;
7. dedicated literature audit against relation groups, regular sets, distinguishing theory, and minimum-size digraph representations of permutation groups.

The next strike should therefore remain mathematical rather than editorial.