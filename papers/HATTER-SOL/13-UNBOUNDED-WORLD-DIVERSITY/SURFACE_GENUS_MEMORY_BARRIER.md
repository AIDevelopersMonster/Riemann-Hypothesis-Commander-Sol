# HATTER-SOL-13 · Surface-Genus Memory Barrier

**Status:** exact theorem layer  
**Probe:** fixed rational integer `2`  
**Worlds:** `K_k = Q(zeta_{2^k-1})`

## 1. Setup

Let

\[
N_k:=g_k=\frac{\varphi(2^k-1)}{k}
\]

be the number of prime ideals above `2` in `K_k`. Under the residue-degree port lift, every prime-ideal vertex has capacity `k`.

For a connected simple feasible carrier `G` on these `N_k` vertices,

\[
B_f(G)=N_k k-2|E(G)|.
\]

Assume that `G` is embeddable in a closed orientable surface of genus `h`.

The graph-theoretic input below is classical: for a connected simple graph with at least three vertices embedded in orientable genus `h`, Euler's formula and `3F<=2E` imply

\[
|E(G)|\le 3N_k-6+6h.
\]

No novelty is claimed for this surface edge bound.

---

## 2. Exact topological lower bound on surviving boundary

### Theorem C13.9 — genus memory barrier

For every sufficiently large `k` (so `N_k>=3`) and every connected simple feasible carrier `G` embeddable in orientable genus `h`,

\[
\boxed{
B_f(G)
\ge
N_k(k-6)+12-12h.
}
\]

Since `B_f(G)>=0` from feasibility, equivalently

\[
\boxed{
B_f(G)
\ge
\max\{0,\,N_k(k-6)+12-12h\}.
}
\]

### Proof

Substitute the classical surface edge bound into the HATTER boundary identity:

\[
B_f(G)
=N_k k-2|E(G)|
\ge
N_k k-2(3N_k-6+6h).
\]

Hence

\[
B_f(G)
\ge
N_k(k-6)+12-12h.
\]

The nonnegativity bound is independent and follows from `deg(v)<=k`. QED.

---

## 3. Planar and toroidal corollaries

### Corollary C13.9a — planar preservation

For every connected simple planar feasible carrier,

\[
\boxed{
B_f(G)
\ge
N_k(k-6)+12.
}
\]

Thus

\[
\boxed{B_f(G)\to\infty.}
\]

More strongly,

\[
\frac{B_f(G)}{N_k k}
\ge
1-\frac6k+\frac{12}{N_k k}
\longrightarrow1.
\]

Therefore planar carriers asymptotically leave almost all of the residue-degree port budget on the boundary.

### Corollary C13.9b — toroidal preservation

For orientable genus `h=1`,

\[
\boxed{
B_f(G)
\ge
N_k(k-6).
}
\]

and again

\[
\boxed{
\frac{B_f(G)}{N_k k}\to1.
}
\]

Thus the one-handle carrier that increased finite resolving power in HATTER-SOL-12 is still far too topologically sparse to erase the growing H13 memory.

---

## 4. Fixed-genus rigidity

### Corollary C13.9c

Fix any orientable genus `h` independent of `k`. Then uniformly over every connected simple feasible carrier embeddable in that genus,

\[
\boxed{
\inf_G \frac{B_f(G)}{N_k k}\longrightarrow1.
}
\]

### Proof

By C13.9,

\[
\frac{B_f(G)}{N_k k}
\ge
1-\frac6k+\frac{12-12h}{N_k k}.
\]

The right-hand side tends to `1`, while trivially `B_f(G)/(N_k k)<=1`. QED.

Hence bounded topological genus cannot remove a positive asymptotic fraction of the growing arithmetic port budget.

---

## 5. More general subcritical-genus law

The same argument gives a stronger scaling statement.

### Corollary C13.9d

Let `h_k` be any genus sequence satisfying

\[
h_k=o(N_k k).
\]

Then uniformly over connected simple feasible carriers embeddable in genus at most `h_k`,

\[
\boxed{
\frac{B_f(G_k)}{N_k k}\longrightarrow1.
}
\]

### Proof

Divide C13.9 by `N_k k`:

\[
\frac{B_f(G_k)}{N_k k}
\ge
1-\frac6k+
\frac{12}{N_k k}
-
12\frac{h_k}{N_k k}.
\]

Every error term tends to zero. QED.

Thus even a growing amount of topology is asymptotically ineffective if its genus is sublinear in the total arithmetic port budget `N_k k`.

---

## 6. Necessary topology cost for complete erasure

### Theorem C13.10 — genus lower bound for saturation

If a connected simple feasible carrier completely erases the scalar boundary,

\[
B_f(G)=0,
\]

then its orientable genus must satisfy

\[
\boxed{
h
\ge
\frac{N_k(k-6)+12}{12}.
}
\]

In particular,

\[
\boxed{h=\Omega(N_k k).}
\]

### Proof

If `B_f(G)=0`, Theorem C13.9 gives

\[
0\ge N_k(k-6)+12-12h.
\]

Rearranging yields the displayed bound. Since `k->infinity`, the right-hand side is asymptotic to `N_k k/12`. QED.

This is a necessary condition, not a claim that the lower bound is always attained.

---

## 7. Fixed-fraction erasure also costs linear genus

Let

\[
\rho_k(G):=\frac{B_f(G)}{N_k k}
\]

be the surviving boundary fraction.

### Corollary C13.10a

Suppose along some sequence of carriers

\[
\rho_k(G_k)\le 1-\eta
\]

for a fixed `eta>0` and all sufficiently large `k`. Then

\[
\boxed{
h_k\ge \left(\frac{\eta}{12}-o(1)\right)N_k k.}
\]

### Proof

From C13.9,

\[
1-\eta
\ge
1-\frac6k+
\frac{12-12h_k}{N_k k}.
\]

Therefore

\[
12h_k
\ge
\eta N_k k-\frac{6N_k k}{k}+12
=
\eta N_k k-6N_k+12.
\]

Divide by `12`. Since `6N_k/(N_k k)=6/k->0`, the result follows. QED.

Thus erasing any fixed positive fraction of the growing residue-degree memory requires orientable genus linear in the total port budget.

---

## 8. Interpretation and claim boundary

The theorem uses two standard ingredients:

1. the classical cyclotomic decomposition law;
2. the classical Euler edge bound for simple surface graphs.

The HATTER-specific composed statement is the bridge between them:

> for one fixed rational integer, arithmetic degree growth creates an unbounded port budget, and bounded/subcritical carrier topology is provably unable to erase a positive asymptotic fraction of it.

This is stronger than the unrestricted carrier spectrum alone. Arbitrary dense carriers can achieve `B_f=0`, but surface complexity itself then has a quantified necessary growth cost.

No entropy, payload, coding, or cryptographic claim is implied.