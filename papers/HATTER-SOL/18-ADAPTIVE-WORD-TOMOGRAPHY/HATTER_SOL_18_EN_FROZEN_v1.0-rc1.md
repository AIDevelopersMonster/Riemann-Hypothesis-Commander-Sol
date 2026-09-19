# HATTER-SOL-18
# Adaptive Non-Abelian Tomography: Nielsen Dynamics, Commutator-Lift Trace, Query-Language Compression, and Hardware Images of Mathematics

**Status:** PUBLICATION FREEZE · EN v1.0-rc1  
**Author:** Alex Malachevsky  
**ORCID:** 0009-0008-6009-3196  
**AI research collaborator:** Commander Sol · Hatter Sol  
**Branch:** `research/hatter-sol-18-adaptive-word-tomography`  
**Parent:** HATTER-SOL-17  
**State date:** 19 September 2026

## Abstract

HATTER-SOL-18 continues the finite \(PSL(2,7)\) laboratory of HATTER-SOL-17 by
replacing a fixed family of word observers with an adaptive interrogation
program. The state space consists of simultaneous-conjugacy orbits of ordered
pairs \((A,B)\). There are 114 generating orbits; the full identify-or-REJECT
quotient of \(PSL(2,7)^2\) contains 197 pair orbits: 114 generating and 83
non-generating.

Among freely reduced words of length at most four, 160 raw words induce 50
distinct class-valued queries. Exact dynamic programming gives the minimum
worst-case adaptive depth

\[
\boxed{D^*(W_4)=4},
\]

whereas fixed observation in the same pool requires at least five queries:

\[
\boxed{5_{\rm fixed}\rightarrow4_{\rm adaptive}}.
\]

On the 114 generating states, the minimum total depth-four state-path length is
382, hence

\[
\boxed{\bar D_{\min}=\frac{191}{57}\approx3.350877}.
\]

Standard Nielsen moves produce four connected components of sizes

\[
\boxed{36,\ 32,\ 32,\ 14}.
\]

These components are exactly the fibers of the canonical commutator-lift trace

\[
\tau(A,B)=\operatorname{tr}([\widetilde A,\widetilde B])\in\mathbb F_7
\]

with values \(6,4,3,5\), connecting the finite H18 decomposition with the
classical Higman invariant.

Three projective shadow observations,

\[
A^2B^2,\qquad ABAB^{-1},\qquad ABA^{-1}B,
\]

reconstruct \(\tau\) on the generating locus, and three is minimal among the
\(W_4\) class observers.

Under one persistent known query erasure, four successful class answers still
suffice:

\[
\boxed{S_1=4,\qquad A_1=5}.
\]

Nielsen structure then compresses the global query vocabulary: first
\(50\to26\), and then a 12-query alphabet is found that preserves the complete
one-erasure contract. An exact lower bound gives

\[
\boxed{9\le M_1(W_4)\le12},
\]

where \(M_1(W_4)\) is the minimum number of globally supported query labels
needed to retain the exact four-successful-answer one-erasure strategy.

Deterministic rematerialization of the restricted 12-query strategy reduces
the query-state count

\[
308\to305
\]

and the explicit microprogram payload

\[
19057\to18425\text{ bits}.
\]

Exact shortest-program analysis also shows that Nielsen semantic compression
does not automatically reduce permutation-composition count: several primitive
queries are cheaper when executed directly.

Two hardware realizations of the same restricted-12 H18 mathematics expose a
strong area/time tradeoff.  The temporal H18-LAB-03 realization on
5CEFA7F23C6 uses 1,455 ALMs + 26 DSP blocks and reaches
\(F_{\max}=47.02\) MHz, but requires up to 42 cycles.  The fully spatialized
H18-LAB-04 uses 10,627 ALMs + 48 DSP blocks and reaches
\(F_{\max}=28.52\) MHz with a one-cycle result.  At measured Fmax this is
approximately \(0.893\,\mu s\) versus \(0.0351\,\mu s\): spatialization costs
about 7.30x ALMs while reducing worst transaction latency by about 25.5x.

