# Tenth Strike — Odd-Cycle Exclusion Is False

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-30  
**Status:** theorem proved; publication status not assigned

## 1. Question

The ninth strike reduced one route to the binary singleton problem to the conjecture that the residual digraph on

\[
C:=\{p\in\mathbb P:p\equiv2\pmod3\}
\]

has no directed odd cycle. Here

\[
p\to r
\iff
p\ne r\text{ and }r\mid N_p,
\qquad
N_p:=\tau(p)^2-p^{11}=\tau(p^2).
\]

This conjecture is false.

---

## 2. Exact counterexample

### Theorem 2.1 — Directed 5-cycle

In the residual digraph \(\Gamma_\Delta[C]\) there is a directed cycle of odd length five:

\[
\boxed{
123527\to83\to71\to1013\to3851\to123527.
}
\tag{1}
\]

All five vertices are distinct primes congruent to \(2\pmod3\).

### Proof

The exact Ramanujan values are

\[
\tau(123527)=-8034037806268003486479195624,
\tag{2}
\]

\[
\tau(83)=-29335099668,
\tag{3}
\]

\[
\tau(71)=9791485272,
\tag{4}
\]

\[
\tau(1013)=8078051360921262,
\tag{5}
\]

\[
\tau(3851)=-32727126447082175148.
\tag{6}
\]

Direct exact integer arithmetic gives the following divisibility certificates:

\[
\tau(123527)^2-123527^{11}
=83\cdot
(-453466880878006246740741427121673566040288427106659309),
\tag{7}
\]

\[
\tau(83)^2-83^{11}
=71\cdot
(-6018075295867494733),
\tag{8}
\]

\[
\tau(71)^2-71^{11}
=1013\cdot
(-133513433652427099),
\tag{9}
\]

\[
\tau(1013)^2-1013^{11}
=3851\cdot
(-282371381492732302217549914843),
\tag{10}
\]

and

\[
\tau(3851)^2-3851^{11}
=123527\cdot
(-13693168457233749257210442750431461).
\tag{11}
\]

Therefore every arrow in (1) is an edge of \(\Gamma_\Delta\).

Finally,

\[
123527\equiv83\equiv71\equiv1013\equiv3851\equiv2\pmod3,
\]

and deterministic trial division up to the square root verifies primality of all five numbers. Hence the whole cycle lies in \(C\). ∎

---

## 3. Small modular certificate

The same five edges can be checked from the following compact residue table.

| source \(p\) | marker \(r\) | \(\tau(p)\bmod r\) | \(p^{11}\bmod r\) | \(\tau(p)^2\bmod r\) |
|---:|---:|---:|---:|---:|
| 123527 | 83 | 4 | 16 | 16 |
| 83 | 71 | 10 | 29 | 29 |
| 71 | 1013 | 495 | 892 | 892 |
| 1013 | 3851 | 1269 | 643 | 643 |
| 3851 | 123527 | 68968 | 54362 | 54362 |

Thus each successor divides \(\tau(p)^2-p^{11}\).

---

## 4. Independent exact verification of the Ramanujan values

The values (2)–(6) were independently recomputed by Niebur's exact formula

\[
\tau(n)
=n^4\sigma_1(n)
-24\sum_{k=1}^{n-1}
\left(35k^4-52k^3n+18k^2n^2\right)
\sigma_1(k)\sigma_1(n-k).
\tag{12}
\]

The accompanying standard-library verifier recomputes the divisor sums, evaluates (12) in exact integers, checks the five primes, and verifies all five divisibilities.

No floating-point arithmetic, probabilistic primality test, Lehmer conjecture, or unproved number-theoretic assumption is used in the certificate.

---

## 5. Quadratic reciprocity alone cannot prove odd-cycle exclusion

Every residual edge between distinct odd primes satisfies

\[
p\to r
\Longrightarrow
\left(\frac pr\right)=1.
\tag{13}
\]

