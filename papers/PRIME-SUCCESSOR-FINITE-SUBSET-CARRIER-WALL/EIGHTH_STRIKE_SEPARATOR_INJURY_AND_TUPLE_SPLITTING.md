# Eighth Strike — Separator Injury, Finite CSP, and the Tuple-Splitting Replacement

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-29  
**Status:** proved statements only; no publication status assigned

## 1. Question

The seventh strike reduced arithmetic multiplicity control to threshold separation of valuation vectors. The proposed next step was a finite-family separator lemma:

> Given finitely many external source pairs \((p_i,q_i)\) with \(|N_{p_i}|\ne|N_{q_i}|\), can one add finitely many marker/threshold coordinates which separate all pairs while preserving an empty active skeleton?

The answer depends critically on whether one asks for an absolute construction from the empty base or a monotone extension of an already chosen active support.

The strongest monotone extension statement is **false**, already for one source pair and one existing active marker. This strike gives an explicit Ramanujan counterexample.

The failure is not merely negative. It identifies the exact finite combinatorial object controlling the problem, proves a compactness reduction for global separation, and shows that pairwise separation was stronger than what the bounded-twin-rank program actually needs. The correct replacement is a finite-family **tuple-splitting** problem.

---

## 2. Valuation coordinates

For every rational prime \(p\), set

\[
N_p:=\tau(p)^2-p^{11}\ne0,
\tag{1}
\]

and for every prime \(r\),

\[
a_r(p):=v_r(N_p).
\tag{2}
\]

A threshold coordinate is a pair

\[
c=(r,k),
\qquad r\in\mathbb P,\ k\ge1.
\tag{3}
\]

It records the Boolean test

\[
\chi_c(p):=[a_r(p)\ge k].
\tag{4}
\]

For distinct source primes \(p,q\), define the raw separation set

\[
\Sigma(p,q)
:=
\{(r,k):\chi_{(r,k)}(p)\ne\chi_{(r,k)}(q)\}.
\tag{5}
\]

Equivalently,

\[
(r,k)\in\Sigma(p,q)
\iff
\min(a_r(p),a_r(q))<k\le\max(a_r(p),a_r(q)).
\tag{6}
\]

Because \(N_pN_q\ne0\), only finitely many primes \(r\) can occur in (5), and each contributes finitely many levels \(k\). Thus:

### Lemma 2.1 — Finite raw separator set

For every source pair \((p,q)\),

\[
|\Sigma(p,q)|<\infty.
\tag{7}
\]

If a finite set \(X\) of source primes is required to remain external, define

\[
\Sigma_X(p,q)
:=
\{(r,k)\in\Sigma(p,q):r\notin X\}.
\tag{8}
\]

The exclusion in (8) prevents a source that is supposed to remain external from being turned into an active marker.

---

## 3. Compatibility of active coordinates

Two distinct marker coordinates

\[
c=(r,k),
\qquad d=(s,\ell),
\qquad r\ne s,
\tag{9}
\]

are called **compatible** if activating both preserves the empty active skeleton, i.e.

\[
a_s(r)<\ell
\tag{10}
\]

and

\[
a_r(s)<k.
\tag{11}
\]

Indeed, (10) is exactly \(\neg E(r;s)\), while (11) is exactly \(\neg E(s;r)\).

Two different coordinates with the same marker prime are declared incompatible, because a threshold profile assigns only one value to that prime.

A set of coordinates is compatible if every two of its distinct members are compatible.

### Lemma 3.1 — Empty-skeleton equivalence

A threshold-coordinate set \(T\) is the active-coordinate set of an empty-skeleton threshold profile if and only if \(T\) is pairwise compatible.

### Proof

The empty-skeleton condition is exactly the simultaneous failure of every directed active-active incidence. For two distinct active primes those two failures are (10)-(11). Diagonal incidence is false by definition. ∎

---

## 4. Exact finite-family separator criterion

