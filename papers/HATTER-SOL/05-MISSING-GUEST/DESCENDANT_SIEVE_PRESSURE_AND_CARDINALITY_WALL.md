# HATTER-SOL-05 · Descendant Sieve Pressure and the Cardinality Wall

## 0. Purpose

The previous strike found a rigorous parameter-space asymmetry between

\[
X_{\{2,3\}}
\quad\text{and}\quad
X_{\{2,5\}},
\]

but this did not yet produce a graph-visible killing certificate for the seed transposition

\[
\tau=(3\ 5).
\]

The promised next attack was to ask whether the asymmetry becomes stronger after passing to exact descendants.

It does: the asymmetry is **hereditary** along every exact-support descendant chain that contains \(3\) but not \(5\), and under the swapped chain the corresponding missing-prime sieve is always stronger by a fixed factor.

However, the same analysis exposes a hard barrier:

\[
\boxed{
\text{the multiplicity tower remembers cardinality, not parameter-space abundance.}
}
\]

Thus even an exponentially accumulating sieve-pressure gap cannot kill an automorphism if every paired exact fiber remains countably infinite.

This note makes both statements exact.

---

# 1. Local divisor profile of an exact support

Fix a finite support

\[
S=\{q_1,\dots,q_k\}\subset\mathbb P,
\qquad 2\in S,
\]

and write

\[
N_S(\mathbf e)
=
1+\prod_{q\in S}q^{e_q},
\qquad
\mathbf e\in\mathbb N_{>0}^{S}.
\]

Let \(\ell\notin S\) be a prime. Define the subgroup

\[
H_\ell(S)
=
\left\langle q\bmod\ell:q\in S\right\rangle
\le(\mathbb Z/\ell\mathbb Z)^\times.
\]

The exponent vector induces a homomorphism from the finite exponent-period group onto \(H_\ell(S)\):

\[
\mathbf e
\longmapsto
\prod_{q\in S}q^{e_q}\pmod\ell.
\]

## Theorem 1.1 — exact one-prime local divisor density

As the exponent vector ranges over a large box \([1,B]^S\), the relative density of vectors satisfying

\[
\ell\mid N_S(\mathbf e)
\]

converges to

\[
\boxed{
\delta_\ell(S)
=
\begin{cases}
|H_\ell(S)|^{-1},&-1\in H_\ell(S),\\[4pt]
0,&-1\notin H_\ell(S).
\end{cases}
}
\]

### Proof

Let

\[
M=\operatorname{lcm}_{q\in S}\operatorname{ord}_\ell(q).
\]

The residue of \(N_S(\mathbf e)\) modulo \(\ell\) depends only on the exponent vector modulo \(M\). Therefore box density is the uniform density on the finite torus \((\mathbb Z/M\mathbb Z)^S\).

The map

\[
\Phi:(\mathbb Z/M\mathbb Z)^S\to H_\ell(S),
\qquad
\Phi(\mathbf e)=\prod q^{e_q},
\]

is a surjective group homomorphism. Hence all fibers of \(\Phi\) have equal cardinality and the image is uniformly distributed on \(H_\ell(S)\).

Now

\[
\ell\mid N_S(\mathbf e)
\iff
\Phi(\mathbf e)=-1.
\]

If \(-1\notin H_\ell(S)\), the density is zero. If \(-1\in H_\ell(S)\), exactly one of the \(|H_\ell(S)|\) equally likely image elements is bad. \(\square\)

---

# 2. The universal 3-versus-5 local gap

Because \(2\) is a primitive root modulo both \(3\) and \(5\),

\[
\langle2\rangle=(\mathbb Z/3\mathbb Z)^\times
\]

and

\[
\langle2\rangle=(\mathbb Z/5\mathbb Z)^\times.
\]

Therefore the rest of the support is irrelevant for these two local factors.

## Corollary 2.1

For every finite support \(S\ni2\):

- if \(3\notin S\), then
  \[
  \boxed{\delta_3(S)=\frac12;}
  \]
- if \(5\notin S\), then
  \[
  \boxed{\delta_5(S)=\frac14.}
  \]

If \(3\in S\), then of course

\[
N_S(\mathbf e)\equiv1\pmod3,
\]

and if \(5\in S\), then

\[
N_S(\mathbf e)\equiv1\pmod5.
\]

So an excluded \(3\) removes one half of all exponent vectors, whereas an excluded \(5\) removes only one quarter.

---

# 3. \(\tau\)-pure supports

Call a finite support \(S\) **3-pure with respect to \(\tau\)** if

\[
2,3\in S,
\qquad
5\notin S.
\]

Under any extension \(g\) of the seed transposition

\[
g(3)=5,
\qquad
g(5)=3,
\]

the image support satisfies

\[
2,5\in gS,
\qquad
3\notin gS.
\]

Thus the local obstruction at the prime omitted by the support changes from \(5\) on the original side to \(3\) on the image side.

## Theorem 3.1 — hereditary descendant sieve-pressure gap

