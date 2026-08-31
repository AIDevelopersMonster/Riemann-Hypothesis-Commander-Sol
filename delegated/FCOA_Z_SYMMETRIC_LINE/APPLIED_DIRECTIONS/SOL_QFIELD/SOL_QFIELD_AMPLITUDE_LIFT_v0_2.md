# SOL-QFIELD — Amplitude Lifts, Terminal Phase Erasure, and the Reconvergence Threshold

**Version:** 0.2  
**Date:** 2026-08-31  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** SECOND TARGET COMPLETE / TERMINAL AMPLITUDE LIFT NO-GO / INTERFERENCE THRESHOLD IDENTIFIED  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264  
**Depends on:** `SOL_QFIELD_REPORT_v0_1.md`

---

## 1. Executive verdict

The first SOL-QFIELD report showed that the current FCOA-Z signed line has a useful **typed channel-support shadow**, but not a QFT model. The next question was whether one could promote the unweighted support to a non-arbitrary complex-amplitude layer

\[
A_\alpha(x,y)\in\mathbb C
\tag{1}
\]

while preserving legacy exactness, reflection, and line closure.

The answer is sharper than expected.

### Result A — normalized complex weights are still wildly underdetermined

If one free input orbit has at least two allowed output channels, then normalization, reflection covariance, and exact recovery of deterministic legacy cells leave an uncountable family of possible amplitude assignments.

Thus

\[
\boxed{
\text{complex amplitudes are not selected by the current FCOA structure.}
}
\tag{2}
\]

### Result B — terminal complex amplitudes collapse operationally to probabilities

If the output channels are terminal and the only available observations distinguish those terminal channels, then independent phase rotations

\[
A_c\mapsto e^{i\theta_c}A_c
\tag{3}
\]

leave every one-step probability invariant.

After quotienting this phase freedom, the amplitude vector contains exactly the probability-simplex data

\[
(p_c)_c,
\qquad
p_c=|A_c|^2,
\qquad
\sum_c p_c=1.
\tag{4}
\]

Therefore a complex decoration on sink outputs adds no operational structure beyond classical stochastic weights.

### Result C — relative phase becomes meaningful only after coherent alternatives can reconverge

For two amplitude-bearing paths

\[
s\to e_1\to t,
\qquad
s\to e_2\to t,
\tag{5}
\]

with path amplitudes \(a_1b_1\) and \(a_2b_2\), a coherent path-sum rule gives

\[
M_t=b_1a_1+b_2a_2
\tag{6}
\]

and hence

\[
|M_t|^2
=
|b_1a_1|^2+|b_2a_2|^2
+2\operatorname{Re}\!\left(b_1a_1\overline{b_2a_2}\right).
\tag{7}
\]

The last term is the first place where relative phase can affect an observable.

Thus the real threshold is not “complex numbers” but

\[
\boxed{
\text{branching}
+
\text{re-entry/reconvergence}
+
\text{coherent path summation}.
}
\tag{8}
\]

### Result D — re-entry is necessary for the present channel architecture but is not sufficient

A deterministic re-entry rule may make two channel labels return to the same FCOA value, but equality of endpoints does not create the sum in (6). Coherent addition of alternative path amplitudes is an additional law.

Therefore

\[
\boxed{
\text{re-entry}\ne\text{interference}.
}
\tag{9}
\]

### Result E — interference still does not force Hilbert/Fock QFT

Complex weighted graphs and weighted automata can already support sums of complex path weights and cancellation. Consequently, even an FCOA amplitude network with interference would not by itself be quantum mechanics.

A Hilbert-like layer begins only after one adds a linear state space, a norm/Born-type evaluation, and norm-preserving linear transformations. A Fock/CAR layer requires still more: tensor composition, variable particle number, and statistics structure.

### Programme verdict

The QFIELD verdict remains

\[
\boxed{\texttt{ANALOGY ONLY}}
\tag{10}
\]

but the branch now contributes a precise architectural boundary:

\[
\boxed{
\texttt{QF0 typed support}
<
\texttt{QF1 stochastic weights}
\equiv_{\rm terminal}
\texttt{QF2 terminal complex weights}
<
\texttt{QF3 coherent reconvergence}
<
\texttt{QF4 Hilbert-like dynamics}
<
\texttt{QF5 Fock/CAR structure}.
}
\tag{11}
\]

This is the main result of the second strike.

