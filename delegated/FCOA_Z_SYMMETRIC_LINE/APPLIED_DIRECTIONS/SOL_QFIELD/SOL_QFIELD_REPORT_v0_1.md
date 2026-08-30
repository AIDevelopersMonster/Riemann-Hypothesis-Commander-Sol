# SOL-QFIELD — Exchange/Operator/Channel Separation and the Deterministic-Channel Obstruction

**Version:** 0.1  
**Date:** 2026-08-30  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** FIRST TARGET COMPLETE / DIRECT PAULI-ANNIHILATION IDENTIFICATION REJECTED / TYPED CHANNEL SHADOW SURVIVES  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264

---

## 1. Executive verdict

The first SOL-QFIELD target has a deliberately conservative answer.

The three notions that motivated the brief are mathematically different:

1. **fermionic exchange antisymmetry** is a statement about the action of particle permutations on a many-particle state;
2. **field/operator anticommutation** is a relation in the operator algebra used to quantize fermionic fields;
3. **particle-antiparticle annihilation/scattering** is an S-matrix transition from an incoming asymptotic state to one or more possible outgoing states.

They are related inside QFT, but they are not interchangeable descriptions of one binary law.

For FCOA-Z this yields a sharp positive-negative result.

### Negative result A — Pauli is not an FCOA commutation law

The existing FCOA commutation status compares

\[
x\star y\qquad\text{with}\qquad y\star x.
\]

Fermionic exchange instead acts on a many-particle state by a permutation operator. The minus sign under exchange is a phase/sign of the state, not inequality of two values of a partial binary operation.

Therefore

\[
\boxed{\text{Pauli/exchange antisymmetry}\ne\text{FCOA noncommutativity}.}
\]

### Negative result B — particle/antiparticle sign is not statistics parity

Electron and positron excitations are both fermionic. If the FCOA reflection

\[
P_n^+\leftrightarrow P_n^-
\]

were compared with particle/antiparticle conjugation, both reflected objects would still have the same fermion parity. Hence the branch sign cannot simultaneously encode the boson/fermion grading.

### Negative result C — annihilation is not commutativity

QED contains both

\[
e^-e^+\to \gamma\gamma
\]

and

\[
e^-e^+\to e^-e^+
\]

for the same incoming particle species, together with further channels when kinematically allowed. Therefore opposite particle/antiparticle labels do not select one unique terminal outcome, and a bosonic final state does not imply that an underlying operation has become commutative.

### Positive result — typed channel conversion is a real abstract match

FCOA already distinguishes outputs that remain in the base carrier from outputs that land in typed terminal families

\[
E^+,\qquad E^*,\qquad E^\times.
\]

This supports an exact **unweighted channel-incidence taxonomy**:

\[
\boxed{
\text{input geometry}
\longrightarrow
\text{output sort/channel class}
}
\]

without identifying the channel with a quantum amplitude, a photon, a boson, or a physical annihilation product.

### Overall programme verdict

\[
\boxed{\texttt{ANALOGY ONLY}}
\]

with the important refinement:

\[
\boxed{
\text{the direct Pauli/annihilation analogy is rejected,}
\quad
\text{but a typed channel-conversion shadow survives.}
}
\]

No genuine QFT model is present at the current FCOA level.

---

## 2. FCOA-Z input used

Use the audited signed carrier

\[
B^{\pm}
=
\{P_0\}
\sqcup
\{P_n^+:n\ge1\}
\sqcup
\{P_n^-:n\ge1\}
\tag{1}
\]

with reflection

\[
\nu(P_0)=P_0,
\qquad
\nu(P_n^+)=P_n^-,
\qquad
\nu(P_n^-)=P_n^+.
\tag{2}
\]

The published core preserves the positive legacy ray exactly, transfers the same-sign sector by reflection, and localizes all genuinely new binary base freedom to

\[
(B^+\times B^-)
\cup
(B^-\times B^+).
\tag{3}
\]

The current FCOA architecture also has terminal output families

\[
E^+,\qquad E^*,\qquad E^\times,
\tag{4}
\]

which do not in general re-enter the old operations as legal arguments.

For any partial operation \(\star\), the FCOA commutation status records whether

\[
x\star y
\quad\text{and}\quad
y\star x
\tag{5}
\]

are both defined and equal, both defined and unequal, or only one/neither is defined.

