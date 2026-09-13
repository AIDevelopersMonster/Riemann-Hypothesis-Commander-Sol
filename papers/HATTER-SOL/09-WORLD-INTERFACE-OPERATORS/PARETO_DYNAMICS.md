# HATTER-SOL-09 · Exact Pareto dynamics for uniform typed factors

**Model:** conservative simple-support continuation of HATTER-SOL-07.  
Each unordered pair of factor vertices supports at most one edge total, typed `P` or `Q`.

This file closes the next theorem target from `TYPED_BOUNDARY_REGION.md`.

---

## 1. Setup

Let

\[
k=2m\ge2
\]

and consider `k` identical typed factor nodes

\[
(P,Q),\qquad P\ge Q\ge0,
\]

with

\[
S:=P+Q\ge2.
\]

For a connected typed simple-support graph write

\[
e_P=|E_P|,\qquad e_Q=|E_Q|,
\]

and

\[
B_P=kP-2e_P,
\qquad
B_Q=kQ-2e_Q.
\]

Put

\[
c:=k-1=2m-1,
\qquad
C:=\binom{k}{2}=\frac{kc}{2}.
\]

The support constraint gives

\[
e_P+e_Q\le C.
\]

The typed Pareto frontier is denoted

\[
\partial_P\mathfrak B^{(2)}_k(P,Q).
\]

---

## 2. Almost-regular existence lemma

### Lemma 2.1

For every `0<=e<=C` there exists a simple graph on `k` vertices with exactly `e` edges whose vertex degrees differ by at most one.

### Proof

Among all `k`-vertex simple graphs with `e` edges choose one minimizing

\[
\sum_v d(v)^2.
\]

If two vertices `x,y` satisfy `d(x)>=d(y)+2`, then there exists a neighbor `z` of `x` that is not adjacent to `y`; otherwise `N(x)\setminus\{y\}` would inject into `N(y)`, contradicting the degree gap. Replace edge `xz` by `yz`. The number of edges is unchanged, while

\[
d(x)^2+d(y)^2
\]

strictly decreases. Contradiction. Hence all degrees differ by at most one. □

### Corollary 2.2

Let integers `0<=l<=u<=k-1` be given. For every integer

\[
\frac{kl}{2}\le e\le\frac{ku}{2}
\]

there is a simple `k`-vertex graph with `e` edges and every degree in `[l,u]`.

Because `k` is even, both endpoint quantities are integers.

---

## 3. Exact Pareto-front theorem

Define effective per-color support caps

\[
p_*:=\min(P,c),
\qquad
q_*:=\min(Q,c).
\]

### Theorem 3.1 — closed regime

If

\[
\boxed{S\le c,}
\]

then

\[
\boxed{
\partial_P\mathfrak B^{(2)}_k(P,Q)=\{(0,0)\}.
}
\]

### Proof

It is enough to construct edge-disjoint `P`-regular and `Q`-regular spanning graphs whose union is connected.

Use a Walecki decomposition of `K_k`: `K_k` (for even `k`) decomposes into Hamilton cycles plus one perfect matching.

- If `P,Q` are both even, assign `P/2` Hamilton cycles to color `P` and `Q/2` to color `Q`.
- If exactly one is odd, assign the perfect matching to that color and use Hamilton cycles for the remaining even degrees.
- If both are odd, split one Hamilton cycle into its two alternating perfect matchings, assigning one to each color, and use further Hamilton cycles for the remaining even degrees.

The inequality `P+Q<=k-1` guarantees enough edge-disjoint factors. Since `S>=2`, the support can be chosen connected. Hence both capacities saturate and `(0,0)` is attainable; it dominates every other boundary vector. □

---

### Theorem 3.2 — congested regime

Assume

\[
\boxed{S>c.}
\]

Define

\[
D_k:=k(S-c),
\]

\[
L_P:=k(P-c)_+,
\qquad
L_Q:=k(Q-c)_+,
\]

where `(x)_+=max(x,0)`.

Then the exact typed Pareto frontier is

\[
\boxed{
\partial_P\mathfrak B^{(2)}_k(P,Q)
=
\left\{
(B_P,B_Q):
\begin{array}{l}
B_P+B_Q=D_k,\\
L_P\le B_P\le D_k-L_Q,\\
B_P\equiv0\pmod2
\end{array}
\right\}.
}
\]

Equivalently, it is the discrete step-two segment joining the two extreme points

\[
\boxed{
(L_P,D_k-L_P)
\quad\text{and}\quad
(D_k-L_Q,L_Q).
}
\]

### Proof

A color-`P` graph has at most

\[
M_P=\frac{k p_*}{2}
\]

edges, and similarly

\[
M_Q=\frac{k q_*}{2}.
\]

Because `S>c`, we have `p_*+q_*>=c`, hence

\[
M_P+M_Q\ge C.
\]

