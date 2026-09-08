# Second Strike — Prime-Only Residual Structure and the Source/Marker Alignment Wall

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-28  
**Status:** proved statements only; publication status not assigned

## 1. Question

The first strike showed that on the amplifying side the full multiplicative source sort may be replaced by an explicit finite-subset carrier

\[
(P,\operatorname{Fin}(P),\in).
\]

The sharper question is whether the finite-set sort itself can be removed.

Let

\[
\mathcal I_\kappa=(P,I_\kappa)
\]

be the **prime-only residual structure**, where the universe is the set of rational primes and

\[
I_\kappa(p,q;r)
:=E_\kappa(p;r)\land E_\kappa(q;r),
\]

with

\[
E_\kappa(p;r)
\iff
p\ne r\land r^{\kappa(r)}\mid \tau(p)^2-p^{11}
\]

when \(\kappa(r)>0\), while for \(\kappa(r)=0\) and \(p\ne r\) the relation \(E_\kappa(p;r)\) is automatic.

Inside \(\mathcal I_\kappa\), the binary incidence is already definable:

\[
E(x;r):=I_\kappa(x,x;r).
\tag{1}
\]

No multiplication, target sort, bridge symbol, divisibility, or explicit finite-set sort remains in the language.

The result of this strike is twofold:

1. finite-set packaging is in fact internally recoverable from differences of residual rows;
2. the remaining obstruction for arbitrary infinite support is not packaging but **source/marker role alignment**.

---

## 2. Every positive row has finite support

For a source prime \(p\), put

\[
N_p:=\tau(p)^2-p^{11}\in\mathbb Z.
\tag{2}
\]

### Lemma 2.1 — Nonvanishing of the residual integer

For every prime \(p\),

\[
N_p\ne0.
\tag{3}
\]

### Proof

If \(N_p=0\), then

\[
\tau(p)^2=p^{11}.
\tag{4}
\]

Taking \(p\)-adic valuations gives

\[
2v_p(\tau(p))=11,
\tag{5}
\]

which is impossible because the left side is even and the right side is odd. Hence \(N_p\ne0\). ∎

### Lemma 2.2 — Finite positive edge support

For every source prime \(p\), the set

\[
S_p^+
:=
\{r:\kappa(r)>0,\ r\ne p,\ E(p;r)\}
\tag{6}
\]

is finite.

### Proof

If \(r\in S_p^+\), then

\[
r^{\kappa(r)}\mid N_p,
\tag{7}
\]

so in particular \(r\mid N_p\). By Lemma 2.1 the nonzero integer \(N_p\) has only finitely many prime divisors. ∎

This local finiteness is the key fact which was hidden by the explicit finite-set carrier in the first strike.

---

## 3. Difference codes are always finite

Define the fixed parameterized formula

\[
D(a,b;r)
:\iff
r\ne a\land r\ne b\land E(a;r)\land\neg E(b;r).
\tag{8}
\]

### Lemma 3.1 — Finite Difference Code

For every pair of primes \(a,b\), the definable set

\[
D_{a,b}:=\{r:D(a,b;r)\}
\tag{9}
\]

is finite.

### Proof

Let \(r\ne a,b\).

If \(\kappa(r)=0\), then zero depth is automatic away from the diagonal, so

\[
E(a;r)=E(b;r)=\text{true}.
\tag{10}
\]

Hence \(D(a,b;r)\) is false.

Therefore every member of \(D_{a,b}\) has positive depth. But then

\[
D(a,b;r)\Longrightarrow E(a;r),
\tag{11}
\]

so

\[
D_{a,b}\subseteq S_a^+.
\tag{12}
\]

The latter set is finite by Lemma 2.2. ∎

Thus the prime-only structure already contains a uniformly definable family of finite sets of marker primes.

---

## 4. Exact coding of arbitrary finite good marker sets

Let \(F_\Delta\) be a finite exceptional set such that the cyclotomic-kernel adelic image contains the full factors

\[
\prod_{r\notin F_\Delta}\operatorname{SL}_2(\mathbb Z_r).
\tag{13}
\]

