# HATTER-SOL-12 · TOROIDAL GEOMETRY-CLASS LIFT

**Status:** exact theorem layer / hostile-audit repair

## 1. Scope

Fix `n=12` and let `Tor_12` denote the class of connected simple graphs on twelve vertices that admit an embedding in the torus. For positive channel weights `(a,o)`, let `U_C(A,O;a,o)` be the maximum weighted number of used typed edges

\[
a e_A+o e_O
\]

over feasible connected simple-support networks on carriers in class `C`, with uniform node capacities `(A,O)`.

Every simple toroidal graph on twelve vertices satisfies the standard Euler bound

\[
|E|\le 3n=36.
\]

The channel capacities also give

\[
e_A\le \frac{nA}{2}=6A,
\qquad
e_O\le \frac{nO}{2}=6O.
\]

Hence every toroidal realization satisfies

\[
\boxed{
e_A+e_O\le36,
\qquad e_A\le6A,
\qquad e_O\le6O.}
\]

## 2. Extremal host

Let `T_12` be the triangular torus on

\[
V=\mathbb Z_3\times\mathbb Z_4
\]

with edge directions

\[
\pm e_1,
\qquad\pm e_2,
\qquad\pm(e_1+e_2).
\]

It is simple, 6-regular and has 36 edges. The three undirected direction classes are pairwise edge-disjoint 2-factors with twelve edges each.

Inside the `e_2` factor choose the perfect matching

\[
M=\{(i,0)(i,1),(i,2)(i,3):i\in\mathbb Z_3\}.
\]

Thus `|M|=6`.

The union of the `e_1` and `e_1+e_2` direction factors is connected: their step vectors generate all of `Z_3 x Z_4`, since their difference is `e_2`. Therefore the `(4,1)` saturation construction below satisfies the connected-network requirement.

## 3. Exact toroidal weighted optima

Consider the four split states of the `61^6` laboratory.

### Gaussian `(6,5)`

The universal constraints are

\[
e_A\le36,
\qquad e_O\le30,
\qquad e_A+e_O\le36.
\]

Hence

\[
U_{Tor}(6,5)=
\begin{cases}
36a,&a\ge o,\\
6a+30o,&o\ge a.
\end{cases}
\]

The first branch is attained on `T_12` by typing every edge `A`; the second by typing `M` as `A` and all remaining 30 edges as `O`.

### Eisenstein `(5,4)`

Now

\[
e_A\le30,
\qquad e_O\le24,
\qquad e_A+e_O\le36.
\]

Therefore

\[
U_{Tor}(5,4)=
\begin{cases}
30a+6o,&a\ge o,\\
12a+24o,&o\ge a.
\end{cases}
\]

For the first branch use `M` as the six `O` edges and the other 30 edges as `A`. For the second, use two complete direction 2-factors as the 24 `O` edges and the remaining direction factor as the 12 `A` edges.

### State `(7,1)`

Here

\[
e_A\le42,
\qquad e_O\le6,
\qquad e_A+e_O\le36.
\]

Thus

\[
U_{Tor}(7,1)=
\begin{cases}
36a,&a\ge o,\\
30a+6o,&o\ge a.
\end{cases}
\]

Both bounds are attained on `T_12` by the all-`A` assignment or by the matching/complement assignment.

### State `(4,1)`

The channel bounds themselves give

\[
e_A\le24,
\qquad e_O\le6,
\]

so at most 30 edges can be used and, for positive weights,

\[
U_{Tor}(4,1)\le24a+6o.
\]

Equality is attained by taking `M` as `O` and the two connected-generating direction factors `e_1` and `e_1+e_2` as the 24 `A` edges. Hence

\[
U_{Tor}(4,1)=24a+6o.
\]

## 4. Geometry-class lifting theorem

### Theorem TG12.1

For each of the four states

\[
(6,5),\quad(5,4),\quad(7,1),\quad(4,1),
\]

the explicit host `T_12` attains the universal weighted upper bound over the entire class `Tor_12`.

Therefore the weighted response formulas previously derived on `T_12` are the exact weighted response formulas of the full twelve-vertex simple toroidal carrier class.

### Proof

The displayed upper bounds use only the universal toroidal edge bound `e<=36` and the two channel-incidence bounds. The explicit assignments on `T_12` attain the corresponding linear-program optimum in every weight regime. Since every construction has connected union, no admissible toroidal carrier can improve the value. QED.

## 5. Consequence for the `61^6` resolving theorem

After subtracting the already exact strict-path optima and normalizing by `a` with `r=o/a`, the toroidal signatures are genuinely geometry-class signatures:

\[
F_{-4}^{Tor}(r)=
\begin{cases}50,&r\le1,\\12+38r,&r\ge1,\end{cases}
\]

\[
F_{-3}^{Tor}(r)=
\begin{cases}38+12r,&r\le1,\\24+26r,&r\ge1,\end{cases}
\]

\[
F_{-19}^{Tor}(r)=50,
\]

\[
F_{-163}^{Tor}(r)=
\begin{cases}26+12r,&r\le1,\\38,&r\ge1.\end{cases}
\]

Consequently the statements

\[
D_{Tor}(r)=3,2,4
\]

in the three regimes `r<1`, `r=1`, `r>1`, and

\[
\operatorname{tdim}_{Tor}=1
\]

hold for the full twelve-vertex simple toroidal carrier class, not merely for one witness host.