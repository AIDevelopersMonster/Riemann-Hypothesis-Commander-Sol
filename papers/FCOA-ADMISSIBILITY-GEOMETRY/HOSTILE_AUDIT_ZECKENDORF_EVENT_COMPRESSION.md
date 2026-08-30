# Hostile Audit — Zeckendorf Event Compression and Optimal Linear AL1

**Project:** FCOA Admissibility Geometry  
**Date:** 2026-08-30  
**Audited target:** `ZECKENDORF_EVENT_COMPRESSION_OPTIMAL_AL1.md`  
**Status:** hostile audit passed within the declared base-sort/generated-history cost model  
**Reproducibility check:** `experiments/fcoa-domain-compilation/verify_event_compression_phase_split.py`

---

## 1. Audit verdict

The central theorem survives hostile audit, with one resource-accounting clarification that must remain explicit in every downstream statement:

\[
\boxed{
C_{AL1}^{\rm generated,base}(m)=\Theta(m)
}
\]

for materialized primitive support in the declared model, while the concrete self-anchored generator uses either

\[
O(\log m)
\]

transient current-word workspace or an equivalent rescan of already materialized events.

No hidden Fibonacci-index oracle, rank oracle, addition table, multiplication table, EqGap oracle, final-size oracle, or uncharged growing auxiliary carrier is required.

The proof separates cleanly into five independent obligations:

1. exact one-up combinatorics;
2. exact event-count telescoping;
3. FO recovery of full Zeckendorf incidence from events;
4. reverse FO recovery of events from full incidence;
5. provenance-safe generation and applicability of the existing linear lower bound.

All five pass.

---

## 2. Attack A — does successor really create exactly one new `1`?

Use shifted Fibonacci weights

\[
F_0=1,\qquad F_1=2,\qquad F_{j+2}=F_{j+1}+F_j.
\]

Let `F_j` be the least summand in the canonical Zeckendorf representation of `n`:

\[
n=H+F_j,
\]

where every summand in `H` has index at least `j+2`.

For `j\ge1`,

\[
F_j-1=F_{j-1}+F_{j-3}+F_{j-5}+\cdots .
\tag{2.1}
\]

### Lemma 2.1 — identity (2.1)

Identity (2.1) holds for every `j>=1`, ending in `F_0` when `j` is odd and in `F_1` when `j` is even.

### Proof

For `j=1`, `F_1-1=1=F_0`. For `j=2`, `F_2-1=2=F_1`.

Assume the identity for `j`. Then

\[
F_{j+2}-1
=F_{j+1}+F_j-1
=F_{j+1}+(F_{j-1}+F_{j-3}+\cdots),
\]

which is exactly the alternating expansion required for `j+2`. The two base cases therefore propagate to all parities. `□`

The right-hand side contains pairwise nonconsecutive Fibonacci indices. Its largest lower term has index `j-1`; every term of `H` has index at least `j+2`. Hence

\[
n-1=H+(F_j-1)
\]

is already canonical. Passing from `n-1` to `n` deletes exactly the alternating lower summands and inserts exactly the single summand `F_j`.

Therefore

\[
\boxed{|U(n,\cdot)|=1\quad(n\ge1).}
\tag{2.2}
\]

No exceptional carry pattern creates a second `0->1` digit.

**Verdict A:** PASS.

---

## 3. Attack B — can the linear event count fail off Fibonacci endpoints?

Let

\[
s_F(n)=\sum_j\varepsilon_j(n)
\]

and let `d_n` be the number of `1->0` events in the increment `n-1 -> n`.

By (2.2), exactly one new `1` is created, so

\[
s_F(n)-s_F(n-1)=1-d_n.
\]

Thus

\[
d_n=1+s_F(n-1)-s_F(n).
\tag{3.1}
\]

Summing (3.1) over every increment of an arbitrary prefix `[m]` gives

\[
|D_m|=m-1-s_F(m-1),
\tag{3.2}
\]

