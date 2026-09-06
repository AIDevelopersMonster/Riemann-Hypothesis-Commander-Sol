# QGE3 LQR — Resolution-Trade Hierarchy at r=7

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** post-publication continuation  
**Scope:** abstract pure defect-two LQR synchronization  
**Proof status:** structural theorems plus exhaustive finite classifications for minimal support 5 and 6

This note continues `LQR_PLANE_RESOLUTION_TRADES.md`. The main point is that the `r=7` obstruction theory does not terminate at support four: minimal resolution trades occur at support 5, 6, 7 and higher. Nevertheless the higher layers admit a uniform permutation/incidence description that is much smaller than brute-force enumeration of all compatible plane families.

---

## 1. Normalized witness model

Let `A` be a closed support of `k` source colors in a pure defect-two obstruction. Normalize the phase-0 permutation to the identity and write

\[
\rho_0=\mathrm{id},\qquad \rho_i\in S_A\quad(1\le i\le r-1).
\]

For source color `a`, the three blocks of its partition are the fibers of

\[
i\longmapsto \rho_i(a).
\]

Since the color has defect two,

\[
\left|\{\rho_i(a):0\le i<r\}\right|=3.
\]

The alternative quotient coloring sends every block of the source partition to the corresponding target value.

---

## 2. Incidence–2-Factor Theorem

Construct a bipartite graph `G` with left vertices the source colors and right vertices the target colors. Join source `a` to target `b` exactly when some phase satisfies

\[
\rho_i(a)=b.
\]

### Theorem 2.1
For every normalized pure-plane resolution trade on `k` colors:

1. `G` is a simple 3-regular bipartite graph;
2. the diagonal matching
   \[
   I=\{(a,a):a\in A\}
   \]
   is contained in `G`;
3. therefore
   \[
   \boxed{G=I\cup H}
   \]
   where `H` is a 2-regular bipartite graph disjoint from the diagonal;
4. every phase permutation `rho_i` is a perfect matching of `G`;
5. the phase matchings cover every edge:
   \[
   \boxed{G=\bigcup_{i=0}^{r-1}M(\rho_i)}.
   \]

### Proof
A source color has exactly three partition blocks, and in a noncanonical trade two blocks of the same source cannot belong to the same target class. Hence every source vertex has three distinct target neighbours. Dually every target resolution class contains exactly three blocks from three distinct sources, so every target vertex also has degree three.

Normalization at phase zero gives `rho_0(a)=a`, hence the diagonal perfect matching is present. Removing it leaves degree two at every left and right vertex, so the remainder is a bipartite 2-factor.

For a fixed phase `i`, the map `a -> rho_i(a)` is a permutation, hence its graph is a perfect matching contained in `G`. Every source-target incidence edge corresponds to a nonempty partition block, so it contains some phase and therefore occurs in at least one phase matching. \(\square\)

This theorem is independent of `r=7`; only the number of phase matchings depends on `r`.

---

## 3. Minimal support and transitivity

Let

\[
\Gamma=\langle \rho_0,\rho_1,\dots,\rho_{r-1}\rangle\le S_A.
\]

### Lemma 3.1
If a closed-support obstruction is inclusion-minimal, then `Gamma` acts transitively on `A`.

### Proof
If `Gamma` has more than one orbit, every phase permutation preserves each orbit. Any nontrivial orbit therefore supports the restricted phase tuple. For every source color in that orbit the same three image values remain, and pairwise compatibility is inherited from the ambient family. Hence a proper orbit gives a smaller closed-support obstruction, contradicting minimality. \(\square\)

Transitivity is necessary, not sufficient: a transitive witness family may still contain a different smaller obstruction with another witness.

After contracting the distinguished diagonal matching `I`, the off-diagonal factor `H` becomes a loopless directed graph with indegree two and outdegree two on the color set. Minimal trades therefore have a connected/transitive permutation skeleton.

---

## 4. Exhaustive finite classification protocol

For `r=7` there are seven phase permutations. To enumerate a minimal trade on `k` colors without enumerating all `k`-subsets of the 301 planes:

1. enumerate 3-regular bipartite support graphs `G` on `k+k` vertices containing the diagonal matching;
2. quotient them by simultaneous relabeling of source and target colors;
3. enumerate the perfect matchings supported by each `G`;
4. fix `rho_0=id` and enumerate multisets of the remaining six phase matchings;
5. retain only tuples whose union covers every edge of `G`;
6. reconstruct the `k` source partitions from the coordinate fibers;
7. enforce pairwise cut-space compatibility;
8. remove families containing a smaller obstruction;
9. quotient the surviving plane families by the natural `S_7` action on phases.

Completeness follows from Theorem 2.1: every normalized trade appears in this search.

---

## 5. Exact minimal five-core layer

For `k=5`, the off-diagonal 2-factor has cycle type either

\[
C_{10}
\qquad\text{or}\qquad
C_4\sqcup C_6.
\]

The distinguished diagonal matching refines these into exactly

\[
\boxed{5}
\]

simultaneous-relabeling support-graph orbits. Four have off-diagonal cycle type `C10` and one has type `C4+C6`.

Exhaustive seven-phase matching enumeration gives:

\[
\boxed{162}
\]

minimal obstructing five-plane `S_7`-orbits.

Their orbit-size distribution is

\[
\boxed{
75\times5040
+81\times2520
+2\times1008
+4\times504.
}
\]

Hence the number of concrete minimal five-cores is

\[
\boxed{586\,152}.
\]

Of the five normalized support-graph orbits, one produces no minimal five-core; every compatible witness arising from it already contains a smaller obstruction. The other four support the complete five-core layer.