Call a positive-depth marker **good** if

\[
r\notin F_\Delta\cup\{2,3\}.
\tag{14}
\]

The following strengthens the first-strike packaging argument: no explicit finite-set sort is needed even to name a prescribed finite marker set exactly.

### Theorem 4.1 — Exact Finite Difference Coding

Let \(T\) be any finite set of good positive-depth primes. Then there exist primes \(a,b\notin T\), \(a\ne b\), such that

\[
\boxed{
D(a,b;r)\iff r\in T
}
\tag{15}
\]

for every rational prime \(r\).

### Proof

By finite pattern realization, choose a prime \(a\notin T\) satisfying

\[
E(a;t)
\qquad(t\in T).
\tag{16}
\]

The full positive edge support

\[
S_a^+
=
\{r:\kappa(r)>0,\ r\ne a,\ E(a;r)\}
\tag{17}
\]

is finite by Lemma 2.2 and contains \(T\).

Choose an absolute Galois element \(\gamma\) representing the Frobenius data of \(a\) in the finite quotient cut out by the residual levels

\[
r^{\kappa(r)}
\qquad(r\in S_a^+).
\tag{18}
\]

For every \(t\in T\), let \(G_t\) denote the corresponding invertible local matrix of \(\gamma\) modulo \(t^{\kappa(t)}\), and put

\[
d_t:=\det(G_t).
\tag{19}
\]

Since \(a\ne t\), \(d_t\) is a unit. Define

\[
M_t=
\begin{pmatrix}
0&-d_t\\
1&0
\end{pmatrix}.
\tag{20}
\]

Then

\[
\det(M_t)=d_t,
\qquad
\operatorname{tr}(M_t)=0,
\tag{21}
\]

so

\[
\operatorname{tr}(M_t)^2\not\equiv\det(M_t)
\pmod{t^{\kappa(t)}}.
\tag{22}
\]

Moreover

\[
h_t:=G_t^{-1}M_t
\in
\operatorname{SL}_2(\mathbb Z/t^{\kappa(t)}\mathbb Z).
\tag{23}
\]

Because every \(t\in T\) is good, the full-factor inclusion (13) supplies an element

\[
h\in G_{\mathbb Q(\mu_\infty)}
\tag{24}
\]

whose local reduction is \(h_t\) at \(t\in T\) and the identity at every other local coordinate relevant to (18). Set

\[
\sigma:=\gamma h.
\tag{25}
\]

At each \(t\in T\), the local matrix of \(\sigma\) is \(M_t\), so the edge condition fails. At every

\[
r\in S_a^+\setminus T,
\tag{26}
\]

the local matrix is unchanged from \(\gamma\), hence the edge condition remains true.

Apply Chebotarev to the conjugacy class of the image of \(\sigma\) in the finite Galois quotient used above. Trace and determinant are conjugacy invariants, so there are infinitely many rational primes \(b\) satisfying

\[
\neg E(b;t)
\qquad(t\in T)
\tag{27}
\]

and

\[
E(b;r)
\qquad(r\in S_a^+\setminus T).
\tag{28}
\]

Choose \(b\) outside the finite set \(T\cup S_a^+\cup\{a\}\).

We now verify (15).

- If \(r\in T\), then (16) and (27) give \(E(a;r)\land\neg E(b;r)\), so \(D(a,b;r)\) holds.
- If \(\kappa(r)=0\) and \(r\ne a,b\), then both incidences are true by (10), so \(D(a,b;r)\) fails.
- If \(\kappa(r)>0\) and \(r\notin S_a^+\), then \(E(a;r)\) is false, so \(D(a,b;r)\) fails.
- If \(r\in S_a^+\setminus T\), then (28) gives \(E(b;r)\), so again \(D(a,b;r)\) fails.
- The points \(r=a,b\) are excluded explicitly in (8).

Therefore \(D_{a,b}=T\) exactly. ∎

### Corollary 4.2 — Internal finite-set packaging

Every finite set of good positive-depth marker primes is represented exactly by one pair \((a,b)\) through the single fixed formula \(D(a,b;r)\).

