# HATTER-SOL-11 · ORDER_46_R17_PHASE_BOUNDARY

**Status:** closed arithmetic classification / phase-boundary layer; no order-46 closure theorem is claimed here.

Set `r=17`, corresponding to `n=46` for a 5-regular planar support.

## Lemma T11.111 — r=17 is the last automatic two-center regime

A simple graph with seventeen edges has at most two vertices of degree at least seven.

### Proof

Three such vertices have degree sum at least 21. At most three edges lie internally among them, so their incident-edge union has size at least `21-3=18>17`. QED.

At `r=18` this argument becomes sharp: three degree-seven vertices with all three mutual edges can have incident-edge union exactly `21-3=18`. Thus `r=18` is the first edge count at which a genuine three-overload-center configuration is arithmetically possible.

Hence `r=17` is the final order controlled by a zero/one/two-center decomposition alone.

## Theorem T11.112 — complete two-center arithmetic at r=17

Let `x,y` be the two overloaded vertices and write `a=d_F(x)>=b=d_F(y)>=7`.

If `xy` is not added, `a+b<=17`. The possible pairs are

`(7,7),(8,7),(9,7),(10,7),(8,8),(9,8)`,

with residual counts respectively

`3,2,1,0,1,0`.

If `xy` is added, `a+b<=18`. The possible pairs are

`(7,7),(8,7),(9,7),(10,7),(11,7),(8,8),(9,8),(10,8),(9,9)`,

with residual counts respectively

`4,3,2,1,0,2,1,0,0`.

### Proof

Without `xy`, the union of center-incident edges has size `a+b`, so the residual count is `17-a-b`.

With `xy`, the union has size `a+b-1`, so the residual count is `18-a-b`. The displayed pairs are exactly the integer solutions with `a>=b>=7`. QED.

## One-center arithmetic

For exactly one overloaded center `x`, put

`d=d_F(x)`, `q=17-d`.

Then

`7<=d<=17`, `0<=q<=10`.

The genuinely new low-center case is `(d,q)=(7,10)`.

A ten-edge off-center graph can have two degree-five hot vertices in two qualitatively different extremal forms:

1. they are nonadjacent and their ten incident edges are disjoint, covering all ten edges;
2. they are adjacent, their incident-edge union has size nine, leaving one residual edge.

Three degree-five vertices are impossible because their incident-edge union is at least `15-3=12>10`.

Thus the `r=16` two-hot mechanism survives, but the new nonadjacent-hot form means there need not be a common added edge whose deletion automatically creates slack.

## Structural consequence

Order 46 is therefore the decisive final test of the current repair architecture:

- center count is still at most two;
- the two-center table is finite;
- but the one-center `(7,10)` case introduces two disjoint degree-five hot stars with no shared added edge;
- immediately after this, at `r=18`, a third overload center becomes possible.

The next theorem target is therefore not merely another host order. It is:

**R17 LAST-TWO-CENTER BALANCING THEOREM:** determine whether the existing ear/protection machinery still balances every seventeen-edge complement, with special attention to the nonadjacent two-hot `(7,10)` configuration.

If this closes, the programme reaches a mathematically natural phase boundary before the first genuine three-center regime.