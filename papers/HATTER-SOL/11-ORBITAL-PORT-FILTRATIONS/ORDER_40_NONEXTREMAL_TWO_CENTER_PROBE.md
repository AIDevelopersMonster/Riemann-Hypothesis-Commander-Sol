# HATTER-SOL-11 · ORDER_40_NONEXTREMAL_TWO_CENTER_PROBE

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Scope:** orbit-total quotient only,
\[
\Omega=(a;\{b,c\})\mapsto\Xi=(A,O)=(a,b+c).
\]
**Status:** closed hostile-audit / overload-classification layer. This note does **not** yet claim the order-40 endpoint theorem.

The branch head before this probe was commit `2fa5bca02593db755b1add00cca73e6c7656644f`, closing order `38`.

The first order-40 question is whether the thirteen-edge two-center argument can simply be continued to fourteen added edges. It cannot: the arithmetic classification changes qualitatively at `|F|=14`.

---

## 1. Hostile audit of the theorem layers through order 38

The following files were re-read before attempting order `40`:

- `PLANAR_CAPACITY_FIVE_FLOOR.md`;
- `PLANAR_65_TERMINAL_TAIL_16_24.md`;
- `PLANAR_65_ORDER_26_CLOSURE.md`;
- `PLANAR_65_ORDER_28_CLOSURE.md`;
- `PLANAR_65_ORDERS_30_32_CLOSURE.md`;
- `PLANAR_65_ORDER_34_CLOSURE.md`;
- `PLANAR_65_ORDER_36_CLOSURE.md`;
- `PLANAR_65_ORDER_38_TWO_CENTER_CLOSURE.md`;

with the earlier supporting layers

- `PLANAR_UNIT_TAIL_THEOREM.md`;
- `PLANAR_LOW_TAIL_B_MATCHING_THEOREM.md`;
- `PLANAR_PLATONIC_THRESHOLD_THEOREM.md`;
- `PLANAR_CRITICAL_CAPACITY_HOSTILE_PROBE.md`.

### Audit verdict

No mathematical failure was found in the closed range `4<=n<=38`, but two hypotheses that were sometimes implicit should be made explicit in future uses.

### 1.1 Strengthened ear-off lemma

T11.72 is valid. After cutting off `x` by the diagonal joining its two facial neighbors, the remaining polygon can be triangulated by the alternating zig-zag

\[
p_0p_{m-2},\ p_1p_{m-2},\ p_1p_{m-3},\ p_2p_{m-3},\ldots
\]

whose diagonal graph is a path. One endpoint of the remaining polygon can be chosen to receive no zig-zag diagonal and the other receives at most one. Restoring the first ear diagonal gives the advertised bound `2` on every unprotected boundary vertex and `0` at `x`.

**Ambient qualification.** As a polygon statement this is purely combinatorial. When it is used to augment a *simple plane graph*, the proposed polygon diagonals must not already be edges of the support drawn on the other side of the facial cycle. In every application from order `26` onward the support is 3-connected, and the polyhedral face-intersection property rules out such facial chords. Thus the actual applications are sound.

### 1.2 Protected ear-off lemma

T11.77 is valid. The point needing explicit justification is that an arbitrary protected boundary vertex `y` of the remaining polygon can be chosen as one of the zero-diagonal ears of a zig-zag triangulation. Rotate the standard alternating-ear construction so that `y` is an isolated vertex of the zig-zag diagonal graph. Then `y` receives only the first ear diagonal if it is one of the two neighbors of `x`, and otherwise receives none. Hence the stated protected bound `<=1` is correct.

Again, the ambient simple-graph use relies on chordlessness of a facial cycle, supplied by 3-connectivity.

### 1.3 Double-ear protection

T11.82 is valid for two **nonadjacent** protected vertices. Cutting off the first protected vertex does not create a diagonal incident with the second; after removing the first ear, the second may also be cut off. A final zig-zag gives at most two further incidences, so every unprotected vertex receives at most four added diagonals.

The nonadjacency condition is essential. Two adjacent boundary vertices of a nontriangular polygon cannot in general both be forced to added degree zero: already in a quadrilateral every triangulation diagonal meets one of the two adjacent protected vertices.