Let \(S\) be 3-pure and let \(g\) be any partial or global graph automorphism extending \((3\ 5)\) on every vertex of \(S\). Then

\[
\boxed{
1-\delta_5(S)=\frac34,
\qquad
1-\delta_3(gS)=\frac12.
}
\]

Hence the ratio of the corresponding one-prime local survival proportions is

\[
\boxed{
\frac{1-\delta_5(S)}{1-\delta_3(gS)}
=
\frac32.
}
\]

This factor is independent of:

- the size of \(S\);
- the identities of all other primes in \(S\);
- the particular way the other vertices are moved by \(g\).

### Proof

Apply Corollary 2.1. The original support omits \(5\), so its mod-5 survival proportion is \(3/4\). The image support omits \(3\), so its mod-3 survival proportion is \(1/2\). \(\square\)

---

# 4. The gap survives exact descendants

Suppose

\[
p\in X_S
\]

for a 3-pure support \(S\), and suppose the next support is formed by adjoining this exact descendant:

\[
S^+=S\cup\{p\}.
\]

Because \(5\notin S\) and \(\operatorname{Pred}(p)=S\), we have

\[
5\nmid p-1.
\]

Nothing forces \(p=5\), and in fact \(p>\max S\ge3\), so \(p\ne5\). Therefore

\[
5\notin S^+,
\qquad
3\in S^+.
\]

Thus \(S^+\) is again 3-pure.

The same holds recursively.

## Corollary 4.1 — hereditary purity

Every exact-support descendant chain

\[
S_0\subset S_1\subset\cdots\subset S_m
\]

obtained by repeatedly adjoining a prime from \(X_{S_j}\), starting from a 3-pure support and never manually adjoining \(5\), remains 3-pure.

Under an automorphism extending \((3\ 5)\), its image chain is 5-pure:

\[
2,5\in gS_j,
\qquad
3\notin gS_j.
\]

Consequently, the factor \(3/2\) from Theorem 3.1 reappears at **every level** of such a paired descendant chain.

---

# 5. Cumulative sieve pressure

For a finite 3-pure descendant chain

\[
\mathcal S=(S_0,S_1,\ldots,S_m),
\]

define the external local-pressure functional

\[
\mathfrak P_5(\mathcal S)
=
\prod_{j=0}^m
(1-\delta_5(S_j)).
\]

For its swapped image chain define

\[
\mathfrak P_3(g\mathcal S)
=
\prod_{j=0}^m
(1-\delta_3(gS_j)).
\]

## Corollary 5.1 — exponential pressure gap

\[
\boxed{
\frac{\mathfrak P_5(\mathcal S)}
{\mathfrak P_3(g\mathcal S)}
=
\left(\frac32\right)^{m+1}.
}
\]

Thus exact descendants do amplify the local arithmetic asymmetry: the parameter-space discrepancy grows exponentially with descendant depth.

But this quantity is **external** to the language of the radical-predecessor graph.

---

# 6. Compatibility with the cyclotomic obstruction

Let

\[
k=|S|\ge2.
\]

From the previous strike, the density of exponent vectors whose common gcd has no odd prime divisor is

\[
c_k
=
\frac1{\zeta(k)(1-2^{-k})}.
\]

For the omitted primes \(3\) and \(5\), the bad local condition is invariant under multiplying the whole exponent vector by an odd integer: if the product of support residues is \(-1\), then raising it to an odd power leaves \(-1\).

Therefore Möbius inversion over odd common divisors combines with the local sieve exactly as in the two-dimensional calculation.

## Theorem 6.1 — cyclotomic-plus-local densities

For every 3-pure support \(S\) of size \(k\ge2\), the density of exponent vectors surviving both

1. the universal common-odd-divisor factorization obstruction, and
2. divisibility by the omitted prime \(5\),

is

\[
\boxed{
\frac34\,c_k.
}
\]

For the swapped support \(gS\), the corresponding density after excluding divisibility by the omitted prime \(3\) is

\[
\boxed{
\frac12\,c_k.
}
\]

Hence the ratio remains exactly

\[
\boxed{\frac32.}
\]

The local gap therefore persists in every support dimension.

---

# 7. The cardinality wall

The multiplicity tower from HATTER-SOL-04 does not record exponent vectors. It records only

\[
\mu(S)=|X_S|.
\]

Because the full prime graph is countable,

\[
\mu(S)\in
\{0,1,2,\ldots,\aleph_0\}.
\]

This produces a severe loss of arithmetic information.

## Theorem 7.1 — cardinality blindness of infinite fibers

Let \(S,T\) be finite supports. If both exact fibers are infinite, then

\[
\boxed{
\mu(S)=\mu(T)=\aleph_0,
}
\]

regardless of any differences in:

- local sieve densities;
- growth rates of prime values;
- singular-series constants;
- exponent-distribution laws;
- numerical density of the prime values.

Therefore none of these quantitative differences, by itself, can prevent a multiplicity-tower extension between \(S\) and \(T\).

