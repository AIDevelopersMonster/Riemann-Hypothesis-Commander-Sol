# HATTER-SOL-21 · H21-LAB-06 RESULT

Status: **CI REPRODUCED / EXACT MECHANISM VALIDATED**

Run:

\`35637122506\`

Range:

\[
n=pq<2^{19},
\qquad
p\ne q
\]

with odd primes \(p,q\).

Distinct semiprimes:

\[
\boxed{90180}.
\]

## 1. Cross-Frobenius theorem

For every declared nonexceptional world and every tested semiprime,

\[
\delta_W(pq)\bmod p
=
\tau^{e_p}
\left(
x^q-\tau^{e_q}(x)
\right),
\]

and symmetrically modulo \(q\).

Exhaustive mismatch count:

\[
\boxed{0}.
\]

Thus the defect modulo one prime factor is controlled by the **other** prime.

This is the precise cross-prime coupling sought in H21.

## 2. Exact factor-exposure criterion

For the two defect coordinates define zero masks

\[
Z_p
=
\{j:d_j\equiv0\pmod p\},
\]

\[
Z_q
=
\{j:d_j\equiv0\pmod q\}.
\]

The theorem states

\[
\boxed{
W\text{ exposes a proper divisor of }pq
\iff
Z_p\ne Z_q.
}
\]

More precisely,

\[
\gcd(pq,d_j)=p
\iff
j\in Z_p\setminus Z_q,
\]

and

\[
\gcd(pq,d_j)=q
\iff
j\in Z_q\setminus Z_p.
\]

Exhaustive theorem mismatch count:

\[
\boxed{0}.
\]

Therefore H21 now has an exact semiprime mechanism, not merely an empirical
factor-coverage observation.

## 3. Important correction to the earlier intuition

Whole-vector local pass/fail asymmetry is only sufficient.

The actual mechanism is finer:

\[
\boxed{
\text{coordinate defect asymmetry}.
}
\]

A world can expose a factor even when neither local defect vector is zero.

Thus the factor observer depends on which defect coordinates the observer
projects to gcds.

## 4. Per-world nonexceptional semiprime exposure

| world | eligible | exposed | fraction | \(p\) only | \(q\) only | both |
|---|---:|---:|---:|---:|---:|---:|
| \(D=-7\) | 82795 | 31206 | 37.690682% | 11709 | 14839 | 4658 |
| \(D=5\) | 80170 | 26492 | 33.044780% | 20384 | 4117 | 1991 |
| \(D=-3\) | 74285 | 0 | **0%** | 0 | 0 | 0 |
| \(D=-11\) | 69374 | 17992 | 25.934788% | 10368 | 7623 | 1 |
| \(D=13\) | 70057 | 12588 | 17.968226% | 12497 | 91 | 0 |
| \(D=-19\) | 77161 | 22443 | 29.085937% | 16792 | 5648 | 3 |

The \(D=-3\) result is structurally important.

In the nonexceptional semiprime layer, this world never creates coordinate
zero-mask asymmetry.

Therefore any factor yield previously attributed to \(D=-3\) must come from
exceptional/precheck mechanisms or from non-semiprime classes.

The observer must distinguish these mechanisms explicitly.

## 5. Two-factor exposure in one world

For \(D=-7\), one world exposes **both** semiprime factors for

\[
\boxed{4658}
\]

eligible semiprimes.

For \(D=5\), the count is

\[
1991.
\]

For \(D=-11,13,-19\), simultaneous two-factor exposure is almost absent.

Thus world quality has more than one dimension:

- any-factor yield;
- directional bias toward the smaller/larger indexed factor;
- two-factor exposure;
- complementarity with other worlds.

## 6. Ordered pair complementarity

The strongest nontrivial gains include:

\[
D=13\to D=-7:
\quad
12588\to38950,
\]

so the second world contributes

\[
\boxed{26362}
\]

new semiprime hits.

Likewise

\[
D=-11\to D=5
\]

adds

\[
\boxed{23859}
\]

new hits.

This confirms that world complementarity is not explained by ranking worlds
only by their individual hit rates.

## 7. Current theorem-level synthesis

The factor-revelation chain is now

\[
\boxed{
pq
\to
\text{cross-Frobenius residuals}
\to
(Z_p,Z_q)
\to
\text{zero-mask asymmetry}
\to
\gcd\text{ factor}.
}
\]

This is the first exact H21 mechanism explaining *why* a world reveals a
factor.

## 8. Hardware consequence

For semiprime factor revelation the FPGA does not need to reconstruct local
CRT components.

The hardware already has the global defect coordinates \(d_0,d_1\).

The theorem guarantees that separate gcd projections

\[
\gcd(n,d_0),
\qquad
\gcd(n,d_1)
\]

are exactly the operational detector of the hidden local zero-mask asymmetry.

Therefore the current two-coordinate defect representation is not merely a
software convenience: it has an exact arithmetic meaning as a factor observer.

## 9. Claim boundary

The CRT and quadratic Frobenius ingredients are classical.

The novelty status of their composition into the H21 world/observer/factor
framework remains unclaimed until a dedicated literature audit.

The theorem itself is exact and does not depend on the finite validation,
which serves as implementation verification.
