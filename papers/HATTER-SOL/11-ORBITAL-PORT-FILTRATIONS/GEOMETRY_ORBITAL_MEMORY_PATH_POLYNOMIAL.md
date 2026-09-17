# HATTER-SOL-11 · Geometry-Dependent Orbital Memory: Exact 1D Polynomial Law

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer; first exact bridge from HATTER-SOL-08 geometry classes to HATTER-SOL-11 orbital forgetting.

This note uses the response-polynomial language of HATTER-SOL-09 only where it compresses the exact Pareto data. No geometry Laplacian is introduced: the dimensional classes are currently a nested family, not yet a canonically generated world graph.

---

## 1. Orbital response polynomial

For an admissible geometry class `C`, a uniform orbital capacity state

\[
\Xi=(A,O),
\]

and a fixed host size `k`, let

\[
\mathcal R^{\mathrm{orb}}_{C,k}(A,O)
\subseteq\mathbb N^2
\]

be the Pareto-minimal boundary set in axial/oblique coordinates.

Define

\[
\boxed{
Z^{\mathrm{orb}}_{C,k}(A,O;X,Y)
:=
\sum_{(B_A,B_O)\in\mathcal R^{\mathrm{orb}}_{C,k}(A,O)}
X^{B_A}Y^{B_O}.
}
\]

This is the direct orbital analogue of the HATTER-SOL-09 typed response polynomial.

Two orbital states have the same full Pareto response iff their response polynomials are equal.

The scalar free boundary is recovered from the support by

\[
\lambda^{\mathrm{orb}}_{C,k}(A,O)
=
\min\{a+b:[X^aY^b]Z^{\mathrm{orb}}_{C,k}\ne0\}.
\]

For later anisotropy diagnostics one may also write

\[
\widetilde Z^{\mathrm{orb}}_{C,k}(u,v)
:=
Z^{\mathrm{orb}}_{C,k}(uv,u/v)
=
\sum u^{B_A+B_O}v^{B_A-B_O}.
\]

No claim of novelty is attached to polynomial encoding itself.

---

## 2. Strict 1D host

Use the HATTER-SOL-08 strict one-dimensional class: a connected simple architecture is a path.

Take

\[
k=2m\ge2
\]

uniform nodes, each with orbit-total capacity `(A,O)`.

The path has `k-1` edges. Let `r` be the number of axial edges. Then the number of oblique edges is `k-1-r`, so every feasible edge typing has boundary

\[
\boxed{
B_A=kA-2r,
\qquad
B_O=kO-2(k-1-r).
}
\]

The total boundary is independent of `r`:

\[
\boxed{
B_A+B_O=k(A+O)-2(k-1).
}
\]

Hence distinct feasible boundary points never dominate one another. The full attainable set is already the Pareto front.

---

## 3. Exact feasible color-count interval

A channel of capacity at least `2` imposes no extra restriction on a path, because every path vertex has degree at most `2`.

A channel of capacity `1` may not occupy two adjacent path edges: its edges must form a matching. The maximum matching size of `P_{2m}` is `m`.

Therefore the axial-edge count `r` ranges over every integer in

\[
\boxed{
r_{\min}(O)\le r\le r_{\max}(A),}
\]

where

\[
r_{\max}(A)=
\begin{cases}
0,&A=0,\\
m,&A=1,\\
k-1,&A\ge2,
\end{cases}
\]

and

\[
r_{\min}(O)=
\begin{cases}
k-1,&O=0,\\
m-1,&O=1,\\
0,&O\ge2.
\end{cases}
\]

Every integer in this interval is realizable by a path edge-coloring satisfying the local capacities.

### Theorem T11.26 — exact strict-1D orbital response polynomial

For every feasible `(A,O)` on `P_{2m}`,

\[
\boxed{
Z^{\mathrm{orb}}_{P,2m}(A,O;X,Y)
=
\sum_{r=r_{\min}(O)}^{r_{\max}(A)}
X^{2mA-2r}
Y^{2mO-2(2m-1-r)}.
}
\]

The scalar boundary is

\[
\boxed{
\lambda^{\mathrm{orb}}_{P,2m}(A,O)
=2m(A+O-2)+2.
}
\]