Let \(A\) be a finite existing compatible coordinate set. Let \(X\) be a finite set of source primes, disjoint from the marker primes used by \(A\), and let

\[
\mathcal P=\{(p_i,q_i):1\le i\le m\}
\tag{12}
\]

be a finite family of source pairs from \(X\).

### Theorem 4.1 — Finite Separator CSP

There exists a finite compatible extension

\[
A\subseteq A\cup T
\tag{13}
\]

which keeps every prime of \(X\) external and separates every pair in \(\mathcal P\) if and only if there exists a compatible set

\[
T\subseteq
\bigcup_{i=1}^m\Sigma_X(p_i,q_i)
\tag{14}
\]

such that:

1. every coordinate of \(T\) is compatible with every coordinate of \(A\);
2. for every \(i\),
   \[
   T\cap\Sigma_X(p_i,q_i)\ne\varnothing.
   \tag{15}
   \]

### Proof

If an extension separates pair \((p_i,q_i)\), some newly selected coordinate must give different Boolean values on \(p_i,q_i\); that coordinate lies in \(\Sigma_X(p_i,q_i)\). Removing irrelevant new coordinates leaves a set \(T\) satisfying (14)-(15), and empty active skeleton gives compatibility.

Conversely, any \(T\) satisfying these conditions can be adjoined to \(A\). Compatibility gives an empty active skeleton, the exclusion \(r\notin X\) keeps the sources external, and (15) separates every pair. ∎

### Corollary 4.2 — Finite decidability of the separator problem

For fixed arithmetic data \(N_p\), a finite-family extension problem is a finite constraint-satisfaction problem: each clause \(\Sigma_X(p_i,q_i)\) is finite, their union is finite, and compatibility of two candidate coordinates is decided by finitely many valuations of explicit nonzero integers.

Thus there is no hidden infinitary freedom at the finite-family level. In particular, Chebotarev cannot create a fresh separator prime for a fixed pair: every raw separator prime already divides \(N_pN_q\).

---

## 5. Explicit Ramanujan counterexample

The monotone finite-family separator lemma fails in the smallest possible nontrivial way.

The relevant exact residual integers are

\[
\tau(2)=-24,
\qquad
N_2=(-24)^2-2^{11}=-1472=-2^6\cdot23,
\tag{16}
\]

\[
\tau(3)=252,
\qquad
N_3=252^2-3^{11}=-113643=-3^4\cdot23\cdot61,
\tag{17}
\]

and

\[
\tau(83)=-29335099668,
\tag{18}
\]

so

\[
N_{83}
=\tau(83)^2-83^{11}
=-427283346006592126043
\tag{19}
\]

with factorization

\[
|N_{83}|
=61\cdot71\cdot971\cdot101603472773843.
\tag{20}
\]

Take the current active support to consist of the single coordinate

\[
A=\{(83,1)\}.
\tag{21}
\]

A singleton active skeleton is empty. Also

\[
83\nmid N_2N_3,
\tag{22}
\]

so sources \(2\) and \(3\) have the same current neighborhood relative to \(A\): both are nonincident to marker \(83\).

Require \(2\) and \(3\) to remain external. From (16)-(17), the valuation differences occur at primes \(2,3,61\), while the valuation at \(23\) is equal. Coordinates at marker primes \(2\) and \(3\) are unavailable because those two sources must remain external. Therefore

\[
\boxed{
\Sigma_{\{2,3\}}(2,3)=\{(61,1)\}.
}
\tag{23}
\]

But (20) gives

\[
a_{61}(83)=v_{61}(N_{83})=1.
\tag{24}
\]

Compatibility of \((61,1)\) with \((83,1)\) would require

\[
a_{61}(83)<1,
\tag{25}
\]

which is false.

Raising the new threshold at \(61\) cannot help: for \(k\ge2\), both

