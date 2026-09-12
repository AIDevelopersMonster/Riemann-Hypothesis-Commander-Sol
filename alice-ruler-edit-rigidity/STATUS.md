# Alice Throws Away the Ruler III — research status

**Branch:** `research/alice-ruler-edit-rigidity`  
**Working folder:** `alice-ruler-edit-rigidity/`  
**Status date:** 2026-09-12  
**Parent publication:** *Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects*  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22722951

## STATUS: RESEARCH OPEN — PROJECTIVE ASSOCIATOR BRIDGE CLOSED

Primary target remains: upgrade the published phase-profile stability theorem to genuine structural/edit-distance rigidity, or identify the sharp obstruction showing why the naive upgrade fails.

## Closed step 1 — `PROJECTIVE_ASSOCIATOR_BRIDGE`

Full proof:

`notes/PROJECTIVE_ASSOCIATOR_BRIDGE.md`

Commit introducing the proof note:

`f959fd2a27233d80e26f994d43cb5bfa11dca87a`

### Main result

Let `L=X∪{0}` be the Steiner loop associated with `STS(v)`, and let `rho_P` be the P-phase density of independent roots from Article II.

If

```math
F_assoc
=
|{(x,y,z)∈L^3 : (x∘y)∘z ≠ x∘(y∘z)}|,
```

and

```math
delta_ind=F_assoc/(6N),
qquad
N=v(v-1)(v-3)/6,
```

then

```math
boxed((1-rho_P)/3 <= delta_ind <= 1-rho_P).
```

For the full loop table,

```math
boxed(
[v(v-1)(v-3)/(3(v+1)^3)](1-rho_P)
<= delta_L
<= [v(v-1)(v-3)/(v+1)^3](1-rho_P)
).
```

Thus the non-P phase density and associativity-failure density are equivalent up to an absolute factor `3`.

### Exact local certificate

For an ordered independent root `(x,y,z)`, put `a=x∘y`. The root is P-phase iff all three identities hold:

```math
Assoc(x,y,z),
```

```math
Assoc(y,z,x),
```

```math
Assoc(x∘y,y,z).
```

The third identity is exactly the missing Fano condition

```math
(x∘y)∘(y∘z)=x∘z.
```

### Destructive audit result

The naive equivalence is false even in the strong root-only form.

An explicit Pasch trade in the projective `STS(15)=PG(3,2)` produces a D-phase root for which **all six permutations of the root associate**, while the derived associativity identity fails. Therefore root associativity by itself cannot characterize P-phase.

### Consequence from Article II

On the P-dominant branch Article II gives

```math
1-rho_P=O(epsilon),
qquad epsilon=c_A/N.
```

The closed bridge now gives immediately

```math
delta_L=O(epsilon).
```

So no additional local charging argument is needed between phase purity and almost-associativity.

## Current bottleneck / next attack

The projective branch is now reduced to:

> **Almost-associative Steiner-loop stability:** prove or source-check a quantitative theorem saying that a finite Steiner loop with `delta_L=o(1)` is `o(1)`-close, in multiplication-table/edit distance, to an associative elementary abelian `2`-group on the same (or controllably adjusted) order.

Required checks before importing any external theorem:

1. same-set versus nearby-set formulation;
2. quantitative dependence on associativity error;
3. whether quasigroup/Latin-square hypotheses improve the bound;
4. preservation or recovery of commutativity and exponent `2`;
5. order obstruction: closeness to a Boolean group requires `v+1` compatible with a power of `2`, unless the stability theorem itself forces order rigidity;
6. conversion from multiplication-table distance back to STS block distance.

This is now the first priority. Hall/distributive branch remains second priority.

## Publication threshold

The bridge is a genuine new local-to-algebraic theorem and satisfies success criterion 5 from the branch TЗ. It is **publication-relevant**, but not yet enough by itself to close the advertised edit-distance theorem. Hold PDF/Zenodo until the almost-associative reconstruction step is either proved or sharply obstructed.

## Research discipline

- no theorem without proof;
- attack counterexamples first;
- keep order-spectrum assumptions explicit;
- distinguish phase-profile stability from edit-distance stability;
- no intermediate PDFs;
- update this file after each closed mathematical step.