Hence the obstruction to eliminating the explicit finite-set sort is **not** the absence of finite-domain packaging.

---

## 5. The remaining issue: source/marker alignment

The original GIR grid uses source witnesses \(p_i,q_j\) and marker witnesses \(r_{ij}\). Difference codes can package an arbitrary finite set exactly only when that set consists of positive-depth marker primes. Therefore, to reproduce the full graph reduction inside \(\mathcal I_\kappa\), one needs GIR witnesses whose row and column primes themselves lie on the positive-depth marker side.

This motivates the following meta-level strengthening of GIR.

### Definition 5.1 — Regular-Positive GIR

Write

\[
\operatorname{GIR}^+(I_\kappa)\ge n
\tag{29}
\]

if there exist pairwise distinct **good positive-depth** primes

\[
p_1,\dots,p_n,
\quad
q_1,\dots,q_n,
\quad
r_{ij}\ (1\le i,j\le n)
\tag{30}
\]

such that

\[
I_\kappa(p_k,q_\ell;r_{ij})
\iff
(k,\ell)=(i,j).
\tag{31}
\]

This is a metamathematical condition on the standard structure; no claim is made that the set of good positive primes is itself uniformly definable in the prime-only language.

---

## 6. Carrier-free graph coding under regular-positive GIR

### Theorem 6.1 — Prime-Only Undecidability from Regular-Positive GIR

If

\[
\operatorname{GIR}^+(I_\kappa)=\infty,
\tag{32}
\]

then the complete theory of the prime-only residual structure

\[
\mathcal I_\kappa=(P,I_\kappa)
\tag{33}
\]

is undecidable.

### Proof

We reproduce the finite-model reduction using difference codes in place of explicit finite-set parameters.

For a pair \(\alpha=(a,b)\), write

\[
C_\alpha(x):=D(a,b;x).
\tag{34}
\]

By Lemma 3.1 every \(C_\alpha\) is finite for every parameter pair, which will supply the reverse direction of the reduction.

Fix a graph size \(n\). By (32), choose a regular-positive GIR grid as in (30)-(31). By Theorem 4.1 there are parameter pairs

\[
\alpha_A,\alpha_C,\alpha_M,\alpha_N
\tag{35}
\]

coding exactly any prescribed finite sets of good positive primes. In particular, for a finite directed graph \(G\subseteq[n]^2\), choose them so that

\[
C_{\alpha_A}=\{p_1,\dots,p_n\},
\tag{36}
\]

\[
C_{\alpha_C}=\{q_1,\dots,q_n\},
\tag{37}
\]

\[
C_{\alpha_M}=\{r_{11},\dots,r_{nn}\},
\tag{38}
\]

and

\[
C_{\alpha_N}
=
\{r_{ij}:(i,j)\in G\}.
\tag{39}
\]

For a marker-code pair \(\alpha\), define

\[
R_\alpha(x,y)
:\iff
\exists r\,
\bigl(C_\alpha(r)\land I_\kappa(x,y;r)\bigr).
\tag{40}
\]

Then (31) implies that \(R_{\alpha_M}\) is the diagonal bijection

\[
p_i\longmapsto q_i
\tag{41}
\]

between the two finite coded domains.

Define the first-order formula \(\operatorname{Bij}(\alpha_A,\alpha_C,\alpha_M)\) by the standard two uniqueness clauses saying that \(R_{\alpha_M}\) is a bijection from \(C_{\alpha_A}\) to \(C_{\alpha_C}\).

Define the graph relation on the coded domain \(C_{\alpha_A}\) by

\[
G_{\bar\alpha}(x,z)
:\iff
\exists y\,
\bigl(
C_{\alpha_C}(y)
\land R_{\alpha_M}(z,y)
\land R_{\alpha_N}(x,y)
\bigr),
\tag{42}
\]

where

\[
\bar\alpha=(\alpha_A,\alpha_C,\alpha_M,\alpha_N).
\tag{43}
\]

For the canonical grid parameters,

\[
G_{\bar\alpha}(p_i,p_j)
\iff
(i,j)\in G.
\tag{44}
\]

