# Alice Throws Away the Ruler III — research status

**Branch:** `research/alice-ruler-edit-rigidity`  
**Working folder:** `alice-ruler-edit-rigidity/`  
**Status date:** 2026-09-13  
**Parent publication:** *Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects*  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22722951

## STATUS: RESEARCH OPEN — PROJECTIVE LOCAL BRIDGE CLOSED; ULTRA-LOW EDIT RIGIDITY CLOSED; POST-GROUP ALGEBRA CLOSED; WRONG-ORDER OBSTRUCTION CLOSED; PASCH LOCALIZATION CLOSED; NEAR-CARRIER OBSTRUCTION CLOSED

Primary target is now corrected again: the robust projective statement cannot be same-carrier and cannot require injection of all points into a Boolean/group carrier of size `(1+o(1))n`. The next viable target is **large projective-core stability after deleting `o(n)` exceptional points and making `o(n^2)` block/pair repairs**.

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
Assoc(y,z,x),
Assoc(x∘y,y,z).
```

The third identity is exactly the missing Fano condition

```math
(x∘y)∘(y∘z)=x∘z.
```

### Destructive audit result

An explicit Pasch trade in the projective `STS(15)=PG(3,2)` produces a D-phase root for which **all six permutations of the root associate**, while the derived associativity identity fails. Therefore root associativity by itself cannot characterize P-phase.

---

## Closed step 2 — `PROJECTIVE_DRAPAL_EDIT_RIGIDITY`

Full proof:

`notes/PROJECTIVE_DRAPAL_EDIT_RIGIDITY.md`

Commit:

`5ab6870d986b3c94bbad6717bf6496b411a65ff8`

For the Steiner loop of `STS(v)`, if

```math
s=F_assoc < 3(v+1)^2/32,
```

then `v+1` is a power of `2` and there exists a projective Steiner triple system `T` on the same point set with

```math
\boxed{
d_blk(S,T)<s/[3(v+1)v(v-1)].
}
```

Hence the projective edit-rigidity theorem is closed in an explicit small-constant `1/v` scale (and therefore in every `o(1/v)` regime).

---

## Closed step 3 — `ROBUST_BOOLEAN_RECOVERY_FROM_GROUP_DISTANCE`

Full proof:

`notes/ROBUST_BOOLEAN_RECOVERY_FROM_GROUP_DISTANCE.md`

Commit:

`4dd80fc1ffbfc25dcb6e213ac75321f30fbd4b33`

Any same-set group law at table distance

```math
t<n^2/8
```

from a Steiner loop is automatically elementary abelian `2`; after aligning identities at `O(n)` cost it yields a projective STS with exact conversion

```math
d_blk(S,T)=t_0/[v(v-1)].
```

---

## Closed step 4 — `PROJECTIVE_WRONG_ORDER_OBSTRUCTION`

Full proof:

`notes/PROJECTIVE_WRONG_ORDER_OBSTRUCTION.md`

Commit:

`0f9b7222388fd6d176257dd9239be52877b4b7d2`

Using Grannell--Lovegrove's Add-4 maxi-Pasch construction, for every `k>=2` there is an STS `T_k` of order

```math
w_k=2^{2k}+3
```

with loop order `n_k=2^{2k}+4`, not a power of `2`, and exact associativity defect

```math
\boxed{s_k=4(w_k-7)(7w_k-48).}
```

Hence

```math
s_k/n_k^3=28/w_k+O(1/w_k^2)->0,
```

while every group law on the same carrier stays at distance at least `n_k^2/8`. Therefore uniform same-carrier `99% associativity => o(n^2)` group reconstruction is false even for Steiner loops.

The same construction, together with the Drápal lower bound, proves the exact projective order-rigidity scale is

```math
\boxed{Theta(1/v)}
```

up to absolute constants.

---

## Closed step 5 — `PROJECTIVE_PASCH_LOCALIZATION_AND_CARRIER_GAP`

Full proof:

`notes/PROJECTIVE_PASCH_LOCALIZATION_AND_CARRIER_GAP.md`

Commit:

`39d81ee754208e416fe003817fead0df33b118ba`

### Exact blockwise defect geometry

For a block

```math
B={x,y,x∘y}
```

let `p(B)` be the number of Pasch configurations through `B`, and let

```math
r_xy=d_H(T_{x∘y},T_xT_y).
```

Then

```math
\boxed{r_{xy}=r_{x,x∘y}=r_{y,x∘y}=(v-3)-p(B).}
```

Thus associator defect is not an abstract Latin-square error: it is exactly the **local Pasch-incidence deficit of the STS block**.

Summing over blocks recovers

```math
\boxed{s=v(v-1)(v-3)-24P(S)=24(M(v)-P(S)).}
```

### Exact `C14` equivalence

Each associativity failure determines the classical seven-point four-block configuration `C14`, and each `C14` gives exactly four ordered failures. Therefore

```math
\boxed{s=4c_{14}.}
```

Hence the projective stability problem is exactly an STS-relative sparse `C14`-removal/stability problem.

### Regularized core

If `delta=s/n^3`, deleting at most `sqrt(delta)n` points leaves every surviving point with first-coordinate associator load at most

```math
sqrt(delta)n^2.
```

This is rigorous regularization, but not yet a projective-core theorem.

### Near-carrier injection is also impossible

Suppose `phi:L->G` is injective and preserves all but `t_phi` products. Then `G` contains at least

```math
n-2t_phi/n
```

involutions. If `G` is non-Boolean and `|G|=lambda n`, then necessarily

```math
\boxed{t_phi/n^2 >= 1/2-3lambda/8.}
```

Thus when `|G|=(1+o(1))n`, vanishing product error forces `G` to be Boolean.

For the Add-4 sequence `n_k=2^{2k}+4`, the smallest Boolean group large enough for an injection has order `2^{2k+1}`, so its size ratio tends to `2`, not `1`. Therefore there is **no** reconstruction of all points into a group of order `(1+o(1))n` with `o(n^2)` product errors.

This strengthens the wrong-order obstruction: both same-carrier and near-supercarrier formulations are false.

---

## Corrected projective target — LARGE PROJECTIVE CORE

The Add-4 obstruction does not kill deletion/core stability: its carrier is only four points larger than the projective source.

The next honest target is:

> If `1-rho_P=o(1)`, can one delete `o(v)` exceptional points and then, after `o(v^2)` repairs, obtain a projective STS / Boolean loop on a projective order `q-1` with `q=2^m=v+1-o(v)`?

Two versions must be separated:

1. **partial-core agreement:** compare only products/pairs remaining inside the large core;
2. **subsystem reconstruction:** after deletion and `o(v^2)` repairs, the retained structure is itself projective.

Attack (1) first.

The preferred internal language is now

```math
associator failures
<-> block Pasch deficits
<-> C14 occurrences.
```

Generic dense hypergraph removal is not enough without an STS-relative/sparse normalization because an STS has only `Theta(v^2)` blocks among `Theta(v^3)` possible triples.

## Current bottleneck / next attack

1. prove or refute large-core stability from `c14=o(v^3)`;
2. exploit the block weights `d(B)=(v-3)-p(B)` and their incidence distribution;
3. test Add-4/Add-6 and other high-Pasch constructions as extremal lower bounds for required vertex deletion;
4. search specifically for STS-relative linear-hypergraph removal/stability results preserving pair-completion;
5. only after projective core stability is resolved, move to the Hall/distributive analogue.

## Publication threshold

The branch is firmly publication-ready as a positive-theorem + sharp-obstruction paper even if large-core stability remains open. The new blockwise Pasch localization and the strengthened near-carrier obstruction materially improve the Article III architecture.

Hold final PDF/Zenodo until the large-core question receives one serious proof attack and the paper is rewritten around:

- local associator certificate;
- ultra-low exact rigidity;
- sharp `Theta(1/v)` order obstruction;
- blockwise Pasch / `C14` defect geometry;
- impossibility of same-carrier and `(1+o(1))` supercarrier reconstruction;
- corrected large-projective-core conjecture.

## Research discipline

- no theorem without proof;
- attack counterexamples first;
- keep order-spectrum assumptions explicit;
- distinguish same-order, supercarrier, and deletion/core notions of rigidity;
- distinguish phase-profile stability from edit-distance stability;
- no intermediate PDFs;
- update this file after each closed mathematical step.
