# SOL-QFIELD — Native Associator Diamonds and the History-Layer Obstruction

**Version:** 0.3  
**Date:** 2026-08-31  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** THIRD TARGET COMPLETE / BASE-ONLY NATIVE DIAMONDS PROVED / TYPED DIAMONDS ABSENT / HISTORY LAYER REQUIRED  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264  
**Depends on:** `SOL_QFIELD_REPORT_v0_1.md`, `SOL_QFIELD_AMPLITUDE_LIFT_v0_2.md`

---

## 1. Executive verdict

The amplitude audit identified coherent reconvergence as the first place where complex relative phase could become operational. The next question was therefore whether the existing FCOA composition rules already contain a native reconvergence skeleton.

The answer is again mixed, but now substantially more structural.

### Result A — an infinite native family of base-only associator diamonds already exists

On the legacy positive ray, for every \(n\ge2\),

\[
(P_0\oplus P_n)\oplus P_0
=
P_{n-1}
=
P_0\oplus(P_n\oplus P_0).
\tag{1}
\]

The two parenthesizations pass through distinct intermediate base states:

\[
P_0\oplus P_n=P_n,
\qquad
P_n\oplus P_0=P_{n-1},
\qquad
P_n\ne P_{n-1}.
\tag{2}
\]

Thus the old operation already contains a genuine **evaluation diamond**: two distinct two-step evaluation histories reconverge to one value.

Reflection produces the same family on the negative branch.

### Result B — current terminal outputs cannot participate in such a diamond

The audited \(E\)-families are terminal: there is no general legacy rule admitting an \(E\)-value as the next operation input. Therefore if the first step of a parenthesized composition lands in

\[
E^+\cup E^*\cup E^\times,
\tag{3}
\]

the corresponding second step is not a legacy FCOA composition.

Hence the current structure has

\[
\boxed{\text{BASE-ONLY DIAMONDS, but no TYPED RE-ENTRY DIAMONDS}.}
\tag{4}
\]

### Result C — associator equality is not coherent superposition

The two sides of (1) are two **evaluation histories of one term triple**. In the extensional FCOA algebra they are not retained as two independent physical/process states after evaluation: both are simply equal to \(P_{n-1}\).

Therefore assigning a relative phase to the two histories cannot be done on the carrier values alone.

### Result D — interference from native diamonds forces a history/morphism lift

If amplitudes are to distinguish the two routes in (1), the routes themselves must survive as distinct mathematical objects before reconvergence. One must replace the purely extensional value semantics

\[
\text{term}\longmapsto\text{value}
\tag{5}
\]

by a process/history semantics containing distinct morphisms or paths

\[
\pi_L,\pi_R:s\rightrightarrows t.
\tag{6}
\]

Only then can one even write

\[
A(\pi_L)+A(\pi_R).
\tag{7}
\]

This gives a new obstruction:

\[
\boxed{
\text{carrier algebra + associator equality}
\not\Rightarrow
\text{interference};
\quad
\text{history retention is additionally necessary}.
}
\tag{8}
\]

### Programme verdict

The third strike selects the second outcome proposed in v0.2:

\[
\boxed{\texttt{BASE-ONLY DIAMONDS}.}
\tag{9}
\]

The discovery does **not** upgrade SOL-QFIELD beyond `ANALOGY ONLY`, but it produces the first native FCOA object that can serve as a reconvergence skeleton without inventing a new coordinate.

The next sharp problem is now no longer geometric. It is categorical/process-theoretic:

\[
\boxed{
\text{Can the native evaluation diamonds be lifted canonically to a path/morphism category}
}
\tag{10}
\]

without destroying legacy exactness or introducing arbitrary extra memory?

---

## 2. Source rules

On the positive legacy ray the audited operation \(\oplus\) satisfies

\[
P_0\oplus P_n=P_n
\qquad(n\ge1),
\tag{11}
\]

and

\[
P_n\oplus P_0=P_{n-1}
\qquad(n\ge1).
\tag{12}
\]

In the signed completion write

\[
x_k=T^k x_0,
\qquad k\in\mathbb Z,
\tag{13}
\]

with

\[
x_0\oplus x_k=x_k
\qquad(k\ne0),
\tag{14}
\]

and

\[
x_k\oplus x_0=\rho(x_k),
\qquad
\rho(x_k)=x_{k-\operatorname{sgn}(k)}.
\tag{15}
\]

The prior `CLASSICAL_SHADOWS_AND_ASSOCIATIVE_COLLAPSE_0_1.md` used these rules to prove that imposing global associativity in an external semigroup collapses all base coordinates. The present note does **not** alter that theorem. It extracts a different, local consequence of the same rules: selected triples already have association status `EQ` inside the partial algebra.

