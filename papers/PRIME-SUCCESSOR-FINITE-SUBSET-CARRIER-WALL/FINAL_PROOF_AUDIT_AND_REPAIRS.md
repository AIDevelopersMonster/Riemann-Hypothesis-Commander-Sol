# Final Proof Reread and Hostile Audit — Prime-Only Carrier Elimination Branch

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Date:** 2026-08-29  
**Status:** final mathematical audit  
**Verdict:** **PASS after two formal repairs recorded below**

## 1. Audit scope

This reread treats the branch as a dependency chain rather than as five independent checkpoints.

The claims audited are:

1. finite-set carrier elimination on the amplifying side;
2. exact finite difference coding in the prime-only reduct;
3. existence of a decidable infinite-support prime-only profile;
4. parameter-free definability of positive support;
5. locally finite incidence normal form;
6. active-skeleton programmability at arbitrarily sparse support;
7. zero-density undecidable profiles and bounded-GIR undecidability;
8. simultaneous skeleton programming plus external-neighborhood saturation;
9. exact WMSO decidability equivalence for saturated profiles;
10. skeleton-plus-multiplicity isomorphism classification.

The audit deliberately attempts to break each transition by checking diagonal cases, future-stage interference, residual exceptional primes, quotient invariance, and effectiveness of all logical reductions.

---

## 2. Dependency input from the published Support-Cardinality Wall

The branch uses one number-theoretic input from the preceding proved work.

For every finite set of sufficiently good positive-depth marker primes

\[
R=\{r_1,\dots,r_m\}
\]

and every subset \(T\subseteq R\), there are infinitely many source primes \(p\notin R\) such that

\[
E_\kappa(p;r)\iff r\in T
\qquad(r\in R).
\]

The earlier proof derives this from:

- adelic openness for the Galois representation attached to \(\Delta\);
- full independent \(\operatorname{SL}_2\)-factors outside a finite exceptional set;
- integral EDGE/NONEDGE matrices valid at all positive finite depths;
- Chebotarev applied to the corresponding finite Galois quotient.

No new arithmetic assumption is introduced in the prime-only branch.

---

## 3. Nonvanishing and local finiteness — PASS

For

\[
N_p=\tau(p)^2-p^{11},
\]

if \(N_p=0\), then

\[
2v_p(\tau(p))=11,
\]

which is impossible. Hence \(N_p\ne0\) for every prime \(p\).

Therefore, for any positive support \(S\),

\[
\{r\in S:r\mid N_p\}
\]

is finite for each fixed source prime \(p\).

**Counterexample attempt:** allow \(\tau(p)=0\). Then \(N_p=-p^{11}\ne0\), so the argument becomes easier rather than failing.

**Verdict:** PASS.

---

## 4. Exact finite difference coding — PASS

The difference formula

\[
D(a,b;r):=r\ne a\land r\ne b\land E(a;r)\land\neg E(b;r)
\]

always defines a finite set because zero-depth markers cancel and every remaining member divides the fixed nonzero integer \(N_a\).

For any finite set \(T\) of good positive-depth markers, the construction first chooses \(a\) incident with every marker in \(T\). Its entire positive edge support is finite. One then changes exactly the coordinates in \(T\) by multiplying the finite residual representation by an element of the cyclotomic-kernel image whose good local components are prescribed and whose other components are identity. Chebotarev supplies \(b\).

The possible presence of bad primes in the finite support of \(a\) causes no problem: the adelic full-factor subgroup used for the correcting element has identity at the exceptional coordinates, so the old local data are preserved there.

Hence

\[
D(a,b;r)\iff r\in T
\]

holds globally.

**Verdict:** PASS.

---

## 5. Decidable sparse profile — PASS

The recursive construction of an independent support \(S\) and exact-neighborhood witnesses has two permanent bookkeeping rules:

1. every new support prime avoids all prime divisors of the earlier support integers \(N_s\), which prevents reverse active-active edges;
2. after an external witness \(c\) for a finite neighborhood \(F\) is chosen, every prime divisor of \(N_c\) outside \(F\), and the prime \(c\) itself, are permanently forbidden from entering the future support.

