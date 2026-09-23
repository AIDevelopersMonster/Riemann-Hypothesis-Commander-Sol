# HATTER-SOL-18 · Publication audit checkpoint

Date: 19 September 2026.

Status: **PRE-FREEZE AUDIT — hardware evidence integrated, two physical coordinates pending local extraction/run**

## 1. Mathematical claims currently supported

The following claims are backed by exact finite certificates or exhaustive
finite computation already present in the branch:

- 197-state simultaneous-conjugacy quotient:
  114 generating + 83 non-generating states;
- 160 freely reduced words of length at most four induce 50 distinct
  class-valued queries;
- exact adaptive worst-case depth \(D^*(W_4)=4\);
- fixed/adaptive separation \(5_{\rm fixed}\to4_{\rm adaptive}\);
- minimum generating-state total depth 382 and mean \(191/57\);
- Nielsen connected components \(36,32,32,14\);
- exact coincidence of those components with canonical commutator-lift trace
  fibers;
- three-shadow recovery of the Higman/commutator trace and
  \(m_\tau(W_4)=3\);
- one persistent known query erasure:
  \(D_0=4,\ S_1=4,\ A_1=5\);
- restricted robust alphabet bound \(9\le M_1(W_4)\le12\);
- 12-query witness and 305-node restricted controller;
- exact explicit microprogram payload 18,425 bits;
- shortest Nielsen-program/direct-composition comparison for the ten primitive
  labels.

No theorem is claimed for general \(PSL(2,q)\), and \(M_1(W_4)\) is not yet
claimed to equal 9, 10, 11, or 12.

## 2. Implementation claims currently supported

### H18-LAB-03

Exhaustive ModelSim regression:

\[
197\times5=985
\]

transactions, with verified maxima

\[
\text{attempts}=5,\qquad \text{RTL cycles}=42.
\]

Cyclone IV EP4CE22F17C6 physical result:

- 5,227 / 22,320 LE;
- 211 registers;
- no inferred memory;
- \(F_{\max}=41.28\) MHz at Slow 1200 mV / 85 C;
- 24.510 ns worst data delay;
- 42 reported logic levels.

The 42-cycle transaction bound means this design is not to be described as
"faster" than a one-cycle implementation merely because its single-cycle
Fmax is higher.

### H18-LAB-04

Exhaustive static-erased-identity regression:

\[
197\times13=2561
\]

transactions.

This is exhaustive over the static fault identities used by LAB-04.  It must
not be labelled strictly stronger than the temporal LAB-03 schedule test
without a formal semantic inclusion theorem.

Cyclone IV EP4CE22F17C6:

- mapped demand 26,332 logic elements;
- target capacity 22,320;
- Fitter NO FIT;
- therefore no routed timing claim.

Cyclone IV EP4CE115F29C7:

- routed worst data delay 46.516 ns;
- 65 reported logic levels;
- 15.721 ns cell delay;
- 30.579 ns routing delay.

The existing local report extractor gives 26,460 logic elements and 69
registers at MAP stage.  This value is retained as a MAP estimate only; no
separate final-fit utilization value is inferred from it.

Cyclone V 5CEFA7F23C6:

- 10,627 / 56,480 ALMs;
- 69 registers;
- 48 / 156 DSP blocks;
- \(F_{\max}=28.52\) MHz;
- 34.827 ns worst data delay;
- 30 logic levels;
- 13.556 ns cell delay;
- 21.270 ns routing delay.

Cyclone V is a platform-level ALM+DSP comparison.  Do not present it as an
ALM-only implementation.

## 3. H17/H18 comparison boundary

The fault-free orbit-identification layer is E0:

\[
\Phi_{17,0}=\Phi_{18,0}.
\]

The fault-tolerant comparison is E1:

\[
\mathcal R_{17}\sim_{\rm contract}\mathcal R_{18},
\]

not raw bit-level equality, because H17 faults erase one coordinate of a fixed
fingerprint while H18 faults remove one adaptive query identity.

The clean one-cycle mathematics-effect experiment is:

\[
H17\text{-LAB-02}\leftrightarrow H18\text{-LAB-04}.
\]

