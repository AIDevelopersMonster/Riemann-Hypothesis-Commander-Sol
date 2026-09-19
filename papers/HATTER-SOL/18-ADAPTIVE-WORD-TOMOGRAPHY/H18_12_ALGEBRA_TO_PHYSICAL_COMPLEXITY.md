# H18-12 · Algebra-to-Physical Complexity
## Hardware images of finite mathematical presentations

Status: **FOUNDATIONAL DRAFT / theorem-program layer**

Date: 19 September 2026.

## 1. Question

The H17/H18 hardware experiments suggest a question that is broader than FPGA
optimization:

> If two different finite mathematical presentations solve the same abstract
> task, can a fixed Boolean/hardware realization process be used to compare
> the physical complexity induced by the mathematics itself?

The intended chain is

\[
\boxed{
\text{mathematical presentation}
\longrightarrow
\text{Boolean realization}
\longrightarrow
\text{mapped circuit}
\longrightarrow
\text{placed/routed physical profile}.
}
\]

The key point is that this is **not** merely the study of one Boolean function.
Different mathematical presentations may factor the same semantics in very
different ways before Boolean synthesis.

This layer introduces a precise vocabulary for that distinction.

---

## 2. Existing theory that this layer connects

This program is adjacent to several established theories, but is not identified
with any one of them.

### 2.1 Relative complexity of algebras and algebraic implementations

Lynch introduced straight-line program length as a complexity parameter
applicable in arbitrary algebras, explicitly including complexity-bounded group
theory:

- N. A. Lynch, *Straight-line program length as a parameter for complexity
  analysis*, JCSS 21(3), 1980,
  DOI 10.1016/0022-0000(80)90024-0.

Lynch and Blum developed relative complexity notions for algebras and for
different primitive-operation bases:

- N. A. Lynch, E. K. Blum, *Relative Complexity of Operations on Numeric and
  Bit-String Algebras*, Mathematical Systems Theory 13, 1980,
  DOI 10.1007/BF01744295.
- N. A. Lynch, E. K. Blum, *Relative Complexity of Algebras*, Mathematical
  Systems Theory 14, 1981,
  DOI 10.1007/BF01752396.

Ehrig and Mahr studied complexity of algebraic implementations of abstract data
types:

- H. Ehrig, B. Mahr, *Complexity of algebraic implementations for abstract
  data types*, JCSS 23(2), 1981,
  DOI 10.1016/0022-0000(81)90014-3.

These works supply precedent for treating the **choice of algebraic
presentation / implementation basis** as a legitimate complexity variable.

### 2.2 Circuits over finite algebraic structures

Kawałek and Krzaczkowski explicitly study the bridge between finite algebraic
structures and circuit complexity:

- P. Kawałek, J. Krzaczkowski,
  *Complexity Classes Arising from Circuits over Finite Algebraic Structures*,
  LICS 2026, DOI 10.4230/LIPIcs.LICS.2026.61.

Their objective is algebra-to-circuit complexity.  The present H18-12 program
continues one step further toward a **technology-relative physical realization
profile**.

### 2.3 VLSI area-time complexity

Thompson's VLSI model treats physical area and computation time as complexity
resources and derives area-time lower bounds:

- C. D. Thompson, *Area-Time Complexity for VLSI*, STOC 1979,
  DOI 10.1145/800135.804401.
- C. D. Thompson, *A Complexity Theory for VLSI*, PhD thesis,
  CMU-CS-80-140, 1980.

This establishes that physical area/time can be treated theoretically rather
than merely as implementation anecdotes.

### 2.4 FPGA technology mapping

LUT technology mapping separates Boolean-network structure from a particular
FPGA realization.  A classical reference is:

- J. Cong, E. Ding, *FlowMap: An Optimal Technology Mapping Algorithm for
  Delay Optimization in Lookup-Table Based FPGA Designs*,
  IEEE TCAD 13(1), 1994, DOI 10.1109/43.273754.

This literature also warns that mapped area and delay depend on the mapping
model and implementation flow.

### 2.5 Claim boundary on novelty

No claim is made here that the individual ingredients above are new.

The provisional research claim is narrower:

> We have not yet identified a standard framework that explicitly compares
> *different finite mathematical presentations of the same abstract task* by
> composing presentation-preserving Boolean realization with a fixed
> FPGA place-and-route process and treating the resulting physical profile as
> a relative characteristic of the presentations.

