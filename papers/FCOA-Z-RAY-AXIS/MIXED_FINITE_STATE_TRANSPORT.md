# FCOA-Z — Finite-State Mixed Transport and the First Memory Threshold

Status: theorem package v0.1  
Date: 2026-08-31

This note continues `MIXED_GENERATOR_CLASSIFICATION.md`.

The preceding theorem established a rigid class:

\[
\text{exact inward covariance} + \text{legacy zero-port boundary}
\Longrightarrow
\text{one unique mixed law}.
\]

The present question is what appears first when exact inward covariance is weakened while retaining the same signed carrier, the same radial normal form, the same legacy boundary, and reflection symmetry.

The answer has three layers.

1. The first homogeneous geometric transport is a unique nontrivial \(\mathbb Z_2\)-twist.
2. The first finite-state freedom therefore requires exactly two phase states: one bit.
3. If arbitrary cancellation-depth phase clocks are allowed, rigidity collapses from one law to continuum many laws, all of which are invisible to the mixed commutation status and to the two root-association phase diagrams proved previously.

This is the first explicit memory hierarchy beyond the canonical inward-covariant FCOA-Z extension.

---

## 1. Fixed radial data

Let

\[
X=\{x_k:k\in\mathbb Z\},\qquad x_0\text{ the distinguished root},
\]

with reflection

\[
\nu(x_k)=x_{-k}
\]

and punctured radial contraction

\[
\rho(x_k)=x_{k-\operatorname{sgn}(k)},\qquad k\neq0.
\]

Write

\[
d(x_k)=|k|.
\]

For a mixed pair

\[
z=(x,y)\in M=(X_+\times X_-)\cup(X_-\times X_+),
\]

let

\[
k(z)=\min\{d(x),d(y)\}
\]

be its cancellation depth, and let

\[
N(z)
\]

be the first zero-port boundary normal form obtained by simultaneous inward contraction.

The inherited boundary evaluation is

\[
\beta(x_0,q)=q,
\]

\[
\beta(q,x_0)=\rho(q),
\]

for non-root \(q\), while

\[
\beta(x_0,x_0)=\bot
\]

where \(\bot\) denotes UNDEF.

Extend reflection by

\[
\nu(\bot)=\bot.
\]

The canonical Radial Cancellation Extension is

\[
F_0(z)=\beta(N(z)).
\]

---

## 2. Reflection-phase clocks

### Definition 2.1 — phase-clock extension

Let

\[
\varepsilon:\mathbb N_0\to\mathbb Z_2
\]

be any function satisfying

\[
\varepsilon(0)=0.
\]

Define the mixed operation

\[
\boxed{
F_\varepsilon(z)=\nu^{\varepsilon(k(z))}\bigl(\beta(N(z))\bigr).
}
\]

On the inherited boundary itself, the operation remains exactly \(\beta\); the condition \(\varepsilon(0)=0\) records that no boundary value is changed.

Thus the only new datum is a sign-phase attached to the number of synchronous inward cancellation steps.

No individual mixed cell is assigned independently once \(\varepsilon\) is fixed.

---

## 3. Basic structure theorem

### Theorem 3.1 — Phase-Clock Extension Theorem

For every phase clock \(\varepsilon\):

1. `F_epsilon` has exactly the same mixed defined/undefined domain as the canonical Radial Cancellation Extension;
2. it preserves the entire inherited zero-port boundary;
3. it is reflection-equivariant;
4. its radial depth output is the same as in the canonical extension whenever the output is defined.

#### Proof

The canonical boundary value is either \(\bot\) or a base point. Reflection fixes \(\bot\), so applying \(\nu^{\varepsilon(k)}\) never changes definedness.

Boundary preservation is immediate from \(\varepsilon(0)=0\).

Because simultaneous radial reduction commutes with reflection,

\[
N(\nu x,\nu y)=(\nu\times\nu)N(x,y),
\]

and because the inherited boundary map is reflection-equivariant,

\[
\beta((\nu\times\nu)b)=\nu\beta(b).
\]

Cancellation depth is also reflection-invariant. Hence

\[
F_\varepsilon(\nu x,\nu y)
=\nu^{\varepsilon(k)}\nu\beta(N(x,y))
=\nu F_\varepsilon(x,y).
\]

