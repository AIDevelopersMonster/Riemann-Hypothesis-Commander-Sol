# HATTER-SOL-14 · HOSTILE AUDIT v0.1

**Date:** 2026-09-14  
**Verdict:** PASS for the current theorem spine; publication hardening still required.

## Audited claims

### A. Regular-action to Cayley reduction — PASS

For the regular action of `Gamma_k` on the prime ideals above `2`, every simple undirected equivariant graph is a Cayley graph `Cay(Gamma_k,S)` with `S=S^{-1}` and identity excluded. Connectedness is equivalent to `<S>=Gamma_k`.

This is standard group-action/Cayley theory and is not a novelty claim.

### B. No scalar exhaustion obstruction — PASS

The proposed first obstruction fails: for sufficiently large `k` there exist inverse-closed generating sets of exact size `k`, hence equivariant complete port-budget exhaustion is possible.

This is retained as a negative control, not as the main result.

### C. Equivariant genus cost — PASS

For every fixed `0<eta<=1`, the equivariant minimum genus remains of order

\[
\gamma_k^{Gal}(\eta)=\Theta(n_k k).
\]

Thus Galois equivariance alone does not create a new scalar asymptotic genus barrier.

This is also a negative structural result.

### D. Rational cycle-module formula — PASS

For `C=Cay(Gamma,S)` with inverse-closed decomposition into `p` non-involutory inverse pairs and involution subset `T`,

\[
[H_1(C;Q)]
=(p-1)[QGamma]
+\sum_{\tau\in T}[Ind_{<\tau>}^Gamma \varepsilon_\tau]
+[1].
\]

The formula follows from the equivariant cellular chain sequence. Orientation choices change bases but not the isomorphism class of the edge-orbit representation.

Novelty should not be claimed for the representation-theoretic Euler-characteristic mechanism itself without a dedicated literature audit.

### E. Exact involution fingerprint — PASS

For nonidentity `g in Gamma`, the cycle-space character is

\[
\chi(g)=1-|Gamma|/2
\]

exactly at involutions included in `T`, and equals `1` at all other nonidentity elements.

Therefore the rational equivariant `H_1` module recovers the exact involution subset `T`; its identity character value then recovers the number `p` of non-involutory inverse-pair directions.

### F. Infinite arithmetic same-graph separation — PASS

For every sufficiently large

\[
k\equiv15\pmod{30},
\]

we have `7*31 | 2^k-1` and `k` odd. The quotient by the odd-order decomposition subgroup `<2>` preserves the full 2-primary part of the unit group. The prime-power CRT factors at `7` and `31` each contribute a direct `C_2` factor, so

\[
Gamma_k\cong C_2\oplus C_2\oplus H_k.
\]

Choose basis involutions `a,c` of the displayed `C_2^2` and an inverse-closed generating set `R_k` of `H_k`. Then

\[
S_{k,1}=R_k\cup\{a,c\},
\qquad
S_{k,2}=R_k\cup\{a+c,c\}
\]

are related by a group automorphism and therefore define isomorphic abstract Cayley graphs, but their equivariant `H_1` characters differ at `a`.

Capacity feasibility holds for all sufficiently large `k` because

\[
|R_k|\le2\omega(2^k-1)=O(k/\log k)=o(k).
\]

Hence the degree is eventually at most the HATTER capacity `k`.

## Claim discipline after audit

What is proved:

- scalar Galois equivariance does not strengthen the H13 asymptotic genus barrier;
- equivariant first homology is strictly finer than scalar boundary, ordinary genus, and even abstract graph isomorphism type;
- this strict separation occurs in infinitely many arithmetic worlds.

What is not yet claimed:

- novelty of the general Cayley/cycle-module representation formula;
- integral classification of `H_1` as a `Z[Gamma_k]`-module;
- entropy, payload, coding, cryptographic hardness, or physical memory;
- optimal classification for every `k`.

## Publication gate

The project has crossed the internal theorem threshold because the infinite same-graph separation theorem is nontrivial and survives scalar and ordinary-topological quotienting.

Before publication: perform prior-art audit, consolidate theorem numbering, produce an article architecture, and test whether the rational theorem can be strengthened integrally or sharpened to a fuller classification.