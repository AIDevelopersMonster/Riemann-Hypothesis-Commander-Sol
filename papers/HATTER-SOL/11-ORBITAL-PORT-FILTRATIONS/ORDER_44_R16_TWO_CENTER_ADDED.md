# HATTER-SOL-11 · ORDER_44_R16_TWO_CENTER_ADDED

**Status:** closed theorem layer for all two-center cases with `xy in F`.

Let `F` be a sixteen-edge face-triangulation complement of a 5-regular 3-connected simple plane support. Let `x,y` be the two overloaded vertices and assume `xy` is an added edge.

Then `x,y` are nonadjacent in the support and share a unique support face `C`, the face containing the added diagonal `xy`. Let `R` be the residual off-center added-edge graph. By T11.101 the possible center degrees and residual sizes are

`(7,7;3), (8,7;2), (9,7;1), (10,7;0), (8,8;1), (9,8;0)`.

For a center `u in {x,y}`, let `k_u(C)` be its old added-edge load in `C`.

## 1. Common-face repair rule

Retriangulate `C` by T11.82 unless a specified noncentral boundary vertex `z` needs extra protection, in which case use T11.99. Thus both centers receive no new diagonal from `C`; every unprotected noncentral boundary vertex receives at most four new diagonals, while `z` receives at most two.

Every old added edge from `x` or `y` to another boundary vertex of `C` disappears and cannot survive in another face by the facial-intersection property.

## 2. Pattern `(7,7)` with three residual edges

The common-face repair deletes at least `xy`, so both centers fall to degree at most six.

If some boundary vertex of `C` has residual degree three, protect it with T11.99. Every other boundary vertex then has residual degree at most two and total degree at most `4+2=6`; the protected vertex has degree at most `2+3=5`.

If no residual degree-three vertex lies on `C`, T11.82 is already sufficient. Hence this pattern is closed.

## 3. Pattern `(8,7)` with two residual edges

The center `y` becomes safe after the common-face repair. If `k_x(C)>=2`, so does `x`.

Assume `k_x(C)=1`. Then `x` has degree seven after repairing `C`; its seven remaining old incidences lie on four other faces, so choose a secondary face `D` with old `x`-load at least two.

If `D` is consecutive to `C`, let `w` be their unique noncentral overlap vertex. Before repairing `C`, choose T11.99 with `z=w` whenever `w` has residual degree two; otherwise ordinary T11.82 is enough. Retriangulate `D` at `x`, using T11.97 to protect `w` when the faces are consecutive.

Then `x<=5`. At the overlap vertex the worst bound is either `2+1+2=5` or `4+1+1=6`. All other affected vertices are below six. Thus the pattern is closed.

## 4. Patterns `(9,7)` and `(10,7)`

There are respectively one and zero residual edges.

For `(9,7)`, if `k_x(C)>=3`, the common repair finishes. If `k_x(C)=2`, then `x=7` afterward and a secondary face has load at least two. If `k_x(C)=1`, then `x=8` and the remaining eight old incidences over four faces again give a secondary face of load at least two. Repair it at `x`; when consecutive to `C`, use T11.97 on the overlap. The worst overlap bound is `4+1+1=6`.

For `(10,7)`, if `k_x(C)>=4`, stop. If `k_x(C)=3` or `2`, a secondary face of load at least two finishes. If `k_x(C)=1`, the remaining nine incidences over four faces give a secondary face of load at least three, again enough. There is no residual edge, so overlap bounds are strictly smaller.

Hence both patterns are closed.

## 5. Pattern `(8,8)` with one residual edge

Apply the common-face repair. A center whose common-face load is at least two is immediately safe. If one center has load one, choose a secondary face of load at least two for it. If both have load one, choose such a secondary face for each center.

Repair each secondary face at its center. When a secondary face is consecutive to `C`, protect the unique overlap vertex by T11.97.

A noncentral vertex on `C` and one secondary face has degree at most `4+1+1=6`. A vertex on both secondary faces but not `C` has local degree at most `3+3` and no surviving center edge. If a vertex lies on all three repaired faces, choose it as the protected vertex `z` in T11.99 on `C`; then its degree is at most `2+1+1+1=5`.

Both centers fall to at most five. Thus `(8,8;1)` is closed.

## 6. Pattern `(9,8)` with no residual edge

The degree-eight center is safe after the common repair unless its common-face load is one; in that case one secondary face of load at least two finishes it.

The degree-nine center is safe if its common-face load is at least three. For load two, one secondary face of load at least two finishes; for load one, the remaining eight old incidences over four faces give a secondary face of load at least two and again finish.

If both centers need secondary repairs, use the same overlap protection as in the `(8,8)` case. With no residual edge, every triple-overlap vertex has degree at most `4+1+1=6`, so T11.99 is not even needed.

Thus `(9,8;0)` is closed.

## Theorem T11.107 — all added-center two-center cases at r=16

Every sixteen-edge augmentation with two overloaded centers joined by an added edge can be retriangulated to maximum added degree at most six.

### Proof

T11.101 gives exactly the six patterns treated in Sections 2--6. QED.