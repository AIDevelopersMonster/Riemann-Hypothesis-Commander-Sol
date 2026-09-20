# HATTER-SOL-19 · STATUS

Branch: \`research/hatter-sol-19-boolean-geometry\`

## Parent state

HATTER-SOL-18 is frozen and publication-ready.

Closed parent evidence includes:

- exact adaptive depth and one-erasure results;
- restricted-12 decision certificate;
- temporal H18-LAB-03 realization;
- spatial H18-LAB-04 realization;
- matched H17/H18 one-cycle FPGA controls;
- H18-12 hardware-image framework;
- H18-13 E0/E1 common-contract boundary.

## H19-01 · formal presentation model — OPENED

Target objects:

\[
M=(X,Y,Q,G,\lambda,\delta,\omega)
\]

for a finite adaptive presentation, with explicit observer labels, response
alphabets, decision DAG, terminal outputs, and encoded semantics.

The first formal distinction is:

\[
\boxed{
\text{query depth}
\neq
\text{Boolean circuit depth}
\neq
\text{transaction latency}.
}
\]

## H19-02 · temporal/spatial compiler theorem — OPENED

Target: exact construction-level formulas for the canonical compiled-DAG
discipline.

No unrestricted circuit lower bound is claimed.

## First controlled E0 family

Use the frozen H18 restricted-12 task and identical external input/fault/output
encoding.

Planned presentations:

1. **DIRECT12** — each word observer realized directly;
2. **PREFIX19** — shared 19-node word-prefix DAG from H18-LAB-04;
3. **NIELSEN12** — observers generated from an explicit Nielsen/SLP basis;
4. **FLAT** — semantics-preserving flattened Boolean control.

The first three are source-structured presentations.  FLAT is the semantic
control.

## H18 closure side branch

\`research/hatter-sol-18-m1-closure\`

Initial strike: test the certified minimum distance-two 9-query alphabet against
the full adaptive one-erasure depth-four contract before launching a global
9/10/11 alphabet search.


## H19-03 · first E0 source-factorization dataset — CLOSED

Three exact source presentations of the same restricted-12 observer semantics
have now been certified before Boolean synthesis.

### DIRECT12

Independent direct evaluation of every observer word:

\[
\boxed{24\text{ permutation-composition nodes}}
\]

with maximum composition depth

\[
\boxed{3}.
\]

### PREFIX19

Global prefix sharing across the same 12 observers:

\[
\boxed{19\text{ shared composition nodes}}
\]

with the same maximum depth

\[
\boxed{3}.
\]

Thus source-level common-subexpression sharing gives the exact E0 reduction

\[
\boxed{24\to19}
\]

without increasing composition depth.

### NIELSEN12

The ten primitive observers use exact shortest elementary Nielsen programmes
from H18-11. Their aggregate source profile is:

\[
\boxed{
18\text{ shear}
+
3\text{ inverse}
}
\]

elementary Nielsen moves.

The two oriented commutator observers remain direct and require six
permutation compositions in this first mixed presentation.

Hence the exact source resource vector is

\[
\boxed{
(\text{swap}=0,\ \text{inverse}=3,\ \text{shear}=18,\
\text{direct commutator compositions}=6).
}
\]

The scalar mixed step count is 27, but it is **not** interpreted as a Boolean
gate-count or FPGA-area metric because the operation types are heterogeneous.

Shortest-program comparison on primitive words gives seven ties with direct
execution and three labels that require one additional elementary Nielsen move.

### Structural conclusion

\[
\boxed{
\text{semantic / algebraic compression}
\not\Rightarrow
\text{source-operation-count compression}.
}
\]

This is now an exact finite statement for the frozen restricted-12 observer
family.

GitHub Actions run \`35487642123\` verifies the NIELSEN12 source certificate.

## H19-04 · E0 RTL comparison — CLOSED

A common generator now emits

- \`direct12\`,
- \`prefix19\`,
- \`nielsen12\`

with one identical 305-node H18 decision DAG, identical static-erasure
interface, identical input/output register shell, and identical 2561-vector
regression contract.

The immediate gate is:

\[
\boxed{
\text{source factorization}
\to
\text{generic Yosys Boolean image}
}
\]

before any FPGA-specific place-and-route comparison.


## H19-04 · compiler forgetting — CLOSED

All three E0 RTL variants pass the same exhaustive 2561-transaction functional
contract.

Under Yosys 0.33

\[
\texttt{proc}\to\texttt{flatten}\to\texttt{opt}
\]

the total cell counts are:

\[
\boxed{
DIRECT12=4919,\qquad
PREFIX19=4919,\qquad
NIELSEN12=5230.
}
\]

Under the further generic Boolean mapping

\[
\texttt{techmap}\to\texttt{opt}
\]

the counts become:

\[
\boxed{
DIRECT12=63719,\qquad
PREFIX19=63719,\qquad
NIELSEN12=72867.
}
\]

DIRECT12 and PREFIX19 have identical reported Boolean-cell histograms despite
the source-level exact difference

\[
24\to19
\]

permutation-composition nodes.

Thus this flow gives the first controlled compiler-forgetting witness:

\[
\boxed{
\text{different source presentation}
\to
\text{same measured optimized Boolean cell histogram}.
}
\]

NIELSEN12 remains distinct and is approximately 14.36% larger than
DIRECT12/PREFIX19 at the post-techmap generic-cell layer.

Claim boundary: this is compiler-relative evidence, not equality of minimum
Boolean circuit complexity.

Detailed record:

- \`H19_04_COMPILER_FORGETTING_RESULT.md\`.

## H19-05 · presentation-preserving compiler discipline — NEXT

Construct a second flow in which declared observer-factorization operations are
explicit module instances with preservation boundaries.

Compare

\[
\Pi_{\rm open}
\quad\text{versus}\quad
\Pi_{\rm preserve}.
\]

The key question is now:

\[
\boxed{
\text{How much hardware difference is hidden by semantic optimization?}
}
\]


## H19-05 · presentation preservation — CLOSED FIRST FAMILY

Two preservation attempts are now distinguished.

### Weak wire preservation

\`(* keep *)\` on intermediate wires did not preserve the source factorization
at the optimized Boolean-cell histogram level.

### Module preservation

Retained mathematical primitive modules preserve the declared factorization.

DIRECT12:

\[
24\,compose+2\,inverse.
\]

PREFIX19:

\[
19\,compose+2\,inverse.
\]

Native NIELSEN12:

\[
21\text{ elementary Nielsen moves}
+
6\text{ direct commutator compositions}
+
2\text{ shared base inversions}.
\]

All three variants pass the common 2561-transaction E0 regression.

The DIRECT12/PREFIX19 pair gives a strict finite compiler-kernel separation:

\[
\ker_{\rm module}
\subsetneq
\ker_{\rm open}
\]

at the declared observables.

Native Nielsen module evidence:

\[
\boxed{\texttt{run 35488601863}}.
\]

## H19-06 · compiler survival tower — ACTIVE

Current survival evidence:

\[
\text{source}
\to
\text{proc/opt}
\to
\text{techmap}.
\]

Next exact measurement:

\[
\boxed{\text{ABC generic logic image}}
\]

for DIRECT12, PREFIX19 and NIELSEN12 under one frozen open flow.

Only after this stage will the first E0 family move to matched Quartus targets.


## H19-LAB-01 · matched Cyclone-V E0 physical family — READY

A parameterized Quartus II 13.1 laboratory has been added for

\[
DIRECT12,\qquad PREFIX19,\qquad NIELSEN12
\]

on the frozen target

\[
\boxed{\texttt{5CEFA7F23C6}}.
\]

All variants use the same:

- generated 305-node decision DAG;
- static persistent-erasure interface;
- registered one-cycle shell;
- 100 MHz reference SDC;
- Slow 1100 mV / 85 C worst-path protocol.

Runner:

\[
\boxed{
\texttt{H19\_LAB\_01\_E0\_CYCLONEV/tools/run\_all\_cyclonev\_a7.ps1}
}
\]

The laboratory is intentionally single-technology first.  No second FPGA
family will be added until the first physical presentation-survival result is
understood.


## H19-07 · non-monotone presentation survival — CLOSED FIRST EXAMPLE

Matched Yosys 0.33 \`abc -fast\` run:

\[
\boxed{\texttt{35489140510}}.
\]

Cell totals:

\[
\boxed{
DIRECT12=60374,\quad
PREFIX19=60383,\quad
NIELSEN12=68406.
}
\]

This is the first H19 re-separation result.

DIRECT12 and PREFIX19 were indistinguishable by complete reported cell
histogram after both

\[
\texttt{proc/opt}
\]

and

\[
\texttt{techmap},
\]

but become distinguishable after \`abc -fast\`.

Therefore presentation survival is not assumed monotone along the compiler
tower:

\[
\boxed{
\text{visible}
\to
\text{hidden}
\to
\text{hidden}
\to
\text{visible}.
}
\]

The source ordering also reverses at this compiler-relative scalar:

\[
19<24
\]

composition nodes for PREFIX19 versus DIRECT12, but

\[
60383>60374
\]

ABC-fast cells.

Detailed record:

- \`H19_07_NONMONOTONE_PRESENTATION_SURVIVAL.md\`.

Next physical gate:

- H19-LAB-01 on 5CEFA7F23C6.


## H19-08 · presentation-survival words — CLOSED FIRST FORMALIZATION

For a presentation pair and a declared compiler/observable tower define the
visibility bits

\[
\nu_i=
\mathbf 1[
O_i(C_i(M_1))\neq O_i(C_i(M_2))
]
\]

and the presentation-survival word

\[
\boxed{
W(M_1,M_2)=\nu_0\nu_1\cdots\nu_k.
}
\]

For DIRECT12 versus PREFIX19, using source composition count, post-proc cell
histogram, post-techmap Boolean-cell histogram, and ABC-fast total cell count:

\[
24\neq19,
\]

\[
4919=4919,
\]

\[
63719=63719,
\]

\[
60374\neq60383.
\]

Hence the first H19 word is

\[
\boxed{
W(DIRECT12,PREFIX19)=1001.
}
\]

The first forgetting and re-separation indices are

\[
\boxed{
f=1,\qquad r=3.
}
\]

This is **observable forgetting**, not proof that the full intermediate
netlists became identical: the post-techmap wire profiles remained different.

Detailed layer:

- \`H19_08_PRESENTATION_SURVIVAL_WORDS.md\`.

H19-LAB-01 will append the physical stage to this survival record.


## H19-09 · Boolean observability and no-resurrection — CLOSED

H19-08's survival word is now separated into two layers:

1. **coarse observable visibility**;
2. **complete compiler-state distinction**.

At one fixed compiler stage, observer refinement is monotone:

[
O_apreceq O_b
quadLongrightarrowquad

u_i(O_a)le
u_i(O_b).
]

For joint observers,

[
oxed{

u_i(O_aee O_b)
=

u_i(O_a)lor
u_i(O_b).
}
]

Thus the visible-observer family is an upset in the observer poset and can be
represented by its minimal visible antichain.

For the complete compiler state (C_i), determinism gives the exact
no-resurrection law

[
oxed{
C_i(M_1)=C_i(M_2)
Longrightarrow
C_{i+1}(M_1)=C_{i+1}(M_2).
}
]

Hence exact-state survival words cannot contain (0	o1).

Because ABC-fast later distinguishes DIRECT12 and PREFIX19, the complete
post-proc and post-techmap states must already have been distinct. Therefore

[
oxed{
W_{m coarse}(DIRECT12,PREFIX19)=1001
}
]

but, through the measured ABC-fast stage,

[
oxed{
W_{m full state}(DIRECT12,PREFIX19)=1111.
}
]

The correct reading is observable hiding and re-exposure, not destruction and
recreation of compiler information.

Detailed layer:

- `H19_09_BOOLEAN_OBSERVABILITY_AND_NO_RESURRECTION.md`.


## H19-10 · exact adaptive/spatialization separation family — CLOSED

A parameterized address-selection family now gives an exact construction-level
separation.

For

[
ain{0,1}^n,
qquad
xin{0,1}^{2^n},
]

define

[
Phi_n(a,x)=x_a.
]

The canonical adaptive presentation queries the (n) address bits and then the
single selected payload bit:

[
oxed{
D_{m query}(M_n)=n+1.
}
]

Its residual frontier grows exactly as

[
oxed{
R_j(M_n)=2^j.
}
]

Under the frozen presentation-preserving compiled-DAG discipline
(Pi_{m DAG}), full spatialization instantiates

[
2^n
]

payload observers and

[
2^n-1
]

binary selectors. Therefore

[
oxed{
N_{m spatial}(M_n)
=
2^{n+1}-1
=
2^{D_{m query}}-1
}
]

when address inputs themselves are treated as wires.

This is an exact exponential temporal-depth/spatial-presentation separation
**within the declared compiler discipline**.

It is not an unrestricted Boolean circuit lower bound and does not claim the
standard multiplexer semantics as novel.

Detailed layer:

- `H19_10_ADAPTIVE_SPATIALIZATION_SEPARATION.md`.


## Publication threshold update

The theoretical publication threshold defined in `DIALOGUE_TZ.md` is now
crossed in substance by two independent theorem layers:

1. H19-09: exact observer-order/no-resurrection structure for compiler
   survival;
2. H19-10: exact parameterized adaptive/spatialization separation under
   (Pi_{m DAG}).

Publication is **not yet frozen**.

Before manuscript assembly, H19 still requires:

1. hostile prior-art/novelty audit, especially against standard multiplexer,
   branching-program, decision-tree, and circuit-compilation literature;
2. claim tightening so construction-level exactness is never promoted to
   unrestricted circuit complexity;
3. completion or explicit deferral of H19-LAB-01 physical Cyclone-V extension;
4. consolidation of the finite DIRECT12/PREFIX19/NIELSEN12 visibility matrix.

## Immediate next strike

The next mathematical/experimental object is the finite visibility matrix

[
Gamma_{i,alpha}
=
mathbf 1[
O_alpha(C_i(M_1))
e O_alpha(C_i(M_2))
].
]

For DIRECT12 versus PREFIX19, populate it with:

- source composition count;
- cell total;
- full cell histogram;
- wire profile;
- module-instance profile;
- ABC-fast cell profile;
- later Cyclone-V physical coordinates.

Then determine the minimal visible frontier

[
partialmathcal V_i
]

at each compiler stage and test which source quantities predict movement of
that frontier.


## H19-11 · visibility-frontier migration — CLOSED

For DIRECT12 versus PREFIX19, the minimal declared observer that still
distinguishes the pair migrates across the open compiler tower as

\[
\boxed{
O_{\rm comp}
\to
O_{\rm wiretot}
\to
O_{\rm wiretot}
\to
O_{\rm celltot}.
}
\]

Thus the presentation distinction moves from source factorization into wiring
structure and later reappears already in scalar Boolean cell count after
ABC-fast.

Detailed layer: H19_11_VISIBILITY_FRONTIER_MIGRATION.md.

## H19-12 · presentation partition lattice — CLOSED

For the E0-equivalent family

\[
\mathcal F=\{DIRECT12,PREFIX19,NIELSEN12\},
\]

each observer induces a partition of \(\mathcal F\).

Post-proc and post-techmap cell histograms give

\[
\boxed{
\{\{D,P\},\{N\}\}.
}
\]

Post-proc wire count and ABC-fast total cell count give the discrete partition

\[
\boxed{
\{\{D\},\{P\},\{N\}\}.
}
\]

Pairwise survival words are therefore the two-presentation special case of a
presentation-partition signature.

Detailed layer: H19_12_PRESENTATION_PARTITION_LATTICE.md.

## H19-13 · hostile prior-art audit — CLOSED FIRST PASS

The audit found that the following are classical/background and must not carry
H19 novelty claims:

- decision-tree / branching-program / circuit comparisons;
- multiplexer/address-selection separation examples;
- observational equivalence;
- compiler semantic preservation / translation validation;
- partition lattices;
- equality saturation and e-graphs;
- compiler phase-ordering / representation-preservation ideas.

Therefore H19-10 remains a calibration theorem inside \(\Pi_{\rm DAG}\), not a
new unrestricted circuit-complexity result.

The plausible H19-specific contribution is narrower:

\[
\boxed{
\text{controlled E0 mathematical presentations}
+
\text{compiler-stage observer partitions/frontiers}
+
\text{physical realization atlas}.
}
\]

Detailed audit: H19_13_PRIOR_ART_AND_NOVELTY_AUDIT.md.

## H19-14 · latent partition gap — CLOSED

For a finite presentation family, define the full-state partition

\[
\mathcal P_i^{\rm full}
\]

and the observer partition

\[
\mathcal P_i^O.
\]

Always

\[
\mathcal P_i^{\rm full}
\preceq
\mathcal P_i^O.
\]

Under deterministic compiler transport, full-state partitions can only
coarsen:

\[
\boxed{
\mathcal P_i^{\rm full}
\preceq
\mathcal P_{i+1}^{\rm full}.
}
\]

Define the hidden-pair latent gap

\[
L_i(O)
=
Q(\mathcal P_i^O)
-
Q(\mathcal P_i^{\rm full}).
\]

For the cell-histogram observer on the frozen H19 family:

\[
\boxed{
L_{\rm cellhist}:1\to1\to0
}
\]

from post-proc to post-techmap to ABC-fast, while the full-state partition
remains discrete throughout.

Thus the measured DIRECT12/PREFIX19 event is rigorously classified as
observer hiding followed by re-exposure, not a compiler state merge followed
by resurrection.

Detailed layer: H19_14_LATENT_PARTITION_GAP.md.

## Publication-threshold status after prior-art audit

Corrected status:

\[
\boxed{
\text{FRAMEWORK THRESHOLD CROSSED;}
\quad
\text{NOVELTY/PUBLICATION THRESHOLD NOT YET SECURE.}
}
\]

The earlier stronger wording has been superseded by the hostile audit.

The next publication-grade gate should be H19-specific and not reducible to
classical decision-tree or order-theory facts.

Priority targets:

1. close H19-LAB-01 physical visibility atlas;
2. test whether latent-gap/frontier trajectories persist across a second
   technology or compiler flow;
3. identify a predictive source quantity for frontier/partition movement;
4. only after one of these succeeds, assemble the manuscript candidate.


## H19-15 · physical visibility atlas protocol — CLOSED / MEASUREMENT PENDING

The Cyclone-V H19-LAB-01 laboratory is now frozen as a physical partition
experiment rather than a one-number FPGA comparison.

Target:

\[
\boxed{\mathrm{5CEFA7F23C6}}
\]

Tool/protocol:

\[
\boxed{
\text{Quartus II 13.1, 100 MHz reference, Slow 1100 mV / 85 C}
}
\]

Physical observer coordinates:

\[
O_{\rm ALM},
O_{\rm reg},
O_{\rm DSP},
O_{F_{\max}},
O_{\rm delay},
O_{\rm logicdepth},
O_{\rm celldelay},
O_{\rm routedelay}.
\]

The matched runner now automatically emits:

- H19_LAB01_CYCLONEV_SUMMARY.csv;
- H19_LAB01_PHYSICAL_PARTITIONS.csv;
- H19_LAB01_PHYSICAL_VISIBILITY_ATLAS.md.

A new analyzer computes:

1. one partition of \(\{D,P,N\}\) per physical observer;
2. the finest joint partition supported by all successfully extracted physical
   coordinates;
3. a profile-relative latent gap
   \[
   L_{\rm profile}(O)
   =
   Q(\mathcal P_O)-Q(\mathcal P_{\rm joint});
   \]
4. the DIRECT12/PREFIX19 physical visibility vector.

The joint measured profile is explicitly **not** identified with the complete
Quartus routed state.

The analyzer refuses to build the atlas unless all three designs have FIT
status.

A deterministic synthetic self-test for the partition logic is included:

- tools/test_physical_visibility_atlas.ps1.

Detailed protocol:

- H19_15_PHYSICAL_VISIBILITY_ATLAS_PROTOCOL.md.

Current state:

\[
\boxed{
\text{protocol closed}
\quad+\quad
\text{automation closed}
\quad+\quad
\text{physical numbers pending local Quartus run}.
}
\]

The next user-side execution command is:

~~~powershell
.\tools\test_physical_visibility_atlas.ps1
.\tools\run_all_cyclonev_a7.ps1
~~~

from the H19_LAB_01_E0_CYCLONEV directory.

No physical result is claimed before those reports exist.
