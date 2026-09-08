# Fifth Strike — Saturated Prime-Only Profiles and Exact WMSO Classification

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-29  
**Status:** proved statements only; publication status not assigned

## 1. Why this strike is the correct stopping target

The preceding strikes established four facts.

1. Full source multiplication is unnecessary for the amplifying side if a finite-subset carrier is supplied.
2. In the prime-only reduct, the positive support is parameter-free definable and every source row has finite active neighborhood.
3. Prime-only infinite support can be decidable or undecidable even at the same threshold alphabet \(\{0,1\}\) and the same Dirichlet density zero.
4. The active skeleton can program arbitrary countable backward DAGs.

Therefore an exact scalar wall no longer exists after all carrier memory is removed. The remaining reasonable classification target is structural: isolate a canonical subfamily in which the only variable datum is the active skeleton and prove an exact logical correspondence.

This file does that.

The result is a saturated realization theorem together with

\[
\boxed{
\operatorname{Th}(\mathcal I_{\kappa_G})\text{ is decidable}
\iff
\operatorname{WMSO}(G)\text{ is decidable}.
}
\tag{1}
\]

Thus the prime-only branch reaches an exact classification on a natural canonical subfamily. Beyond this point, arbitrary multiplicity spectra constitute a strictly broader new problem rather than an unfinished part of the present branch.

---

## 2. Prime-only normal form recalled

For a binary threshold profile

\[
\kappa_S(r)=
\begin{cases}
1,&r\in S,\\
0,&r\notin S,
\end{cases}
\tag{2}
\]

let

\[
N_p=\tau(p)^2-p^{11}.
\tag{3}
\]

The prime-only residual structure is

\[
\mathcal I_{\kappa_S}=(\mathbb P,I_{\kappa_S}).
\tag{4}
\]

Define

\[
E(x;r):=I_{\kappa_S}(x,x;r).
\tag{5}
\]

The active support \(S\) is parameter-free definable by

\[
\operatorname{Pos}(r)
:\iff
\exists p\,(p\ne r\land\neg E(p;r)).
\tag{6}
\]

and the active incidence relation is

\[
R(p,r)
:\iff
\operatorname{Pos}(r)\land E(p;r).
\tag{7}
\]

Every left fiber

\[
N_S(p):=\{r\in S:R(p,r)\}
\tag{8}
\]

is finite, because

\[
r\in N_S(p)\Longrightarrow r\mid N_p
\tag{9}
\]

and \(N_p\ne0\).

The full relation \(E\) is recovered from \((S,R)\) by

\[
E(p;r)
\iff
p\ne r\land\bigl(r\notin S\lor R(p,r)\bigr).
\tag{10}
\]

Hence the prime-only structure is parameter-free interdefinable with its locally finite normal form.

---

## 3. Canonical saturated extension of an active skeleton

Let

\[
G=(V,\to_G)
\tag{11}
\]

be a countably infinite backward DAG, with an enumeration

\[
V=\{v_0,v_1,\dots\}
\tag{12}
\]

satisfying

\[
v_i\to_G v_j\Longrightarrow j<i.
\tag{13}
\]

Define an abstract one-sorted normal-form structure

\[
\mathcal K(G)
\tag{14}
\]

as follows.

Its domain is the disjoint union

\[
V
\sqcup
\bigl(\operatorname{Fin}(V)\times\mathbb N\bigr).
\tag{15}
\]

The unary active predicate \(S\) holds exactly on \(V\). The relation \(R(x,v)\), whose second argument is active, is defined by

\[
R(u,v)
\iff
u\to_G v
\qquad(u,v\in V),
\tag{16}
\]

and

\[
R((F,n),v)
\iff
v\in F.
\tag{17}
\]

Thus every finite subset \(F\subseteq V\) occurs as the active neighborhood of countably infinitely many external elements.

Recover the residual relation by

\[
E(x;y)
\iff
x\ne y\land\bigl(y\notin S\lor R(x,y)\bigr),
\tag{18}
\]

and

\[
I(x,z;y)
\iff
E(x;y)\land E(z;y).
\tag{19}
\]

We call \(\mathcal K(G)\) the **saturated prime-only normal form** over \(G\).

---

## 4. Simultaneous programming and saturation

The active-skeleton programmability proof can be dovetailed with the exact-neighborhood construction from the decidable sparse-support strike.

### Theorem 4.1 — Saturated Active-Skeleton Realization

Let \(G\) be any countable backward DAG. Let

