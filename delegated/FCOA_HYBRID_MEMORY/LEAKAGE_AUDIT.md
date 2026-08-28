# FCOA Hybrid Memory — Arithmetic Leakage Audit

**Status:** internal branch audit.

## 1. Scope

This audit concerns only the explicit finite witnesses in `MINIMAL_WITNESSES.md` and the scalable path families in `SYNERGY_CLASSES.md`.

The firewall questions are:

1. Is successor recovered?
2. Is full order recovered?
3. Is any internal addition-like or multiplication-like graph definable?
4. Are external index calculations smuggled into branch definitions?

## 2. Three-point witnesses DD-3, DV-3, VV-3

### Verdict

\[
\boxed{\text{Arithmetic Leakage: NONE / below AL0.}}
\]

Reason:

- the active carrier has exactly three points;
- the constructions use only one distinguished diagonal cell, or anonymous equality partitions of three diagonal values;
- no external linear order is part of the definition;
- no successor relation, directed path, betweenness, equal-gap relation, addition graph, or multiplication graph is compiled into either operation;
- the joint structure becomes rigid, but rigidity of a fixed finite structure is not uniform recovery of arithmetic across an unbounded family.

The jointly definable singleton in each witness is merely a finite relational distinction. It does not encode rank arithmetic.

## 3. Scalable DD path family

The scalable family uses two undirected paths `P` and `Q`.

Each reduct individually remembers its path only up to reversal. The joint reduct is rigid because the two path reversals are transverse.

### Order risk

A finite undirected path with distinguished orientation absent does not itself define one of the two linear orientations. The pair of transverse paths may distinguish every vertex, so a finite total ordering can be *externally listed* after rigidity, but this is not yet a proved **uniform parameter-free FO definition of the canonical external index order**.

Therefore no AL0 claim is made.

### Index leakage

The displayed path `Q` is defined by the vertex order `1,0,2,3,...`. This uses external labels only as a specification device. The actual operation contains only the explicit path edges. No addition, subtraction, distance, or rank comparison on indices appears as an operation rule.

Nevertheless, because the scalable family is indexed by `n`, any future claim of uniform order nondefinability/definability must be hostile-audited separately. This branch does not infer such a statement from finite rigidity.

## 4. Scalable value lifts

Any complete-domain value-coloring family whose fibers are chosen from an externally ordered pattern must be treated as potentially higher leakage risk than the three-point witnesses.

Before upstreaming such a family, one must prove one of:

- the coloring is uniformly interpretable in a known weak structure below AL0; or
- exact order is not uniformly recoverable; or
- if order is recoverable, classify it explicitly as AL0 and verify no EqGap/addition leakage.

No scalable value-lift is presently promoted to `UPSTREAM_MEMO.md`.

## 5. Current firewall summary

| witness | successor | full order | addition/EqGap | multiplication | status |
|---|---|---|---|---|---|
| DD-3 | no meaningful uniform family claim | no | no | no | safe |
| DV-3 | no meaningful uniform family claim | no | no | no | safe |
| VV-3 | no meaningful uniform family claim | no | no | no | safe |
| scalable DD paths | not established | not established | not established | not established | quarantine for leakage claims |
| scalable value lifts | not established | not established | not established | not established | quarantine |

## 6. Firewall rule for this branch

Joint rigidity by itself must never be reported as order recovery. A rigid finite structure can define every element orbit-theoretically without thereby yielding a uniform canonical arithmetic interpretation across the family.

The branch will therefore prefer the three-point minimal witnesses for the first upstream memo: they demonstrate genuine hybrid memory while staying maximally far from the G4-A order wall.
