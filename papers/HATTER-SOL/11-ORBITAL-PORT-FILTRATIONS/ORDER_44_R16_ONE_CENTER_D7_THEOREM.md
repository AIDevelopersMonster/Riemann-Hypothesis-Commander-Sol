# HATTER-SOL-11 · ORDER_44_R16_ONE_CENTER_D7_THEOREM

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the new `r=16` low-center case.

Let `H` be a 5-regular 3-connected simple plane graph. Let `F` be the added-edge graph of a face-by-face triangulation with `|F|=16`. Assume exactly one vertex `x` is overloaded and

`d_F(x)=7`.

Let `Q` be the nine-edge graph of added edges not incident with `x`.

## Lemma T11.102 — at most two degree-five vertices in `Q`

There are at most two vertices of `Q` having degree at least five. If there are two, say `u,v`, then

`d_Q(u)=d_Q(v)=5`, `uv in Q`,

and every edge of `Q` is incident with at least one of `u,v`.

### Proof

Three degree-five vertices have degree sum at least fifteen and at most three internal edges, so their incident-edge union has size at least `15-3=12>9`.

For two vertices,

`d_Q(u)+d_Q(v)-1_{uv in Q}<=9`.

If both degrees are at least five, equality is forced throughout: both degrees are five, `uv` is present, and their incident-edge union is all nine edges. QED.

## Theorem T11.103 — the `(d,q)=(7,9)` repair

Under the standing hypotheses, the support faces can be retriangulated so that the resulting sixteen-edge added graph has maximum degree at most six.

### Proof

Only one old incidence must be removed from `x`. Choose any support face `C` incident with `x` whose old `x`-load is positive.

Call a vertex of `Q` hot if its degree is at least five.

### No hot vertex on `C`

Apply T11.72 at `x`. Then `x` loses at least one incidence and falls to degree at most six. Every other boundary vertex has `Q`-degree at most four and receives at most two new diagonals, hence has final degree at most six.

### Exactly one hot vertex `u` on `C`

Apply T11.77 at `x`, protecting `u`.

The center `x` again falls to at most six. The protected vertex receives at most one new diagonal.

If `u` is the only hot vertex, then `d_Q(u)<=6` because a degree-seven vertex of `Q` would be a second overloaded vertex of `F`. Any old `Q`-edge lying inside `C` is deleted before retriangulation, so the outside-`C` degree of `u` is at most six and is in fact at most five whenever `C` contains one of its old diagonals. Thus `u` has final degree at most six after protection.

For every other boundary vertex, if `d_Q(u)>=5`, at most four of the nine edges avoid `u`; including a possible edge to `u`, its `Q`-degree is at most five, and the only way to reach five would create a second hot vertex. Hence every unprotected boundary vertex has `Q`-degree at most four and T11.77's local bound at most three is safe except at degree four. If a degree-four boundary vertex occurs, use Lemma T11.97 when it is a boundary neighbor of `x`; otherwise orient the protected zig-zag so that this unique degree-four vertex is the low-incidence end. It then receives at most two new incidences. Thus the bound remains six.

### Two hot vertices `u,v`

By T11.102 they both have degree five, `uv` is an added edge, and every edge of `Q` meets `u` or `v`.

Because `uv` is added, `u,v` are nonadjacent in the support and therefore lie together on a unique support face, namely the face containing the diagonal `uv`.

If `C` contains neither hot vertex, T11.72 is safe: every boundary vertex has `Q`-degree at most two.

If `C` contains exactly one hot vertex, use T11.77 protecting it. Every other boundary vertex has `Q`-degree at most two, so the local bound three is harmless, while the protected hot vertex has degree at most `5+1=6`.

If `C` contains both hot vertices, then `C` is their unique common support face and contains the old diagonal `uv`. Retriangulating `C` deletes `uv`, so each hot vertex has outside-`C` `Q`-degree at most four. Apply the ordinary T11.72 at `x`. Every boundary vertex, including `u,v`, then has final degree at most

`4+2=6`.

Thus every possible placement of the hot structure admits a repair with `Delta<=6`. QED.

## Consequence

The new two-hot phenomenon at nine off-center edges is not an order-44 obstruction. The remaining one-center degrees at `r=16` are `8<=d<=16`; for `d>=8` the off-center graph has at most eight edges and therefore at most one degree-five hot vertex, returning to the single-hot regime of T11.95.