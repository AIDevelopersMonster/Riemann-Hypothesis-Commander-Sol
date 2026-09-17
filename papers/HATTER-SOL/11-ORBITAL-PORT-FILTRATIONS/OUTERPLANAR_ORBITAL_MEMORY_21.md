# HATTER-SOL-11 · Exact Outerplanar Orbital Memory for the `(2,1)` Fiber

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer.

This note solves the first hostile outerplanar laboratory proposed in `GEOMETRY_ORBITAL_MEMORY_PATH_POLYNOMIAL.md` and gives an exact fixed-host dimensional memory staircase.

---

## 1. The smallest interior forgetting fiber

Take the generic-odd folded pair

\[
(P,Q)=(2,1).
\]

Its three canonical orbital members have orbit-total capacities

\[
\boxed{
\Xi_I=(2,1),
\qquad
\Xi_{II}=(1,2),
\qquad
\Xi_{III}=(0,3).
}
\]

Let the host have even size

\[
k=2m.
\]

We write the orbit-labelled Pareto response polynomial as

\[
Z^{\mathrm{orb}}_{C,2m}(A,O;X,Y)
=
\sum_{(B_A,B_O)\in\mathcal R^{\mathrm{orb}}_{C,2m}(A,O)}
X^{B_A}Y^{B_O}.
\]

---

## 2. Outerplanar low-degree obstruction

### Lemma 11.28.1

Every finite simple outerplanar graph on at least two vertices has at least two vertices of degree at most `2`.

### Proof

For two vertices the claim is immediate.

For `n>=3`, augment the outerplanar graph by adding edges, without adding vertices, until an edge-maximal outerplanar supergraph is obtained. Such a graph is a maximal outerplanar graph: it is the triangulation of a polygon in an outerplane embedding.

Every polygon triangulation has at least two ears. The ear vertices have degree `2` in the maximal outerplanar supergraph, hence degree at most `2` in the original graph. QED.

### Corollary 11.28.2

If every vertex has total capacity `3`, then every outerplanar realization on `2m` vertices has total free boundary at least `2`.

Indeed,

\[
\sum_v\deg(v)
\le
3(2m)-2,
\]

so

\[
|E|\le3m-1
\]

and therefore

\[
\boxed{
B_A+B_O
=6m-2|E|
\ge2.
}
\]

This improves the coarse edge-density obstruction from HATTER-SOL-08 for the special total capacity `3`.

---

## 3. Sharp extremal outerplanar family

For every `m>=2`, define `G_m` on the cyclically ordered vertices

\[
0,1,\ldots,2m-1
\]

by taking the outer cycle `C_{2m}` and adding the nested chords

\[
\boxed{
\{j,2m-j\},
\qquad
1\le j\le m-1.
}
\]

These chords are pairwise disjoint and nested, hence noncrossing. Thus `G_m` is outerplanar.

It has

\[
2m+(m-1)=3m-1
\]

edges. Vertices `0` and `m` have degree `2`, and every other vertex has degree `3`.

Hence the lower bound from Corollary 11.28.2 is sharp.

---

## 4. Two exact colorings of the same host

The graph `G_m` supports two complementary extremal channel allocations.

### Coloring A — saturated capacity-2 channel

Color every outer-cycle edge by the capacity-2 channel and every nested chord by the capacity-1 channel.

Then the capacity-2 channel has degree exactly `2` at every vertex, while the capacity-1 channel is a matching of size `m-1`.

For the state `(2,1)` this gives

\[
\boxed{(B_A,B_O)=(0,2).}
\]

For the state `(1,2)` with the labels exchanged it gives

\[
\boxed{(B_A,B_O)=(2,0).}
\]

### Coloring B — saturated capacity-1 channel

Take the alternating boundary perfect matching

\[
\boxed{
M_0=
\bigl\{\{2j,2j+1\}:0\le j\le m-1\bigr\}.
}
\]

Color `M_0` by the capacity-1 channel and all remaining edges of `G_m` by the capacity-2 channel.

Every vertex is incident to exactly one edge of `M_0`, so the capacity-1 channel is saturated.

After removing `M_0`, every vertex except `0` and `m` has degree `2`, while `0` and `m` have degree `1`. The remaining graph is connected: one explicit Hamiltonian traversal begins