A matched one-cycle comparison with H17-LAB-02 on the same Cyclone V gives
7,941 ALMs + 40 DSP blocks and 35.694 ns for H17 versus
10,627 ALMs + 48 DSP blocks and 34.827 ns for H18.  On the large Cyclone IV
EP4CE115F29C7, the two one-cycle designs both report 65 logic levels and nearly
equal selected worst data delays, 47.249 ns and 46.516 ns.

These measurements motivate a separate H18-12 framework:

\[
\boxed{
\text{mathematical presentation}
\to
\text{Boolean realization}
\to
\text{technology-relative hardware image}.
}
\]

The FPGA is used here as a reproducible physical transformation for comparing
finite mathematical presentations, not as a proof of absolute mathematical
complexity.

## 1. Problem formulation

H17 uses a fixed robust fingerprint. H18 asks whether the next word can be
chosen from the answers already observed:

\[
w_1\rightarrow c_1\rightarrow w_2(c_1)\rightarrow c_2\rightarrow\cdots.
\]

The fixed code becomes a branching interrogation program.

Three complexity measures are kept separate:

1. **transaction complexity** — answers required on one path;
2. **query-alphabet complexity** — distinct query labels supported globally;
3. **hardware realization complexity** — controller memory, arithmetic, logic,
   routing, and latency.

## 2. Finite model

Let

\[
G=PSL(2,7),\qquad |G|=168.
\]

For \((A,B)\in G^2\), use simultaneous conjugacy

\[
(A,B)\sim(hAh^{-1},hBh^{-1}).
\]

Generating pairs form 114 orbits. The full quotient of ordered pairs contains

\[
\boxed{197=114+83}
\]

orbits, with the 83 non-generating states sharing terminal REJECT.

For freely reduced words of lengths \(1,\ldots,4\),

\[
4+12+36+108=160
\]

raw words occur. Exact response-vector deduplication leaves

\[
\boxed{50}
\]

distinct \(W_4\) class queries.

## 3. Exact adaptive depth four

Exact dynamic programming proves

\[
\boxed{D^*(W_4)=4}.
\]

Depth three is impossible and depth four is sufficient.

No fixed subset of sizes \(1,2,3,4\) separates all 114 generating states.
The five words

\[
\boxed{A,\ B,\ AB,\ Ab,\ ABab}
\]

do, so

\[
\boxed{5_{\rm fixed}\rightarrow4_{\rm adaptive}}.
\]

Among depth-four trees, the minimum total state-path length is \(382\), hence

\[
\boxed{\bar D_{\min}=382/114=191/57}.
\]

One selected optimum has 48 internal nodes, root \(\texttt{AAB}\), with 74
states terminating at depth three and 40 at depth four.

## 4. Nielsen dynamics

Consider standard Nielsen moves including

\[
S(A,B)=(B,A),\qquad
I_A(A,B)=(A^{-1},B),\qquad
N_A(A,B)=(AB,B).
\]

On the 114 generating orbit states, the induced graph has connected components

\[
\boxed{36,\ 32,\ 32,\ 14}
\]

with diameters

\[
\boxed{7,\ 6,\ 8,\ 4}.
\]

Their projective commutator classes are \(3A\), \(4A\), \(4A\), and
\(7A/7B\), respectively. Projective commutator class alone does not distinguish
the two 32-state sectors.

## 5. Canonical lift trace and the Higman invariant [1,9]

Choose determinant-one lifts

\[
\widetilde A,\widetilde B\in SL(2,7).
\]

The commutator lift is independent of the lift signs, so

\[
\boxed{
\tau(A,B)=\operatorname{tr}([\widetilde A,\widetilde B])
}
\]

is well-defined on the projective pair.

The exact fibers on the 114 states are

\[
\boxed{
\tau=6:36,\qquad
\tau=4:32,\qquad
\tau=3:32,\qquad
\tau=5:14.
}
\]

Each fiber is exactly one Nielsen connected component. In particular,

\[
\boxed{
4A^{(+)}:\tau=3,\qquad
4A^{(-)}:\tau=4=-3\pmod7.
}
\]