However, even the combination

- \(p_i\equiv2\pmod3\), and
- \(\left(\frac{p_i}{p_{i+1}}\right)=1\) cyclically,

is compatible with an odd cycle at the pure reciprocity level.

Indeed the three primes

\[
5,11,89\equiv2\pmod3
\]

satisfy

\[
\left(\frac5{11}\right)
=
\left(\frac{11}{89}\right)
=
\left(\frac{89}{5}\right)
=1,
\tag{14}
\]

with explicit square witnesses

\[
4^2\equiv5\pmod{11},
\qquad
10^2\equiv11\pmod{89},
\qquad
2^2\equiv89\pmod5.
\tag{15}
\]

Therefore no argument using only the necessary Legendre-symbol constraints and quadratic reciprocity can rule out directed odd cycles.

The actual 5-cycle (1) shows that the stronger Ramanujan divisibility relation itself also permits them.

---

## 6. Bounded exhaustive search record

An exact bounded search on \(C\) found:

- no directed odd cycle with every vertex at most \(123526\);
- at cutoff \(123527\), the 5-cycle (1) appears;
- the previously known 4-cycle
  \[
  83\to71\to347\to443\to83
  \]
  remains present.

This is a computational minimality statement relative to the maximum-vertex cutoff, not an independent structural theorem and not needed for Theorem 2.1.

The bounded search computed the \(q\)-expansion from

\[
\Delta(q)=q\left(\sum_{j\ge0}(-1)^j(2j+1)q^{j(j+1)/2}\right)^8,
\tag{16}
\]

using exact modular NTT arithmetic and CRT reconstruction; Deligne's bound

\[
|\tau(p)|\le2p^{11/2}
\]

makes the reconstruction unique. Candidate residual divisors were then checked by exact integer divisibility.

---

## 7. Consequence for the binary singleton program

The conditional route

\[
\text{odd-cycle exclusion}
\Longrightarrow
\text{Richardson kernel}
\Longrightarrow
\text{binary singleton}
\]

is closed: its first premise is false.

This does **not** show that the corridor digraph

\[
H=\Gamma_\Delta[C\setminus\{2\}]
\]

has no kernel. Directed graphs containing odd cycles may still possess kernels, and the cycle vertices have outgoing residual divisors outside the five-cycle.

For example, full factorization gives

\[
D(123527)\cap C
\supset
\{83,6815279995247,39835403227071167\},
\tag{17}
\]

so the discovered odd cycle is not a terminal isolated obstruction.

The correct remaining question is therefore the direct one:

\[
\boxed{
\text{Does }H\text{ itself have a kernel?}
}
\tag{18}
\]

Any further attack must use more than odd-cycle exclusion or bare quadratic reciprocity.

---

## 8. Hostile audit

1. **Are all five vertices in the mod-3 corridor?** Yes; each is prime and congruent to \(2\pmod3\).
2. **Are the arrows merely Legendre-symbol candidates?** No; (7)–(11) are exact divisibility identities for \(N_p=\tau(p)^2-p^{11}\).
3. **Could a wrong \(\tau\)-value create the cycle?** The values are recomputed from the independent exact Niebur formula in the verifier.
4. **Is numerical rounding involved?** No.
5. **Does the counterexample depend on Lehmer's conjecture?** No.
6. **Does the 5-cycle itself prove nonexistence of a kernel?** No; that stronger claim is explicitly not made.
7. **Is the “first” claim global?** No; it is only the result of an exhaustive bounded search ordered by maximum vertex.
8. **Can quadratic reciprocity still exclude odd cycles after adding further Ramanujan-specific constraints?** Possibly; what is disproved is the use of bare residue-symbol necessity as a complete obstruction, and the actual cycle disproves total odd-cycle exclusion itself.

**Audit verdict:** PASS for the directed 5-cycle counterexample and for the failure of the odd-cycle-exclusion conjecture.
