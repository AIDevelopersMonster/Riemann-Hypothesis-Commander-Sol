# HATTER-SOL-11 · Exact `(6,5)` Closure at Planar Order 40

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the orbit-total `Xi` model.

**Scope.** Throughout,
\[
\Omega=(a;\{b,c\})\mapsto\Xi=(A,O)=(a,b+c)
\]
is the orbit-total quotient. No statement below upgrades the result to full `Omega` semantics.

The preceding order-40 probes established two facts:

1. the order-38 two-center proof does not extend verbatim, because a fourteen-edge added graph may have separated degree-seven centers;
2. nevertheless every genuine two-center fourteen-edge augmentation is repairable (T11.88).

This note closes the remaining one-center case and therefore order `40` itself.

---

## 1. External support existence at order 40

For a planar 5-regular graph on `n` vertices,
\[
|E|=\frac{5n}{2},
\qquad
f=2+|E|-n=\frac{3n}{2}+2.
\]
At `n=40`,
\[
\boxed{f=62.}
\]

We use the following **external** existence input, not proved in HATTER-SOL-11:

> There are 5-connected 5-regular planar graphs with `f` faces for `f=20` and for every `f>=26` with `f congruent 2 (mod 3)`.

This range is quoted explicitly in Franz J. Brandenburg, *On Optimal Beyond-Planar Graphs*, Computing in Geometry and Topology 2(1), 2023, DOI `10.57717/cgt.v2i1.10`, citing Hasheminezhad--McKay--Reeves.

Since
\[
62\ge26,
\qquad
62\equiv2\pmod3,
\]
there exists a 5-connected 5-regular plane graph `H_40`.

Fix one such support. Then
\[
|V(H_{40})|=40,
\qquad
|E(H_{40})|=100.
\]
A triangulation on the same vertex set has
\[
3\cdot40-6=114
\]
edges, so every face-by-face triangulation adds exactly
\[
\boxed{14}
\]
edges.

---

## 2. One-center setup

Let `F` be a fourteen-edge triangulation complement of a 5-regular 3-connected plane support `H`.

Assume `F` has exactly one overloaded vertex `x`, meaning
\[
d_F(x)=d\ge7,
\]
while every other vertex has degree at most six.

Put
\[
q:=14-d.
\]
Thus `q` is the number of old added edges not incident with `x`.

Because `H` is 5-regular, exactly five support faces meet `x`. For such a face `C`, let `k_C` be the number of old added diagonals of `C` incident with `x`. Then
\[
\sum_{C\ni x} k_C=d.
\]

Let `Q` denote the off-center subgraph consisting of the `q` added edges not incident with `x`.

The local repair tools T11.72 and T11.77 are used with the following bookkeeping rule: if `v!=x` lies on a repaired face `C` at `x`, then no old added edge `xv` survives in another face, by the facial intersection property of 3-connected plane graphs.

---

## 3. The new case `d=7`, `q=7`

This is the first pattern not covered by the order-38 proof.

Choose any loaded face `C` at `x`, so `k_C>=1`.

### Ordinary subcase

Suppose every boundary vertex `v!=x` of `C` has **outside-`C`** degree in `Q` at most four.

Apply T11.72 at `x` on `C`. Then `x` loses at least one incidence and falls to degree at most six. Every other affected vertex receives at most two new local diagonals, so
\[
d(v)\le4+2=6.
\]
Thus the repair is complete.

### Hot-vertex subcase

Suppose some boundary vertex `y!=x` has outside-`C` `Q`-degree at least five. Such a vertex is unique: in a seven-edge graph two vertices of degree at least five are impossible because
\[
5+5-1>7.
\]

Apply T11.77 to `C`, ear-off at `x` and protect `y`.

If the outside-`C` degree of `y` is at most five, then
\[
d(y)\le5+1=6
\]
and every other affected vertex is safe; the unique high-degree structure of a seven-edge graph forces every other `Q`-degree low enough for the local `<=3` bound.

The only remaining situation is
\[
d_{Q,\mathrm{outside}\ C}(y)=6.
\]
Then six of the seven off-center edges form a star centered at `y`; the seventh edge is a single residual off-center edge. After the first repair, `y` has degree at most seven.

Choose a face `D` at `y` containing one of those six star edges outside `C`, and apply T11.72 at `y` on `D`. This removes at least one old star incidence, so `y` falls to degree at most six.

If `D` does not contain `x`, then `x` remains at degree at most six and the repair is complete.