At each finite stage only finitely many primes are forbidden, while every prescribed finite residual pattern has infinitely many realizers. The recursion therefore never gets stuck.

Every finite \(F\subseteq S\) receives infinitely many exact external witnesses. The resulting structure has the canonical form

\[
S\ \dot\cup\ \bigl(\operatorname{Fin}(S)\times\mathbb N\bigr)
\]

with independent active part and countably many copies of every finite neighborhood.

Its first-order theory reduces effectively to WMSO over a countable pure enumeration (equivalently to WS1S after adding an arbitrary order used only for coding). Each structure variable is translated by a two-case syntactic disjunction:

- active case: one first-order number variable;
- external case: one finite-set variable together with one first-order copy-index variable.

No definable tag element is required.

**Verdict:** PASS.

---

## 6. Parameter-free support definability — PASS

Define

\[
\operatorname{Pos}(r):=\exists p\,(p\ne r\land\neg E(p;r)).
\]

If \(\kappa(r)=0\), then every off-diagonal incidence into \(r\) is true, so \(\operatorname{Pos}(r)\) fails.

If \(k=\kappa(r)\ge1\) and \(r\ne3\), take the identity conjugacy class in the finite residual image modulo \(r^k\). Chebotarev gives infinitely many primes \(p\ne r\) with

\[
\tau(p)\equiv2,
\qquad
p^{11}\equiv1
\pmod{r^k}.
\]

Thus

\[
N_p\equiv3\pmod{r^k},
\]

so \(r^k\nmid N_p\) for \(r\ne3\). For \(r=3\), the explicit prime \(p=2\) gives

\[
N_2=-1472,
\qquad
3\nmid N_2.
\]

Hence \(\operatorname{Pos}(r)\) defines the positive support exactly.

The case \(r=2\) is covered by the identity-class argument because \(3\) is odd.

**Verdict:** PASS.

---

## 7. Locally finite incidence normal form — PASS

With

\[
R(p,r):=\operatorname{Pos}(r)\land E(p;r),
\]

every left fiber is finite. Conversely,

\[
E(p;r)
\iff
p\ne r\land
\bigl(\neg\operatorname{Pos}(r)\lor R(p,r)\bigr).
\]

Thus the ternary prime-only structure is parameter-free interdefinable with

\[
(P,S,R),
\]

where \(R\subseteq P\times S\) is left-locally finite.

No information is lost at zero-depth target primes: all such columns are determined by equality alone.

**Verdict:** PASS.

---

## 8. Active-skeleton programmability — PASS

For a backward DAG enumeration \(v_0,v_1,\dots\), the new support prime \(s_n\) is chosen to realize exactly the prescribed outgoing pattern on earlier markers. Reverse edges from old support primes to \(s_n\) are killed by avoiding the finite union of prime divisors of the earlier \(N_{s_i}\).

Future stages cannot alter already decided incidences.

Arbitrary lower bounds on \(s_n\) can be imposed because every finite pattern realization set is infinite and hence unbounded. Choosing, for example,

\[
s_n>2^{n^2}
\]

gives natural and Dirichlet density zero.

**Verdict:** PASS.

---

## 9. Formal repair 1 — incidence-DAG graph interpretation

The fourth checkpoint defined adjacency of sink vertices informally “for distinct vertices.” In the publication manuscript the formula must include this restriction syntactically.

The correct definition is

\[
\operatorname{Adj}(x,y)
:=
\operatorname{Vert}(x)
\land
\operatorname{Vert}(y)
\land
x\ne y
\land
\exists e\,(e\to x\land e\to y).
\]

Without the conjunct \(x\ne y\), every endpoint would acquire a loop because the same edge-node witnesses both occurrences when \(x=y\).

This is a **formal repair only**. All uses of the relation in the checkpoint were explicitly for distinct vertices, so no theorem changes.

**Repair status:** CLOSED.

---