H18 does not claim discovery of the Higman invariant.  Classically, the
Higman invariant is formulated through the conjugacy classes of the commutator
and its inverse; the quantity \(\tau\) used here is the canonical
determinant-one commutator-lift trace.  The H18 result is the exact finite
identification of its trace fibers with the Nielsen components in the H17/H18
state model, together with the connection of this trace invariant to the
adaptive query structure.

## 6. Three-shadow reconstruction theorem

Put

\[
x=\operatorname{tr}\widetilde A,\qquad
y=\operatorname{tr}\widetilde B,\qquad
z=\operatorname{tr}(\widetilde A\widetilde B).
\]

Fricke's identity [1,9] is

\[
\tau=x^2+y^2+z^2-xyz-2.
\]

Define

\[
R_z=A^2B^2,\qquad
R_x=ABAB^{-1},\qquad
R_y=ABA^{-1}B.
\]

Then

\[
\operatorname{tr}(R_z)=z^2-\tau,
\]

\[
\operatorname{tr}(R_x)=x^2-\tau,
\]

\[
\operatorname{tr}(R_y)=y^2-\tau.
\]

Projective conjugacy class determines the squared trace of a lift. Therefore
the three shadow classes reconstruct \(\tau\) on the generating locus.

Exact search over all 50 \(W_4\) queries gives

\[
\boxed{m_\tau(W_4)=3}.
\]

No single query or pair determines \(\tau\), whereas exactly 16 triples do.

## 7. Persistent known query erasure

The fault model allows at most one requested query to return ERASED. Its
identity is known, the failed query is unavailable for the remainder of the
transaction, and it may not be repeated.

For the full 197-state identify-or-REJECT task,

\[
\boxed{D_0=4}
\]

without erasure and

\[
\boxed{S_1=4}
\]

successful answers under one persistent erasure. Therefore

\[
\boxed{A_1=5}.
\]

Three successful answers are already impossible without erasure, so the
successful-query bound is exact.

## 8. First RTL realization

H18-07 materializes the exact strategy as sequential RTL with

\[
308=69+239
\]

nonterminal query states, 24 distinct query labels, maximum word length four,
one shared word datapath, and one reused class engine.

The verified regression is

\[
\boxed{197\times5=985/985\ \mathrm{PASS}}.
\]

Observed maxima are

\[
\boxed{\text{max attempts}=5,\qquad \text{max RTL wait}=32\text{ cycles}}.
\]

Under one common generic Yosys methodology,

\[
H17\text{-LAB-03}=13547,
\qquad
H18\text{-LAB-01}=17205
\]

hierarchy-expanded generic cells. The first hardwired adaptive implementation
is about 27% larger than the H17 reference. This is an implementation result,
not a general theorem about the cost of adaptivity.

## 9. Canonical microcoded baseline

H18-08 replaces hardwired decode by a canonical microprogram.

Its baseline payload is

\[
1540+16632+621+264
=
\boxed{19057\text{ bits}}.
\]

Direct loading of the first word letter also reduces the worst five-attempt
arithmetic bound

\[
19\rightarrow14
\]

permutation compositions without changing the decision strategy.

H18-08 remains the baseline 24-query architecture and must close through its
own dual-RTL CI evidence.

## 10. Nielsen-normal query compression

Exactly 24 of the 50 canonical \(W_4\) queries are primitive free-group words,
hence Nielsen transports of a coordinate observer.

On the 114 generating states their joint signature has 107 values and leaves
exactly seven doublets:

\[
\boxed{
(12,27),(13,28),(14,29),(84,89),(90,92),(100,103),(106,107).
}
\]

These are precisely the H17 commutator-defect pairs.

All seven are separated by the oriented commutator query \(\texttt{ABab}\).
The natural restricted pool is therefore

\[
\boxed{
24\text{ primitive}+2\text{ commutator orientations}=26.
}
\]

On this pool,

\[
\boxed{D_0=4,\qquad S_1=4,\qquad A_1=5}
\]

and

\[
\boxed{5_{\rm fixed}\rightarrow4_{\rm adaptive}}
\]

remain unchanged.

The generating-only optimum total path length changes only