---

## 2. Starting point: unweighted FCOA channel support

Let \(q=(x,y)\) be an admissible FCOA input pair, or more generally an input record for a finite operation family \(\Omega\). The first QFIELD report defined an unweighted channel-support set

\[
C(q)
=
\Gamma_\Omega(x,y),
\tag{12}
\]

whose elements may be coarse classes such as

\[
\mathrm{BASE},E^+,E^*,E^\times.
\tag{13}
\]

The current FCOA theory records whether such output sorts are available, but it assigns no complex transition amplitudes to them.

The present report asks what happens if amplitudes are added conservatively.

---

## 3. Weak amplitude lift

### Definition 3.1 — Weak normalized amplitude lift

For every input \(q\) with finite nonempty channel support \(C(q)\), a **weak amplitude lift** is a map

\[
A_q:C(q)\to\mathbb C
\tag{14}
\]

satisfying

\[
\sum_{c\in C(q)}|A_q(c)|^2=1.
\tag{15}
\]

The associated one-step channel weights are

\[
p_q(c):=|A_q(c)|^2.
\tag{16}
\]

For a deterministic legacy cell with unique old output channel \(c_0\), legacy exactness is represented by

\[
A_q(c_0)=1.
\tag{17}
\]

A reflected input \(\nu q\) has reflected support \(\nu_C C(q)\). Reflection covariance may be imposed in either of the two elementary forms

\[
A_{\nu q}(\nu_C c)=A_q(c)
\tag{18a}
\]

or

\[
A_{\nu q}(\nu_C c)=\overline{A_q(c)}.
\tag{18b}
\]

Nothing in the present result chooses between (18a) and (18b); that choice itself would require additional structure.

### Remark 3.2

Definition 3.1 is intentionally weak. It does **not** assume a Hilbert space, linear operators, superposition of input states, unitarity, tensor products, or a physical Born rule. Equation (16) is merely a proposed probability readout from channel amplitudes.

---

## 4. Theorem A — amplitude underdetermination

### Theorem 4.1 — Weak amplitude-lift non-uniqueness

Assume there is at least one free reflection orbit of inputs \(\{q,\nu q\}\) whose channel support has cardinality

\[
|C(q)|=m\ge2.
\tag{19}
\]

Then the set of normalized, reflection-covariant weak amplitude lifts extending all deterministic legacy cells contains an uncountable family.

This remains true even if every channel in \(C(q)\) is required to have nonzero amplitude.

### Proof

Choose an ordering

\[
C(q)=\{c_1,\ldots,c_m\}.
\tag{20}
\]

A normalized amplitude assignment on \(q\) is a vector

\[
a=(a_1,\ldots,a_m)\in\mathbb C^m
\tag{21}
\]

on the unit sphere

\[
S^{2m-1}
=
\left\{a:\sum_{j=1}^m|a_j|^2=1\right\}.
\tag{22}
\]

For \(m\ge2\), this sphere is uncountable. The subset on which all coordinates are nonzero is obtained by removing finitely many coordinate hyperplane sections and is still uncountable.

After choosing \(a\) freely on one representative \(q\), equation (18a) or (18b) uniquely determines amplitudes on the reflected representative \(\nu q\). All old deterministic cells remain fixed by (17), so legacy exactness is untouched.

Therefore current normalization, reflection covariance, and legacy exactness do not select a unique amplitude lift or even a finite family of lifts. \(\square\)

### Corollary 4.2 — QFIELD amplitude selector failure

From the present FCOA invariants alone,

\[
\boxed{
\texttt{amplitude lift = REALIZABLE WILD / UNDERDETERMINED}.
}
\tag{23}
\]

### Corollary 4.3

Adding the word “unitarity” as a slogan does not solve the selector problem. A meaningful unitarity condition requires a linear state space and linear transformations between state spaces; neither exists in the current typed-support layer.

---

## 5. Terminal phase erasure

The underdetermination theorem says there are too many amplitude assignments. A stronger fact holds when the channels are terminal.

### Definition 5.1 — Terminal one-step observation model

Fix an input \(q\) and channel support

\[
C(q)=\{c_1,\ldots,c_m\}.
\tag{24}
\]

Assume:

1. the channels are terminal: after producing \(c_j\), the current model has no coherent re-entry transition that can combine it with another channel;
2. available one-step observations distinguish only which terminal channel occurred;
3. the readout is
   \[
   p_j=|A_q(c_j)|^2.
   \tag{25}
   \]