We first realize every edge-count point

\[
(e_P,e_Q)
\]

on the complete-support line

\[
e_P+e_Q=C
\]

with

\[
C-M_Q\le e_P\le M_P.
\]

Let

\[
l:=c-q_*,\qquad u:=p_*.
\]

Choose a graph `H` with `e_P` edges and all degrees between `l` and `u`, which exists by Corollary 2.2. Color `H` by `P` and its complement in `K_k` by `Q`. Then

\[
d_P(v)\le p_*\le P,
\]

while

\[
d_Q(v)=c-d_H(v)\le c-l=q_*\le Q.
\]

Thus every edge of `K_k` receives exactly one type and the support is connected.

Now take any feasible point with `e_P+e_Q<C`. Since `e_P<=M_P`, `e_Q<=M_Q`, and `M_P+M_Q>=C`, there exists

\[
t\in[C-M_Q,M_P]
\]

such that

\[
t\ge e_P,
\qquad
C-t\ge e_Q.
\]

The complete-support realization `(t,C-t)` therefore weakly increases both edge counts and strictly increases at least one. Hence the original boundary point is not Pareto-minimal.

So all Pareto points lie on `e_P+e_Q=C`, and the realizable interval above gives all of them. Translating edge counts to boundary coordinates yields

\[
B_P+B_Q
=k(P+Q)-2C
=k(S-c)=D_k,
\]

with minima

\[
\min B_P=k(P-p_*)=k(P-c)_+=L_P,
\]

\[
\min B_Q=k(Q-q_*)=k(Q-c)_+=L_Q.
\]

Because changing `e_P` by one changes `B_P` by two, the frontier has step two. □

---

## 4. Scalar boundary is the total mass of the typed frontier

Every Pareto point in the congested regime has the same scalar projection:

\[
\boxed{B_P+B_Q=D_k.}
\]

Combining both regimes,

\[
\boxed{
\lambda_k(S)
=
\begin{cases}
 k(S-k+1),&S>k-1,\\
 0,&S\le k-1.
\end{cases}
}
\]

for even `k` and uniform scalar capacity `S>=2`.

With `k=2m`, define

\[
\boxed{
D_m(S)
=2m\,\bigl(S-2m+1\bigr)_+.
}
\]

This is the scalar boundary pulse underlying the full typed frontier.

While both `m` and `m+1` are in the congested regime,

\[
\boxed{
D_{m+1}-D_m=2(S-4m-1).
}
\]

Thus the scalar boundary may first grow as conjugate factor pairs are added, then decay, and finally collapse to zero.

The continuous parabola associated with the congested formula peaks near

\[
m\approx\frac{S+1}{4}.
\]

---

## 5. Center and width of the typed frontier

For a boundary point define its imbalance

\[
\delta=B_P-B_Q.
\]

In the congested regime the midpoint imbalance of the two Pareto extremes is

\[
\boxed{
C_k(P,Q)
=k\bigl[(P-c)_+-(Q-c)_+\bigr].
}
\]

Normalize by the number of factor nodes:

\[
\boxed{
A_k(P,Q)
:=\frac{C_k}{k}
=(P-c)_+-(Q-c)_+.
}
\]

Since `P>=Q`, this has the exact piecewise form

\[
\boxed{
A_k(P,Q)=
\begin{cases}
P-Q,&c<Q,\\
P-c,&Q\le c<P,\\
0,&P\le c.
\end{cases}
}
\]

Hence the network carries the full intrinsic anisotropy `P-Q` at very small support degree, then linearly loses it, then becomes centered at zero before full closure is necessarily reached.

The `B_P`-coordinate width of the frontier is

\[
W_k
:=(D_k-L_Q)-L_P.
\]

A direct case split gives

\[
\boxed{
W_k
=k\min\{c,Q,S-c\}
}
\]

in the congested regime.

The number of Pareto points is therefore

\[
\boxed{
N_k
=1+\frac{k}{2}\min\{c,Q,S-c\}.
}
\]

---

## 6. Two exact thresholds

### Definition 6.1 — interface-forgetting threshold

Define

\[
\boxed{
\sigma(P,Q)
:=
\min\{m:2m-1\ge P\}
=
\left\lceil\frac{P+1}{2}\right\rceil.
}
\]

For every `m>=sigma`, the Pareto frontier (if still nonzero) is centered at zero and depends only on `S=P+Q`, not on the split between `P` and `Q`.

### Definition 6.2 — full-closure threshold

Define

\[
\boxed{
\tau(P,Q)
:=
\min\{m:2m-1\ge P+Q\}
=
\left\lceil\frac{P+Q+1}{2}\right\rceil.
}
\]

For every `m>=tau`,

\[
\boxed{
\partial_P\mathfrak B^{(2)}_{2m}(P,Q)=\{(0,0)\}.
}
\]