\[
382\rightarrow386,
\]

so mean depth changes from \(191/57\) to \(193/57\), with worst-case depth
still four.

## 11. Global query alphabet

Let \(M_1(W_4)\) denote the minimum number of globally supported query labels
that retain the exact four-successful-answer one-erasure strategy.

Any alphabet tolerating one persistent query erasure must have distance at
least two on every required generating/generating and generating/non-generating
pair.

In the full 50-query pool, exactly seven critical pairs have only two
separating labels:

\[
\boxed{\texttt{ABab},\qquad\texttt{AbaB}}.
\]

Thus both commutator orientations are forced.

After fixing them, a size-eight alphabet could add only six of the remaining
48 labels. Exhaustive checking of

\[
\binom{48}{6}=12\,271\,512
\]

completions proves that none satisfies the necessary distance-two condition.

A size-nine distance-two witness exists. For the full adaptive contract, the
following 12-query witness suffices:

\[
\boxed{
A,B,ABab,AbaB,ABB,Abb,AAb,AAAB,AAAb,Baa,aab,abb.
}
\]

Exact DP on this alphabet gives again

\[
\boxed{D_0=4,\qquad S_1=4,\qquad A_1=5}.
\]

Hence

\[
\boxed{9\le M_1(W_4)\le12}.
\]

## 12. Restricted 12-query controller

Rematerializing the exact controller under the 12-query alphabet gives

\[
\boxed{305=67+238}
\]

nonterminal query nodes instead of

\[
308=69+239.
\]

All 12 labels are used by the selected deterministic strategy.

With a canonical 9-bit node address and a 4-bit query selector, the explicit
payload is

\[
305\times4=1220
\]

query-selector bits,

\[
305\times6\times9=16470
\]

class-transition bits,

\[
67\times9=603
\]

erasure-transition bits, and

\[
12\times11=132
\]

word-descriptor bits.

Total:

\[
\boxed{18425\text{ bits}}.
\]

Relative to H18-08,

\[
\boxed{
19057\rightarrow18425
}
\]

or

\[
\boxed{-632\text{ bits}=-3.32\%}.
\]

The query vocabulary is halved, but the overall payload falls only modestly
because the dominant term is the six-way transition table.

## 13. Nielsen semantic compression is not arithmetic compression

Shortest elementary Nielsen programs were computed for the ten primitive
labels in the 12-query witness.

For seven labels, shortest Nielsen cost equals direct \(L-1\) permutation
composition cost. For three labels, Nielsen execution requires one additional
move.

Therefore

\[
\boxed{
\text{Nielsen semantic compression}
\not\Rightarrow
\text{automatic arithmetic compression}.
}
\]

The next hardware optimization must therefore attack controller/transition
structure rather than assume a faster word datapath from Nielsen equivalence
alone.

## 14. Main structural conclusion

The H18 query language contracts as

\[
50\text{ canonical }W_4\text{ queries}
\]

\[
\Downarrow
\]

\[
24\text{ primitive Nielsen transports}
+
2\text{ commutator orientations}
\]

\[
\Downarrow
\]

\[
12\text{-label adaptive witness},
\]

while preserving the exact worst-case information bound

\[
\boxed{
4\text{ successful answers}
+
1\text{ possible erasure}.
}
\]

Adaptive tomography and Nielsen dynamics are therefore not separate themes:
the dynamics explains how the interrogation language can be organized and
compressed.  Hardware realization adds a second distinction: semantic
compression and physical circuit compression are not the same problem.

## 15. Two hardware realizations of one H18 mathematics

### 15.1 H18-LAB-03: temporal microcoded realization

LAB-03 uses one reused word engine, one reused class engine, microcoded
transitions, and sequential execution of only those observers actually reached
by the adaptive strategy.

Exhaustive ModelSim regression verifies

\[
\boxed{197\times5=985\text{ transactions}}
\]

with

\[
\boxed{\max\text{ attempts}=5,\qquad\max\text{ RTL cycles}=42}.
\]

On Cyclone IV EP4CE22F17C6 it uses

\[
\boxed{5227/22320\text{ LE}=23\%}
\]

