# Seventh Strike — Asymmetric Multiplicity Coding and the Twin-Rank Barrier

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-29  
**Status:** proved statements only; arithmetic realization remains open; no publication status assigned

## 1. Aim

The sixth strike proved that pure multiplicity memory can make an empty-skeleton incidence model undecidable, using the exact prescription

\[
\mu(F)\in\{1,2\}.
\]

That exact cap is arithmetically expensive. The present strike asks whether one can weaken it to an asymmetric condition in which the positive coding direction uses only lower multiplicity control and the negative direction asks for as little upper control as possible.

Three proposed alternatives are analyzed:

1. finite versus infinite multiplicity;
2. parity of finite multiplicity;
3. existence of a unique twin class.

The main conclusion is that the right first-order invariant is not literal finite-versus-infinite multiplicity of one class but the **bounded-versus-unbounded twin rank by neighborhood size**.

This yields a strictly weaker undecidability target than the previous \(1/2\)-coding:

\[
\boxed{
\sup_{|F|=n}\mu(F)=\infty
\quad\text{versus}\quad
\sup_{|F|=n}\mu(F)<\infty.
}
\]

On positive coding sizes, unboundedness can be forced by lower control alone. On negative coding sizes, one needs only the existence of some finite bound, not a prescribed cap and not exact multiplicities.

For the actual Ramanujan threshold family, this remaining upper-control problem is equivalent to a constrained threshold-separation/hitting problem on the valuation vectors of

\[
N_p=\tau(p)^2-p^{11}.
\]

---

## 2. Empty-skeleton setting

Let \(S\) be the definable active set and suppose the active skeleton is empty. For an external point \(x\), write

\[
N(x)=\{s\in S:R(x,s)\}.
\]

Every external neighborhood is finite.

Define the twin relation

\[
\operatorname{Twin}(x,y)
:\iff
x,y\notin S
\land
\forall s\in S\,
\bigl(R(x,s)\leftrightarrow R(y,s)\bigr).
\tag{1}
\]

For \(n\ge0\), let \(\operatorname{Deg}_n(x)\) be the first-order formula saying that \(x\) is external and has exactly \(n\) active neighbors.

For \(m\ge1\), define the sentence

\[
\Theta_{n,m}
:\iff
\exists x_1\cdots\exists x_m
\left[
\bigwedge_{i\ne j}x_i\ne x_j
\land
\bigwedge_{i=1}^m\operatorname{Twin}(x_1,x_i)
\land
\operatorname{Deg}_n(x_1)
\right].
\tag{2}
\]

Thus \(\Theta_{n,m}\) says that some neighborhood of size \(n\) has at least \(m\) external copies.

For a multiplicity function \(\mu\), define the **twin rank at size \(n\)** by

\[
M_\mu(n)
:=
\sup\{\mu(F):F\subseteq S,\ |F|=n\}
\in
\mathbb N_0\cup\{\infty\},
\tag{3}
\]

where \(\infty\) means that the finite multiplicities are unbounded or that at least one fiber is actually infinite.

### Lemma 2.1 — First-order visibility of twin rank

For every \(n,m\),

\[
\boxed{
\mathfrak M_\mu\models\Theta_{n,m}
\iff
M_\mu(n)\ge m.
}
\tag{4}
\]

### Proof

The sentence \(\Theta_{n,m}\) is true exactly when there exists some size-\(n\) neighborhood fiber containing \(m\) distinct external representatives. This is exactly the condition that the supremum in (3) is at least \(m\). ∎

### Consequence 2.2

The complete first-order theory determines whether \(M_\mu(n)\) is each particular finite number: query \(\Theta_{n,1},\Theta_{n,2},\dots\) until the first false sentence. If no threshold ever fails, first-order theory sees the value only as \(\infty\); it does not by these sentences distinguish one infinite fiber from arbitrarily large finite fibers.

---

## 3. Why literal finite-versus-infinite multiplicity is not the correct FO bit

A single fiber may have finite or infinite cardinality. However this distinction is not uniformly first-order definable across the class of multiplicity models.

### Proposition 3.1 — No uniform FO test for fiber infinitude

There is no first-order formula \(\Phi(x)\) such that in every empty-skeleton multiplicity model and for every external \(x\),

