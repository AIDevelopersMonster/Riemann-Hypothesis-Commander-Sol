# H20-EXT · Computational Structure Mining
## RESEARCH QUESTION

**Branch:** `research/hatter-sol-20-computational-structure-mining`  
**Parent branch:** `research/hatter-sol-finite-arithmetic-spatialization`  
**Parent tip at branch creation:** `38c7c0424b5f6b85f46770f3770a75b898085428`  
**Status:** EVIDENCE-FIRST EXPLORATORY LAYER  
**Publication status:** NOT A PAPER / BELOW PUBLICATION THRESHOLD

## 1. Recovered H20 state

H20 is not restarted here. The parent branch already closed the first arithmetic-presentation and physical-realization programme.

For fixed width (W), the frozen strict-next-prime function is

[
S_W(x)=min{p>x:p	ext{ prime}},
qquad 0le x<2^W.
]

Three exact presentations were generated:

- DIRECT: complete finite lookup;
- BALANCED: balanced threshold decision tree;
- LINEAR: ordered threshold chain.

Formal Yosys SAT equivalence established

[
D_Wequiv B_Wequiv L_W
]

for every (W=4,ldots,10).

After Boolean normalization and ABC-fast, all three remained structurally separated for every measured width, with the measured cell-count ordering

[
D_W<B_W<L_W.
]

The physical layer is already closed and is not reopened in this extension.

### Cyclone V

Target: `5CEFA7F23C6`, Quartus II 13.1.

For (W=8,9,10), DIRECT mapped to M10K hard memory while BALANCED and LINEAR remained in logic fabric. The BALANCED/LINEAR physical ordering crossed between (W=8) and (W=9).

### Gowin GW5A-25

Target: `GW5A-LV25MG121NC1/I0`, Gowin Education 1.9.9Beta-4.

DIRECT mapped to BSRAM while BALANCED and LINEAR remained in logic fabric. The corresponding BALANCED/LINEAR crossover occurred later, between (W=9) and (W=10).

Therefore the closed H20 physical conclusion is

[
oxed{
	ext{presentation ordering}
=
f(	ext{backend},W,	ext{observer})
}
]

with a backend-dependent crossover location.

The stable qualitative cross-vendor fact is

[
D_W	o	ext{hard-memory resource class},
qquad
B_W,L_W	o	ext{logic fabric}
]

for the measured (W=8,9,10) experiments.

No further FPGA benchmarking is justified merely to enlarge these tables.

## 2. Place in the H16 -> H20 programme

The recovered programme sequence is:

[
oxed{
H16	o H17	o H18	o H19	o H20.
}
]

- **H16 · Nonsolvable Ports:** finite non-Abelian/nonsolvable observer families.
- **H17 · Nonabelian Tomography Hardware:** exact hardware realization and tomography of finite mathematical observer structures.
- **H18 · Adaptive Word Tomography:** adaptive decision structure and temporal execution become first-class implementation variables.
- **H19 · Boolean Geometry of Mathematical Presentations:** presentation, observer, compiler stage and physical backend are separated formally. Observer-induced partitions, visibility frontiers, no-resurrection for complete deterministic compiler states, latent partition gaps and cross-vendor physical quotients are the central language.
- **H20 · Finite Arithmetic Spatialization:** the H19 presentation/observer framework is instantiated on exact finite arithmetic, first with prime membership and strict next-prime.

H20-EXT changes the research object again. It no longer asks which of several source presentations produces the better physical image. It asks whether exact finite arithmetic data itself exhibits a reproducible structural object worth theorizing.

## 3. Closed or currently nonproductive directions

The following directions are not reopened merely under new terminology:

- primes as rectangles / absence of nontrivial (a	imes b);
- factorization geometry by itself;
- divisibility matrices by themselves;
- boundary-only or degenerate factorization pictures;
- factorization monoids by themselves;
- ANF as an end in itself;
- ROBDD as an end in itself;
- ordinary Kolmogorov complexity (K(C_W));
- immediate search for a "geometry of primes";
- any direct RH interpretation before an autonomous finite structural result exists.

