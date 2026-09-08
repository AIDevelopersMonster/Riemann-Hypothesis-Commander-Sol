# First Strike — Finite-Subset Carrier versus Full Multiplicative Source

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-28  
**Status:** research checkpoint; proved statements only

## 1. Question

The v1.1 review asks whether the multiplicative source sort

\[
(\mathbb N_{>0},\times,1)
\]

is stronger than necessary for the amplifying side. The proof of the Support-Cardinality Wall uses source multiplication mainly to obtain finite sets of prime vertices and marker primes through squarefree products and divisibility.

We therefore replace the source arithmetic memory by a canonical finite-subset carrier and ask whether the graph-universality/undecidability mechanism survives.

## 2. The weaker carrier

Let \(\mathbb P\) be the set of rational primes and let

\[
\operatorname{Fin}(\mathbb P)
\]

be the set of finite subsets of \(\mathbb P\).

Consider a two-sorted source memory consisting of:

- a prime sort \(P\), with equality only;
- a finite-set sort \(F=\operatorname{Fin}(P)\);
- the membership relation

\[
M(p,A)\iff p\in A.
\]

Keep the target sort \((\mathbb Q,+,0)\), the Ramanujan bridge \(U_\Delta\), and the threshold predicate \(B_\kappa\). Call the resulting structure

\[
\mathcal F_{\Delta,\kappa}.
\]

No multiplication, source integer constants, divisibility, or prime-factorization coding is present.

## 3. Residual incidence does not use source multiplication

Define exactly as before

\[
E_\kappa(p;r)
:\iff
p\ne r\land\exists x\,(U_\Delta(p,x)\land B_\kappa(r,x)).
\]

For \(r\in P_{\mathrm{pos}}(\kappa)\) and \(p\ne r\),

\[
E_\kappa(p;r)
\iff
r^{\kappa(r)}\mid \tau(p)^2-p^{11}.
\]

This formula and its number-theoretic proof use only the prime sort, target sort, bridge, and threshold predicate.

Therefore the full finite-pattern realization theorem from the Support-Cardinality proof remains valid verbatim on the prime sort of \(\mathcal F_{\Delta,\kappa}\): for every finite good marker set \(R\subseteq P_{\mathrm{pos}}(\kappa)\) and every \(T\subseteq R\), infinitely many source primes \(p\) satisfy

\[
E_\kappa(p;r)\iff r\in T
\qquad(r\in R).
\]

The only external inputs remain adelic independence and Chebotarev.

## 4. Infinite GIR survives unchanged

Let

\[
I_\kappa(p,q;r)
:=E_\kappa(p;r)\land E_\kappa(q;r).
\]

The same row/column realization gives, for every \(n\), pairwise distinct primes \(p_i,q_j,r_{ij}\) such that

\[
I_\kappa(p_k,q_\ell;r_{ij})
\iff
(k,\ell)=(i,j).
\]

Hence

\[
\boxed{
\operatorname{GIR}(I_\kappa)=\infty
}
\]

in the weaker finite-subset-carrier structure as soon as \(P_{\mathrm{pos}}(\kappa)\) is infinite.

This proves that source multiplication is not responsible for the GIR explosion.

## 5. Finite graph coding using genuine finite sets

In the original proof a squarefree source integer \(a\) encoded a finite vertex set through its prime divisors. In \(\mathcal F_{\Delta,\kappa}\) we can use a finite-set element directly.

For \(A\in F\), its vertex domain is simply

\[
D_A(x):=M(x,A).
\]

For a marker set \(N\in F\), define

\[
R_N(x,y)
:\iff
\exists r\,(M(r,N)\land I_\kappa(x,y;r)).
\]

Given an \(n\times n\) GIR grid \((p_i,q_j,r_{ij})\), let

\[
A=\{p_1,\dots,p_n\},
\qquad
C=\{q_1,\dots,q_n\},
\]

and let

\[
M_0=\{r_{11},\dots,r_{nn}\}.
\]

Then \(R_{M_0}\) is a bijection from \(A\) to \(C\).

For a finite directed graph \(G\subseteq[n]^2\), put

\[
N_G=\{r_{ij}:(i,j)\in G\}.
\]

Define

\[
G_{A,C,M_0,N}(x,z)
:\iff
\exists y\,
\bigl(
M(y,C)
\land R_{M_0}(z,y)
\land R_N(x,y)
\bigr).
\]

Then

\[
G_{A,C,M_0,N_G}(p_i,p_j)
\iff
(i,j)\in G.
\]

No multiplication is used anywhere in this coding.

## 6. Reverse direction

Define \(\operatorname{Bij}(A,C,M_0)\) by the usual first-order uniqueness clauses saying that \(R_{M_0}\) is a bijection between the finite membership domains \(D_A\) and \(D_C\).

For any witnesses \(A,C,M_0,N\) satisfying \(A\ne\varnothing\) and \(\operatorname{Bij}(A,C,M_0)\), the formula \(G_{A,C,M_0,N}\) defines some binary relation on the finite set \(D_A\).

Therefore every graph sentence \(\varphi\) in one binary relation admits an effective translation \(\widehat\varphi\) obtained by:

1. existentially quantifying \(A,C,M_0,N\) in the finite-set sort;
2. requiring \(D_A\ne\varnothing\) and \(\operatorname{Bij}(A,C,M_0)\);
3. relativizing graph quantifiers to \(D_A\);
4. replacing the graph atom by \(G_{A,C,M_0,N}\).

Exactly as before,

\[
\varphi\text{ has a finite nonempty model}
\iff
\mathcal F_{\Delta,\kappa}\models\widehat\varphi.
\]

The forward direction uses a GIR grid and literal finite sets. The reverse direction uses only finiteness of the finite-set sort elements.

## 7. Theorem — Multiplicative source elimination on the amplifying side

### Theorem 7.1

Assume \(P_{\mathrm{pos}}(\kappa)\) is infinite. Then in the structure \(\mathcal F_{\Delta,\kappa}\), whose source memory is only the incidence structure

\[
(P,\operatorname{Fin}(P),M),
\]

one fixed parameter-free ternary formula has infinite GIR, every finite directed graph is uniformly coded, and

\[
\boxed{
\operatorname{Th}(\mathcal F_{\Delta,\kappa})
\text{ is undecidable}.
}
\]

### Proof

Infinite GIR is proved in Section 4. Uniform finite graph coding and both directions of the finite-model reduction are proved in Sections 5-6. Trakhtenbrot's theorem then implies undecidability of the complete theory. ∎

## 8. Exact conclusion of the first strike

The full multiplicative Skolem source sort is **not necessary** for the wild side of the Support-Cardinality Wall.

The actual combinatorial memory needed by the graph-universality proof is much weaker:

\[
\boxed{
\text{prime atoms}
+
\text{finite-set membership}
+
\text{residual incidence}.
}
\]

Thus source multiplication was serving primarily as an internal implementation of finite-set memory by squarefree products. Once genuine finite subsets are supplied directly, the same wild phase survives.

## 9. What this does not prove

This theorem does not say that the finite-subset carrier is minimal. In particular, it remains open whether even the explicit finite-set sort can be removed.

The next natural question is:

> Does the prime sort together with the ternary residual isolator \(I_\kappa\), but with no multiplication and no finite-set sort, already have an undecidable complete theory?

Infinite GIR alone does not immediately provide quantifiable finite graph domains. The missing issue is **internal finite-domain packaging**.

This is now the sharper candidate boundary beyond the Support-Cardinality Wall.