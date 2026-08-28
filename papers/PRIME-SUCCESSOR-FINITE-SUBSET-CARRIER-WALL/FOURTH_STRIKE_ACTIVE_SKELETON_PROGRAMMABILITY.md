# Fourth Strike — Locally Finite Normal Form and Active-Skeleton Programmability

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-28  
**Status:** proved statements only; publication status not assigned

## 1. Aim of the strike

The previous strike showed that the hoped-for implication

\[
|P_{\mathrm{pos}}(\kappa)|=\infty
\Longrightarrow
\operatorname{Th}(\mathbb P,I_\kappa)
\text{ undecidable}
\tag{1}
\]

fails in the prime-only reduct. It also isolated a sufficient mechanism, regular-positive GIR, and exhibited a sparse support on which that mechanism collapses.

The natural next hope is that a recurrence or Chebotarev-hitting statistic of the support might still classify the prime-only structures.

This strike shows that the situation is substantially richer.

The prime-only reduct admits an exact locally finite incidence normal form, and its active positive-depth skeleton is **programmable**: every countable directed acyclic graph with a backward topological enumeration can be realized exactly as the positive-support induced residual graph of a binary profile of Dirichlet density zero.

Consequently:

1. zero density occurs on both decidable and undecidable sides;
2. regular-positive GIR infinity is sufficient but not necessary for undecidability;
3. there are continuum many pairwise distinct complete prime-only theories even among \(\{0,1\}\)-valued profiles whose positive support has Dirichlet density zero;
4. no scalar statistic such as cardinality, density, growth, or grid-hitting rank can classify the full prime-only theory across arbitrary supports.

Every theorem below is proved in this checkpoint.

---

## 2. Prime-only residual structure

For a threshold profile

\[
\kappa:\mathbb P\to\mathbb N_0,
\tag{2}
\]

write

\[
S_\kappa
=
P_{\mathrm{pos}}(\kappa)
=
\{r\in\mathbb P:\kappa(r)>0\}.
\tag{3}
\]

For a source prime \(p\), let

\[
N_p:=\tau(p)^2-p^{11}.
\tag{4}
\]

The prime-only structure is

\[
\mathcal I_\kappa=(\mathbb P,I_\kappa),
\tag{5}
\]

where

\[
I_\kappa(p,q;r)
=
E_\kappa(p;r)\land E_\kappa(q;r).
\tag{6}
\]

The binary relation \(E_\kappa\) is already definable in the ternary language by

\[
E(x;r):=I_\kappa(x,x;r).
\tag{7}
\]

For \(x\ne r\),

\[
E(x;r)
\iff
\begin{cases}
\text{true},&\kappa(r)=0,\\
r^{\kappa(r)}\mid N_x,&\kappa(r)>0.
\end{cases}
\tag{8}
\]

By definition,

\[
E(r;r)=\text{false}.
\tag{9}
\]

---

## 3. Nonvanishing and finite active neighborhoods

### Lemma 3.1 — Nonvanishing

For every rational prime \(p\),

\[
N_p\ne0.
\tag{10}
\]

### Proof

If \(N_p=0\), then

\[
\tau(p)^2=p^{11}.
\tag{11}
\]

Taking \(p\)-adic valuations gives

\[
2v_p(\tau(p))=11,
\tag{12}
\]

which is impossible because the left-hand side is even and the right-hand side is odd. ∎

### Lemma 3.2 — Local finiteness over positive markers

For every prime \(p\), the set

\[
\mathcal N_\kappa(p)
:=
\{r\in S_\kappa:r\ne p\land E(p;r)\}
\tag{13}
\]

is finite.

### Proof

If \(r\in\mathcal N_\kappa(p)\), then \(\kappa(r)>0\) and

\[
r^{\kappa(r)}\mid N_p.
\tag{14}
\]

In particular \(r\mid N_p\). By Lemma 3.1, \(N_p\) is a nonzero integer and has only finitely many prime divisors. ∎

Thus every source row has finite support when restricted to the positive-depth marker set.

---

## 4. The positive-depth support is definable inside the prime-only reduct