\[
a_{61}(2)=0,
\qquad
a_{61}(3)=1
\tag{26}
\]

lie below \(k\), so \((61,k)\) no longer separates the pair.

Hence:

### Theorem 5.1 — Separator Injury Counterexample

There exists an empty active support consisting of one depth-one marker and a single external source pair with unequal absolute residuals for which **no compatible finite extension separates the pair while keeping both sources external**.

The explicit example is

\[
A=\{(83,1)\},
\qquad
(p,q)=(2,3).
\tag{27}
\]

### Consequence 5.2 — Nonmonotonicity

Separator capacity is not monotone under empty-skeleton support extension.

From the empty base, \((61,1)\) separates \(2\) and \(3\). After adjoining the harmless-looking marker \((83,1)\), that unique external separator is permanently injured.

This invalidates the naive diagonal strategy

> enumerate colliding source pairs and always add a fresh compatible separator later.

There need not be any fresh separator later.

---

## 6. Reservation works in the forward direction

Although arbitrary past choices can injure a future separator, a separator chosen **before** neutral support extension can be protected.

### Lemma 6.1 — Finite Reservation Lemma

Let

\[
A=\{(r_1,k_1),\dots,(r_t,k_t)\}
\tag{28}
\]

be a finite compatible set of good marker coordinates, in the range where the previously proved finite-depth pattern-realization theorem applies.

Then there are infinitely many primes \(s\) for which

\[
a_{r_i}(s)<k_i
\qquad(1\le i\le t).
\tag{29}
\]

For any such \(s\), choosing

\[
\ell>\max_{1\le i\le t}a_s(r_i)
\tag{30}
\]

makes the new coordinate \((s,\ell)\) compatible with every member of \(A\).

### Proof

The finite-depth pattern theorem realizes the all-NONEDGE Boolean pattern simultaneously at the finitely many existing marker coordinates, giving infinitely many source primes \(s\) satisfying (29). Since each \(N_{r_i}\) is a fixed nonzero integer, all valuations \(a_s(r_i)\) are finite, so an integer \(\ell\) satisfying (30) exists. Equation (29) gives the new-source-to-old-marker nonedges, and (30) gives the old-source-to-new-marker nonedges. ∎

### Corollary 6.2

Every finite compatible separator system can be embedded in an infinite empty-skeleton support by repeated neutral extensions.

### Limitation

The new thresholds produced by (30) may be large. Therefore the neutral marker \((s,\ell)\) need not remain usable as a low-depth separator for a future source pair. Reservation protects old separators; it does not solve future separator compatibility.

---

## 7. Compactness: why the empty-base finite-family problem still matters

Fix disjoint countable sets:

- \(X\), the source reservoir required to remain external;
- \(M\), a marker-prime pool.

Allow coordinates only at primes in \(M\). For each distinct \(p,q\in X\), let

\[
\Sigma_M(p,q)
=
\{(r,k)\in\Sigma(p,q):r\in M\}.
\tag{31}
\]

### Theorem 7.1 — Compatible-Transversal Compactness

There exists a compatible threshold-coordinate set \(T\) supported on \(M\) which separates every distinct pair of primes in \(X\) if and only if every finite family of pairs from \(X\) has a finite compatible separator system supported on \(M\).

### Proof

The forward direction is immediate by taking finitely many coordinates from the global set which witness the finitely many pair clauses.

For the reverse direction, introduce one propositional variable \(z_c\) for every allowed coordinate \(c\). Add:

1. for every source pair \((p,q)\), the finite clause
   \[
   \bigvee_{c\in\Sigma_M(p,q)}z_c;
   \tag{32}
   \]
2. for every incompatible pair of coordinates \(c,d\), the clause
   \[
   \neg z_c\lor\neg z_d.
   \tag{33}
   \]

Every finite subset of these propositional clauses mentions only finitely many source-pair requirements. By hypothesis those requirements admit a finite compatible hitting set, which satisfies all relevant incompatibility clauses. Hence every finite subset is satisfiable.

