# Third Strike — A Decidable Prime-Only Infinite-Support Profile

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-28  
**Status:** full proof checkpoint; proved statements only; not yet publication-final

## 0. Result of the strike

The previous checkpoint left open whether source primes outside the positive-depth support could always restore carrier-free Trakhtenbrot coding.

The answer is **no**.

We construct an infinite positive-depth support

\[
S\subseteq\mathbb P
\tag{1}
\]

such that for the profile

\[
\kappa_S(r)=
\begin{cases}
1,&r\in S,\\
0,&r\notin S,
\end{cases}
\tag{2}
\]

the **prime-only residual structure** has a decidable complete theory.

Thus, after removing both source multiplication and the explicit finite-subset carrier, support cardinality alone no longer controls undecidability.

The full Support-Cardinality Wall remains valid in the original two-sorted structure. What fails is its persistence in the prime-only reduct.

---

## 1. Prime-only language

For every prime \(p\), put

\[
N_p:=\tau(p)^2-p^{11}.
\tag{3}
\]

For the profile (2), define

\[
E_S(p;r)
:\iff
p\ne r
\land
\begin{cases}
r\mid N_p,&r\in S,\\
\text{true},&r\notin S.
\end{cases}
\tag{4}
\]

and

\[
I_S(p,q;r)
:=E_S(p;r)\land E_S(q;r).
\tag{5}
\]

Let

\[
\mathcal I_S=(\mathbb P,I_S).
\tag{6}
\]

The binary relation \(E_S\) and the ternary relation \(I_S\) are definitionally equivalent inside this family because

\[
E_S(p;r)
\iff
I_S(p,p;r),
\tag{7}
\]

and (5) defines \(I_S\) from \(E_S\).

Hence it is enough to analyze

\[
\mathcal E_S=(\mathbb P,E_S).
\tag{8}
\]

---

## 2. Every active neighborhood is finite

### Lemma 2.1 — Residual nonvanishing

For every prime \(p\),

\[
N_p\ne0.
\tag{9}
\]

### Proof

If \(N_p=0\), then

\[
\tau(p)^2=p^{11}.
\tag{10}
\]

Taking \(p\)-adic valuations gives

\[
2v_p(\tau(p))=11,
\tag{11}
\]

which is impossible because the left side is even. ∎

For any set \(S\) of primes and any prime \(p\), define the active neighborhood

\[
F_S(p)
:=
\{r\in S:r\ne p,\ r\mid N_p\}.
\tag{12}
\]

### Lemma 2.2 — Local finiteness

For every \(p\), the set \(F_S(p)\) is finite.

### Proof

By Lemma 2.1, \(N_p\) is a nonzero integer. Every member of \(F_S(p)\) is a prime divisor of \(N_p\), and a nonzero integer has only finitely many prime divisors. ∎

---

## 3. Number-theoretic finite-pattern input

Fix once and for all a finite exceptional set

\[
F_\Delta
\tag{13}
\]

outside which the depth-one residual finite-pattern theorem holds. Thus, for every finite set

\[
R\subseteq\mathbb P\setminus F_\Delta
\tag{14}
\]

and every subset \(T\subseteq R\), there are infinitely many source primes \(p\notin R\) such that

\[
r\mid N_p
\iff
r\in T
\qquad(r\in R).
\tag{15}
\]

This is the already-proved depth-one specialization of the adelic-independence plus Chebotarev pattern theorem. No new use of Loeffler or Chebotarev is hidden below; (15) is the only number-theoretic input needed in the construction.

Call a prime **good** if it lies outside \(F_\Delta\).

---

## 4. Construction of a canonical sparse support

We construct recursively an infinite sequence of pairwise distinct good primes

\[
S=\{s_1,s_2,s_3,\dots\}
\tag{16}
\]

with two final properties:

### (A) internal independence

For distinct \(s,t\in S\),

\[
t\nmid N_s.
\tag{17}
\]

### (B) exact finite-neighborhood saturation

For every finite set \(F\subseteq S\), there are infinitely many primes

\[
p\notin S
\tag{18}
\]

such that

\[
F_S(p)=F.
\tag{19}
\]

The construction also allows arbitrary sparseness conditions, for example

\[
s_{n+1}>s_n^2,
\tag{20}
\]

because every pattern-realization set used below is infinite.

### Theorem 4.1 — Existence of a saturated independent support

There exists an infinite good set \(S\) satisfying (17) and (19).

### Proof