This is already enough structure to separate **value symmetry** from **output-channel type**.

---

## 3. Target-field definitions

This section fixes the QFT notions before any comparison is attempted.

### 3.1 Exchange antisymmetry

For two identical fermions the two-particle state belongs to the antisymmetric sector. If \(\tau\) exchanges the two identical particles, then

\[
U(\tau)\,|\Psi\rangle=-|\Psi\rangle.
\tag{6}
\]

Equivalently, in a wavefunction description,

\[
\Psi(1,2)=-\Psi(2,1).
\tag{7}
\]

When the complete one-particle quantum labels coincide, antisymmetry forces the corresponding two-fermion state to vanish. This is the structural origin of the Pauli exclusion statement.

The important type information is:

\[
\boxed{
\text{exchange antisymmetry acts on a many-particle state space.}
}
\tag{8}
\]

It is not itself a scattering process and not a binary product of particle labels.

### 3.2 Canonical anticommutation relations

For a quantized Dirac field the equal-time fermionic canonical anticommutation relations have the form

\[
\{\psi_\alpha(t,\mathbf x),\psi_\beta(t,\mathbf y)\}=0,
\tag{9}
\]

\[
\{\psi_\alpha(t,\mathbf x),\psi_\beta^\dagger(t,\mathbf y)\}
=
\delta_{\alpha\beta}\delta^{(3)}(\mathbf x-\mathbf y).
\tag{10}
\]

The particle and antiparticle mode operators satisfy corresponding CARs. In the standard Dirac-field expansion the electron and positron operators are different mode operators of the same fermionic field, and both sectors obey fermionic statistics.

Thus

\[
\boxed{
\text{CAR is an operator-algebra relation, not an annihilation channel.}
}
\tag{11}
\]

### 3.3 Scattering and annihilation channels

QFT scattering is organized by matrix elements

\[
S_{fi}=\langle f|S|i\rangle,
\tag{12}
\]

or, after stripping the universal momentum-conserving delta distribution, by an amplitude

\[
\mathcal A_{fi}.
\tag{13}
\]

Probabilities, decay rates, and cross sections depend on

\[
|\mathcal A_{fi}|^2
\tag{14}
\]

together with phase-space measures, flux factors, and conservation constraints.

For electron-positron states, QED includes for example

\[
e^-e^+\to\gamma\gamma,
\tag{15}
\]

and elastic Bhabha scattering

\[
e^-e^+\to e^-e^+.
\tag{16}
\]

With additional fields and sufficient center-of-mass energy there are further final species, for example

\[
e^-e^+\to\mu^-\mu^+.
\tag{17}
\]

Hence a fixed incoming particle-type pair generally determines a **family of possible final channels with amplitudes**, not one deterministic output value.

---

## 4. Three-layer taxonomy

The core conceptual output of SOL-QFIELD is the following separation.

### Layer X — exchange/state symmetry

Data:

\[
U(\pi)|\Psi\rangle,
\qquad \pi\in S_N.
\tag{18}
\]

Question:

> How does a many-particle state transform when identical particle slots are permuted?

This is where fermionic minus signs live.

### Layer O — operator algebra

Data:

\[
[A,B],
\qquad
\{A,B\},
\tag{19}
\]

or their local/graded field-theoretic counterparts.

Question:

> What algebraic relation holds among field or creation/annihilation operators?

This is where CAR/CCR and microcausal graded commutation live.

### Layer C — transition/channel structure

Data:

\[
|i\rangle
\xrightarrow{S}
\{|f\rangle\},
\qquad
\mathcal A_{fi}.
\tag{20}
\]

Question:

> Which final states are allowed and with what amplitudes/probabilities?

This is where annihilation, elastic scattering, pair creation, and species conversion live.

### Separation rule

\[
\boxed{
X\ne O\ne C.
}
\tag{21}
\]

QFT relates these layers through the full theory, but no one layer is definitionally identical to another.

This separation should become a permanent anti-overclaim rule for any future FCOA physical analogy.

---

## 5. FCOA channel-type map

For a typed partial FCOA operation

\[
\star:X\times X\rightharpoonup X\sqcup E^+\sqcup E^*\sqcup E^\times,
\tag{22}
\]

define the **output-channel class**

\[
\kappa_\star(x,y)
\in
\{\mathrm{BASE},E^+,E^*,E^\times,\mathrm{UNDEF}\}
\tag{23}
\]

