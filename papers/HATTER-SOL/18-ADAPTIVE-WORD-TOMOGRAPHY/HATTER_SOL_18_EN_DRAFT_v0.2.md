# HATTER-SOL-18
# Adaptive Non-Abelian Tomography: Nielsen Dynamics, Higman Trace, and Query-Language Compression

**Status:** publication working draft EN v0.2  
**Branch:** \`research/hatter-sol-18-adaptive-word-tomography\`  
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

## 5. Canonical lift trace and the Higman invariant

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

H18 does not claim discovery of the Higman invariant; the new result is its
exact identification inside the H17/H18 state model and its connection to the
adaptive query structure.

## 6. Three-shadow reconstruction theorem

Put

\[
x=\operatorname{tr}\widetilde A,\qquad
y=\operatorname{tr}\widetilde B,\qquad
z=\operatorname{tr}(\widetilde A\widetilde B).
\]

Fricke's identity is

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
the dynamics explains how the language of the interrogation program can be
organized and compressed.

## 15. Claim boundaries

Certified or directly verified:

- exact finite state counts;
- exact adaptive depth four;
- strict fixed/adaptive separation;
- exact Nielsen component decomposition;
- identification with Higman trace fibers;
- three-shadow reconstruction and \(m_\tau(W_4)=3\);
- exact persistent-one-erasure bound;
- H18-07 RTL regression;
- generic H17/H18 synthesis comparison;
- 26-query Nielsen-normal reduction;
- \(9\le M_1(W_4)\le12\);
- 305-node restricted controller;
- explicit 18,425-bit restricted program count;
- exact shortest Nielsen programs for the ten primitive labels.

Not claimed:

- a theorem for all \(PSL(2,q)\);
- exact \(M_1\) before separate exhaustive closure;
- cryptographic hardness;
- physical fault tolerance;
- target-FPGA superiority of H18 over H17;
- lower LUT/ALM/BRAM/Fmax/power for the 12-query architecture before target
  synthesis.

## 16. Reproducibility

Principal certificates:

- \`h18_adaptive_depth4_certificate.py\`;
- \`h18_nielsen_dynamics_certificate.py\`;
- \`h18_higman_trace_lift_certificate.py\`;
- \`h18_adaptive_with_tau_certificate.py\`;
- \`h18_three_shadow_higman_decoder.py\`;
- \`h18_adaptive_one_erasure_certificate.py\`;
- \`h18_nielsen_query_compression_certificate.py\`;
- \`h18_query_alphabet_compression_certificate.py\`;
- \`h18_restricted12_controller_certificate.py\`.

Hardware layers:

- H18-LAB-01 adaptive hardwired RTL;
- H18-LAB-02 canonical 24-query microcoded dual RTL;
- restricted 12-query successor architecture from H18-11.

## 17. Literature boundary

Classical Nielsen equivalence and the Higman invariant predate H18.
McCullough and Wanderley study Nielsen equivalence of generating pairs of
\(SL(2,q)\) and \(PSL(2,q)\), with commutator trace as a central invariant.

The H18-specific contribution is the exact finite chain

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
\text{RTL}.
}
\]

## 18. Remaining gates before publication freeze

1. Determine the exact value
   \[
   M_1(W_4)\in\{9,10,11,12\}.
   \]
2. Close the baseline H18-08 dual-RTL CI.
3. Implement the restricted 12-query microcoded RTL as a separate successor
   experiment.
4. Factor the six-way transition table under Nielsen/Higman symmetry.
5. Perform the final theorem/claim/reproducibility audit.
6. Assemble RU/EN publication PDFs only after these gates close.

## References

1. D. McCullough, M. Wanderley, *Nielsen Equivalence of Generating Pairs of
   SL(2,q)*, Glasgow Mathematical Journal 55 (2013), 481–509.
   DOI: 10.1017/S0017089512000675.
2. J. Boschheidgen, B. Klopsch, A. Thillaisundaram, *Generating pairs of
   projective special linear groups that fail to lift*, Mathematische
   Nachrichten 293 (2020). DOI: 10.1002/mana.201900354.
3. HATTER-SOL-17 repository and DOI materials.
