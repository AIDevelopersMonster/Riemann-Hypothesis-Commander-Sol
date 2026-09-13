# HATTER-SOL-08 · Research kernel

## 1. Architecture classes

For a capacity vector

\[
\mathbf c=(c_1,\ldots,c_k),\qquad c_i\ge2,
\]

let `C` be one of the following classes of simple graphs:

- `P`: paths (strict 1D connected straight-line architectures);
- `O`: outerplanar graphs (all vertices may be placed on one boundary, equivalently one-page/circular topological architecture);
- `Pl`: planar graphs;
- `A`: all finite simple graphs (equivalently the 3D straight-line class, since every finite graph has a crossing-free straight-line drawing in R^3).

Define

\[
M_C(\mathbf c)
=
\max\{|E(G)|:\;G\in C,\;G\text{ connected},\;\deg(v_i)\le c_i\},
\]

and

\[
\lambda_C(\mathbf c)=\sum_i c_i-2M_C(\mathbf c).
\]

The inclusions

\[
P\subset O\subset Pl\subset A
\]

imply

\[
\boxed{
\lambda_P(\mathbf c)
\ge
\lambda_O(\mathbf c)
\ge
\lambda_{Pl}(\mathbf c)
\ge
\lambda_A(\mathbf c).
}
\]

We identify `lambda_A` with the HATTER-SOL-07 invariant `lambda`.

---

## 2. Exact 1D theorem

For `k>=2`, a connected simple straight-line graph embedded on a line without overlapping edge interiors must be a path. Therefore

\[
M_P(\mathbf c)=k-1
\]

because every `c_i>=2`, and hence

\[
\boxed{
\lambda_P(\mathbf c)=\sum_i c_i-2(k-1).
}
\]

If `\mathbf c'` is obtained from `\mathbf c` by one multiplicative refinement

\[
ab\to(a,b),\qquad a,b\ge2,
\]

then the number of vertices increases from `k` to `k+1`, while total capacity drops by

\[
\delta(a,b)=ab-a-b.
\]

Thus