by

\[
\kappa_\star(x,y)=
\begin{cases}
\mathrm{UNDEF}, & x\star y\text{ undefined},\\
\mathrm{BASE}, & x\star y\in X,\\
E^\alpha, & x\star y\in E^\alpha.
\end{cases}
\tag{24}
\]

For a finite operation family \(\Omega\), define the unweighted channel-support set

\[
\Gamma_\Omega(x,y)
:=
\{\kappa_\star(x,y):\star\in\Omega,\ \kappa_\star(x,y)\ne\mathrm{UNDEF}\}.
\tag{25}
\]

Equation (25) contains no amplitude and no probability. It records only which output sorts occur.

This is the strongest object in the present FCOA language that can be compared safely with the **support** of a physical channel set.

---

## 6. Theorem A — commutation status and channel type are independent

### Theorem 6.1 — Output-sort/commutation independence

In a typed partial algebra with at least one base output sort \(X\) and one terminal output sort \(E\), commutation status does not determine whether an interaction is carrier-preserving or channel-converting, and output sort does not determine commutation status.

### Proof

Take two inputs \(a,b\) in a currently free input orbit.

There are four logically consistent local patterns:

1. symmetric base-valued:
   \[
   a\star b=b\star a=c\in X;
   \tag{26}
   \]

2. symmetric terminal-valued:
   \[
   a\star b=b\star a=e\in E;
   \tag{27}
   \]

3. asymmetric base-valued:
   \[
   a\star b=c_1,
   \qquad
   b\star a=c_2,
   \qquad
   c_1\ne c_2,
   \qquad
   c_i\in X;
   \tag{28}
   \]

4. asymmetric terminal-valued:
   \[
   a\star b=e_1,
   \qquad
   b\star a=e_2,
   \qquad
   e_1\ne e_2,
   \qquad
   e_i\in E.
   \tag{29}
   \]

Patterns (26) and (27) have the same commutation status but different channel type. Patterns (26) and (28) have the same base-valued type but different commutation status. Patterns (27) and (29) have the same terminal-valued type but different commutation status.

On the FCOA signed line these patterns can be installed only on previously undefined mixed-sign orbits and their reflected copies, leaving every legacy value untouched. Therefore the independence persists under conservative extension. \(\square\)

### Corollary 6.2

Neither implication is valid:

\[
\text{commutative}\Longrightarrow\text{terminal/converting},
\tag{30}
\]

\[
\text{terminal/converting}\Longrightarrow\text{commutative}.
\tag{31}
\]

Hence

\[
\boxed{
\text{``annihilation into bosons'' cannot be represented as ``the operation became commutative''.}
}
\tag{32}
\]

This is a structural theorem independent of detailed QFT dynamics.

---

## 7. Theorem B — particle/antiparticle conjugation cannot be the fermionic grading

Suppose, only for comparison, that FCOA reflection is mapped to a particle/antiparticle involution

\[
\nu:
P_n^+\leftrightarrow P_n^-
\quad\leadsto\quad
f\leftrightarrow\bar f.
\tag{33}
\]

For a Dirac fermion both \(f\) and \(\bar f\) are fermionic excitations, so their statistics parity is the same:

\[
|f|=|\bar f|=1\pmod2.
\tag{34}
\]

### Proposition 7.1 — Charge/statistics orthogonality

A two-sided FCOA branch sign that flips under \(\nu\) cannot simultaneously serve as the boson/fermion parity of a Dirac particle-antiparticle pair.

### Proof

The branch sign changes under \(\nu\) by construction, whereas the fermionic parity in (34) is invariant under particle-antiparticle conjugation. Therefore any map identifying the two labels fails to preserve the involution action. \(\square\)

### Consequence

The tempting dictionary

\[
+\leftrightarrow\text{fermion},
\qquad
-\leftrightarrow\text{antifermion/boson}
\tag{35}
\]

is invalid.

If a future FCOA construction needs a genuine statistics grading, it must be an **additional label or structure**, not the present branch sign alone.

---

## 8. Theorem C — deterministic single-operation channel no-go

The most important obstruction is not philosophical but mathematical.

### Definition 8.1 — faithful channel-support representation

Let \(I\) be a class of incoming states/types and \(F\) a class of outgoing channel labels. A map into a partial operation

