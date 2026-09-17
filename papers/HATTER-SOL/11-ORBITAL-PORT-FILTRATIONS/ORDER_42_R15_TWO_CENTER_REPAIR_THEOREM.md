# HATTER-SOL-11 · ORDER_42_R15_TWO_CENTER_REPAIR_THEOREM

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer.  
**Scope:** plane-graph augmentation theorem used by the orbit-total `Xi=(A,O)` programme.

`ORDER_42_R15_OVERLOAD_CLASSIFICATION.md` classified all two-center degree patterns for a fifteen-edge augmentation. This note closes all six patterns geometrically.

---

## 1. Standing hypotheses and local tools

Let `H` be a 5-regular 3-connected simple plane graph. Let `T` be a face-by-face triangulation of `H`, and let
\[
F:=E(T)\setminus E(H),
\qquad |F|=15.
\]
Assume `F` has two overloaded vertices `x,y`, meaning
\[
d_F(x),d_F(y)\ge7.
\]

By T11.93, up to exchanging `x,y`, exactly one of the following occurs:

1. `(7,7)`, `xy notin F`, one residual edge;
2. `(8,7)`, `xy notin F`, no residual edge;
3. `(7,7)`, `xy in F`, two residual edges;
4. `(8,7)`, `xy in F`, one residual edge;
5. `(9,7)`, `xy in F`, no residual edge;
6. `(8,8)`, `xy in F`, no residual edge.

We use three already proved polygon tools:

- **T11.72:** ear off one chosen boundary vertex; it receives no new diagonal and every other boundary vertex receives at most two;
- **T11.77:** ear off one chosen boundary vertex while protecting a second boundary vertex; the first receives `0`, the protected vertex at most `1`, and every other boundary vertex at most `3`;
- **T11.82:** if two protected boundary vertices are nonadjacent on the facial polygon, they can both receive `0`, while every other boundary vertex receives at most `4`.

We also use the standard 3-connected plane-graph intersection facts:

- two nonadjacent support vertices share at most one face;
- two adjacent support vertices share exactly the two faces incident with their support edge;
- two nonconsecutive faces around a vertex have no other common vertex;
- two distinct facial cycles meet in at most one vertex or one edge.

A repeated bookkeeping rule is crucial: if a repaired face contains a center `x` and another boundary vertex `v`, then no old added edge `xv` survives in another face. If `xv` is a support edge it was never added; otherwise a second common face would contradict 3-connectivity.

---

## 2. The four patterns with `xy in F`

If `xy` is added, then `x,y` are nonadjacent in the support `H`. Hence there is a unique support face `C` containing both centers, namely the face in which the added diagonal `xy` occurs.

### 2.1 Pattern `(7,7)` with two residual edges

Apply T11.82 to `C`, protecting both centers.

Both centers lose at least the old diagonal `xy`, so
\[
d(x),d(y)\le6.
\]
Every other boundary vertex of `C` has no surviving old added edge to either center outside `C`. The only old incidences that may remain are the two residual edges. Thus
\[
d(v)\le4+2=6.
\]
Vertices outside `C` were not overloaded. Hence this pattern is repaired.

### 2.2 Pattern `(8,7)` with one residual edge

Let `k_x(C)` be the old `x`-load in `C`.

If `k_x(C)>=2`, apply T11.82 to `C`. Then
\[
d(x)\le8-2=6,
\qquad d(y)\le7-1=6,
\]
and every other boundary vertex has degree at most `4+1=5`.

Assume therefore
\[
k_x(C)=1.
\]
After applying T11.82 to `C`,
\[
d(x)=7,
\qquad d(y)\le6.
\]
The seven remaining old incidences at `x` lie on the other four faces at `x`; hence one such face `D` has old `x`-load at least two.

The face `D` does not contain `y`, because `C` is the unique common face of the nonadjacent support vertices `x,y`.

If `D` is nonconsecutive to `C` around `x`, apply T11.72 to `D` at `x`.

If `D` is consecutive to `C`, the two faces share the support edge `xw` for one noncentral vertex `w`. Apply T11.77 to `D`, ear-off at `x` and protect `w`.

Then `x` loses at least two further old incidences and falls to degree at most five. At the only possible noncentral overlap vertex,
\[
4+1+1=6,
\]
where the terms are: at most four from the repaired common face, at most one from the protected secondary repair, and at most one from the residual edge. Every other affected vertex is strictly below six. Thus the pattern is repaired.

### 2.3 Pattern `(9,7)` with no residual edge

Again use the unique common face `C`.

If
\[
k_x(C)\ge3,
\]
T11.82 on `C` finishes immediately.

If `k_x(C)=2`, the common-face repair leaves `x` of degree at most seven; if `k_x(C)=1`, it leaves `x` of degree at most eight. In either case the remaining old `x`-load on the other four faces is respectively at least seven or eight, so some secondary face `D` has load at least two.

Retriangulate `D` at `x`. If `D` is consecutive to `C`, protect their unique noncentral overlap vertex with T11.77; otherwise use T11.72.

The common-face contribution at an overlap vertex is at most four and the protected secondary contribution at most one, so the overlap degree is at most five. There is no residual edge. The center `x` falls to at most six and `y` was already reduced to at most six by the common-face repair.

Hence `(9,7)` is repaired.

### 2.4 Pattern `(8,8)` — the genuine three-face case

Let
\[
k_x(C),k_y(C)
\]
be the old center loads in the common face `C`.

Apply T11.82 to `C`.

If both loads are at least two, both centers immediately fall to at most six.