\[
\Phi(x)
\iff
[x]_{\operatorname{Twin}}\text{ is infinite}.
\tag{5}
\]

### Proof

Let \(q\) be the quantifier rank of a proposed formula \(\Phi\). Fix one finite neighborhood \(F\), and consider two models identical outside the fiber over \(F\). In the first model let that fiber have some finite cardinality \(N>q+1\); in the second let it be countably infinite. Point each model at one representative of that fiber.

In the \(q\)-round Ehrenfeucht–Fraïssé game, Duplicator matches the distinguished point and, whenever Spoiler chooses a new member of the distinguished fiber, chooses a fresh member on the other side. Fewer than \(q+1\) fresh representatives are ever required, and both fibers contain enough. Outside the fiber the structures are identical. Hence the two pointed structures satisfy the same formulas of quantifier rank at most \(q\), contradicting (5). ∎

### Remark 3.2

Thus the complete theory can observe all finite thresholds \(\mu(F)\ge m\), but “this fiber is infinite” is an infinite scheme, not one first-order bit.

This matters for reductions: finite-versus-infinite coding becomes useful only if the finite side comes with enough uniform boundedness to make a finite threshold eventually fail, or if one uses a Turing reduction together with an external semidecision procedure.

---

## 4. Bounded-versus-unbounded twin rank is enough

Let \(K\subseteq\mathbb N\) be any fixed computably enumerable nonrecursive set, for example a standard halting set.

### Theorem 4.1 — Asymmetric Twin-Rank Undecidability Criterion

Suppose an empty-skeleton multiplicity model satisfies

\[
M_\mu(n)=\infty
\iff
n\in K,
\tag{6}
\]

and

\[
M_\mu(n)<\infty
\iff
n\notin K.
\tag{7}
\]

Then

\[
\boxed{
\operatorname{Th}(\mathfrak M_\mu)
\text{ is undecidable}.
}
\tag{8}
\]

Indeed,

\[
K\le_T\operatorname{Th}(\mathfrak M_\mu).
\tag{9}
\]

### Proof

Assume an oracle for the complete theory is available. To decide whether a given \(n\) belongs to \(K\), run two procedures in parallel.

1. Enumerate the c.e. set \(K\) until \(n\) appears.
2. Query the theory successively on
   \[
   \Theta_{n,1},\Theta_{n,2},\Theta_{n,3},\dots.
   \tag{10}
   \]
   Stop when the first false answer appears.

If \(n\in K\), then by (6) every sentence in (10) is true, while the enumeration of \(K\) eventually outputs \(n\). The first procedure halts and answers yes.

If \(n\notin K\), then by (7) there is a finite value

\[
B_n:=M_\mu(n).
\]

Hence \(\Theta_{n,B_n+1}\) is false. The second procedure eventually reaches this query and answers no.

Thus the two procedures together decide \(K\) using the theory oracle. Since \(K\) is nonrecursive, the complete theory cannot be decidable. ∎

### Why this is strictly weaker than exact \(1/2\)-coding

For \(n\in K\), no exact multiplicity is prescribed. It is enough that arbitrarily large twin classes exist; there need not even be one infinite class.

For \(n\notin K\), no cap is prescribed in advance. One only requires the existence of some finite bound \(B_n\), which may depend arbitrarily on \(n\) and need not be computable.

Thus the exact old requirement

\[
\mu(F)=1\text{ or }2
\]

has been weakened to

\[
\boxed{
\text{unbounded twin multiplicity on positive sizes,}
\quad
\text{some finite uniform bound on negative sizes.}
}
\tag{11}
\]

This is the weakest successful asymmetric target obtained in this strike.

---

## 5. Positive bits require only lower control

### Proposition 5.1 — Lower-control sufficiency on the positive side

Fix a size \(n\). To force

\[
M_\mu(n)=\infty,
\tag{12}
\]

it is enough, for every \(m\ge1\), to construct one finite neighborhood \(F_m\) of size \(n\) with

\[
\mu(F_m)\ge m.
\tag{13}
\]

No upper multiplicity control is needed.

### Proof

Conditions (13) imply

\[
M_\mu(n)\ge m
\]

for every \(m\), hence the supremum in (3) is \(\infty\). ∎

### Arithmetic relevance