The previous work treated \(S_\kappa\) externally. In fact the prime-only relation itself detects it.

Define

\[
\operatorname{Pos}(r)
:\iff
\exists p\,(p\ne r\land\neg E(p;r)).
\tag{15}
\]

### Theorem 4.1 — Internal support definability

For every threshold profile \(\kappa\),

\[
\boxed{
\mathcal I_\kappa\models\operatorname{Pos}(r)
\iff
r\in S_\kappa.
}
\tag{16}
\]

### Proof

Suppose first that \(\kappa(r)=0\). By (8),

\[
E(p;r)=\text{true}
\tag{17}
\]

for every \(p\ne r\). Hence \(\operatorname{Pos}(r)\) is false.

Now suppose

\[
k:=\kappa(r)\ge1.
\tag{18}
\]

We must find \(p\ne r\) with

\[
r^k\nmid N_p.
\tag{19}
\]

If \(r\ne3\), consider the finite Galois extension cut out by the representation attached to \(\Delta\) modulo \(r^k\). The identity element belongs to its finite Galois image. By Chebotarev there are infinitely many unramified primes \(p\ne r\) whose Frobenius image is the identity modulo \(r^k\). For such \(p\),

\[
\tau(p)\equiv2\pmod{r^k},
\qquad
p^{11}\equiv1\pmod{r^k},
\tag{20}
\]

and therefore

\[
N_p
\equiv
4-1
\equiv3
\pmod{r^k}.
\tag{21}
\]

Since \(r\ne3\), (21) implies (19).

For \(r=3\), take \(p=2\). Since

\[
N_2
=(-24)^2-2^{11}
=576-2048
=-1472,
\tag{22}
\]

we have

\[
3\nmid N_2,
\tag{23}
\]

so (19) holds for every \(k\ge1\).

Thus every positive-depth marker has a nonedge from some distinct source prime, and (16) follows. ∎

### Remark 4.2

No large-image theorem is needed for support definability. For \(r\ne3\), only the identity element in the finite residual image and Chebotarev are used.

---

## 5. Locally Finite Incidence Normal Form

Define the binary relation

\[
R_\kappa(p,r)
:\iff
\operatorname{Pos}(r)\land E(p;r).
\tag{24}
\]

By Lemma 3.2, every left fiber

\[
R_\kappa(p,-)
\tag{25}
\]

is finite.

### Theorem 5.1 — Prime-only normal form

The structure

\[
\mathcal I_\kappa=(\mathbb P,I_\kappa)
\tag{26}
\]

is parameter-free interdefinable with the one-sorted locally finite incidence structure

\[
\mathcal L_\kappa
=
(\mathbb P,S_\kappa,R_\kappa),
\tag{27}
\]

where \(S_\kappa\) is a unary predicate and \(R_\kappa\subseteq\mathbb P\times S_\kappa\) has finite left fibers.

### Proof

Starting from \(I_\kappa\), define \(E\) by (7), define \(S_\kappa\) by Theorem 4.1, and then define \(R_\kappa\) by (24).

Conversely, from \((S_\kappa,R_\kappa)\) recover \(E\) by

\[
E(p;r)
\iff
p\ne r
\land
\bigl(
\neg S_\kappa(r)
\lor
R_\kappa(p,r)
\bigr).
\tag{28}
\]

Indeed, zero-depth columns are co-singletons by (8)-(9), whereas positive-depth columns are exactly recorded by \(R_\kappa\). Finally recover

\[
I_\kappa(p,q;r)
\iff
E(p;r)\land E(q;r).
\tag{29}
\]

All translations are parameter-free. ∎

### Consequence 5.2

After the carrier has been removed, all nontrivial information in the prime-only reduct is concentrated in a locally finite incidence system over the definable active marker set \(S_\kappa\).

This is the correct structural normal form for the rest of the branch.

---

## 6. The active skeleton

Define the induced directed graph on the active set

\[
\mathcal G_\kappa
=
(S_\kappa,\to_\kappa),
\tag{30}
\]

where for distinct \(p,r\in S_\kappa\),