\[
B_0<B_1<\cdots
\tag{20}
\]

be any prescribed sequence of lower bounds.

Then there is a binary threshold profile \(\kappa_G\) with positive support

\[
S_G=\{s_0,s_1,\dots\}
\tag{21}
\]

such that:

1. \(s_i>B_i\) for every \(i\);
2. the active skeleton on \(S_G\) is isomorphic to \(G\) under \(s_i\leftrightarrow v_i\);
3. for every finite subset \(F\subseteq S_G\), there are countably infinitely many primes
   \[
   c\notin S_G
   \tag{22}
   \]
   with exact active neighborhood
   \[
   N_{S_G}(c)=F.
   \tag{23}
   \]

Consequently the locally finite normal form of \(\mathcal I_{\kappa_G}\) is isomorphic to \(\mathcal K(G)\).

### Proof

We perform one recursion satisfying two countable families of requirements.

#### A. Skeleton requirements

At stage \(n\), once

\[
s_0,\dots,s_{n-1}
\tag{24}
\]

have been chosen, the outgoing pattern required for \(s_n\) is

\[
T_n
=
\{s_j:j<n\text{ and }v_n\to_G v_j\}.
\tag{25}
\]

Finite residual pattern realization supplies infinitely many primes \(p\) with

\[
E(p;s_j)
\iff
s_j\in T_n
\qquad(j<n).
\tag{26}
\]

As in the active-skeleton theorem, reverse unwanted edges are prevented by choosing \(p\) outside the finitely many prime divisors of

\[
N_{s_0},\dots,N_{s_{n-1}}.
\tag{27}
\]

#### B. Saturation requirements

Enumerate all pairs

\[
(J,m),
\qquad
J\subseteq\mathbb N\text{ finite},
\quad
m\in\mathbb N.
\tag{28}
\]

A requirement \((J,m)\) becomes eligible after every \(s_j\) with \(j\in J\) has been chosen. Its task is to create a fresh external prime \(c_{J,m}\) whose final active neighborhood is exactly

\[
F_J=\{s_j:j\in J\}.
\tag{29}
\]

When the requirement is served at a finite stage with current support prefix

\[
S^{(t)}=\{s_0,\dots,s_t\},
\tag{30}
\]

finite pattern realization gives infinitely many primes \(c\) satisfying

\[
E(c;s)=
\begin{cases}
\text{true},&s\in F_J,\\
\text{false},&s\in S^{(t)}\setminus F_J.
\end{cases}
\tag{31}
\]

Choose a fresh such \(c\) outside the currently forbidden finite set and declare it permanently external.

To ensure that no future support prime creates an additional edge from \(c\), add to the permanent support-forbidden set every prime divisor of

\[
N_c
\tag{32}
\]

which is not already a member of \(F_J\), and add \(c\) itself.

Because \(N_c\ne0\), only finitely many primes are added by each served requirement.

#### C. Compatibility of the two tasks

At every finite stage only finitely many skeleton vertices and finitely many saturation witnesses have been created. Hence the union of all currently forbidden primes is finite.

When choosing a new skeleton vertex \(s_n\), intersect the infinite realization set from (26) with the complement of:

- the fixed finite residual exceptional set;
- all previously chosen support primes;
- all previously declared external witnesses;
- all support-forbidden prime divisors introduced by (32);
- all prime divisors in (27);
- all primes at most \(B_n\).

This removes only finitely many primes from an infinite realization set, so a choice remains.

When choosing a saturation witness, the same finite-avoidance argument applies.

Dovetail the recursion so that every eligible pair \((J,m)\) is eventually served. For fixed finite \(J\), the infinitely many values of \(m\) yield infinitely many distinct witnesses with neighborhood exactly \(F_J\).

The skeleton incidences are preserved by the same argument as in the previous strike, and the permanent divisor prohibition guarantees that every external witness keeps the exact neighborhood assigned in (31).

Thus all three conclusions hold. ∎

### Corollary 4.2 — Zero-density saturated realization

Every countable backward DAG has a saturated prime-only realization with natural and Dirichlet density zero.

### Proof

Choose, for example,

\[
B_n=2^{n^2}.
\tag{33}
\]

Then

\[
\sum_n\frac1{s_n}<\infty,
\tag{34}
\]

which implies Dirichlet density zero, and the counting function is sublinear, giving natural density zero. ∎

---

## 5. Weak monadic second-order structure of the skeleton

Let

\[
\mathcal W(G)
=
\bigl(
V,
\operatorname{Fin}(V),
\in,
\to_G
\bigr).
\tag{35}
\]