The previous finite-pattern and protection constructions are precisely of this one-sided type: one may choose finitely many source primes with the same prescribed current neighborhood and then forbid every future support marker that would alter those protected witnesses. Repeating this for increasing \(m\) can force unbounded twin rank on designated coding sizes, subject to compatibility with the simultaneous support construction.

Therefore the positive half of Theorem 4.1 is compatible with the existing Chebotarev machinery.

---

## 6. The negative side is now only a bounded-collision problem

For \(n\notin K\), Theorem 4.1 does **not** require singleton fibers. It asks only for

\[
\boxed{
\exists B_n<\infty
\quad
\forall F\subseteq S,\ |F|=n:
\mu(F)\le B_n.
}
\tag{14}
\]

This is strictly weaker than the previous cap

\[
\mu(F)\le1.
\tag{15}
\]

and far weaker than exact \(\mu(F)=1\).

The arithmetic problem has therefore sharpened from exact finite multiplicity control to **uniform boundedness of collision classes at selected neighborhood sizes**.

---

## 7. Collision spectrum: the fixed-threshold special case

The weakest nontrivial one-sentence multiplicity threshold is duplication.

Define

\[
C_\mu
:=
\{n:M_\mu(n)\ge2\}.
\tag{16}
\]

Then

\[
\Theta_{n,2}
\]

decides membership in \(C_\mu\).

### Corollary 7.1 — Collision-Spectrum Criterion

If \(C_\mu\) is nonrecursive, then

\[
\operatorname{Th}(\mathfrak M_\mu)
\]

is undecidable.

### Proof

The computable map

\[
n\mapsto\Theta_{n,2}
\]

is a many-one reduction from \(C_\mu\) to the complete theory. ∎

This requires only:

- for positive \(n\): at least one duplicated size-\(n\) neighborhood;
- for negative \(n\): every size-\(n\) neighborhood has multiplicity at most one.

It is simpler logically than Theorem 4.1 but arithmetically stronger on the negative side because it fixes the cap at one.

---

## 8. Parity does not lower the barrier

A tempting alternative is to encode information by the parity of a finite multiplicity.

### Proposition 8.1 — No uniform FO parity test for unbounded fibers

There is no first-order formula which, uniformly over all multiplicity models and all external fibers of finite size, holds exactly when the fiber cardinality is even.

### Proof

Let \(q\) be the quantifier rank of a proposed formula. Choose consecutive integers

\[
N,N+1>q+1
\]

of opposite parity. Construct two models identical except that one distinguished fiber has size \(N\) in the first model and \(N+1\) in the second. Point at one representative.

The same \(q\)-round back-and-forth argument as in Proposition 3.1 shows the pointed structures are \(q\)-equivalent, because both fibers contain more unused representatives than Spoiler can exhaust. Hence no formula of rank \(q\) distinguishes the two parities. ∎

### Remark 8.2

If a particular fiber multiplicity is already known to be finite, a theory oracle can recover its exact value by querying all finite thresholds until the first failure, and then compute its parity. But this uses finiteness as prior upper control; parity therefore does not weaken the arithmetic barrier.

---

## 9. A unique twin class is stronger, not weaker

For fixed \(n\), the statement

> there exists exactly one twin-equivalence class of degree \(n\) having at least two representatives

is first-order expressible.

However to make it true one must both:

1. create one duplicated degree-\(n\) class;
2. forbid duplication in every other degree-\(n\) class.

Thus this target contains essentially the full cap-one exclusion problem on all competing classes. It is arithmetically stronger than merely requiring finite twin rank in Theorem 4.1 and offers no simplification.

---

## 10. Arithmetic translation via valuation vectors

Return to the actual Ramanujan threshold family. For every source prime \(p\), write

\[
N_p=\tau(p)^2-p^{11}\ne0.
\tag{17}
\]

For each rational prime \(r\), set

\[
a_r(p):=v_r(N_p)\in\mathbb N_0.
\tag{18}
\]

A threshold profile selects, for each active marker \(r\in S_\kappa\), one positive integer

\[
k_r:=\kappa(r).
\tag{19}
\]

For an external source prime \(p\),

\[
r\in N_\kappa(p)
\iff
a_r(p)\ge k_r.
\tag{20}
\]

