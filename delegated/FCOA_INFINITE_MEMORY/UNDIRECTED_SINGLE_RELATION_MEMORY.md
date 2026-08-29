# Undirected Single-Relation Payload Memory — Directedness Is Not Essential

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Date:** 2026-08-28  
**Status:** theorem checkpoint  
**Scope:** infinite fixed-carrier branch; pure-order dimension-2 provenance

## 1. Question

`SINGLE_RELATION_PAYLOAD_MEMORY.md` compressed the payload-preserving derived-instability mechanism to one directed binary relation.

The next question is whether the direction of that primitive relation is itself essential.

The answer is **no**.

A single **simple undirected graph** already suffices while preserving:

- interpretation dimension \(2\);
- payload preservation;
- no witness-only population;
- one primitive binary relation;
- no loops;
- symmetry;
- bounded atomic ladder depth;
- \(\Theta(N)\) primitive incidence cost;
- FO recovery of a full order of type \(\omega\);
- no FO ordinary addition or multiplication.

---

## 2. Carrier

Let

\[
U=\mathbb N^2.
\]

Write

\[
d_i=(i,i)
\]

for the diagonal point with coordinate \(i\).

For every off-diagonal point

\[
x=(i,j),\qquad i\ne j,
\]

write

\[
x^\top=(j,i)
\]

for its transpose.

Every point of \(U\) remains a generic payload peer.

---

## 3. One simple symmetric relation

Define a symmetric irreflexive graph relation

\[
G(x,y)=G(y,x),
\qquad
\neg G(x,x)
\]

by the following undirected edges.

For every \(i\ne j\):

### Row-coordinate edge

\[
\boxed{
(i,j)\;--\;d_i.
}
\]

### Transpose edge

\[
\boxed{
(i,j)\;--\;(j,i).
}
\]

### Upper-triangle marker edge

If \(i<j\), add

\[
\boxed{
(i,j)\;--\;d_j.
}
\]

No other edges are present.

Thus for every unordered coordinate pair \(i<j\), with

\[
u_{ij}=(i,j),
\qquad
\ell_{ij}=(j,i),
\]

the local gadget contains

\[
d_i--u_{ij},
\qquad
d_j--u_{ij},
\qquad
d_j--\ell_{ij},
\qquad
u_{ij}--\ell_{ij}.
\]

The asymmetry between the upper and lower payload point replaces primitive edge direction.

---

## 4. Exact local degrees

For an off-diagonal point \(x=(i,j)\):

- if \(i<j\), then
  \[
  \deg(x)=3;
  \]
- if \(i>j\), then
  \[
  \deg(x)=2.
  \]

Each diagonal point \(d_i\) has infinite degree because it is adjacent to all row points

\[
(i,j),\qquad j\ne i.
\]

Hence the diagonal is first-order definable by a fixed finite degree threshold:

\[
\boxed{
D(x):=
\exists y_1y_2y_3y_4
\Bigl(
\bigwedge_{p\ne q}y_p\ne y_q
\wedge
\bigwedge_{p=1}^4G(x,y_p)
\Bigr).
}
\]

Then

\[
D(U)=\{d_i:i\in\mathbb N\}.
\]

---

## 5. The transpose map is FO-recoverable

Every off-diagonal point has exactly one non-diagonal neighbor, namely its transpose.

Define

\[
\boxed{
T(x,y):=
\neg D(x)\wedge\neg D(y)\wedge G(x,y).
}
\]

Then for all \(i\ne j\),

\[
T((i,j),(j,i)).
\]

Uniqueness is immediate from the graph definition.

For diagonal points one may set the definitional extension

\[
T_D(x,y):=(D(x)\wedge x=y)\vee T(x,y).
\]

---

## 6. Upper versus lower payload points

An off-diagonal point is upper exactly when it has two distinct diagonal neighbors.

Define