Finally, reflection preserves radial depth, so the output depth is unchanged. □

---

## 4. The rigidity cliff

### Theorem 4.1 — Continuum Phase Freedom

The map

\[
\varepsilon\longmapsto F_\varepsilon
\]

from phase clocks with \(\varepsilon(0)=0\) to mixed operations is injective.

Consequently there are

\[
\boxed{2^{\aleph_0}}
\]

distinct reflection-equivariant mixed extensions in the unrestricted phase-clock class, all preserving the same legacy boundary and the same mixed domain.

#### Proof

Suppose \(\varepsilon\neq\eta\). Choose \(k\ge1\) with

\[
\varepsilon(k)\neq\eta(k).
\]

Take a mixed pair of cancellation depth exactly \(k\) whose first-boundary output is non-root; for example choose depths \(k\) and \(k+2\), with the deeper argument in the second slot. Then the normal-form boundary output is a depth-two non-root point \(q\).

Therefore

\[
F_\varepsilon(z)=\nu^{\varepsilon(k)}q,
\qquad
F_\eta(z)=\nu^{\eta(k)}q.
\]

Since \(q\neq x_0\), reflection moves it, and the two values differ. Hence the map is injective.

There are continuum many binary sequences with fixed zeroth term, proving the cardinality statement. □

### Interpretation

Exact inward covariance gave one law. Merely allowing an unconstrained reflection phase indexed by cancellation depth gives continuum many.

Thus the passage beyond exact covariance is not a gentle perturbation. It is a **rigidity cliff**.

---

## 5. Mixed commutation is blind to the phase clock

### Theorem 5.1 — Commutation-Status Blindness

Let \(x,y\) be mixed.

- If \(d(x)=d(y)\), then both \(F_\varepsilon(x,y)\) and \(F_\varepsilon(y,x)\) are UNDEF.
- If \(d(x)\neq d(y)\), let \(q\) be the unique non-root survivor after simultaneous cancellation. Then

\[
\boxed{
\{F_\varepsilon(x,y),F_\varepsilon(y,x)\}
=
\{\nu^{\varepsilon(k)}q,\nu^{\varepsilon(k)}\rho(q)\}.
}
\]

In particular the two oriented values are always distinct.

Therefore every phase-clock extension has exactly the same mixed pairwise commutation status as the canonical extension.

#### Proof

Swapping the arguments does not change cancellation depth. For unequal depths the same survivor \(q\) reaches the boundary, but it appears once in the second slot and once in the first slot. The inherited zero ports therefore return respectively \(q\) and \(\rho(q)\). The same reflection power is then applied to both. Since reflection commutes with radial contraction and \(q\neq\rho(q)\), the two outputs remain distinct. Equal depths reduce to root/root and remain UNDEF. □

Thus the mixed commutation spectrum cannot recover the hidden phase clock.

---

## 6. Root-association phase diagrams are also blind

Let \(x,y\) be mixed and put

\[
\delta=d(x)-d(y).
\]

Use the association status

\[
\mathcal A\in\{EQ,NEQ,LEFT,RIGHT,NONE\}.
\]

### Theorem 6.1 — Right-Root Phase-Clock Blindness

For every phase clock \(\varepsilon\),

\[
\boxed{
\mathcal A_{F_\varepsilon}(x,y,x_0)=
\begin{cases}
EQ, & \delta\le -2,\\
LEFT, & \delta=-1,\\
RIGHT, & \delta\in\{0,1\},\\
NEQ, & \delta\ge2.
\end{cases}}
\]

This is exactly the same four-phase law as for the canonical Radial Cancellation Extension.

#### Proof

**Case \(\delta\le-2\).** The second argument survives. Both bracketings reduce to the same contracted survivor and use the same cancellation depth \(d(x)\), hence receive the same reflection phase. Therefore they are equal.

**Case \(\delta=-1\).** The left bracketing reaches a depth-one survivor and then the root; the right bracketing first contracts the second argument, creating an equal-depth mixed collision and hence UNDEF. The phase cannot alter definedness. Thus `LEFT`.

**Case \(\delta=0\).** The left inner mixed product is UNDEF. The right bracketing is defined and reaches the root. Thus `RIGHT`.

**Case \(\delta=1\).** The left inner mixed product is the root, so the subsequent root/root cell is UNDEF. The right bracketing is defined. Thus `RIGHT`.

