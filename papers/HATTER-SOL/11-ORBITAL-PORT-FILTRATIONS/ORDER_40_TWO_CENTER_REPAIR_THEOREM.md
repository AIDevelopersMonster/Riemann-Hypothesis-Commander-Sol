# HATTER-SOL-11 · ORDER_40_TWO_CENTER_REPAIR_THEOREM

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer.  
**Scope:** orbit-total `Xi=(A,O)` programme; the theorem itself is a plane-graph augmentation statement.

`ORDER_40_NONEXTREMAL_TWO_CENTER_PROBE.md` showed that a fourteen-edge augmentation has three distinct two-center arithmetic types and that the order-38 one-face proof cannot simply be repeated. This note closes **all** two-center types. The remaining order-40 obstruction, if any, is therefore a one-center obstruction.

---

## 1. Standing hypotheses

Let `H` be a 5-regular 3-connected simple plane graph. Let `T` be a face-by-face triangulation of `H`, and put
\[
F:=E(T)\setminus E(H),
\qquad |F|=14.
\]
Assume `F` has two vertices of degree at least seven, denoted `x,y`.

By T11.87 from `ORDER_40_NONEXTREMAL_TWO_CENTER_PROBE.md`, exactly one of the following occurs:

1. `d_F(x)=d_F(y)=7`, `xy notin F`, and every edge of `F` is incident with exactly one center;
2. `d_F(x)=d_F(y)=7`, `xy in F`, and exactly one edge is incident with neither center;
3. up to relabeling, `d_F(x)=8`, `d_F(y)=7`, `xy in F`, and every edge is incident with at least one center.

We use the already proved local tools:

- T11.72: ear off one chosen boundary vertex, giving it added degree zero and every other boundary vertex local added degree at most two;
- T11.77: ear off one chosen vertex while protecting another, giving local added degrees `0` and at most `1`, respectively, and at most `3` at every other boundary vertex;
- T11.82: if two protected boundary vertices are nonadjacent on the facial polygon, triangulate the face with local added degree zero at both and at most `4` elsewhere.

We repeatedly use the 3-connected plane-graph facts that two nonadjacent support vertices share at most one face and two adjacent support vertices share exactly the two faces incident with their support edge.

---

## 2. A bookkeeping observation

Suppose a face `C` incident with a center `x` is retriangulated and a boundary vertex `v!=x` also lies on `C`.

Then no old added edge `xv` can survive in another face:

- if `xv` is a support edge, it was never in `F`;
- if `xv` is not a support edge, a second face containing both `x,v` would contradict the facial intersection property.

Therefore after a local repair, the only old center-incidences that can remain at `v` come from the **other** center, unless that other center also lies on the repaired face.

This is the key reason the local degree estimates below do not accumulate hidden old incidences.

---

## 3. Type II: adjacent added centers `(7,7)` plus one residual edge

Assume
\[
d_F(x)=d_F(y)=7,
\qquad xy\in F,
\]
and let `e_0` be the unique edge of `F` incident with neither center.

Because `xy` is added rather than a support edge, `x,y` are nonadjacent in `H`. Hence they lie together on a unique support face `C`, the face in which the diagonal `xy` occurs.

Apply the double-ear protection T11.82 to `C`, protecting `x` and `y`.