\[
\boxed{
U(x):=
\neg D(x)\wedge
\exists a\ne b\,
\bigl(D(a)\wedge D(b)\wedge G(x,a)\wedge G(x,b)\bigr).
}
\]

Then

\[
U(i,j)\iff i<j.
\]

The lower points are

\[
L(x):=\neg D(x)\wedge\neg U(x).
\]

---

## 7. Recovering both ordered coordinates

For every off-diagonal \(x\), let \(t=x^\top\).

The pair \(x,t\) has exactly one common diagonal neighbor.

- If \(x=(i,j)\) is upper, that common diagonal neighbor is \(d_j\), the **second** coordinate of \(x\).
- If \(x=(i,j)\) is lower, that common diagonal neighbor is \(d_i\), the **first** coordinate of \(x\).

Define the shared-diagonal predicate

\[
C(x,a):=
D(a)\wedge
\exists t\bigl(T(x,t)\wedge G(x,a)\wedge G(t,a)\bigr).
\]

Now define the first-coordinate projection.

For diagonal \(x\), both coordinates are \(x\). For off-diagonal \(x\):

\[
\boxed{
P_1(x,a):=
(D(x)\wedge a=x)
\vee
\Bigl(
U(x)\wedge D(a)\wedge G(x,a)\wedge\neg C(x,a)
\Bigr)
\vee
\Bigl(
L(x)\wedge C(x,a)
\Bigr).
}
\]

Then

\[
P_1((i,j),d_k)\iff k=i.
\]

Similarly, define the second-coordinate projection by

\[
\boxed{
P_2(x,b):=
(D(x)\wedge b=x)
\vee
\Bigl(
U(x)\wedge C(x,b)
\Bigr)
\vee
\Bigl(
L(x)\wedge
\exists t\bigl(
T(x,t)\wedge D(b)\wedge G(t,b)\wedge\neg C(x,b)
\bigr)
\Bigr).
}
\]

Then

\[
P_2((i,j),d_k)\iff k=j.
\]

Thus the graph FO-recovers the ordered coordinate pair of every payload point.

---

## 8. Derived order on the diagonal

For diagonal points \(a=d_i\), \(b=d_j\), define

\[
\boxed{
\operatorname{DLess}(a,b):=
D(a)\wedge D(b)\wedge
\exists x\bigl(
U(x)\wedge P_1(x,a)\wedge P_2(x,b)
\bigr).
}
\]

Then

\[
\operatorname{DLess}(d_i,d_j)\iff i<j.
\]

Therefore the order property is generated only after nontrivial FO composition of a symmetric primitive graph relation.

---

## 9. Full order on every payload point

Once the two diagonal coordinates of every \(x=(i,j)\) are FO-recovered, repeat the shell construction of `PAYLOAD_PRESERVING_DERIVED_INSTABILITY.md`.

Define the max-coordinate key

\[
\mu(x)=d_{\max(i,j)}
\]

using \(P_1,P_2\) and \(\operatorname{DLess}\).

Order all payload points by:

1. increasing \(\mu(x)\);
2. within one max-shell, increasing first coordinate;
3. if first coordinates agree, increasing second coordinate.

Every max-shell

\[
S_m=\{(i,j):\max(i,j)=m\}
\]

has exactly

\[
2m+1
\]

elements, so the resulting FO-definable order \(\prec\) has type \(\omega\).

Hence:

### Theorem UD-1 — undirected derived order

\[
\boxed{
(U;G)\Rightarrow_{\rm FO}(U,\prec)\cong(\mathbb N,<).
}
\]

Directedness is therefore not required for FO global-order memory.

---

## 10. The primitive graph is C4-free

### Lemma UD-2

Any two distinct vertices of \(G\) have at most one common neighbor.

### Proof

We check the three possible type combinations.

#### Two diagonal vertices

Let \(d_i\ne d_j\). If \(i<j\), their unique common neighbor is the upper point

\[
(i,j).
\]