---

## 3. Native positive-ray diamond

### Theorem 3.1 — Radial Associator Diamond

For every \(n\ge2\), both parenthesizations of the triple

\[
(P_0,P_n,P_0)
\tag{16}
\]

are defined and satisfy

\[
\boxed{
(P_0\oplus P_n)\oplus P_0
=
P_0\oplus(P_n\oplus P_0)
=
P_{n-1}.
}
\tag{17}
\]

Moreover, the first-step intermediate values are distinct:

\[
P_0\oplus P_n=P_n,
\qquad
P_n\oplus P_0=P_{n-1},
\qquad
P_n\ne P_{n-1}.
\tag{18}
\]

Hence (17) is a nondegenerate base-valued evaluation diamond.

### Proof

Using (11) and then (12),

\[
\begin{aligned}
(P_0\oplus P_n)\oplus P_0
&=P_n\oplus P_0\\
&=P_{n-1}.
\end{aligned}
\tag{19}
\]

Using (12) and then (11), with \(n-1\ge1\),

\[
\begin{aligned}
P_0\oplus(P_n\oplus P_0)
&=P_0\oplus P_{n-1}\\
&=P_{n-1}.
\end{aligned}
\tag{20}
\]

Thus the two parenthesizations are both defined and equal.

Their intermediate values are \(P_n\) and \(P_{n-1}\), respectively. Since the legacy carrier points are distinct and \(n\ge2\),

\[
P_n\ne P_{n-1}.
\tag{21}
\]

Therefore the two-step evaluation histories are genuinely distinct before reconverging. \(\square\)

### Corollary 3.2 — Association status

For every \(n\ge2\),

\[
\mathcal A_\oplus(P_0,P_n,P_0)=EQ.
\tag{22}
\]

Thus global nonassociativity is compatible with an infinite local family of associative triples.

### Corollary 3.3 — No new operation was introduced

The diamond uses only legacy cells (11)-(12). It is therefore native to the old positive-ray FCOA and is not a hand-written mixed-sector extension.

---

## 4. Reflected diamond family

The signed completion transfers (11)-(12) by reflection.

### Theorem 4.1 — Signed Radial Diamond Family

For every \(k\in\mathbb Z\) with \(|k|\ge2\),

\[
\boxed{
(x_0\oplus x_k)\oplus x_0
=
x_0\oplus(x_k\oplus x_0)
=
\rho(x_k).
}
\tag{23}
\]

The two intermediate states are

\[
x_k
\qquad\text{and}\qquad
\rho(x_k),
\tag{24}
\]

which are distinct.

### Proof

From (14),

\[
(x_0\oplus x_k)\oplus x_0
=x_k\oplus x_0
=\rho(x_k).
\tag{25}
\]

From (15), and because \(|k|\ge2\) implies \(\rho(x_k)\ne x_0\),

\[
\begin{aligned}
x_0\oplus(x_k\oplus x_0)
&=x_0\oplus\rho(x_k)\\
&=\rho(x_k).
\end{aligned}
\tag{26}
\]

Since radial contraction changes the signed coordinate by one step toward zero,

\[
\rho(x_k)\ne x_k.
\tag{27}
\]

Hence the intermediates are distinct. \(\square\)

### Reflection covariance

Because

\[
\nu(x_k)=x_{-k}
\tag{28}
\]

and

\[
\nu\rho=\rho\nu,
\tag{29}
\]

the positive and negative diamonds occur in reflected pairs. No independent negative-side choice is involved.

---

## 5. Why this does not contradict associative collapse

At first sight Theorem 3.1 may seem to conflict with the earlier result that global associativization collapses the carrier. There is no conflict.

The native theorem says only that the specific family

\[
(P_0,P_n,P_0)
\tag{30}
\]

has equal left and right evaluations.

The collapse theorem concerns a **total associative target semigroup** in which associativity must hold for every relevant triple after embedding the old defined cells. The global law propagates the radial relations until all coordinates are identified.

Thus

\[
\boxed{
\text{local associator diamonds can exist while global associative saturation is impossible injectively}.
}
\tag{31}
\]

This distinction is important for the entire Interaction-Induced Laws programme.

---

## 6. Typed re-entry diamond no-go in the current structure

### Definition 6.1 — Typed first-step diamond

A parenthesized two-step evaluation is **typed-first-step** if its inner operation returns a terminal output

\[
e\in E^+\cup E^*\cup E^\times.
\tag{32}
\]