\[
p\to_\kappa r
\iff
R_\kappa(p,r)
\iff
E(p;r).
\tag{31}
\]

This graph is parameter-free interpretable in \(\mathcal I_\kappa\) by Theorem 4.1.

By Lemma 3.2 every vertex has finite out-degree.

The next theorem says that, despite this local finiteness, the active skeleton can be programmed almost arbitrarily.

---

## 7. Backward DAGs

Call a countable loopless directed graph

\[
G=(V,\to_G)
\tag{32}
\]

a **backward DAG** if there is an enumeration

\[
V=\{v_0,v_1,v_2,\dots\}
\tag{33}
\]

such that

\[
v_i\to_G v_j
\Longrightarrow
j<i.
\tag{34}
\]

Condition (34) implies acyclicity. At stage \(i\), the desired outgoing neighborhood of \(v_i\) is a subset of the finite set \(\{v_0,\dots,v_{i-1}\}\).

---

## 8. Active-Skeleton Programmability

We use the finite-pattern theorem from the Support-Cardinality proof at depth one: for every finite set of sufficiently good marker primes and every Boolean edge/nonedge pattern on them, infinitely many source primes realize exactly that pattern on the chosen finite marker set.

Let \(F_\Delta\) denote a fixed finite exceptional marker set large enough for that theorem, and exclude also \(2,3\) from the programmed support.

### Theorem 8.1 — Active-Skeleton Programmability

Let \(G\) be any countable backward DAG. Let

\[
B_0<B_1<B_2<\cdots
\tag{35}
\]

be any prescribed sequence of integers.

Then there exists an infinite set of good primes

\[
S=\{s_0,s_1,s_2,\dots\}
\tag{36}
\]

such that

\[
s_i>B_i
\tag{37}
\]

for every \(i\), and for the binary profile

\[
\kappa_S(r)
=
\begin{cases}
1,&r\in S,\\
0,&r\notin S,
\end{cases}
\tag{38}
\]

the active skeleton satisfies

\[
\boxed{
\mathcal G_{\kappa_S}\cong G
}
\tag{39}
\]

under \(s_i\leftrightarrow v_i\).

### Proof

We construct \(s_i\) recursively.

Choose any good prime

\[
s_0>B_0.
\tag{40}
\]

Suppose

\[
s_0,\dots,s_{n-1}
\tag{41}
\]

have been chosen so that all active-active incidences among them agree with \(G\).

Let

\[
T_n
=
\{s_j:j<n\text{ and }v_n\to_G v_j\}.
\tag{42}
\]

Apply finite pattern realization to the marker set

\[
R_n=\{s_0,\dots,s_{n-1}\}
\tag{43}
\]

with EDGE exactly on \(T_n\) and NONEDGE on \(R_n\setminus T_n\). There are infinitely many primes \(p\) satisfying

\[
E(p;s_j)
\iff
s_j\in T_n
\qquad(j<n).
\tag{44}
\]

To ensure the reverse incidences have the required value, observe that for each \(i<n\), Lemma 3.1 gives

\[
N_{s_i}\ne0,
\tag{45}
\]

so the set of prime divisors of \(N_{s_i}\) is finite. Hence

\[
F_n
:=
F_\Delta\cup\{2,3,s_0,\dots,s_{n-1}\}
\cup
\bigcup_{i<n}\operatorname{PrimeDiv}(N_{s_i})
\tag{46}
\]

is finite.

Choose a realization \(p\) of (44) such that

\[
p\notin F_n
\qquad\text{and}\qquad
p>B_n.
\tag{47}
\]

This is possible because the realization set in (44) is infinite and therefore unbounded.

Set

\[
s_n=p.
\tag{48}
\]

Equation (44) gives

\[
s_n\to_{\kappa_S}s_j
\iff
v_n\to_G v_j
\qquad(j<n).
\tag{49}
\]

For the reverse direction, (46)-(47) imply

\[
s_n\nmid N_{s_i}
\qquad(i<n),
\tag{50}
\]

and because \(\kappa_S(s_n)=1\),

\[
\neg E(s_i;s_n)
\qquad(i<n).
\tag{51}
\]

