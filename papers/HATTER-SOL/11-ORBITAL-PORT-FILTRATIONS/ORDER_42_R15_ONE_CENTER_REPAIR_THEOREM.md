# HATTER-SOL-11 · ORDER_42_R15_ONE_CENTER_REPAIR_THEOREM

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer.  
**Scope:** plane-graph augmentation theorem used by the orbit-total `Xi=(A,O)` programme.

T11.94 closes every two-center pattern at `r=15`. This note closes the remaining case: exactly one vertex of the fifteen-edge augmentation has degree at least seven.

---

## 1. Setup and the hot-vertex lemma

Let `H` be a 5-regular 3-connected simple plane graph. Let `F` be the added-edge graph of a face-by-face triangulation with
\[
|F|=15.
\]
Assume exactly one vertex `x` is overloaded. Put
\[
d:=d_F(x)\ge7,
\qquad q:=15-d,
\]
and let `Q` be the `q`-edge subgraph consisting of the added edges not incident with `x`.

The five support faces incident with `x` have old `x`-loads
\[
k_1,\ldots,k_5,
\qquad \sum_i k_i=d.
\]

### Lemma T11.95 — uniqueness of an off-center hot vertex

If `q<=8`, then `Q` has at most one vertex of degree at least five.

### Proof

If distinct `u,v` both had `Q`-degree at least five, then
\[
|E(Q)|\ge d_Q(u)+d_Q(v)-\mathbf1_{uv\in Q}
\ge5+5-1=9,
\]
contradicting `q<=8`. QED.

Call this unique vertex, when it exists, the **hot vertex** `y`.

Two useful consequences are:

- if `d_Q(y)=5`, every other vertex has `Q`-degree at most `q-5+1<=4` and in the cases below in fact at most four;
- if `d_Q(y)=6`, the remaining `q-6` off-center edges give every other vertex very small residual degree.

We use T11.72 (ordinary two-incidence ear-off) and T11.77 (one protected boundary vertex) throughout.

---

## 2. Degree seven: `(d,q)=(7,8)`

Only one incidence must be removed from `x`.

If there is a loaded face `C` at `x` not containing the hot vertex `y` (or if no hot vertex exists), apply T11.72 to `C` at `x`.

Then `x` falls to degree at most six. Every other boundary vertex of `C` has outside off-center degree at most four by T11.95 and receives at most two new diagonals, so its total degree is at most six.

It remains to suppose that **every** loaded face at `x` contains `y`. Two vertices of a 3-connected plane graph lie together on at most two faces unless they are joined by a support edge, in which case the same bound is exactly two. Thus all seven old `x`-incidences lie in at most two common faces. One such face `C` has
\[
k_C\ge4.
\]

Now ear off `C` at `y`, using T11.72 with `y` as the removed vertex. The new triangulation contributes at most two incidences at `x`, while all `k_C` old `x`-diagonals in `C` disappear. Hence
\[
d'(x)\le7-k_C+2\le5.
\]
The hot vertex receives no new diagonal in `C`, so it cannot become overloaded. Every other boundary vertex has `Q`-degree at most four and receives at most two new local incidences. Thus `Delta<=6`.

So `(7,8)` is closed.

---

## 3. Degree eight: `(d,q)=(8,7)`

Some incident face `C` has
\[
k_C\ge2.
\]

If `C` does not contain the hot vertex, use T11.72 and finish: `x` loses at least two incidences, and every other affected vertex has off-center degree at most four plus at most two local incidences.

Suppose the hot vertex `y` lies on `C`. Apply T11.77 to `C`, ear-off at `x` and protect `y`.

Then
\[
d'(x)\le8-k_C\le6.
\]
If the outside-`C` off-center degree of `y` is at most five, then
\[
d'(y)\le5+1=6,
\]
and every other boundary vertex is safe: when a seven-edge graph has a degree-five vertex, at most two residual edges avoid it, so every other vertex has old off-center degree at most three, and T11.77 adds at most three.

The only remaining case is outside-`C` off-center degree six. Then six off-center edges form a star at `y`, with one residual edge.

After the protected first repair, `y` has degree at most seven. Choose a face `D` at `y` containing one of those six star edges outside `C` and ear off at `y`.

If `D` avoids `x`, both centers are immediately safe.

If `D` contains `x`, then `C,D` are the two common support faces of adjacent support vertices `x,y`. Let `k_D` be the old `x`-load in `D`. After the two repairs,
\[
d''(x)\le8-k_C-k_D+2.
\]
If this is at most six, stop. Otherwise `k_C+k_D<=3`. Since `k_C>=2`, at least five old `x`-incidences lie in the three noncommon faces at `x`; one such face `E` has load at least two.

Ear off `E` at `x`. If `E` is consecutive to one of the already repaired faces, protect their unique noncentral overlap vertex with T11.77. This lowers `x` by at least two and cannot affect `y`.

There is no noncentral overlap between the two common faces `C,D`: they intersect exactly in the support edge `xy`. The only remaining residual off-center edge contributes at most one, so all noncentral degree bounds are at most six.