The clean same-mathematics architecture-effect experiment is:

\[
H18\text{-LAB-03}\leftrightarrow H18\text{-LAB-04}.
\]

## 4. Matched one-cycle evidence

### Cyclone IV large C7

H17/H18 selected worst data delays:

\[
47.249\text{ ns}\leftrightarrow46.516\text{ ns}.
\]

Both report 65 logic levels.

This supports a statement about close matched physical delay with different
internal delay decomposition.  It does not support an absolute complexity
equivalence.

### Cyclone V C6

H17:

\[
7941\text{ ALM}+40\text{ DSP},\quad35.694\text{ ns},\quad34\text{ levels}.
\]

H18:

\[
10627\text{ ALM}+48\text{ DSP},\quad34.827\text{ ns},\quad30\text{ levels}.
\]

Hence the measured H18/H17 ratios are approximately:

\[
\rho_A=1.338,\quad
\rho_{\rm DSP}=1.200,\quad
\rho_T=0.976,\quad
\rho_d=0.882.
\]

This is a genuine Pareto tradeoff: H18 spends more spatial/hard-block
resources while producing a slightly shorter and shallower selected critical
path.


## 4A. Same-mathematics architecture control — Cyclone V

H18-LAB-03 and H18-LAB-04 share the same restricted-12 H18-11 mathematical
certificate and differ principally in temporal versus spatial execution.

Measured 5CEFA7F23C6 result:

\[
\begin{array}{c|cc}
& \mathrm{LAB03\ temporal} & \mathrm{LAB04\ spatial}\\
\hline
\mathrm{ALM} & 1455 & 10627\\
\mathrm{DSP} & 26 & 48\\
F_{\max} & 47.02\ \mathrm{MHz} & 28.52\ \mathrm{MHz}\\
\mathrm{data\ delay} & 21.075\ \mathrm{ns} & 34.827\ \mathrm{ns}\\
\mathrm{logic\ levels} & 18 & 30\\
N_{\rm cyc} & 42 & 1
\end{array}
\]

At measured Fmax the worst transaction times are approximately 0.893 us and
0.0351 us respectively.

Hence full spatialization costs approximately 7.30x ALMs while reducing
worst transaction latency approximately 25.5x.

This is now the principal architecture-effect control in H18-12.

## 5. H18-12 theory claim boundary

The proposed map

\[
M\to\mathcal B_\Pi(M)\to P_\Theta(M)
\]

is a formal framework for comparing technology-relative hardware images of
finite mathematical presentations.

At publication time it should be described as:

- a definition/framework;
- a controlled experimental methodology;
- an empirically supported research program.

It should **not** yet be described as:

- a universal complexity theory;
- a technology-independent invariant;
- a proof that FPGA area equals mathematical complexity;
- a proof of global circuit optimality.

## 6. Waveform claim boundary

The canonical H18-LAB-04 waveform uses one certified pair twice.

Normal transaction:

\[
AAAB\to\text{node }16.
\]

Root-query-erasure transaction:

\[
AAAB\text{ erased}\to\text{node }233.
\]

Both return IDENTIFIED / orbit 0.

Because LAB-04 is fully spatialized, the waveform is best interpreted as a
visual witness that mutually exclusive adaptive futures are represented by
simultaneously existing combinational branches and selected by logic.  It is
not a propagation-delay measurement of the post-fit FPGA.

## 7. Remaining publication gates

The immediate hardware matrix is now closed for the intended manuscript:

- H17-LAB-02 spatial: Cyclone IV and Cyclone V;
- H18-LAB-04 spatial: Cyclone IV and Cyclone V;
- H18-LAB-03 temporal: Cyclone IV and Cyclone V.

The EP4CE115F29C7 H18 value 26,460 remains explicitly labelled MAP estimate
until a separate final-fit utilization line is archived.

Remaining gates are now editorial/theoretical rather than required physical
measurements:

1. final bibliography verification;
2. final claim/non-claim consistency pass;
3. EN v0.3 synchronization with RU v0.3;
4. optional exact closure of (M_1(W_4)in{9,10,11,12}) if completed before
   publication freeze;
5. final RU/EN PDF assembly.