with \(F_{\max}=41.28\) MHz, 24.510 ns selected worst data delay, and 42
reported logic levels.

On Cyclone V 5CEFA7F23C6 it uses

\[
\boxed{1455/56480\text{ ALMs}=3\%},
\]

211 registers and 26/156 DSP blocks.  Slow 1100 mV / 85 C timing gives

\[
\boxed{F_{\max}=47.02\text{ MHz}},
\]

with selected worst path

\[
\texttt{class\_perm[23]}\to\texttt{next\_node\_q[4]},
\]

data delay 21.075 ns, 18 logic levels, 10.227 ns cell delay and 10.850 ns
routing delay.

### 15.2 H18-LAB-04: fully spatialized combinational realization

LAB-04 keeps the restricted-12 mathematics but eliminates sequential query
execution:

\[
\boxed{
\text{registered inputs}
\to
\text{12 parallel observers}
\to
\text{compiled 305-node decision DAG}
\to
\text{registered result}.
}
\]

The shared word-prefix DAG contains 19 permutation compositions with maximum
composition depth three.

Its static erased-query identity implements the persistent known-query-erasure
semantics by consulting the erased identity only when the pre-erasure strategy
actually reaches that query.

Exhaustive regression covers

\[
\boxed{197\times13=2561}
\]

registered transactions: no erasure and each of the 12 possible erased query
identities.

This static-identity enumeration must not be called strictly stronger than the
LAB-03 temporal schedule regression; the fault representations differ.

### 15.3 Spatialization cost on Cyclone V

The same H18-11 mathematics is now measured under both temporal and spatial
execution disciplines on 5CEFA7F23C6:

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

At the measured Fmax values,

\[
T_{\rm temporal}
=
\frac{42}{47.02\text{ MHz}}
\approx0.893\,\mu s,
\]

\[
T_{\rm spatial}
=
\frac{1}{28.52\text{ MHz}}
\approx0.0351\,\mu s.
\]

Thus full spatialization costs approximately

\[
\boxed{7.30\times}
\]

in ALM usage while reducing worst transaction latency by approximately

\[
\boxed{25.5\times}.
\]

This is the clean same-mathematics architecture control of H18-12.

It also shows why \(F_{\max}\) alone is not a transaction-speed metric: the
temporal design has the higher Fmax and shorter one-cycle critical path, yet
the 42-cycle schedule gives much larger end-to-end latency.

## 16. H17 versus H18: two mathematical presentations

The H17 construction and hardware baselines used here are archived in the
programme repository [10].

### 16.1 Equivalence boundary

H17 and H18 must not be described as two bit-identical fault-tolerant RTL
implementations.

In the fault-free layer, both identify the same simultaneous-conjugacy orbit of
the ordered pair \((A,B)\), with REJECT for non-generating pairs.

In the fault-tolerant layer, H17 uses a fixed robust fingerprint with one known
erased coordinate, whereas H18 uses adaptive word queries with one persistent
known query erasure.

Hence the fault-tolerant comparison is

\[
\boxed{\mathrm{E1}:\ \text{common abstract correctness contract}},
\]

while the fault-free layer admits the stronger E0 pointwise comparison.

To isolate the mathematical-presentation effect, use the same execution
discipline:

\[
\boxed{
\text{registered input}
\to
\text{combinational mathematical core}
\to
\text{registered output}.
}
\]

This compares H17-LAB-02 with H18-LAB-04.

### 16.2 Cyclone IV EP4CE22F17C6: capacity boundary

H17-LAB-02 fits at

\[
19540/22320\text{ LE}=88\%.
\]

H18-LAB-04 requires

\[
26332/22320\text{ LE}=118\%
\]

and does not fit.

Thus the same-target mapping-demand ratio is approximately

\[
\boxed{26332/19540\approx1.348}.
\]

This is a density result only; H18 has no routed timing on this target.

### 16.3 Cyclone IV EP4CE115F29C7: matched timing

Both one-cycle designs route successfully on the larger C7 target.