\[
0,
2m-1,
1,
2,
2m-2,
2m-3,
3,
4,
2m-4,
2m-5,
\ldots,
 m.
\]

Hence the remaining graph is a Hamiltonian path and therefore respects capacity `2`.

For `(2,1)` this gives

\[
\boxed{(B_A,B_O)=(2,0),}
\]

while for `(1,2)` it gives

\[
\boxed{(B_A,B_O)=(0,2).}
\]

Thus both mixed orbital states attain both extremal boundary allocations.

---

## 5. Exact outerplanar Pareto fronts

### Theorem T11.28 — exact outerplanar `(2,1)` response

For every

\[
m\ge2,
\]

the three members of the `(2,1)` forgetting fiber have responses

\[
\boxed{
\mathcal R^{\mathrm{orb}}_{O,2m}(2,1)
=
\{(0,2),(2,0)\},
}
\]

\[
\boxed{
\mathcal R^{\mathrm{orb}}_{O,2m}(1,2)
=
\{(0,2),(2,0)\},
}
\]

and

\[
\boxed{
\mathcal R^{\mathrm{orb}}_{O,2m}(0,3)
=
\{(0,2)\}.
}
\]

Equivalently,

\[
\boxed{
Z_I^{O}=Z_{II}^{O}=X^2+Y^2,
\qquad
Z_{III}^{O}=Y^2.
}
\]

### Proof

By Corollary 11.28.2 every feasible boundary vector has total boundary at least `2`.

Because the host size is even, each coordinate

\[
B_A=2mA-2|E_A|,
\qquad
B_O=2mO-2|E_O|
\]

is even.

For Types I and II, Section 4 constructs both possible nonnegative even boundary vectors of total `2`, namely `(0,2)` and `(2,0)`. Any other feasible even boundary vector has total at least `2` and is dominated by one of these two points. Therefore they form the complete Pareto front.

For Type III there is only the oblique channel. The graph `G_m` uses `3m-1` edges, so

\[
B_O=6m-2(3m-1)=2.
\]

The lower bound shows this is optimal. Thus its front is the singleton `(0,2)`. QED.

---

## 6. The two-node exception

For `m=1`, all architecture classes coincide with the single edge `K_2`, and the earlier two-node theorem gives

\[
Z_I=X^4+X^2Y^2,
\]

\[
Z_{II}=X^2Y^2+Y^4,
\]

\[
Z_{III}=Y^4.
\]

Hence all three orbital states are still distinct at `k=2`.

The first outerplanar collision occurs exactly at

\[
\boxed{k=4.}
\]

From that host size onward, Types I and II remain permanently identified by the full outerplanar response, while Type III remains distinct.

Thus the outerplanar memory law for this fiber is

\[
\boxed{
3\longrightarrow2\longrightarrow2\longrightarrow\cdots.
}
\]

---

## 7. Planar closure for the same fiber

Outerplanarity is the last class in which one member remains distinguishable.

### Lemma 11.29.1

For every even host size

\[
k=2m\ge4,
\]
there exists a connected planar cubic graph on `2m` vertices with a perfect matching whose complement is a spanning 2-factor.

### Proof

For `m=2`, use `K_4`. Any perfect matching has two edges, and its complement is a 4-cycle.

For `m>=3`, use the prism graph

\[
C_m\square K_2.
\]

It is planar and 3-regular. The `m` rung edges form a perfect matching; deleting them leaves the two `m`-cycles, a spanning 2-factor. QED.

### Corollary 11.29.2

For every `m>=2`, all three `(2,1)` orbital states have zero planar boundary:

\[
\boxed{
Z_I^{Pl}=Z_{II}^{Pl}=Z_{III}^{Pl}=1.
}
\]

Indeed:

- Type I colors the perfect matching by the capacity-1 channel and the 2-factor by the capacity-2 channel;
- Type II swaps those labels;
- Type III colors every cubic edge oblique.

The zero vector dominates every other response, so the Pareto front is exactly `{(0,0)}`.

Since planar graphs are admissible in the unrestricted class, the same zero response holds there.

---

## 8. Exact fixed-host dimensional memory staircase

Define the orbital response-class count for one forgetting fiber by