\[
\begin{aligned}
\lambda_P(\mathbf c')-\lambda_P(\mathbf c)
&=-\delta-2\\
&=-(ab-a-b+2)\\
&=-[(a-1)(b-1)+1]<0.
\end{aligned}
\]

### Theorem 2.1

\[
\boxed{
\lambda_P(\mathbf c')-\lambda_P(\mathbf c)
=-(ab-a-b+2)<0.
}
\]

Hence refinement inversion is impossible in strict 1D.

---

## 3. Complete-capacity dimensional staircase

Let

\[
\mathbf c^{(k)}=(k-1,\ldots,k-1),\qquad k\ge4.
\]

The capacities do not constrain any simple graph on `k` vertices, so the architecture-class edge maxima alone determine the boundary.

Classical extremal edge counts:

\[
M_P=k-1,
\]

\[
M_O=2k-3,
\]

\[
M_{Pl}=3k-6,
\]

\[
M_A=\binom{k}{2}.
\]

Therefore

\[
\boxed{\lambda_P=(k-1)(k-2)},
\]

\[
\boxed{\lambda_O=(k-2)(k-3)},
\]

\[
\boxed{\lambda_{Pl}=(k-3)(k-4)},
\]

\[
\boxed{\lambda_A=0}.
\]

This is a useful exact calibration family, but it is a direct consequence of classical extremal graph theory and is not itself claimed as novel.

Define dimensional-release increments

\[
R_{P\to O}=\lambda_P-\lambda_O=2(k-2),
\]

\[
R_{O\to Pl}=\lambda_O-\lambda_{Pl}=2(k-3),
\]

\[
R_{Pl\to A}=\lambda_{Pl}-\lambda_A=(k-3)(k-4).
\]

---

## 4. Connectivity lemma for planar and outerplanar maxima

The HATTER-SOL-07 proof technique needs a class-specific version of the fact that connectivity does not reduce the maximum feasible edge count.

### Lemma 4.1

For `C in {O,Pl}` and capacities `c_i>=2`, the maximum number of edges among all simple `C`-graphs satisfying `deg(v_i)<=c_i` is attained by a connected graph.

### Proof sketch with all required local operations

Choose a maximum-edge feasible graph `H` with the minimum number of connected components.

If two components contain unsaturated vertices, embed the two components in disjoint disks with the chosen vertices on the outer face and join those vertices by a new edge. This preserves planarity; in the outerplanar case all vertices can remain on the outer face. The edge count increases, contradicting maximality.

Thus at most one component contains unsaturated vertices.

Every saturated nontrivial component has minimum degree at least two and hence contains a cycle and a nonbridge edge. Such a nonbridge edge can be selected on the boundary of a suitable outer face of a planar embedding; in an outerplanar component one may select a cycle edge exposed on the outer boundary.

If the unique unsaturated component is an isolated vertex `z`, choose a nonbridge outer-face edge `xy` in a saturated component, delete `xy`, and add `xz`. Edge count and degree feasibility are preserved while the number of components decreases.

If two nontrivial saturated components remain, choose nonbridge outer-face edges `xy` and `uv`, delete them, and reconnect crosswise by `xu` and `yv` after placing the components in disjoint disks. The two new edges can be routed in the common outer face without crossings; outerplanarity is preserved in the outerplanar case. Degrees and edge count are unchanged, while the number of components decreases.

All cases contradict minimality of the number of components. Therefore a maximum-edge feasible graph can be chosen connected. `QED`.

---

## 5. One-step refinement upper bound survives in 2D classes

Let `C in {O,Pl}` and let `\mathbf c'` be obtained from `\mathbf c` by

\[
ab\to(a,b).
\]

Set

\[
\delta=ab-a-b.
\]

### Lemma 5.1 — local split in an embedding

Take a `C`-embedding of a feasible graph and a vertex `x` of capacity `ab` and degree `d`.

If `d<=a+b`, cut the cyclic order of the edges at `x` into two consecutive blocks of sizes at most `a` and `b`. Replace `x` locally by nearby vertices `u,v` and assign the two blocks to them. This preserves the embedding class and loses no edge.

If `d>a+b`, retain `a+b` consecutive incidences around `x`, split them into consecutive blocks of sizes `a` and `b`, and delete the remaining `d-a-b` incidences. The same local replacement preserves planarity / outerplanarity and loses exactly `d-a-b` edges.

Thus one can produce a (not necessarily connected) feasible `C`-graph after refinement losing at most

\[
\max(0,d-a-b)\le ab-a-b=\delta
\]

edges.

By Lemma 4.1 the same maximum edge count is attainable by a connected feasible `C`-graph. Hence

\[
M_C(\mathbf c')\ge M_C(\mathbf c)-\delta.
\]

Since total capacity drops by `delta`, exactly as in HATTER-SOL-07,

\[
\boxed{
\lambda_C(\mathbf c')-\lambda_C(\mathbf c)
\le\delta
=ab-a-b.
}
\]

### Theorem 5.2

For `C=O` and `C=Pl`,

\[
\boxed{
\lambda_C(\ldots,a,b,\ldots)
-
\lambda_C(\ldots,ab,\ldots)
\le ab-a-b.
}
\]

This theorem says that dimensional restrictions do **not** amplify one-step refinement inversion beyond the unrestricted HATTER-SOL-07 bound.

What remains open is whether the bound is sharp for every pair `(a,b)` in either restricted class.

---

## 6. Exact dimensional sign reversal

Take the HATTER-SOL-07 inversion family with odd `q>=3` and `m>=2q`:

\[
\mathbf A=(2q,2^m),
\qquad
\mathbf A'=(q,2^{m+1}).
\]

The coarse saturated construction is a cactus consisting of `q` cycles sharing one hub. This graph is outerplanar.

The refined boundary-one construction is a bouquet of triangles sharing the capacity-`q` hub, together with one path tail. It is also outerplanar.

Therefore

\[
\boxed{
\lambda_O(\mathbf A)=\lambda_{Pl}(\mathbf A)=\lambda_A(\mathbf A)=0,
}
\]

and, by odd total capacity plus the explicit outerplanar realization,

\[
\boxed{
\lambda_O(\mathbf A')=\lambda_{Pl}(\mathbf A')=\lambda_A(\mathbf A')=1.
}
\]

But Theorem 2.1 gives in strict 1D

\[
\lambda_P(\mathbf A')-\lambda_P(\mathbf A)
=-(q-2+2)=-q.
\]

Hence the **same arithmetic refinement** has opposite response signs:

\[
\boxed{
\Delta_P=-q<0,
\qquad
\Delta_O=\Delta_{Pl}=\Delta_A=+1
}
\]

for this explicit ambient family.

For `q=3`, i.e. split `6->2*3`, Theorem 5.2 gives upper bound `1`, and the outerplanar family attains `1`; therefore

\[
\boxed{
\Delta_O^{\max}(2,3)
=
\Delta_{Pl}^{\max}(2,3)
=
\Delta_A^{\max}(2,3)
=1.
}
\]

In contrast every 1D ambient vector gives

\[
\lambda_P(\mathbf c')-\lambda_P(\mathbf c)=-3.
\]

This is the first exact dimension-dependent refinement theorem of HATTER-SOL-08.

---

## 7. Main open quantities

Define for each class `C`

\[
\Delta_C^{\max}(a,b)
=
\sup_{\text{ambient}}
\left[
\lambda_C(\ldots,a,b,\ldots)
-
\lambda_C(\ldots,ab,\ldots)
\right].
\]

We currently have

\[
\Delta_P^{\max}(a,b)=-(ab-a-b+2),
\]

\[
\Delta_A^{\max}(a,b)=ab-a-b,
\]

\[
\Delta_O^{\max}(a,b)\le ab-a-b,
\qquad
\Delta_{Pl}^{\max}(a,b)\le ab-a-b,
\]

and exactly

\[
\Delta_O^{\max}(2,3)=\Delta_{Pl}^{\max}(2,3)=1.
\]

For odd `q>=3`, the explicit family gives the lower bounds

\[
\Delta_O^{\max}(2,q)\ge1,
\qquad
\Delta_{Pl}^{\max}(2,q)\ge1,
\]

while Theorem 5.2 gives

\[
\Delta_O^{\max}(2,q),\Delta_{Pl}^{\max}(2,q)\le q-2.
\]

The next main target is to close this gap.

---

## 8. Prior-art boundary

Classical ingredients used here:

- outerplanar edge bound `|E|<=2n-3`;
- planar edge bound `|E|<=3n-6`;
- Fary's theorem: every simple planar graph has a crossing-free straight-line planar drawing;
- every finite graph admits a crossing-free straight-line drawing in R^3, e.g. via the moment curve;
- classical vertex splitting / detachment theory;
- classical planar and outerplanar degree-realization theory.

No priority claim is attached to these facts.

Candidate new layer: the comparison of **free-boundary sensitivity under the arithmetic split `ab->(a,b)` across nested dimensional architecture classes**, including the exact 1D law, the class-preserving one-step upper bound, and the explicit sign reversal between 1D and outerplanar/planar/unrestricted architectures.