| quantity | H17-LAB-02 | H18-LAB-04 |
| --- | ---: | ---: |
| selected worst data delay | 47.249 ns | 46.516 ns |
| logic levels | 65 | 65 |
| cell delay | 17.092 ns | 15.721 ns |
| routing delay | 29.941 ns | 30.579 ns |
| reciprocal data-delay frequency | 21.16 MHz | 21.50 MHz |

The total selected delays are nearly equal and both paths contain 65 reported
logic levels, but the internal delay decomposition differs.

The H18 MAP report additionally gives

\[
\boxed{26460\text{ logic elements}}
\]

and 69 registers.  This value is explicitly reported as a **MAP estimate**, not
as final fitter utilization, because the archived extractor output does not
contain a separate final-fit utilization line.

### 16.4 Cyclone V 5CEFA7F23C6: second matched technology point

Cyclone V uses inferred hard DSP blocks, so this is a platform-level ALM+DSP
comparison rather than an ALM-only comparison.

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

Thus H18 uses approximately 33.8% more ALMs and 20% more DSP blocks, while the
selected worst data delay is about 2.4% shorter and the reported logic depth is
about 11.8% smaller.

Neither presentation Pareto-dominates the other on the full physical vector.

The closeness of the Cyclone-IV mapping-demand ratio \(1.348\) and the
Cyclone-V fitted ALM ratio \(1.338\) is an empirical regularity only, not an
invariant.

## 17. H18-12: hardware image of a mathematical presentation

Let a finite task be

\[
\Phi:X\to Y
\]

or, under a fault model, a correctness relation

\[
\mathcal R\subseteq X\times F\times Y.
\]

Let \(M\) be a finite mathematical presentation: carriers, primitive
operations, and an explicit factorization/decision program.

After finite injective encoding of each carrier, every primitive operation has
an exact Boolean realization.  Therefore one may write

\[
\boxed{
M\xrightarrow{\mathcal B_\Pi}C_M,
}
\]

where \(\Pi\) fixes the realization discipline: permitted rewrites, sharing,
register boundaries, temporal reuse, spatialization, and fault encoding.

Fix also a technology stack

\[
\Theta=
(\text{device, speed grade, tool, settings, constraints, corner}),
\]

and physical profile

\[
P_\Theta(C)=
(A,R,M,DSP,d_{\rm logic},
t_{\rm cell},t_{\rm route},F_{\max},N_{\rm cyc},T_{\rm tx},\ldots).
\]

### 17.1 Presentation hardware image

Define

\[
\boxed{
H_{\Theta,\Pi}(M)
=
\operatorname{ParetoMin}
\{P_\Theta(C):C\in\mathscr C_\Pi(M)\}.
}
\]

A concrete Quartus run produces only a reproducible witness

\[
\widehat H_{\Theta,\Pi,S}(M),
\]

not automatically the optimum.

### 17.2 Presentation complexity and task complexity are different

If synthesis is allowed to forget the internal mathematics and optimize only
the flattened truth table, two distinct presentations may become
indistinguishable.

Therefore the presentation hardware image must be separated from the semantic
frontier

\[
H_\Theta^*(\Phi).
\]

In general,

\[
\boxed{
H_{\Theta,\Pi}(M)\ne H_\Theta^*(\Phi).
}
\]

### 17.3 Three independent experimental effects

The methodology separates:

\[
\boxed{\text{mathematics effect}}
\]

— vary \(M\), hold \(\Pi,\Theta\) fixed;

\[
\boxed{\text{architecture effect}}
\]

— vary \(\Pi\), hold \(M,\Theta\) fixed;

\[
\boxed{\text{technology effect}}
\]

— vary \(\Theta\), hold \(M,\Pi\) fixed.

The present HATTER controls are:

- mathematics: H17-LAB-02 vs H18-LAB-04;
- architecture: H18-LAB-03 vs H18-LAB-04;
- technology: Cyclone IV vs Cyclone V.

This yields the experimental chain

\[
\boxed{
\text{mathematics}
\to
\text{Boolean geometry}
\to
\text{physical geometry}.
}
\]

No claim is made that FPGA measurements directly equal absolute mathematical
complexity.

## 18. Waveform evidence