### 1.4 Face-intersection property

The uses of facial intersection in T11.68--T11.84 are legitimate. For a 3-connected simple plane graph:

- facial boundaries are simple cycles;
- two distinct faces meet in `empty`, one vertex, or one edge;
- two nonconsecutive faces around a fixed vertex have no other common vertex;
- two nonadjacent support vertices lie together on at most one face;
- if two vertices lie on a chosen face, an added diagonal joining them cannot occur in a second face.

These are exactly the facts required to bound old added incidences outside a repaired face.

### 1.5 One-center and two-center overload arguments through `r=13`

The concentration bound
\[
d_F(u)+d_F(v)-\mathbf 1_{uv\in E(F)}\le |F|
\]
is used correctly.

For `|F|<=12`, there is at most one vertex of degree at least seven. For `|F|=13`, two overloaded vertices force
\[
d_F(x)=d_F(y)=7,\qquad xy\in E(F),
\]
and every added edge is incident with at least one center. Therefore the order-38 common-face double-ear repair is genuinely justified at `r=13`.

### 1.6 No hidden “P fills first” assumption

No closed proof in the audited chain requires a maximal-first or “fill the `P` channel before `Q`” rule. The constructions explicitly choose two edge-disjoint channel subgraphs and verify both degree bounds. `P>=Q` is used only as a symmetry convention when naming a folded fiber.

### 1.7 Quotient scope

All audited terminal-tail statements are about the orbit-total quotient
\[
\Xi=(A,O),
\]
not about the full orbital datum `Omega`. Nothing in the order-40 argument below upgrades the semantics beyond `Xi`.

### 1.8 External existence input

The mathematical repair theorems are internal. Existence of suitable 5-connected 5-regular planar supports is an external input.

Hasheminezhad--McKay--Reeves (JGAA 15(3), 2011, DOI `10.7155/jgaa.00232`) explicitly enumerate connectivity classes only through order `36` in Table 1. Therefore Table 1 itself must **not** be cited as an order-38 or order-40 witness.

A later published route is Franz J. Brandenburg, *On Optimal Beyond-Planar Graphs*, whose existence theorem states, citing Hasheminezhad--McKay--Reeves, that 5-connected 5-regular planar graphs with `f` faces exist for
\[
f=20\quad\text{or}\quad f\ge26,\ f\equiv2\pmod3.
\]
For a 5-regular planar graph on `n` vertices,
\[
f=\frac{3n}{2}+2.
\]
Thus `n=38` gives `f=59` and `n=40` gives `f=62`, both in the external existence range. This existence statement remains external to HATTER-SOL-11 and is not part of the repair proof.

---

## 2. Fourteen-edge overload arithmetic

Let `F` be a simple graph with
\[
|E(F)|=14.
\]
Call `v` overloaded if
\[
d_F(v)\ge7.
\]

### Lemma T11.86 — at most two overload centers at `r=14`

`F` has at most two overloaded vertices.

### Proof

If three vertices were overloaded, their degree sum would be at least `21`. At most three edges lie internally among the three vertices, so the number of distinct edges incident with at least one of them is at least
\[
21-3=18>14,
\]
a contradiction. QED.

---

## 3. Complete two-center classification at `r=14`

Suppose `F` has two overloaded vertices `x,y`. Put
\[
a=d_F(x),\qquad b=d_F(y),\qquad a\ge b\ge7.
\]
For the union of their incident edge sets,
\[
a+b-\mathbf1_{xy\in E(F)}\le14.
\]

### Theorem T11.87 — order-40 two-center arithmetic trichotomy

Exactly one of the following arithmetic patterns occurs.

#### Type I — separated `(7,7)`
\[
\boxed{a=b=7,\qquad xy\notin E(F).}
\]
Then
\[
a+b=14,
\]
so **every** edge of `F` is incident with exactly one of the two centers. There is no off-center edge, but there is also no center-center added edge.

#### Type II — adjacent `(7,7)` plus one residual edge
\[
\boxed{a=b=7,\qquad xy\in E(F).}
\]
The union of the two incident edge sets has size
\[
7+7-1=13,
\]
so exactly one edge of `F` is incident with neither center.