By the backward condition (34), precisely these reverse edges are required to be absent in \(G\).

Thus all incidences on the first \(n+1\) programmed vertices agree with \(G\). The induction continues.

No later stage can alter an already determined edge: an old source-to-new-marker edge is forced absent by the divisor avoidance at the moment the new marker is chosen, and all old-marker incidences of the new source were fixed by (44).

Therefore the final active skeleton is exactly \(G\). ∎

---

## 9. Zero-density programmability

### Corollary 9.1 — Arbitrarily sparse programming

Every countable backward DAG occurs as the active skeleton of a binary threshold profile whose positive support has natural density zero and Dirichlet density zero.

### Proof

In Theorem 8.1 choose, for example,

\[
B_i=2^{i^2}.
\tag{52}
\]

Then

\[
s_i>2^{i^2}.
\tag{53}
\]

Hence the counting function of \(S\) grows sublinearly, so \(S\) has natural density zero.

Moreover

\[
\sum_{s\in S}\frac1s
\le
\sum_{i\ge1}2^{-i^2}
<\infty.
\tag{54}
\]

For \(\sigma>1\),

\[
\sum_{s\in S}s^{-\sigma}
\le
\sum_{s\in S}s^{-1}
<\infty,
\tag{55}
\]

while

\[
\log\frac1{\sigma-1}\to\infty
\qquad(\sigma\downarrow1).
\tag{56}
\]

Therefore the Dirichlet density of \(S\), when computed by the usual prime-density quotient, is zero. ∎

Thus density cannot be the sought exact invariant.

---

## 10. Every countable graph can be interpreted in a programmed active skeleton

Let

\[
H=(V,E_H)
\tag{57}
\]

be any countable simple undirected graph.

Construct its directed incidence DAG \(J(H)\) as follows.

Its universe is the disjoint union

\[
V\sqcup E_H.
\tag{58}
\]

For every graph edge

\[
e=\{u,v\}\in E_H,
\tag{59}
\]

put exactly the two directed edges

\[
e\to u,
\qquad
e\to v.
\tag{60}
\]

There are no other directed edges.

### Lemma 10.1 — Incidence DAG lemma

The graph \(J(H)\) is a countable backward DAG, every vertex has out-degree at most two, and \(H\) is parameter-free first-order interpretable in \(J(H)\).

### Proof

Enumerate the vertices of \(H\) as \(u_0,u_1,\dots\). At stage \(n\), list \(u_n\), then list the finitely many edge-nodes \(\{u_i,u_n\}\) with \(i<n\). Every edge-node is therefore listed after both of its endpoints, so all arrows in (60) point backward. Out-degree is zero on original vertex-nodes and two on edge-nodes.

Inside \(J(H)\), define

\[
\operatorname{Vert}(x)
:\iff
\forall y\,\neg(x\to y).
\tag{61}
\]

These are exactly the original vertices of \(H\). For distinct such vertices define

\[
\operatorname{Adj}(x,y)
:\iff
\exists e\,(e\to x\land e\to y).
\tag{62}
\]

By construction, (62) holds exactly when \(\{x,y\}\in E_H\). Thus \(H\) is interpreted on the definable sink set. ∎

### Theorem 10.2 — Graph universality across zero-density supports

For every countable graph \(H\), there exists a binary threshold profile \(\kappa_H\) with

\[
\delta_{\mathrm{Dir}}(S_{\kappa_H})=0
\tag{63}
\]

such that \(H\) is parameter-free first-order interpretable in the prime-only residual structure

\[
\mathcal I_{\kappa_H}.
\tag{64}
\]

### Proof

Apply Corollary 9.1 to the backward DAG \(J(H)\). The resulting active skeleton is definable in \(\mathcal I_{\kappa_H}\) by Theorem 4.1 and is isomorphic to \(J(H)\). Lemma 10.1 then interprets \(H\). ∎

This is a universality theorem for the **family** of prime-only reducts as the support varies. It does not claim that one fixed profile interprets every countable graph.

---

## 11. Undecidability with bounded regular-positive GIR

The previous strike proved