It is a **typed re-entry path** if the outer operation is then defined with \(e\) as one of its arguments.

### Theorem 6.2 — Legacy Typed-Diamond No-Go

In the currently audited FCOA-Z structure, no typed-first-step two-step evaluation can be a legacy typed re-entry path.

Consequently there is no native legacy associator diamond in which an \(E\)-output is an intermediate state.

### Proof

By the audited typing of the present FCOA-Z, the families

\[
E^+,E^*,E^\times
\tag{33}
\]

are terminal outputs: there is no general legacy operation rule that accepts such an \(E\)-value as a later argument of \(\oplus\), \(\otimes\), or the relevant old base operations.

Therefore once an inner evaluation returns \(e\in E\), the required outer legacy operation is undefined. Hence the path stops and cannot form a two-step legacy evaluation, much less reconverge with another parenthesization. \(\square\)

### Corollary 6.3

The native-diamond classification requested in v0.2 is

\[
\boxed{
\texttt{BASE-ONLY DIAMONDS: YES},
\qquad
\texttt{TYPED RE-ENTRY DIAMONDS: NO in the current legacy structure}.
}
\tag{34}
\]

The latter could change only after a genuine LC2 extension.

---

## 7. Evaluation diamonds are not yet process diamonds

The phrase “two paths” must now be disciplined carefully.

For a triple \((x,y,z)\), the syntax contains two parenthesized terms

\[
t_L=((x\oplus y)\oplus z),
\qquad
t_R=(x\oplus(y\oplus z)).
\tag{35}
\]

When both are defined, ordinary extensional evaluation gives values

\[
\operatorname{ev}(t_L),
\qquad
\operatorname{ev}(t_R)
\tag{36}
\]

in the carrier/output sorts.

For the radial diamond,

\[
\operatorname{ev}(t_L)=\operatorname{ev}(t_R)=\rho(x_k).
\tag{37}
\]

The carrier algebra remembers the common value. It does not automatically retain the derivation trees \(t_L,t_R\) as two independently evolving states.

Thus the diagram

\[
\begin{array}{ccc}
& (x_0,x_k,x_0) &\\
/ && \\\
 x_k && \rho(x_k)\\
\\ && /\\
& \rho(x_k) &
\end{array}
\tag{38}
\]

is first of all an **evaluation/rewrite diamond**, not yet a quantum transition diagram.

This distinction is the central new obstruction of the third strike.

---

## 8. Theorem C — Extensionality/History Obstruction

### Definition 8.1 — Extensional amplitude semantics

An amplitude assignment is **carrier-extensional** if the amplitude of a completed computation depends only on its represented input data and final FCOA value, not on the internal evaluation history.

Thus whenever two histories \(\pi_1,\pi_2\) have the same source data \(s\) and same final value \(t\),

\[
A(\pi_1)=A(\pi_2)=A(s,t)
\tag{39}
\]

or, more strongly, the histories are not separately present as arguments of \(A\) at all.

### Theorem 8.2 — Extensionality/Interference No-Go

A carrier-extensional amplitude semantics cannot extract a nontrivial relative phase from the two branches of a native associator diamond.

To obtain a coherent expression with independently variable route amplitudes

\[
A_L+A_R,
\tag{40}
\]

the two evaluation histories must be retained as distinct mathematical objects prior to summation.

### Proof

In an extensional semantics, histories with the same represented source and endpoint are identified at the level on which amplitudes are evaluated. For the radial diamond,

\[
\pi_L:s\to t,
\qquad
\pi_R:s\to t,
\qquad
 t=\rho(x_k).
\tag{41}
\]

If only \((s,t)\) is retained, there is a single amplitude datum

\[
A(s,t).
\tag{42}
\]

There are not two independent arguments to which two independently phased complex numbers can be assigned. Consequently no relative phase

\[
\arg A_L-\arg A_R
\tag{43}
\]

is defined internally.

To form (40), one must first distinguish \(\pi_L\) and \(\pi_R\), assign amplitudes to them separately, and only afterward apply a coherent combination rule. Hence history retention is necessary. \(\square\)

### Corollary 8.3 — Value equality destroys path phase unless history is promoted

Associator equality

\[
t_L=t_R
\tag{44}
\]

is not itself a source of interference. In an extensional algebra it tends in the opposite direction: it identifies the final value and forgets how that value was obtained.

### Corollary 8.4 — Required new layer

Any interference interpretation of FCOA associator diamonds must introduce a structure of the form

\[
\boxed{
\text{objects = FCOA states/typed states},
\qquad
\text{morphisms = retained admissible histories/processes}.
}
\tag{45}
\]

