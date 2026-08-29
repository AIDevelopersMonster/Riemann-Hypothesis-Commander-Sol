# Two-Output Extremality — P5

**Laboratory:** FCOA — SOL-PASSPORT  
**Question:** with exactly two anonymous terminal outputs and maximally symmetric definedness, is `n!/2` the largest possible VRI?  
**Status:** theorem-level construction and exact extremal bound in the pure active-sort setting

## 1. General upper bound

For any finite active sort `X_n` with `|X_n|=n`,

`VRI(star) = [Aut(D_star|X_n) : pi_X Aut(star)]`.

Therefore

`VRI(star) <= |Aut(D_star|X_n)| <= n!`.

So `n!` is the absolute largest possible active-sort VRI on `n` points.

The question is whether exactly two anonymous terminal outputs can attain this upper bound while the definedness reduct itself remains maximally symmetric.

## 2. Maximally symmetric definedness

Let

`X_n={x_1,...,x_n}`, `n>=3`,

and let the total terminal-output set be exactly

`O={Omega_+,Omega_-}`.

Define the operation on every off-diagonal pair, leaving only the diagonal undefined. Thus

`D(x_i,x_j) <=> i != j`,

so

`Aut(D|X_n) ~= S_n`.

## 3. Rigid-path coloring

Assign `Omega_+` exactly to the directed Hamilton path

`x_1 -> x_2 -> ... -> x_n`:

`x_i star x_{i+1} = Omega_+` for `1<=i<n`.

Assign `Omega_-` to every other off-diagonal ordered pair.

Hence

`|D_+|=n-1`,

while

`|D_-|=n(n-1)-(n-1)=(n-1)^2`.

For `n>=3`, these fiber cardinalities are unequal.

## 4. Anonymous outputs become internally distinguishable

The outputs are not named, sorted separately from one another, or externally colored. Nevertheless, any full-operation automorphism must preserve preimage cardinality of terminal outputs.

Since

`n-1 != (n-1)^2`

for every `n>=3`, no automorphism can exchange `Omega_+` and `Omega_-`.

Thus both anonymous outputs are individually fixed by the operation's internal geometry.

This is not a violation of anonymity: anonymity means the outputs are not externally named; it does not require them to remain structurally indiscernible.

## 5. Full-operation rigidity

Because `Omega_+` is fixed, every full automorphism of the operation must preserve its preimage relation

`R_+ = {(x_i,x_{i+1}):1<=i<n}`.

But `R_+` is a finite directed path. Its automorphism group is trivial: `x_1` is the unique vertex with no incoming `R_+` edge, `x_n` the unique vertex with no outgoing `R_+` edge, and every intermediate point is fixed recursively by successor along the path.

Therefore

`Aut(star)=1`.

Hence

`VRI(star)=|S_n|=n!`.

## 6. Exact extremality theorem

### Two-Output Maximum VRI Theorem

For every `n>=3`, there exists a pure partial operation on `n` active points with exactly two anonymous terminal outputs such that

- its definedness relation is complete off-diagonal and has automorphism group `S_n`;
- its full operation is rigid;
- its active-sort Value-Rigidity Index is exactly

`VRI(star)=n!`.

Since no active-sort VRI on `n` points can exceed `n!`, this construction attains the absolute maximum.

Therefore the earlier orientation construction with `VRI=n!/2` is not extremal. Its factor `1/2` loss comes specifically from the balanced two-fiber coloring that admits a global complement/reversal symmetry.

## 7. Minimality plus extremality

P4 proved that one terminal output always gives

`VRI=1`.

P5 proves that two anonymous terminal outputs can attain

`VRI=n!`,

the absolute maximum possible on `n` active points.

Thus the output-cardinality hierarchy is now exact in both threshold and strength:

- `|O|=1`: no value-induced rigidity at all;
- `|O|=2`: maximal possible value-induced rigidity.

Equivalently, two terminal outputs are simultaneously:

1. minimal for any positive VRI;
2. sufficient for maximal VRI.

## 8. Why the previous reversal was not unavoidable

In the P3 orientation construction, every unordered pair receives opposite colors in opposite directions and the two fibers have equal size. This balanced design admits the unique order reversal together with output swap.

P5 breaks that accidental symmetry without adding outputs or changing definedness. The small `Omega_+` fiber is chosen to be a rigid relation, while the `Omega_-` fiber is its complement inside the complete off-diagonal domain.

The mechanism is therefore:

`maximally symmetric domain + rigid unequal value fiber = rigid full operation`.

## 9. One-sorted presentation

Take the one-sorted universe

`U_n = X_n disjoint_union {Omega_+,Omega_-}`,

with no operation involving either output as an argument.

Every base point occurs as an argument in defined cells, while the two output elements never do. Hence the active/output partition is internally recoverable.

After value erasure, the two isolated output points contribute an independent `S_2`, so

`Aut_full(D) ~= S_n x S_2`.

In the full operation, the unequal preimage cardinalities distinguish the two outputs and the rigid path fixes every base point, so the full one-sorted automorphism group is trivial.

Thus a separate full one-sorted order ratio would be `2 n!`, whereas the active-sort VRI is `n!`. The two invariants must remain explicitly separated.

## 10. General design lemma

The construction is an instance of a reusable principle.

### Rigid-Fiber Lemma

Let `D` be a maximally symmetric domain on `X`, and partition its cells into exactly two anonymous value fibers `F` and `D\F`. If

1. `|F| != |D\F|`, so the fibers cannot be exchanged;
2. the setwise stabilizer of `F` inside `Aut(D)` is trivial;

then the resulting two-output partial operation is rigid and

`VRI=|Aut(D)|`.

The directed-path construction takes `D` to be complete off-diagonal and `F` to be a rigid directed Hamilton path.

## 11. Programme consequence

The two-output cardinality problem is completely resolved in the pure terminal-output setting:

`one output -> VRI 1`,

`two outputs -> VRI n! achievable`.

No larger output alphabet is needed to reach the maximum possible active-sort rigidity amplification.