## 10. Zero-density undecidability and bounded active GIR — PASS

Programming the incidence DAG of a graph \(H\) gives a parameter-free interpretation of \(H\) in the active skeleton. Choosing a graph whose complete theory computes a nonrecursive set gives an undecidable prime-only profile.

If the incidence DAG is used, every active vertex has out-degree at most two. An active GIR grid of size \(n\) forces each active row witness to have at least \(n\) distinct active outgoing marker edges. Hence

\[
\operatorname{GIR}^+\le2.
\]

Thus infinite regular-positive GIR is sufficient but not necessary for prime-only undecidability.

**Verdict:** PASS.

---

## 11. Saturated skeleton realization — PASS

The saturation construction dovetails two countable requirement families:

- support vertices implementing the prescribed backward DAG;
- external witnesses \(c_{J,m}\) for every finite set of support indices \(J\) and every copy number \(m\).

When a witness \(c_{J,m}\) is created, all support markers indexed by \(J\) already exist. The current finite residual pattern makes those and only those current markers adjacent to \(c_{J,m}\). Every prime divisor of \(N_{c_{J,m}}\) outside the prescribed neighborhood is then permanently forbidden from entering the support.

Therefore no future marker can enlarge the witness neighborhood.

At every finite stage the union of all forbidden sets remains finite, so the next skeleton vertex and the next external witness can both be chosen from infinite residual realization sets.

Every finite subset of the final support corresponds to a finite index set \(J\), and all requirements \((J,m)\) are eventually served.

Hence every finite neighborhood occurs countably infinitely often.

**Verdict:** PASS.

---

## 12. WMSO lower interpretation — PASS

In the saturated normal form \(\mathcal K(G)\), define on external elements

\[
x\sim y
\iff
\forall v\in S\,
(R(x,v)\leftrightarrow R(y,v)).
\]

The quotient is exactly \(\operatorname{Fin}(V)\): every external neighborhood is finite, and saturation supplies representatives of every finite set.

Membership is invariant on equivalence classes and is given by \(R(x,v)\). The active relation restricted to \(S\times S\) is exactly \(G\).

Therefore

\[
\mathcal W(G)
=(V,\operatorname{Fin}(V),\in,\to_G)
\]

is parameter-free interpretable by a definable quotient in \(\mathcal K(G)\).

This yields an effective reduction

\[
\operatorname{WMSO}(G)\le_m\operatorname{Th}(\mathcal K(G)).
\]

**Verdict:** PASS.

---

## 13. Formal repair 2 — WMSO upper reduction

The fifth checkpoint said “use a finite tag” to combine active representatives \(v\) and external representatives \((F,c)\) into one interpreted domain. A literal definable tag is unnecessary and, without naming constants in the pure-copy sort, would require extra bookkeeping.

The publication proof will instead use the following direct effective translation.

For every first-order variable \(x\) of \(\mathcal K(G)\), introduce two representation cases:

\[
A_x(v_x)
\qquad\text{or}\qquad
X_x(F_x,c_x),
\]

where \(v_x\) is a vertex variable, \(F_x\) is a finite-set variable of \(\mathcal W(G)\), and \(c_x\) is a variable in an independent infinite pure equality sort \(C\).

Translate atomic equality by four cases:

\[
A_x\land A_y:\quad v_x=v_y,
\]

\[
A_x\land X_y\quad\text{or}\quad X_x\land A_y:\quad\bot,
\]

\[
X_x\land X_y:\quad F_x=F_y\land c_x=c_y.
\]

Translate the active predicate by the active case only.

Translate \(R(x,y)\) by the disjunction of the two possible source cases with the mandatory active target case:

\[
A_x(v_x)\land A_y(v_y)\land(v_x\to_G v_y),
\]

or

\[
X_x(F_x,c_x)\land A_y(v_y)\land(v_y\in F_x).
\]

All other cases are false.

Boolean connectives are translated recursively. A quantifier

\[
\exists x\,\varphi
\]

is translated to the disjunction