Thus `(8,7)` is closed.

---

## 4. Degree nine: `(d,q)=(9,6)`

If some face `C` has
\[
k_C\ge3,
\]
repair it.

- If no hot vertex lies on `C`, use T11.72.
- If the hot vertex lies on `C`, use T11.77 protecting it.

A degree-five hot vertex remains at most six. If its outside degree is six, all six off-center edges form a star; after protection it can have degree seven. Choose a second face `D` containing a remaining star edge and ear off at the hot vertex. If `D` contains `x`, protect `x`; after the first repair `x<=6`, so the protected contribution at most one preserves the bound. Thus the star bounce terminates.

Now suppose no face has load at least three. Then the five loads are exactly
\[
\{2,2,2,2,1\}.
\]
Choose two nonconsecutive load-two faces and repair both. The hot vertex can lie on at most one of them: two common support faces are consecutive, and nonadjacent support vertices share at most one face. Protect the hot vertex on that face if necessary.

The center `x` loses four incidences and falls to degree at most five. If a degree-six hot vertex becomes degree seven after the protected repair, bounce once at a face containing a remaining star edge; protect `x` if that bounce face contains `x`. Since `x` has a full unit of reserve, it remains at most six.

Every noncentral vertex is affected by at most one of the two nonconsecutive first-stage repairs. The bounce can add at most three if protected or two if ordinary, while a six-edge star leaves no residual off-center edges. Hence no new overload is created.

Thus `(9,6)` is closed.

---

## 5. Degree ten: `(d,q)=(10,5)`

We must remove four incidences from `x`.

If one face has load at least four, repair that face. Otherwise consider the five pairs of nonconsecutive faces around `x`. Their total pair-load is
\[
2d=20,
\]
so some nonconsecutive pair has combined load at least four.

Repair a qualifying single face or nonconsecutive pair.

The only possible hot off-center graph is a five-edge star. The star center can lie on at most one face of a selected nonconsecutive pair. Protect it there with T11.77; use T11.72 on the other face.

The hot vertex remains at degree at most six (`5+1`). Every other vertex has off-center degree at most one and receives at most three local incidences. The center loses at least four and falls to at most six.

Hence `(10,5)` is closed.

---

## 6. Degrees eleven through fifteen

Here
\[
q<=4,
\]
so no hot-vertex protection is needed. The strengthened two-incidence ear-off lemma gives the same safe estimates as in the preceding orders.

### `d=11`, `q=4`

Either a face has load at least five, or a nonconsecutive face pair has combined load at least
\[
\left\lceil\frac{22}{5}\right\rceil=5.
\]
Repair it. The center falls to at most six and every affected noncentral vertex has degree at most `4+2=6`.

### `d=12`, `q=3`

The three heaviest incident faces have total load at least
\[
\left\lceil\frac{36}{5}\right\rceil=8.
\]
Repair them. Any noncentral vertex lies on at most two faces incident with `x`, so it receives at most four new local incidences; adding at most three off-center incidences is a crude bound, but with only three off-center edges any vertex of off-center degree three is unique. If such a vertex lies on two selected faces, replace one of those two local repairs by T11.77 protecting it, reducing the local contribution from `4` to at most `3`; if it lies on one selected face, ordinary T11.72 gives at most `2+3=5`. Thus every noncentral degree remains at most six.

### `d=13`, `q=2`

Repair the three heaviest faces; their total load is at least eight. A noncentral vertex receives at most four local incidences and at most two off-center incidences, hence at most six.

### `d=14`, `q=1`

The three heaviest faces have load at least nine. Repair them. Every noncentral vertex has degree at most `4+1=5`.

### `d=15`, `q=0`

The three heaviest faces have load at least nine. Repair them. The center falls to degree at most six and every other vertex receives at most four new incidences.

Thus all one-center degrees are closed.

---

## 7. Fifteen-edge one-center theorem

### Theorem T11.96 — complete one-center repair at `r=15`

Let `H` be a 5-regular 3-connected simple plane graph and let a face-by-face triangulation have added-edge graph `F` with
\[
|F|=15.
\]
If `F` has exactly one vertex of degree at least seven, then the faces of `H` can be retriangulated so that the resulting added-edge graph `F'` satisfies
\[
\boxed{|F'|=15,\qquad \Delta(F')\le6.}
\]

### Proof

Sections 2--6 cover every possible center degree `7<=d<=15`. QED.

No external existence theorem and no computation is used in T11.96.

---

## 8. Immediate combination

Together T11.94 and T11.96 imply:

### Corollary T11.96a — fifteen-edge balancing theorem

Let `H` be a 5-regular 3-connected simple plane graph whose faces require exactly fifteen added edges to triangulate. Then there exists a triangulation `T` on the same vertex set such that
\[
F=E(T)\setminus E(H)
\]
satisfies
\[
\boxed{|F|=15,\qquad \Delta(F)\le6.}
\]

Indeed an initial augmentation has zero, one, or two overloaded vertices by T11.92; the zero-center case is already balanced, T11.96 handles one center, and T11.94 handles two.