Now let \(\varphi\) be any sentence in the language of one binary graph relation. Construct effectively a sentence \(\widehat\varphi\) in the language \(\{I\}\) by:

1. existentially quantifying the eight prime parameters making up the four pairs in (43);
2. requiring \(C_{\alpha_A}\ne\varnothing\) and \(\operatorname{Bij}(\alpha_A,\alpha_C,\alpha_M)\);
3. relativizing every graph-domain quantifier to \(C_{\alpha_A}\);
4. replacing every graph atom by (42).

The translation is purely syntactic and contains no oracle for \(\kappa\).

If \(\varphi\) has a finite nonempty model, choose a GIR grid of the same size and use (36)-(39); then \(\widehat\varphi\) is true.

Conversely, if \(\widehat\varphi\) is true for arbitrary witnesses, Lemma 3.1 guarantees that \(C_{\alpha_A}\) is a finite nonempty set. The formula (42) defines some binary relation on it, and the relativized sentence says exactly that this finite graph satisfies \(\varphi\).

Thus

\[
\varphi\text{ has a finite nonempty model}
\iff
\mathcal I_\kappa\models\widehat\varphi.
\tag{45}
\]

Trakhtenbrot's theorem now implies that \(\operatorname{Th}(\mathcal I_\kappa)\) is undecidable. ∎

### Conceptual conclusion

Once \(\operatorname{GIR}^+=\infty\), both full source multiplication and the explicit finite-set carrier can be removed. The single ternary residual relation already contains enough internal finite memory for Trakhtenbrot coding.

---

## 7. A natural sufficient condition: density-one positive support

Finite pattern realization comes from Chebotarev and therefore gives not merely infinitely many realizing primes but a positive-density Chebotarev set for each fixed finite pattern.

### Theorem 7.1 — Density-One Carrier Elimination

Assume the positive-depth support

\[
P_{\mathrm{pos}}(\kappa)
=
\{r:\kappa(r)>0\}
\tag{46}
\]

has relative Dirichlet density \(1\) among the rational primes. Then

\[
\operatorname{GIR}^+(I_\kappa)=\infty,
\tag{47}
\]

and consequently

\[
\boxed{
\operatorname{Th}(\mathcal I_\kappa)
\text{ is undecidable}.
}
\tag{48}
\]

### Proof

Fix \(n\) and choose \(n^2\) distinct good positive-depth marker primes \(r_{ij}\). This is possible because removing finitely many primes from a density-one set leaves an infinite set.

For every required row pattern and column pattern on this finite marker set, the finite-pattern theorem is obtained by Chebotarev from a nonempty conjugacy class in a finite Galois quotient. Hence the set of rational primes realizing that pattern has positive Dirichlet density.

The complement of \(P_{\mathrm{pos}}(\kappa)\) has Dirichlet density \(0\). Therefore the intersection of any such positive-density realization set with \(P_{\mathrm{pos}}(\kappa)\) still has the same positive density, in particular is infinite.

We may thus choose all row witnesses \(p_i\) and column witnesses \(q_j\) inside the positive-depth support, outside the fixed finite exceptional set and pairwise distinct. This gives a regular-positive GIR grid of size \(n\).

Since \(n\) was arbitrary, (47) follows. Apply Theorem 6.1. ∎

### Corollary 7.2

Cofinite positive-depth support is sufficient for prime-only undecidability.

No explicit source arithmetic and no finite-set sort are then necessary.

---

## 8. Infinite support alone does not force role alignment

The Support-Cardinality Wall says that infinitude of positive support is enough in the full structure. After the carrier is removed, this is no longer enough to force regular-positive GIR.

### Theorem 8.1 — Infinite Independent Positive Support

There exists an infinite set of good primes

\[
S\subseteq\mathbb P
\tag{49}
\]

such that, for the profile

\[
\kappa_S(r)
=
\begin{cases}
1,&r\in S,\\
0,&r\notin S,
\end{cases}
\tag{50}
\]

we have

\[
E_{\kappa_S}(p;r)=\text{false}
\qquad
\text{for all distinct }p,r\in S.
\tag{51}
\]

Consequently