**Case \(\delta\ge2\).** Both bracketings are defined. Their output radial depths are respectively \(\delta-2\) and \(\delta\). Reflection changes only side, never radial depth. Hence the two values cannot be equal. Thus `NEQ`. □

### Theorem 6.2 — Left-Root Phase-Clock Blindness

For every phase clock \(\varepsilon\),

\[
\boxed{
\mathcal A_{F_\varepsilon}(x_0,x,y)=
\begin{cases}
NONE, & \delta=0,\\
LEFT, & \delta=1,\\
EQ, & \delta\notin\{0,1\}.
\end{cases}}
\]

Again this is identical to the canonical collision law.

#### Proof

Because \(x_0\oplus x=x\), the left bracketing is exactly the mixed product whenever that product is defined.

For \(\delta=0\) the mixed product is UNDEF, so both bracketings are UNDEF.

For \(\delta=1\) the mixed product is the root. The left bracketing is therefore defined with value root, while the right bracketing requires root/root and is UNDEF.

For every other \(\delta\), the mixed product is a non-root point \(z\), and the left-zero port gives

\[
x_0\oplus z=z.
\]

So both bracketings are defined and equal. □

### Corollary 6.3 — coarse local-law incompleteness

The combined data consisting of

- mixed definedness,
- mixed pairwise commutation status,
- the right-root association phase diagram,
- the left-root association phase diagram

do **not** classify mixed FCOA-Z extensions.

Indeed continuum many distinct `F_epsilon` share all of those invariants.

---

## 7. The missing invariant: value phase

### Definition 7.1 — observable transport phase

For a phase-clock extension and a mixed cell whose canonical boundary output is non-root, define

\[
\Pi_F(z)=
\begin{cases}
0,&F(z)=\beta(N(z)),\\
1,&F(z)=\nu\beta(N(z)).
\end{cases}
\]

Then for `F_epsilon`,

\[
\boxed{\Pi_{F_\varepsilon}(z)=\varepsilon(k(z)).}
\]

Thus the hidden cancellation-depth phase is recoverable directly from operation values once the inherited normal-form boundary is fixed.

### Corollary 7.2 — completeness inside the phase-clock class

The value-phase observable is a complete invariant of the phase-clock family:

\[
F_\varepsilon=F_\eta
\Longleftrightarrow
\varepsilon=\eta.
\]

This is the first invariant in the FCOA-Z line that detects the new memory degree of freedom missed by the coarse commutation/association statuses.

---

## 8. Which geometric transports are actually available?

The previous sections allowed an arbitrary phase clock. We now restrict to a much more intrinsic homogeneous transport law.

Let

\[
\operatorname{Aut}(X,x_0,\rho)
\]

be the group of bijections \(h:X\to X\) satisfying

\[
h(x_0)=x_0
\]

and

\[
h\rho=\rho h
\]

on non-root points.

### Theorem 8.1 — Radial Automorphism Dichotomy

\[
\boxed{
\operatorname{Aut}(X,x_0,\rho)=\{\mathrm{id},\nu\}\cong C_2.
}
\]

#### Proof

Radial depth is characterized intrinsically as the least number of contractions needed to reach the root, so every automorphism preserves depth.

At depth one there are exactly two points, \(x_1\) and \(x_{-1}\). Hence an automorphism either fixes both or swaps them.

If it fixes \(x_1\), then the unique point of depth \(n+1\) contracting to \(x_n\) on that ray must also be fixed. Induction fixes the entire positive ray; the negative ray is fixed similarly. Thus the automorphism is the identity.

If it swaps the two depth-one points, the same induction forces every positive depth-\(n\) point to be sent to the negative depth-\(n\) point and conversely. Thus the automorphism is reflection \(\nu\). □

This is a strong restriction: there is only one nontrivial geometric output transport compatible with the rooted radial carrier.

---

## 9. Homogeneous transport covariance

Fix \(\tau\in\operatorname{Aut}(X,x_0,\rho)\), extended by \(\tau(\bot)=\bot\).

A homogeneous transport extension obeys one rule per inward step:

\[
F(z)=\tau\bigl(F(Cz)\bigr),
\]

with the inherited boundary value \(\beta\) at the first zero-port normal form.

### Theorem 9.1 — Transport Trace Formula

