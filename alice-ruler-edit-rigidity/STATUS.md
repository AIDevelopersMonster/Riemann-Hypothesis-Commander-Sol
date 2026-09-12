# Alice Throws Away the Ruler III — research status

**Branch:** `research/alice-ruler-edit-rigidity`  
**Working folder:** `alice-ruler-edit-rigidity/`  
**Status date:** 2026-09-13  
**Parent publication:** *Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects*  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22722951

## STATUS: RESEARCH OPEN — PROJECTIVE LOCAL BRIDGE CLOSED; ULTRA-LOW EDIT RIGIDITY CLOSED; POST-GROUP ALGEBRA CLOSED; WRONG-ORDER OBSTRUCTION CLOSED

Primary target is now corrected: upgrade phase-profile stability to **carrier-adjusted** structural/edit-distance rigidity, or identify the sharp obstruction. Exact same-order rigidity at arbitrary `o(1)` P-phase impurity is false.

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

Hence the projective edit-rigidity theorem is closed in an explicit small-constant `1/v` scale (and therefore in every `o(1/v)` regime).

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

### Identity alignment costs only `O(n)`

If the group identity is not the added Steiner-loop point `0`, transpose those two labels and transport the Boolean group law. The multiplication table changes in at most

```math
6n
```

cells.

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

---

## Closed step 4 — `PROJECTIVE_WRONG_ORDER_OBSTRUCTION`

Full proof:

`notes/PROJECTIVE_WRONG_ORDER_OBSTRUCTION.md`

Commit:

`0f9b7222388fd6d176257dd9239be52877b4b7d2`

### Exact wrong-order sequence

Using Grannell--Lovegrove's Add 4 maxi-Pasch construction, for every `k>=2` there is an STS `T_k` of order

```math
w_k=2^{2k}+3
```

whose loop order

```math
n_k=w_k+1=2^{2k}+4
```

is not a power of `2`.

Their exact Pasch count, combined with Kozlik's formula for associative triples in Steiner loops, gives

```math
\boxed{
s_k=4(w_k-7)(7w_k-48).
}
```

Hence

```math
s_k/n_k^3 = 28/w_k + O(1/w_k^2) -> 0.
```

The associator bridge then yields

```math
\boxed{1-rho_P(T_k)=Theta(1/w_k),}
```

so in particular

```math
rho_P(T_k)->1
```

along a sequence of **wrong projective orders**.

### Same-set 99% reconstruction is false

If any group law on the same `n_k`-point set were at table distance `<n_k^2/8`, the robust Boolean recovery theorem would force `n_k=2^m`, contradiction. Therefore

```math
\boxed{
\min_{\text{group laws }*\text{ on }L_k}
d_H(\circ_k,*)
\ge n_k^2/8,
}
```

while `s_k/n_k^3->0`.

Thus the former target

```math
s/n^3 -> 0
=>
t/n^2 -> 0
```

for a group law on the **same carrier** is false even for Steiner loops.

### Exact order rigidity at `o(1)` phase impurity is false

The same sequence refutes

```math
1-rho_P=o(1)
=>
v+1=2^m.
```

Therefore no unconditional theorem can take distance to `P_v` on the same order for every `rho_P->1`, since `P_v` is empty on the above orders.

### Sharp scale

The Drápal-regime lower bound for every wrong-order STS is

```math
1-rho_P
>=
3(v+1)^2/[32v(v-1)(v-3)]
=
3/(32v)+O(1/v^2).
```

The explicit Add 4 sequence has

```math
1-rho_P=O(1/v).
```

Therefore the exact projective **order-rigidity scale is Theta(1/v)** up to absolute constants.

This is a genuine sharpness result, not merely an obstruction.

---

## Corrected projective target

The projective problem must now allow a nearby carrier/order.

The Grannell--Lovegrove sequence is itself only four points away from its projective source: it is constructed from projective order `2^{2k}-1` and has order `2^{2k}+3`.

The new target is therefore:

> if `s/n^3=o(1)` (equivalently on the P-dominant branch `1-rho_P=o(1)`), recover a Boolean group / projective STS on a carrier of size `n'=n+o(n)` and show agreement on `1-o(1)` of the relevant multiplication cells / STS pairs or blocks.

This is **open**, not assumed true.

It is also the correct shape of the 99% theorem attributed to Elad Levi by Gowers--Long: an injection into a group of approximately the same size, not necessarily a group law on the identical carrier.

## Current bottleneck / next attack

1. formulate a precise carrier-adjusted edit metric compatible with STS block distance;
2. source-check/reconstruct the Levi 99% theorem in a form usable for Steiner loops;
3. determine quantitative `|n'-n|/n` and edit error from `delta_assoc`;
4. use the Add 4/Add 6 families as lower-bound/extremal tests;
5. only after projective branch is settled, move to the Hall/distributive analogue.

## Publication threshold

The branch has now crossed a stronger publication threshold than before:

1. exact local P-phase / associator certificate;
2. explicit counterexample to the naive root criterion;
3. explicit ultra-low-defect projective edit-rigidity theorem;
4. robust Boolean recovery from group distance;
5. **explicit wrong-order counterexample to uniform same-set reconstruction**;
6. **sharp `Theta(1/v)` scale for exact projective order rigidity**.

This is enough for a mathematically substantive Article III even if the carrier-adjusted 99% theorem remains open. However, because the new obstruction changes the headline theorem, hold final PDF/Zenodo until the carrier-adjusted formulation is attacked and the paper architecture is rewritten around the positive theorem + sharp obstruction dichotomy.

## Research discipline

- no theorem without proof;
- attack counterexamples first;
- keep order-spectrum assumptions explicit;
- distinguish same-order rigidity from carrier-adjusted rigidity;
- distinguish phase-profile stability from edit-distance stability;
- no intermediate PDFs;
- update this file after each closed mathematical step.