\[
\operatorname{GIR}^+(I_\kappa)=\infty
\Longrightarrow
\operatorname{Th}(\mathcal I_\kappa)
\text{ undecidable}.
\tag{65}
\]

We now prove that the converse fails dramatically.

Choose any nonrecursive set

\[
A\subseteq\mathbb N.
\tag{66}
\]

Define a countable graph \(H_A\) to be the disjoint union of:

1. countably infinitely many isolated vertices;
2. one clique \(K_{n+3}\) for every \(n\in A\).

For each \(m\ge3\), let \(\chi_m\) be the graph sentence asserting that there is a connected component which is exactly a clique of size \(m\). Explicitly, \(\chi_m\) existentially names \(m\) distinct pairwise adjacent vertices and requires that no vertex outside the named tuple is adjacent to any of them.

Then

\[
H_A\models\chi_{n+3}
\iff
n\in A.
\tag{67}
\]

Hence

\[
A\le_m\operatorname{Th}(H_A),
\tag{68}
\]

so \(\operatorname{Th}(H_A)\) is undecidable.

Apply Theorem 10.2 to \(H_A\), using the incidence DAG \(J(H_A)\).

### Theorem 11.1 — Undecidable zero-density profile with bounded active grid rank

There exists a binary profile \(\kappa\) such that

\[
\delta_{\mathrm{Dir}}(S_\kappa)=0,
\tag{69}
\]

\[
\operatorname{Th}(\mathcal I_\kappa)
\text{ is undecidable},
\tag{70}
\]

but

\[
\boxed{
\operatorname{GIR}^+(I_\kappa)\le2.
}
\tag{71}
\]

### Proof

Program the active skeleton to be \(J(H_A)\). By Theorem 10.2, \(H_A\) is interpretable in \(\mathcal I_\kappa\), so (68) implies (70). Sparsity gives (69).

Every active vertex of \(J(H_A)\) has out-degree at most two. In an active GIR grid of size \(n\), each row witness \(p_i\) must satisfy

\[
E(p_i;r_{i1}),\dots,E(p_i;r_{in}),
\tag{72}
\]

on \(n\) distinct active markers. Thus its active out-degree is at least \(n\). Therefore \(n\le2\), proving (71). ∎

### Consequence 11.2

Regular-positive infinite GIR is a sufficient **grid-coding mechanism**, not an exact invariant for prime-only undecidability.

The hoped-for classification by a Chebotarev grid-hitting rank therefore fails at the level of the full complete theory.

---

## 12. Continuum many theories at zero support density

For every subset

\[
A\subseteq\mathbb N,
\tag{73}
\]

form \(H_A\) as above and program its incidence DAG into a zero-density support \(S_A\).

If

\[
A\ne B,
\tag{74}
\]

choose \(n\in A\triangle B\). The translated interpretation of \(\chi_{n+3}\) holds in exactly one of

\[
\mathcal I_{\kappa_A},
\qquad
\mathcal I_{\kappa_B}.
\tag{75}
\]

Hence their complete theories differ.

### Corollary 12.1 — Continuum spectrum at Dirichlet density zero

There are

\[
\boxed{2^{\aleph_0}}
\tag{76}
\]

pairwise distinct complete first-order theories among prime-only residual structures with all of the following fixed macroscopic properties:

\[
\kappa(r)\in\{0,1\},
\tag{77}
\]

\[
|S_\kappa|=\infty,
\tag{78}
\]

and

\[
\delta_{\mathrm{Dir}}(S_\kappa)=0.
\tag{79}
\]

### Proof

The construction gives at least \(2^{\aleph_0}\) pairwise distinct theories. The language is countable, so there are at most \(2^{\aleph_0}\) complete theories. ∎

---

## 13. Comparison with the decidable sparse support

The third strike constructed a sparse binary support \(S_{\mathrm{dec}}\) with a canonical saturated finite-neighborhood geometry and a decidable prime-only theory.

The present strike constructs sparse binary supports \(S_{\mathrm{und}}\) with

\[
\delta_{\mathrm{Dir}}(S_{\mathrm{dec}})
=
\delta_{\mathrm{Dir}}(S_{\mathrm{und}})
=0,
\tag{80}
\]