A previously visited object may return only if a new exact measurable object makes the question materially different from the standard formulation.

## 4. Central research question

[
oxed{
	ext{Does exact finite prime arithmetic expose a reproducible structural object}
atop
	ext{that survives falsification strongly enough to deserve a theorem statement?}
}
]

A useful candidate must satisfy, as far as computationally testable:

1. it is not a direct restatement of primality;
2. it is not merely (pi(x)), (	au(n)), (Omega(n)), prime gaps, or a divisor table;
3. it recurs across consecutive widths;
4. it survives at least one representation-transport test;
5. it has an exact finite definition;
6. it survives a suitable baseline comparison;
7. it can be falsified by a predeclared criterion.

A negative outcome is acceptable and scientifically preferred to an artificial conjecture.

## 5. Evidence-first discipline

The branch order is frozen as

[
oxed{
	ext{COMPUTE}
	o
	ext{OBSERVE}
	o
	ext{FALSIFY}
	o
	ext{FORMULATE}
	o
	ext{PROVE}.
}
]

Not

[
	ext{IMAGINE}	o	ext{FIT DATA}.
]

Every candidate result must separate:

### Observation
What was numerically/combinatorially measured.

### Exact finite statement
What is exhaustively true on the declared finite range.

### Interpretation
What structural reading is suggested.

### Non-claim
What asymptotic, number-theoretic, circuit-complexity, or RH statement does not follow.

## 6. Discovery / validation contract

The first mining layer freezes the ranges before results are inspected:

- **Discovery:** (W=4,ldots,10)
- **Validation:** (W=11,ldots,14)
- **Extrapolation gate:** (W=15,16)

If a conjecture is altered after inspecting validation widths, the altered conjecture starts a new validation layer.

## 7. Candidate computational observers

| ID | Observer | Exact object | First-range cost | Novelty risk | Predeclared falsification criterion |
|---|---|---|---|---|---|
| O1 | Exact continuation quotient | Equivalence classes of prefixes having identical behavior on every suffix, plus the quotient split DAG | (O(W2^W)) time, (O(2^W)) memory; practical through (W=16) | Medium-high: automata/OBDD/Myhill-Nerode literature | Reject as candidate law if prime signatures do not separate from density/parity baselines or are strongly variable under bit-order transport |
| O2 | Walsh spectral mass by degree | Exact Walsh transform grouped by Hamming degree | (O(W2^W)) via FWHT | High: classical Boolean analysis; strong parity artifacts expected | Reject if deviations are explained by oddness/density or fail hold-out widths |
| O3 | Influence / sensitivity profile | Exact variable influences and local sensitivity histogram | (O(W2^W)) | High | Reject if profile is explained by low-order residue filters or unstable across widths |
| O4 | Certificate profile | Exact/near-exact 0/1 certificate-size distribution for small (W) | potentially exponential beyond truth-table scan | Medium-high | Stop before expensive scaling unless small widths show nontrivial baseline separation |
| O5 | ANF degree-mass profile | Algebraic degree and monomial-count distribution by degree | (O(W2^W)) Möbius transform | Very high; ANF already rejected as self-goal | Continue only if a transport-stable law appears that is not merely "degree grows" |
| O6 | Residue-conditioned residuals | Continuation quotient after conditioning out selected small-prime residue information | (O(W2^W)) for fixed conditioning | Medium | Reject if all apparent structure disappears after explicit wheel conditioning |
| O7 | Technology-independent DAG motif census | Canonical repeated subgraphs in AIG/Boolean DAG derived from exact functions | polynomial in netlist size after synthesis | Medium-high and tool-sensitive | Do not run until truth-level evidence identifies a target motif/invariant |
| O8 | Cross-width structural transport | Exact shared canonical substructures between (W) and (W+1) | depends on base observer; typically (O(W2^W)) | Medium | Reject if only the trivial lower-half embedding survives |
| O9 | Incidence/hypergraph kernels | Sparse divisibility/multiplication/residue incidence kernels | potentially (O(Nlog N)) sparse | Very high because old factorization routes are already weak | Do not continue without a new invariant absent from standard divisor structure |