For fixed \(\tau\), there exists exactly one such extension, namely

\[
\boxed{
F_\tau(z)=\tau^{k(z)}\beta(N(z)).
}
\]

#### Proof

Repeated transport covariance along the unique inward chain gives

\[
F(z)=\tau F(Cz)=\tau^2F(C^2z)=\cdots=\tau^{k(z)}\beta(N(z)).
\]

This proves uniqueness and existence simultaneously. □

### Corollary 9.2 — Homogeneous Geometric Transport Dichotomy

There are exactly two homogeneous geometric transport extensions:

1. \(\tau=\mathrm{id}\), giving the canonical Radial Cancellation Extension;
2. \(\tau=\nu\), giving

\[
\boxed{
F_{\mathrm{par}}(z)=\nu^{k(z)}\beta(N(z)).
}
\]

The second extension depends only on the parity of cancellation depth.

Thus the **unique first homogeneous geometric freedom is one \(\mathbb Z_2\) phase bit**.

---

## 10. The parity extension is genuinely different

For example, take a mixed pair whose depths are `1` and `3`, with the deeper argument in the second slot. Its boundary survivor has depth two.

The canonical extension returns that survivor, while the parity extension reflects it because exactly one cancellation step occurred.

Hence the two operations differ on infinitely many mixed cells.

They are not related by an automorphism of the inherited rooted zero-port geometry.

### Proposition 10.1 — Legacy-relative nonisomorphism

No automorphism of the inherited rooted zero-port reduct conjugates the canonical mixed extension to the parity extension.

#### Proof

Any automorphism of the inherited zero-port reduct fixes the named root and satisfies

\[
h(\rho x)=h(x\oplus x_0)=h(x)\oplus x_0=\rho(hx).
\]

Therefore Theorem 8.1 forces

\[
h\in\{\mathrm{id},\nu\}.
\]

Take the cell \((x_1,x_{-3})\). The canonical value is \(x_{-2}\), whereas the parity value is \(x_2\).

The identity plainly does not conjugate the two operations. Reflection sends the canonical value to \(x_2\), but the parity value of the reflected input \((x_{-1},x_3)\) is \(x_{-2}\), so reflection also fails. □

Therefore the phase bit is not removable by a global symmetry of the inherited radial structure.

---

## 11. Finite-state phase clocks

The homogeneous parity twist is only the first member of a larger bounded-memory class.

### Definition 11.1 — unary Moore phase clock

A finite-state phase clock is a tuple

\[
\mathcal Q=(Q,q_0,\sigma,o)
\]

where

- \(Q\) is finite;
- \(q_0\in Q\) is the initial state;
- \(\sigma:Q\to Q\) is the transition applied once per synchronous cancellation step;
- \(o:Q\to\mathbb Z_2\) is the phase output;
- \(o(q_0)=0\) so the legacy boundary is unchanged.

It generates

\[
\varepsilon_{\mathcal Q}(k)=o(\sigma^k(q_0)).
\]

The induced mixed operation is \(F_{\varepsilon_{\mathcal Q}}\).

### Theorem 11.2 — Finite-State Phase Classification

A phase sequence is generated by a finite-state unary phase clock iff it is ultimately periodic.

#### Proof

For a finite state set, the unary orbit

\[
q_0,\sigma q_0,\sigma^2q_0,\ldots
\]

must eventually repeat. From the first repetition onward it runs around a finite cycle. Therefore the output sequence \(o(\sigma^kq_0)\) is ultimately periodic.

Conversely, any ultimately periodic binary sequence can be represented by a finite tail feeding into a finite cycle, with the desired phase bit attached to each state. □

This is the standard tail-plus-cycle structure of unary finite automata, here applied to cancellation-depth memory.

### Corollary 11.3 — First Memory Threshold

A one-state phase clock preserving the boundary has

\[
\varepsilon(k)=0
\]

for every \(k\), so it gives only the canonical extension.

A two-state toggle

\[
0\leftrightarrow1
\]

with phase output equal to the state gives

\[
\varepsilon(k)=k\bmod2
\]

and hence the nontrivial parity extension.

Therefore

\[
\boxed{
\text{the first finite-state freedom occurs at two states = one bit.}
}
\]

---

## 12. Arbitrarily high finite memory

