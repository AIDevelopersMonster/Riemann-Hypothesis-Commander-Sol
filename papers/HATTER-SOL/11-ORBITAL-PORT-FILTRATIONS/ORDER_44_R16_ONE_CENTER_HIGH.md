# HATTER-SOL-11 · ORDER_44_R16_ONE_CENTER_HIGH

**Status:** closed theorem layer for one-center degrees `13<=d<=16`.

Let `F` be a sixteen-edge face-triangulation complement of a 5-regular 3-connected simple plane support. Assume exactly one vertex `x` is overloaded. Put `d=d_F(x)` and `q=16-d`.

## T11.105a — degree 13, q=3

Repair the three incident faces of largest old `x`-load. Their total load is at least

`ceil(3*13/5)=8`,

which exceeds the seven incidences that must be removed.

A noncentral vertex can lie on at most two selected faces. If two selected faces are consecutive around `x`, they share exactly one noncentral support neighbor. Among any three selected faces in the cyclic order of five faces, the adjacency graph is a forest. Orient each adjacency edge toward one of its incident selected faces so that every selected face receives at most one assigned overlap vertex.

On a selected face with an assigned overlap vertex, use T11.97: ear off at `x` and protect that overlap vertex. Use T11.72 on any remaining selected face.

Thus a noncentral vertex lying on two selected consecutive faces receives local added degree at most `1+2=3`; a vertex lying on only one selected face receives at most two. Since `Q` has only three edges, its degree contribution is at most three. Therefore every noncentral final degree is at most six, while `x` loses at least eight incidences and falls to at most five.

So `(13,3)` is closed.

## T11.105b — degree 14, q=2

Repair the three heaviest incident faces. Their total load is at least

`ceil(3*14/5)=9`,

which is at least the required eight.

Every noncentral vertex lies on at most two selected faces and therefore receives at most four new local incidences. Since the off-center graph has only two edges, its old degree at any vertex is at most two. Hence every noncentral final degree is at most six. The center falls to at most five.

So `(14,2)` is closed.

## T11.105c — degree 15, q=1

The three heaviest incident faces have total load at least

`ceil(45/5)=9`,

exactly the amount required to reduce the center to degree at most six. A noncentral vertex receives at most four new local incidences and at most one off-center incidence, hence final degree at most five.

So `(15,1)` is closed.

## T11.105d — degree 16, q=0

The three heaviest incident faces have total load at least

`ceil(48/5)=10`,

exactly the amount required to reduce the center to degree six. Every noncentral vertex receives at most four new local incidences.

So `(16,0)` is closed.

## Theorem T11.106 — complete one-center repair at r=16

Let `H` be a 5-regular 3-connected simple plane graph and let a face-by-face triangulation have added-edge graph `F` with `|F|=16`. If `F` has exactly one vertex of degree at least seven, then the faces can be retriangulated so that the resulting added graph has maximum degree at most six.

### Proof

T11.103 handles `d=7`; `ORDER_44_R16_ONE_CENTER_LOW.md` handles `8<=d<=12`; Sections T11.105a--d above handle `13<=d<=16`. QED.

No external existence theorem and no computation is used in T11.106.