Suppose exactly one load is one, say
\[
k_x(C)=1,
\qquad k_y(C)\ge2.
\]
Then `y` is already safe while `x` has degree seven. Its remaining seven old incidences lie on four faces, so choose a secondary face `D_x` of load at least two. Retriangulate `D_x` at `x`, protecting its unique possible noncentral overlap with `C` if the two faces are consecutive. Then `x<=5`, and every overlap vertex has degree at most
\[
4+1=5.
\]

It remains to treat
\[
k_x(C)=k_y(C)=1.
\]
After the common-face repair both centers have degree seven.

Choose a secondary face `D_x` at `x` with old `x`-load at least two and a secondary face `D_y` at `y` with old `y`-load at least two. Neither secondary face contains the opposite center, because `C` is the unique common face.

For `D_x`, if it is consecutive to `C`, protect the unique noncentral overlap vertex with `C`; otherwise use ordinary ear-off. Do the analogous operation on `D_y`.

Then both centers lose at least two further incidences and fall to degree at most five.

We now audit every possible noncentral overlap.

- A vertex on `C` only has local added degree at most four.
- A vertex on `C` and exactly one secondary face is protected on that secondary face, hence has degree at most `4+1=5`.
- A vertex on both secondary faces but not on `C` receives at most `3+3=6`.
- A vertex lying on all three repaired faces is necessarily the protected overlap vertex for each secondary face, hence receives at most
  \[
  4+1+1=6.
  \]
- A vertex on one secondary face only may retain at most one old edge from the opposite center; its new local contribution is at most three, so its total is at most four.

There are no residual edges. Therefore the `(8,8)` pattern is repaired to maximum degree six.

---

## 3. The two patterns with `xy notin F`

Now the centers are not joined by an added edge. They may share zero, one, or two support faces, but the proof below avoids a separate common-face count.

### 3.1 Pattern `(7,7)` with one residual edge

First repair `x` with one unit of reserve.

Because seven incidences are distributed over five incident faces, some face `C` has old `x`-load at least two. Retriangulate `C` at `x`.

- If `C` contains `y`, use T11.77 and protect `y`.
- Otherwise use T11.72.

Then
\[
d(x)\le7-2=5.
\]
All noncentral vertices remain safe: on a face not containing `y`, the bound is
\[
2+1+1=4
\]
(new local contribution, at most one old `y`-edge, and the unique residual edge); on a face containing `y`, the protected triangulation gives at most three at every unprotected vertex and no old `y`-edge can survive outside that face, so the bound is again at most four.

The degree of `y` after this first repair is at most eight: only a protected common face can increase its local contribution, and then by at most one.

If `d(y)<=6`, stop. If `d(y)=7`, choose any loaded face `D`; if `d(y)=8`, choose a face `D` with current `y`-load at least two. Such a face exists by pigeonhole.

Retriangulate `D` at `y`.

- If `D` contains `x`, protect `x` with T11.77. Since `d(x)<=5`, this keeps `d(x)<=6`.
- Otherwise use T11.72.

The center `y` falls to at most six.

For a noncentral vertex lying on both repaired faces `C,D`, the two local contributions are at most five in total. Indeed, the only way both local bounds could be `3` is for both faces to contain both centers; if the centers are support-adjacent, their two common faces meet only in the support edge `xy`, so no noncentral vertex lies in both. Adding the single residual incidence gives at most six.

Thus the `(7,7)` nonadded pattern is repaired.

### 3.2 Pattern `(8,7)` with no residual edge

We again create one unit of reserve at `x`.

If some incident face has `x`-load at least three, repair that face. Otherwise every face has load at most two. Since the five loads sum to eight, at least three faces have load two, and therefore two load-two faces are nonconsecutive around `x`. Repair such a nonconsecutive pair.

If one selected face contains `y`, protect `y` there. Because two common support faces of adjacent vertices are consecutive, and nonadjacent support vertices share at most one face, at most one selected nonconsecutive face can contain `y`.

The selected faces remove at least three old `x`-incidences, so
\[
d(x)\le5.
\]
They have no noncentral overlap with each other. Every noncentral affected vertex has degree at most three after this phase.

Again `y` has degree at most eight. Repair it exactly as in Section 3.1: one loaded face if its degree is seven, or a face of load at least two if its degree is eight. Protect `x` if the selected `y`-face contains `x`.

A noncentral vertex lies on at most one first-phase face, because those faces were nonconsecutive at `x`. Its first-phase contribution is at most three and its second-phase contribution at most three. The simultaneous value `3+3` cannot occur at a noncentral vertex on two distinct common faces of support-adjacent centers, since those common faces intersect only in `x,y`; in all other overlaps the sum is at most five. There is no residual edge.

Hence `(8,7)` is repaired.

---

## 4. Complete fifteen-edge two-center theorem

### Theorem T11.94 — complete two-center repair at `r=15`

Let `H` be a 5-regular 3-connected simple plane graph, and let a face-by-face triangulation have added-edge graph `F` with
\[
|F|=15.
\]
If `F` has two vertices of degree at least seven, then the faces of `H` can be retriangulated so that the resulting added-edge graph `F'` satisfies
\[
\boxed{|F'|=15,\qquad \Delta(F')\le6.}
\]

### Proof

T11.93 gives the exhaustive six-pattern classification. Sections 2 and 3 construct an explicit repair for each pattern. QED.

No external existence theorem and no computation is used in T11.94.

---

## 5. Consequence for order 42

The difficult `(8,8)` configuration is therefore not an obstruction. If a fifteen-edge triangulation complement is bad, the only remaining possibility is
\[
\boxed{\text{exactly one overloaded vertex}.}
\]
The next theorem layer must close the one-center degrees
\[
7\le d\le15,
\qquad q=15-d,
\]
with the new low-overload cases `(7,8)`, `(8,7)`, `(9,6)` and the new overlap-sensitive case `(12,3)`.