This is a literature-search statement, not a priority claim.  It must be
re-audited before publication.

---

## 3. Finite computational task

Let

\[
\Phi:X\to Y
\]

be a finite deterministic computational task.

For fault-tolerant or adversarial problems it is often better to use a finite
relation

\[
\mathcal R\subseteq X\times F\times Y,
\]

where \(F\) is an abstract fault/adversary space.  A realization is correct if
its output belongs to the allowed relation for every \((x,f)\).

This distinction matters for H17/H18 because their concrete erasure alphabets
are presentation-dependent.

---

## 4. Mathematical presentation

A **finite mathematical presentation** of the task is denoted

\[
M=(\mathcal A,\Omega,\Gamma,\llbracket\cdot\rrbracket),
\]

where:

- \(\mathcal A\) is a finite collection of carrier sets / state spaces;
- \(\Omega\) is the declared primitive operation family;
- \(\Gamma\) is a finite factorization graph, decision graph, straight-line
  program, or other explicit construction over those primitives;
- \(\llbracket M\rrbracket\) is the induced abstract semantics.

Two presentations may therefore have the same semantics while exposing very
different internal structures.

Examples in HATTER:

- H17: fixed robust fingerprint + known-erasure repair;
- H18: adaptive interrogation + decision DAG;
- the same H18 presentation executed sequentially or spatialized
  combinationally.

The last pair has the same mathematics but a different hardware execution
discipline; H17 versus H18 changes the mathematical presentation itself.

---

## 5. Booleanization theorem

Let every finite carrier \(A_i\in\mathcal A\) have an injective encoding

\[
e_i:A_i\hookrightarrow\{0,1\}^{m_i}.
\]

For each primitive operation

\[
f:A_{i_1}\times\cdots\times A_{i_k}\to A_j
\]

there exists a Boolean function

\[
B_f:
\{0,1\}^{m_{i_1}+\cdots+m_{i_k}}
\to
\{0,1\}^{m_j}
\]

such that on valid codes

\[
B_f(e_{i_1}(a_1),\ldots,e_{i_k}(a_k))
=
e_j(f(a_1,\ldots,a_k)).
\]

### Proposition 5.1 — finite exact Boolean realizability

Every finite mathematical presentation has an exact Boolean-circuit
realization after finite encoding of its carriers.

### Proof

Each primitive operation is a function on a finite domain.  Each output bit
therefore has a finite truth table and hence admits a Boolean formula, for
example in disjunctive normal form.  Replacing each primitive node of
\(\Gamma\) by its exact Boolean realization and wiring according to
\(\Gamma\) gives an exact Boolean circuit for the presentation.  No efficiency
claim is implied. \(\square\)

This proposition establishes **existence only**.  The central problem is the
size/depth/physical quality of the resulting realization.

---

## 6. Why semantics alone is insufficient

Suppose

\[
\llbracket M_1\rrbracket
=
\llbracket M_2\rrbracket
=
\Phi.
\]

If an unrestricted optimizer is allowed to discard both internal
factorizations and optimize only the flattened truth table of \(\Phi\), the
two presentations may become indistinguishable.

Therefore two different complexity objects must be separated.

### 6.1 Semantic physical complexity

Let

\[
\mathscr C(\Phi)
\]

be the class of all correct Boolean circuits implementing \(\Phi\).

The semantic hardware optimum concerns \(\Phi\) alone and deliberately forgets
the presentation.

### 6.2 Presentation-preserving realization class

Let

\[
\Pi
\]

be a **realization discipline** specifying which structural aspects of \(M\)
must be preserved, for example:

- declared primitive operations;
- permitted common-subexpression sharing;
- permitted algebraic rewrites;
- decision-DAG sharing;
- register boundaries;
- sequential versus combinational execution;
- fault encoding;
- input/output encoding.

Define

\[
\mathscr C_\Pi(M)
\]

as the circuits obtainable from \(M\) under discipline \(\Pi\).

If \(M\) is semantically exact, then

\[
\mathscr C_\Pi(M)\subseteq\mathscr C(\Phi).
\]

This inclusion is the formal place where "different mathematics" survives the
Booleanization step.

---

## 7. Technology stack

A hardware measurement is meaningless without fixing the realization
environment.