\[
\star:X\times X\rightharpoonup Y
\tag{36}
\]

is **channel-support faithful** at an incoming pair \(i\in I\) if distinct physically allowed outgoing channel classes with nonzero amplitude are represented by distinct available outputs for the same represented incoming data.

### Theorem 8.2 — Single-function obstruction

If one incoming state/type pair has at least two distinct allowed outgoing channel classes with nonzero amplitudes, then no single deterministic partial function of only that incoming pair can be channel-support faithful.

### Proof

A partial function assigns at most one output to each ordered input pair. If the represented physical input has two distinct outgoing channel classes \(f_1\ne f_2\) that must both be retained, faithfulness requires two distinct outputs for the same input pair, contradicting functionality. \(\square\)

### QED witness

At the level of particle species, the same incoming pair

\[
(e^-,e^+)
\tag{37}
\]

has at least the channel types

\[
(e^-,e^+)	o(e^-,e^+)
\tag{38}
\]

and

\[
(e^-,e^+)	o(\gamma,\gamma).
\tag{39}
\]

Therefore a single old FCOA binary operation on particle-type labels cannot faithfully represent QED reaction support.

### What would remove the obstruction?

At least one of the following is required:

1. a set-valued/multivalued channel relation;
2. a family of operations indexed by interaction/channel data;
3. an enlarged input carrying kinematic and internal-state data;
4. a linear state space in which one incoming state has amplitudes to many final states;
5. an S-matrix-like operator on a Fock/Hilbert space.

Items 4-5 are the genuinely QFT-like route.

---

## 9. Minimal FCOA toy model — two-class channel-incidence shadow

The no-go theorem does **not** prevent a coarse channel-support quotient.

Fix an equal-radius mixed pair

\[
a=P_n^+,
\qquad
\bar a=P_n^-.
\tag{40}
\]

Assume the relevant mixed cells of two existing operation symbols \(\star_1,\star_2\) are currently undefined. Extend only the full reflection orbit of these cells.

Choose

\[
a\star_1\bar a\in X,
\qquad
\bar a\star_1 a\in X,
\tag{41}
\]

with the two values related by reflection, and choose

\[
a\star_2\bar a\in E,
\qquad
\bar a\star_2 a\in E,
\tag{42}
\]

again with reflected output values.

Then

\[
\Gamma_{\{\star_1,\star_2\}}(a,\bar a)
=
\{\mathrm{BASE},\mathrm{TERMINAL}\}.
\tag{43}
\]

This can encode the two-color quotient

\[
\{\text{carrier-preserving},\text{channel-converting}\}
\tag{44}
\]

of a reaction-support set.

For example, at the level of channel type only, one may compare

\[
e^-e^+\to e^-e^+
\quad\mapsto\quad
\mathrm{BASE},
\tag{45}
\]

\[
e^-e^+\to\gamma\gamma
\quad\mapsto\quad
\mathrm{TERMINAL}.
\tag{46}
\]

### What the toy model preserves

- old FCOA values are unchanged;
- only previously free mixed-sign cells are used;
- reflection can be respected;
- no ordinary integer addition or multiplication is introduced;
- the construction remains one-dimensional at the carrier level.

### What the toy model discards

- quantum amplitudes;
- interference between diagrams;
- spin/helicity;
- momenta and thresholds;
- conservation laws;
- phase space;
- particle multiplicity;
- superposition;
- unitarity;
- gauge structure.

Therefore (43)-(46) are a **channel-incidence shadow**, not a physical model.

---

## 10. Required negative capability audit

The SOL-QFIELD brief specifically requires a test for missing QFT structure. The result is unequivocal.

| QFT structure | Needed for genuine QFT modeling | Present in current FCOA-Z? | Consequence |
|---|---:|---:|---|
| complex Hilbert/state space | yes | no | no superposition or inner product |
| bosonic/fermionic Fock space | yes | no | no variable particle-number state space |
| permutation representation on many-particle states | yes | no | no literal Pauli/exchange antisymmetry |
| field operators/distributions | yes | no | no field algebra |
| canonical CAR/CCR | yes | no | no literal fermionic/bosonic quantization |
| Hamiltonian/Lagrangian dynamics | yes | no | no QFT time evolution |
| unitary S-matrix | yes for scattering interpretation | no | no transition amplitudes |
| complex amplitudes \(\mathcal A_{fi}\) | yes | no | no interference or phases |
| Born probabilities / cross sections | yes | no | no probabilistic channel weights |
| Lorentz/Poincare structure | yes for relativistic QFT | no | no relativistic kinematics |
| 4-momentum conservation | yes | no primitive law | no physical threshold/channel test |
| charge/current conservation | yes | no primitive law | branch sign is not physical charge |
| gauge structure | yes for QED | no | no photon/QED identification |
| phase-space measure | yes for rates/cross sections | no | no quantitative scattering prediction |