If `D` contains `x`, then `x,y` are adjacent in the support and `C,D` are the two faces incident with the support edge `xy`. Let their old `x`-loads be `k_C,k_D`. After the two repairs,
\[
d(x)\le7-k_C-k_D+2.
\]
If this is at most six, stop.

Otherwise
\[
k_C+k_D\le2.
\]
Hence at least five old `x`-incidences lie in the three noncommon faces at `x`. One such face `E` has `x`-load at least two. Apply T11.72 to `E` at `x`. Since `E` does not contain `y`, this decreases `x` by at least two without changing `y`, and therefore gives `d(x)<=6`.

Degree safety for noncentral vertices follows from the same facial-overlap bounds used at orders `36` and `38`:

- the first protected repair contributes at most three;
- the second and third ordinary ear-off repairs contribute at most two each;
- consecutive faces at a center share only one support edge;
- a vertex lying on a common repaired face with a center cannot retain an added edge to that center elsewhere;
- outside the six-edge star there is only one residual edge.

The worst possible overlap is `3+2+1=6`.

Thus `d=7` is closed.

---

## 4. The case `d=8`, `q=6`

Some incident face `C` has
\[
k_C\ge2.
\]

If every boundary vertex has outside-`C` `Q`-degree at most four, T11.72 gives the bound `4+2=6` and lowers `x` to degree at most six.

Otherwise there is a unique hot vertex `y` of outside `Q`-degree at least five. Apply T11.77 protecting `y`.

If its outside degree is five, then `5+1=6` and the repair is complete.

The only exceptional possibility is outside degree six. Then all six off-center edges form a star centered at `y`. After the protected repair, `y` has degree at most seven.

Choose a face `D` containing one of the six star edges outside `C` and ear off at `y` using T11.72. This lowers `y` to degree at most six.

If `D` avoids `x`, stop. If `D` is the second support face common to adjacent vertices `x,y`, then after the first two repairs
\[
d(x)\le8-k_C-k_D+2.
\]
If this exceeds six, then because `k_C>=2` we have `k_C+k_D<=3`, so at least five old `x`-incidences lie on the three noncommon faces. Choose one of load at least two and ear it off at `x`. This final repair lowers `x` to at most six and does not affect `y`.

There is no residual off-center edge in this case, so the noncentral degree estimates are even smaller than in Section 3.

Thus `d=8` is closed.

---

## 5. The case `d=9`, `q=5`

If some incident face has
\[
k_C\ge3,
\]
repair it.

If `Delta(Q)<=4`, T11.72 is enough. If `Delta(Q)=5`, then `Q` is a five-edge star centered at a unique vertex `y`; protect `y` with T11.77 if it lies on the chosen face. Then
\[
d(y)\le5+1=6,
\]
while every other affected vertex has off-center degree at most one and receives at most three new incidences.

If no face has load at least three, the five loads are
\[
\{2,2,2,2,1\}.
\]
Choose two nonconsecutive load-two faces and repair both. A vertex other than `x` belongs to at most one of them. If `Q` is a five-star and its center lies on one repaired face, use T11.77 on that face and T11.72 on the other. The two common support faces of adjacent vertices are consecutive, so the star center cannot lie on both selected nonconsecutive faces.

Thus `x` loses four incidences and every other vertex remains at degree at most six.

---

## 6. The cases `d>=10`

Here
\[
q\le4.
\]
The strengthened two-incidence ear-off lemma is sufficient, so the order-34/36/38 load arguments apply without a new hot-vertex phenomenon.

### `d=10`, `q=4`

If one face has load at least four, repair it. Otherwise, among the five pairs of nonconsecutive faces one has combined load at least four because their total pair-load is `2d=20`. Repair such a pair. Every affected noncentral vertex has degree at most
\[
4+2=6.
\]

### `d=11`, `q=3`

A nonconsecutive pair has combined load at least
\[
\left\lceil\frac{22}{5}\right\rceil=5.
\]
Repair it (or one face of load at least five). Noncentral degree is at most `3+2=5`.

### `d=12`, `q=2`

The three heaviest incident faces have total load at least
\[
\left\lceil\frac{36}{5}\right\rceil=8.
\]
Repair them. Any other vertex lies on at most two faces incident with `x`, so it receives at most four local incidences; with the two off-center edges its degree is at most six.

### `d=13`, `q=1`

Repair the three heaviest faces; their total load is at least eight. Every noncentral vertex has degree at most `4+1=5`.

### `d=14`, `q=0`

