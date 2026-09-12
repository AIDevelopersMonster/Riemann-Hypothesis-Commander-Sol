# Alice Throws Away the Ruler III — research status

**Branch:** `research/alice-ruler-edit-rigidity`  
**Working folder:** `alice-ruler-edit-rigidity/`  
**Status date:** 2026-09-12  
**Parent publication:** *Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects*  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22722951

## STATUS: RESEARCH OPEN — PROJECTIVE LOCAL BRIDGE CLOSED; ULTRA-LOW EDIT RIGIDITY CLOSED; POST-GROUP ALGEBRA CLOSED

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
Assoc(y,z,x),
Assoc(x∘y,y,z).
```

The third identity is exactly the missing Fano condition

```math
(x∘y)∘(y∘z)=x∘z.
```

### Destructive audit result

The naive equivalence is false even in the strong root-only form.

An explicit Pasch trade in the projective `STS(15)=PG(3,2)` produces a D-phase root for which **all six permutations of the root associate**, while the derived associativity identity fails. Therefore root associativity by itself cannot characterize P-phase.

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

### Consequence

For the Steiner loop of `STS(v)`, if

```math
s=F_assoc < 3(v+1)^2/32,
```

then `v+1` is a power of `2` and there exists a projective Steiner triple system `T` on the same point set with

```math
\boxed{
d_blk(S,T)
< s/[3(v+1)v(v-1)].
}
```

Hence the projective edit-rigidity theorem is closed in the ultra-low scale `1-rho_P=O(1/v)`.

---

## Closed step 3 — `ROBUST_BOOLEAN_RECOVERY_FROM_GROUP_DISTANCE`

Full proof:

`notes/ROBUST_BOOLEAN_RECOVERY_FROM_GROUP_DISTANCE.md`

Commit:

`4dd80fc1ffbfc25dcb6e213ac75321f30fbd4b33`

This step removes every algebraic obstruction **after** a same-set near-group theorem is obtained.

Let the Steiner loop have order `n=v+1`, and suppose an arbitrary group law `*` on the same set is at Hamming distance `t` from the Steiner table.

### Robust involution count

For each row `a`, compare the group translation `P_a` with the Steiner involution `Q_a`. If `a*a` is not the group identity, then

```math
r_a=d_H(P_a,Q_a) >= n/2.
```

Therefore the approximating group contains at least

```math
n-2t/n
```

involutions.

### Boolean threshold

A finite group with more than `3n/4` involutions is elementary abelian `2`. Consequently

```math
\boxed{t<n^2/8}
```

already forces the approximating group to be Boolean and forces the exact order spectrum

```math
\boxed{n=2^m}.
```

This improves the earlier absolute condition `t<n/2` to a genuine normalized constant threshold.

### Identity alignment costs only `O(n)`

If the group identity is not the added Steiner-loop point `0`, transpose those two labels and transport the Boolean group law. The multiplication table changes in at most

```math
6n
```

cells.

Thus there is a Boolean group law with identity `0` at distance at most

```math
t+6n
```

from the Steiner loop.

### Exact conversion to STS edit distance

For two Boolean/Steiner tables with common identity `0`, table mismatch and block mismatch satisfy exactly

```math
d_blk(S,T)=t_0/[v(v-1)].
```

Hence any same-set group approximation with `t<n^2/8` yields a projective STS `T` with

```math
\boxed{
d_blk(S,T)
<= (t+6n)/[(n-1)(n-2)].
}
```

Therefore, if one proves only

```math
t/n^2 <= f(s/n^3),
qquad f(delta)->0,
```

then **all remaining projective consequences follow automatically**:

- elementary abelian `2`;
- exact projective order `v+1=2^m` once `f(delta)<1/8`;
- correct distinguished zero after `o(n^2)` relabeling cost;
- projective STS on the same point set;
- block edit distance `f(delta)+o(1)`.

---

## Translation formulation of the sole remaining bottleneck

For the Steiner loop define translations

```math
T_x(z)=x∘z.
```

Every `T_x` is an involution, and Latin cancellation gives

```math
d_H(T_x,T_y)=n
```

for `x!=y`.

Moreover associativity is exactly

```math
T_{x∘y}(z)=T_xT_y(z).
```

Thus the total failure count is

```math
\boxed{
s
=
\sum_{x,y} d_H(T_{x∘y},T_xT_y).
}
```

The uniform projective problem can therefore be restated as stability of an `n`-point family of pairwise maximally separated involutions in `Sym(n)` whose products lie near the family on average.

This translation viewpoint is now the preferred route for an in-house proof.

---

## Literature/stability audit

- **Drápal 1983:** exact same-set Hamming reconstruction, but only when `s<3n^2/32`.
- **Gowers–Long 2020:** explicitly state that Elad Levi proved the 99% case: if associativity holds for almost all triples, the quasigroup table agrees almost everywhere, after injection, with multiplication in a group of approximately the same size. Published Gowers–Long do not reproduce that proof; their reference is Levi's M.A. thesis/private communication.
- **Levi source audit:** web search confirms the thesis title *Symmetric abstract independence relations and the group configuration theorem* and that Levi completed an M.A. under Ehud Hrushovski in 2013, but no accessible thesis text/proof has yet been located. Thus it is not imported as a publication-grade black box.
- **Gowers–Long positive-density theorem:** gives rough approximate-group structure for the 1% regime, not directly whole-table Hamming reconstruction.
- **Property testers:** no checked theorem yet converts uniform associativity-failure density directly into same-set group-table distance with the required quantitative control.

## Current bottleneck / next attack

There is now exactly one substantive projective obstruction:

```math
\boxed{
s/n^3 -> 0
\quad\Longrightarrow?\quad
t/n^2 -> 0
}
```

where `s` is the number of nonassociative triples of the Steiner loop and `t` is distance to a group law on the same set (or to a group law after an `o(n)`-size adjustment that can then be transferred back).

Two active routes:

1. reconstruct a proof of the Levi 99% theorem in the special Steiner setting using the translation family `T_x`;
2. derive a dense partial group law and complete it, exploiting pairwise distance `n`, involutivity, and commutativity.

Hall/distributive branch remains second priority.

## Publication threshold

The branch now contains three closed mathematical contributions:

1. exact local P-phase / associator certificate plus explicit counterexample to the naive criterion;
2. ultra-low-defect projective edit-rigidity with explicit order gap;
3. robust normalized Boolean recovery showing that **any** uniform near-group theorem immediately yields the desired projective STS reconstruction.

This is already publication-relevant as a substantial Article III core. However the intended main theorem remains the uniform `o(1)` edit-rigidity statement, so hold final PDF/Zenodo while the sole remaining 99% stability step is attacked.