The second formula is exactly the HATTER-SOL-08 path law applied to total capacity `A+O`, while the polynomial records the orbit-label information discarded by that scalar projection.

---

## 4. Apply T11.26 to one generic-odd forgetting fiber

Fix

\[
P>Q>0,
\qquad
S=P+Q.
\]

The three canonical members of the generic-odd `(P,Q)` forgetting fiber have orbit totals

\[
\Xi_I=(P,Q),
\qquad
\Xi_{II}=(Q,P),
\qquad
\Xi_{III}=(0,S).
\]

We now compare their exact path response polynomials.

---

## 5. Case `Q>=2`

Both channels of Types I and II have capacity at least `2`, hence every edge count

\[
0\le r\le2m-1
\]

is feasible.

Thus

\[
\boxed{
Z_I^{1D}
=
\sum_{r=0}^{2m-1}
X^{2mP-2r}
Y^{2mQ-2(2m-1-r)},
}
\]

\[
\boxed{
Z_{II}^{1D}
=
\sum_{r=0}^{2m-1}
X^{2mQ-2r}
Y^{2mP-2(2m-1-r)},
}
\]

and the pure-oblique state has the singleton response

\[
\boxed{
Z_{III}^{1D}
=Y^{2mS-2(2m-1)}.
}
\]

The maximum `X` exponent of `Z_I^{1D}` is `2mP`, while that of `Z_{II}^{1D}` is `2mQ`. Since `P>Q`, the first two polynomials differ. Each has `2m` monomials, whereas Type III has one.

---

## 6. Case `Q=1`

Now the small channel is matching-limited.

For Type I `(P,1)`, the oblique edges form a matching, so

\[
m-1\le r\le2m-1.
\]

Hence

\[
\boxed{
Z_I^{1D}
=
\sum_{r=m-1}^{2m-1}
X^{2mP-2r}
Y^{2m-2(2m-1-r)}.
}
\]

For Type II `(1,P)`, the axial edges form a matching, so

\[
0\le r\le m,
\]

and

\[
\boxed{
Z_{II}^{1D}
=
\sum_{r=0}^{m}
X^{2m-2r}
Y^{2mP-2(2m-1-r)}.
}
\]

Type III remains

\[
\boxed{
Z_{III}^{1D}
=Y^{2m(P+1)-2(2m-1)}.
}
\]

The first two polynomials each have `m+1` monomials and are distinct. Indeed

\[
\deg_X Z_I^{1D}
=2mP-2(m-1)
=2m(P-1)+2
>2m
=\deg_X Z_{II}^{1D}.
\]

Neither can equal the singleton Type-III polynomial.

---

## 7. Permanent orbital memory in strict 1D

### Theorem T11.27 — no host-scale orbital forgetting on a line

For every generic-odd interior fiber

\[
P>Q>0
\]

and every even path size

\[
k=2m\ge2,
\]

we have

\[
\boxed{
Z_I^{1D}\ne Z_{II}^{1D},
\qquad
Z_I^{1D}\ne Z_{III}^{1D},
\qquad
Z_{II}^{1D}\ne Z_{III}^{1D}.
}
\]

Equivalently, the strict one-dimensional full orbital response separates all three canonical members of the forgetting fiber at every host scale.

### Consequence

The unrestricted complete-host law from `EVEN_COMPLETE_HOST_ORBITAL_FORGETTING.md` has

\[
3\to2\to1
\]

memory loss as host degree grows.

Strict 1D has instead

\[
\boxed{3\to3\to3\to\cdots.}
\]

Thus dimensional restriction can protect orbital information that unrestricted geometry eventually erases.

This is the first exact HATTER-SOL-08/HATTER-SOL-11 bridge.

---

## 8. Why complete closure is impossible in low dimension

Let every one of `k` nodes have total capacity

\[
S=A+O.
\]

For any connected architecture class `C`, zero total boundary requires a graph with

\[
|E|=\frac{kS}{2}.
\]

Classical edge bounds give immediate obstructions.

### Strict 1D

A path has `k-1` edges, hence

\[
\lambda_P\ge kS-2(k-1)=k(S-2)+2.
\]

Thus for every interior fiber (`S>=3`), complete saturation is impossible for every finite host.

### Outerplanar

For `k>=2`, a simple outerplanar graph has at most `2k-3` edges, so