Repair the three heaviest faces; their total load is at least
\[
\left\lceil\frac{42}{5}\right\rceil=9.
\]
Thus `x` falls to degree at most five, and every other vertex receives at most four new incidences.

Hence every one-center pattern is repairable.

---

## 7. Fourteen-edge augmentation theorem

Combine the one-center analysis above with T11.88 for two centers.

### Theorem T11.89 — fourteen added edges can always be balanced below degree seven

Let `H` be a 5-regular 3-connected simple plane graph whose faces require exactly fourteen added edges to triangulate. Then there exists a face-by-face triangulation `T` such that
\[
F:=E(T)\setminus E(H)
\]
satisfies
\[
\boxed{|F|=14,\qquad \Delta(F)\le6.}
\]

### Proof

Start from any face triangulation.

- If `Delta(F)<=6`, stop.
- By T11.86 there are at most two overloaded vertices.
- If there are two, apply T11.88.
- If there is one, Sections 2--6 above give a repair for every possible degree `7<=d<=14`.

Thus a balanced triangulation always exists. QED.

This is stronger than what order `40` requires: it holds for **every** 5-regular 3-connected plane support with fourteen-edge triangulation defect, not merely for one chosen support.

---

## 8. Terminal endpoint `B_O=0` at order 40

Apply T11.89 to the external 5-connected support `H_40`. Obtain a triangulation `T_40` with
\[
|F|=14,
\qquad
\Delta(F)\le6.
\]

Color `H_40` by the capacity-five channel and `F` by the capacity-six channel.

Then
\[
B_O=5\cdot40-2\cdot100=0,
\]
and
\[
B_A=6\cdot40-2\cdot14=212.
\]
Therefore
\[
\boxed{(212,0)}
\]
is attained.

---

## 9. One-edge recoloring and `B_O=2`

Let
\[
S:=\{v:d_F(v)=6\}.
\]
Since
\[
\sum_v d_F(v)=28,
\]
we have
\[
|S|\le4.
\]

The 5-regular support has one hundred edges. At most
\[
5|S|\le20
\]
of them are incident with `S`, so there exists a support edge `e` with both endpoints outside `S`.

Move `e` from the capacity-five channel to the capacity-six channel. Then
\[
\Delta(F\cup\{e\})\le6,
\qquad
\Delta(H_{40}-e)\le5.
\]
The resulting boundary is
\[
\boxed{(210,2)}.
\]

### Theorem T11.90 — terminal-pair closure at order 40

For the planar orbit-total state `(6,5)` on forty vertices, both terminal points
\[
\boxed{(210,2),\qquad(212,0)}
\]
are attainable.

---

## 10. Exact order-40 Pareto front

The universal planar inequalities are
\[
B_A\ge12,
\qquad
B_O\ge0,
\qquad
B_A+B_O\ge5\cdot40+12=212.
\]

T11.57 realizes every parity-compatible point on this line with `B_O>=4` for every even `n>=16`. T11.90 supplies the missing `B_O=2,0` endpoints.

Therefore:

### Theorem T11.91 — exact planar `(6,5)` front at order 40

\[
\boxed{
\mathcal R^\Xi_{Pl,40}(6,5)
=
\{(12+2t,200-2t):0\le t\le100\}.
}
\]

Equivalently,
\[
\boxed{
Z^\Xi_{Pl,40}(6,5;X,Y)
=
\sum_{t=0}^{100}X^{12+2t}Y^{200-2t}.
}
\]

Any feasible point above the minimum-total line is componentwise dominated by one of these even lattice points. Hence this is the complete Pareto front. QED.

---

## 11. Updated exact range and next structural target

The exact planar `(6,5)` front is now proved for every even host size
\[
\boxed{4\le n\le40.}
\]

At order `42`, the triangulation complement has
\[
r=\frac{42}{2}-6=15
\]
added edges.

The fourteen-edge theorem shows that the first two-center nonextremality at `r=14` is still locally repairable. The next question should therefore not be attacked as another isolated host order. The correct structural target is:

> determine how the overload-center classification and multi-face repair scale for `r>=15`, and whether there is a finite local threshold or an inductive balancing mechanism for arbitrary triangulation complements.

The branch has now crossed another meaningful internal threshold: order `40` is closed by a universal fourteen-edge augmentation theorem rather than by a support-specific computation. It is worth continuing before packaging a publication update, because `r=15` is the first test of whether this theorem is the beginning of an induction or the end of the finite local regime.