This describes exactly the proposed amplitude decoration of current sink-like FCOA output fibers before any LC2 re-entry structure has been added.

### Theorem 5.2 — Terminal Phase Erasure

Under Definition 5.1, the torus

\[
G_q=U(1)^m
\tag{26}
\]

acts on amplitude assignments by

\[
(e^{i\theta_1},\ldots,e^{i\theta_m})\cdot
(a_1,\ldots,a_m)
=
(e^{i\theta_1}a_1,\ldots,e^{i\theta_m}a_m),
\tag{27}
\]

and leaves every available one-step observable invariant.

The quotient of normalized amplitude assignments by this observational equivalence is naturally identified with the probability simplex

\[
\Delta_{m-1}
=
\left\{(p_1,\ldots,p_m):p_j\ge0,\ \sum_jp_j=1\right\}.
\tag{28}
\]

Hence terminal complex amplitudes contain no operational information beyond ordinary probabilities.

### Proof

For each coordinate,

\[
|e^{i\theta_j}a_j|^2=|a_j|^2,
\tag{29}
\]

so (27) leaves every channel probability unchanged.

Conversely, if two normalized vectors \(a,b\in\mathbb C^m\) have the same coordinate moduli,

\[
|a_j|=|b_j|
\qquad\forall j,
\tag{30}
\]

then for every nonzero coordinate there is a phase \(e^{i\theta_j}\) with

\[
b_j=e^{i\theta_j}a_j.
\tag{31}
\]

For zero coordinates the phase is arbitrary. Thus equal probability vectors are exactly the orbits of the action (27).

The map

\[
[a]\longmapsto(|a_1|^2,\ldots,|a_m|^2)
\tag{32}
\]

therefore gives the stated identification with \(\Delta_{m-1}\). \(\square\)

### Corollary 5.3 — Complex-number decoration is not yet a quantum step

At the terminal one-step level,

\[
\boxed{
\texttt{QF2 terminal complex amplitudes}
\equiv
\texttt{QF1 stochastic channel weights}.
}
\tag{33}
\]

The equivalence is operational with respect to the current observation language.

### Important scope qualification

The theorem does not say that relative phase is never physical. It says that relative phase is not accessible when the theory has only mutually exclusive terminal outcomes and no later operation that recombines them coherently.

That missing recombination is precisely the next threshold.

---

## 6. The reconvergence threshold

### Definition 6.1 — Amplitude-bearing transition network

Let \(G=(V,E)\) be a finite directed acyclic transition fragment. Every edge \(e\) has complex weight

\[
w(e)\in\mathbb C.
\tag{34}
\]

For a directed path

\[
\pi=(e_1,\ldots,e_k)
\tag{35}
\]

define its path amplitude

\[
W(\pi)=\prod_{r=1}^k w(e_r).
\tag{36}
\]

For an observed endpoint \(t\), a **coherent path-sum semantics** assigns

\[
M_t
=
\sum_{\pi:s\rightsquigarrow t}W(\pi),
\tag{37}
\]

and probability/weight

\[
P(t)=|M_t|^2.
\tag{38}
\]

The sum in (37) is extra structure. It is not present in a bare deterministic partial algebra.

### Theorem 6.2 — No reconvergence, no phase interference

Suppose every observed endpoint \(t\) is reachable from the source \(s\) by at most one nonzero-amplitude path. Then every endpoint probability has the form

\[
P(t)=|W(\pi_t)|^2,
\tag{39}
\]

and is invariant under arbitrary changes of phases of edge weights that preserve their moduli.

Therefore no relative phase between alternative histories is observable.

### Proof

By hypothesis the sum (37) contains at most one nonzero term. Hence

\[
M_t=W(\pi_t)
\tag{40}
\]

when the endpoint is reachable, and

\[
P(t)=|W(\pi_t)|^2
=
\prod_{e\in\pi_t}|w(e)|^2.
\tag{41}
\]

Equation (41) depends only on edge moduli. There are no cross terms involving two distinct path amplitudes. \(\square\)

### Corollary 6.3 — Necessary structural condition for operational relative phase

Under coherent path-sum semantics, observable relative phase requires at least one endpoint \(t\) with two distinct nonzero paths

\[
\pi_1\ne\pi_2,
\qquad
s\rightsquigarrow t.
\tag{42}
\]

