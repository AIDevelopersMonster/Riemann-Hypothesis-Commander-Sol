# HATTER-SOL-18
# Adaptive Non-Abelian Tomography: When the Next Word Is Chosen by the Previous Observation

**Status:** publication working draft EN v0.1  
**Branch:** `research/hatter-sol-18-adaptive-word-tomography`  
**Parent:** HATTER-SOL-17

## Abstract

HATTER-SOL-18 continues the finite (PSL(2,7)) mathematical/hardware
laboratory of HATTER-SOL-17 by replacing a fixed observer family with an
adaptive interrogation program.

The states are simultaneous-conjugacy orbits of ordered pairs ((A,B)).
There are 114 generating orbits. For the full identify-or-REJECT contract we
use all 197 pair orbits in (PSL(2,7)^2): 114 generating and 83
non-generating.

Among freely reduced words of length at most four, 160 raw words induce 50
distinct class-valued queries. Exact dynamic programming proves that the
minimum worst-case adaptive decision depth is four, whereas any fixed
separating family in the same pool needs at least five queries:

[
oxed{5_{m fixed}	o4_{m adaptive}}.
]

Among depth-four trees, the minimum total state-path length is 382, giving
minimum mean depth

[
rac{191}{57}approx3.350877.
]

Standard Nielsen moves on the 114 generating orbit states produce four
connected components of sizes

[
36, 32, 32, 14.
]

These are exactly the fibers of the canonical commutator-lift trace

[
	au(A,B)=operatorname{tr}([widetilde A,widetilde B])inmathbb F_7
]

with values (6,4,3,5). Thus the previously unexplained (32+32) split
inside projective commutator class (4A) is identified with the classical
Higman/commutator-trace invariant.

A three-shadow theorem then shows that the projective classes of

[
A^2B^2,qquad ABAB^{-1},qquad ABA^{-1}B
]

reconstruct (	au) on the generating locus, and that three is minimal among
the (W_4) class observers.

Under one persistent known query erasure, four successful class answers still
suffice, so at most five attempts are required:

[
oxed{S_1=4,qquad A_1=5}.
]

Finally, Nielsen structure compresses the globally supported query vocabulary.
The full 50-query pool first reduces to 26 queries consisting of 24 primitive
Nielsen-coordinate observers plus the two oriented commutator observers,
without changing the worst-case adaptive bounds. A further 12-query alphabet
preserves the full one-erasure theorem. An exact exhaustive lower bound gives

[
oxed{9le M_1(W_4)le12},
]

where (M_1(W_4)) is the minimum number of globally supported query labels
needed to retain the exact four-successful-answer one-erasure strategy.

The resulting chain connects adaptive decision trees, Nielsen dynamics,
Fricke trace geometry, query-language compression, and sequential RTL. The
hardware layers are reported separately from the mathematical theorems.

## 1. From a fixed fingerprint to an interrogation program

H17 showed that a fixed family of eight class-valued word observers forms a
robust fingerprint with exact recovery from one erased coordinate when the
erased position is known.

H18 changes the information model. Rather than evaluating every probe in
advance, the observer chooses the next group word from the class answers
already obtained:

[
w_1	o c_1	o w_2(c_1)	o c_2	ocdots.
]

The observer family is therefore no longer only a code. It becomes a
branching program.

Three complexity measures must be separated:

1. **transaction complexity:** how many answers are needed on one path;
2. **query-alphabet complexity:** how many distinct query labels must be
   supported globally;
3. **realization complexity:** how much controller memory, logic, arithmetic,
   routing, and latency are required in hardware.

H18 treats these as different optimization problems.

## 2. Finite state and query model

Let

[
G=PSL(2,7),qquad |G|=168.
]

Elements are represented by their exact permutation action on
(mathbb P^1(mathbb F_7)).

For ((A,B)in G^2), identify pairs under simultaneous conjugacy:

[
(A,B)sim(hAh^{-1},hBh^{-1}).
]

