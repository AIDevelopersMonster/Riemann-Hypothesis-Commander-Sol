# HATTER-SOL-13 · Residue-Degree Carrier Survival/Collapse Dichotomy

**Status:** exact theorem layer  
**Probe:** the fixed rational integer `2`  
**Worlds:** `K_k = Q(zeta_{2^k-1})`

## 1. Why a new port lift is needed

The arithmetic theorem `CYCLOTOMIC_FIXED_PRIME_UNBOUNDED_SUPPORT.md` proves that

\[
2\mathcal O_{K_k}=\prod_{i=1}^{g_k}\mathfrak p_{k,i},
\qquad
 g_k=\frac{\varphi(2^k-1)}{k}\to\infty,
\]

and every prime ideal above `2` has residue degree exactly `k`.

To test whether this arithmetic branching survives HATTER wiring, define the **residue-degree port lift** as follows.

For every prime ideal `p` above a rational prime `q`, assign the scalar port capacity

\[
\boxed{
c_f(\mathfrak p):=f(\mathfrak p/q)
=\dim_{\mathbf F_q}(\mathcal O_K/\mathfrak p).
}
\]

The residue degree is intrinsic arithmetic data. Using it as a port capacity is a HATTER modeling choice, but it introduces no external labels.

For a simple graph `G` on the prime ideals above `q`, define the free boundary exactly as in HATTER-SOL-07:

\[
B_f(G)=\sum_{v}c_f(v)-2|E(G)|,
\]

subject to the local feasibility condition

\[
\deg_G(v)\le c_f(v).
\]

For the cyclotomic family considered here,

\[
\boxed{c_f(\mathfrak p_{k,i})=k\quad\text{for every }i.}
\]

Hence

\[
\boxed{B_f(G)=g_k k-2|E(G)|.}
\]

Since `g_k k=phi(2^k-1)`, the total port budget is exactly the degree of the cyclotomic field.

---

## 2. Sparse carriers preserve unbounded diversity

### Theorem C13.4 — exact tree response

Let `T_k` be any tree whose vertex set is the `g_k` prime ideals above `2` in `K_k`. Then `T_k` is capacity-feasible for every `k>=2` whenever its maximum degree is at most `k`; in particular a path is always feasible. For every such tree,

\[
\boxed{
B_f(T_k)
=g_k k-2(g_k-1)
=\varphi(2^k-1)-2g_k+2.
}
\]

Equivalently,

\[
\boxed{
B_f(T_k)=g_k(k-2)+2.
}
\]

### Proof

A tree on `g_k` vertices has exactly `g_k-1` edges. Substitute this in the HATTER port-balance identity. QED.

### Corollary C13.4a — unbounded tree/path response

For the path carrier `P_{g_k}`,

\[
\boxed{B_f(P_{g_k})\to\infty.}
\]

Indeed, for `k>=3`,

\[
B_f(P_{g_k})
=\left(1-\frac2k\right)\varphi(2^k-1)+2.
\]

Using the odd-integer bound

\[
\varphi(2^k-1)\ge\sqrt{2^k-1},
\]

we get

\[
B_f(P_{g_k})
\ge
\left(1-\frac2k\right)\sqrt{2^k-1}+2
\to\infty.
\]

Thus the fixed integer `2` has an unbounded scalar HATTER network response across this natural world family on the strict path carrier.

In particular the number of distinct path responses among the first `m` worlds is unbounded as `m->infinity`.

---

## 3. Dense carriers can erase the same diversity completely

The same arithmetic state admits a radically different carrier behavior.

Because

\[
g_k\ge\frac{\sqrt{2^k-1}}{k},
\]

we have

\[
 g_k>k
\]

for all sufficiently large `k`.

Also

\[
g_k k=\varphi(2^k-1)
\]

is even for every `k>=2` because `2^k-1>2`.

We now construct a connected simple `k`-regular graph on `g_k` vertices whenever `g_k>k`.

Write the vertex set as `Z/g_k Z`.

- If `k` is even, connect each `x` to
  \[
  x\pm1,\ldots,x\pm k/2.
  \]
- If `k` is odd, then `g_k` is even because `g_k k` is even. Connect each `x` to
  \[
  x\pm1,\ldots,x\pm (k-1)/2,
  \]
  and also to the antipodal vertex
  \[
  x+g_k/2.
  \]

Because `g_k>k`, these neighbors are distinct and no loop occurs. The `+-1` edges make the graph connected. Every vertex has degree exactly `k`.

Call this carrier `S_k`.

### Theorem C13.5 — exact saturated collapse

For every sufficiently large `k`, the carrier `S_k` is simple, connected, capacity-feasible, and uses every residue-degree port. Consequently

\[
\boxed{B_f(S_k)=0.}
\]

### Proof

Every vertex has capacity `k` and degree `k`, so there are no unused ports. Equivalently,

\[
2|E(S_k)|=g_k k
\]

and therefore

\[
B_f(S_k)=g_k k-2|E(S_k)|=0.
\]

QED.

---

## 4. Carrier survival/collapse theorem

### Theorem C13.6 — unbounded arithmetic state, opposite carrier outcomes

For the single fixed rational integer `2` and worlds

\[
K_k=\mathbb Q(\zeta_{2^k-1}),
\]

the intrinsic residue-degree port lift has the following two exact carrier regimes:

\[
\boxed{
B_f(P_{g_k})=g_k(k-2)+2\to\infty,
}
\]

while for the explicit saturated connected carriers `S_k`,

\[
\boxed{B_f(S_k)=0}
\]

for all sufficiently large `k`.

Therefore the same unbounded arithmetic prime-ideal support can be either

1. preserved as an unbounded scalar network boundary response by a sparse carrier; or
2. erased completely by a capacity-saturating carrier.

This is an infinite-world analogue of the finite carrier-collapse phenomena of HATTER-SOL-11/12.

---

## 5. Diversity consequence

Let

\[
D_m^{path}(2)
:=\#\{B_f(P_{g_k}):2\le k\le m\},
\]

and define `D_m^{sat}(2)` analogously using the saturated carriers whenever they exist.

Then

\[
\boxed{D_m^{path}(2)\to\infty,}
\]

whereas the saturated response is eventually constant:

\[
\boxed{B_f(S_k)=0.}
\]

Thus unbounded arithmetic-world diversity is not itself a carrier-invariant notion.

---

## 6. Claim boundary

What is now proved:

- fixed integer `2` has unbounded prime-ideal support across the cyclotomic family;
- an intrinsic residue-degree scalar port lift converts this into an unbounded HATTER boundary response on paths/trees;
- an explicit connected capacity-saturating carrier collapses the same scalar response to zero.

What is not yet proved:

- that the richer HATTER-SOL-10 ideal typed frontier has unbounded rank;
- that every natural carrier preserves or collapses a prescribed amount of diversity;
- any entropy, payload, coding or cryptographic statement.

The next target is to quantify the carrier interpolation between the two extremes, preferably by an exact response law as a function of carrier edge density or maximum degree.