Thus a branch-and-recombine pattern is structurally necessary.

### Minimal diamond

Take

\[
s\xrightarrow{a_1}e_1\xrightarrow{b_1}t,
\qquad
s\xrightarrow{a_2}e_2\xrightarrow{b_2}t.
\tag{43}
\]

Then

\[
M_t=b_1a_1+b_2a_2
\tag{44}
\]

and

\[
\begin{aligned}
P(t)
&=|b_1a_1+b_2a_2|^2\\
&=|b_1a_1|^2+|b_2a_2|^2
+2\operatorname{Re}\left(b_1a_1\overline{b_2a_2}\right).
\end{aligned}
\tag{45}
\]

For generic nonzero path amplitudes the final term varies with their relative phase. This is the minimal algebraic witness that complex phase has become operational.

### Physical precedent

This structural requirement is the familiar interferometric one: alternatives acquire relative phase and are later brought to a common detection alternative, where the phase changes observed probabilities. The FCOA result here is not a new quantum-mechanical theorem; its value is that it gives a precise **architecture gate** for any proposed FCOA amplitude interpretation.

---

## 7. Theorem C — re-entry is not interference

The line-completion programme already isolates LC2, the problem of allowing terminal outputs to re-enter operations. It is tempting to think that solving LC2 would automatically create an interference layer. It does not.

### Theorem 7.1 — Deterministic re-entry insufficiency

Let \(e_1,e_2\) be two distinct typed outputs and suppose a conservative extension adds deterministic re-entry rules satisfying

\[
r(e_1)=t,
\qquad
r(e_2)=t.
\tag{46}
\]

Then the algebraic fact (46) alone does not determine an interference expression of the form

\[
|z_1+z_2|^2.
\tag{47}
\]

In particular, it determines neither complex path weights \(z_1,z_2\), nor their addition, nor a modulus-square observation rule.

### Proof

Equation (46) is a statement in the deterministic transition/value structure: both inputs have the same image. It contains no scalar field, no assignment of complex weights to the two histories, no operation that combines weights of alternative histories, and no observation functional from combined weights to probabilities.

Many inequivalent probabilistic semantics can therefore be placed over the same deterministic diamond. Examples include:

\[
P(t)=p_1+p_2,
\tag{48}
\]

for mutually exclusive classical alternatives, or

\[
P(t)=|z_1+z_2|^2,
\tag{49}
\]

for a coherent amplitude rule, or other nonstandard weight-combination laws. The endpoint equality (46) selects none of them.

Hence deterministic re-entry/reconvergence is not sufficient to derive interference. \(\square\)

### Corollary 7.2 — Three independent ingredients

A minimal FCOA interference candidate requires at least:

1. **branch support** — two distinguishable alternative channels/histories;
2. **re-entry/reconvergence** — the alternatives can contribute to one later observed outcome;
3. **coherent composition law** — sequential weights multiply and alternative path weights add before observation.

Symbolically,

\[
\boxed{
\mathrm{INTERFERENCE\ CANDIDATE}
=
\mathrm{BRANCH}
+
\mathrm{RECONVERGENCE}
+
\mathrm{PATH\text{-}SUM}.
}
\tag{50}
\]

None of the three may be silently substituted for another.

---

## 8. Current FCOA-Z fails the reconvergence gate

The current FCOA terminal families

\[
E^+,
\qquad
E^*,
\qquad
E^\times
\tag{51}
\]

are sink-like at the audited level: there is no general old rule making them legal inputs to later operations.

Therefore a path such as

\[
q\to E_n^\alpha\to t
\tag{52}
\]

is not currently available as an old FCOA compositional path.

Even if one decorates

\[
q\to E_n^+
\qquad\text{and}\qquad
q\to E_n^\times
\tag{53}
\]

with arbitrary complex numbers, they remain separate terminal records. By Theorem 5.2 their independent phases have no current operational witness.

Hence

\[
\boxed{
\text{the present FCOA-Z channel layer is below the interference threshold.}
}
\tag{54}
\]

This is stronger than the statement “FCOA lacks a Hilbert space.” It identifies the earlier obstruction at which the proposed amplitude interpretation already fails.

---

## 9. Conservative finite diamond: existence does not imply selection

The line-completion gate asks whether typed outputs require an independent coordinate. The interference analysis gives a useful negative control.