The generating pairs form 114 simultaneous-conjugacy orbits. The quotient of
all ordered pairs contains

[
oxed{197=114+83}
]

orbits: 114 generating and 83 non-generating. The latter share the common
terminal output REJECT.

For freely reduced words of lengths (1,ldots,4),

[
4+12+36+108=160
]

raw words occur. Deduplication by exact response vector on the finite model
leaves

[
oxed{50}
]

distinct class-valued queries.

## 3. Exact adaptive depth-four theorem

Let (D^*(W_4)) be the minimum worst-case depth of an adaptive class-query
tree identifying the 114 generating orbit states.

Exact dynamic programming proves

[
oxed{D^*(W_4)=4}.
]

Depth three is impossible and depth four is sufficient.

Within the same query pool, no fixed set of one through four queries separates
all 114 states. The five-query family

[
A, B, AB, Ab, ABab
]

does separate them. Hence

[
oxed{5_{m fixed}	o4_{m adaptive}}.
]

Among all depth-four trees, the minimum total state-path length is

[
382,
]

so the minimum mean depth is

[
oxed{ar D_{min}=191/57}.
]

One selected optimum has 48 internal decision nodes, root query
(	exttt{AAB}), with 74 states terminating at depth three and 40 at depth
four.

## 4. Nielsen dynamics on orbit space

Consider elementary moves including

[
S(A,B)=(B,A),qquad I_A(A,B)=(A^{-1},B),
]

and

[
N_A(A,B)=(AB,B).
]

They descend to permutations of the 114 generating orbit states.

The Nielsen graph generated by standard moves has connected-component sizes

[
oxed{36, 32, 32, 14}
]

with diameters

[
oxed{7, 6, 8, 4}.
]

The projective commutator classes on these components are:

- (36) states in (3A);
- (32) states in (4A);
- (32) states in (4A);
- (14) states split as (7A/7B).

Thus the projective commutator class does not separate the two 32-state
components.

## 5. Canonical lift trace and the Higman invariant

Choose determinant-one lifts

[
widetilde A,widetilde Bin SL(2,7).
]

The commutator

[
[widetilde A,widetilde B]
]

is independent of the sign choices of the two lifts. Therefore

[
oxed{
	au(A,B)=operatorname{tr}([widetilde A,widetilde B])
}
]

is well-defined on the projective pair.

On the 114 H17 states the exact fibers are

[
	au=6:36,qquad
	au=4:32,qquad
	au=3:32,qquad
	au=5:14.
]

Each fiber is exactly one Nielsen connected component.

In particular,

[
oxed{
4A^{(+)}:	au=3,qquad
4A^{(-)}:	au=4=-3pmod7.
}
]

This identifies the finite H18 component split with the classical Higman /
commutator-trace invariant. H18 does not claim discovery of that invariant;
its contribution is the exact connection to the H17/H18 orbit-tomography
state space and adaptive observer language.

## 6. Three projective shadows reconstruct the lift trace

Put

[
x=operatorname{tr}widetilde A,qquad
y=operatorname{tr}widetilde B,qquad
z=operatorname{tr}(widetilde Awidetilde B).
]

Fricke's identity is

[
	au=x^2+y^2+z^2-xyz-2.
]

Define

[
R_z=A^2B^2,qquad
R_x=ABAB^{-1},qquad
R_y=ABA^{-1}B.
]

Then

[
operatorname{tr}(R_z)=z^2-	au,
]

[
operatorname{tr}(R_x)=x^2-	au,
]

[
operatorname{tr}(R_y)=y^2-	au.
]

A projective conjugacy class determines the square of the trace of an
(SL(2,7)) lift. Hence the three projective classes of these shadow words
determine (	au) on the generating locus.

Exact search over the 50 (W_4) queries proves

[
oxed{m_	au(W_4)=3}.
]

No single query or pair of queries determines (	au); exactly 16 query
triples do.

This is the structural bridge from projective word observations to the
canonical lift invariant.

## 7. One persistent known query erasure

