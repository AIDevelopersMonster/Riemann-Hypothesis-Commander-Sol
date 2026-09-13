# Refinement inversion in capacity factor networks

## 1. Model

Let

\[
\mathbf a=(a_1,\ldots,a_k),\qquad a_i\ge2,
\]

be a multiplicative decomposition of an integer, so that

\[
\prod_{i=1}^k a_i=n.
\]

A **capacity-respecting network** for `\mathbf a` is a finite connected simple graph `G` on vertices `v_1,...,v_k` satisfying

\[
\deg_G(v_i)\le a_i.
\]

Its free boundary is

\[
B(G;\mathbf a)
:=\sum_{i=1}^k\bigl(a_i-\deg_G(v_i)\bigr)
=\sum_i a_i-2|E(G)|.
\]

Define the minimum free boundary of the decomposition by

\[
\lambda(\mathbf a)
:=\min_G B(G;\mathbf a),
\]

where the minimum ranges over connected simple capacity-respecting networks.

Because every `a_i>=2`, a path on the `k` vertices is always feasible when `k>=2`, so the admissible class is nonempty.

---

## 2. Cycle-rank identity

For a connected graph let

\[
\beta_1(G)=|E(G)|-|V(G)|+1
\]

be its cycle rank. Then

\[
\boxed{
B(G;\mathbf a)
=2+\sum_{i=1}^k(a_i-2)-2\beta_1(G).
}
\]

Thus the boundary splits into an arithmetic part and a topological correction:

\[
\text{tree boundary}
\; - \;
2\times\text{cycle rank}.
\]

Every independent cycle consumes exactly two free ports.

This identity is elementary (handshake lemma plus Euler cycle rank) and is not claimed as new.

---

## 3. Fixed-decomposition spectrum has no internal parity gaps

For fixed `\mathbf a`, let

\[
M_c(\mathbf a)
:=\max\{|E(G)|:\;G\text{ connected, simple, and }\deg_G(v_i)\le a_i\}.
\]

### Proposition 3.1 — parity-interval spectrum

The boundary spectrum of the fixed decomposition is exactly

\[
\boxed{
\mathcal B(\mathbf a)
=
\left\{
\sum_i a_i-2e:
 k-1\le e\le M_c(\mathbf a)
\right\}.
}
\]

Equivalently,

\[
\boxed{
\mathcal B(\mathbf a)
=
\{\lambda(\mathbf a),\lambda(\mathbf a)+2,\ldots,
2+\sum_i(a_i-2)\}.
}
\]

### Proof

Choose a connected admissible graph `G_max` with `M_c(\mathbf a)` edges and a spanning tree `T\subseteq G_max`. The tree has `k-1` edges. For any integer

\[
e\in\{k-1,k,\ldots,M_c(\mathbf a)\},
\]

start with `T` and add any `e-(k-1)` edges from `E(G_max)\setminus E(T)`. The resulting graph remains connected, simple, and capacity-respecting, and has exactly `e` edges. Therefore all boundary values of the required parity between the tree maximum and `\lambda(\mathbf a)` occur. The reverse inclusion follows from the handshake identity. `\square`

### Interpretation

For one fixed multiplicative decomposition, topology alone creates no mysterious holes: the spectrum is a complete interval with step two. Any more complicated gaps in the global spectrum

\[
\mathcal B(n)
=\bigcup_{\prod a_i=n}\mathcal B(\mathbf a)
\]

must come from the arithmetic arrangement of the multiplicative decompositions and their parity classes, not from missing intermediate cycle ranks inside one decomposition.

---

## 4. Tree refinement is strictly monotone

Suppose one factor `ab` is refined to `a,b`, with `a,b>=2`.

For trees the free boundary is

\[
B_T(\mathbf a)=2+\sum_i(a_i-2).
\]

Hence the loss under refinement is

\[
B_T(\ldots,ab,\ldots)-B_T(\ldots,a,b,\ldots)
=ab-a-b+2
=(a-1)(b-1)+1>0.
\]

So in the tree-only model, exposing more multiplicative structure always lowers the free boundary.

The next theorem shows that this monotonicity fails once cycles are allowed.

---

## 5. Refinement inversion theorem

### Theorem 5.1

