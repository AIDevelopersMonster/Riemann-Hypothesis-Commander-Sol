# HATTER-SOL-17 · H17-03 · DEPTH-5 ONE-ERASURE ORBIT CODE

## Result

For the 114 simultaneous-conjugacy orbits of generating pairs in `PSL(2,7)`, let each cyclic trace word define one class-coordinate in the oriented six-class alphabet.

The complete family of all cyclic words of primitive depth at most four contains 25 coordinates and has minimum Hamming distance

\[
d_{\min}=1.
\]

There are exactly seven distance-one orbit pairs. For every one of them the unique distinguishing depth-`<=4` coordinate is

\[
ABab=[A,B].
\]

Therefore no observer built only from cyclic trace probes of depth at most four can recover the orbit after an arbitrary single probe erasure.

## Minimal depth theorem

At exact depth five, the word

\[
\boxed{AABAb}
\]

distinguishes all seven depth-four defect pairs. Hence the full depth-`<=4` family augmented by `AABAb` has

\[
d_{\min}=2.
\]

Since depth `<=4` is impossible and depth five succeeds,

\[
\boxed{
\text{the minimum possible maximum primitive depth for one-erasure orbit recovery is }5.
}
\]

This is an exact finite theorem for the current `PSL(2,7)` laboratory and cyclic-trace observer class.

## Cost if the H16 five-probe core is frozen

The H16 minimal exact tomography core is

```text
A, B, AB, Ab, ABab
```

where `Ab = AB^{-1}` and `ABab=[A,B]`.

Exhaustive search over all 26 exact-depth-five cyclic words proves that adding one, two, or three depth-five probes never raises this five-coordinate code to distance two.

Four additions are sufficient. One exact solution is

```text
AAABB
AAAbb
AABab
ABBaB
```

so a backward-compatible one-erasure extension is

```text
A
B
AB
Ab
ABab
AAABB
AAAbb
AABab
ABBaB
```

with nine total probes and maximum word depth five.

Thus, under the constraint that the original H16 five probes remain physically present,

\[
\boxed{5+4=9}
\]

is the exact minimum probe count for one-erasure orbit recovery within the depth-five candidate family.

## Global re-optimization

If the H16 five-probe interface is not frozen and the observer may be redesigned from the complete 51-word family of depth `<=5`, a binary integer program with one constraint per unordered orbit pair,

\[
\sum_{w:\,\sigma_w(i)\ne\sigma_w(j)} x_w\ge2,
\]

returns an optimum of eight probes. HiGHS reports zero MIP gap and dual bound eight; the same model with the cardinality constrained to at most seven is infeasible.

Among cardinality-eight solutions, a second optimization proves that at least four probes must have exact depth five. A minimum-total-word-length solution is

```text
AAB
ABB
AAAb
Abbb
AABAb
AAbAb
ABaBB
AbAbb
```

with depths

```text
3, 3, 4, 4, 5, 5, 5, 5
```

and total primitive word length `34`.

This eight-probe optimum is currently **solver-certified**. The exact depth-five theorem and frozen-five `+4` result are separately checked by exhaustive finite enumeration without relying on the optimizer's optimality claim.

## Important separation: orbit recovery vs generation admissibility

The globally optimized eight-probe set has distance two on the 114 generating orbits, but it is not automatically a generation-domain recognizer.

For the minimum-length eight-probe solution above, the generating signature image has two signatures also realized by non-generating ordered port pairs.

Therefore H17 must treat as separate design objectives:

1. **orbit code distance** among the 114 admissible generating states;
2. **admissibility distance** between generating and non-generating states.

The original five-probe H16 signature has the special stronger property that its generating and non-generating images are disjoint.

Consequently the next optimization target is not merely the smallest `d_min>=2` orbit code, but the smallest depth-limited observer satisfying both

\[
d_{\rm gen/gen}\ge2
\]

and

\[
S_{\rm gen}\cap S_{\rm non}=\varnothing
\]

(or preferably positive erasure distance between those two images as well).

## Certificate

`certificates/psl27_depth5_erasure_certificate.py`

The certificate checks:

- 114 canonical generating orbits;
- 25 depth-`<=4` cyclic words;
- 26 exact-depth-five cyclic words;
- the seven commutator-critical pairs;
- success of `AABAb` against all seven;
- impossibility of adding at most three exact-depth-five probes to the frozen H16 five-core;
- one explicit four-probe extension;
- full 51-word depth-`<=5` code distance `5`.
