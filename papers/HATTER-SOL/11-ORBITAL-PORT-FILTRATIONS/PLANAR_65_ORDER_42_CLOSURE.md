# HATTER-SOL-11 · Exact `(6,5)` Closure at Planar Order 42

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the orbit-total `Xi` model.

**Scope.** Throughout,
\[
\Omega=(a;\{b,c\})\mapsto\Xi=(A,O)=(a,b+c)
\]
is the orbit-total quotient. No statement below upgrades the result to full `Omega` semantics.

The preceding two theorem layers proved a universal fifteen-edge triangulation-complement balancing theorem. Order `42` is therefore no longer a special repair problem; only the external existence of one suitable planar quintic support remains to be supplied.

---

## 1. External support existence

For a planar 5-regular graph on `n` vertices,
\[
|E|=\frac{5n}{2},
\qquad
f=2+|E|-n=\frac{3n}{2}+2.
\]
At
\[
n=42,
\]
we have
\[
\boxed{f=65.}
\]

We use the same **external** classical existence input as in the order-40 layer:

> 5-connected 5-regular planar graphs exist for `f=20` and for every `f>=26` satisfying `f congruent 2 (mod 3)`.

A published route is Franz J. Brandenburg, *On Optimal Beyond-Planar Graphs*, Computing in Geometry and Topology 2(1), 2023, DOI `10.57717/cgt.v2i1.10`, which quotes the quintic-planar existence range while citing Hasheminezhad--McKay--Reeves.

Since
\[
65\ge26,
\qquad
65\equiv2\pmod3,
\]
there exists a 5-connected 5-regular plane graph `H_42`.

This support existence is external. Everything in the balancing theorem itself is internal to HATTER-SOL-11.

For `H_42`,
\[
|E(H_{42})|=\frac{5\cdot42}{2}=105.
\]
A triangulation on the same vertex set has
\[
3\cdot42-6=120
\]
edges, so every face-by-face triangulation adds exactly
\[
\boxed{15}
\]
edges.

---

## 2. Universal fifteen-edge balancing input

T11.92 showed that a fifteen-edge simple graph has at most two vertices of degree at least seven.

T11.94 proved that every two-center fifteen-edge triangulation complement of a 5-regular 3-connected simple plane support can be retriangulated to maximum added degree at most six.

T11.96 proved the corresponding one-center theorem.

Therefore Corollary T11.96a gives:

\[
\boxed{
|F|=15
\Longrightarrow
\text{there is a face-by-face triangulation with }\Delta(F)\le6.
}
\]

Apply this to `H_42` and obtain a triangulation `T_42` with
\[
F:=E(T_{42})\setminus E(H_{42}),
\qquad
|F|=15,
\qquad
\Delta(F)\le6.
\]

---

## 3. Terminal endpoint `B_O=0`

For the orbit-total state
\[
\Xi=(6,5),
\]
color every edge of `H_42` by the capacity-five channel and every edge of `F` by the capacity-six channel.

Both degree bounds hold:
\[
\Delta(H_{42})=5,
\qquad
\Delta(F)\le6.
\]

Hence
\[
B_O
=5\cdot42-2\cdot105
=0,
\]
and
\[
B_A
=6\cdot42-2\cdot15
=222.
\]
Thus
\[
\boxed{(222,0)}
\]
is attained.

---

## 4. One-edge recoloring and `B_O=2`

Let
\[
S:=\{v:d_F(v)=6\}.
\]
Since
\[
\sum_vd_F(v)=30,
\]
we have
\[
|S|\le5.
\]

The support `H_42` has `105` edges. At most
\[
5|S|\le25
\]
support edges are incident with `S`. Hence there exists a support edge
\[
e\in E(H_{42})
\]
whose endpoints both lie outside `S`.

Move `e` from the capacity-five channel to the capacity-six channel. Then
\[
\Delta(F\cup\{e\})\le6,
\qquad
\Delta(H_{42}-e)\le5.
\]
The resulting boundary is
\[
\boxed{(220,2)}.
\]

### Theorem T11.97 — terminal-pair closure at order 42

For the planar orbit-total state `(6,5)` on `42` vertices, both terminal minimum-total points
\[
\boxed{(220,2),\qquad(222,0)}
\]
are attainable.

---

## 5. Exact full order-42 front

For every even host in state `(6,5)`,
\[
B_A\ge12,
\qquad
B_O\ge0,
\qquad
B_A+B_O\ge5n+12.
\]
At `n=42`, the minimum-total line is
\[
B_A+B_O=222.
\]

T11.57 from `PLANAR_65_TERMINAL_TAIL_16_24.md` realizes every parity-compatible point on this line with
\[
B_O\ge4.
\]
T11.97 supplies the two missing levels `B_O=2,0`.

Therefore:

### Theorem T11.98 — exact planar `(6,5)` front at order 42

\[
\boxed{
\mathcal R^\Xi_{Pl,42}(6,5)
=
\{(12+2t,210-2t):0\le t\le105\}.
}
\]

Equivalently,
\[
\boxed{
Z^\Xi_{Pl,42}(6,5;X,Y)
=
\sum_{t=0}^{105}X^{12+2t}Y^{210-2t}.
}
\]

Any feasible point strictly above the minimum-total line is componentwise dominated by a displayed parity-compatible point. Hence there are no other Pareto-minimal responses. QED.

---

## 6. Updated exact range

Combining the preceding theorem layers with T11.98,
\[
\boxed{
\mathcal R^\Xi_{Pl,n}(6,5)
=
\{(12+2t,5n-2t):0\le t\le5n/2\}
}
\]
is now proved for every even
\[
\boxed{4\le n\le42.}
\]

The next host is
\[
\boxed{n=44,}
\]
with triangulation-complement size
\[
r=\frac{44}{2}-6=16.
\]

The main structural question is no longer order 42 itself. It is whether the `r=14,15` repair architecture continues for `r=16`, or whether a qualitatively new multi-center interaction first appears there.