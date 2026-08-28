# FCOA Nesting & Atomicity — Branch Closure

**Direction:** `FCOA — SOL-NESTING — Sandbox Atomicity & Composition Boundary`  
**Closure date:** 2026-08-28  
**Publication:** v1.0, DOI `10.5281/zenodo.22140527`  
**Branch state:** `MATHEMATICALLY_CLOSED`

## Closure criterion

The branch is closed because every required research question in `ROLE_AND_PROMPT.md` has a theorem, counterexample, or exact negative statement, and the resulting theorem package has passed hostile audit, prior-art audit, supervisor repair, bilingual publication audit, and archival freeze.

Publication closure alone is not being used as the criterion. The decisive point is that no unresolved theorem obligation remains inside the scope originally delegated to this branch.

## Required-question ledger

### Q1 — Left, right, and two-sided decomposition in partial noncommutative settings

**Closed.** `DEFINITIONS.md` and the publication define directional and bilateral decomposition witness classes without assuming commutativity. Side reversal is handled by an anti-automorphism theorem rather than by silently imposing symmetry.

### Q2 — Separate isolated, indecomposable, atoms, irreducibles, and nesting-minimal elements

**Closed.** The notions are formally separated. Finite witnesses show failure of the converses. `U`-irreducibility was repaired to U-transport-irreducibility, with coincidence with atoms only under explicit U-coherence.

### Q3 — Determine coincidence and divergence conditions

**Closed.** Principal exact criteria include:

\[
\operatorname{Atom}\subseteq\operatorname{MinNest}
\]

and

\[
\operatorname{Atom}=\operatorname{MinNest}
\iff
\text{every minimal SCC is an edge-free singleton}.
\]

In the well-founded case,

\[
x\text{ atomic}\iff\rho(x)=0.
\]

Under U-coherence, atomhood coincides with U-transport-irreducibility.

### Q4 — Effect of changing operations, result sorts, and UNDEF geometry at fixed carrier

**Closed.** Sandbox monotonicity gives the operation-expansion/restriction law. Terminal-value-fiber invariance isolates a class of result-sort changes that leave active atomicity unchanged. Finite examples demonstrate that changing admitted cells at fixed carrier can change atomhood.

### Q5 — Carrier erasure and loss of external order

**Closed.** Pure erasure preserving carrier, typing, `U`, operation domains and values preserves decomposition witnesses literally, hence preserves atomicity, factor graph, SCC structure and well-founded rank even when external-order symmetry is lost.

### Q6 — Finite same-point atomic/composite counterexamples

**Closed.** `SEPARATION_EXAMPLES.md` contains explicit finite witnesses, including same carrier/same `U` with different admitted operation cells, quotient destruction of atoms, triviality-collapse creation of atoms, cyclic minimal SCCs without atoms, and ordinary quotients destroying well-foundedness.

### Q7 — Reconstruct nesting from translation profiles or operation graphs without ordinary divisibility

**Closed.** The full typed operation graph together with `U` reconstructs the factor relation directly. All labeled left/right partial translations also reconstruct it. Coarse unlabeled translation counts are proved insufficient by finite counterexample. Thus the question has both a positive exact answer and a negative coarse-data boundary.

### Q8 — Classical primes as one sandbox example

**Closed.** In

\[
\mathfrak S_{\mathbb N}=(\mathbb Z_{>0},\{\cdot\},\{1\}),
\]

bilateral atoms are precisely ordinary primes. Unique factorization and the extra algebraic structure of multiplication are explicitly excluded from the general definition.

## Extra quotient obligation generated during hostile audit

The initial ordinary-quotient counterexample created one new internal obligation: identify a stronger quotient contract that safely preserves well-founded nesting and rank.

This is also **closed**.

After passing to the induced factor relation, triviality reflection plus the standard bounded-morphism forth/back conditions give:

\[
\bar\triangleleft\text{ well-founded}
\]

and

\[
\boxed{\bar\rho(q(x))=\rho(x)}.
\]

Hence atomhood is preserved exactly. This result is recorded in the v1.0 publication and the final `THEOREMS.md` ledger. No claim is made that bounded morphism is necessary for every quotient that happens to preserve rank.

## Deliverable audit

Required branch deliverables are present:

- `DEFINITIONS.md` — complete;
- `SEPARATION_EXAMPLES.md` — complete exploratory witness bank;
- `THEOREMS.md` — synchronized final theorem ledger;
- `CLASSICAL_COMPARISON.md` — complete;
- `UPSTREAM_MEMO.md` — complete;
- publication package — complete;
- prior-art audit — complete;
- publication audit — complete;
- HTML finite-witness demonstrator — complete;
- Zenodo archival record — complete.

## Publication freeze

The v1.0 claim set is frozen at:

`10.5281/zenodo.22140527`

Substantive new mathematics must not be silently appended to v1.0. It requires either a later publication version with an explicit new claim set or, preferably for a genuinely new problem, a new delegated FCOA branch.

## Final scientific status

\[
\boxed{\texttt{MATHEMATICALLY\_CLOSED}}
\]

There is no remaining question in the original Nesting & Atomicity mandate whose solution is needed to complete this branch.

Possible future research can build on this branch, but that would be a new direction rather than unfinished work here.