The fault model is:

- at most one requested query returns ERASED;
- the failed query identity is known;
- that query becomes unavailable for the rest of the transaction;
- it may not be repeated.

For the full 197-state identify-or-REJECT task, exact dynamic programming
gives

[
oxed{D_0=4}
]

without erasure and

[
oxed{S_1=4}
]

successful answers under one persistent erasure. Therefore

[
oxed{A_1=5}
]

total attempts suffice.

The H17 and H18 output contracts are different: H17 reconstructs a fixed
robust fingerprint, whereas H18 identifies a generating orbit or returns
REJECT through a data-dependent interrogation program.

## 8. First adaptive RTL realization

H18-07 materializes the exact H18-06 strategy as sequential RTL:

- 308 nonterminal query states;
- 69 pre-erasure states;
- 239 post-erasure states;
- 24 distinct query labels;
- maximum word length four;
- one shared word datapath;
- one reused class engine.

The regression result is

[
197	imes5=985/985 mathrm{PASS}.
]

The observed RTL maximum is five attempts and 32 cycles.

Under a common technology-independent Yosys methodology:

[
H17	ext{-LAB-03}=13547
]

and

[
H18	ext{-LAB-01}=17205
]

hierarchy-expanded generic cells. The first hardwired adaptive realization is
therefore about 27% larger than the H17 reference under that methodology.

This is an implementation result, not a theorem that adaptive tomography is
intrinsically larger.

## 9. Canonical microcoded representation

H18-08 replaces the large hardwired controller decode by a canonical
microprogram.

Before vendor-specific memory packing, the program payload is

[
1540+16632+621+264
=
oxed{19057	ext{ bits}}.
]

Direct loading of the first word letter also reduces the worst five-attempt
word-composition count from

[
19	o14.
]

This layer changes the representation while preserving the exact H18-06
decision strategy.

## 10. Nielsen-normal query compression

Exactly 24 of the 50 canonical (W_4) queries are primitive free-group words,
hence Nielsen transports of a coordinate observer.

On the 114 generating states, their joint signatures give 107 distinct
classes and leave exactly seven doublets:

[
(12,27),(13,28),(14,29),(84,89),(90,92),(100,103),(106,107).
]

These are precisely the H17 depth-(le4) commutator-defect pairs.

They are all separated by the oriented commutator query (	exttt{ABab}).
The natural Nielsen-normal query family therefore consists of

[
oxed{24	ext{ primitive}+2	ext{ commutator orientations}=26}.
]

On this restricted pool the exact worst-case results remain

[
oxed{D_0=4,qquad S_1=4,qquad A_1=5}
]

and the fixed/adaptive separation remains

[
oxed{5_{m fixed}	o4_{m adaptive}}.
]

The generating-only optimum total path length increases only from 382 to 386,
so the mean depth changes from (191/57) to (193/57), while worst-case
depth remains four.

## 11. Global query-alphabet compression theorem

H18-10 asks how many distinct labels the machine must support globally.

Any alphabet tolerating one persistent query erasure must distinguish each
required generating/generating and generating/non-generating pair by at least
two supported labels.

In the complete 50-query (W_4) pool, exactly seven critical pairs have only
two separating labels:

[
oxed{	exttt{ABab},qquad	exttt{AbaB}}.
]

Therefore both oriented commutator queries are forced in every distance-two
alphabet.

With those two labels fixed, an eight-query alphabet could add only six of the
remaining 48 labels. Exhaustive search of all

[
inom{48}{6}=12,271,512
]

possibilities proves that none satisfies the necessary distance-two
condition.

A nine-query distance-two witness exists, so the minimum robust alphabet under
that coding condition is exactly nine.

For the full adaptive four-successful-answer contract, the following
12-query alphabet is sufficient:

[
oxed{
A,B,ABab,AbaB,ABB,Abb,AAb,AAAB,AAAb,Baa,aab,abb.
}
]

Exact dynamic programming on this restricted alphabet gives again

