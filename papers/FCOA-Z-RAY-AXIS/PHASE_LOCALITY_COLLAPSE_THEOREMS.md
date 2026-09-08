# FCOA-Z — Phase Locality: Collapse and Non-Collapse Theorems

Status: theorem package v0.1  
Date: 2026-08-31

This note continues `MIXED_FINITE_STATE_TRANSPORT.md`.

The active question was:

\[
\boxed{\text{which intrinsic local conditions force the hidden phase clock to collapse from }M_\infty\text{ toward }M_{FS},M_1,M_0?}
\]

The answer splits sharply according to whether a local rule is merely **admissibility-like** or actually **deterministic**.

---

## 1. Phase-clock reduction

Inside the reflection-phase family, a mixed FCOA-Z extension is encoded by

\[
\varepsilon:\mathbb N_0\to\mathbb Z_2,\qquad \varepsilon(0)=0,
\]

through

\[
F_\varepsilon(z)=\nu^{\varepsilon(k(z))}\beta(N(z)).
\]

Thus every structural restriction on this family can be studied as a restriction on the one-sided binary phase word

\[
\varepsilon(0)\varepsilon(1)\varepsilon(2)\cdots.
\]

The purpose of this note is to identify which local restrictions force this word to be ultimately periodic and which do not.

---

## 2. Finite forbidden patterns do not imply finite-state collapse

### Definition 2.1 — finite-type phase admissibility

Fix a finite set \(\mathcal F\) of forbidden finite binary words. A phase clock is admissible if no member of \(\mathcal F\) occurs as a consecutive block in \(\varepsilon\).

This is a bounded-radius local condition.

### Theorem 2.2 — Local-Admissibility Non-Collapse

There exist finite forbidden-pattern systems that admit continuum many distinct phase clocks, including continuum many non-ultimately-periodic clocks.

Consequently a bounded-radius local admissibility principle does **not**, by itself, imply collapse

\[
M_\infty\to M_{FS}.
\]

#### Proof

Take the single forbidden word

\[
11.
\]

For every arbitrary binary sequence

\[
a=(a_0,a_1,a_2,\ldots)\in\{0,1\}^{\mathbb N},
\]

define

\[
\varepsilon_a=0\,a_0\,0\,a_1\,0\,a_2\,0\,a_3\cdots.
\]

No two `1` symbols are adjacent, so every \(\varepsilon_a\) satisfies the local rule forbidding `11`. The map

\[
a\mapsto\varepsilon_a
\]

is injective. Hence there are \(2^{\aleph_0}\) admissible phase clocks.

Only countably many binary sequences are ultimately periodic: each is specified by a finite preperiod, a finite period, and two finite binary words. Therefore, after deleting that countable subset from the continuum-sized admissible family, continuum many admissible clocks remain non-ultimately-periodic. □

### Corollary 2.3

There exist continuum many reflection-equivariant FCOA-Z mixed operations obeying one fixed finite-radius local phase constraint while lying outside the finite-state phase-clock class.

Thus `local` and `finite-state` are distinct notions in this programme.

---

## 3. Fibonacci growth witness

For the rule forbidding `11`, let \(A_n\) be the number of allowed binary words of length \(n\).

### Proposition 3.1

\[
A_n=F_{n+2},
\]

where \(F_n\) is the Fibonacci sequence with \(F_1=F_2=1\).

#### Proof

An admissible length-\(n\) word either ends in `0`, in which case its first \(n-1\) symbols are arbitrary admissible words, or ends in `10`, in which case its first \(n-2\) symbols are arbitrary admissible words. Therefore

\[
A_n=A_{n-1}+A_{n-2},
\]

with \(A_1=2\), \(A_2=3\). Hence \(A_n=F_{n+2}\). □

The exponential number of allowed prefixes is a concrete witness that a very small local rule can retain large phase freedom.

---

## 4. Finite-type phase rules as finite directed graphs

Any forbidden-pattern rule of maximal window length \(r+1\) can be represented by a finite directed graph \(G\):

- vertices are admissible length-\(r\) blocks;
- an edge
  \[
  u_1\cdots u_r\to u_2\cdots u_r b
  \]
  exists exactly when the resulting length-\(r+1\) block is allowed.

An infinite admissible phase clock corresponds to an infinite directed path in this graph.

### Theorem 4.1 — Finite-Type Periodicity Criterion

Every infinite phase clock allowed by a finite-type rule is ultimately periodic **iff** every strongly connected component reachable by an infinite path is a directed simple cycle after transient vertices are removed.