We maintain at stage \(n\):

1. a finite chosen set
   \[
   S_n=\{s_1,\dots,s_n\};
   \tag{21}
   \]
2. a finite forbidden set \(B_n\), disjoint from \(S_n\);
3. finitely many already chosen witness primes, all placed in the forbidden set so that none can later enter \(S\).

Start with any good prime \(s_1\), set \(S_1=\{s_1\}\), and begin with a finite forbidden set containing the fixed exceptional primes.

Assume \(S_n\) and \(B_n\) have been constructed.

#### Step 1: create exact-neighborhood witnesses for every current finite subset

For each

\[
F\subseteq S_n,
\tag{22}
\]

apply (15) to the marker set \(R=S_n\) and pattern \(T=F\). There are infinitely many primes \(p\) such that

\[
s\mid N_p
\iff
s\in F
\qquad(s\in S_n).
\tag{23}
\]

Choose one fresh such prime, denoted \(p_{n,F}\), avoiding the finite set consisting of

- \(S_n\);
- \(B_n\);
- all witnesses chosen earlier in the same stage.

This is possible because the realization set is infinite.

Let

\[
Q_{n,F}
:=
\{q\in\mathbb P:q\mid N_{p_{n,F}},\ q\notin F\}.
\tag{24}
\]

The set \(Q_{n,F}\) is finite by Lemma 2.1. By (23), it is disjoint from \(S_n\).

Add to the forbidden set both the witness itself and all its unwanted prime divisors:

\[
p_{n,F}\in B_{n}^{\prime},
\qquad
Q_{n,F}\subseteq B_{n}^{\prime}.
\tag{25}
\]

Doing this for all finitely many subsets \(F\subseteq S_n\) enlarges the forbidden set only finitely.

The purpose of (25) is permanent: no future member of \(S\) will be allowed to be an unwanted prime divisor of \(N_{p_{n,F}}\).

#### Step 2: choose the next support prime

We now choose \(s_{n+1}\).

First use (15) with marker set \(S_n\) and the all-NONEDGE pattern \(T=\varnothing\). Thus there are infinitely many primes \(q\) such that

\[
s_i\nmid N_q
\qquad(1\le i\le n).
\tag{26}
\]

To guarantee the reverse nonedges, define the finite set

\[
C_n
:=
\bigcup_{i=1}^n
\{q:q\mid N_{s_i}\}.
\tag{27}
\]

Choose \(s_{n+1}=q\) from the infinite realization set in (26), additionally avoiding

\[
S_n\cup B_n'\cup C_n\cup F_\Delta,
\tag{28}
\]

and, if desired, satisfying the extra lower bound (20). All excluded sets in (28) are finite, so such a choice exists.

Then (26) gives

\[
s_i\nmid N_{s_{n+1}}
\qquad(i\le n),
\tag{29}
\]

while avoidance of \(C_n\) gives

\[
s_{n+1}\nmid N_{s_i}
\qquad(i\le n).
\tag{30}
\]

Set

\[
S_{n+1}=S_n\cup\{s_{n+1}\}
\tag{31}
\]

and let \(B_{n+1}\) be the finite forbidden set after all additions in the stage.

This completes the recursion.

#### Verification of (A)

Whenever \(s_{n+1}\) is added, equations (29) and (30) establish both directed nonedges between it and all earlier support primes. Therefore (17) holds for every distinct pair in the final set \(S\).

#### Verification of (B)

Let \(F\subseteq S\) be finite. Choose \(N\) such that

\[
F\subseteq S_N.
\tag{32}
\]

For every stage \(n\ge N\), Step 1 chooses a fresh witness \(p_{n,F}\) satisfying (23). All prime divisors of \(N_{p_{n,F}}\) outside \(F\) are placed permanently in the forbidden set by (24)-(25), so none can ever be selected into the future support.

Hence in the final set \(S\),

\[
F_S(p_{n,F})=F.
\tag{33}
\]

The witness prime itself is forbidden from future support membership, so

\[
p_{n,F}\notin S.
\tag{34}
\]

The witnesses are chosen fresh at every stage. Therefore every finite \(F\subseteq S\) has infinitely many distinct witnesses satisfying (19). ∎

---

## 5. Exact isomorphism type of the prime-only structure

Fix a support \(S\) supplied by Theorem 4.1.

Partition the prime universe into

\[
A:=S
\tag{35}
\]

and

\[
C:=\mathbb P\setminus S.
\tag{36}
\]

