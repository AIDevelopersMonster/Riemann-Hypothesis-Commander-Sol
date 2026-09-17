# HATTER-SOL-11 · Exact `(6,5)` Closure at Planar Orders 30 and 32

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the orbit-total `Xi` model.

**Scope.** Throughout,

\[
\Omega=(a;\{b,c\})\mapsto\Xi=(A,O)=(a,b+c)
\]

is the canonical orbit-total two-channel projection. This note concerns only the `Xi` response model.

The previous theorem closed order `28`. Here the next two orders are closed simultaneously. Their 5-regular planar supports require respectively `9` and `10` added triangulation edges.

The main technical point is that, up to ten added edges, any degree concentration above six can still be removed by controlled local retriangulation of one or two faces incident with the unique overloaded vertex.

---

## 1. External existence input

Hasheminezhad, McKay and Reeves, *Recursive generation of simple planar 5-regular graphs and pentangulations* (JGAA 15(3), 2011), Table 1, list 5-connected simple planar 5-regular graphs at both orders:

- order `30`: `21542` 5-connected examples;
- order `32`: `165530` 5-connected examples.

Fix one such plane graph `H_n` for each

\[
n\in\{30,32\}.
\]

Then

\[
|E(H_n)|=\frac{5n}{2}.
\]

A triangulation on the same vertex set has `3n-6` edges, so the number of added edges is

\[
r_n
=3n-6-\frac{5n}{2}
=\frac n2-6.
\]

Hence

\[
\boxed{r_{30}=9,
\qquad
r_{32}=10.}
\]

Because `H_n` is 5-connected, it is 3-connected. We use the standard polyhedral face-intersection property: two distinct facial cycles intersect in at most one vertex or one edge. In particular, two nonconsecutive faces around a fixed vertex have no other common vertex.

---

## 2. Local ear-off lemma recalled

From `PLANAR_65_ORDER_28_CLOSURE.md`:

> If `C` is a nontriangular facial polygon and `x` is a boundary vertex, then `C` can be retriangulated so that no added diagonal is incident with `x`, while every other boundary vertex receives at most three added incidences from the new triangulation of `C`.

We call this an **ear-off retriangulation at `x`**.

---

## 3. A simple concentration bound

Let `F` be any simple graph with `m` edges. For two distinct vertices `x,y`,

\[
d_F(x)+d_F(y)
\le m+1,
\]

because

\[
d_F(x)+d_F(y)-\mathbf 1_{xy\in E(F)}
\]

counts edges incident with `x` or `y`, and there are at most `m` such edges.

Therefore if

\[
m\le10,
\]
there cannot be two vertices of degree at least seven:

\[
7+7>10+1.
\]

### Lemma T11.67 — uniqueness of the overloaded augmentation vertex

For a triangulation-complement graph `F` with

\[
|F|\le10,
\]
there is at most one vertex satisfying

\[
d_F(v)\ge7.
\]

---

## 4. The nine-edge augmentation theorem

### Theorem T11.68 — nine added edges can be balanced below degree seven

Let `H` be a 5-regular 3-connected plane graph whose faces require exactly nine added edges to triangulate. Then there is a face-by-face triangulation whose added-edge graph `F` satisfies

\[
\boxed{|F|=9,
\qquad
\Delta(F)\le6.}
\]

### Proof

Start from an arbitrary triangulation. If `Delta(F)<=6`, stop.

Otherwise let `x` be the unique overloaded vertex, and set

\[
d:=d_F(x)\in\{7,8,9\}.
\]

There are

\[
q:=9-d
\]

added edges not incident with `x`.

Because `H` is 5-regular, exactly five faces are incident with `x`. For such a face `C`, let `k_C` denote the number of added diagonals in `C` incident with `x`. Then

\[
\sum_{C\ni x}k_C=d.
\]

### Case `d=7`

Choose an incident face with `k_C>=1` and perform ear-off retriangulation there.

The degree of `x` falls to at most six.

For any other vertex `v` of `C`, no added edge from `x` in another face can hit `v`: otherwise two distinct faces of the 3-connected plane graph would contain both `x` and `v` without sharing the original edge `xv`. Hence outside `C`, `v` is incident only with the `q=2` off-center added edges. The new triangulation of `C` contributes at most three. Thus

\[
d_F(v)\le2+3=5.
\]

All vertices outside `C` were already of degree at most six by T11.67.

### Case `d=8`

Now `q=1`. Since eight incidences are distributed among five incident faces, some face satisfies `k_C>=2`.

Ear-off retriangulation of that face reduces the degree of `x` by at least two, hence to at most six. Every other boundary vertex has outside added degree at most one and gains at most three inside the face, so its new degree is at most four.

### Case `d=9`

Here `q=0`.

If some incident face has `k_C>=3`, ear it off and reduce `d_F(x)` to at most six; every other affected vertex gets added degree at most three.

Otherwise every `k_C<=2`. Since five nonnegative integers at most two sum to nine, their multiset is exactly

\[
\{2,2,2,2,1\}.
\]

Among the four faces with value two, choose two that are nonconsecutive in the cyclic order around `x`. Such a pair exists on a 5-cycle.

Ear off both faces. Their facial cycles have no common vertex other than `x`, so no other vertex receives diagonals from both retriangulations. The degree of `x` drops by four, from nine to five, while every other affected vertex has added degree at most three.

Thus in all cases the modified augmentation has maximum degree at most six. QED.

---

## 5. The ten-edge augmentation theorem

The order-32 case has one additional concentration pattern.

### Theorem T11.69 — ten added edges can be balanced below degree seven

