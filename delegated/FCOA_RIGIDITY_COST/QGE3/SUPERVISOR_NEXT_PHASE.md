# Supervisor Directive — QGE3 Post-Publication Phase

**Status:** article already published; research continues from the published result.

## 1. Freeze the publication

Treat the published QGE3 article as an immutable baseline. Do not silently rewrite its theorem set.

The hostile audit found two local repairs:

1. in the lower-bound argument for `L_q(r)`, use **left composition** on a disconnected block, `pi_i -> sigma o pi_i`, not right composition;
2. replace the existence-level extension from `q=3` to all `q>3` by the explicit fixed-point construction with fresh points `x_j` and two cells `(0,x_j),(1,x_j)` colored `j`.

If the published version does not already contain these repaired formulations, prepare a short corrigendum / v1.1 note. The main theorems remain valid.

## 2. Primary next problem: determine L_q(r)

Work on the exact extremal synchronization number

`L_q(r)` = minimum number of point-image constraints `pi_i(a)=pi_j(a)` that force an arbitrary tuple in `S_q^r` to be diagonal.

Priority order:

- exact values for `q=3` and moderate `r`;
- exact values for `r=2,3` and general `q`;
- structural lower bounds stronger than `r-1`;
- constructions beating `(q-1)(r-1)`;
- conjecture an exact formula only after exhaustive small tables support it.

Deliverables:

- `LQR_DEFINITIONS.md`
- `LQR_SMALL_TABLES.md`
- `LQR_LOWER_BOUNDS.md`
- `LQR_CONSTRUCTIONS.md`
- `verify_lqr.py`
- `LQR_STATUS.md`

## 3. Secondary theorem target: non-vacuous minimum

The current six-cell connected `Q_D != empty` witness is accepted as a witness, but its minimality is computational only.

Try to prove or disprove

`|D|_min^{connected, Q_D nonempty, q=3}=6`.

A proof should not depend on exhaustive computation. Classify `|D|=4,5` connected domains up to carrier symmetry and show why any nonempty ternary equality destroys the required source-color splitting, or find a smaller counterexample.

## 4. Characterize color-rigid T-quotients

Study which graphs `H_T(C)` can actually arise from ordered-cell domains and when their proper `k`-color partition is unique up to relabeling.

The useful target is not arbitrary unique colorability, but an FCOA realizability theorem:

- characterize realizable `H_T(C)`;
- identify sufficient local domain conditions forcing color-rigidity;
- determine whether every uniquely colorable graph is realizable as a T-quotient or find the obstruction.

## 5. Do not define multicolor alpha_q yet

Real operation-cell repair for `q>=3` is postponed until local partition ambiguity is controlled. Do not copy the binary `alpha` definition into the multicolor setting and do not claim `alpha_q <= lambda_q^ph`.

When the local theory is mature, the correct real-cell problem must include two repair layers:

1. local partition repair on `H_T(C)`;
2. inter-component phase/gluing repair.

## 6. Relation to director's current binary work

Keep QGE3 separate from the post-Article-B binary conjecture `alpha<=lambda`. The two lines may later meet through actual cell-extension theory, but current theorems use different local state spaces.

## 7. Publication threshold

Do not prepare another paper merely from more examples. Signal publication readiness only if one of the following is achieved:

- exact formula or strong asymptotic for `L_q(r)`;
- theorem-level proof of the non-vacuous six-cell minimum plus a structural classification;
- realizability/color-rigidity theorem for T-quotients;
- a genuine multicolor real-cell extension theorem.

## 8. Reporting format

Return to Commander Sol with:

1. theorem statements;
2. complete proofs or exact proof gaps;
3. minimal counterexamples;
4. exhaustive verifier output where used;
5. literature comparison;
6. explicit recommendation: continue / publication threshold reached / line exhausted.

**Directive:** continue research. The published QGE3 article is now a foundation, not the endpoint.