---

## 6. Exact minimal six-core layer

For `k=6`, the off-diagonal 2-factor can have cycle type

\[
C_{12},\quad
C_4\sqcup C_8,\quad
C_6\sqcup C_6,\quad
C_4\sqcup C_4\sqcup C_4.
\]

After retaining the distinguished diagonal matching there are exactly

\[
\boxed{23}
\]

simultaneous-relabeling support-graph orbits, distributed as

\[
10\text{ of type }C_{12},\qquad
4\text{ of type }C_4+C_8,\qquad
7\text{ of type }C_6+C_6,\qquad
2\text{ of type }C_4+C_4+C_4.
\]

Only 16 of the 23 normalized support types produce inclusion-minimal six-color trades after compatibility and smaller-core exclusion.

The final `S_7` classification contains exactly

\[
\boxed{1\,908}
\]

minimal obstructing six-plane orbits.

Their orbit-size distribution is

\[
\boxed{
1684\times5040
+202\times2520
+13\times1680
+4\times1260
+5\times840.
}
\]

Therefore the concrete minimal six-core layer has size

\[
\boxed{9\,027\,480}.
\]

This explosive jump

\[
6\to25\to162\to1908
\]

in the numbers of minimal `S_7` trade orbits at supports `3,4,5,6` shows that a complete obstruction theory cannot reasonably be organized as a flat list of cores.

---

## 7. Genuine higher-support trades

Higher support is not optional.

An explicit inclusion-minimal seven-plane trade is

```text
(70, 73, 136, 164, 211, 224, 295)
```

in the canonical plane indexing of the verifier. Its partitions are

```text
 70 : 014 | 26  | 35
 73 : 015 | 246 | 3
136 : 024 | 1   | 356
164 : 03  | 124 | 56
211 : 056 | 12  | 34
224 : 034 | 156 | 2
295 : 06  | 15  | 234
```

Every subfamily of size at most six is synchronizing, while the seven-family has a noncanonical resolution.

The symmetry-aware cutting-plane search also produced inclusion-minimal examples of support ten and twelve, for example

```text
10-core:
(2, 14, 34, 59, 144, 147, 243, 249, 264, 278)

12-core:
(2, 47, 53, 73, 84, 120, 142, 208, 213, 249, 256, 278)
```

These examples prove that the `r=7` hierarchy is genuinely nonlocal: forbidding all cores through support six does not characterize synchronization.

---

## 8. Compact cutting-plane formulation

The pure-plane compatibility problem has a particularly small linear packing formulation. The ambient cut space is

\[
\mathbb F_2^6\setminus\{0\},
\]

with 63 nonzero cut vectors. Every partition plane occupies exactly three of them. Therefore pairwise compatibility is equivalent to the 63 inequalities

\[
\boxed{
\sum_{P:\,v\in W(P)}x_P\le1
\qquad(v\in\mathbb F_2^6\setminus\{0\}).
}
\]

For every known obstruction core `C`, add the valid cut

\[
\boxed{
\sum_{P\in C}x_P\le |C|-1.
}
\]

This gives an exact cutting-plane strategy:

1. solve for a packing with at least 15 planes;
2. run the exact resolution oracle;
3. if the family is non-synchronizing, shrink to an inclusion-minimal trade;
4. add the whole `S_7` orbit of that trade;
5. repeat.

A proof of `M_7=14` would result if the finite accumulated cuts make `|F|>=15` infeasible. A synchronizing feasible family would instead disprove that equality.

---

## 9. Current status of M_7

Let

\[
M_7=\max\{m_2:\text{there is a synchronizing pure defect-two family on seven phases}\}.
\]

The explicit construction in `LQR_PLANE_RESOLUTION_TRADES.md` still gives

\[
M_7\ge14.
\]

The raw cut-space packing bound gives

\[
M_7\le21.
\]

The present computations have not produced a synchronizing fifteen-plane family. A compact cutting-plane search has accumulated many valid obstruction orbits, including supports 5, 6, 7, 8, 9, 10 and 12, but the current MILP has not yet certified infeasibility of `|F|>=15`.

Therefore the rigorous status remains

\[
\boxed{14\le M_7\le21.}
\]

In particular, neither `M_7=14` nor `M_7=15` is claimed here.

---

## 10. Revised general target

The first plane-core guess

\[
M_r\stackrel{?}{=}2^{r-3}-1
\]

was useful for discovering the problem, but the `r=7` hierarchy shows that the correct invariant is not a single plane count. The natural object is now:

\[
\boxed{
\text{the unique-resolution trade hypergraph of partition-plane packings.}
}
\]

The structural route forward is:

1. study cubic incidence graphs with their distinguished diagonal matching;
2. study the transitive permutation systems whose seven phase matchings cover those graphs;
3. derive sufficient conditions forcing a resolution trade without enumerating every hyperedge;
4. use `r=7` only as the first nontrivial laboratory for the general theory.

A particularly sharp next question is whether a uniquely resolvable compatible family on seven phases can contain fifteen planes. This is now a finite extremal problem with a clean permutation/incidence model rather than an undifferentiated search over `301 choose 15` families.

---

## 11. Scope firewall

1. This note concerns abstract LQR point-image synchronization only.
2. No real-operation-cell repair invariant is introduced.
3. The Incidence–2-Factor Theorem and transitivity lemma are analytic statements.
4. The support-5 and support-6 orbit counts are finite computer-assisted classifications reproduced by the accompanying verifier.
5. Cutting-plane failures to find a synchronizing 15-family are treated only as search evidence, not as a theorem.