### Construction 9.1 — Finite-fiber reconvergence skeleton

At every chosen radial level \(n\), suppose two typed outputs

\[
e_{n,1},e_{n,2}
\tag{55}
\]

are generated from a common input record \(q_n\). Extend the structure by a uniform re-entry map

\[
r(e_{n,1})=t_n,
\qquad
r(e_{n,2})=t_n,
\tag{56}
\]

where \(t_n\) lies on the old base line or in a fixed finite fiber over its level. Apply the corresponding reflected rule on the reflected level/orbit.

No old base-base operation value is changed. No second unbounded coordinate is needed; each radial level only receives finitely many internal channel states and a uniform return rule.

Thus a finite diamond can be represented as a one-dimensional enriched-line extension.

### What this construction proves

It proves only the existence of a **1D reconvergence skeleton**.

It does not select:

- which old \(E\)-families should be paired;
- which re-entry target \(t_n\) is canonical;
- which complex weights should be used;
- why sequential amplitudes multiply;
- why alternative path amplitudes add;
- why a modulus square gives the observable weight.

Consequently the extension remains mathematically underdetermined.

### Dimension verdict

\[
\boxed{
\text{interference-style finite branching/recombination does not by itself force a second spatial coordinate.}
}
\tag{57}
\]

What it forces is **compositional re-entry structure** if terminal FCOA outputs are to participate.

---

## 10. Why QF3 still is not quantum mechanics

Suppose FCOA is enriched far enough that alternative paths carry complex weights and coherent path sums such as (37) are defined.

That would produce cancellation/interference phenomena. But this fact alone does not characterize quantum mechanics.

Complex weighted automata provide an important control example: directed transition systems with complex weights can aggregate path weights and can exploit interference-like cancellation. Literature explicitly studies the relation between quantum finite automata and weighted automata over \(\mathbb C\).

Therefore

\[
\boxed{
\text{complex path interference}\not\Rightarrow\text{Hilbert-space quantum theory}.
}
\tag{58}
\]

The next structural threshold requires a state-space law.

---

## 11. Hilbert-like threshold

A standard finite-dimensional route becomes visible only after adding substantially more than the present FCOA data.

Let a finite channel state be represented by

\[
\psi\in\mathbb C^m
\tag{59}
\]

with normalization

\[
\|\psi\|_2^2=1.
\tag{60}
\]

Let a reversible process act linearly

\[
T:\mathbb C^m\to\mathbb C^m
\tag{61}
\]

and preserve the norm for every state:

\[
\|T\psi\|_2=\|\psi\|_2
\qquad\forall\psi.
\tag{62}
\]

### Proposition 11.1 — Norm-preserving linear threshold

Under (61)-(62),

\[
T^*T=I.
\tag{63}
\]

For square finite-dimensional \(T\), this is the unitary condition.

### Proof

For every \(\psi\),

\[
\langle T\psi,T\psi\rangle
=
\langle\psi,\psi\rangle.
\tag{64}
\]

Hence

\[
\langle\psi,(T^*T-I)\psi\rangle=0
\qquad\forall\psi.
\tag{65}
\]

By the polarization identity, the sesquilinear form associated with \(T^*T-I\) vanishes identically, so

\[
T^*T=I.
\]

In finite equal dimensions an isometry is surjective and therefore unitary. \(\square\)

### Interpretation

Proposition 11.1 is standard linear algebra, not an FCOA theorem deriving quantum mechanics. Its role is diagnostic: it shows exactly what must already have been introduced before the word “unitarity” is mathematically meaningful.

Current FCOA-Z does not yet supply (59), linear superposition, the inner product, or (61).

---

## 12. Fock/CAR threshold lies still higher

Even QF4 would not reconstruct the QFIELD material that motivated Pauli and particle-antiparticle physics.

To reach a fermionic field-like layer one additionally needs, at minimum:

1. one-particle state spaces;
2. composition of independent systems, normally through tensor structure;
3. antisymmetric many-fermion sectors;
4. variable particle number or a Fock-like direct-sum construction;
5. creation and annihilation operators;
6. CAR or an equivalent fermionic statistics structure;
7. dynamical/conservation structure for transitions.

Therefore the ladder from typed FCOA channels to QFT is not one missing axiom but several categorically distinct extensions.

---

## 13. The QFIELD structural ladder

The second strike motivates the following canonical hierarchy for future work.

