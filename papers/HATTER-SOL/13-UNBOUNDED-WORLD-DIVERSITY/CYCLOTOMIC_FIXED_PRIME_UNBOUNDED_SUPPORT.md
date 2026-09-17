# HATTER-SOL-13 · Fixed Prime, Unbounded Cyclotomic Support

**Status:** exact theorem layer  
**Probe:** the fixed rational prime `2`

## 1. World family

For every integer `k>=2`, set

\[
m_k=2^k-1
\]

and define the cyclotomic world

\[
K_k=\mathbb Q(\zeta_{m_k}).
\]

Because `m_k` is odd, the rational prime `2` is unramified in `K_k`.

For a rational prime `p` with `p\nmid m`, the residue degree of any prime of `Q(zeta_m)` above `p` is

\[
f=\operatorname{ord}_m(p),
\]

and the number of prime ideals above `p` is

\[
g=\frac{\varphi(m)}{f}.
\]

We specialize this standard cyclotomic decomposition law to `p=2` and `m=m_k`.

---

## 2. Exact multiplicative order

### Lemma C13.1

For every `k>=2`,

\[
\boxed{\operatorname{ord}_{2^k-1}(2)=k.}
\]

### Proof

Since

\[
2^k\equiv1\pmod{2^k-1},
\]

the order divides `k` or, more directly, is at most `k`.

Suppose there were an integer `d` with

\[
1\le d<k
\]

and

\[
2^d\equiv1\pmod{2^k-1}.
\]

Then `2^k-1` would divide `2^d-1`. But

\[
0<2^d-1<2^k-1,
\]

which is impossible. Therefore no smaller positive exponent works, and the order is exactly `k`. QED.

---

## 3. Prime-ideal branching count

By the cyclotomic decomposition law and Lemma C13.1,

\[
2\mathcal O_{K_k}
=\mathfrak p_{k,1}\cdots\mathfrak p_{k,g_k},
\]

with distinct prime ideals, common residue degree `k`, and

\[
\boxed{
g_k=\frac{\varphi(2^k-1)}{k}.}
\]

Thus the fixed rational prime `2` acquires `g_k` canonical prime-ideal directions in the world `K_k`.

---

## 4. Elementary totient lower bound

### Lemma C13.2

For every positive integer `m`,

\[
\boxed{\varphi(m)\ge\sqrt{m/2}.}
\]

### Proof

Write

\[
m=\prod_p p^{a_p}.
\]

Then

\[
\frac{\varphi(m)^2}{m}
=
\prod_{p\mid m}p^{a_p-2}(p-1)^2.
\]

For every odd prime `p` and every `a_p>=1`,

\[
p^{a_p-2}(p-1)^2\ge \frac{(p-1)^2}{p}\ge1.
\]

For `p=2`, the factor equals `1/2` when `a_2=1` and is at least `1` when `a_2>=2`.

Hence the complete product is at least `1/2`, giving

\[
\varphi(m)^2\ge m/2.
\]

Taking square roots proves the claim. QED.

For the present sequence `m_k=2^k-1`, which is odd, the proof actually gives the stronger bound

\[
\varphi(m_k)\ge\sqrt{m_k}.
\]

---

## 5. Unbounded support theorem

### Theorem C13.3 — fixed-prime unbounded cyclotomic support

For

\[
K_k=\mathbb Q(\zeta_{2^k-1}),
\qquad k\ge2,
\]

the number of prime ideals above the single fixed rational prime `2` satisfies

\[
\boxed{
g_k=\frac{\varphi(2^k-1)}{k}\to\infty.}
\]

In particular,

\[
\boxed{
\#\{\mathfrak p:\mathfrak p\mid2\mathcal O_{K_k}\}
\to\infty.
}
\]

### Proof

Because `2^k-1` is odd, Lemma C13.2 yields

\[
\varphi(2^k-1)\ge\sqrt{2^k-1}.
\]

Therefore

\[
g_k
\ge
\frac{\sqrt{2^k-1}}{k}.
\]

The numerator grows exponentially in `k/2`, while the denominator grows linearly. Hence the right-hand side tends to infinity. QED.

---

## 6. Immediate observer consequence

Define the intrinsic ideal-support observer

\[
O_{supp}(p,K)
:=
\#\{\mathfrak p\subset\mathcal O_K:\mathfrak p\mid p\mathcal O_K\}.
\]

Then Theorem C13.3 gives

\[
\boxed{O_{supp}(2,K_k)=g_k\to\infty.}
\]

Thus H13 already has a positive fixed-integer theorem at the arithmetic-state level:

> one fixed rational integer, namely `2`, has unbounded canonical prime-ideal support across a natural sequence of cyclotomic worlds.

This is stronger than merely having infinitely many world addresses: the observer values themselves are unbounded.

---

## 7. Claim boundary

The theorem proves unbounded **arithmetic structural diversity** for a fixed integer.

It does not yet prove:

- unbounded HATTER Pareto-polynomial diversity;
- unbounded network-response rank;
- independent information or entropy;
- arbitrary payload capacity.

The next nontrivial question is whether a canonical HATTER network/carrier construction preserves an unbounded amount of this growing prime-ideal support or collapses it to finitely many response classes.
