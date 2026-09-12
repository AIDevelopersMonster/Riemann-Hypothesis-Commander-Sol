# Alice Throws Away the Ruler III — research status

**Branch:** `research/alice-ruler-edit-rigidity`  
**Working folder:** `alice-ruler-edit-rigidity/`  
**Status date:** 2026-09-12  
**Parent publication:** *Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects*  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22722951

## STATUS: RESEARCH OPEN — PROJECTIVE LOCAL BRIDGE CLOSED; ULTRA-LOW EDIT RIGIDITY CLOSED

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
\boxed{(1-rho_P)/3 <= delta_ind <= 1-rho_P}.
```

For the full loop table,

```math
\boxed{
[v(v-1)(v-3)/(3(v+1)^3)](1-rho_P)
<= delta_L
<= [v(v-1)(v-3)/(v+1)^3](1-rho_P)
}.
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

The closed bridge gives immediately

```math
delta_L=O(epsilon).
```

So no additional local charging argument is needed between phase purity and almost-associativity.

---

## Closed step 2 — `PROJECTIVE_DRAPAL_EDIT_RIGIDITY`

Full proof:

`notes/PROJECTIVE_DRAPAL_EDIT_RIGIDITY.md`

Commit introducing the proof note:

`5ab6870d986b3c94bbad6717bf6496b411a65ff8`

### Imported theorem checked

Aleš Drápal, *On quasigroups rich in associative triples*, Discrete Mathematics 44 (1983), 251–265, gives for a quasigroup of order `n`:

```math
1 <= s < 3n^2/32
\quad\Longrightarrow\quad
3tn < s,
```

where `s` is the number of failed associativity triples and `t` is the Hamming distance to a group operation on the same underlying set.

This is an exact same-set theorem, but only in the ultra-low-defect scale `s=O(n^2)`.

### New branch theorem

For the Steiner loop of `STS(v)`, if

```math
s=F_assoc < 3(v+1)^2/32,
```

then:

1. `v+1` is a power of `2`;
2. the approximating group is forced to be an elementary abelian `2`-group with the same identity `0`;
3. there is a projective STS `T` on the same point set such that

```math
\boxed{
d_blk(S,T)
< s/[3(v+1)v(v-1)].
}
```

The proof that the nearby group is Boolean uses only the Steiner translation identities and the strict bound `t<(v+1)/2`.

### Phase-density form

A sufficient condition is

```math
1-rho_P
<
3(v+1)^2/[32v(v-1)(v-3)].
```

Then

```math
\boxed{
d_blk(S,T)
< [(v-3)/(3(v+1))](1-rho_P).
}
```

If `v+1` is not a power of `2`, this yields the explicit order gap

```math
\boxed{
1-rho_P
>=
3(v+1)^2/[32v(v-1)(v-3)].
}
```

Thus wrong projective order has phase impurity at least `Theta(1/v)`.

### Anti-mitre consequence

On the P-dominant branch, Article II gives `1-rho_P=O(epsilon)` with `epsilon=c_A/N`. Hence any sequence with

```math
epsilon=o(1/v)
```

is eventually projective-order compatible and satisfies

```math
d(S,P_v)=O(epsilon).
```

This is a genuine edit-distance reconstruction theorem, but only in the ultra-low-defect regime.

---

## Literature/stability audit

- **Drápal 1983:** exact same-set Hamming reconstruction, strong enough only for `s<3n^2/32`.
- **Gowers–Long 2020:** addresses positive-density partial associativity via rough approximate groups, but does not directly give whole-table Hamming closeness to a group.
- **Levi 99% result:** reported in Gowers–Long, but the accessible citation is thesis/private-communication level; not yet suitable as a publication-grade imported theorem without source verification.
- **Modern property testers:** do not automatically convert uniform associativity-failure density into whole-table Hamming distance; no such implication is imported without proof.

## Current bottleneck / next attack

The projective branch is now split cleanly by scale.

1. **Ultra-low scale `1-rho_P=O(1/v)`: CLOSED.**
2. **Uniform 99% scale `1-rho_P=o(1)`: OPEN.** Need either:
   - a checked quantitative theorem giving `t/n^2 -> 0` from `s/n^3 -> 0`, or
   - a Steiner-loop-specific proof exploiting commutativity and involutory translations.

The next research priority is the uniform 99% regime. Hall/distributive branch remains second priority.

## Publication threshold

The branch now contains:

1. a new exact local phase-to-associator theorem;
2. a destructive counterexample to the naive root criterion;
3. a new ultra-low-defect projective edit-rigidity theorem with explicit order gap and exact STS block-distance conversion.

This crosses the **research significance threshold** for a short note/section, but not yet the intended main publication threshold of Article III. Hold PDF/Zenodo until the uniform `o(1)` reconstruction is either proved or sharply obstructed.

## Research discipline

- no theorem without proof;
- attack counterexamples first;
- keep order-spectrum assumptions explicit;
- distinguish phase-profile stability from edit-distance stability;
- no intermediate PDFs;
- update this file after each closed mathematical step.