## 8. Selected first experiment

### H20-EXT-LAB-01 · Exact continuation quotient census

The first experiment is **O1**.

Reason for selection:

[
rac{	ext{potential scientific information}}{	ext{computational cost}}
]

is highest among the current candidates because:

- it uses only exact finite primality data;
- it is canonical once input-variable order is declared;
- it records a full finite quotient object, not only one scalar metric;
- it admits exhaustive verification through the validation and extrapolation gates on an ordinary CPU;
- it has an immediate falsification path using baselines and a second bit order;
- it postpones all expensive synthesis work.

### Exact object

For the prime indicator

[
P_W:{0,1}^W	o{0,1},
]

fix a variable order (sigma).

At depth (d), two length-(d) assignments/prefixes (a,b) are continuation-equivalent when their residual functions on every remaining assignment are identical:

[
asim_{W,d,sigma}b
iff
orall sin{0,1}^{W-d}:
P_W(aVert_sigma s)=P_W(bVert_sigma s).
]

The primary object is the complete quotient data

[
mathcal Q_{W,d,sigma}
]

including:

1. exact residual classes;
2. class multiplicities;
3. exact child-pair incidence under the next assigned bit;
4. the resulting canonical quotient DAG across all depths.

A reduced ordered BDD is one possible implementation of this quotient. **The BDD itself is not the scientific claim.** The research object is exact continuation equivalence and its cross-width/baseline/transport behavior.

### Representation transport

The same exact predicate is processed under two predeclared variable orders:

- (sigma_{m MSB}): most-significant bit first;
- (sigma_{m LSB}): least-significant bit first.

Any candidate law visible in only one order is classified as representation-sensitive unless later justified otherwise.

### Baselines

The first run includes deterministic comparison families:

- ODD indicator;
- SQUAREFREE indicator;
- SEMIPRIME indicator;
- density-matched RANDOM sets with fixed seeds;
- SHUFFLED-PRIME indicator with fixed seeds.

Random baselines preserve the number of ones for each width.

### First falsification gate

No positive structural claim is opened unless, on discovery widths, a prime-specific quotient feature:

1. is not explained by density or parity;
2. has a precise exact definition;
3. persists on (W=11,ldots,14) without retuning;
4. is not destroyed by changing MSB-first to LSB-first, unless the representation dependence itself becomes the exact result;
5. survives comparison with at least one non-prime arithmetic baseline.

If these conditions fail, H20-EXT-LAB-01 closes as a negative result.

## 9. Output contract

The first experiment must emit only reproducible CPU artifacts:

- `continuation_quotient.csv`
- `continuation_quotient.json`
- `H20_EXT_LAB01_REPORT.md`

No FPGA flow is invoked.

No exact circuit minimization is invoked.

No expensive graph-mining package is required.

## 10. Literature gate

No observation from LAB-01 is called new before targeted checks against:

- Myhill-Nerode / residual-function literature;
- ordered BDD / branching-program literature;
- Boolean-function complexity literature;
- automatic/regular descriptions of prime-related languages;
- OEIS if a numerical sequence is promoted from diagnostic to candidate law.

The initial continuation quotient is expected to overlap known concepts. Novelty, if any, would have to lie in a specifically defined finite prime structural law or transport obstruction, not in the existence of residual quotients themselves.

## 11. RH boundary

[
oxed{	ext{NO RH CLAIMS}}
]

until an autonomous finite structural result exists and a separate literature audit establishes a rigorous bridge to prime-distribution estimates.

## 12. Publication threshold

H20-EXT remains unpublished unless at least one of the following is reached:

- a new proved finite/asymptotic theorem;
- a strong reproducible empirical law passing discovery/validation, baselines and representation transport;
- an impossibility result for a natural candidate class;
- a nontrivial representation-transport invariant or obstruction.

Otherwise the correct closure statement is:

> After systematic computational investigation of the declared finite observers on the tested range, no structural law strong enough for an independent theorem or publication claim was found. H20 remains closed pending new external or computational evidence.