while

\[
|U_m|=m-1.
\tag{3.3}
\]

Hence exactly

\[
\boxed{|U_m|+|D_m|=2m-2-s_F(m-1).}
\tag{3.4}
\]

This is not an endpoint asymptotic. It is an exact identity for every `m>=1`.

Since the largest Zeckendorf index below `m` is `O(log m)`,

\[
s_F(m-1)=O(\log m),
\]

and therefore

\[
|U_m|+|D_m|=2m+O(\log m)=\Theta(m).
\]

**Verdict B:** PASS.

---

## 4. Attack C — does latest-event integration really reconstruct every digit?

Define

\[
Event(t,p):=U(t,p)\lor D(t,p).
\]

Let

\[
Latest(t,p,x)
\]

mean that `t<=x`, an event occurs at `(t,p)`, and no later event at column `p` occurs by time `x`.

Then define

\[
\widehat Z(x,p)
\iff
\exists t\,[Latest(t,p,x)\land U(t,p)].
\tag{4.1}
\]

Potential failure modes are:

- a column has no event at all;
- the first event is a deletion;
- the zero row needs a special seed;
- finite-prefix truncation hides a later event needed to determine the current value.

All four are harmless.

Every digit starts at value `0`. A first deletion is therefore impossible by construction. If a column has no event up to `x`, (4.1) is false, correctly returning `0`. The zero row is the all-zero Zeckendorf representation, so no initial positive seed is needed. Finally, the value at time `x` depends only on events at times `<=x`; future events beyond the finite prefix are irrelevant.

Thus for every `x,p<m`,

\[
\boxed{\widehat Z(x,p)\iff Z(x,p).}
\tag{4.2}
\]

The definition uses only the primitive event relations and the base linear order.

**Verdict C:** PASS.

---

## 5. Attack D — is interdefinability genuinely uniform?

From full incidence, predecessor in the row coordinate is FO-definable from `<`:

\[
Pred(y,x):=y<x\land\neg\exists z(y<z<x).
\]

For `x>0`,

\[
U(x,p)
\iff
Z(x,p)\land\exists y(Pred(y,x)\land\neg Z(y,p)),
\tag{5.1}
\]

\[
D(x,p)
\iff
\neg Z(x,p)\land\exists y(Pred(y,x)\land Z(y,p)).
\tag{5.2}
\]

At `x=0`, both formulas are false because no predecessor exists, matching the convention that no zero-row event is stored.

Together with (4.1), the translations are fixed formulas independent of `m`. Therefore

\[
\boxed{([m],<,Z)\equiv_{FO-def}([m],<,U,D)}
\tag{5.3}
\]

uniformly over all finite prefixes.

Consequently every previously established uniform FO upper or lower arithmetic result transfers exactly:

\[
Add,EqGap\in FO(<,U,D),
\]

and

\[
Mul\notin FO(<,U,D).
\]

**Verdict D:** PASS.

---

## 6. Attack E — is `FibPos(p)=U(p,p)` safe?

If `p=F_j`, then the canonical representation of `p` is the singleton `F_j`; by the one-up lemma the increment `p-1 -> p` creates the digit at column `p`, so `U(p,p)` holds.

Conversely, if `U(p,p)` holds, column `p` must be a valid digit anchor of the Zeckendorf incidence system. By the self-anchor invariant of the hostile-audited full construction, digit anchors are exactly Fibonacci weights.

Hence

\[
\boxed{FibPos(p)\iff U(p,p).}
\tag{6.1}
\]

The event structure therefore retains its own digit-coordinate anchors without an external Fibonacci predicate.

**Verdict E:** PASS.

---

## 7. Attack F — hidden workspace / hidden oracle

The most serious provenance question is whether the event-only final structure can be generated without retaining the full `Z` table as a free primitive.

The answer is yes, but the resource passport must distinguish **materialized support** from **transient generator workspace**.

