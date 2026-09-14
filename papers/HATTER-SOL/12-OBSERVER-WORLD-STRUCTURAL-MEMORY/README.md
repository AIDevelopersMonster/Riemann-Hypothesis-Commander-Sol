# HATTER-SOL-12 · Observer–World Structural Memory

**Working title:** *Observer Laws, World Rotation, and Structural Memory of an Integer*  
**Russian working title:** «Законы наблюдателя, вращение по мирам и структурная память числа»  
**Series:** HATTER-SOL · Arithmetic Tea Party  
**Branch:** `research/hatter-sol-observer-world-structural-memory`  
**Parent:** HATTER-SOL-11 · ORBITAL-PORT-FILTRATIONS  
**Status:** active theory construction  
**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** `0009-0008-6009-3196`

## Central thesis

A rational integer has one numerical value, but its admissible structural realizations may depend on the arithmetic world, the quotient through which it is observed, the network/geometry carrier, and the observation scale.

HATTER-SOL-12 studies the resulting four-way object

\[
\boxed{(n,W,C,O)}
\]

rather than collapsing immediately to a single invariant.

- `n` — the integer probe;
- `W` — the arithmetic world;
- `C` — the carrier/geometry/topology class;
- `O` — the observer or quotient.

The theory asks two different questions:

1. **generation:** what structural states of `n` exist in world `W` on carrier `C`?
2. **observation:** which of those states remain distinguishable under `O`?

This separation is essential. A world generates structure; an observer forgets distinctions; a carrier imposes global compatibility.

## Why HATTER-SOL-11 is the parent

HATTER-SOL-11 supplied the prototype chain

\[
\Omega\longrightarrow\Xi\longrightarrow(P,Q),
\]

and exact geometry-controlled collisions such as

\[
3\longrightarrow2\longrightarrow1.
\]

HATTER-SOL-12 does not replace that theorem. It abstracts the mechanism: several structural states can project to the same observable state, and changes of world, carrier, or observer can split or merge those fibers.

## The paper will not collapse to one mechanism

The following layers remain deliberately distinct until hostile audit:

1. **world rotation** — prime-toggle and later other canonical world transitions;
2. **polynomial digits** — `Z_W(n;X,Y)` and mixed world derivatives;
3. **observer hierarchy** — scalar, threshold-bit, typed, orbital, polynomial and combined observers;
4. **carrier hierarchy** — path, outerplanar, planar, toroidal and later surface carriers;
5. **topological memory** — homology/holonomy-like global constraints when justified;
6. **embedded geometry memory** — curvature or other geometric sectors when the embedding itself is part of the model;
7. **scale** — host-size dependence and critical memory-loss thresholds.

No one layer is declared fundamental in advance.

## Canonical response field

The working object is a structured state family

\[
\mathsf S(n;W,C)
\]

with observation map

\[
O:\mathsf S(n;W,C)\to Y_O.
\]

For an observed value `y`, the hidden structural fiber is

\[
\boxed{\mathcal F_O(n;W,C;y)=O^{-1}(y).}
\]

When finite, its raw distinguishability is

\[
M_O=\log_2|\mathcal F_O|.
\]

This is a structural multiplicity measure, not automatically Shannon information and not automatically payload capacity.

## Current exact seeds

- `WORLD_DIGIT_FIELD.md` — polynomial-valued world digits and exact finite-cube reconstruction.
- `MAXIMAL_FACTOR_BIT_OBSERVER.md` — a deliberately coarse factor-depth observer and its threshold hierarchy.
- Parent HATTER-SOL-11 torus seed — exact geometry-induced observability transition, retained as a carrier example rather than the definition of HATTER-SOL-12.

## Publication discipline

HATTER-SOL-12 is the theory paper. It may establish observer laws, world-response reconstruction, carrier/observer monotonicity, structural-fiber notions, finite/infinite world expansions, and explicit separation examples.

It will **not** claim cryptographic security, practical error correction, self-synchronization performance or tamper resistance. Those belong to a possible HATTER-SOL-13 only after the mathematical theory identifies a non-artificial mechanism and survives prior-art and hostile audits.

## Immediate programme

1. Prove the general observer laws.
2. Preserve the world-digit field without claiming independent infinite entropy.
3. Define canonical observation horizons and truncations.
4. Build at least one explicit separation ladder: the same integer seen by successively richer observers.
5. Build at least one carrier separation: the same world/observer on different carrier classes.
6. Test whether an infinite family of worlds gives genuinely unbounded response diversity or only redundant readout.
7. Audit prior art before any novelty language is frozen.

See `RESEARCH_KERNEL.md`, `ARTICLE_ARCHITECTURE.md`, `WORLD_DIGIT_FIELD.md`, `MAXIMAL_FACTOR_BIT_OBSERVER.md`, and `STATUS.md`.