Let `q>=3` be odd and let `m>=2q`. Consider

\[
\mathbf A=(2q,\underbrace{2,\ldots,2}_{m\text{ copies}})
\]

and its one-step refinement

\[
\mathbf A'=(q,\underbrace{2,\ldots,2}_{m+1\text{ copies}}),
\]

obtained by replacing `2q` with `2,q`.

Then

\[
\boxed{\lambda(\mathbf A)=0}
\]

but

\[
\boxed{\lambda(\mathbf A')=1}.
\]

Thus a proper multiplicative refinement can **increase** the minimum free boundary.

### Proof: coarse decomposition

There are `m` capacity-two vertices and one hub of capacity `2q`.

Because `m>=2q`, partition the `m` capacity-two vertices into `q` nonempty blocks, each containing at least two vertices. On each block form a path. Connect both endpoints of every path to the hub.

Then:

- the hub has degree `2q`;
- each path endpoint has one path edge and one hub edge, hence degree `2`;
- each internal path vertex has degree `2`.

Every port is used, so

\[
B=0.
\]

Therefore `\lambda(\mathbf A)=0`.

### Proof: refined decomposition — lower bound

The total capacity is

\[
q+2(m+1),
\]

which is odd because `q` is odd. Since every graph has even total degree,

\[
B(G;\mathbf A')
=\bigl(q+2(m+1)\bigr)-2|E(G)|
\]

is odd. Hence

\[
B(G;\mathbf A')\ge1
\]

for every admissible network.

### Proof: refined decomposition — construction with boundary one

Write

\[
q=2r+1,
\qquad r=(q-1)/2.
\]

Use one capacity-`q` hub `h`.

First form `r` triangles sharing only `h`:

\[
h-x_i-y_i-h,
\qquad i=1,\ldots,r.
\]

These triangles use `2r=q-1` capacity-two vertices and `2r=q-1` ports of the hub.

There remain

\[
(m+1)-(q-1)=m-q+2\ge1
\]

capacity-two vertices. Arrange all of them in a path

\[
h-z_1-z_2-\cdots-z_t.
\]

This uses the last hub port. Every vertex except `z_t` now has its full capacity used; `z_t` has degree one and therefore exactly one unused port.

Thus

\[
B=1.
\]

Combined with the parity lower bound,

\[
\lambda(\mathbf A')=1.
\qquad\square
\]

---

## 6. Arithmetic corollary: prime resolution need not minimize free boundary

Let `q` be an odd prime and `m>=2q`. Put

\[
n=q\,2^{m+1}.
\]

The full prime decomposition is

\[
\mathbf p=(q,\underbrace{2,\ldots,2}_{m+1}),
\]

so Theorem 5.1 gives

\[
\lambda(\mathbf p)=1.
\]

But the coarser multiplicative decomposition

\[
\mathbf c=(2q,\underbrace{2,\ldots,2}_{m})
\]

has

\[
\lambda(\mathbf c)=0.
\]

Therefore

\[
\boxed{
\text{complete prime refinement does not in general minimize the free boundary}
}
\]

in the connected simple network model.

This is the first genuinely nontrivial structural correction to the initial chain intuition.

### First member of the explicit family

Take

\[
q=3,\qquad m=6.
\]

Then

\[
n=3\cdot2^7=384.
\]

The coarse decomposition

\[
384=6\cdot2^6
\]

admits a fully saturated network with boundary zero, whereas the prime decomposition

\[
384=3\cdot2^7
\]

has odd total capacity `17`, so its boundary cannot be zero; the construction above realizes boundary one.

No claim is made here that `384` is the globally smallest possible refinement inversion without a separate exhaustive proof.

---

## 7. What the theorem means — and what it does not

The theorem does **not** produce a new factorization algorithm or a new primality criterion. It proves a structural fact inside the chosen capacity-network representation:

- tree refinement is strictly boundary-decreasing;
- cycle-capable refinement can reverse that order;
- the reversal can be forced solely by the interaction of degree capacity, simple-graph topology, and parity.

In Wonderland language: exposing the hidden `2\times q` inside a hub can make the network *less able to close itself*, even though the arithmetic description became more refined.

That tension — multiplicative refinement versus topological closure — is now the main research hinge of HATTER-SOL-07.
