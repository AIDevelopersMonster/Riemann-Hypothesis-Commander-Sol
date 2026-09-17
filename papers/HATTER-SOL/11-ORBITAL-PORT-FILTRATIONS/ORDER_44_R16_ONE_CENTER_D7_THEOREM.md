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

Only one old incidence must be removed from `x`. Call a vertex of `Q` **hot** if its `Q`-degree is at least five.

### Case A — no hot vertex

Choose any loaded face `C` at `x` and apply T11.72 at `x`.

The center loses at least one incidence and therefore falls to degree at most six. Every other boundary vertex has `Q`-degree at most four and receives at most two new diagonals, so its final added degree is at most six.

### Case B — exactly one hot vertex `u`

Because `x` is the unique overloaded vertex of `F`,

`5<=d_Q(u)<=6`.

If some loaded face `C` at `x` does **not** contain `u`, apply T11.72 to that face. Every boundary vertex of `C` has `Q`-degree at most four, so the repair is immediately safe.

Assume therefore that every loaded face at `x` contains `u`.

Two vertices of a 3-connected simple plane graph lie together on at most two support faces: one if they are nonadjacent, exactly two if they are adjacent. Hence all seven old `x`-incidences lie in at most two common faces of `x,u`. One such face `C` has old `x`-load

`k_C>=4`.

Retriangulate `C` by T11.72 **at `u`**, not at `x`.

The hot vertex `u` receives no new diagonal. All `k_C` old `x`-diagonals in `C` disappear, while the new triangulation contributes at most two diagonals at `x`. Therefore

`d'(x)<=7-k_C+2<=5`.

Every other boundary vertex has `Q`-degree at most four and receives at most two new diagonals, hence remains at degree at most six. Thus the repair is complete.

### Case C — two hot vertices `u,v`

By T11.102,

`d_Q(u)=d_Q(v)=5`, `uv in Q`,

and every edge of `Q` is incident with `u` or `v`.

Because `uv` is an added edge, `u,v` are nonadjacent in the support and therefore share a unique support face, namely the face containing the diagonal `uv`.

Choose any loaded face `C` at `x`.

#### C1. `C` contains neither hot vertex

Apply T11.72 at `x`. Every boundary vertex has `Q`-degree at most two, so the local bound two is harmless.

#### C2. `C` contains exactly one hot vertex, say `u`

Apply T11.77 at `x`, protecting `u`.

The protected vertex has degree at most `5+1=6`. Every other boundary vertex has `Q`-degree at most two, because all nine edges of `Q` are covered by the two hot centers, so the local bound three is safe. The center `x` loses at least one old incidence and falls to degree at most six.

#### C3. `C` contains both hot vertices

Then `C` is the unique common support face of `u,v` and contains the old diagonal `uv`.

Retriangulating `C` deletes `uv`, so each hot vertex has outside-`C` `Q`-degree at most four. Apply T11.72 at `x`. Each boundary vertex, including `u,v`, then has final added degree at most

`4+2=6`.

Thus every possible hot configuration admits a repair with `Delta<=6`. QED.

## Consequence

The new two-hot phenomenon at nine off-center edges is not an order-44 obstruction. The remaining one-center degrees at `r=16` are `8<=d<=16`; for `d>=8`, the off-center graph has at most eight edges and therefore at most one degree-five hot vertex, returning to the single-hot regime of T11.95.