Let `H` be a 5-regular 3-connected plane graph whose faces require exactly ten added edges to triangulate. Then there exists a triangulation whose added-edge graph `F` satisfies

\[
\boxed{|F|=10,
\qquad
\Delta(F)\le6.}
\]

### Proof

Again begin with any face triangulation. If `Delta(F)<=6`, stop. By T11.67 the overloaded vertex `x` is unique.

Let

\[
d=d_F(x)\in\{7,8,9,10\},
\qquad
q=10-d.
\]

The cases `d=7,8,9` are handled exactly as in T11.68, with one extra off-center edge available in each corresponding estimate:

- `d=7`: `q=3`; ear off any face with `k_C>=1`; every other affected vertex has degree at most `3+3=6`;
- `d=8`: `q=2`; some face has `k_C>=2`; every other affected vertex has degree at most `2+3=5`;
- `d=9`: `q=1`; either one face has `k_C>=3`, or the distribution is `{2,2,2,2,1}` and two nonconsecutive two-faces are ear-off retriangulated; every other affected vertex has degree at most four.

It remains to treat `d=10`, where every added edge is incident with `x`.

Let the five incident-face loads be

\[
k_1,\ldots,k_5,
\qquad
k_i\ge0,
\qquad
\sum_i k_i=10.
\]

If some `k_i>=4`, ear off that one face and reduce the degree of `x` to at most six.

Assume therefore that every `k_i<=3`.

Consider the five unordered pairs of nonconsecutive faces around `x`. Each face appears in exactly two such pairs. Therefore the sum of the five pair-weights is

\[
2\sum_i k_i=20.
\]

Their average weight is four, so at least one nonconsecutive pair has total load at least four.

Ear off those two faces. Because they are nonconsecutive, their facial cycles intersect only in `x`. Hence every other vertex is affected by at most one new local triangulation and receives at most three added incidences. The degree of `x` falls by at least four, to at most six.

Thus `Delta(F)<=6`. QED.

---

## 6. Terminal endpoints for orders 30 and 32

Apply T11.68 at order `30` and T11.69 at order `32`. For either host we obtain a triangulation `T_n` with added-edge graph `F_n` such that

\[
|F_n|=r_n,
\qquad
\Delta(F_n)\le6.
\]

Color the original 5-regular support `H_n` by the capacity-five channel and the added edges `F_n` by the capacity-six channel.

This gives

\[
B_O=0
\]

and

\[
B_A=6n-2r_n=5n+12.
\]

Hence the terminal points are

\[
\boxed{(162,0)}
\]

at `n=30`, and

\[
\boxed{(172,0)}
\]

at `n=32`.

For the `B_O=2` endpoint, let

\[
S_n:=\{v:d_{F_n}(v)=6\}.
\]

Since

\[
\sum_v d_{F_n}(v)=2r_n,
\]
we have

\[
|S_{30}|\le3,
\qquad
|S_{32}|\le3.
\]

The 5-regular supports have respectively `75` and `80` edges. At most `5|S_n|<=15` support edges are incident with `S_n`, so in either case there exists an edge `e` of `H_n` whose two endpoints lie outside `S_n`.

Move `e` from the capacity-five channel to the capacity-six channel. Then

\[
\Delta(F_n\cup\{e\})\le6,
\qquad
\Delta(H_n-e)\le5.
\]

Thus `B_O=2` is attained, giving

\[
\boxed{(160,2)}
\]

at order `30`, and

\[
\boxed{(170,2)}
\]

at order `32`.

### Theorem T11.70 — terminal-pair closure at orders 30 and 32

For `n=30,32`, both terminal minimum-total points

\[
\boxed{(5n+10,2),
\qquad
(5n+12,0)}
\]

belong to the planar `(6,5)` Pareto front.

---

## 7. Exact full fronts

For `(6,5)` on any even host,

\[
B_A\ge12,
\qquad
B_O\ge0,
\qquad
B_A+B_O\ge5n+12.
\]

T11.57 from `PLANAR_65_TERMINAL_TAIL_16_24.md` realizes every parity-compatible point on the minimum-total line with `B_O>=4` for every even `n>=16`.

T11.70 supplies the last two points for `n=30,32`.

Therefore:

### Theorem T11.71 — exact planar `(6,5)` fronts at orders 30 and 32

For

\[
n\in\{30,32\},
\]

\[
\boxed{
\mathcal R^\Xi_{Pl,n}(6,5)
=
\left\{
(12+2t,5n-2t):
0\le t\le\frac{5n}{2}
\right\}.
}
\]

Equivalently,

\[
\boxed{
Z^\Xi_{Pl,n}(6,5;X,Y)
=
\sum_{t=0}^{5n/2}X^{12+2t}Y^{5n-2t}.
}
\]

Any feasible point above the minimum-total line is componentwise dominated by a displayed even lattice point. Hence the displayed segment is the complete Pareto front. QED.

---

## 8. Updated exact range

Combining the previous layers with T11.71, the exact planar `(6,5)` Pareto front is now known for every even host size

\[
\boxed{4\le n\le32.}
\]

The first unresolved order is now

\[
\boxed{n=34,}
\]

where a 5-regular support requires

\[
\frac{34}{2}-6=11
\]

added triangulation edges.

At eleven edges, a degree-seven overloaded vertex may coexist with four off-center edges. The present ear-off estimate then gives only

\[
4+3=7,
\]

so the one-face argument is no longer automatically safe.

Thus order `34` is the first place where the current local proof genuinely stops. The next target is either:

1. strengthen the ear-off lemma from local added-degree `3` to `2`, or
2. exploit the distribution of the four off-center edges to choose a repair face avoiding their high-incidence vertices.

That is a real new obstruction rather than a bookkeeping extension.