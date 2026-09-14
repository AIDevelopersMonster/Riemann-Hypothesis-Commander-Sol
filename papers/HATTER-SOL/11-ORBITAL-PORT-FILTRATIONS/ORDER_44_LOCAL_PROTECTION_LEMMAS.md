# HATTER-SOL-11 · ORDER_44_LOCAL_PROTECTION_LEMMAS

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed local theorem layer.

The `r=16` step first needs two polygon facts slightly stronger than T11.77 and T11.82.

## Lemma T11.97 — adjacent-protected two-incidence ear-off

Let `C` be a polygonal face, let `x` be a boundary vertex, and let `y` be one of the two boundary neighbors of `x`. Then `C` has a triangulation such that

- `x` is incident with no added diagonal;
- `y` is incident with at most one added diagonal;
- every other boundary vertex is incident with at most two added diagonals.

### Proof

Let `y,z` be the two boundary neighbors of `x`. Add the diagonal `yz`, cutting off the ear `xyz`. Triangulate the remaining polygon by an alternating zig-zag oriented so that `y` is the zero-incidence end and `z` receives at most one zig-zag diagonal. Thus `y` receives only `yz`, while `z` receives `yz` plus at most one further diagonal. Every other vertex receives at most two zig-zag diagonals. QED.

## Lemma T11.98 — one ear with two protected vertices

Let `C` be a polygonal face, let `x` be a boundary vertex, and let `p,q` be two further boundary vertices. Then `C` admits a triangulation such that

- `d_add(x)=0`;
- `d_add(p)<=1`;
- `d_add(q)<=2`;
- every other boundary vertex has added degree at most four.

### Proof

Let `a,b` be the neighbors of `x`. Add `ab` and remove the ear at `x`. In the remaining polygon, cut off `p` as an ear. Finally triangulate the last polygon by a zig-zag chosen so that `q` is a zero-incidence zig-zag ear. Vertex `p` receives at most the first ear diagonal `ab` if it coincides with `a` or `b`, hence at most one. Vertex `q` can be hit by at most the two ear diagonals and by no zig-zag diagonal, hence at most two. Every other vertex can be hit by at most two ear diagonals and at most two zig-zag diagonals, hence at most four. QED.

## Lemma T11.99 — double-ear protection with one residual-hot vertex

Let `C` be a polygonal face. Let `x,y` be two nonadjacent boundary vertices and let `z` be a third boundary vertex. Then `C` has a triangulation such that

- `d_add(x)=d_add(y)=0`;
- `d_add(z)<=2`;
- every other boundary vertex has added degree at most four.

### Proof

Cut off `x` as an ear, then cut off `y` as an ear. Nonadjacency ensures that the first ear diagonal is not incident with `y`. Triangulate the remaining polygon by a zig-zag in which `z` is a zero-incidence ear. The vertex `z` can receive only the two ear diagonals, while every other unprotected vertex receives at most those two ear diagonals plus two zig-zag diagonals. QED.

These lemmas are purely local. Their use inside a simple plane graph relies, as before, on the 3-connected facial-cycle intersection property so that the chosen facial diagonals are not already support edges drawn elsewhere.