\[
\operatorname{GIR}^+(I_{\kappa_S})=0.
\tag{52}
\]

### Proof

We build

\[
S=\{s_1,s_2,\dots\}
\tag{53}
\]

recursively.

Choose any good prime \(s_1\). Suppose good primes

\[
s_1,\dots,s_n
\tag{54}
\]

have been chosen so that for all \(i\ne j\le n\),

\[
s_j\nmid N_{s_i}.
\tag{55}
\]

Apply the finite-pattern realization theorem at depth one to the marker set

\[
R_n=\{s_1,\dots,s_n\}
\tag{56}
\]

with the all-NONEDGE pattern. There are infinitely many primes \(q\) such that

\[
s_i\nmid N_q
\qquad(1\le i\le n).
\tag{57}
\]

For the reverse directions, each fixed nonzero integer \(N_{s_i}\) has only finitely many prime divisors. Hence only finitely many primes \(q\) violate one of

\[
q\nmid N_{s_i}
\qquad(1\le i\le n).
\tag{58}
\]

Choose \(s_{n+1}=q\) among the infinitely many realizers of (57), avoiding:

- the previously chosen primes;
- the fixed exceptional set;
- every prime divisor of the finitely many integers \(N_{s_i}\).

Then both

\[
s_i\nmid N_{s_{n+1}}
\tag{59}
\]

and

\[
s_{n+1}\nmid N_{s_i}
\tag{60}
\]

hold for every \(i\le n\). The induction continues indefinitely.

After defining \(\kappa_S\) by (50), every member of \(S\) has threshold one. For distinct \(p,r\in S\), condition (51) is precisely

\[
r\nmid N_p,
\tag{61}
\]

which holds by construction.

Therefore for positive row/column/marker witnesses inside \(S\),

\[
I_{\kappa_S}(p,q;r)
=E(p;r)\land E(q;r)
\tag{62}
\]

is always false. No positive GIR cell can be isolated, so (52) follows. ∎

### Important limitation

Theorem 8.1 does **not** prove that \(\operatorname{Th}(\mathcal I_{\kappa_S})\) is decidable. Source primes outside \(S\) still realize arbitrary finite patterns on markers in \(S\). The theorem proves only that **infinite support by itself does not force the source/marker alignment needed by Theorem 6.1**.

---

## 9. Revised boundary after carrier elimination

The first strike suggested a “Finite-Domain Packaging Wall.” Theorem 4.1 shows that this diagnosis was too coarse: exact finite packaging is already internally available in the prime-only structure.

The genuine remaining obstruction is alignment of the two roles played by primes:

- as **source witnesses** realizing residual Boolean patterns;
- as **positive-depth marker atoms** that can be packed into finite difference codes.

This leads to the sharper picture

\[
\boxed{
\text{infinite support}
\Longrightarrow
\text{finite marker packaging}
}
\tag{63}
\]

but not

\[
\boxed{
\text{infinite support}
\Longrightarrow
\operatorname{GIR}^+=\infty.
}
\tag{64}
\]

Under density-one support, role alignment is automatic and the finite-set carrier disappears completely. Under arbitrary infinite support, Theorem 8.1 shows that role alignment can collapse maximally on the positive subset.

A more accurate name for the next boundary is therefore:

\[
\boxed{
\textbf{Source/Marker Alignment Wall}.
}
\tag{65}
\]

---

## 10. What remains open

The central unresolved problem is now precise.

> **Prime-Only Infinite-Support Problem.**  
> If \(P_{\mathrm{pos}}(\kappa)\) is merely infinite, with no density or distribution hypothesis, must the complete theory of \(\mathcal I_\kappa=(P,I_\kappa)\) be undecidable?

The present strike proves:

- **yes** under regular-positive GIR infinity;
- in particular **yes** under density-one positive support;
- exact finite-set packaging is not the missing ingredient;
- cardinality alone does not force regular-positive GIR.

What is not yet known is whether the source primes outside the positive support can themselves simulate the missing role alignment by a different first-order coding mechanism.

No claim of decidability is made for the independent-support profile of Theorem 8.1.