This is the standard two-sorted first-order presentation of weak monadic second-order logic over \(G\): first-sort variables range over vertices and second-sort variables range over finite subsets of vertices.

Thus

\[
\operatorname{Th}(\mathcal W(G))
\tag{36}
\]

is exactly the weak monadic second-order theory \(\operatorname{WMSO}(G)\).

---

## 6. The saturated prime-only structure interprets WMSO

Inside \(\mathcal K(G)\), let

\[
\operatorname{Ext}(x):=\neg S(x).
\tag{37}
\]

For external elements define the equivalence relation

\[
x\sim y
\iff
\operatorname{Ext}(x)
\land
\operatorname{Ext}(y)
\land
\forall v\,
\bigl(
S(v)\to(R(x,v)\leftrightarrow R(y,v))
\bigr).
\tag{38}
\]

### Lemma 6.1 — Finite-set quotient

The quotient of the external domain by \(\sim\) is canonically isomorphic to \(\operatorname{Fin}(V)\).

### Proof

By construction, two external elements are equivalent exactly when they have the same finite active neighborhood. Every external neighborhood is finite by (17), and saturation gives at least one external representative for every finite subset \(F\subseteq V\). Thus

\[
[x]_\sim
\longmapsto
\{v\in V:R(x,v)\}
\tag{39}
\]

is a well-defined bijection from the quotient to \(\operatorname{Fin}(V)\). ∎

Membership is definable on representatives by

\[
v\in[x]_\sim
\iff
R(x,v).
\tag{40}
\]

The graph relation on the active sort is simply

\[
u\to_G v
\iff
S(u)\land S(v)\land R(u,v).
\tag{41}
\]

### Theorem 6.2 — WMSO lower interpretation

The two-sorted weak monadic structure \(\mathcal W(G)\) is parameter-free interpretable, using the definable quotient (38), in \(\mathcal K(G)\).

Consequently

\[
\operatorname{WMSO}(G)
\le_m
\operatorname{Th}(\mathcal K(G))
\tag{42}
\]

under effective sentence translation.

### Proof

Use the active domain \(S\) for the vertex sort, the quotient of external elements by \(\sim\) for the finite-set sort, (40) for membership, and (41) for the graph relation. Standard first-order interpretation with a definable equivalence relation gives an effective translation of sentences. ∎

In particular, decidability of \(\operatorname{Th}(\mathcal K(G))\) implies decidability of \(\operatorname{WMSO}(G)\).

---

## 7. WMSO gives an upper interpretation of the saturated structure

Let \(C\) be a countably infinite pure set with equality only. Consider the disjoint multi-sorted structure

\[
\mathcal W(G)\sqcup C.
\tag{43}
\]

### Lemma 7.1 — Pure-copy sort does not change decidability

The complete first-order theory of \(\mathcal W(G)\sqcup C\) is decidable if and only if \(\operatorname{WMSO}(G)\) is decidable.

### Proof

One direction is immediate because \(\mathcal W(G)\) is a definable union of sorts.

Conversely, the theory of an infinite pure equality sort admits effective quantifier elimination: a formula is determined by equality and inequality patterns among finitely many variables. Since the languages of \(\mathcal W(G)\) and \(C\) are disjoint and there are no cross-sort relations, every mixed sentence effectively separates into finitely many Boolean combinations of sentences from the two component theories. Thus a decision procedure for \(\operatorname{WMSO}(G)\), together with the trivial decision procedure for the infinite equality sort, decides the union. ∎

### Lemma 7.2 — Upper interpretation

The saturated normal form \(\mathcal K(G)\) is first-order interpretable in

\[
\mathcal W(G)\sqcup C.
\tag{44}
\]

### Proof

Represent an active element \(v\in V\) by a tagged vertex-sort object.

Represent an external element of \(\mathcal K(G)\) by a pair

\[
(F,c)
\in
\operatorname{Fin}(V)\times C.
\tag{45}
\]

Use a finite tag to form the disjoint interpreted domain.

Equality of external elements is

\[
(F,c)=(F',c')
\iff
F=F'\land c=c'.
\tag{46}
\]

The active predicate holds only on the vertex-tagged part. The incidence relation is interpreted by

\[
R(u,v)
\iff
u\to_G v
\tag{47}
\]

on two active elements, and by

\[
R((F,c),v)
\iff
v\in F
\tag{48}
\]

for an external source and active marker. No other \(R\)-instances hold.

