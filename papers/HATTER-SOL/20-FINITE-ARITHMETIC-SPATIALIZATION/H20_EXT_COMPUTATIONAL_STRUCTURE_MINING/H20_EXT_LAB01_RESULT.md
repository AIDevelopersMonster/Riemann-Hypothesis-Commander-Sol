# H20-EXT-LAB-01 · Exact continuation quotient census

Status: **FIRST CPU EXPERIMENT CLOSED / NO CONJECTURE PROMOTED**

Tool: `tools/continuation_quotient.py`

Frozen range:

- discovery: (W=4,ldots,10);
- validation: (W=11,ldots,14);
- extrapolation gate: (W=15,16).

The experiment computes exact continuation-equivalence quotients for the prime indicator and declared baselines under both MSB-first and LSB-first variable orders.

## Prime continuation quotient

| W | MSB nodes | LSB nodes | MSB peak classes | LSB peak classes |
|---:|---:|---:|---:|---:|
| 4 | 7 | 7 | 4 | 4 |
| 5 | 11 | 13 | 5 | 6 |
| 6 | 16 | 19 | 5 | 8 |
| 7 | 29 | 29 | 11 | 11 |
| 8 | 46 | 49 | 16 | 18 |
| 9 | 73 | 78 | 29 | 31 |
| 10 | 122 | 127 | 47 | 48 |
| 11 | 204 | 212 | 68 | 72 |
| 12 | 352 | 344 | 126 | 128 |
| 13 | 601 | 597 | 242 | 244 |
| 14 | 1063 | 1063 | 446 | 442 |
| 15 | 1863 | 1863 | 736 | 727 |
| 16 | 3242 | 3222 | 1093 | 1065 |

The two bit orders are not identical, but the node counts remain close at the larger widths. This is a representation-transport observation, not an invariant theorem.

## Baseline screen

For (Wge 6), the prime quotient is consistently smaller than the mean density-matched random and shuffled-prime quotients in both declared bit orders. At (W=16):

[
N_{m prime}^{MSB}=3242,
qquad
N_{m random}^{MSB}approx 4506.67,
qquad
N_{m shuffled}^{MSB}approx4525.33,
]

and

[
N_{m prime}^{LSB}=3222,
qquad
N_{m random}^{LSB}approx4503.33,
qquad
N_{m shuffled}^{LSB}approx4513.67.
]

The prime quotient is also smaller than the squarefree and semiprime quotients at the upper widths.

This is a real finite compressibility signal relative to the selected baselines, but it is **not yet a publishable law**.

## Literature control

The broad automata/finite-state direction is known territory.

In particular:

1. the characteristic sequence of the primes is known not to be (q)-automatic for any (qge2);
2. Shallit studied finite automaticity/descriptional complexity and proved a quantitative lower bound for the prime characteristic sequence.

Therefore this experiment must not be described as discovery of a new "finite automaton of primes" or as novelty of state growth itself.

The exact continuation quotient used here is closer to a residual-function / ordered branching-program object than to Shallit's finite-prefix automaticity, so exact equivalence has **not** been established. The correct classification at this stage is:

> **known-neighbouring framework / apparently distinct finite observer / novelty unresolved.**

A targeted literature audit would be required before promoting any specific quotient law.

## Observation

The exact finite prime predicates have smaller reduced continuation quotients than density-matched random and shuffled-prime baselines over most of the tested range, and this qualitative gap survives both MSB-first and LSB-first orders.

## Exact finite statement

The accompanying tool exhaustively computes the exact residual-function quotient for every declared predicate and bit order. The local reference run covered (W=4,ldots,16).

Reference SHA-256 values for that run:

- tool: `b9be54cd3521d19bef0866effdb6b97d8aa85f551ba3d8fbf9911661f1ffe5a5`;
- generated Markdown report: `591f3a2c25a24bba0e14279fc94c767b50035400e9ba7f74424f92e7a5c4d487`;
- full local CSV: `6df6bbb189f2a39f78ba75f1ff21d2e1181ac42939356c8088c3497dbf3a2db4`;
- full local JSON: `080fd84782a20e87800cb081979d527b4e1d68d60e2f7331a953e695cefaeb8c`.

The repository tool emits compact reproducible `continuation_quotient.csv`, `continuation_quotient.json`, and `H20_EXT_LAB01_REPORT.md`.

## Interpretation

The experiment has found a **candidate compressibility phenomenon**, not yet a mathematical invariant.

A plausible mundane explanation is that primality contains strong small-modulus residue structure. The present baselines control density and shuffling, but they do not yet factor out wheel/residue information.

Because the validation and extrapolation widths have now been inspected, no conjecture formulated from the full (Wle16) table may be called independently validated on (W=11,ldots,16).

Any promoted law now requires a **new validation layer**, or a new predeclared residual-conditioning experiment.

## Non-claim

This result does not establish:

- a new theorem on primes;
- a new lower or upper bound for primality OBDD complexity;
- a finite-state characterization of primes;
- an asymptotic recurrence law;
- a circuit-complexity lower bound;
- a relation to the zeros of the zeta function;
- any RH implication.

## Decision

[
oxed{	ext{PUBLICATION THRESHOLD NOT REACHED}}
]

H20-EXT remains open as an evidence-first research branch.

The strongest justified next question is not "what formula fits the node counts?" but:

[
oxed{
	ext{does the compressibility gap survive after explicitly conditioning out}
atop
	ext{small-prime residue / wheel structure?}
}
]

That is a new experiment and must be frozen before execution.