### QF0 — Typed support

Data:

\[
C(q)\subseteq\{\mathrm{BASE},E^+,E^*,E^\times,\ldots\}.
\tag{66}
\]

Meaning: which channel classes exist?

**Current FCOA status:** present as an abstract shadow.

### QF1 — Stochastic support

Data:

\[
p_q(c)\ge0,
\qquad
\sum_cp_q(c)=1.
\tag{67}
\]

Meaning: classical channel weights.

**Current FCOA status:** can be freely decorated; no internal selector known.

### QF2 — Terminal complex amplitudes

Data:

\[
A_q(c)\in\mathbb C,
\qquad
p_q(c)=|A_q(c)|^2.
\tag{68}
\]

with terminal channels.

**Status:** by Terminal Phase Erasure, operationally collapses to QF1 under the current observation language.

### QF3 — Coherent reconvergent transition network

Data:

\[
W(\pi)=\prod_{e\in\pi}w(e),
\qquad
M_t=\sum_{\pi:s\rightsquigarrow t}W(\pi).
\tag{69}
\]

Meaning: relative phase can affect endpoint weights through cross terms.

**Status:** not present; requires LC2-style re-entry plus an additional path-sum law. Still not uniquely quantum.

### QF4 — Linear normed state dynamics

Data: complex vector states, linear transformations, inner product/norm, Born-like observations, reversible norm-preserving maps.

**Status:** absent. At this layer unitary structure becomes meaningful.

### QF5 — Many-particle / Fock / statistics layer

Data: system composition, antisymmetrization, variable particle number, CAR/CCR-like operator structure.

**Status:** absent. This is the first layer capable of addressing Pauli and particle/antiparticle field theory literally.

### Ladder theorem-like summary

For the current FCOA architecture,

\[
\boxed{
QF0\not\Rightarrow QF1,
\qquad
QF1\equiv_{\rm terminal}QF2,
\qquad
QF2\not\Rightarrow QF3,
\qquad
QF3\not\Rightarrow QF4,
\qquad
QF4\not\Rightarrow QF5.
}
\tag{70}
\]

Each arrow failure is witnessed by a missing independent structure identified in this report.

---

## 14. Line-completion gate update

### LC1 — mixed cell/value selection

Amplitude decoration does not improve the selector problem. By Theorem 4.1 it enlarges the wild family.

\[
\boxed{\texttt{LC1: still UNDERDETERMINED}.}
\tag{71}
\]

### LC2 — output re-entry

The second strike shows why LC2 matters more sharply than before: without re-entry/reconvergence, relative channel phase cannot become operational in a transition network.

But QFIELD does not derive a unique re-entry rule.

\[
\boxed{\texttt{LC2: structurally necessary for QF3, but selector OPEN}.}
\tag{72}
\]

### LC3 — mixed-sign realization

Nothing in amplitude theory chooses a canonical mixed-sign generator. Arbitrary amplitude decoration must not be mistaken for a solution.

\[
\boxed{\texttt{LC3: REALIZABLE WILD / UNDERDETERMINED from QFIELD}.}
\tag{73}
\]

### One-dimensional closure

Finite channel fibers and finite reconvergence diamonds can be placed over the line without an independent unbounded coordinate.

\[
\boxed{\texttt{1D-CLOSED in principle through QF3 skeletons}.}
\tag{74}
\]

This does **not** mean QF3 is already realized canonically; it means that the mere existence of an interference graph would not prove emergent spatial dimension.

---

## 15. Hostile audit

### Claim: “Put a phase on every \(E\)-channel and FCOA becomes quantum.”

**Rejected.** Terminal Phase Erasure reduces those phases to unobservable gauge freedom relative to the current one-step channel observations.

### Claim: “Normalization \(\sum|A|^2=1\) fixes the amplitude law.”

**Rejected.** The unit sphere contains an uncountable family of normalized assignments.

### Claim: “Reflection symmetry fixes the phases.”

**Rejected.** Reflection propagates a choice from one orbit representative to another but does not select the original choice.

### Claim: “If two \(E\)-outputs re-enter the same base point, they interfere.”

**Rejected.** Re-entry supplies endpoint reconvergence, not coherent amplitude addition.

### Claim: “Interference proves Hilbert-space quantum mechanics.”

**Rejected.** Complex weighted transition systems already support path cancellation without providing the full Hilbert/Fock architecture.

