# HATTER-SOL-13 · Local Ideal-Type Polynomial and Unbounded Rank

**Status:** exact theorem layer  
**Probe:** fixed rational prime `2`  
**Worlds:** `K_k = Q(zeta_{2^k-1})`

## 1. Why HATTER-SOL-10 cannot be copied verbatim

The ideal typed state of HATTER-SOL-10 was built for imaginary quadratic fields and inherited a two-coordinate element geometry from HATTER-SOL-09. The present cyclotomic worlds have growing degree, so there is no canonical reason to force them into the same two-coordinate interface.

Therefore H13 uses the intrinsic local ideal decomposition data itself.

For a number field `K` and a rational prime `p`, write

\[
p\mathcal O_K=\prod_{i=1}^{g}\mathfrak p_i^{e_i},
\]

with residue degrees

\[
f_i=[\mathcal O_K/\mathfrak p_i:\mathbf F_p].
\]

Define the local ideal-type polynomial

\[
\boxed{
A_{K,p}(E,F)
:=
\sum_{i=1}^{g}E^{e_i}F^{f_i}.
}
\]

This polynomial introduces no external labels. It records only the canonical ramification and residue-degree multiset above `p`.

The transform itself is not claimed as new number theory; it is a compact HATTER observer for local ideal structure.

---

## 2. Exact cyclotomic specialization

For

\[
K_k=\mathbb Q(\zeta_{2^k-1}),
\]

the prime `2` is unramified and every prime ideal above it has

\[
e_i=1,
\qquad
f_i=k.
\]

The number of primes above `2` is

\[
g_k=\frac{\varphi(2^k-1)}{k}.
\]

Therefore

\[
\boxed{
A_k(E,F):=A_{K_k,2}(E,F)
=g_k E F^k.
}
\]

---

## 3. Galois-symmetry no-go at the individual-node level

The extension `K_k/Q` is Galois. Hence the Galois group acts transitively on the prime ideals above the unramified rational prime `2`.

Consequently every Galois-invariant observer of a **single** prime ideal that depends only on its local decomposition type assigns the same value to all `g_k` primes above `2`.

Thus the growing arithmetic richness in this family is not obtained by giving the individual prime ideals different local labels. It resides in

1. their growing multiplicity `g_k`, and
2. their common residue degree `k`.

This is a useful symmetry obstruction: any richer observer must aggregate the prime-ideal family or introduce genuinely nonlocal arithmetic data.

---

## 4. Linear independence theorem

### Theorem C13.8 — unbounded local ideal-type polynomial rank

The family

\[
\{A_k(E,F):k\ge2\}
\]

is linearly independent over `Q`.

### Proof

For each `k`,

\[
A_k(E,F)=g_k E F^k,
\]

with `g_k>0`.

Suppose

\[
\sum_{k=2}^{m}c_kA_k(E,F)=0
\]

for rational coefficients `c_k`. Then

\[
E\sum_{k=2}^{m}c_kg_kF^k=0.
\]

Since the monomials

\[
F^2,F^3,\ldots,F^m
\]

are linearly independent in `Q[F]`, every coefficient satisfies

\[
c_kg_k=0.
\]

Because `g_k>0`, we obtain `c_k=0` for every `k`. QED.

Therefore, if

\[
r_m^{loc}(2)
:=
\dim_Q\operatorname{span}\{A_k(E,F):2\le k\le m\},
\]

then

\[
\boxed{r_m^{loc}(2)=m-1.}
\]

In particular,

\[
\boxed{r_m^{loc}(2)\to\infty.}
\]

---

## 5. Difference-rank version

H13 originally proposed the centered rank

\[
\widetilde r_m(2)
=
\dim_Q\operatorname{span}
\{A_k-A_2:3\le k\le m\}.
\]

### Corollary C13.8a

For every `m>=3`,

\[
\boxed{\widetilde r_m(2)=m-2.}
\]

### Proof

Suppose

\[
\sum_{k=3}^{m}c_k(A_k-A_2)=0.
\]

Then

\[
\sum_{k=3}^{m}c_kA_k
-\left(\sum_{k=3}^{m}c_k\right)A_2=0.
\]

By Theorem C13.8, the family `A_2,...,A_m` is linearly independent. Hence every `c_k=0`. QED.

Thus H13 achieves the stronger target proposed in its original research specification: one fixed rational integer has a canonical world-response family of unbounded linear rank.

---

## 6. Relation to the scalar carrier theorem

The local ideal-type polynomial and the residue-degree port lift retain different aspects of the same arithmetic decomposition.

The polynomial

\[
A_k=g_kEF^k
\]

sees both the multiplicity `g_k` and the common local degree `k` symbolically.

The scalar port lift assigns capacity `k` to each of the `g_k` prime-ideal nodes and produces the exact connected-carrier spectrum

\[
\mathcal B_k
=
\{0,2,4,\ldots,g_k(k-2)+2\}.
\]

Hence H13 now has two independent forms of unboundedness:

1. **world-direction rank:** the polynomial family `A_k` has unbounded linear rank;
2. **within-world carrier diversity:** `|B_k|` grows without bound.

---

## 7. Claim boundary

What is proved:

- a canonical local ideal-decomposition polynomial for the fixed rational prime `2`;
- exact formula `A_k=g_k E F^k` in the chosen cyclotomic worlds;
- unbounded linear rank of this polynomial-valued world response;
- Galois symmetry prevents local decomposition type from distinguishing the individual primes above `2` inside a fixed world.

What is not claimed:

- novelty of the classical decomposition invariants `(e_i,f_i)` themselves;
- entropy or independent payload equal to the polynomial rank;
- cryptographic hardness;
- equivalence with the quadratic two-coordinate ideal typed state of HATTER-SOL-10.

The novelty candidate is the composed HATTER statement: a single fixed rational integer supports a natural arithmetic-world response with provably unbounded symbolic rank, while carrier wiring admits an exact independent survival/collapse spectrum.