Thus

\[
\boxed{
\text{current FCOA-Z cannot model QFT annihilation in the physical sense.}
}
\tag{47}
\]

The obstruction is not merely that a parameter is missing. The target theory lives in a qualitatively richer category of structures.

---

## 11. Correspondence dictionary

The safe dictionary is deliberately asymmetric: some QFT objects have only a weak FCOA shadow and some have none.

| QFT notion | FCOA object | Status |
|---|---|---|
| exchange of identical fermion slots | argument swap \((x,y)\mapsto(y,x)\) | analogy only; acts on different mathematical objects |
| fermionic minus sign under exchange | no current object | absent |
| CAR of Dirac-field operators | local commutation/definedness status | analogy only; not an operator algebra |
| particle/antiparticle conjugation | branch reflection \(\nu\) | analogy only; branch sign is not charge |
| boson/fermion parity | no current faithful object | absent |
| allowed reaction-channel support | \(\Gamma_\Omega(x,y)\) from typed output sorts | clean abstract shadow |
| carrier-preserving channel | base-valued output | coarse formal match |
| species/channel conversion | terminal/new-sort output | coarse formal match |
| amplitude \(\mathcal A_{fi}\) | none | absent |
| probability/cross section | none | absent |
| conservation constraints | none in current QFIELD layer | absent |
| Fock-space superposition of final states | none | absent |

The only robust positive row is therefore the typed support distinction.

---

## 12. Hostile tests

### Test 1 — “Pauli means the operation is noncommutative”

**Fail.** Pauli is a permutation action on an antisymmetric state sector. FCOA noncommutativity compares two partial-operation values.

### Test 2 — “electron and positron are opposite statistics types”

**Fail.** Both are fermionic excitations of a Dirac field.

### Test 3 — “opposite signs imply annihilation”

**Fail.** Electron-positron states also have elastic scattering and other final channels.

### Test 4 — “annihilation into photons means the binary law became commutative”

**Fail.** Theorem 6.1 proves output sort and commutation status are independent even abstractly.

### Test 5 — “a terminal FCOA symbol is a photon”

**Fail.** No Lorentz representation, gauge field, polarization, energy-momentum, or bosonic Fock structure is present.

### Test 6 — “one deterministic FCOA operation can represent QED channel support”

**Fail.** Theorem 8.2.

### Test 7 — “channel outputs force a second spatial dimension”

**Fail at current level.** The toy channel-incidence shadow is realizable using finite/internal typed outputs over the one-dimensional signed line.

---

## 13. Line-completion gate assessment

The QFIELD result is useful for `LINE_COMPLETION_GATE.md`.

### LC1 — cell realization

QFT does not select a unique mixed-sign FCOA value. The physical analogy supplies no canonical generator for one mixed cell.

Verdict from QFIELD alone:

\[
\boxed{\texttt{REALIZABLE WILD / UNDERDETERMINED}.}
\tag{48}
\]

### LC2 — output re-entry

QFT strongly suggests that a genuine transition theory would require outputs to participate in later dynamics, but current FCOA terminal values do not re-enter generally. QFIELD provides no canonical re-entry rule.

Verdict:

\[
\boxed{\texttt{OPEN}.}
\tag{49}
\]

### LC3 — mixed-sign realization

A coarse base-vs-terminal channel taxonomy can be represented conservatively, but it is not uniquely selected by QFT.

Verdict:

\[
\boxed{
\texttt{1D-CLOSED at unweighted channel-incidence level;}
\quad
\texttt{QFT MODEL OBSTRUCTED at current structure level.}
}
\tag{50}
\]

### Dimension status

Nothing in SOL-QFIELD proves `DIMENSION-FORCING`.

The missing structure is principally

\[
\boxed{\text{state-space / amplitude / dynamics structure, not a second coordinate}.}
\tag{51}
\]