A dedicated H18-LAB-04 ModelSim scenario evaluates the same certified pair
twice:

\[
A=\texttt{0x5e3b88},
\qquad
B=\texttt{0x7ecc11},
\]

with expected orbit 0.

The restricted-12 root query is

\[
\texttt{AAAB}
\]

with local hardware word ID 8 and response class 2 for the selected state.

Without erasure, root follows ordinary child node 16.

With

\[
\texttt{erase\_valid}=1,
\qquad
\texttt{erased\_word\_id}=8,
\]

root follows erasure child node 233.

Both branches return

\[
\texttt{node\_result}=0x100,
\]

corresponding to

\[
\texttt{status}=2=\mathrm{IDENTIFIED},
\qquad
\texttt{orbit\_id}=0.
\]

Because LAB-04 is fully spatialized, the two alternative adaptive futures exist
simultaneously as combinational branches; root logic selects one of them.

This waveform is therefore a visual witness of

\[
\boxed{
\text{same input}
\to
\text{different decision branch}
\to
\text{same certified orbit}.
}
\]

It is not a post-fit propagation-delay measurement.

## 19. Claim boundaries

Certified or directly verified:

- exact finite state counts;
- exact adaptive depth four;
- strict fixed/adaptive separation;
- exact Nielsen component decomposition;
- identification with canonical commutator-lift trace fibers;
- three-shadow reconstruction and \(m_\tau(W_4)=3\);
- exact persistent-one-erasure bound;
- restricted 12-query controller and 18,425-bit program;
- H18-LAB-03 temporal RTL regression and Cyclone-IV/Cyclone-V physical runs;
- H18-LAB-04 static-erased-identity regression and tested FPGA runs;
- matched H17/H18 one-cycle comparisons on Cyclone IV and Cyclone V;
- same-mathematics H18 temporal/spatial architecture control;
- exact shortest Nielsen programs for the ten primitive labels.

Not claimed:

- a theorem for all \(PSL(2,q)\);
- exact \(M_1(W_4)\) before exhaustive closure;
- cryptographic hardness;
- arbitrary transient hardware-fault tolerance;
- global minimum FPGA area or delay;
- technology-independent superiority of either mathematics;
- equality of FPGA area with mathematical complexity;
- ALM-only interpretation of Cyclone-V results, because DSP blocks are used.

## 20. Reproducibility

Principal certificates:

- `h18_adaptive_depth4_certificate.py`;
- `h18_nielsen_dynamics_certificate.py`;
- `h18_higman_trace_lift_certificate.py`;
- `h18_adaptive_with_tau_certificate.py`;
- `h18_three_shadow_higman_decoder.py`;
- `h18_adaptive_one_erasure_certificate.py`;
- `h18_nielsen_query_compression_certificate.py`;
- `h18_query_alphabet_compression_certificate.py`;
- `h18_restricted12_controller_certificate.py`.

Hardware layers:

- H18-LAB-01 — first hardwired adaptive RTL;
- H18-LAB-02 — canonical 24-query microcoded baseline;
- H18-LAB-03 — restricted-12 temporal target-FPGA realization;
- H18-LAB-04 — restricted-12 fully spatialized combinational realization.

Comparison framework:

- `H18_12_ALGEBRA_TO_PHYSICAL_COMPLEXITY.md`;
- `H18_12_MATHEMATICS_COMPARISON_PROTOCOL.md`;
- `H18_13_H17_H18_COMMON_CONTRACT.md`;
- `PUBLICATION_AUDIT_2026-09-19.md`.

## 21. Literature boundary

Classical Nielsen equivalence, commutator-trace methods, Fricke identities,
and the Higman invariant predate H18 [1,9].  For related generating-pair and
lifting questions in projective special linear groups, see also [2].

Within this manuscript, the H18 contribution is the exact finite integration

\[
\boxed{
\text{Nielsen dynamics}
\leftrightarrow
\text{adaptive word tomography}
\leftrightarrow
\text{Fricke/Higman reconstruction}
\leftrightarrow
\text{query-language compression}
\leftrightarrow
\text{hardware realization}.
}
\]