At step `n`, the self-anchored Zeckendorf successor procedure scans the current canonical word over already generated anchors and computes the next word by fixed finite control plus the current `O(log n)` digit string. It emits only positions whose bits change:

- `U(n,p)` for `0->1`;
- `D(n,p)` for `1->0`.

The old current word can then be discarded. Equivalently, a generator may reconstruct each required old digit by scanning the latest event in its column, trading workspace for time.

The procedure never asks for:

- the numerical Fibonacci index of an anchor;
- a precomputed Fibonacci table;
- `Add`, `Mul`, or `EqGap`;
- the final prefix size `m`;
- an arbitrary size-dependent relation.

The only growing working state is the current representation itself, of `O(log n)` bits.

Therefore the correct resource statement is

\[
\boxed{
\text{materialized support }\Theta(m),\quad
\text{transient workspace }O(\log m)
}
\tag{7.1}
\]

for the direct streaming implementation.

This construction is not a unary finite-state color generator and does not contradict the `U1_FINITE_STATE_WALL` theorem.

**Verdict F:** PASS, with explicit workspace accounting retained.

---

## 8. Attack G — does the base-sort lower bound actually apply?

The existing Base-Sort Linear Support Barrier allows arbitrary `m`-dependent interpretations of a **fixed finite bounded-arity primitive signature** on the explicit ordered carrier `[m]`, charges every added primitive tuple, and uses ordinary FO queries.

The event construction uses exactly two added binary relations, `U` and `D`, on the base carrier and no uncharged growing auxiliary carrier. Hence it lies inside the lower-bound class.

Since exact AL1 entails uniform recovery of truncated addition,

\[
|U_m|+|D_m|=\Omega(m).
\]

The construction gives the matching `O(m)` upper bound. Thus

\[
\boxed{C_{AL1}^{\rm generated,base}(m)=\Theta(m)}
\tag{8.1}
\]

within the declared model.

**Verdict G:** PASS.

---

## 9. Attack H — finite verification

`verify_event_compression_phase_split.py` independently checks finite prefixes for both Zeckendorf and binary counting. For the Zeckendorf side it verifies:

- canonical greedy representations;
- exactly one `0->1` event on every increment;
- exact formulas (3.2)-(3.4);
- reconstruction of every row from the event stream.

The script is evidence against indexing and boundary mistakes. It is not used as a substitute for the proofs above.

**Verdict H:** PASS.

---

## 10. Audit conclusion

The hostile audit found no mathematical defect in the linear event theorem.

The only point requiring permanent emphasis is the two-coordinate resource passport:

\[
\boxed{
(\text{materialized support},\text{transient workspace})
=(\Theta(m),O(\log m)).
}
\]

Accordingly the status of `ZECKENDORF_EVENT_COMPRESSION_OPTIMAL_AL1.md` may be promoted from “proof complete; audit recommended” to **hostile-audited theorem checkpoint**.

The asymptotic support optimization problem for generated exact AL1 on the explicit base carrier is closed in this model.

---

## 11. Immediate consequence for the central line

Apply the same differential encoding to ordinary binary counting. Binary increment also creates exactly one new `1` bit, and if `s_2(n)` is popcount then

\[
|U^{(2)}_m|+|D^{(2)}_m|
=2m-2-s_2(m-1)
=\Theta(m).
\tag{11.1}
\]

Latest-event integration recovers the full BIT history, so the differential binary structure remains FO-equivalent to the already established BIT/AL2 presentation.

Thus there exist generated histories of the same asymptotically optimal materialized size

\[
\Theta(m)
\]

but in different arithmetic phases:

\[
\boxed{
\text{Zeckendorf events: exact AL1},
\qquad
\text{binary events: AL2}.
}
\tag{11.2}
\]

This is now a theorem-level phase split, not a density heuristic.

The next central target is therefore the **Equal-Linear-Cost Phase Separator**: a semantic invariant that distinguishes these two linear families without referring to their chosen digit names.