No other payload point is adjacent to both diagonals because an off-diagonal point has at most the two diagonal neighbors corresponding to its own coordinates, and it has both exactly in upper orientation. Thus the codegree is one.

#### One diagonal and one off-diagonal vertex

Let \(d_k\) and \(x=(i,j)\). The off-diagonal vertex has at most three neighbors:

\[
d_i,
\qquad x^\top,
\qquad d_j\text{ if }i<j.
\]

A direct inspection of these possibilities shows that at most one can also lie in the neighborhood of \(d_k\). Coordinate uniqueness rules out two simultaneous common neighbors.

#### Two off-diagonal vertices

Each off-diagonal point has one transpose neighbor and one or two diagonal neighbors determined by its coordinate pair. Two distinct off-diagonal vertices can share two diagonal neighbors only if they have the same unordered coordinate pair. In that case they are transposes; but the lower member has only one diagonal neighbor, so only one diagonal is common. A transpose neighbor cannot provide a second common neighbor without forcing equality of the two vertices.

Hence the codegree is always at most one. \(\square\)

Therefore the graph contains no \(4\)-cycle:

\[
\boxed{G\text{ is }C_4\text{-free}.}
\]

---

## 11. Exact atomic ladder depth

A half-graph of depth \(3\) contains a \(4\)-cycle on

\[
a_0,a_1,b_1,b_2,
\]

because the required edges include

\[
a_0b_1,
\quad a_0b_2,
\quad a_1b_1,
\quad a_1b_2.
\]

Since \(G\) is \(C_4\)-free, no atomic half-graph of depth \(3\) exists.

Depth \(2\) does occur. For \(i<j\), take

\[
a_0=(i,j),
\qquad a_1=(j,i),
\qquad b_0=d_i,
\qquad b_1=d_j.
\]

Then

\[
G(a_0,b_0),
\quad G(a_0,b_1),
\quad G(a_1,b_1),
\quad \neg G(a_1,b_0).
\]

Thus:

### Theorem UD-3 — exact primitive ladder depth

\[
\boxed{
\lambda_G^{\rm atomic}=2.
}
\]

The primitive graph relation is therefore uniformly ladder-shallow even though the full structure FO-defines an infinite linear order.

---

## 12. Primitive incidence cost is linear

Let

\[
W_m=\{(i,j):0\le i,j\le m\},
\qquad |W_m|=(m+1)^2.
\]

Inside \(W_m\), the undirected edge families are disjoint and have sizes:

### Row edges

\[
(m+1)^2-(m+1)=m(m+1).
\]

### Transpose edges

One per unordered pair \(i<j\):

\[
\frac{m(m+1)}2.
\]

### Upper marker edges

One per upper point \(i<j\):

\[
\frac{m(m+1)}2.
\]

Therefore

\[
|E(G[W_m])|
=2m(m+1).
\]

Since

\[
|W_m|=(m+1)^2,
\]

we obtain

\[
\boxed{
|E(G[W_m])|=2|W_m|+O(\sqrt{|W_m|}).
}
\]

If the symmetric relation is counted as ordered tuples rather than undirected edges, the count doubles, but remains linear.

Hence:

### Theorem UD-4 — linear symmetric memory cost

For the intrinsic first \(N\) payload points of the recovered order,

\[
\boxed{
C_G(N)=\Theta(N).
}
\]

---

## 13. FO interdefinability with the previous payload structure

The graph \(G\) is FO-definable from the three-relation structure

\[
(U;P_1,P_2,M)
\]

of `PAYLOAD_PRESERVING_DERIVED_INSTABILITY.md`:

- row edges come from \(P_1\);
- transpose edges are defined by swapping the recovered two coordinates;
- upper marker edges connect an upper point to its \(P_2\)-coordinate.

Conversely, Sections 4–7 recover

\[
P_1,
\qquad P_2,
\qquad M
\]

from \(G\).

Therefore:

### Theorem UD-5 — interdefinability

\[
\boxed{
(U;G)
\quad\text{and}\quad
(U;P_1,P_2,M)
\text{ are FO-interdefinable}.}
\]