Both centers receive zero new diagonals from `C` and each loses at least the old diagonal `xy`. Thus
\[
d_{F'}(x)\le6,
\qquad
d_{F'}(y)\le6.
\]

For any other boundary vertex `v` of `C`, no old center-edge incident with `v` survives outside `C` by Section 2. The only possible old outside incidence is the residual edge `e_0`, contributing at most one. T11.82 contributes at most four new incidences. Hence
\[
d_{F'}(v)\le1+4=5.
\]
Vertices outside `C` are unchanged and were not overloaded.

Therefore Type II is repairable to `Delta<=6`.

---

## 4. Type III: adjacent added centers `(8,7)`

Assume, after relabeling,
\[
d_F(x)=8,
\qquad d_F(y)=7,
\qquad xy\in F,
\]
and every added edge is incident with `x` or `y`.

Again `x,y` are nonadjacent in `H` and share a unique face `C` containing the added diagonal `xy`.

Let `k_x(C)` be the number of old added diagonals of `C` incident with `x`.

### Case A: `k_x(C)>=2`

Apply T11.82 to `C`.

Then
\[
d_{F'}(x)\le8-2=6,
\qquad
d_{F'}(y)\le7-1=6.
\]
Every other boundary vertex receives at most four new diagonals and has no surviving old center-incidence outside `C`. Thus the repair is complete.

### Case B: `k_x(C)=1`

The unique old `x`-diagonal of `C` is then `xy`.

First apply T11.82 to `C`. This gives
\[
d(x)=7,
\qquad d(y)\le6.
\]
The remaining seven old `x`-incidences are distributed among the other four faces at `x`, so some face `D!=C` has `x`-load at least two.

Because `C` is the unique common face of the nonadjacent support vertices `x,y`, the face `D` does not contain `y`.

Apply T11.72 to `D` at `x`. The center `x` loses at least two further incidences and hence falls to degree at most five.

For another boundary vertex `v` of `D`, at most one old edge from the other center `y` can remain, and the new triangulation of `D` contributes at most two. Thus ordinarily
\[
d(v)\le3.
\]
If `D` is consecutive with `C` around `x`, the two faces share one support edge and therefore one additional endpoint `w`. At `w`, the first repair contributes at most four and the second at most two, giving
\[
d(w)\le6.
\]
No old `y`-diagonal survives at `w`, because `w,y` already lie together on `C`.

Thus Type III is also repairable to `Delta<=6`.

---

## 5. Type I: separated added centers `(7,7)`

Now assume
\[
d_F(x)=d_F(y)=7,
\qquad xy\notin F,
\]
and every added edge is incident with **exactly one** of `x,y`.

This is the genuinely new order-40 pattern.

We distinguish the number of support faces containing both centers.

### 5.1 No common support face

Choose any loaded face `C_x` at `x` and any loaded face `C_y` at `y`. They are distinct and neither contains the other center.

Apply T11.72 to `C_x` at `x` and to `C_y` at `y`.

Both centers lose at least one incidence and hence fall to degree at most six.

A noncentral vertex lying on only one repaired face receives at most two new incidences and may retain at most one old edge from the other center, so its degree is at most three.

If a vertex lies on both repaired faces, then no old edge from either center survives outside those faces, and it receives at most
\[
2+2=4
\]
new incidences.

Hence `Delta<=6`.

### 5.2 Exactly one common support face

Then `x,y` are nonadjacent in `H`; denote their unique common face by `C`.

If both centers have a loaded face outside `C`, choose one for each and argue exactly as in Section 5.1.

So suppose, without loss of generality, that every old added edge at `x` lies in `C`. Thus `x` has seven added incidences in `C`.

Apply T11.82 to `C`, protecting both centers. The center `x` drops to degree zero.

If `y` had at least one old added incidence in `C`, then after the repair
\[
d(y)\le6
\]
and we are finished.

If `y` had no added incidence in `C`, then all seven `y`-edges lie outside `C`, so choose a loaded face `D` at `y` and apply T11.72 there.

Now `y` falls to degree at most six. The only possible overlap of `C` and `D` apart from `y` is one support neighbor when the faces are consecutive around `y`. Such a vertex receives at most four incidences from the double-ear repair and at most two from the second repair, hence at most six. Since every old `x`-edge lay in `C`, no hidden old `x`-incidence survives there.

Thus the one-common-face case is closed.

### 5.3 Two common support faces

Then `x,y` are adjacent in `H`. Let `C_1,C_2` be the two faces incident with the support edge `xy`.

If each center has a loaded noncommon face, choose such a face for each and use Section 5.1.

Assume therefore, without loss of generality, that `x` has no loaded noncommon face. Hence all seven old `x`-incidences lie in `C_1 union C_2`. One of these two faces, say `C_1`, has `x`-load at least four.

Apply the protected ear-off lemma T11.77 to `C_1`, ear-off at `x` and protect `y`.

Then
\[
d(x)\le7-4=3.
\]
Let `h` be the old `y`-load in `C_1`. After the first repair,
\[
d(y)\le7-h+1=8-h.
\]

- If `h>=2`, then `d(y)<=6` and the repair is complete.
- If `h=1`, then `y` has degree at most seven and still has six old incidences distributed over its remaining faces. Choose any remaining loaded face `D` and apply T11.72 at `y`; one removed incidence is enough.
- If `h=0`, then `y` has degree at most eight and all seven old `y`-incidences lie outside `C_1`. Among the remaining four faces at `y`, one has load at least two. Choose such a face `D` and apply T11.72 at `y`; at least two incidences are removed.

If `D` is a noncommon face, it does not contain `x`. If `D=C_2`, then the second repair may create at most two new incidences at `x`; since the first repair left `x` with degree at most three, this still gives at most five. Moreover retriangulating `C_2` removes any old `x`-diagonals in that face before adding the at-most-two new ones.

For noncentral vertices, the first repair contributes at most three and the second at most two. If the two repaired faces meet at a noncentral vertex, the total new contribution is at most five. Old center-incidences outside the relevant repaired face are excluded by the facial intersection property.

Hence the adjacent-support case is also repaired to maximum degree at most six.

---

## 6. Fourteen-edge two-center theorem

### Theorem T11.88 — complete two-center repair at `r=14`

Let `H` be a 5-regular 3-connected simple plane graph, and let a face-by-face triangulation have added-edge graph `F` with
\[
|F|=14.
\]
If `F` has two vertices of degree at least seven, then the faces of `H` can be retriangulated so that the resulting added-edge graph `F'` satisfies
\[
\boxed{|F'|=14,\qquad \Delta(F')\le6.}
\]

### Proof

T11.87 gives the exhaustive Types I--III. Sections 3--5 construct the required retriangulation in each type. QED.

---

## 7. Consequence for the order-40 programme

The nonextremal two-center phenomenon is **not** an obstruction.

At order `40`, if an arbitrary fourteen-edge triangulation complement is bad, the only case still requiring proof is:

\[
\boxed{\text{exactly one vertex has added degree }\ge7.}
\]

Thus the order-40 problem has been reduced to a strengthened one-center theorem for fourteen added edges. The difficult low-overload patterns are
\[
(d,q)=(7,7),(8,6),(9,5),
\]
where `q=14-d` is the number of off-center edges.

No existence theorem is used in T11.88; it is an internal local theorem about any 5-regular 3-connected plane support satisfying the stated augmentation hypothesis.
