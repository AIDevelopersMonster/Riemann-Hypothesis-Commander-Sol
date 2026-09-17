# Scientific Supervisor — Pre-v1.0 Repairs

**Date:** 2026-08-28  
**Artifact:** bilingual FCOA Sandbox Atomicity manuscript  
**Decision:** both remarks accepted and implemented  
**Claim-set effect:** none

| ID | Severity | Location | Supervisor remark | Implemented repair | Effect |
|---|---|---|---|---|---|
| S01 | C6 | §8 | Existential-representative quotient convention should be explicit because partial-algebra quotient conventions vary. | Added a displayed definition of `bar omega(bar a,bar b)=bar z` through existence of source representatives `a',b',z'` with `omega(a',b')=z'`; stated that congruence/compatibility guarantees independence of the result class from the witnessing representatives; explicitly retained existential domain semantics. | clarification only |
| S02 | C6 | §9, Exact Rank Preservation | The strongest proof should display the quotient rank supremum and both inequalities explicitly. | Expanded the well-founded-induction proof: back + IH gives `bar rho(q(x)) <= rho(x)`; forth + IH gives `rho(x) <= bar rho(q(x))`; equality follows. | proof transparency only |

## Mathematical status

Neither theorem statement, hypothesis set, counterexample, claim boundary, bibliography, nor novelty claim changed.

The quotient repair deliberately does **not** replace existential representative semantics by a stronger convention requiring all representative pairs to be defined. It only makes the already intended semantics explicit and records the well-definedness obligation for the result class.

## Release gate

Both EN and RU versions were rebuilt after the repairs and the changed §8–§9 pages were visually inspected. No undefined references/citations or overfull boxes remain.

**v1.0 gate:** `PASS`  
**Release status:** `PUBLICATION_READY`