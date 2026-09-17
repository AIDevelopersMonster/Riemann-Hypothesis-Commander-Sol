# HATTER-SOL-11 · ORDER_46_R17_ONE_CENTER_D8

**Status:** closed theorem layer for `(d,q)=(8,9)`.

Let `F` be a seventeen-edge face-triangulation complement of a 5-regular 3-connected simple plane support. Assume `x` is the unique overloaded vertex and

`d_F(x)=8`.

Let `Q` be the nine off-center edges. A vertex of `Q` is hot if its `Q`-degree is at least five.

## Lemma T11.115 — nine-edge hot structure

There are at most two hot vertices. If there are two, then both have degree five, they are adjacent in `Q`, and every edge of `Q` is incident with at least one of them.

If there is exactly one hot vertex `u`, then `d_Q(u)` is five or six and every other vertex has degree at most four.

### Proof

The first assertion is the nine-edge equality case

`5+5-1=9`.

Three hot vertices would require at least `15-3=12` edges. Since `x` is the unique overloaded vertex of `F`, every vertex of `Q` has degree at most six. QED.

## Theorem T11.116 — repair of `(8,9)`

The faces can be retriangulated so that the resulting seventeen-edge added graph has maximum degree at most six.

### Proof

The five old `x`-loads sum to eight, so some incident face `C` has load at least two.

### Two hot vertices `u,v`

By T11.115 both have degree five, `uv` is an added edge, and every nonhot vertex has `Q`-degree at most two.

Choose any load-at-least-two face `C`.

- If `C` contains neither hot vertex, apply T11.72 at `x`.
- If it contains exactly one hot vertex, apply T11.77 at `x` protecting that vertex.
- If it contains both, then `C` is the unique support face containing the added edge `uv`. Retriangulating `C` deletes `uv`; both hot vertices then have outside degree at most four. Apply T11.72 at `x`.

In every subcase `x` loses at least two old incidences and falls to degree at most six. The local bounds are respectively `2`, `1/3`, and `2`; combined with the displayed `Q`-degree bounds they never exceed six.

### Exactly one hot vertex `u` of degree five

If a load-at-least-two face avoids `u`, use T11.72 there. Every other boundary vertex has `Q`-degree at most four, so the final bound is `4+2=6`.

Assume every load-at-least-two face contains `u`. At most two support faces contain both `x,u`; every other face has `x`-load at most one. Hence the common faces carry at least five of the eight old `x`-incidences, so one common face `C` has load at least three.

If `C` has load at least four, ear off `C` at `u`; then

`d'(x)<=8-4+2=6`.

If `C` has load exactly three, the other common face has load at least two. Therefore `x,u` are support-adjacent. Apply T11.97 to `C` with ear vertex `u` and protected adjacent vertex `x`. Then `u` receives no new diagonal and `x` receives at most one, so

`d'(x)<=8-3+1=6`.

All other boundary vertices receive at most two new diagonals and have `Q`-degree at most four.

### Exactly one hot vertex `u` of degree six

Again, a load-at-least-two face avoiding `u` is handled by T11.72; every nonhot vertex has `Q`-degree at most four.

Assume all load-at-least-two faces contain `u`. As above, one common face `C` has load at least three.

If its load is at least four, ear off at `u` and obtain `x<=6`.

If its load is exactly three, the second common face has load at least two, so `x,u` are support-adjacent. Apply T11.97 to `C`, now ear-off at `u` and protect `x`. This gives

`d'(x)<=8-3+1=6`,

while `u` receives zero new diagonals and therefore remains at most six. Every other vertex receives at most two new diagonals; since only three `Q`-edges avoid the degree-six hot center, every nonhot vertex has degree at most four.

Thus all cases are repaired to `Delta<=6`. QED.

## Consequence

The first post-`(7,10)` case is also not an obstruction. What fails at `r=17` is not the theorem so far, but the possibility of proving the remaining cases by a blind one-edge shift from the `r=16` arguments.