Define the technology stack

\[
\Theta=
(
D,S,V,T,O,C,P
),
\]

where, minimally:

- \(D\): FPGA device/family/package;
- \(S\): speed grade and operating corner;
- \(V\): synthesis/P&R tool and version;
- \(T\): synthesis / mapping / fitting options and seed policy;
- \(O\): I/O and register-boundary convention;
- \(C\): timing constraints;
- \(P\): physical reporting protocol.

For H17/H18 matched experiments this includes, for example, exact device,
Quartus II 13.1, the same 100 MHz reference constraint, and the same
slow-corner TimeQuest analysis.

---

## 8. Physical realization profile

For a successfully placed-and-routed circuit \(C\), define the vector

\[
P_\Theta(C)=
(
A,L,R,M,DSP,d_{\rm logic},
t_{\rm cell},t_{\rm route},
F_{\max},N_{\rm cyc},T_{\rm tx}
),
\]

where:

- \(A\): mapped logic area (LE/LUT/ALM);
- \(L\): combinational-logic count;
- \(R\): register count;
- \(M\): mapped memory bits / RAM blocks;
- \(DSP\): hard multiplier/DSP usage;
- \(d_{\rm logic}\): critical-path logic levels;
- \(t_{\rm cell}\): critical-path cell delay;
- \(t_{\rm route}\): critical-path routing delay;
- \(F_{\max}\): routed maximum clock frequency;
- \(N_{\rm cyc}\): transaction-cycle bound;
- \(T_{\rm tx}=N_{\rm cyc}/F_{\max}\): physical transaction latency.

A no-fit result is also information:

\[
P_\Theta(C)=\mathrm{NOFIT}(A_{\rm est},A_{\rm cap},\ldots).
\]

No routed \(F_{\max}\) may be inferred from a design that did not fit.

---

## 9. Hardware image of a mathematical presentation

### Definition 9.1 — presentation hardware image

For fixed \((\Theta,\Pi)\), define

\[
\boxed{
H_{\Theta,\Pi}(M)
=
\operatorname{ParetoMin}
\{P_\Theta(C): C\in\mathscr C_\Pi(M)\}.
}
\]

This is a set/vector frontier, not necessarily one scalar.

### Definition 9.2 — semantic physical complexity frontier

For the abstract function/relation itself,

\[
\boxed{
H_\Theta^\*(\Phi)
=
\operatorname{ParetoMin}
\{P_\Theta(C): C\in\mathscr C(\Phi)\}.
}
\]

In general,

\[
H_\Theta^\*(\Phi)
\]

is not computationally available.  Practical experiments produce certified
realization witnesses and therefore empirical upper bounds / best-known
frontiers.

### Important distinction

\[
\boxed{
H_{\Theta,\Pi}(M)
\neq
H_\Theta^\*(\Phi)
\quad\text{in general}.
}
\]

The first measures a mathematical presentation under a declared realization
discipline.

The second measures the task after forgetting how the mathematics described
it.

---

## 10. Measured image versus theoretical optimum

A proprietary synthesis run is not a proof of optimal hardware.

Let a concrete flow \(S\) produce circuit

\[
C=S_{\Theta,\Pi}(M).
\]

The measured result

\[
\widehat H_{\Theta,\Pi,S}(M)=P_\Theta(C)
\]

is a reproducible **witness**, not automatically the Pareto optimum
\(H_{\Theta,\Pi}(M)\).

Therefore published HATTER claims must say:

- "measured under Quartus II 13.1 flow ...",
- not "minimum FPGA complexity",

unless an independent lower-bound/optimality proof exists.

---

## 11. Three effects that must not be conflated

The experiments naturally separate three variables.

### 11.1 Mathematical-presentation effect

Hold \(\Theta\) and execution discipline \(\Pi\) fixed; vary \(M\):

\[
M_1\longleftrightarrow M_2.
\]

This is the comparison relevant to "different mathematics".

H17-LAB-02 versus H18-LAB-04 is designed to approximate this comparison:
both use registered inputs, one combinational mathematical core, and registered
outputs.

### 11.2 Architecture effect

Hold \(M\) and \(\Theta\) fixed; vary \(\Pi\):

\[
\Pi_1\longleftrightarrow\Pi_2.
\]

H18-LAB-03 versus H18-LAB-04 isolates this direction:

- LAB-03: sequential reuse;
- LAB-04: full spatialization.

This reveals the price of converting time/adaptivity into space.

### 11.3 Technology effect

Hold \(M\) and \(\Pi\) fixed; vary \(\Theta\):

\[
\Theta_1\longleftrightarrow\Theta_2.
\]

H17's 22K-versus-115K same-generation capacity experiments are examples.

A strong comparison program needs controls in all three directions.

---

## 12. Exact versus contract-level equivalence

Different mathematical models need not expose identical auxiliary inputs.

### Level E0 — exact semantic equivalence

After fixed input/output encodings,

\[
\Phi_{M_1}=\Phi_{M_2}
\]

pointwise.

This is the strongest comparison.

### Level E1 — common abstract contract

The models solve the same abstract relation \(\mathcal R\), but their internal
query/fault alphabets differ.

This is the present H17/H18 robust-tomography situation.

For E1 comparisons:

- the fault-free subproblem can be compared pointwise;
- fault tolerance must be compared through a declared common adversary model;
- model-specific erasure identities must not be silently treated as identical
  inputs.

### Level E2 — related but non-equivalent tasks

Only descriptive hardware comparison is valid.  No claim about relative
complexity of "the same mathematics problem" is permitted.

---

## 13. No universal scalar by default

Area, latency, memory, and routing are different resources.

Therefore the primary order is Pareto dominance.

For two measured profiles \(p,q\), say \(p\preceq q\) if all declared cost
coordinates of \(p\) are no worse than those of \(q\), with at least one
strictly better for strict dominance.

Scalar products such as

\[
AT,\qquad AT^2
\]

may be reported, following the area-time tradition, but only as
application-dependent projections of the profile.

They are not universal rankings of mathematics.

---

## 14. Relative hardware ratios

For two matched successful implementations define dimensionless ratios

\[
\rho_A(M_2:M_1)=\frac{A_2}{A_1},
\]

\[
\rho_F(M_2:M_1)=\frac{F_{\max,2}}{F_{\max,1}},
\]

\[
\rho_T(M_2:M_1)=\frac{T_{{\rm tx},2}}{T_{{\rm tx},1}},
\]

and similarly for logic depth, memory, routing delay, and register count.

These ratios are meaningful only when the corresponding technology,
interfaces, and reporting rules are matched.

---

## 15. Mathematical-to-hardware leverage

A transformation

\[
M\to M'
\]

may look large mathematically but have little hardware effect, or vice versa.

Define the **hardware leverage vector**