These formulas reproduce exactly (15)-(17), so they interpret \(\mathcal K(G)\). ∎

### Theorem 7.3 — WMSO upper reduction

If \(\operatorname{WMSO}(G)\) is decidable, then

\[
\operatorname{Th}(\mathcal K(G))
\tag{49}
\]

is decidable.

### Proof

By Lemma 7.1, the ambient structure (43) has decidable theory. By Lemma 7.2, every sentence of \(\mathcal K(G)\) effectively translates to a sentence of that decidable ambient theory. ∎

---

## 8. Exact WMSO classification

### Theorem 8.1 — Saturated Prime-Only WMSO Classification

For every countable backward DAG \(G\), let \(\kappa_G\) be any saturated realization supplied by Theorem 4.1. Then

\[
\boxed{
\operatorname{Th}(\mathcal I_{\kappa_G})
\text{ is decidable}
\iff
\operatorname{WMSO}(G)
\text{ is decidable}.
}
\tag{50}
\]

### Proof

The prime-only structure \(\mathcal I_{\kappa_G}\) is parameter-free interdefinable with its locally finite normal form, which by Theorem 4.1 is isomorphic to \(\mathcal K(G)\). Therefore their complete theories are effectively intertranslatable.

If \(\operatorname{Th}(\mathcal I_{\kappa_G})\) is decidable, then so is \(\operatorname{Th}(\mathcal K(G))\), and Theorem 6.2 implies that \(\operatorname{WMSO}(G)\) is decidable.

Conversely, if \(\operatorname{WMSO}(G)\) is decidable, Theorem 7.3 gives decidability of \(\operatorname{Th}(\mathcal K(G))\), hence of \(\operatorname{Th}(\mathcal I_{\kappa_G})\). ∎

### Corollary 8.2 — Exact classification at zero density

The equivalence (50) holds while simultaneously requiring

\[
\kappa_G(r)\in\{0,1\},
\qquad
|S_G|=\infty,
\qquad
\delta_{\mathrm{Dir}}(S_G)=0.
\tag{51}
\]

Thus even after fixing all three macroscopic profile invariants in (51), prime-only decidability can realize exactly the WMSO decidability spectrum of countable backward DAGs.

---

## 9. Isomorphism classification of the saturated subfamily

The same canonical form gives a clean isomorphism theorem.

### Theorem 9.1 — Saturated Skeleton Rigidity

For countable backward DAGs \(G,H\),

\[
\boxed{
\mathcal K(G)\cong\mathcal K(H)
\iff
G\cong H.
}
\tag{52}
\]

### Proof

If \(f:G\to H\) is a graph isomorphism, extend it to finite subsets by

\[
F\longmapsto f[F].
\tag{53}
\]

Choose any bijection of the countably infinite copy index set \(\mathbb N\) with itself in each fiber. This extends \(f\) to an isomorphism \(\mathcal K(G)\to\mathcal K(H)\).

Conversely, the active set is definable in \(\mathcal K(G)\), and the induced active relation is exactly \(G\). Hence any isomorphism of saturated normal forms restricts to an isomorphism of their active skeletons. ∎

Thus the profile family already contains the full isomorphism complexity of countable backward DAGs, even under zero-density binary supports.

---

## 10. General multiplicity decomposition

The saturated case is canonical, but it also reveals the exact additional datum in an arbitrary profile.

For a locally finite normal form \(\mathcal L_\kappa=(P,S,R)\), define for every finite subset \(F\subseteq S\)

\[
\mu_\kappa(F)
:=
\bigl|
\{x\in P\setminus S:N_S(x)=F\}
\bigr|
\in
\mathbb N_0\cup\{\aleph_0\}.
\tag{54}
\]

### Theorem 10.1 — Skeleton plus Multiplicity Isomorphism Invariant

The isomorphism type of \(\mathcal L_\kappa\) is completely determined by:

1. the active skeleton
   \[
   G_\kappa=(S,R|_{S\times S});
   \tag{55}
   \]
2. the external multiplicity function \(\mu_\kappa\) on finite subsets of \(S\).

More precisely, two locally finite normal forms \(\mathcal L_\kappa\) and \(\mathcal L_\lambda\) are isomorphic iff there is an active-skeleton isomorphism

\[
f:G_\kappa\to G_\lambda
\tag{56}
\]

such that

\[
\mu_\kappa(F)
=
\mu_\lambda(f[F])
\tag{57}
\]

for every finite \(F\subseteq S_\kappa\).

### Proof