The exact categorical formalism is not yet selected, but a path/morphism distinction is structurally unavoidable if route phases are to be meaningful.

---

## 9. Minimal path lift

The previous theorem identifies what must be added, but not how much.

### Definition 9.1 — Free evaluation-path lift

Let \(\mathcal G\) be the directed graph whose vertices are well-typed FCOA intermediate records and whose edges are single legal applications of an old operation rule.

Form the free path category

\[
\mathsf{Path}(\mathcal G),
\tag{46}
\]

whose morphisms are finite composable paths of legal rule applications.

The radial associator diamond then supplies two distinct morphisms

\[
\pi_L,\pi_R:s_k\to t_k
\tag{47}
\]

with the same source and target.

### Proposition 9.2 — Existence of a history lift

The free path construction preserves all legacy FCOA values as endpoint labels while distinguishing legal evaluation histories. Therefore it provides a mathematical container in which route-dependent amplitudes could be defined without changing any old operation value.

### Proof

Every edge is generated from an already legal operation application, so no old cell is modified. The evaluation functor

\[
E:\mathsf{Path}(\mathcal G)\to\mathsf{Val}
\tag{48}
\]

sends a path to its endpoint value and hence recovers the old extensional semantics after forgetting history. Distinct paths may have the same endpoint, so the lift retains information that the old value algebra forgets. \(\square\)

### Critical limitation

The free path category is far too large to count as a canonical physical model. It remembers every syntactic/evaluation distinction unless quotient relations are imposed.

Therefore existence is easy; **canonical quotient selection** is the hard problem.

---

## 10. Why the free path lift is still underdetermined

Once histories are available, one can assign a complex weight

\[
w(e)\in\mathbb C
\tag{49}
\]

to each generating edge and extend multiplicatively along paths:

\[
A(\pi_2\circ\pi_1)=A(\pi_2)A(\pi_1).
\tag{50}
\]

For parallel histories one could then impose an additive rule

\[
A(\pi_L\boxplus\pi_R)=A(\pi_L)+A(\pi_R).
\tag{51}
\]

But none of (49)-(51) is selected by the old carrier algebra.

In particular, the following choices remain free:

1. which evaluation distinctions count as physically/process-wise distinct;
2. which paths should be quotient-identified;
3. which elementary steps carry nontrivial phase;
4. whether path composition is represented multiplicatively;
5. whether parallel histories add coherently, probabilistically, idempotently, or by another semiring law;
6. what observation functional converts a summed weight into an outcome probability.

Thus

\[
\boxed{
\text{native diamonds solve the topology of reconvergence, not the amplitude selector problem}.
}
\tag{52}
\]

This is the cleanest statement of the current boundary.

---

## 11. A stronger interpretation of the QF ladder

The QF ladder from v0.2 can now be refined.

### QF0 — typed support

Current FCOA output sorts.

### QF1 — stochastic weights

Arbitrary probability weights on output channels.

### QF2 — terminal complex weights

Operationally equivalent to QF1 while outputs remain terminal.

### QF2.5 — native evaluation diamonds

Distinct legal evaluation trees reconverge to one extensional FCOA value.

**New result:** present already in the legacy base operation through Theorem 3.1/4.1.

### QF3a — history/morphism retention

Distinct evaluation paths survive as parallel morphisms.

**Status:** constructible by a free path lift, but not canonically selected.

### QF3b — coherent path algebra

Sequential path amplitudes compose and parallel alternatives add coherently.

**Status:** absent and underdetermined.

### QF4 — Hilbert-like linear normed state dynamics

Absent.

### QF5 — Fock/CAR statistics structure

Absent.

The important refinement is therefore

\[
\boxed{
QF2 < QF2.5 < QF3a < QF3b < QF4 < QF5.
}
\tag{53}
\]

The existing FCOA unexpectedly reaches QF2.5 without an amplitude extension.

---

## 12. Geometry versus memory

The native diamond yields a useful conceptual distinction for the wider FCOA programme.

The signed line already supplies enough geometry for two evaluation histories to reconverge. Therefore the obstruction to interference is **not** lack of a Cartesian second coordinate.

Instead the missing resource is

\[
\boxed{\text{path/history memory}.}
\tag{54}
\]

This is significant because the FCOA programme already treats memory/cost/typed output structure as an independent resource in other branches.

For QFIELD, at least, the next layer is more naturally described as

\[
\text{carrier geometry}
\longrightarrow
\text{history category}
\longrightarrow
\text{weight algebra}
\tag{55}
\]

rather than

