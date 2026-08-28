# FCOA Nesting & Atomicity — Upstream Memo

**Direction:** `FCOA — SOL-NESTING — Sandbox Atomicity & Composition Boundary`  
**Status:** delegated exploratory branch  
**Scientific authority:** main Commander Sol retains acceptance/rejection authority for the central FCOA line.

## Sharp results worth upstream attention

### 1. Atomicity is monotone in the allowed composition family

For fixed carrier, typing, and trivial class `U`, if sandbox `S1` is a restriction of sandbox `S2`, then

\[
\operatorname{Atom}(S_2,U)\subseteq\operatorname{Atom}(S_1,U).
\]

Thus expanding admissible composition can only destroy atoms, while restricting composition can only create them.

This is the cleanest theorem-level formulation currently supporting the phrase "atomicity is sandbox-relative".

### 2. Local atomicity and global nesting minimality are different notions

Define the nontrivial factor graph by adding edges from each nontrivial factor to the result of a two-sided nontrivial allowed composition.

A bilateral U-atom is exactly an indegree-zero vertex of this graph.

If the graph is finite and acyclic, then U-atoms are exactly the minimal points of the transitive nesting order.

If cycles are present, the equivalence fails. The correct global boundary object is a minimal strongly connected nesting class. A minimal SCC can contain no atoms at all.

This appears to be the most important conceptual repair to the original slogan:

\[
\boxed{
\text{atomicity = local composition boundary;}
\quad
\text{minimal SCC = global nesting boundary in cyclic sandboxes.}
}
\]

### 3. Rigidity memory and atomicity separate cleanly

If two sandboxes differ only in the partition/coloring of cells whose outputs are terminal, while all active-result cells are unchanged, then active-carrier atom classes are unchanged.

Therefore G3-style anonymous terminal value-fiber changes may alter automorphism groups, commutation behavior, and Value-Rigidity Index without changing active-result atomicity.

This is a direct bridge to the main FCOA domain/value programme and is likely worth retaining centrally as a warning against conflating rigidity with decomposition structure.

### 4. Pure carrier erasure preserves atomicity

If erasure removes only external labels/order/relations while preserving carrier elements, typing, `U`, and all operation cells and values, all decomposition witness sets remain unchanged. Hence atomicity survives even when external order and role distinguishability are lost.

This gives a precise positive answer to the branch question about Carrier-Erasure, under an explicit "pure erasure" hypothesis.

### 5. Nesting is reconstructible without divisibility

The one-step nontrivial nesting relation is reconstructible from the typed full operation graph, or equivalently from labeled left/right translations plus `U`. No ordinary divisibility predicate is required.

However coarse unlabeled translation summaries such as domain cardinalities do not suffice in general.

### 6. Classical primes are one acyclic special case

In

\[
(\mathbb Z_{>0},\{\cdot\},\{1\}),
\]

bilateral U-atoms are exactly ordinary prime numbers. The familiar collapse of atomicity, irreducibility, and divisibility-minimality is explained by extra unit behavior and well-foundedness/acyclicity, not by the abstract definition alone.

## Separation examples already constructed

The branch now contains explicit finite witnesses showing:

- same carrier, same `U`, different allowed cells -> same point atomic in one sandbox and composite in another;
- indecomposable need not be isolated;
- U-atomic need not be indecomposable;
- left- and right-atomicity can diverge;
- U-atomic need not be U-irreducible when `U` is merely declared trivial rather than unit-like;
- minimal nesting SCC need not contain any atom;
- terminal value recoloring can change rigidity while preserving active atomicity;
- coarse translation-count data do not determine atom classes;
- terminal results cannot be promoted to factors unless the signature explicitly admits them as arguments.

## Current claim ceiling

These results concern finite or abstract typed partial-composition sandboxes. They do **not** establish:

- unique factorization;
- existence of atomic decompositions for every element;
- a canonical notion of `U` across arbitrary signatures;
- any equivalence with ordinary divisibility outside the classical multiplicative sandbox;
- any new result about the published M0-G1-G2 chain itself;
- any validation of G4, whose main-line hostile audit remains separate.

## Recommendation to main scientific director

The strongest candidate for integration into central FCOA memory is not the philosophical phrase "primes are boundary points", but the theorem-level pair:

1. **Sandbox Monotonicity of Atomicity**;
2. **Acyclic Boundary Theorem:** atoms coincide with nesting-minimal points exactly under an acyclicity/well-foundedness hypothesis, while cycles force minimal SCCs as the correct global boundary object.

A second useful integration result is **Terminal Value-Fiber Invariance of Active Atomicity**, because it orthogonalizes this branch from G3/G4 rigidity amplification.

No publication threshold is claimed yet. The next research task should be a hostile audit of the definitions, especially `U`-irreducibility, quotient/erasure behavior, and the exact hypotheses needed to replace finite acyclicity by a well-founded rank theorem.