but

\[
\operatorname{Th}(\mathcal I_{\kappa_{\mathrm{dec}}})
\text{ decidable},
\tag{81}
\]

while

\[
\operatorname{Th}(\mathcal I_{\kappa_{\mathrm{und}}})
\text{ undecidable}.
\tag{82}
\]

Moreover (82) can hold with bounded regular-positive GIR by Theorem 11.1.

Therefore none of the following is an exact classifier of the prime-only complete theory:

- support cardinality;
- natural density;
- Dirichlet density;
- threshold alphabet \(\{0,1\}\);
- regular-positive GIR infinity.

---

## 14. Revised conceptual boundary

The Support-Cardinality Wall remains exact in the **full** structure because source multiplication or an explicit finite-set carrier packages arbitrary source witnesses.

After all carrier memory is removed, the situation changes categorically.

The prime-only reduct is governed by the locally finite active incidence system

\[
p\longmapsto\mathcal N_\kappa(p)\subseteq S_\kappa.
\tag{83}
\]

The active part

\[
p\in S_\kappa
\longmapsto
\mathcal N_\kappa(p)\cap S_\kappa
\tag{84}
\]

can itself encode arbitrary backward DAGs.

Thus the next boundary is not a scalar “wall” comparable to support cardinality. It is a **skeleton-classification problem**.

A suitable name is

\[
\boxed{
\textbf{Active-Skeleton Complexity Frontier}.
}
\tag{85}
\]

The exact classification problem becomes:

> Which locally finite active skeletons, together with the multiplicity spectrum of external finite neighborhoods, yield decidable prime-only theories?

The previous sparse decidable model is one tame point of this space. The present programmability theorem shows that the space also contains arbitrary countable graph complexity.

---

## 15. Claim boundary

This checkpoint proves programmability **across profiles**. It does not claim:

- that one fixed prime-only profile interprets every countable graph;
- that every zero-density profile is programmable or undecidable;
- that every undecidable profile has bounded or infinite GIR;
- that the active skeleton alone determines the full prime-only theory;
- an exact decidability criterion for arbitrary locally finite skeletons;
- computability of the programmed support from an arbitrary noncomputable target graph.

The theorem does show that any proposed exact criterion based only on support size, density, growth, or regular-positive grid rank is insufficient.

---

## 16. Hostile audit checklist

The following failure modes were checked in the proof above.

1. **Could \(N_p=0\) make divisor avoidance infinite?** No; Lemma 3.1 rules this out by parity of \(p\)-adic valuation.
2. **Could the positive support fail to be definable in the prime-only language?** No; Theorem 4.1 gives the explicit parameter-free formula (15).
3. **Does support definability secretly use adelic open image?** No; identity Frobenius plus Chebotarev suffices, with the explicit \(r=3\) check.
4. **Can a new programmed marker create an unwanted old-to-new edge?** The new prime is chosen outside the finite union of prime divisors of all previous \(N_{s_i}\).
5. **Can finite-pattern realization conflict with divisor avoidance?** No; each finite pattern has infinitely many realizing primes, while the forbidden set at each stage is finite.
6. **Can sparsity be imposed simultaneously?** Yes; every infinite set of realizing primes is unbounded, so any prescribed lower bound \(B_n\) can be met.
7. **Does the graph interpretation require parameters?** No; the active support is parameter-free definable, and the sink/adjacency interpretation in the incidence DAG is parameter-free.
8. **Could future stages alter already programmed incidences?** No; existing marker coordinates of a newly chosen source are fixed at its stage, and reverse edges are killed when future markers are selected.
9. **Does undecidability in Theorem 11.1 come from an unproved arithmetic interpretation?** No; it comes from the explicit many-one reduction (67)-(68) from a nonrecursive set through finite clique-component sentences.
10. **Is infinite regular-positive GIR being smuggled back in?** No; the programmed incidence DAG has active out-degree at most two, giving the explicit bound (71).

**Audit verdict:** no internal contradiction found. A separate literature audit is still required before publication status is considered.