### Proof

Every exact fiber is a subset of the countable set of primes. Hence every infinite fiber is countably infinite. The extension criterion at one tower level compares only the cardinalities \(\mu(S)\) and \(\mu(T)\). \(\square\)

This is elementary but strategically decisive.

---

# 8. Consequence for the \(3\leftrightarrow5\) programme

The hereditary sieve-pressure gap does **not** kill the seed swap if all paired descendant fibers are infinite.

Even an arbitrarily large discrepancy such as

\[
\left(\frac32\right)^m
\]

in an external parameter-space pressure is collapsed by the graph to the same value

\[
\aleph_0
\]

on both sides.

Thus there are only three graph-visible ways for arithmetic abundance to matter at a given exact support:

\[
\boxed{
\text{empty vs nonempty},
}
\]

\[
\boxed{
\text{finite vs infinite},
}
\]

or

\[
\boxed{
\text{different finite cardinalities}.}
\]

Asymptotic counting constants are invisible once both fibers are infinite.

---

# 9. A no-go theorem for local descendant amplification

Combine:

- the finite-divisor escape theorem from the previous strike;
- hereditary exact-support purity;
- Theorem 7.1.

## Theorem 9.1 — local descendant amplification barrier

No argument based solely on finitely many fixed congruence divisors at finitely many exact-descendant levels can produce a killing certificate for \((3\ 5)\).

More precisely, at every finite support encountered in such a descendant construction:

1. the candidate family escapes every finite set of fixed prime divisors;
2. the mod-3/mod-5 local sieve may create a quantitative asymmetry, but leaves a positive-density periodic set of exponent vectors;
3. if the surviving prime-value sets on both sides are infinite, the multiplicity tower identifies both cardinalities with \(\aleph_0\).

Therefore any unconditional killing proof must eventually establish a **global prime-value statement** strong enough to force emptiness or finite cardinality on at least one exact support.

---

# 10. Heuristic dimension test — explicitly non-theorem

The rigorous results above suggest a useful heuristic.

For a support

\[
S=\{q_1,\ldots,q_k\},
\qquad k\ge2,
\]

the number of exponent vectors satisfying

\[
\sum_{i=1}^k e_i\log q_i\le L
\]

is of order

\[
L^k.
\]

After the cyclotomic obstruction and finitely many local sieves, a positive proportion of these vectors remains.

A Cramér-style model assigns primality probability of order \(1/L\) to a candidate of size about \(e^L\). The expected cumulative number of prime values is therefore of order

\[
\boxed{L^{k-1}}.
\]

For \(k\ge2\), this diverges.

In contrast, for \(k=1\), cyclotomic factorization collapses the exponent set to powers of two, and the analogous expected sum is convergent.

This heuristic predicts a genuine phase transition:

\[
\boxed{
|S|=1:\text{ finite-prime behaviour plausible},
}
\]

\[
\boxed{
|S|\ge2:\text{ infinite exact fibers plausible}.
}
\]

It is consistent with the Higher-Fiber Infinitude hypothesis HFI introduced in the previous strike.

This is **not a proof** of HFI and must never be quoted as one. In particular, even infinitude of the classical Pierpont-prime fiber

\[
X_{\{2,3\}}
\]

remains unproved.

---

# 11. What exact descendants taught us

The descendant experiment did not produce the hoped-for finite-height killing certificate.

Instead it gave a sharper picture:

\[
\boxed{
\text{arithmetic sieve asymmetry amplifies down the descendant tree,}
}
\]

but

\[
\boxed{
\text{the graph erases that quantitative asymmetry once both fibers are infinite.}
}
\]

This is the **cardinality wall**.

The wall explains why the automorphism problem can remain difficult even in the presence of strong and persistent numerical asymmetries.

---

# 12. Next strike

There are now two serious routes.

## Route A — attack finite/empty fibers directly

Look for a theorem from exponential Diophantine or prime-value arithmetic that proves, for some explicit support \(S\), that

\[
\mu(S)<\infty
\]

or even

\[
\mu(S)=0.
\]

A mismatch with the swapped support would kill the seed symmetry.

## Route B — formalize the higher-fiber infinitude frontier

Determine the weakest support-wise infinitude hypothesis under which every seed Fermat-layer permutation survives globally, and compare that hypothesis with standard conjectures or heuristics on primes of the form

\[
1+\prod q_i^{e_i}.
\]

The present evidence points toward Route B as the structurally natural direction, while Route A would deliver the stronger breakthrough if an explicit finite fiber can be proved.

## Publication status

Not yet publication-ready as HATTER-SOL-05, but the branch now has a coherent emerging theme of its own:

> **local arithmetic sees a persistent 3-versus-5 asymmetry, while the radical graph is cardinality-blind to it whenever both exact fibers are infinite.**

One more theorem-level advance on the finite/empty-fiber frontier or on the minimal survival hypothesis would likely cross the publication threshold.
