# HATTER-SOL-11 · Exact `(6,5)` Closure at Planar Order 44

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the orbit-total `Xi=(A,O)` model.

## 1. Sixteen-edge balancing theorem

### Theorem T11.109

Let `H` be a 5-regular 3-connected simple plane graph whose faces require exactly sixteen added edges to triangulate. Then there exists a face-by-face triangulation `T` such that

`F=E(T)\E(H)`

satisfies

`|F|=16` and `Delta(F)<=6`.

### Proof

Start with any face triangulation.

- If no vertex of `F` has degree at least seven, stop.
- T11.100 shows that there are at most two overloaded vertices.
- If there is exactly one, apply T11.106.
- If there are two and their joining edge is added, apply T11.107.
- If there are two and their joining edge is not added, apply T11.108.

Thus a balanced triangulation always exists. QED.

No external existence theorem and no computation enters T11.109.

## 2. External support existence at order 44

For a planar 5-regular graph on `n` vertices,

`|E|=5n/2`, `f=3n/2+2`.

At `n=44`,

`|E|=110`, `f=68`.

We use the same external existence input already separated at orders 40 and 42: there are 5-connected 5-regular planar graphs with `f` faces for `f=20` and every `f>=26` satisfying `f=2 mod 3` (Brandenburg 2023, citing Hasheminezhad--McKay--Reeves).

Since `68>=26` and `68=2 mod 3`, fix such a support `H_44`.

A triangulation on 44 vertices has `3*44-6=126` edges, so the triangulation complement has exactly

`126-110=16`

edges.

## 3. Terminal endpoint `B_O=0`

Apply T11.109 to `H_44`. Put the 110 support edges in the capacity-five channel and the sixteen added edges in the capacity-six channel.

Then

`B_O=5*44-2*110=0`,

`B_A=6*44-2*16=232`.

Therefore

`(232,0)`

is attained.

## 4. Endpoint `B_O=2`

Let `S={v:d_F(v)=6}`. Since the degree sum of the sixteen-edge added graph is 32,

`|S|<=5`.

At most `5|S|<=25` support edges are incident with `S`, while `H_44` has 110 support edges. Hence there exists a support edge `e` whose endpoints both lie outside `S`.

Move `e` from the capacity-five channel to the capacity-six channel. Then the capacity-six maximum degree remains at most six and the capacity-five maximum degree remains at most five. The boundary becomes

`(230,2)`.

## 5. Exact front at order 44

T11.57 supplies the universal terminal segment for every even `n>=16` at `B_O>=4`. Sections 3 and 4 supply the two missing endpoints.

### Theorem T11.110

For `n=44`,

`R^Xi_Pl,44(6,5) = {(12+2t, 220-2t): 0<=t<=110}`.

Equivalently, the exact planar `(6,5)` Pareto front is the full parity segment from `(12,220)` to `(232,0)`.

Hence the exact even-order range now extends through

`4<=n<=44`.

The statement remains strictly in the orbit-total quotient `Xi=(A,O)` and is not an upgrade to full `Omega` semantics.