This is an important negative control for later FCOA-CARTESIAN and FCOA-QUANTIZED programmes.

---

## 14. What is proved and what is not

### Proved inside the abstract comparison

1. exchange/state symmetry, operator algebra, and transition channels are different structural layers;
2. FCOA commutation status and FCOA output-channel type are independent;
3. branch reflection cannot simultaneously encode particle/antiparticle conjugation and fermion/boson parity for a Dirac pair;
4. a single deterministic partial binary function cannot faithfully represent a genuinely multi-channel reaction support for one fixed input pair;
5. FCOA can encode an unweighted base-vs-terminal channel-incidence quotient on the signed line;
6. this quotient is 1D-closed and does not force a new spatial dimension.

### Not proved and not claimed

- that FCOA signs are electric charge;
- that FCOA reflection is charge conjugation, CP, or CPT;
- that any \(E\)-family is a photon, boson, vacuum, or physical final state;
- that a mixed-sign FCOA cell is physical annihilation;
- that FCOA commutation spectra are quantum statistics;
- that FCOA reproduces QED amplitudes or cross sections;
- that a Hilbert/Fock lift of FCOA exists;
- that QFT selects a unique FCOA mixed-sector operation.

---

## 15. Research consequence

The useful lesson is narrower and stronger than the original analogy:

\[
\boxed{
\text{do not ask whether opposite signs make an operation commutative;}
}
\]

ask instead

\[
\boxed{
\text{whether input geometry can select an output-sort/channel class independently of local commutation status.}
}
\tag{52}
\]

This reframes SOL-QFIELD from a speculative particle analogy into a precise algebraic design question.

The natural FCOA object is therefore not “annihilation” but a **typed transition-support relation**.

---

## 16. Publication decision

**Recommendation:** `HOLD FOR APPLIED-DIRECTIONS SYNTHESIS`.

The result is valuable as an anti-overclaim theorem and as a three-layer taxonomy, but it is not a standalone QFT/FCOA paper. A standalone publication would require at minimum one of:

1. a nontrivial Hilbert/Fock lift of an FCOA structure;
2. a mathematically natural amplitude-valued extension;
3. a conservation-law selector derived from FCOA invariants;
4. a theorem connecting output-channel support to a recognized transition-system formalism beyond a hand-chosen finite quotient.

Until then the correct scientific use is as a rigorous negative-control section in the applied-directions synthesis.

---

## 17. Next strike

The next QFIELD question should not be “which \(E\) is a photon?”

The sharp next question is:

\[
\boxed{
\text{Can one enrich FCOA channel support with amplitudes while preserving legacy exactness and line closure?}
}
\tag{53}
\]

A minimal target would be a complex-amplitude decoration

\[
A_\alpha(x,y)\in\mathbb C
\tag{54}
\]

on typed output channels satisfying at least:

1. reflection covariance;
2. a normalization/unitarity surrogate;
3. a conservation-like selection rule derived internally rather than imposed as a lookup table;
4. exact recovery of the old deterministic FCOA operation when precisely one channel has nonzero weight.

If every such nontrivial amplitude lift necessarily introduces a linear/Fock-like state layer, that would be a genuine structural bridge to the later `FCOA-QUANTIZED` programme. If arbitrary weights can be attached freely, the analogy remains underdetermined and should stop here.

---

## 18. References

1. David Tong, **Lectures on Quantum Field Theory**, Section 5, *Quantizing the Dirac Field* — fermionic quantization, spin-statistics discussion, particle/antiparticle mode operators and canonical anticommutation relations.  
   https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S5.html

2. David Tong, **Lectures on Quantum Field Theory**, Section 6, *Quantum Electrodynamics* — QED Feynman rules, electron-positron annihilation, Bhabha scattering, and additional channels.  
   https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S6.html

3. David Tong, **Lectures on Quantum Field Theory**, Section 3, *Interacting Fields* — S-matrix elements, amplitudes, momentum-conserving delta functions, decay rates, phase space, and cross sections.  
   https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S3.html

4. M. E. Peskin and D. V. Schroeder, **An Introduction to Quantum Field Theory**, Addison-Wesley, 1995.

5. S. Weinberg, **The Quantum Theory of Fields, Vol. I**, Cambridge University Press, 1995.

6. FCOA-Z v1.1 mathematical base, DOI: https://doi.org/10.5281/zenodo.22169264