Necessity is immediate: an isomorphism preserves the definable active set, the active relation, and active neighborhoods of external elements, hence preserves each fiber cardinality.

For sufficiency, start with \(f\) on the active set. For every finite \(F\subseteq S_\kappa\), condition (57) provides a bijection between the external fiber with neighborhood \(F\) and the external fiber with neighborhood \(f[F]\). Taking the union of these fiberwise bijections with \(f\) gives an isomorphism of the full locally finite normal forms. ∎

### Consequence 10.2

The arbitrary-profile prime-only classification problem has exactly two channels of information:

\[
\boxed{
\text{active skeleton}
+
\text{external finite-neighborhood multiplicity spectrum}.
}
\tag{58}
\]

The saturated subfamily freezes the second channel to the constant value \(\aleph_0\), leaving only the skeleton. This is why Theorem 8.1 is the natural canonical endpoint of the present branch.

---

## 11. What has now been answered

The original post-Wall question was whether the wild phase survives after weakening or deleting the multiplicative source memory.

The sequence of proved answers is now complete at the structural level.

### Full multiplicative source

For infinite positive support:

\[
\text{undecidable}.
\tag{59}
\]

### Explicit finite-subset carrier

Multiplication can be deleted and the same conclusion remains:

\[
\text{undecidable}.
\tag{60}
\]

### Prime-only reduct

No single support-cardinality wall survives:

\[
\text{decidable and undecidable examples both occur.}
\tag{61}
\]

The exact structural normal form is (58).

### Saturated prime-only subfamily

The external multiplicity channel can be canonically frozen, and then

\[
\boxed{
\text{prime-only decidability}
\iff
\text{WMSO decidability of the active skeleton}.
}
\tag{62}
\]

This is an exact theorem, not a heuristic phase diagram.

---

## 12. What is deliberately not pursued in this branch

A complete decidability classification for **all** possible multiplicity functions \(\mu_\kappa\) would require classifying arbitrary finite-subset multiplicity spectra together with arbitrary programmable active skeletons.

Theorem 10.1 shows that this is not a missing local lemma. It is a genuinely larger classification problem containing two independent infinite relational channels.

Accordingly, the following should be treated as future work rather than an obligation before finalizing the present branch:

- exact decidability criteria for arbitrary multiplicity spectra;
- classification up to elementary equivalence rather than isomorphism for all nonsaturated profiles;
- effective-degree spectra of arbitrary profile theories;
- extensions from backward DAGs to other canonical skeleton classes;
- journal-level comparison with the literature on weak monadic theories and locally finite incidence structures.

---

## 13. Hostile audit checklist

1. **Does simultaneous skeleton programming and saturation exhaust the finite-pattern reservoir?** No. At each finite stage only finitely many primes are forbidden, whereas every required finite pattern has infinitely many realizers.
2. **Can a future active marker spoil an external exact neighborhood?** No. All prime divisors of the witness integer \(N_c\) outside its prescribed neighborhood are permanently forbidden from entering the support.
3. **Can an external witness accidentally become active later?** No. The witness prime itself is permanently support-forbidden.
4. **Does every finite subset eventually receive infinitely many copies?** Yes. The dovetailing enumeration includes every pair \((J,m)\) with \(J\) finite and \(m\in\mathbb N\).
5. **Is the finite-set quotient in Theorem 6.2 genuinely definable?** Yes. Same-neighborhood equivalence is the first-order formula (38), and saturation makes its quotient exactly all finite subsets.
6. **Does quotient interpretation illegitimately identify distinct external copies?** No. The quotient is used only to interpret the finite-set sort of \(\mathcal W(G)\); the original copy multiplicity remains in \(\mathcal K(G)\).
7. **Can \(\mathcal K(G)\) be reconstructed from WMSO without selecting canonical representatives of finite sets?** Yes. External elements are represented by pairs \((F,c)\) in the product of the finite-set sort and an independent pure infinite copy sort.
8. **Does adding the pure copy sort create undecidability?** No. It is a disjoint infinite equality sort with effective quantifier elimination.
9. **Is the equivalence (50) only one-way?** No. Theorem 6.2 gives the lower interpretation and Theorem 7.3 gives the upper reduction.
10. **Does Theorem 10.1 forget active points whose neighborhoods coincide with external fibers?** No. Active membership is a definable unary distinction and is preserved separately by the skeleton isomorphism.

**Internal verdict:** PASS. A dedicated external literature audit and an independent proof reread are still required before publication status is assigned.
