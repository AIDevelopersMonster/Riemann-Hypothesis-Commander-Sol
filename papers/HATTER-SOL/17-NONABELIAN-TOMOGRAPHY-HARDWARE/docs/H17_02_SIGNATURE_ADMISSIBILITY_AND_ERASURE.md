# H17-02 · SIGNATURE ADMISSIBILITY AND FIRST ERASURE LAW

**Status:** exact finite computer-assisted theorem layer, certified by exhaustive enumeration.  
**Laboratory:** `G = PSL(2,7)` in its faithful action on `P^1(F_7)`.  
**Observer:** the frozen H16 five-probe signature

\[
\sigma(A,B)=\bigl([A],[B],[AB],[AB^{-1}],[[A,B]]\bigr).
\]

## Proposition H17.A — the five-probe ROM is also an admissibility oracle

Let `S_gen` be the set of five-probe signatures of generating pairs and `S_non` the set of signatures of non-generating pairs in `G^2`. Exact enumeration gives

- `|G| = 168`;
- `|G^2| = 28,224`;
- generating ordered pairs: `19,152`;
- non-generating ordered pairs: `9,072`;
- `|S_gen| = 114`;
- `|S_non| = 66`;
- `S_gen ∩ S_non = ∅`.

Hence, for valid `PSL(2,7)` port inputs,

\[
\boxed{\sigma(A,B)\in S_{gen} \iff \langle A,B\rangle=PSL(2,7).}
\]

Combined with H16 injectivity on generating-pair simultaneous-conjugacy orbits, a single 114-entry ROM performs two jobs:

1. it decides whether the pair generates the full group;
2. if it does, it returns the unique canonical orbit ID `0..113`.

**Engineering consequence:** H17 does not need a separate subgroup-generation engine on the exact `PSL(2,7)` laboratory path.

## Proposition H17.B — asymmetric one-erasure behaviour

Use probe-coordinate Hamming distance on the five class labels. Exact enumeration gives

\[
 d_{min}(S_{gen},S_{gen})=1,
 \qquad
 d_{min}(S_{gen},S_{non})=2.
\]

Therefore one erased probe can already destroy the exact orbit ID, while after erasing any one fixed probe a generating signature still cannot be confused with a non-generating signature.

Thus the minimal five-probe observer has zero guaranteed erasure tolerance for orbit reconstruction, but one-erasure tolerance for generating/non-generating admissibility.

### Exact orbit-collision statistics after deleting one probe

| erased probe | distinct generating projections | orbits in collision buckets | collision buckets | max bucket |
|---|---:|---:|---:|---:|
| `A` | 88 | 52 | 26 | 2 |
| `B` | 88 | 52 | 26 | 2 |
| `AB` | 110 | 8 | 4 | 2 |
| `AB^-1` | 110 | 8 | 4 | 2 |
| `[A,B]` | 107 | 14 | 7 | 2 |

So the five channels are not equally informative under erasure: losing `AB` or `AB^-1` damages the fewest orbit identifications; losing `A` or `B` damages the most.

## Proposition H17.C — depth-4 redundancy barrier

Let `W_{<=4}` be the complete H16 family of cyclically reduced trace words of primitive length at most four, modulo cyclic rotation and inversion. It has 25 coordinates.

Exact enumeration of the 114 generating-pair orbit signatures over all 25 coordinates gives minimum probe-coordinate Hamming distance

\[
\boxed{d_{min}(W_{\le4})=1.}
\]

There are exactly seven unordered pairs of generating-pair orbits at distance one. For all seven pairs, the unique separating coordinate is

\[
\boxed{ABab=[A,B].}
\]

Therefore no observer system built only from cyclic trace probes of primitive depth at most four can guarantee exact orbit reconstruction after one arbitrary probe erasure. In particular, adding more depth-`<=4` wires cannot solve the one-erasure orbit problem.

This turns the next hardware question into a genuine depth problem: an erasure-correcting extension must introduce information from depth strictly greater than four, or leave the cyclic-trace observer class.

## Certificate

`certificates/psl27_signature_admissibility_certificate.py`

The certificate constructs `PSL(2,7)` exactly, enumerates all `28,224` ordered pairs, computes subgroup generation and all five probe classes, and asserts Propositions H17.A and H17.B. The depth-4 barrier was independently exhaustively checked against the full 25-word H16 candidate family and is the next item to fold into the permanent certificate.

## Hardware consequence

The end-to-end core may safely expose

```text
orbit_valid = group_input_valid AND signature_hit
```

with the proved interpretation on the exact finite laboratory domain:

```text
orbit_valid = 1  <=>  <A,B> = PSL(2,7)
```

and, when valid, `orbit_id` is the canonical generating-pair simultaneous-conjugacy orbit.