[
D_0=4,qquad S_1=4,qquad A_1=5.
]

Hence, for the minimum globally supported alphabet preserving the complete
H18-06 contract,

[
oxed{9le M_1(W_4)le12}.
]

Determining whether the exact value is 9, 10, 11, or 12 is the next finite
theorem target.

## 12. Structural interpretation

The H18 query language contracts through the following chain:

[
50	ext{ canonical }W_4	ext{ queries}
]

[
Downarrow
]

[
24	ext{ primitive Nielsen transports}
+
2	ext{ commutator orientations}
]

[
Downarrow
]

[
12	ext{-label adaptive witness},
]

while preserving the exact worst-case information bound

[
oxed{
4	ext{ successful class answers}
+
1	ext{ possible erasure}.
}
]

The adaptive and Nielsen parts of H18 are therefore not separate themes.
Nielsen geometry explains how the language of the interrogation program can
be compressed.

## 13. Claim boundaries

Certified or directly verified in the current project:

- exact finite state counts;
- exact adaptive depth four;
- strict fixed/adaptive separation;
- exact Nielsen component decomposition;
- identification of components with canonical lift-trace fibers;
- three-shadow reconstruction and its (W_4) minimality;
- exact one-persistent-erasure bound;
- finite RTL regression of H18-07;
- generic synthesis comparison of current H17/H18 implementations;
- 26-query Nielsen-normal reduction;
- exact global alphabet bracket (9le M_1le12).

Not claimed:

- a theorem for all (PSL(2,q));
- cryptographic hardness;
- physical fault tolerance;
- target-FPGA superiority of H18 over H17;
- an exact value of (M_1) before the remaining finite optimization closes;
- measured power, Fmax, or board behavior for H18.

## 14. Reproducibility

Principal certificates:

- `h18_adaptive_depth4_certificate.py`;
- `h18_nielsen_dynamics_certificate.py`;
- `h18_higman_trace_lift_certificate.py`;
- `h18_adaptive_with_tau_certificate.py`;
- `h18_three_shadow_higman_decoder.py`;
- `h18_adaptive_one_erasure_certificate.py`;
- `h18_nielsen_query_compression_certificate.py`;
- `h18_query_alphabet_compression_certificate.py`.

Hardware layers:

- H18-LAB-01 adaptive RTL;
- H18-LAB-02 canonical microcoded dual RTL.

## 15. Literature boundary

Classical Nielsen equivalence and the Higman invariant predate H18.
McCullough and Wanderley study Nielsen equivalence of generating pairs of
(SL(2,q)) and (PSL(2,q)), with the Higman invariant and the commutator
trace playing central roles.

The H18-specific contribution is the exact finite chain

[
	ext{Nielsen dynamics}
leftrightarrow
	ext{adaptive word tomography}
leftrightarrow
	ext{Fricke/Higman reconstruction}
leftrightarrow
	ext{query-program compression}
leftrightarrow
	ext{RTL}.
]

## 16. Remaining theorem targets before publication freeze

1. Determine the exact value
   [
   M_1(W_4)in{9,10,11,12}.
   ]
2. Determine whether one can jointly minimize global query alphabet and total
   adaptive path length.
3. Compare direct-word execution with Nielsen-microprogram execution under an
   explicit arithmetic cost model rather than assuming the latter is cheaper.
4. Close H18-08 dual-RTL CI.
5. Run a final theorem/claim/reproducibility audit and assemble RU/EN PDFs.

## References

1. D. McCullough, M. Wanderley, *Nielsen Equivalence of Generating Pairs of
   SL(2,q)*, Glasgow Mathematical Journal 55 (2013), 481–509.
   DOI: 10.1017/S0017089512000675.
2. J. Boschheidgen, B. Klopsch, A. Thillaisundaram, *Generating pairs of
   projective special linear groups that fail to lift*, Mathematische
   Nachrichten 293 (2020). DOI: 10.1002/mana.201900354.
3. HATTER-SOL-17 repository and DOI materials.