\[
\Lambda_{\Theta,\Pi}(M\to M')
=
\left(
\frac{A'}{A},
\frac{T'_{\rm tx}}{T_{\rm tx}},
\frac{d'_{\rm logic}}{d_{\rm logic}},
\frac{M'}{M},
\ldots
\right).
\]

This deliberately remains a vector.

Examples already seen in H17/H18 motivate the distinction:

- a closure theorem can delete repeated membership machinery and have large
  physical leverage;
- a strong query-vocabulary compression can have weak memory leverage if the
  six-way transition table remains dominant.

Thus

\[
\boxed{
\text{semantic compression}
\not\Rightarrow
\text{proportional physical compression}.
}
\]

This is an observation/hypothesis program, not yet a universal theorem.

---

## 16. Spatialization cost

For one mathematical presentation \(M\), compare a sequential discipline
\(\Pi_{\rm seq}\) with a one-cycle spatial discipline \(\Pi_{\rm spat}\).

Define, when both fit,

\[
\sigma_A(M)=
\frac{A_{\rm spat}}{A_{\rm seq}},
\qquad
\sigma_T(M)=
\frac{T_{\rm spat}}{T_{\rm seq}}.
\]

This measures the physical price of converting temporal reuse into spatial
parallelism.

H18 provides an unusually clean finite test because its adaptive protocol can
be executed temporally or compiled into a finite combinational decision
network.

---

## 17. Preliminary H17/H18 evidence

These numbers are **experimental inputs**, not conclusions of the theory.

### H17-LAB-02, EP4CE22F17C6

Wide fixed robust8 combinational core with one registered result cycle:

- 19,540 / 22,320 LE = 88%;
- 132 registers;
- \(F_{\max}=24.52\) MHz, Slow 85 C;
- worst data delay 41.082 ns;
- 65 logic levels.

### H18-LAB-03, EP4CE22F17C6

Restricted-12 adaptive microcoded realization:

- 5,227 / 22,320 LE = 23%;
- 211 registers;
- \(F_{\max}=41.28\) MHz;
- worst data delay 24.510 ns;
- 42 logic levels;
- verified worst transaction: 42 cycles.

Thus temporal reuse gives a large area reduction and shorter single-cycle
critical path, but a much larger transaction latency.

### H18-LAB-04, EP4CE22F17C6

Full combinational spatialization of the same restricted-12 adaptive
mathematics:

- estimated/mapped combinational nodes: 26,332;
- target capacity: 22,320;
- utilization estimate: 118%;
- fitter result: **NO FIT**.

Therefore LAB-04 has no valid routed timing result on this target.

This no-fit result is already informative: full spatialization of the H18
presentation crosses a physical capacity boundary that H17-LAB-02 did not.

### Matched large-device experiment — TIMING MEASURED

H17-LAB-02 and H18-LAB-04 have now both been routed and timed on the same
EP4CE115F29C7 target under the same C7 speed grade and Slow 1200 mV / 85 C
analysis model.

Selected worst-path data:

| quantity | H17-LAB-02 | H18-LAB-04 |
| --- | ---: | ---: |
| data delay | 47.249 ns | 46.516 ns |
| logic levels | 65 | 65 |
| data-path cell delay | 17.092 ns | 15.721 ns |
| data-path routing delay | 29.941 ns | 30.579 ns |
| reciprocal-delay frequency | 21.16 MHz | 21.50 MHz |

Thus H18's selected data path is about 1.55% shorter.  The two paths have
exactly the same reported logic-level count, while H18 exchanges about 8.0%
less cell delay for about 2.1% more routing delay.

This is the first matched evidence for a central H18-12 point:

\[
\boxed{
\text{similar physical scalar cost can hide different internal physical
factorizations.}
}
\]

The timing coordinate is now closed for this matched comparison.  The exact
115K H18 area coordinate remains pending extraction from the map/fit summary;
it is not inferred from the earlier 22K no-fit estimate.



### Matched Cyclone V experiment — SECOND TECHNOLOGY POINT

The same one-cycle H17-LAB-02 and H18-LAB-04 presentations have now also been
mapped, fitted, and timed on the same 5CEFA7F23C6 target under Quartus II 13.1
and the Slow 1100 mV / 85 C model.

| quantity | H17-LAB-02 | H18-LAB-04 | H18/H17 |
| --- | ---: | ---: | ---: |
| ALMs | 7,941 | 10,627 | 1.338 |
| DSP blocks | 40 | 48 | 1.200 |
| registers | 132 | 69 | 0.523 |
| Fmax | 27.85 MHz | 28.52 MHz | 1.024 |
| worst data delay | 35.694 ns | 34.827 ns | 0.976 |
| logic levels | 34 | 30 | 0.882 |
| cell delay | 12.726 ns | 13.556 ns | 1.065 |
| routing delay | 22.969 ns | 21.270 ns | 0.926 |

This point is more discriminating than the large Cyclone-IV result.  The
spatialized H18 presentation is substantially more expensive in ALMs and DSPs,
yet it is slightly faster and has fewer reported logic levels.  Its critical
path pays more cell delay but less routing delay.

Therefore the two presentations occupy different coordinates of a
technology-relative area/depth/routing frontier rather than admitting a
single scalar ordering.

An important empirical regularity also appears: the H18/H17 area ratio on
Cyclone V is about 1.338, close to the approximately 1.35 pre-fit
combinational-node ratio seen on the Cyclone-IV 22K experiment.  This
cross-technology similarity is evidence worth testing on further targets, but
it is not yet treated as an invariant.

The two matched technology points now support a stronger experimental reading
of H12-H1: presentation-sensitive hardware images persist across more than one
FPGA target.  They do not yet establish technology-independent ordering or
circuit lower bounds.



### Same-mathematics Cyclone V architecture control — CLOSED

The H18-LAB-03 temporal and H18-LAB-04 spatial realizations have now both
been fitted and timed on the same 5CEFA7F23C6 target.  They are generated from
the same restricted-12 H18-11 mathematical certificate and differ principally
in execution discipline.

| quantity | LAB-03 temporal | LAB-04 spatial | spatial/temporal |
| --- | ---: | ---: | ---: |
| ALMs | 1,455 | 10,627 | 7.304 |
| DSP blocks | 26 | 48 | 1.846 |
| registers | 211 | 69 | 0.327 |
| Fmax | 47.02 MHz | 28.52 MHz | 0.607 |
| worst data delay | 21.075 ns | 34.827 ns | 1.653 |
| logic levels | 18 | 30 | 1.667 |
| cell delay | 10.227 ns | 13.556 ns | 1.326 |
| routing delay | 10.850 ns | 21.270 ns | 1.960 |
| worst transaction cycles | 42 | 1 | 0.0238 |

At each implementation's measured Fmax,

\[
T_{\rm temporal}\approx
\frac{42}{47.02\ {\rm MHz}}
=
0.893\,\mu{\rm s},
\]

whereas

\[
T_{\rm spatial}\approx
\frac{1}{28.52\ {\rm MHz}}
=
0.0351\,\mu{\rm s}.
\]

Thus full spatialization multiplies ALM usage by about 7.30 and DSP usage by
about 1.85, while reducing worst transaction latency by about 25.5 times.

This is the cleanest present experimental isolation of the architecture effect

\[
\Pi_{\rm seq}\leftrightarrow\Pi_{\rm spat}
\]

for one fixed mathematical presentation.

The result also shows why \(F_{\max}\) alone is not a transaction-speed
metric: the temporal design has the higher Fmax and the shorter one-cycle
critical path, yet its 42-cycle protocol has far larger end-to-end latency.


---

## 18. Preliminary hypotheses

These are explicitly hypotheses to be tested.

### H12-H1 — presentation sensitivity

Semantically comparable finite mathematical presentations can induce
substantially different physical realization profiles under one fixed
technology stack and one matched realization discipline.

### H12-H2 — non-proportional leverage

Reduction in a natural mathematical size parameter (query alphabet, SLP
length, state count, invariant count) need not produce proportional reduction
in FPGA area or latency.

### H12-H3 — spatialization penalty

An adaptive decision presentation can be cheap when temporally reused but
expensive when fully spatialized, because mutually exclusive future branches
become simultaneous hardware.

### H12-H4 — representation-versus-task gap

A large difference

\[
H_{\Theta,\Pi}(M_1)
\quad\text{vs}\quad
H_{\Theta,\Pi}(M_2)
\]

does not imply that the underlying semantic task has that complexity gap.
It may measure presentation overhead.

### H12-H5 — physical bottleneck localization

The hardware consequence of a mathematical transformation is governed mainly
by whether it removes structure lying on a dominant physical path/resource,
not by its semantic elegance alone.

### H12-H6 — ordering may be technology-relative

A presentation that dominates on one FPGA family need not dominate on another,
because LUT structure, hard DSP/RAM inference, routing architecture, and
mapping heuristics differ.

---

## 19. What would constitute a theorem beyond measurement?

The framework becomes mathematically stronger when one proves statements such
as:

1. lower bounds on Boolean size/depth for a presentation-preserving
   realization class;
2. lower bounds on semantic circuit complexity of the task itself;
3. invariance of a profile component under a class of algebraic rewrites;
4. monotonicity or subadditivity of presentation cost under composition;
5. bounded distortion between algebraic SLP complexity and Boolean depth for
   a fixed primitive library;
6. lower bounds on spatialization cost for adaptive decision structures.

These are future theorem targets.

---

## 20. Immediate HATTER program

The next steps are:

1. retain the two matched H17/H18 technology points as the first
   presentation-effect dataset;
2. retain the now-closed Cyclone-V H18-LAB-03/LAB-04 pair as the
   same-mathematics architecture-effect control;
3. treat the EP4CE115F29C7 H18 value 26,460 as a MAP estimate only until a
   separately archived final fitter utilization line is available;
4. use H18-13 as the common H17/H18 abstract fault contract;
5. define a small family of alternative mathematically equivalent
   factorizations and test whether the area/depth ordering is stable;
6. search for the first provable lower bound connecting decision/query
   structure to circuit size/depth.

The objective is not merely to optimize one FPGA design.

It is to study the map

\[
\boxed{
\text{mathematics}
\longrightarrow
\text{Boolean geometry}
\longrightarrow
\text{physical geometry}.
}
\]