All earlier logical consequences transfer exactly.

---

## 14. Arithmetic non-leakage

By UD-5, ordinary addition and multiplication relative to the recovered full payload order remain FO-undefinable.

Thus

\[
\boxed{
G\not\Rightarrow_{\rm FO}+,
\qquad
G\not\Rightarrow_{\rm FO}\times.
}
\]

The same pure-order dimension-2 provenance proof applies: if ordinary addition were definable, parity restricted to the definable coordinate line would become definable in pure discrete order, contradicting unary quantifier elimination. Multiplication would imply addition in the presence of recovered successor by Julia Robinson's theorem.

---

## 15. One commutative partial-operation realization

Introduce one terminal output \(\Omega\) and define one partial binary operation by

\[
\boxed{
x\star y=\Omega
\iff G(x,y).
}
\]

Because \(G\) is symmetric,

\[
x\star y\text{ is defined}
\iff
y\star x\text{ is defined},
\]

and both values equal \(\Omega\). Hence the operation layer is commutative on its domain.

Because \(G\) is irreflexive,

\[
x\star x
\]

is undefined for every generic payload point.

So the full result can be stated directly in FCOA language:

### Theorem UD-6 — commutative one-layer realization

There exists a single one-output **commutative** partial binary operation layer on a dimension-2 payload-preserving carrier whose generic trace:

- is symmetric and irreflexive;
- is \(C_4\)-free;
- has exact atomic ladder depth \(2\);
- has \(\Theta(N)\) primitive cost;
- FO-recovers a full \(\omega\)-order;
- does not FO-recover ordinary \(+\) or \(\times\).

---

## 16. Main verdict

Directedness is **not** an essential resource.

The current extremal package can be strengthened to

\[
\boxed{
\begin{array}{l}
\operatorname{dim}_{\rm self}=2;\\
1\text{ primitive binary relation};\\
1\text{ partial-operation layer};\\
1\text{ terminal output};\\
\text{symmetric};\\
\text{irreflexive};\\
\text{commutative domain};\\
C_4\text{-free};\\
\lambda^{\rm atomic}=2;\\
\Theta(N)\text{ primitive cost};\\
\text{payload-preserving};\\
\text{FO full order};\\
\neg\text{FO }+;\\
\neg\text{FO }\times.
\end{array}
}
\]

Thus all asymmetry needed for global order can be generated **compositionally from local degree/transpose geometry inside a completely undirected primitive graph**.

---

## 17. What resource actually remains

After UD-6, none of the following is irreducible in this provenance class:

- directedness;
- primitive orientation;
- loops;
- multiple relations;
- multiple operation layers;
- multiple terminal outputs;
- unbounded primitive ladder depth;
- superlinear primitive incidence.

The essential resources still visible are:

1. interpretation dimension \(2\);
2. infinitely many infinite-degree coordinate hubs;
3. finite-degree payload points coupled to those hubs through transpose geometry.

The Sparse Memory Threshold already says that some infinite nonlocal core is unavoidable. The new construction shows that this nonlocality can coexist with a \(C_4\)-free, commutative, one-layer primitive graph.

---

## 18. Next frontier

The natural next independent barrier is now **nonlocal-core sparsity**:

> how sparse can the set of infinite-degree coordinate hubs be inside the FO-recovered carrier order while retaining the same one-relation, symmetric, linear-cost, arithmetic-safe package?

In the present max-shell order, the number of diagonal hubs among the first \(N\) payload points is

\[
\Theta(\sqrt N).
\]

The Sparse Memory Threshold only requires infinitely many hubs, not this density.

So the next sharp quantitative problem is whether

\[
\Theta(\sqrt N)
\]

can be reduced to

\[
O(\log N),
\quad O(\log^*N),
\quad\text{or even an arbitrarily slow unbounded function},
\]

without reintroducing arithmetic leakage or higher source complexity.