\[
\boxed{
\lambda_O\ge kS-4k+6=k(S-4)+6.
}
\]

In particular, if

\[
\boxed{S\ge4,}
\]

zero boundary is impossible for every finite outerplanar host.

### Planar

For `k>=3`, a simple planar graph has at most `3k-6` edges, so

\[
\boxed{
\lambda_{Pl}\ge kS-6k+12=k(S-6)+12.
}
\]

Hence if

\[
\boxed{S\ge6,}
\]

zero boundary is impossible for every finite planar host.

### Unrestricted

By contrast, on complete hosts the unrestricted model closes once the host degree reaches the total capacity:

\[
c=k-1\ge S.
\]

So the complete-saturation mechanism itself obeys the dimensional hierarchy

\[
\boxed{
\text{1D protects every }S\ge3;
\quad
O\text{ protects every }S\ge4;
\quad
Pl\text{ protects every }S\ge6;
\quad
A\text{ eventually closes every fixed }S.
}
\]

Here `protects` means only "prevents zero-boundary complete saturation". It does not by itself prove pairwise separation of all orbital states in the outerplanar or planar classes.

---

## 9. Polynomial memory witnesses

For any two fiber members `i,j`, define the response difference

\[
\boxed{
D^{C,k}_{ij}(X,Y)
:=
Z^{\mathrm{orb}}_{C,k}(\Xi_i;X,Y)
-
Z^{\mathrm{orb}}_{C,k}(\Xi_j;X,Y).
}
\]

Then

\[
D^{C,k}_{ij}=0
\]

iff the two full Pareto responses coincide.

For strict 1D, T11.27 says

\[
\boxed{
D^{P,2m}_{I,II},
D^{P,2m}_{I,III},
D^{P,2m}_{II,III}
\ne0
\quad\text{for all }m\ge1.
}
\]

For unrestricted even complete hosts, `EVEN_COMPLETE_HOST_ORBITAL_FORGETTING.md` gives exact host ranges where these differences vanish.

This provides a compact language for the next dimensional comparison without collapsing the Pareto data to one scalar.

---

## 10. Why there is no geometry Laplacian yet

HATTER-SOL-09 introduced a Laplacian only after a canonical prime-toggle adjacency between arithmetic worlds had been defined.

The HATTER-SOL-08 classes

\[
P\subset O\subset Pl\subset A
\]

are currently a nested inclusion hierarchy. Inclusion alone does not force unique edge weights, reversibility, or a canonical graph of geometry moves.

Therefore at this stage we use only the finite differences

\[
Z_O-Z_P,
\qquad
Z_{Pl}-Z_O,
\qquad
Z_A-Z_{Pl}
\]

when they are informative.

A geometry Laplacian should be introduced only if a natural generating set of geometry transitions is proved or explicitly chosen as part of an experimental protocol.

---

## 11. What is now proved

The following layer is closed:

1. the orbital Pareto front has an exact response-polynomial encoding;
2. the uniform strict-1D orbital response polynomial is explicit for all channel capacities;
3. every generic-odd interior `(P,Q)` forgetting fiber remains fully separated on every even path;
4. unrestricted complete hosts exhibit the previously proved `3 -> 2 -> 1` collapse;
5. classical edge-density bounds show that complete saturation is dimensionally forbidden for large enough total capacity in 1D, outerplanar, and planar classes;
6. the response polynomial is useful now; a geometry Laplacian is not yet justified.

---

## 12. Next target

The next difficult layer is no longer 1D.

Attack the outerplanar class first, because it is the smallest geometry in HATTER-SOL-08 where refinement inversion already survives.

For one fixed generic-odd fiber `(P,Q)`, determine whether there is an outerplanar analogue of T11.27:

- permanent separation;
- a finite first collision scale;
- or a capacity-dependent dichotomy.

The polynomial target is

\[
Z^{\mathrm{orb}}_{O,k}(P,Q),
\qquad
Z^{\mathrm{orb}}_{O,k}(Q,P),
\qquad
Z^{\mathrm{orb}}_{O,k}(0,P+Q).
\]

The first hostile test should be the smallest interior fiber

\[
(P,Q)=(2,1),
\]

because `S=3` lies below the outerplanar density obstruction and is therefore the first place where genuine outerplanar saturation / collision can occur.