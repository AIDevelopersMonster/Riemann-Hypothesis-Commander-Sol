# FCOA Hybrid Memory — Arithmetic Leakage Audit

**Status:** internal branch audit; updated for shared-output synchronization.

## 1. Scope

This audit concerns the explicit finite witnesses in `MINIMAL_WITNESSES.md` and the scalable families in `SYNERGY_CLASSES.md`.

Firewall questions:

1. Is successor recovered?
2. Is full order recovered?
3. Is any internal addition-like or multiplication-like graph definable?
4. Are index calculations smuggled into branch definitions?

## 2. Minimal three-point witnesses

This includes DD-3, DV-I-3, VV-I-3, and the new shared-output witness JFS-3.

### Verdict

\[
\boxed{\text{Arithmetic Leakage: NONE / below AL0.}}
\]

Reasons:

- the active carrier has exactly three points;
- no external linear order is part of any construction;
- no directed path, successor, betweenness, EqGap, addition graph, or multiplication graph is compiled;
- JFS-3 uses only equality of anonymous terminal outputs across two operation symbols;
- the joint structure becomes rigid, but rigidity of a fixed finite structure is not uniform recovery of arithmetic across an unbounded family.

## 3. Specific audit of JFS-3

JFS-3 is

\[
a\oplus a=u,
\qquad
b\otimes b=u,
\qquad
c\otimes c=v.
\]

Its new information is the cross-operation statement

\[
a\oplus a=b\otimes b
\]

versus

\[
a\oplus a\ne c\otimes c.
\]

This distinguishes `b` from `c` jointly, but contains no rank, orientation, distance, or arithmetic law.

The mechanism is output-synchronization only. It is therefore strictly safer, from the arithmetic-leakage perspective, than G4-A order memory.

## 4. Scalable DD path family

The scalable family uses two undirected paths. Each reduct remembers a path up to reversal; the joint reduct is rigid because the residual path reversals are transverse.

Finite rigidity does not by itself prove a uniform parameter-free definition of the canonical external order. No AL0 claim is made.

## 5. Scalable value lifts

Any scalable value-coloring family derived from external order remains quarantined until uniform order/leakage behavior is classified.

The new JFS mechanism suggests a safer alternative scalable research direction: seek families based on incompatible output-lift constraints that do **not** encode a path or total order at all.

## 6. Firewall summary

| witness | successor | full order | addition/EqGap | multiplication | status |
|---|---|---|---|---|---|
| DD-3 | no uniform family claim | no | no | no | safe |
| DV-I-3 | no uniform family claim | no | no | no | safe |
| VV-I-3 | no uniform family claim | no | no | no | safe |
| JFS-3 | no uniform family claim | no | no | no | safe |
| scalable DD paths | not established | not established | not established | not established | quarantine |
| scalable value lifts | not established | not established | not established | not established | quarantine |

## 7. Firewall rule

Joint rigidity must never be reported as order recovery.

Shared-output equality is also not arithmetic merely because it coordinates two operation symbols. Any future scalable JFS family must still be checked for whether its pattern of shared fibers accidentally defines order, distance, EqGap, or another arithmetic gateway.