By propositional compactness, the whole clause set is satisfiable. The coordinates assigned true form a compatible set \(T\) and hit every pair-separation clause. ∎

### Interpretation

A finite-family theorem from a **clean reserved base** would be powerful enough, by compactness, to produce a global separating empty-skeleton profile on a fixed external reservoir. The explicit \((83;2,3)\) counterexample shows only that such a theorem cannot be used as an arbitrary monotone extension principle.

The clean-base finite-family problem remains open.

---

## 8. Pairwise separation was stronger than the twin-rank goal

The seventh strike does not require injectivity of the neighborhood map. For a negative coding size \(n\), it only requires a finite bound on the size of each twin class.

This changes the correct local combinatorics.

Let \(Y\) be a finite set of external source primes. Define its **variation set**

\[
\Omega(Y)
:=
\{(r,k):\chi_{(r,k)}\text{ is not constant on }Y\}.
\tag{34}
\]

Equivalently,

\[
\Omega(Y)
=
\bigcup_{p,q\in Y}\Sigma(p,q).
\tag{35}
\]

### Lemma 8.1 — Tuple-Twin Criterion

Let \(T\) be a compatible coordinate set disjoint from a finite external source set \(Y\). Then all primes in \(Y\) have the same active neighborhood if and only if

\[
T\cap\Omega(Y)=\varnothing.
\tag{36}
\]

### Proof

All points of \(Y\) are twins exactly when every selected coordinate gives the same Boolean threshold value on every point of \(Y\). This is precisely the negation of intersecting the variation set. ∎

### Theorem 8.2 — Exact bounded-twin criterion

Fix an external reservoir \(X\) and an integer \(B\ge1\). A compatible coordinate set \(T\) gives twin classes of size at most \(B\) on \(X\) if and only if

\[
\boxed{
T\cap\Omega(Y)\ne\varnothing
\quad
\text{for every }Y\in[X]^{B+1}.
}
\tag{37}
\]

### Proof

If some \((B+1)\)-element set \(Y\) misses all selected variation coordinates, Lemma 8.1 says all its points lie in one twin class, so that class has size at least \(B+1\).

Conversely, if a twin class has size at least \(B+1\), choose \(Y\) to be any \(B+1\) points from it. Lemma 8.1 gives \(T\cap\Omega(Y)=\varnothing\). ∎

### Corollary 8.3 — Pair blockers need not obstruct bounded multiplicity

Failure to separate one pair forces only that some twin class may have size at least two. It does **not** obstruct a bound \(B\ge2\).

Therefore the explicit \((2,3)\) separator injury refutes injective separation but does not refute the asymmetric bounded-twin-rank program.

This is the central correction produced by the strike.

---

## 9. Compactness for bounded twin classes

### Theorem 9.1 — Tuple-Splitting Compactness

Fix disjoint external and marker reservoirs \(X,M\) and an integer \(B\ge1\). There exists a compatible coordinate set supported on \(M\) whose twin classes on \(X\) all have size at most \(B\) if and only if every finite family

\[
Y_1,\dots,Y_t\in[X]^{B+1}
\tag{38}
\]

admits a finite compatible coordinate set \(T\) supported on \(M\) such that

\[
T\cap\Omega(Y_j)\ne\varnothing
\qquad(1\le j\le t).
\tag{39}
\]

### Proof

Use propositional variables for allowed coordinates as in Theorem 7.1. Replace pair-separation clauses by the finite tuple-variation clauses

\[
\bigvee_{c\in\Omega(Y_j),\ \operatorname{prime}(c)\in M}z_c.
\tag{40}
\]

Together with the pairwise incompatibility clauses, finite satisfiability is exactly the hypothesis. Propositional compactness yields a global compatible hitting set. Theorem 8.2 converts it to the desired uniform twin bound. ∎