\[
\text{line}
\longrightarrow
\text{plane}
\longrightarrow
\text{quantum physics}.
\tag{56}
\]

Equation (56) is not supported by the current results.

---

## 13. Line-completion gate update

### LC1

No change: native diamonds use old cells and do not select new mixed values.

\[
\boxed{\texttt{LC1: UNDERDETERMINED}.}
\tag{57}
\]

### LC2

Typed re-entry remains absent. Theorem 6.2 makes this a precise barrier for terminal \(E\)-channels.

\[
\boxed{\texttt{LC2: OPEN; required for typed-channel diamonds}.}
\tag{58}
\]

### LC3

No QFIELD principle yet selects mixed-sign values.

\[
\boxed{\texttt{LC3: REALIZABLE WILD / UNDERDETERMINED from QFIELD}.}
\tag{59}
\]

### 1D closure

The base-only native diamond is already on the one-dimensional legacy ray and its reflected copy. Therefore

\[
\boxed{\texttt{QF2.5 is strictly 1D-CLOSED}.}
\tag{60}
\]

No dimensional emergence claim is licensed.

---

## 14. Hostile audit

### “The associator diamond proves quantum interference.”

**Rejected.** It proves only two distinct evaluation histories with a common endpoint.

### “Because the two histories have the same result, their amplitudes should add.”

**Rejected.** Equality of extensional values supplies no rule for adding histories.

### “The two parenthesizations are automatically two physical alternatives.”

**Rejected.** They are two syntactic/evaluation orders until a process semantics says otherwise.

### “We can assign different phases to the same FCOA value depending on how it was reached.”

**Only after changing the semantic level.** Such a rule is history-dependent and therefore cannot live purely on extensional carrier values.

### “The free path category solves the problem.”

**Rejected.** It proves existence of a history container but is maximally nonselective; canonical quotient and weight laws remain open.

### “A second coordinate is required for the diamond.”

**Rejected.** The family occurs already on the original positive ray and its reflected signed-line copy.

---

## 15. Publication decision

`HOLD FOR APPLIED-DIRECTIONS SYNTHESIS` remains the correct status.

The third strike is mathematically useful because it does more than repeat a QFT analogy:

1. it identifies an explicit infinite family of native FCOA reconvergence/evaluation diamonds;
2. it proves that terminal typed outputs cannot currently enter such diamonds;
3. it isolates **history retention** as a structural resource distinct from carrier dimension;
4. it proves that extensional value semantics alone cannot support relative phase between reconvergent histories.

However, the path-category lift is currently a generic construction rather than a theorem uniquely forced by FCOA. A standalone publication would overstate the result.

---

## 16. Next strike — canonical history quotient

The next decisive target is

\[
\boxed{
\text{Find the coarsest nontrivial FCOA-internal equivalence on evaluation paths}
}
\tag{61}
\]

that simultaneously:

1. preserves all old extensional operation values;
2. identifies syntactic redundancies that should not count as distinct histories;
3. keeps at least one radial associator pair \(\pi_L\ne\pi_R\) distinct;
4. respects reflection;
5. composes congruentially under legal continuation of paths;
6. does not import ordinary arithmetic or an external time/space coordinate.

Call such a quotient, if it exists, the **minimal FCOA history category**.

There are three possible outcomes:

### H0 — total history collapse

Every congruence satisfying the natural FCOA invariances identifies \(\pi_L\) with \(\pi_R\). Then native diamonds cannot carry intrinsic phase memory.

### H1 — nontrivial finite/local history memory

At least one natural quotient keeps the two radial routes distinct but only in finite fibers over the line. This would give a native QF3a candidate while remaining 1D-closed.

### H2 — unbounded compositional memory

Any nontrivial path distinction propagates under composition into an unbounded independent history coordinate. Only this outcome would begin to resemble a genuine new resource dimension, though still not necessarily a spatial dimension.

This H0/H1/H2 trichotomy is now the sharp research frontier of SOL-QFIELD.

---

## 17. Source provenance

The algebraic rules used in Theorems 3.1 and 4.1 are not newly invented for QFIELD. They are the established legacy/signed rules already recorded in the FCOA-Z article and in `CLASSICAL_SHADOWS_AND_ASSOCIATIVE_COLLAPSE_0_1.md`:

\[
x_0\oplus x_k=x_k,
\qquad
x_k\oplus x_0=\rho(x_k).
\]

The new contribution of this report is their use to identify the explicit reconvergent evaluation family and the subsequent history-layer obstruction.

The standard physical motivation for retaining distinct alternatives until recombination remains quantum interference, but no physical identification is claimed.
