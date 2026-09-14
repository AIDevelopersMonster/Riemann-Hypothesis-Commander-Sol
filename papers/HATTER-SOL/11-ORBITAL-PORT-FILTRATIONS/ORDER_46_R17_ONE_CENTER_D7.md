# HATTER-SOL-11 · ORDER_46_R17_ONE_CENTER_D7

**Status:** closed theorem layer for the new `(d,q)=(7,10)` case.

Let `F` be a seventeen-edge face-triangulation complement of a 5-regular 3-connected simple plane support. Assume exactly one vertex `x` is overloaded and `d_F(x)=7`. Let `Q` be the ten-edge off-center graph.

A vertex of `Q` is called hot if its degree is at least five. Since `x` is the unique overloaded vertex, every hot vertex has degree at most six.

## Lemma T11.113 — hot structure in a ten-edge graph

There are at most two hot vertices.

If there are two, `u,v`, then exactly one of the following occurs:

1. `d_Q(u)=d_Q(v)=5`, `uv notin Q`, and all ten edges are incident with exactly one of `u,v`;
2. `d_Q(u)=d_Q(v)=5`, `uv in Q`, and exactly one residual edge is incident with neither hot vertex;
3. up to exchange, `d_Q(u)=6`, `d_Q(v)=5`, `uv in Q`, and every edge is incident with at least one hot vertex.

### Proof

Three hot vertices would have incident-edge union at least `15-3=12>10`.

For two hot vertices,

`d(u)+d(v)-1_{uv in Q}<=10`.

If `uv` is absent, only `(5,5)` is possible and its incident-edge union already has size ten. If `uv` is present, `d(u)+d(v)<=11`, giving `(5,5)` or `(6,5)`, with residual counts one and zero respectively. QED.

## Theorem T11.114 — repair of `(7,10)`

The support faces can be retriangulated so that the resulting seventeen-edge added graph has maximum degree at most six.

### Proof

Only one old incidence must be removed from `x`. Choose a loaded support face at `x` subject to the cases below.

### No hot vertex

Use T11.72 at `x`. Every other boundary vertex has off-center degree at most four and receives at most two new diagonals. Done.

### Exactly one hot vertex `u`

If there is a loaded face avoiding `u`, use T11.72 there. Otherwise every loaded face contains `u`. The pair `x,u` lies together on at most two support faces, so all seven old `x`-incidences are concentrated on at most two faces. One such face `C` has load at least four.

Ear off `C` at `u`. Then `u` receives no new diagonal and

`d'(x)<=7-4+2=5`.

Every other boundary vertex has `Q`-degree at most four and receives at most two new incidences. Done.

### Two hot vertices `u,v`

First suppose there is a loaded face `C` that does not contain both hot vertices.

- If it contains neither, use T11.72. In all three structures of T11.113, every nonhot vertex has off-center degree at most three, so all boundary vertices are safe.
- If it contains exactly one hot vertex of degree five, use T11.77 protecting it. The protected vertex remains at most six and every unprotected boundary vertex is safe.
- If it contains the degree-six hot vertex from Type 3, choose instead a loaded face avoiding that vertex whenever one exists. If no loaded face avoids it, all loaded faces contain it; as in the one-hot case, one common face has old `x`-load at least four. Ear off that face at the degree-six hot vertex, protecting the other hot vertex if it is also present. Then `x<=6` and both hot vertices are safe.

It remains only the concentration case in which every loaded face contains both hot vertices. The three vertices `x,u,v` can share at most two support faces through `x`; hence the seven old incidences at `x` lie on at most two faces, and one face `C` has load at least four.

Ear off `C` at one hot vertex, say `u`, and protect the other `v` using T11.77. Then

`d'(x)<=7-4+3=6`.

The ear-off hot vertex receives no new diagonal. The protected hot vertex receives at most one. If `uv` is an added edge, it lies in their unique common support face and is deleted whenever `C` is that face, creating one additional unit of slack; if `uv` is absent, both hot degrees are exactly five by T11.113, so protection alone gives at most six.

Every remaining boundary vertex has off-center degree at most three and receives at most three new local incidences. Hence all final degrees are at most six.

Thus every placement of the ten-edge hot structure is repairable. QED.

## Consequence

The new nonadjacent two-hot pattern at `r=17` is not an obstruction. The remaining one-center degrees have `q<=9`, so they fall back into the hot-structure regimes already controlled at `r=16`, with one additional total edge at the center rather than off-center.