Equivalently, every recurrent phase state has exactly one recurrent successor.

#### Proof

If every recurrent strongly connected component is a simple directed cycle, any infinite path in the finite graph eventually leaves the transient part and enters one such component. Once inside, the continuation is forced around the cycle forever, so the phase word is ultimately periodic.

Conversely, suppose a reachable recurrent strongly connected component is not a simple directed cycle. Then within that component there is a recurrent branching choice: some recurrent state admits two distinct finite return routes that can be concatenated indefinitely. Choosing between these return routes according to an arbitrary infinite binary control sequence gives infinitely many paths; choosing a non-ultimately-periodic control sequence gives a non-ultimately-periodic phase path. Hence not every allowed phase clock is ultimately periodic. □

### Interpretation

A finite local constraint forces finite-state collapse only when its recurrent graph has **no persistent branching**.

So the obstruction to collapse is not locality itself. It is recurrent choice.

---

## 5. Deterministic bounded-window rules always collapse to finite state

### Definition 5.1 — deterministic radius-\(r\) phase law

Fix

\[
f:\{0,1\}^r\to\{0,1\}.
\]

A phase clock obeys the deterministic local recurrence

\[
\boxed{
\varepsilon(k+r)=f\bigl(\varepsilon(k),\ldots,\varepsilon(k+r-1)\bigr)
}
\]

for all sufficiently large \(k\) (or for all \(k\ge0\), in the global version).

### Theorem 5.2 — Deterministic Locality Collapse

Every phase clock satisfying a deterministic radius-\(r\) recurrence is ultimately periodic.

More precisely, its phase evolution is generated by a deterministic finite-state machine with at most

\[
2^r
\]
window states.

#### Proof

Define the state at time \(k\) to be the length-\(r\) window

\[
s_k=(\varepsilon(k),\ldots,\varepsilon(k+r-1)).
\]

The recurrence determines the next state uniquely:

\[
s_{k+1}=(\varepsilon(k+1),\ldots,\varepsilon(k+r-1),f(s_k)).
\]

Thus the sequence of states follows a deterministic map on a set of at most \(2^r\) states. Every orbit of a deterministic map on a finite set has a finite transient tail followed by a cycle. Therefore \(\varepsilon\) is ultimately periodic. □

### Corollary 5.3

Any deterministic bounded-window identity imposed on the hidden FCOA-Z phase collapses

\[
M_\infty\to M_{FS}.
\]

This gives a sufficient intrinsic route to the finite-state corridor.

---

## 6. One-step deterministic laws recover the first hierarchy levels

For \(r=1\), there are only four Boolean update maps

\[
f:\{0,1\}\to\{0,1\}.
\]

Boundary preservation fixes \(\varepsilon(0)=0\).

### Proposition 6.1 — Radius-One Classification

The four deterministic one-step recurrences give:

1. `f(0)=0, f(1)=0`: the zero phase \(0000\cdots\), hence the canonical extension;
2. `f(0)=0, f(1)=1`: starting from zero, again the zero phase;
3. `f(0)=1, f(1)=0`: the parity phase \(010101\cdots\);
4. `f(0)=1, f(1)=1`: the phase \(01111\cdots\), an eventually constant non-homogeneous transport law.

Thus exact covariance and parity are not the only radius-one deterministic clocks, but parity is the unique nontrivial **reversible** radius-one clock.

#### Proof

Immediate iteration from the initial phase \(0\). A one-bit update is reversible iff \(f\) is a permutation of \(\{0,1\}\). The two permutations are identity and toggle. Identity keeps the zero phase; toggle produces parity. □

### Corollary 6.2 — Reversible One-Bit Dichotomy

If the phase memory update is required to be reversible, the one-bit finite-state possibilities reduce exactly to

\[
\boxed{
\text{zero phase}\quad\text{or}\quad\text{parity phase}.
}
\]

This recovers the homogeneous geometric transport dichotomy from a purely memory-theoretic viewpoint.

---

## 7. Exact r-step covariance forces periodic phase

A particularly natural family of identities can be stated directly at operation level.

Suppose that whenever \(r\) simultaneous inward contractions are possible,

\[
\boxed{
F(z)=F(C^r z).
}
\]

Inside the phase-clock family this says

\[
\varepsilon(k)=\varepsilon(k-r)
\]

for every sufficiently large cancellation depth \(k\).

### Theorem 7.1 — r-Step Covariance Collapse

Exact \(r\)-step inward covariance forces the phase clock to be eventually periodic with period dividing \(r\).