For every \(p\ge2\), choose a purely periodic binary phase pattern with least period \(p\). Then a \(p\)-cycle unary clock realizes a phase-clock FCOA-Z extension of period \(p\).

If the binary output pattern itself has least period \(p\), no deterministic unary Moore clock with fewer than \(p\) reachable cycle states can realize that purely periodic sequence.

Thus finite-state mixed memory has no universal finite ceiling:

\[
1,2,3,\ldots
\]

all occur as genuine phase-clock periods.

The canonical extension is the period-one zero phase; parity is the first nontrivial period-two point.

---

## 13. Hierarchy beyond exact inward covariance

The results give the following sharp hierarchy.

### Level M0 — exact inward covariance

\[
F(z)=F(Cz).
\]

Legacy boundary preservation forces one unique mixed extension.

### Level M1 — homogeneous geometric transport

\[
F(z)=\tau F(Cz),
\qquad
\tau\in\operatorname{Aut}(X,x_0,\rho).
\]

There are exactly two possibilities:

\[
\tau=\mathrm{id},\qquad \tau=\nu.
\]

The unique new law is cancellation-depth parity.

### Level MFS — finite-state reflection phase

\[
F(z)=\nu^{\varepsilon(k(z))}\beta(N(z)),
\]

with ultimately periodic \(\varepsilon\).

This gives an unbounded hierarchy of finite memory clocks.

### Level M∞ — arbitrary reflection phase

The phase clock \(\varepsilon\) is unrestricted apart from \(\varepsilon(0)=0\).

There are continuum many distinct extensions.

Hence

\[
\boxed{
\text{rigid normal form}
\to
\text{one-bit geometric phase}
\to
\text{finite-state phase hierarchy}
\to
\text{continuum phase freedom}.
}
\]

---

## 14. Classical boundary of the result

Two ingredients have classical analogues and are not novelty claims by themselves.

1. Deterministic cancellation/normal-form reduction is related to standard rewriting and bicyclic-type cancellation structures.
2. A deterministic finite automaton over one input symbol has a tail followed by a cycle, hence unary finite-state behavior is ultimately periodic. A standard reference is:

G. Pighizzini, J. Shallit, *Unary Language Operations, State Complexity and Jacobsthal's Function*, International Journal of Foundations of Computer Science 13(1) (2002), 145-159, DOI `10.1142/S012905410200100X`.

The FCOA-Z-specific result is the conjunction:

- the cancellation depth is generated by mixed radial reduction on the reversible carrier;
- the boundary evaluator is the inherited asymmetric FCOA zero-port law;
- the rooted radial output geometry has automorphism group exactly \(C_2\);
- the unique nontrivial homogeneous transport is therefore the reflection parity phase;
- arbitrary/finite-state phase clocks produce distinct mixed operations while the previously introduced commutation and root-association status spectra remain blind to them;
- the missing information is captured exactly by the new value-phase observable.

No worldwide priority claim is made without a broader dedicated literature audit.

---

## 15. Current conclusion

The earlier frontier asked:

\[
\text{what is the first extra degree of freedom beyond exact inward covariance?}
\]

It now has a precise answer:

\[
\boxed{
\text{one cancellation-depth }\mathbb Z_2\text{ phase bit.}
}
\]

Moreover, the one-bit phase is not an arbitrary choice among many carrier automorphisms: reflection is the **only** nontrivial rooted-radial automorphism.

The result also exposes a defect in the earlier diagnostic language:

\[
\boxed{
\mathcal C\text{-status and root }\mathcal A\text{-status do not see transport phase.}
}
\]

The FCOA-Z programme therefore needs a second layer of invariants, beginning with \(\Pi_F\).

---

## 16. Next strike

The next sharp question is not to find more periodic examples. Their full finite-state source is already classified.

The next question is:

\[
\boxed{
\text{which intrinsic local identities force the phase clock }\varepsilon\text{ to be regular, periodic, parity, or zero?}
}
\]

Equivalently: determine the weakest algebraic/covariance condition that collapses the hierarchy

\[
M_\infty\to M_{FS}\to M_1\to M_0.
\]

A second, independent strike is to ask whether the second legacy operation \(\otimes\), whose zero-port behavior exits to terminal fibers, has a larger output-transport symmetry group than \(C_2\). If so, the first mixed memory could be genuinely non-binary there.