### Consequence 9.2

The right finite-family problem for the negative side of the multiplicity program is **not**:

> separate every finite family of pairs.

It is:

> for some finite \(B\), split every finite family of \((B+1)\)-tuples by pairwise compatible threshold coordinates.

This is strictly weaker and survives some pairwise separator injuries.

---

## 10. Revised arithmetic frontier

The requested finite-family separator lemma has therefore produced a decisive answer:

\[
\boxed{
\text{arbitrary monotone pair-separator extension is false.}
}
\tag{41}
\]

The explicit cause is **low-depth separator injury**: a previously activated marker source may already satisfy the only low-depth congruence capable of distinguishing a future pair.

But the undecidability program does not require full pairwise injectivity. The sharp replacement is:

\[
\boxed{
\textbf{Finite Tuple-Splitting Problem}.}
\tag{42}
\]

For a chosen finite \(B\), determine whether every finite collection of \((B+1)\)-source tuples admits a compatible set of active threshold coordinates that is nonconstant on every tuple.

A positive theorem of this form, combined with Theorem 9.1, would yield an empty-skeleton profile with uniformly bounded external twin classes. One could then superimpose the lower-control construction on selected coding sizes to recover the bounded-versus-unbounded twin-rank dichotomy from the seventh strike.

---

## 11. Next strike

The next target is now narrower and better matched to what is actually needed:

1. Study \(B=2\): can every finite family of source triples be split by a compatible threshold system from a clean reserved base?
2. If not, find the least \(B\) for which finite tuple splitting becomes possible, or construct arbitrarily large finite **inseparable packs**.
3. Formulate the conflict hypergraph of threshold coordinates explicitly and search for a Hall-/Helly-/Ramsey-type sufficient condition for compatible tuple transversals.
4. Separate unavoidable equal-residual classes \(|N_p|=|N_q|\) from support-induced injuries such as \((83;2,3)\).

The most informative immediate attack is therefore the **triple-splitting case \(B=2\)**. A positive result would already be enough to tolerate all isolated pair injuries while imposing a global multiplicity cap of two on the tame side.

---

## 12. Hostile audit

1. **Could multiple new markers rescue the pair \((2,3)\) after marker \(83\)?**  
   No. Any difference of their final neighborhoods requires at least one individually separating coordinate, and (23) shows the only allowable one is \((61,1)\), which is incompatible with \((83,1)\).

2. **Could threshold \(k>1\) at marker \(61\) preserve independence and still separate \(2,3\)?**  
   No. Their \(61\)-valuations are \(0\) and \(1\), so all \(k\ge2\) give the same Boolean value.

3. **Does marker \(83\) itself already separate \(2,3\)?**  
   No. Equation (22) gives valuation zero for both.

4. **Is the counterexample dependent on an unproved Galois or Chebotarev claim?**  
   No. It uses only explicit values of \(\tau(2),\tau(3),\tau(83)\) and integer factorizations.

5. **Is the relative failure being overstated as failure from the empty base?**  
   No. From the empty base \((61,1)\) separates the pair. The clean-base finite-family theorem is explicitly left open.

6. **Is compactness legitimate although infinitely many coordinates exist?**  
   Yes. Every separation/variation clause is finite by Lemma 2.1, and propositional compactness applies to the countable clause family.

7. **Does pairwise separation remain necessary for the bounded-twin-rank program?**  
   No. Theorem 8.2 proves the exact weaker \((B+1)\)-tuple condition.

8. **Has an actual bounded-twin-rank empty-skeleton Ramanujan profile now been constructed?**  
   No. The strike identifies the correct finite local problem but does not yet prove the triple-splitting or general tuple-splitting lemma.

**Audit verdict:** the monotone pair-separator lemma is refuted by an explicit arithmetic counterexample; the finite CSP, reservation, compactness, and tuple-splitting replacement are proved. The clean-base tuple-splitting problem remains open.