If the covariance holds all the way from the first admissible depth, the phase is periodic from the start (subject to the fixed boundary phase at depth zero).

#### Proof

The operation-level covariance compares cells having the same normal-form boundary but cancellation depths differing by \(r\). Since the boundary output is non-root on suitable representatives, equality of the operation values implies equality of their reflection phases:

\[
\varepsilon(k)=\varepsilon(k-r).
\]

Iteration gives period dividing \(r\) beyond the threshold where covariance is assumed. □

Special cases:

- \(r=1\): exact inward covariance gives the zero phase and the canonical mixed law;
- \(r=2\): two-step covariance allows period dividing two, so the only boundary-compatible purely periodic possibilities are zero or parity.

---

## 8. Twisted one-step covariance forces parity

Suppose instead that one inward step transports the value by reflection:

\[
\boxed{
F(z)=\nu F(Cz)
}
\]

whenever one inward step is possible.

### Theorem 8.1 — Twisted-Covariance Rigidity

With inherited boundary preservation, twisted one-step covariance uniquely forces

\[
\varepsilon(k)=k\bmod2.
\]

Hence the unique solution is the parity extension.

#### Proof

At depth zero the boundary phase is \(\varepsilon(0)=0\). Each inward step introduces exactly one additional reflection. Therefore

\[
\varepsilon(k+1)=\varepsilon(k)+1\pmod2.
\]

Induction gives

\[
\varepsilon(k)=k\pmod2.
\]

The boundary trace then fixes the operation uniquely. □

This identifies parity by a one-line local covariance identity, not by an externally supplied clock.

---

## 9. Collapse ladder

We can now replace the informal hierarchy by a hierarchy of **forcing principles**.

### No collapse

Finite-radius admissibility with recurrent branching can leave continuum many aperiodic phase clocks:

\[
M_\infty\text{ survives.}
\]

### Finite-state collapse

A deterministic bounded-window phase recurrence forces

\[
M_\infty\to M_{FS}.
\]

### Period-r collapse

Exact \(r\)-step inward covariance forces eventual period dividing \(r\).

### One-bit reversible collapse

Reversible radius-one phase evolution gives only identity or toggle:

\[
M_{FS}\to\{M_0,M_1\}.
\]

### Canonical collapse

Exact one-step inward covariance forces

\[
M_1\to M_0.
\]

### Parity selection

Twisted one-step covariance selects the unique nontrivial homogeneous phase:

\[
M_1\to \text{parity}.
\]

---

## 10. Main conceptual result

The first memory threshold is now structurally understood.

The phase hierarchy is not controlled merely by how *local* an axiom is. It is controlled by whether local information leaves **persistent branching**.

The sharp distinction is

\[
\boxed{
\text{local admissibility} \neq \text{local determinism}.
}
\]

A local admissibility law may preserve continuum freedom.

A local deterministic recurrence has a finite state space and therefore forces eventual periodicity.

In FCOA-Z language:

\[
\boxed{
\text{persistent local choice is the first source of unbounded mixed memory.}
}
\]

This is stronger than the previous statement that the first finite-state freedom is one bit. It identifies **why** the hierarchy becomes unbounded.

---

## 11. Current novelty boundary

The following ingredients are classical separately:

- finite directed graph presentations of forbidden-word systems;
- eventual periodicity of deterministic finite-state unary dynamics;
- tail-plus-cycle behavior of finite automata;
- finite-state recurrence representations.

The FCOA-Z-specific content is their placement in the already-derived mixed radial transport problem, giving a collapse/non-collapse theorem for hidden interaction phase and identifying recurrent branching as the precise obstruction to finite-state collapse within this phase-clock model.

No priority claim is made for the automata-theoretic ingredients themselves.

---

## 12. Active frontier

The phase-clock branch is now substantially classified:

1. exact inward covariance -> unique canonical law;
2. twisted homogeneous covariance -> unique parity law;
3. deterministic bounded-window phase law -> finite-state / ultimately periodic law;
4. arbitrary finite-type local admissibility -> may retain continuum aperiodic freedom.

The next strike should therefore leave the scalar \(\mathbb Z_2\) phase model.

The strongest candidate is the second legacy operation \(\otimes\), whose boundary values can leave the base carrier and enter terminal fibers. Its output transport group may be larger than

\[
\operatorname{Aut}(X,x_0,\rho)\cong C_2.
\]

If a terminal fiber admits a non-Abelian or larger finite automorphism group, then the first mixed-memory law may be a genuine group-valued cocycle rather than one reflection bit.

That is the next mathematically distinct frontier.