### Claim: “A reconvergence diamond is a second spatial dimension.”

**Rejected.** A finite diamond can be represented by finite fibers over a one-dimensional line.

### Claim: “Once a unitary matrix is written down, FCOA has derived unitarity.”

**Rejected.** Writing a unitary matrix assumes a complex linear state space and inner product. The derivation target is precisely whether such structure can arise from FCOA rather than be imported.

---

## 16. Publication decision

**Recommendation remains:** `HOLD FOR APPLIED-DIRECTIONS SYNTHESIS`.

The new result is stronger than the first QFIELD report because it identifies a genuine no-go boundary:

\[
\boxed{
\text{terminal complex amplitudes are an empty enrichment over probabilities}
}
\tag{75}
\]

relative to the current FCOA observation/composition structure.

However, this theorem is an architectural application of standard interference principles, not yet a standalone physical theory or a standalone quantum-foundations result.

It should enter the applied-directions synthesis as:

1. an anti-overclaim theorem;
2. a precise gate between typed channels and coherent process theory;
3. a routing criterion for `FCOA-QUANTIZED`.

A separate paper would become plausible only if a **native FCOA reconvergence mechanism or amplitude-composition law** is derived rather than freely adjoined.

---

## 17. Next strike — search for a native FCOA interference skeleton

The next question is no longer whether arbitrary amplitudes can be attached. They can, and that is mathematically uninformative.

The sharp target is now

\[
\boxed{
\text{Does existing FCOA composition already contain two distinct internal paths}
\text{ that reconverge to one typed/base result?}
}
\tag{76}
\]

The first place to search is the existing association/composition structure.

For three inputs one already compares

\[
(x\star y)\star z
\qquad\text{and}\qquad
x\star(y\star z).
\tag{77}
\]

If both sides are defined through genuinely distinct intermediate states and return to a common result, then an **associator diamond** could provide a native reconvergence skeleton without inventing a new spatial dimension.

Three outcomes are possible:

1. **NO NATIVE DIAMONDS:** terminality/partiality prevents every nontrivial reconvergence; then QF3 requires genuinely new re-entry structure.
2. **BASE-ONLY DIAMONDS:** distinct base-valued compositions reconverge, but terminal channels do not; these may provide a process skeleton but not yet a channel-conversion bridge.
3. **TYPED RE-ENTRY DIAMONDS:** an existing or conservatively forced typed-output composition reconverges; this would be the first serious candidate for routing to `FCOA-QUANTIZED`.

Even in cases 2-3, a path-sum law would still have to be derived rather than assumed.

That is the next research strike.

---

## 18. References

1. R. L. Jaffe, **MIT Quantum Theory Notes / Supplementary Notes on Canonical Quantization and a Charged Particle in a Magnetic Field**, MIT OpenCourseWare. The notes explicitly exhibit two wave-packet paths that reconverge at a common point and show that their relative phase is measurable through interference.  
   https://ocw.mit.edu/courses/8-06-quantum-physics-iii-spring-2016/

2. MIT OpenCourseWare, **Quantum Physics III, Chapter 2: Time-Dependent Approximation Methods**, discussion of overall versus relative phase and observable interference.  
   https://ocw.mit.edu/courses/8-06-quantum-physics-iii-spring-2016/

3. M. V. Panduranga Rao and V. Vinay, **Quantum Finite Automata and Weighted Automata**, arXiv:quant-ph/0701144 (2007). This provides a useful control showing that complex-valued weighted automata can mimic aspects of quantum phase/interference without making every weighted transition system a full quantum theory.  
   https://arxiv.org/abs/quant-ph/0701144

4. G. Chiribella, G. M. D'Ariano, P. Perinotti, **Informational derivation of Quantum Theory**, arXiv:1011.6451 (2010). A useful benchmark demonstrating that full quantum theory requires a richer process-theoretic principle set than merely assigning complex weights to channels.  
   https://arxiv.org/abs/1011.6451

5. G. Chiribella, G. M. D'Ariano, P. Perinotti, **Probabilistic theories with purification**, arXiv:0908.1583 (2009).  
   https://arxiv.org/abs/0908.1583

6. FCOA-Z v1.1 mathematical base, DOI: https://doi.org/10.5281/zenodo.22169264

7. `LINE_COMPLETION_GATE.md`, FCOA-Z applied directorate, current repository branch.