For every finite \(F\subseteq A\), put

\[
C_F
:=
\{p\in C:F_S(p)=F\}.
\tag{37}
\]

By Theorem 4.1(B), every \(C_F\) is infinite. Since the whole prime set is countable, every \(C_F\) is countably infinite.

The relation \(E_S\) has the following complete description.

### Lemma 5.1 — Canonical relation table

For \(a,a'\in A\) and \(c\in C_F\), \(d\in C_G\):

\[
E_S(a;a')=\text{false},
\tag{38}
\]

\[
E_S(a;c)=\text{true},
\tag{39}
\]

\[
E_S(c;a)
\iff
a\in F,
\tag{40}
\]

and

\[
E_S(c;d)
\iff
c\ne d.
\tag{41}
\]

### Proof

Equation (38) follows from internal independence (17), together with the explicit condition \(p\ne r\) on the diagonal.

If the target prime \(c\) lies outside \(S\), then \(\kappa_S(c)=0\), so the threshold condition is automatic away from the diagonal. Since \(a\in A\) and \(c\in C\) are distinct, (39) follows.

Equation (40) is exactly the definition of \(F_S(c)=F\).

Finally both \(c,d\) lie outside \(S\), so zero depth is automatic whenever \(c\ne d\), and the diagonal exclusion gives (41). ∎

### Definition 5.2 — Canonical finite-subset-copy structure

Let \(A_0\) be a countably infinite pure set. For every finite subset \(F\subseteq A_0\), let

\[
C_F^0=\{(F,n):n\in\mathbb N\}.
\tag{42}
\]

Let

\[
K=A_0\;\dot\cup\;\bigcup_{F\in\operatorname{Fin}(A_0)}C_F^0.
\tag{43}
\]

Define a binary relation \(E_K\) by the same table:

\[
E_K(a,a')=\text{false},
\tag{44}
\]

\[
E_K(a,(F,n))=\text{true},
\tag{45}
\]

\[
E_K((F,n),a)\iff a\in F,
\tag{46}
\]

and

\[
E_K((F,n),(G,m))
\iff
(F,n)\ne(G,m).
\tag{47}
\]

Call this countable structure

\[
\mathcal K=(K,E_K).
\tag{48}
\]

### Theorem 5.3 — Canonicalization

For the support constructed in Theorem 4.1,

\[
\boxed{
\mathcal E_S\cong\mathcal K.
}
\tag{49}
\]

### Proof

Choose an arbitrary bijection

\[
f_A:A\to A_0.
\tag{50}
\]

For each finite \(F\subseteq A\), the set \(C_F\) is countably infinite, as is

\[
C^0_{f_A[F]}.
\tag{51}
\]

Choose a bijection

\[
f_F:C_F\to C^0_{f_A[F]}.
\tag{52}
\]

The union of \(f_A\) and all maps \(f_F\) is a bijection from \(\mathbb P\) to \(K\). Lemma 5.1 and equations (44)-(47) show directly that this bijection preserves and reflects \(E\). ∎

Thus all number-theoretic irregularity has disappeared from the isomorphism type: every finite subset of the active set occurs with countably infinite multiplicity, and no active element points to another active element.

---

## 6. Decidability of the canonical structure

We now prove that \(\operatorname{Th}(\mathcal K)\) is decidable.

The proof is by an effective translation into weak monadic second-order logic over \((\mathbb N,<)\), whose decidability is classical (Büchi-Elgot).

In weak monadic second-order logic, second-order variables range over **finite** subsets of \(\mathbb N\).

### Lemma 6.1 — Effective WMSO interpretation

The first-order theory of \(\mathcal K\) is effectively reducible to the weak monadic second-order theory of

\[
(\mathbb N,<).
\tag{53}
\]

### Proof

Identify the pure active set \(A_0\) with \(\mathbb N\).

Represent elements of \(\mathcal K\) by two representation types:

1. an active element \(a\in A_0\) is represented by one first-order variable \(a\in\mathbb N\);
2. an inactive element \((F,n)\) is represented by a pair
   \[
   (X,c),
   \tag{54}
   \]
   where \(X\) is a weak monadic set variable, hence a finite subset of \(\mathbb N\), and \(c\) is a first-order variable.

The pair \((X,c)\) represents exactly the canonical element \((F,n)\) with \(F=X\) and copy index \(n=c\).

Equality is translated by cases:

- active-active:
  \[
  a=b;
  \tag{55}
  \]
- active-inactive or inactive-active: false;
- inactive-inactive:
  \[
  X=Y\land c=d,
  \tag{56}
  \]
  where set equality is
  \[
  \forall z\,(z\in X\leftrightarrow z\in Y).
  \tag{57}
  \]

The relation \(E_K\) is translated using (44)-(47):

- active-active: false;
- active-inactive: true;
- inactive-active:
  \[
  a\in X;
  \tag{58}
  \]
- inactive-inactive:
  \[
  \neg(X=Y\land c=d).
  \tag{59}
  \]

Finally, every first-order quantifier over \(K\) is translated by splitting into the two representation types. Schematically,

\[
\exists v\,\psi(v)
\tag{60}
\]

becomes the disjunction of

\[
\exists a\,\psi_A(a)
\tag{61}
\]

and

\[
\exists X\exists c\,\psi_C(X,c),
\tag{62}
\]

and universal quantifiers are handled dually. Repeating this recursively gives an effective translation of every first-order \(E\)-sentence into a WMSO sentence over \((\mathbb N,<)\). The order symbol itself need not occur in the translated sentence; it is available only as part of the known decidable ambient theory.

By construction, truth is preserved in both directions. ∎

### Theorem 6.2 — Decidability of the canonical structure

\[
\boxed{
\operatorname{Th}(\mathcal K)
\text{ is decidable}.
}
\tag{63}
\]

### Proof

By Lemma 6.1, every first-order sentence about \(\mathcal K\) is effectively translated to a sentence of the weak monadic second-order theory of \((\mathbb N,<)\). The latter theory is decidable by the classical Büchi-Elgot decision theorem. Therefore truth in \(\mathcal K\) is decidable. ∎

A convenient classical reference is:

J. Richard Büchi, *Weak Second-Order Arithmetic and Finite Automata*, Mathematical Logic Quarterly 6 (1960), 66-92, DOI 10.1002/malq.19600060105.

The proof above needs only the decision procedure as an external theorem; the interpretation itself is explicit.

---

## 7. Decidable prime-only infinite-support theorem

### Theorem 7.1 — Decidable Sparse Infinite Support

There exists a threshold profile

\[
\kappa:\mathbb P\to\{0,1\}
\tag{64}
\]

with infinite positive-depth support

\[
|P_{\mathrm{pos}}(\kappa)|=\infty
\tag{65}
\]

such that the complete theory of the prime-only residual structure

\[
\mathcal I_\kappa=(\mathbb P,I_\kappa)
\tag{66}
\]

is decidable.

Moreover the positive support may be chosen arbitrarily sparse, for example satisfying (20).

### Proof

Take the support \(S\) from Theorem 4.1 and the profile \(\kappa_S\) from (2). The support is infinite by construction and takes only values \(0,1\).

By Theorem 5.3,

\[
(\mathbb P,E_S)\cong\mathcal K.
\tag{67}
\]

Theorem 6.2 gives decidability of \(\operatorname{Th}(\mathbb P,E_S)\).

Since \(I_S\) and \(E_S\) are definitionally equivalent by (5) and (7), their complete theories are effectively interreducible. Therefore

\[
\operatorname{Th}(\mathcal I_S)
\]

is decidable. ∎

---

## 8. The carrier-free infinite-support implication is false

The preceding theorem settles the exact question left by the second strike.

### Corollary 8.1 — Failure of carrier-free support-cardinality universality

The implication

\[
|P_{\mathrm{pos}}(\kappa)|=\infty
\Longrightarrow
\operatorname{Th}(\mathbb P,I_\kappa)
\text{ undecidable}
\tag{68}
\]

is false.

### Proof

The profile supplied by Theorem 7.1 has infinite positive support but decidable prime-only theory. ∎

Thus source primes outside the positive support **cannot, in general, remove the alignment hypothesis**.

This is stronger than the previous independent-support construction, which only proved collapse of regular-positive GIR. Here the entire prime-only complete theory is shown decidable.

---

## 9. A genuine new phase split after carrier removal

Combine Theorem 7.1 with the previously proved density-one theorem:

\[
\delta(P_{\mathrm{pos}}(\kappa))=1
\Longrightarrow
\operatorname{Th}(\mathbb P,I_\kappa)
\text{ undecidable}.
\tag{69}
\]

We therefore obtain two infinite-support profiles with opposite logical behavior in the prime-only reduct:

\[
\boxed{
\begin{array}{ccl}
\text{density-one support}
&\Longrightarrow&
\text{prime-only undecidable},\\[2mm]
\text{saturated independent sparse support}
&\Longrightarrow&
\text{prime-only decidable}.
\end{array}
}
\tag{70}
\]

In the **full** threshold structure, both profiles still lie on the amplifying side of the published Support-Cardinality Wall and hence have undecidable complete theories.

Therefore the finite-set/multiplicative carrier is not a cosmetic convenience. It is exactly what makes mere infinitude of positive support sufficient uniformly over all profiles.

After deleting that carrier, the phase diagram becomes distribution-sensitive.

---

## 10. Conceptual interpretation

The prime-only residual graph can be viewed as follows.

For active markers \(S\), each source prime \(p\) carries the finite neighborhood

\[
F_S(p)\subseteq S.
\tag{71}
\]

The construction forces:

1. every active source has empty active neighborhood;
2. every finite subset of \(S\) occurs as the active neighborhood of infinitely many inactive sources.

Hence the prime-only structure collapses to a canonical finite-subset incidence system with infinite multiplicities. Such a system is still expressive enough to exhibit arbitrary finite local patterns, but those patterns do **not** force undecidability: its entire first-order theory is reducible to decidable WMSO.

This gives a precise warning:

\[
\boxed{
\text{arbitrary finite pattern realization}
\not\Rightarrow
\text{undecidability}.
}
\tag{72}
\]

The missing ingredient is not simply finite-set packaging, since finite subsets can be represented internally. What matters is a stronger mechanism that lets finite codes be **reified and composed as graph addresses**.

---

## 11. Revised research boundary

The second strike named a Source/Marker Alignment Wall. The third strike shows that this is a real boundary, not merely a gap in one proof technique.

For the prime-only reduct:

\[
\boxed{
\text{support cardinality alone is insufficient.}
}
\tag{73}
\]

A sharper future classification problem is now:

> **Carrier-Free Classification Problem.**  
> Characterize those infinite supports \(S\) for which \(\operatorname{Th}(\mathbb P,I_{\kappa_S})\) is decidable, and those for which it is undecidable.

Known proved points are now:

- density-one positive support: undecidable;
- regular-positive GIR infinity: undecidable;
- the saturated independent sparse support constructed here: decidable.

The next invariant must therefore measure more than cardinality. Natural candidates are recurrence of \(S\) inside the relevant Chebotarev pattern classes, or an intrinsic source/marker reification property.

No theorem identifying the exact invariant is claimed here.

---

## 12. Hostile-audit checklist

The proof above was checked against the following failure modes.

1. **Could \(N_p=0\) destroy local finiteness?** No; Lemma 2.1 rules this out by parity of \(p\)-adic valuation.
2. **Could a witness later acquire extra active neighbors?** No; every unwanted prime divisor of its fixed integer \(N_p\) is permanently forbidden from entering \(S\).
3. **Could the forbidden set become infinite at a finite stage?** No; each stage handles finitely many subsets of the finite set \(S_n\), and each corresponding integer has finitely many prime divisors.
4. **Could the recursion run out of new support primes?** No; the required all-NONEDGE realization set is infinite, while every additional exclusion at that stage is finite.
5. **Are both directions of internal independence enforced?** Yes; (26) gives new-to-old nonedges and avoidance of (27) gives old-to-new nonedges.
6. **Does every final finite subset get infinitely many exact witnesses?** Yes; once \(F\subseteq S_N\), it is handled afresh at every stage \(n\ge N\).
7. **Do zero-depth columns obey the canonical table?** Yes; away from the diagonal their threshold condition is automatic.
8. **Is the canonical isomorphism affected by multiplicities?** No; every finite-neighborhood class is countably infinite on both sides.
9. **Does the WMSO translation quantify only over finite sets?** Yes; inactive supports are represented by weak monadic set variables, whose semantics are finite subsets.
10. **Is the decision reduction effective?** Yes; every first-order quantifier is recursively split into the two representation types and every atomic formula has an explicit WMSO translation.
11. **Does decidability depend on computing the constructed set \(S\)?** No. The complete theory depends only on the canonical isomorphism type (48), not on an algorithm deciding membership in \(S\).
12. **Does this contradict the Support-Cardinality Wall?** No. That wall concerns the full structure with its carrier; the theorem here concerns the much weaker prime-only reduct.

**Current verdict:** the counterexample theorem survives the first full hostile audit. A separate literature/priority audit is still required before publication.