\[
\boxed{
\nu_{C,k}(P,Q)
:=
\left|
\left\{
Z^{\mathrm{orb}}_{C,k}(\Xi;X,Y):
\Xi\in f^{-1}(P,Q)
\right\}
\right|.
}
\]

For the smallest interior fiber `(2,1)` and every even host `k=2m>=4` we obtain:

### Theorem T11.29 — dimensional orbital-memory staircase

\[
\boxed{
\nu_{P,2m}(2,1)=3,
\qquad
\nu_{O,2m}(2,1)=2,
\qquad
\nu_{Pl,2m}(2,1)=1,
\qquad
\nu_{A,2m}(2,1)=1.
}
\]

Here:

- strict 1D preserves all three canonical orbital states by T11.27;
- outerplanar geometry identifies exactly Types I and II by T11.28;
- planar geometry already permits complete closure by Corollary 11.29.2;
- unrestricted geometry therefore also has one response class.

Thus at fixed arithmetic input and fixed host size,

\[
\boxed{
3\ \xrightarrow{\text{1D -> outerplanar}}
2\ \xrightarrow{\text{outerplanar -> planar}}
1.
}
\]

This is an exact dimension-driven information-loss theorem, not an activation assumption.

---

## 9. The `k=4` polynomial microscope

At the first nontrivial common host `k=4`, the entire dimensional transition can be written explicitly.

### Strict 1D

From T11.26,

\[
\boxed{
Z_I^{P}=X^6+X^4Y^2+X^2Y^4,
}
\]

\[
\boxed{
Z_{II}^{P}=X^4Y^2+X^2Y^4+Y^6,
}
\]

\[
\boxed{
Z_{III}^{P}=Y^6.
}
\]

All three differ.

### Outerplanar

\[
\boxed{
Z_I^{O}=Z_{II}^{O}=X^2+Y^2,
\qquad
Z_{III}^{O}=Y^2.
}
\]

Exactly one collision has occurred.

### Planar and unrestricted

\[
\boxed{
Z_I^{Pl}=Z_{II}^{Pl}=Z_{III}^{Pl}=1,
}
\]

and likewise in the unrestricted class.

This is the smallest exact laboratory in which increasing admissible geometric dimension progressively erases a canonical orbital refinement that the published `(P,Q)` fold had already forgotten statically.

---

## 10. What is new in this layer

The ingredients used in the proof are classical:

- polygon triangulations and ear vertices;
- outerplanar embeddings;
- perfect matchings;
- prism graphs;
- polynomial encoding of finite Pareto sets.

The HATTER-SOL claim is their composition with the previously proved generic-odd forgetting fiber:

\[
\boxed{
\text{same arithmetic fiber}
\to
\text{same host size}
\to
\text{different architecture classes}
\to
3,2,1\text{ distinguishable orbital responses}.
}
\]

No claim is made that the classical graph facts themselves are new.

---

## 11. Consequence for the geometry-operator programme

The polynomial language is now doing real work: each geometry class produces a finite polynomial-valued signal

\[
C\longmapsto Z_C^{\mathrm{orb}}.
\]

For `(2,1)` this signal has exact collisions along the inclusion ladder.

However, this result still does **not** by itself justify a geometry Laplacian. The inclusion chain

\[
P\subset O\subset Pl\subset A
\]

provides an ordered comparison, but no canonical reversible generator or edge weight has yet been derived.

The correct next object is therefore the finite-difference profile

\[
Z_O-Z_P,
\qquad
Z_{Pl}-Z_O,
\qquad
Z_A-Z_{Pl},
\]

not a Laplacian imposed by analogy.

---

## 12. Next target

The `(2,1)` fiber is now completely classified across the full HATTER-SOL-08 dimensional ladder.

The next strike should test whether the staircase

\[
3\to2\to1
\]

is exceptional to total capacity `3` or begins an infinite law.

The smallest next interior fibers are

\[
(3,1)
\qquad\text{and}\qquad
(2,2).
\]

The hostile target is:

> determine whether outerplanar geometry still identifies the rank-swapped states `(P,Q)` and `(Q,P)`, or whether the `(2,1)` collision depends essentially on the subcubic extremal structure.

A single counterexample is enough to kill any naive universal `I=II` outerplanar rule.