#### Type III — adjacent `(8,7)`
Up to exchanging the names of the centers,
\[
\boxed{a=8,\qquad b=7,\qquad xy\in E(F).}
\]
Then
\[
8+7-1=14,
\]
so every edge of `F` is incident with at least one center.

No other degree pair is possible.

### Proof

If `xy` is absent, then `a+b<=14`; because `a,b>=7`, equality forces `(7,7)`.

If `xy` is present, then `a+b<=15`; with `a,b>=7`, the only possibilities are `(7,7)`, `(8,7)`, and its transpose. The residual-edge counts follow from the size of the union of the two incident edge sets. QED.

---

## 4. The naive order-38 extension is false

At `r=13`, two overload centers were forced to satisfy `xy in F`. This immediately placed the two centers on the unique original face containing the added diagonal `xy`, and one double-ear retriangulation could reduce both degrees.

At `r=14` this inference fails.

An abstract simple-graph witness is
\[
F=K_{1,7}(x; a_1,\ldots,a_7)\;\sqcup\;K_{1,7}(y;b_1,\ldots,b_7).
\]
It has fourteen edges and
\[
d_F(x)=d_F(y)=7,
\qquad
xy\notin E(F).
\]

This witness is **not** asserted to be a triangulation complement of a particular 5-regular plane support. Its role is narrower and rigorous: it disproves the arithmetic claim that two overload centers in a fourteen-edge augmentation must be adjacent in `F` or must be carried by one common added-edge face.

Therefore the naive universal theorem

> “the order-38 two-center proof extends verbatim to `r=14` by repairing the unique face containing `xy`”

is false.

This does **not** disprove the stronger desired statement

> every fourteen-edge face-triangulation augmentation of a 5-regular 3-connected plane graph can be retriangulated to `Delta(F)<=6`.

That stronger statement remains open after the present probe.

---

## 5. Geometric consequences of the trichotomy

The three arithmetic types have different facial geometry.

### Types II and III

Because `xy` is an added edge, `x,y` are nonadjacent in the original support. In a 3-connected plane graph they lie together on a unique original face `C`, the face containing the diagonal `xy`.

- Type II can potentially be repaired on `C` exactly as at order `38`, because both centers need to lose only one incidence; the single residual off-center edge leaves ample slack.
- Type III is already different: the degree-eight center must lose at least two incidences. Removing only `xy` can leave degree seven. Thus even when a common face exists, a second repair face may be required.

### Type I

There is no added edge `xy`. Hence the overload arithmetic alone says nothing about whether the centers share an original face.

They may be:

- adjacent in the support, in which case they share the two faces incident with the original edge `xy`;
- nonadjacent but cofacial, in which case 3-connectivity allows at most one common face;
- noncofacial.

So any order-40 theorem must allow genuinely multi-face repair.

---

## 6. One-center patterns at order 40

If there is only one overloaded vertex `x`, let
\[
d=d_F(x),\qquad q=14-d.
\]
Then
\[
\boxed{7\le d\le14,\qquad 0\le q\le7.}
\]

The first new one-center difficulty relative to order `38` is `d=7,q=7`: the ordinary two-incidence ear-off estimate can see `7+2`, so the off-center graph must be used structurally rather than only through its edge count.

The key favorable fact is that, in a genuine one-center configuration, the `q=7` off-center graph cannot itself have degree seven; otherwise there would be a second overload center. Hence its maximum degree is at most six, and there is at most one vertex of degree at least five in any `q<=7` off-center graph. This sharply limits the number of vertices that may need protection during a repair.

---

## 7. Next proof target

The hostile probe therefore leaves a precise target rather than a vague order-40 case split.

To prove the universal fourteen-edge augmentation theorem it is enough to establish:

1. a one-center repair for `d=7,8,9` with `q=7,6,5`, using at most one protected off-center concentration;
2. a Type-III `(8,7)` repair using the common `xy` face plus, if necessary, one additional face at the degree-eight center;
3. a Type-I separated `(7,7)` **two-face repair theorem**, with special handling when the centers are adjacent in the original support and both loads are concentrated on their two common faces.

The old order-38 one-face mechanism is therefore dead as a universal template, but the stronger multi-face theorem is still structurally plausible.
