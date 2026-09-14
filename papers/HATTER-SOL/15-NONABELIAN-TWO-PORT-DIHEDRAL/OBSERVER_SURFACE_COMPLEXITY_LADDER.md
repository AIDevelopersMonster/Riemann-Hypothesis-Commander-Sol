# HATTER-SOL-15 · Observer-Surface Complexity Ladder

**Status:** exact theorem layer

Let

\[
X=\mathbb F_p,
\qquad
R(i)=i+1,
\qquad
S(i)=-i,
\]

with `p` an odd prime. For

\[
w_j=R^jS
\]

we have

\[
w_j(i)=-(i+j).
\]

Hence the signed displacement of the endpoint relative to the start along the oriented `R`-cycle is

\[
\Delta_j(i):=w_j(i)-i=-2i-j\pmod p.
\]

This single formula gives three observer regimes.

## 1. Closure-only observer

The weakest observer records only

\[
C_j(i)=\mathbf1_{\{\Delta_j(i)=0\}}.
\]

By H15.4, exact sector identification requires exactly

\[
\boxed{p-1}
\]

nontrivial closure probes in the worst case.

## 2. Unoriented metric observer

Now retain the cyclic graph metric of the `R`-cycle but forget its orientation. Define

\[
M_j(i):=d_{C_p}(i,w_j(i))
       =\|\Delta_j(i)\|_p,
\]

where

\[
\|x\|_p:=\min(\bar x,p-\bar x)
\]

for the representative `0<=bar x<p`.

Put

\[
x=-2i\in\mathbb F_p.
\]

Then

\[
M_j(i)=d_{C_p}(x,j).
\]

### Theorem H15.5 — two metric probes resolve all sectors

The map

\[
i\longmapsto (M_0(i),M_1(i))
\]

is injective. Thus the two short words

\[
S,\qquad RS
\]

identify every sector using only unoriented cyclic distances.

### Proof

Because multiplication by `-2` is a bijection of `F_p`, it is enough to show that the distance pair

\[
x\mapsto(d_{C_p}(x,0),d_{C_p}(x,1))
\]

resolves the odd cycle `C_p`.

If `d(x,0)=0`, then `x=0`. Otherwise write

\[
d(x,0)=m,
\qquad
1\le m\le(p-1)/2.
\]

The only two candidates are `x=m` and `x=-m`. Their distances to `1` are different: along the odd cycle one candidate is one step closer to the landmark `1` than the reflected candidate (including the endpoint case `m=(p-1)/2`). Hence the pair distinguishes the sign and therefore determines `x`, and then `i=-x/2`. QED.

### Theorem H15.6 — one metric probe is insufficient

For every fixed `j`, the map `i -> M_j(i)` is not injective for `p>=3`.

### Proof

For every nonzero distance `m<= (p-1)/2`, there are exactly two vertices of the cycle at distance `m` from `j`. Since `i -> -2i` is bijective, the same two-fold ambiguity occurs among sectors. QED.

Therefore the exact metric-probe complexity is

\[
\boxed{2}.
\]

## 3. Oriented displacement observer

Finally let the surface retain the orientation/coordinate of the `R`-cycle, so the observer can record the signed displacement

\[
D_j(i)=\Delta_j(i)\in\mathbb F_p.
\]

### Theorem H15.7 — one oriented probe resolves all sectors

Already

\[
D_0(i)=-2i
\]

is injective. Hence the single port word `S` identifies the sector:

\[
\boxed{i=-\frac12D_0(i)}.
\]

Thus the exact oriented-displacement probe complexity is

\[
\boxed{1}.
\]

## 4. Observer-surface ladder

For the same world and the same two ports,

\[
\boxed{
\mathsf C_{closure}=p-1,
\qquad
\mathsf C_{metric}=2,
\qquad
\mathsf C_{oriented}=1.
}
\]

The gain comes entirely from what the carrier/surface allows the observer to retain:

- incidence/closure only;
- cyclic metric but no orientation;
- oriented cyclic displacement.

No change of arithmetic world is needed.

## 5. Claim boundary

The metric and oriented observers use additional carrier structure attached to the chosen rotation port `R`. This structure is not an intrinsic invariant of the abstract degree-`p` number field by itself. It is a marked-Schreier-carrier observable.

Accordingly H15 must distinguish:

\[
\text{arithmetic world}
\quad / \quad
\text{marked carrier geometry}
\quad / \quad
\text{observer strength}.
\]

The theorem is precisely useful because it quantifies how those layers interact rather than conflating them.