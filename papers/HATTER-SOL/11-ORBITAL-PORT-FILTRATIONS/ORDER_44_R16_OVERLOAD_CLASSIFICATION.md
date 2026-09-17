# HATTER-SOL-11 · ORDER_44_R16_OVERLOAD_CLASSIFICATION

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed arithmetic classification layer.

Let `F` be a simple graph with `|E(F)|=16`. Call a vertex overloaded if its degree is at least seven.

## Lemma T11.100 — at most two overload centers

`F` has at most two overloaded vertices.

### Proof

Three overloaded vertices have degree sum at least `21`. At most three edges are internal to the triple, so at least `21-3=18>16` distinct graph edges would be incident with the triple. Contradiction. QED.

## Theorem T11.101 — complete two-center arithmetic at `r=16`

Let `x,y` be the two overloaded vertices and put

`a=d_F(x)>=b=d_F(y)>=7`.

Then

`a+b-1_{xy in F}<=16`.

Up to exchanging `x,y`, the only possibilities are:

### `xy notin F`

1. `(7,7)` with `2` residual edges;
2. `(8,7)` with `1` residual edge;
3. `(9,7)` with `0` residual edges;
4. `(8,8)` with `0` residual edges.

### `xy in F`

5. `(7,7)` with `3` residual edges;
6. `(8,7)` with `2` residual edges;
7. `(9,7)` with `1` residual edge;
8. `(10,7)` with `0` residual edges;
9. `(8,8)` with `1` residual edge;
10. `(9,8)` with `0` residual edges.

Here a residual edge means an added edge incident with neither overload center.

### Proof

If `xy` is absent, `a+b<=16`, leaving exactly the four displayed pairs. The residual count is `16-a-b`.

If `xy` is present, `a+b<=17`, leaving exactly the six displayed pairs. The residual count is `16-(a+b-1)`. QED.

## One-center arithmetic

If there is exactly one overloaded center `x`, write

`d=d_F(x)` and `q=16-d`.

Then

`7<=d<=16`, `0<=q<=9`.

The genuinely new low-center patterns are

`(d,q)=(7,9),(8,8),(9,7),(10,6)`.

For `q=9`, the off-center graph can contain two vertices of degree five. If it does, they must be adjacent and all nine off-center edges are incident with at least one of them: indeed `5+5-1=9`. This extremal structure is useful rather than harmful, because their common added edge is deleted whenever their common support face is retriangulated.

The geometric target is therefore finite and explicit: repair the ten two-center patterns above and then the one-center range `7<=d<=16`.