### Definition 10.1 — Pair-separation coordinates

For distinct source primes \(p,q\), define

\[
\Sigma(p,q)
:=
\left\{
(r,k):
\min(a_r(p),a_r(q))<k\le\max(a_r(p),a_r(q))
\right\}.
\tag{21}
\]

A coordinate \((r,k)\in\Sigma(p,q)\) separates \(p\) and \(q\), because exactly one of

\[
a_r(p)\ge k,
\qquad
a_r(q)\ge k
\]

holds.

The profile itself determines the selected coordinate set

\[
T_\kappa
:=
\{(r,\kappa(r)):r\in S_\kappa\}.
\tag{22}
\]

### Theorem 10.2 — Exact Threshold-Separator Criterion

Let \(p,q\notin S_\kappa\). Then

\[
\boxed{
N_\kappa(p)=N_\kappa(q)
\iff
T_\kappa\cap\Sigma(p,q)=\varnothing.
}
\tag{23}
\]

Equivalently,

\[
N_\kappa(p)\ne N_\kappa(q)
\iff
T_\kappa\cap\Sigma(p,q)\ne\varnothing.
\tag{24}
\]

### Proof

By (20), the two neighborhoods differ exactly when there exists an active marker \(r\) for which the two threshold inequalities

\[
a_r(p)\ge\kappa(r),
\qquad
a_r(q)\ge\kappa(r)
\]

have different truth values. This is precisely the condition

\[
(r,\kappa(r))\in\Sigma(p,q).
\]

Taking the existence or nonexistence of such a marker gives (23)-(24). ∎

This converts collision control into a hitting problem for the hyperedges \(\Sigma(p,q)\).

---

## 11. Empty-skeleton constraint on the same coordinates

The selected threshold coordinates cannot be arbitrary. If \(r,s\in S_\kappa\) are distinct active markers and the active skeleton is empty, then both active-active incidences must fail:

\[
a_s(r)<k_s,
\qquad
a_r(s)<k_r.
\tag{25}
\]

Hence the selected set \(T_\kappa\) must satisfy

\[
\boxed{
\forall r\ne s\in S_\kappa:
\quad
v_s(N_r)<\kappa(s).
}
\tag{26}
\]

and symmetrically with \(r,s\) exchanged.

Therefore the arithmetic upper-control problem is not an unconstrained hitting-set problem. It is a **constrained threshold transversal**:

- hit enough pair-separation sets \(\Sigma(p,q)\) to keep unwanted twin classes bounded;
- simultaneously choose the marker thresholds so that all selected markers remain mutually nonadjacent.

This is the precise form of the remaining arithmetic barrier.

---

## 12. Unavoidable valuation twins

### Proposition 12.1 — Absolute-residual obstruction

For distinct external primes \(p,q\),

\[
\Sigma(p,q)=\varnothing
\iff
|N_p|=|N_q|.
\tag{27}
\]

Consequently, if

\[
|N_p|=|N_q|
\tag{28}
\]

and both \(p,q\) remain external, then they are twins for **every** threshold profile:

\[
N_\kappa(p)=N_\kappa(q).
\tag{29}
\]

### Proof

The set \(\Sigma(p,q)\) is empty exactly when

\[
v_r(N_p)=v_r(N_q)
\]

for every rational prime \(r\). By unique factorization this is equivalent to equality of the absolute values of the two nonzero integers \(N_p,N_q\). The second statement then follows from Theorem 10.2. ∎

### Claim boundary

No assertion is made here about whether distinct primes with

\[
|\tau(p)^2-p^{11}|=|\tau(q)^2-q^{11}|
\]

actually exist, or about a uniform bound on the sizes of such equality classes. Those are separate arithmetic questions.

---

## 13. The new arithmetic target

The exact \(1/2\)-multiplicity target from the sixth strike is no longer necessary.

Fix a c.e. nonrecursive set \(K\). It is enough to build an empty-skeleton threshold profile satisfying

\[
\boxed{
M_\kappa(n)=\infty
\quad(n\in K)
}
\tag{30}
\]

and

\[
\boxed{
M_\kappa(n)<\infty
\quad(n\notin K).
}
\tag{31}
\]

The positive requirements (30) are lower-control requirements and fit the existing Chebotarev witness-protection machinery.