\[
\exists v_x\,\varphi^{A_x}
\quad\lor\quad
\exists F_x\exists c_x\,\varphi^{X_x}.
\]

Universal quantifiers are treated by duality.

This is a uniform effective translation of every first-order sentence of \(\mathcal K(G)\) into the first-order theory of the two-sorted weak-monadic structure \(\mathcal W(G)\) disjointly expanded by the pure infinite equality sort \(C\).

The latter expansion is decidable exactly when \(\operatorname{WMSO}(G)\) is decidable, because the pure equality sort has effective quantifier elimination and no cross-sort relations.

Hence

\[
\operatorname{Th}(\mathcal K(G))\le_m\operatorname{WMSO}(G)
\]

for decidability purposes.

This makes the upper direction fully formal without any tag constants.

**Repair status:** CLOSED.

---

## 14. Exact WMSO equivalence — PASS

Combining Sections 12 and 13 gives, for every saturated realization of a backward DAG \(G\),

\[
\boxed{
\operatorname{Th}(\mathcal I_{\kappa_G})
\text{ decidable}
\iff
\operatorname{WMSO}(G)
\text{ decidable}.
}
\]

The construction of the support itself need not be computable from a noncomputable presentation of \(G\). The theorem is a statement about fixed structures. The logical translations are uniform and effective once the language of \(G\) is given.

**Verdict:** PASS.

---

## 15. Skeleton plus multiplicity invariant — PASS

For an arbitrary prime-only normal form define

\[
\mu(F)
=
|\{x\notin S:N_S(x)=F\}|
\in\mathbb N_0\cup\{\aleph_0\}.
\]

An isomorphism preserves the definable active set, active-active incidence, and every external active-neighborhood fiber, so it preserves the active skeleton and \(\mu\).

Conversely, an active-skeleton isomorphism that preserves all fiber cardinalities extends by choosing independent bijections on each external neighborhood fiber.

Therefore

\[
(G_\kappa,\mu_\kappa)
\]

is a complete isomorphism invariant for the prime-only normal form.

**Verdict:** PASS.

---

## 16. Counterexample campaign

The final audit explicitly attempted the following breaks.

1. **Lehmer-zero break:** \(\tau(p)=0\). Fails to break the proof because \(N_p=-p^{11}\ne0\).
2. **Diagonal break:** source equals marker. All formulas retain explicit diagonal exclusion where required.
3. **Bad-prime break:** exceptional residual primes. Programming uses only good active markers; support definability handles every prime separately and treats \(3\) explicitly.
4. **Future-marker break:** a later support prime could enlarge an exact external neighborhood. Permanent divisor prohibition blocks this.
5. **Reverse-edge break:** a new support prime could create an old-to-new active edge. Divisor avoidance of previous \(N_s\) blocks this.
6. **Finite-reservoir break:** infinitely many requirements might exhaust realizers. At each finite stage only finitely many primes are excluded from an infinite Chebotarev set.
7. **Quotient break:** two external copies of the same finite set collapse. This is intended only in the lower WMSO interpretation; the original structure retains copies in the upper translation.
8. **Copy-index break:** adding infinitely many copies might add undecidability. The copy coordinate is a disjoint pure equality sort.
9. **Density break:** zero density might forbid programming. Arbitrarily large realizers allow any prescribed growth lower bounds.
10. **GIR-classification break:** undecidability might still require infinite active GIR. The incidence-DAG construction gives undecidability with active out-degree at most two and hence \(\operatorname{GIR}^+\le2\).

No counterexample survives.

---

## 17. Final mathematical verdict

After the two formal repairs above, the branch has no known open proof obligation.

The mathematically justified stopping point is:

\[
\boxed{
\text{prime-only normal form}
=
\text{active skeleton}
+
\text{external finite-neighborhood multiplicity spectrum},
}
\]

with the saturated subfamily satisfying the exact WMSO decidability equivalence.

A complete decidability classification for arbitrary multiplicity spectra is a larger new problem, not a missing lemma of this branch.

**FINAL INTERNAL VERDICT: PASS.**
