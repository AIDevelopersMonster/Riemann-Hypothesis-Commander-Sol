# QGE3 LQR — Lower Bounds

## 1. Pair-union connectivity

Let `S` be synchronizing and let `Gamma_a` be the constraint graph for source color `a`.

### Theorem 1.1
For every two distinct colors `a,b`,

\[
\boxed{\Gamma_a\cup\Gamma_b\text{ is connected}.}
\]

### Proof
If the union is disconnected, let `X` be a nonempty proper union of its connected components. No constraint of color `a` or `b` crosses the cut `(X,[r]\\X)`. Let `sigma=(a\ b)` and put `pi_i=sigma` on `X`, `pi_i=id` outside `X`. Every crossing constraint has a source color fixed by `sigma`, while internal constraints compare equal permutations. Thus all constraints hold but the tuple is non-diagonal, contradiction. \(\square\)

After replacing each `Gamma_a` by a spanning forest of each of its connected components, write `m_a=|E(Gamma_a)|`. Since a connected graph on `r` vertices has at least `r-1` edges,

\[
 m_a+m_b\ge r-1
\]

for every pair `a!=b`.

Summing over all unordered pairs gives

\[
(q-1)\sum_a m_a\ge \binom q2(r-1).
\]

Hence:

### Corollary 1.2 — universal half-density bound

\[
\boxed{L_q(r)\ge \left\lceil\frac{q(r-1)}2\right\rceil.}
\]

This strictly strengthens the old connectivity bound `r-1` for every `q>=3`.

---

## 2. Exact lower bound for q=3

For three colors, Theorem 1.1 yields

\[
m_0+m_1\ge r-1,
\quad
m_0+m_2\ge r-1,
\quad
m_1+m_2\ge r-1.
\]

Therefore

\[
2(m_0+m_1+m_2)\ge3(r-1),
\]

so

\[
\boxed{L_3(r)\ge\left\lceil\frac{3(r-1)}2\right\rceil.}
\]

The matching construction is given in `LQR_CONSTRUCTIONS.md`, so this lower bound is exact.

---

## 3. Exact lower bound for r=2

On two phase vertices, each reduced `Gamma_a` has either zero or one edge. If two colors had zero edges, their union would be disconnected, violating Theorem 1.1. Thus at least `q-1` colors contribute one edge:

\[
\boxed{L_q(2)\ge q-1.}
\]

The standard agreement-on-`q-1`-points construction gives equality.

---

## 4. Exact lower bound for r=3

On three phase vertices, a reduced `Gamma_a` is a forest with `m_a in {0,1,2}`.

If some `m_a=0`, then pair-union connectivity forces every other `Gamma_b` to be connected, hence `m_b=2`. Therefore

\[
|S|\ge2(q-1)>2q-3.
\]

Assume now every `m_a>=1`. If `m_a=m_b=1`, then `Gamma_a` and `Gamma_b` each consist of one edge. Their union is connected only when these are two distinct edges of the triangle on three phase vertices. There are only three possible one-edge graphs. Hence at most three colors can have `m_a=1`; all remaining colors have `m_a=2`.

For `q>=3`,

\[
|S|=\sum_a m_a\ge3+2(q-3)=2q-3.
\]

Thus

\[
\boxed{L_q(3)\ge2q-3.}
\]

Again `LQR_CONSTRUCTIONS.md` supplies equality.

---

## 5. Relation to classical uniquely colorable graphs

By the quotient theorem in `LQR_DEFINITIONS.md`, a synchronizing system produces a uniquely `q`-colorable graph `H(S)` with

\[
|V(H(S))|=qr-|S|.
\]

Classical unique-colorability implies that the subgraph induced by any two color classes is connected. In the present quotient this is exactly the pair-union connectivity theorem above. Thus the lower-bound mechanism is a specialization of a classical necessary condition to the FCOA transversal quotient.

A classical edge lower bound for uniquely `q`-colorable graphs,

\[
|E(H)|\ge(q-1)|V(H)|-\binom q2,
\]

combined with the fact that `H(S)` is the union of at most `r` canonical `K_q` transversals, reproduces the same universal half-density lower bound. The FCOA-specific gain comes from exploiting the restricted partition geometry, as in the exact `r=3` argument.