The negative requirements (31) ask only for finite bounded collision rank at each noncoding size. Through Theorem 10.2 they become a constrained threshold-transversal problem, much weaker than prescribing exact multiplicities.

We therefore replace the previous barrier

\[
\text{Upper Multiplicity Control Barrier}
\]

by the more precise

\[
\boxed{
\textbf{Bounded Twin-Rank / Threshold-Transversal Barrier}.
}
\tag{32}
\]

---

## 14. What this strike settles

The proposed weakenings have now been separated cleanly.

### Finite versus infinite multiplicity

Literal infinitude of one twin class is not uniformly first-order definable. The robust FO-visible replacement is **bounded versus unbounded multiplicity over all degree-\(n\) fibers**.

### Parity

Uniform parity of arbitrarily large finite fibers is not first-order definable. If exact finite multiplicity is recoverable, parity adds no weakening.

### Unique twin class

It is first-order expressible but demands stronger global exclusion than bounded twin rank.

### Best current asymmetric target

\[
\boxed{
M_\kappa(n)=\infty
\text{ versus }
M_\kappa(n)<\infty.
}
\]

This is sufficient for undecidability through a Turing reduction from any fixed c.e. nonrecursive set and requires no prescribed finite cap.

---

## 15. Next strike

The next problem is now completely arithmetic and combinatorial:

> **Constrained Threshold-Transversal Problem.**  
> Can one construct an infinite threshold support \(S\) with empty active skeleton such that the selected coordinates \(T_\kappa\) keep the twin rank bounded on a prescribed collection of neighborhood sizes while allowing unbounded twin rank on another prescribed c.e. collection?

The most useful intermediate questions are:

1. Can one prove a uniform finite bound on unavoidable valuation-twin classes?
2. For any finite family of external source pairs \((p_i,q_i)\) with \(|N_{p_i}|\ne|N_{q_i}|\), can one choose a new marker/threshold coordinate separating all or a controlled fraction of them while preserving active independence?
3. Is there a sparse independent support whose threshold coordinates form a transversal for every pair-separation hyperedge outside finitely bounded exceptional classes?
4. Can higher threshold depth \(k>1\) bypass the lack of fresh prime divisors by separating sources through unequal valuations at already available primes?

A positive answer to a sufficiently uniform version of Questions 2–3 would cross the remaining barrier and produce an actual Ramanujan empty-skeleton profile with undecidable prime-only theory.

---

## 16. Hostile audit

1. **Was “infinite fiber” incorrectly treated as a first-order property?**  
   No. Proposition 3.1 explicitly proves that it is not uniformly FO-definable.

2. **Does Theorem 4.1 require a known bound on the finite side?**  
   No. The bound \(B_n\) may be arbitrary and noncomputable. The theory oracle search simply waits for the first false threshold sentence.

3. **Why does the Turing reduction halt on the unbounded side?**  
   Because the coding set \(K\) is chosen c.e.; its external enumeration eventually certifies membership.

4. **Could unbounded finite fibers masquerade as an infinite fiber?**  
   Yes, and the theorem intentionally treats both as \(M_\mu(n)=\infty\). This is why twin rank, not literal fiber infinitude, is the correct invariant.

5. **Does parity provide a hidden one-formula shortcut?**  
   No; Proposition 8.1 rules out uniform FO parity detection on unbounded finite fibers.

6. **Is the unique-twin-class proposal weaker than cap-one collision control?**  
   No. To ensure uniqueness one must suppress every competing duplicated class.

7. **Is the separator criterion merely sufficient?**  
   No. Theorem 10.2 is an exact equivalence for external source pairs.

8. **Was empty active skeleton incorporated into the separator problem?**  
   Yes. Equation (26) gives the simultaneous mutual-nonincidence constraint on selected markers.

9. **Were equal absolute residuals silently assumed absent?**  
   No. Proposition 12.1 isolates them as unavoidable twins and makes no unproved claim about whether they occur.

10. **Has the actual Ramanujan undecidable empty-skeleton profile now been constructed?**  
    No. The strike weakens and reformulates the necessary upper control but does not cross the constrained threshold-transversal barrier.

**Audit verdict:** all stated abstract and reduction results are proved. The arithmetic realization problem remains open and is stated as such.
