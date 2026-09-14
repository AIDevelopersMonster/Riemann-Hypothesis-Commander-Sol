# HATTER-SOL-11 · ORDER_42_R15_OVERLOAD_CLASSIFICATION

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed classification/probe layer; no order-42 closure theorem is claimed here.

The fourteen-edge theorem T11.89 closes order `40`. To test whether the method is inductive, move immediately to
\[
r=15,
\]
which corresponds to order
\[
n=42.
\]

The purpose of this note is to classify the overload arithmetic before attempting geometry. This is the first required step for any honest induction.

---

## 1. At most two overload centers still

Let `F` be a simple graph with fifteen edges. Call a vertex overloaded if its degree is at least seven.

### Lemma T11.92

`F` has at most two overloaded vertices.

### Proof

Three overloaded vertices have degree sum at least `21`. At most three edges are internal to the triple, so at least
\[
21-3=18>15
\]
distinct edges would be incident with the triple. Contradiction. QED.

Thus the center-count part of the `r=14` theory survives unchanged at `r=15`.

---

## 2. Complete two-center arithmetic at `r=15`

Let `x,y` be the two overloaded vertices and put
\[
a=d_F(x)\ge b=d_F(y)\ge7.
\]
Then
\[
a+b-\mathbf 1_{xy\in F}\le15.
\]

### Theorem T11.93 — fifteen-edge two-center classification

Up to exchanging `x,y`, the only possible degree/adjacency patterns are the following.

### Nonadjacent in `F`

If `xy notin F`, then `a+b<=15`, so:

1. `(a,b)=(7,7)`, with exactly one residual edge incident with neither center;
2. `(a,b)=(8,7)`, with no residual edge.

### Adjacent in `F`

If `xy in F`, then `a+b<=16`, so:

3. `(7,7)`, with two residual off-center edges;
4. `(8,7)`, with one residual off-center edge;
5. `(9,7)`, with no residual edge;
6. `(8,8)`, with no residual edge.

No other pair is possible.

### Proof

If `xy` is absent, the union of the two incident edge sets has size `a+b`; subtracting from fifteen gives the residual count.

If `xy` is present, the union has size `a+b-1`; again subtract from fifteen. The inequality `a+b<=16` and lower bounds `a,b>=7` leave exactly the four displayed adjacent pairs. QED.

---

## 3. What is genuinely new relative to `r=14`

The `r=14` trichotomy had only
\[
(7,7)_{nonadj},
\quad
(7,7)_{adj},
\quad
(8,7)_{adj}.
\]

At `r=15` three new patterns appear:

\[
\boxed{
(8,7)_{nonadj},
\qquad
(9,7)_{adj},
\qquad
(8,8)_{adj}.
}
\]

The last one is structurally the most important. If `xy` is an added edge and both centers have degree eight, a double-ear repair of their common face need not finish the job: if that face contained only the diagonal `xy` at each center, both degrees fall only from eight to seven. Thus a genuine **common-face plus two secondary-face** repair can be required.

This is the first configuration in the programme in which both centers may simultaneously need a second repair after their common face has been removed.

---

## 4. First geometric check on the `(8,8)` pattern

Suppose
\[
d_F(x)=d_F(y)=8,
\qquad xy\in F,
\]
with no residual edge.

Because `xy` is added, `x,y` are nonadjacent in the support and share a unique original face `C`.

If the old `x`-load and `y`-load in `C` are both at least two, T11.82 immediately lowers both centers to at most six.

The hostile subcase is therefore
\[
k_x(C)=k_y(C)=1.
\]
After double-ear protection of `C`, both centers have degree seven.

Each center then has seven remaining old incidences distributed over four other incident faces, so each has a secondary face of load at least two.

Thus the arithmetic itself supplies enough removable load to finish both centers. The only unresolved issue is **overlap protection**: a noncentral boundary vertex may lie on `C` and also on one secondary face at each center, so the crude local estimate
\[
4+2+2=8
\]
is too large.

However this does not yet produce a counterexample. Such an overlap vertex is geometrically special: it must be the support neighbor through which the corresponding secondary face is consecutive to `C`. The protected ear-off lemma can reduce each secondary contribution at that chosen overlap vertex from `2` to at most `1`, giving the target bound
\[
4+1+1=6.
\]

This is a **repair blueprint**, not yet promoted to a theorem because the simultaneous choice of secondary faces and protected overlap vertices must be audited across all six patterns of T11.93.

---

## 5. One-center arithmetic at `r=15`

If there is exactly one overloaded center `x`, write
\[
d=d_F(x),
\qquad q=15-d.
\]
Then
\[
7\le d\le15,
\qquad
0\le q\le8.
\]

The new low-degree cases are
\[
(d,q)=(7,8),(8,7),(9,6).
\]
The off-center graph cannot itself contain a degree-seven vertex, because that would create a second overload center. Thus in the unique-center regime
\[
\boxed{\Delta(Q)\le6.}
\]

As at `r=14`, a vertex of off-center degree five or six is unique whenever it occurs in the small `q<=8` graph. Hence a one-protected-face repair remains plausible; the first issue is again not arithmetic but whether an exceptional protected vertex can force a secondary repair that feeds back into the original center.

---

## 6. Structural conclusion

No arithmetic counterexample appears at `r=15`.

The repair mechanism has changed in a controlled way:

- center count remains at most two;
- residual off-center edges remain at most two in every two-center pattern;
- the genuinely new object is the adjacent-added `(8,8)` pattern, requiring potentially three repaired faces (`C`, one secondary face at `x`, one at `y`);
- T11.77 appears exactly strong enough to protect the possible triple-overlap boundary vertex.

Therefore the next theorem target is sharply defined:

> **R15 MULTI-PROTECTED TWO-CENTER REPAIR:** prove that all six patterns in T11.93 can be repaired with `Delta<=6`, with special attention to `(8,8)` and to a vertex lying simultaneously on the common face and both secondary repaired faces.

If that theorem closes, the remaining one-center `r=15` cases should be attacked with the same hot-star bounce mechanism used in T11.89. Only after both parts are proved should order `42` be declared closed.