Always

\[
\boxed{\sigma(P,Q)\le\tau(P,Q).}
\]

Thus there may be a genuine intermediate regime

\[
\boxed{
\sigma\le m<\tau
}
\]

in which the network is **still open but has already forgotten the interface anisotropy**.

This is the first natural dynamical phenomenon produced by the typed model.

---

## 7. Prime 37: identical scalar dynamics, different typed dynamics

Both worlds have scalar factor capacity

\[
S=7
\]

for the split factors of `37`, so

\[
\boxed{D_m=2m(8-2m)_+}
\]

is identical in both worlds.

The sequence is

\[
\boxed{12,16,12,0,0,\ldots}
\]

for `m=1,2,3,4,...`.

But the typed pairs differ.

### Square world

\[
(P,Q)=(6,1).
\]

The exact Pareto fronts are

\[
m=1:\quad \{(10,2),(12,0)\},
\]

\[
m=2:\quad \{(12,4),(14,2),(16,0)\},
\]

\[
m=3:\quad \{(6,6),(8,4),(10,2),(12,0)\},
\]

\[
m\ge4:\quad \{(0,0)\}.
\]

The thresholds are

\[
\boxed{\sigma_G(37)=4,\qquad\tau_G(37)=4.}
\]

So the square world retains a nonzero directional center until the moment of closure.

### Triangular world

\[
(P,Q)=(4,3).
\]

The exact Pareto fronts are

\[
m=1:\quad \{(6,6),(8,4)\},
\]

\[
m=2:\quad
\{(4,12),(6,10),(8,8),(10,6),(12,4),(14,2),(16,0)\},
\]

\[
m=3:\quad
\{(0,12),(2,10),(4,8),(6,6),(8,4),(10,2),(12,0)\},
\]

\[
m\ge4:\quad \{(0,0)\}.
\]

The thresholds are

\[
\boxed{\sigma_E(37)=3,\qquad\tau_E(37)=4.}
\]

Thus at `m=3` the triangular world is still open (`D_3=12`) but its Pareto frontier has already become perfectly centered and depends only on the scalar capacity `S=7`.

This is a stronger separation than the original `m=1` witness:

\[
\boxed{
\text{37 has identical scalar boundary dynamics in both worlds,}
}
\]

but

\[
\boxed{
\text{different interface-memory dynamics.}
}
\]

---

## 8. Other laboratory values

### `7` in the triangular world

\[
(P,Q)=(2,1),\qquad S=3.
\]

\[
\boxed{\sigma=2,\qquad\tau=2.}
\]

The typed anisotropy survives until closure.

### `53` in the square world

\[
(P,Q)=(7,2),\qquad S=9.
\]

\[
\boxed{\sigma=4,\qquad\tau=5.}
\]

At `m=4` the network is still open but the Pareto frontier is already symmetric; at `m=5` it closes.

This corrects the earlier multiplex interpretation: in the **07-faithful simple-support model**, preserving types does not move the full-closure threshold from the scalar value `5`. Instead it reveals the additional earlier threshold `sigma=4` at which interface anisotropy is forgotten.

---

## 9. A pre-operator response profile

For `k=2m`, define the normalized center response

\[
\boxed{
\mathcal A_m(P,Q)
:=
(P-(2m-1))_+-(Q-(2m-1))_+.
}
\]

This is not a world Laplacian. It is a one-dimensional scale response of a single world's typed factor pair.

It has a rigid shape:

1. plateau `P-Q` while `2m-1<Q`;
2. linear decay `P-(2m-1)` while `Q<=2m-1<P`;
3. zero after `2m-1>=P`.

The two breakpoints are exactly the two interface capacities.

Therefore the entire canonical pair `(P,Q)` can in principle be recovered from the breakpoint structure of the response profile.

This is the first natural candidate for the data on which a later inter-world operator could act:

\[
R\mapsto \mathcal A_m^R(n),
\]

rather than only

\[
R\mapsto\Lambda_R(n).
\]

No inter-world operator is defined yet.

---

## 10. Verification note

The exact formula above was independently brute-force checked for all typed pairs

\[
1\le P\le5,\qquad 0\le Q\le P,
\]

with `P+Q>=2`, on `k=2` and `k=4` vertices. No discrepancy was found. This is regression evidence only; the proof is Theorem 3.2.

---

## 11. Next proof obligation

The uniform-factor problem is now closed.

The next nontrivial step is the first heterogeneous case:

\[
(P_1,Q_1),\ldots,(P_k,Q_k),
\]

especially products containing factors from more than one rational prime.

The target is to determine whether the typed Pareto frontier admits a cut/deficiency theorem analogous in spirit to b-matching deficiency, and whether the arithmetic world determines a canonical family of such deficiencies.

Only after that should a genuine operator on a graph/category of worlds be attempted.