The hardware-image framework is adjacent to straight-line program and relative
algebraic complexity [3,4], algebraic implementation complexity [5], VLSI
area-time complexity [6], FPGA LUT technology mapping [7], and circuits over
finite algebraic structures [8].  No priority claim over those fields, or over
the general idea of connecting algebraic and hardware complexity, is made.

## 22. Publication freeze

The mathematical, claim-discipline, bibliography, and reproducibility audit was
completed on 19 September 2026.

The freeze includes:

- exact finite H18-01--H18-11 claims within their explicitly stated finite
  models;
- H18-LAB-03/LAB-04 physical evidence on the declared FPGA targets;
- the H17/H18 E0/E1 comparison boundary from H18-13;
- the H18-12 hardware-image construction as a **framework/methodology**, not as
  a technology-independent complexity theorem.

The following remain open **without blocking this publication**:

- the exact value \(M_1(W_4)\in\{9,10,11,12\}\);
- further technology points and DSP-disabled controls;
- provable Boolean/circuit lower bounds;
- a separate final-fit utilization line for the 115K H18 run, if later needed;
  the current \(26{,}460\) value remains a MAP estimate only.

**Release status:** `PUBLICATION_READY_PENDING_RENDER_AUDIT`.

## References

1. Darryl McCullough, Marcus Wanderley, *Nielsen Equivalence of Generating
   Pairs of SL(2,q)*, **Glasgow Mathematical Journal** 55(3) (2013),
   481–509. DOI: 10.1017/S0017089512000675.

2. Jan Boschheidgen, Benjamin Klopsch, Anitha Thillaisundaram, *Generating
   pairs of projective special linear groups that fail to lift*,
   **Mathematische Nachrichten** 293(7) (2020), 1251–1258.
   DOI: 10.1002/mana.201900354.

3. Nancy A. Lynch, *Straight-line program length as a parameter for complexity
   analysis*, **Journal of Computer and System Sciences** 21(3) (1980),
   251–280. DOI: 10.1016/0022-0000(80)90024-0.

4. Nancy A. Lynch, Edward K. Blum, *Relative Complexity of Algebras*,
   **Mathematical Systems Theory** 14 (1981), 193–214.
   DOI: 10.1007/BF01752396.

5. Hartmut Ehrig, Bernd Mahr, *Complexity of algebraic implementations for
   abstract data types*, **Journal of Computer and System Sciences** 23(2)
   (1981), 223–253. DOI: 10.1016/0022-0000(81)90014-3.

6. C. D. Thompson, *Area-Time Complexity for VLSI*, in **Proceedings of the
   11th Annual ACM Symposium on Theory of Computing (STOC '79)** (1979),
   81–88. DOI: 10.1145/800135.804401.

7. Jason Cong, Yuzheng Ding, *FlowMap: An Optimal Technology Mapping Algorithm
   for Delay Optimization in Lookup-Table Based FPGA Designs*,
   **IEEE Transactions on Computer-Aided Design of Integrated Circuits and
   Systems** 13(1) (1994), 1–12. DOI: 10.1109/43.273754.

8. Piotr Kawałek, Jacek Krzaczkowski, *Complexity Classes Arising from Circuits
   over Finite Algebraic Structures*, in **41st Annual Symposium on Logic in
   Computer Science (LICS 2026)**, LIPIcs 380 (2026), 61:1–61:26.
   DOI: 10.4230/LIPIcs.LICS.2026.61.

9. A. M. Macbeath, *Generators of the linear fractional groups*, in
   **Number Theory (Houston, 1967)**, Proceedings of Symposia in Pure
   Mathematics 12, American Mathematical Society (1969), 14–32.
   DOI: 10.1090/pspum/012/0262379.

10. Alex Malachevsky (with Commander Sol as AI research collaborator), **HATTER-SOL-17 ·
    Non-Abelian Tomography Hardware**, repository
    `AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol`,
    `papers/HATTER-SOL/17-NONABELIAN-TOMOGRAPHY-HARDWARE/`,
    branch `research/hatter-sol-17-nonabelian-tomography-hardware`.
