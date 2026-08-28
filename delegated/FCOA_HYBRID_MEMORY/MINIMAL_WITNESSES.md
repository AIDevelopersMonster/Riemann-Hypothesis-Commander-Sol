# FCOA Hybrid Memory — Minimal Witnesses

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** director-repaired internal checkpoint; hostile audit still required  
**Convention:** `n=|X|` is the active carrier size. Terminal outputs lie in anonymous pure output sorts and are never operation arguments.

## 0. Notation firewall

The operation symbols in this delegated sandbox are **not** the canonical M0 operations of the main FCOA family.

The canonical M0 addition satisfies

\[
P_0\oplus P_i=P_i,
\qquad
P_i\oplus P_0=P_{i-1},
\qquad
P_i\oplus P_i=E_i^+,
\]

and is already rigid. Therefore it cannot serve as one side of a balanced hybrid witness.

To prevent confusion, this file now denotes the two abstract sandbox operations by

\[
\star,
\qquad
\diamond.
\]

Any earlier use of `\oplus,\otimes` in this branch should be read only as shorthand for two abstract partial operations, not as a claim about the exact M0 addition/multiplication tables.

The shared-output constructions below also use an ambient signature extension in which both operation symbols may take values in one common anonymous terminal-output sort. That is a legitimate FCOA-style sandbox, but it is an **extension of the canonical M0 output architecture**, not a theorem about the exact M0 pair.

## 1. Two output semantics

### Independent-output regime

The output alphabets of `\star` and `\diamond` are disjoint/typed independently. Value memory is controlled separately by the two value-fiber partitions.

### Common-output regime

Both operations map into the same anonymous terminal-output sort `O`, and one output element may occur as a value of both operations. Equality of values **across operation symbols** is then structural information.

This distinction is decisive for minimality.

## 2. What “balanced hybrid rigidity” means

We require nontrivial **active carrier action** in each reduct:

\[
\pi_X\operatorname{Aut}(\star)\ne1,
\qquad
\pi_X\operatorname{Aut}(\diamond)\ne1,
\]

but joint active rigidity:

\[
\boxed{
\pi_X\operatorname{Aut}(\star,\diamond)=1.
}
\]

Whenever the terminal output action is also forced, the full joint automorphism group is trivial as well.

The active-action condition excludes degenerate examples whose only residual symmetry permutes unused outputs while the carrier is already pointwise fixed.

## 3. Corrected active-carrier minimum

The earlier claim that every balanced hybrid witness needs `n\ge3` is false once a common output sort is allowed.

### Theorem HM-0R — active-carrier minimum

For shared-output hybrid memory,

\[
\boxed{n_{\min}=2.}
\]

One active point cannot carry a nontrivial active permutation. Two active points suffice.

### JFS-2 witness

Let

\[
X=\{a,b\},
\qquad
O=\{u,v\}.
\]

Define

\[
a\star a=u,
\qquad
b\star b=u,
\]

and

\[
a\diamond a=u,
\qquad
b\diamond b=v.
\]

Let

\[
r=(a\ b).
\]

For `\star`, the carrier swap `r` survives while fixing the used output `u` (and hence also `v` in the two-element output sort):

\[
\pi_X\operatorname{Aut}(\star)=\langle r\rangle\cong C_2.
\]

For `\diamond`, the same carrier swap survives only together with

\[
u\leftrightarrow v,
\]

so

\[
\pi_X\operatorname{Aut}(\diamond)=\langle r\rangle\cong C_2.
\]

In the joint structure the same output permutation must serve both symbols. The nontrivial carrier swap would have to satisfy simultaneously

\[
u\mapsto u
\]

and

\[
u\mapsto v,
\]

which is impossible. Therefore

\[
\boxed{\operatorname{Aut}(\star,\diamond)=1.}
\]

This is the smallest possible active carrier.

### Cell cost at `n=2`

Under the nontrivial carrier swap, every nonempty invariant subset of `X^2` is a union of two-element orbits:

\[
\{(a,a),(b,b)\},
\qquad
\{(a,b),(b,a)\}.
\]

Hence each nonempty reduct retaining the swap needs at least two defined cells. Therefore a two-point balanced JFS witness has total cell cost at least

\[
\boxed{2+2=4,}
\]

and JFS-2 attains this bound.

## 4. DD-3 — minimum cell cost for pure domain-domain synergy

Let

\[
X=\{a,b,c\}.
\]

Define only

\[
a\star a=\alpha,
\qquad
b\diamond b=\beta,
\]

with anonymous terminal outputs.

Then

\[
\pi_X\operatorname{Aut}(\star)=\langle(b\ c)\rangle\cong C_2,
\]

\[
\pi_X\operatorname{Aut}(\diamond)=\langle(a\ c)\rangle\cong C_2,
\]

while

\[
\boxed{\pi_X\operatorname{Aut}(\star,\diamond)=1.}
\]

Total cost is

\[
\boxed{1+1=2.}
\]

Thus `n=3` is not the global active-carrier minimum, but it is the first carrier size on which the absolute two-cell DD cost can be attained.

## 5. Value memory inside one operation

### Lemma HM-V2

Let one partial operation have at most two defined cells and anonymous terminal outputs. Restoring its values cannot reduce the active automorphism group of its definedness reduct.

### Proof

Values contribute the equality partition of the defined cells. A set of size `0` or `1` has one partition. A set of size `2` has only the indiscrete and discrete partitions; both are invariant under every permutation of the two cells. Hence every domain automorphism preserves the value-equality partition. `□`

Consequently, in the independent-output regime, an operation that contributes genuine value rigidity needs at least three defined cells.

## 6. Independent-output minima

### DV-I

One operation contributes one domain cell and the other contributes a genuine three-cell value partition. The sharp cost remains

\[
\boxed{1+3=4.}
\]

### VV-I

If **each operation separately** must have a value partition that reduces its own definedness automorphism group, then each requires at least three cells by HM-V2. Hence

\[
\boxed{3+3=6}
\]

is sharp **only for VV with independent output alphabets / separate intra-operation value effects**.

It is not the global hybrid value threshold.

## 7. JFS-3 — global minimum cell cost for value-induced joint memory

Let

\[
X=\{a,b,c\},
\qquad
O=\{u,v\}.
\]

Define exactly three cells:

\[
\boxed{a\star a=u,}
\]

\[
\boxed{b\diamond b=u,
\qquad
c\diamond c=v.}
\]

The active transposition

\[
r=(b\ c)
\]

survives in each reduct separately.

For `\star`, the surviving lift fixes `u`. For `\diamond`, the nontrivial lift swaps `u,v`. No common lift exists. Thus

\[
\boxed{\operatorname{Aut}(\star,\diamond)=1,}
\]

while joint definedness still has the `C_2` carrier symmetry.

Erasing either operation's value layer restores that symmetry. This is genuine shared-output value synchronization.

## 8. Global three-cell lower bound for value-induced joint memory

Treat all defined cells as a tagged disjoint union `T`, tagged by operation symbol, and color them by their common output value.

If

\[
|T|\le2,
\]

then every equality partition of `T` is invariant under every permutation of `T`. Hence restoring values cannot shrink the joint definedness automorphism group.

Therefore:

\[
\boxed{
\text{every genuinely value-induced joint effect needs at least three total defined cells.}
}
\]

JFS-3 attains the bound.

Thus the global resource threshold remains

\[
\boxed{
2\text{ cells for pure DD},
\qquad
3\text{ cells for genuinely value-induced joint memory}.
}
\]

## 9. Pareto frontier: carrier size versus cell cost

The corrected picture is not described by one scalar minimum.

### Minimum active carrier

\[
\boxed{n=2}
\]

attained by JFS-2 with four cells.

### Minimum total cell cost for value-induced joint memory

\[
\boxed{3\text{ cells}}
\]

attained by JFS-3 on three active points.

Therefore the first Pareto points are

\[
\boxed{(n,\text{cells})=(2,4)\quad\text{and}\quad(3,3).}
\]

This is the correct replacement for the old statement “the minimal active carrier is three.”

## 10. Three-cell classification remains a separate result

For `|X|=3`, exactly three total tagged cells, nonrigid individual active reducts, nonrigid joint definedness, and rigid joint valued structure, every witness has split `1+2` or `2+1`.

Up to relabeling the one-cell operation has a loop `(a,a)` and residual swap `(b c)`. The two-cell operation domain is one of the four two-element orbits:

\[
\{(a,b),(a,c)\},
\]

\[
\{(b,a),(c,a)\},
\]

\[
\{(b,b),(c,c)\},
\]

\[
\{(b,c),(c,b)\}.
\]

A cross-operation shared output must identify the singleton-operation value with exactly one of those two cells. The previous exhaustive count

\[
48\text{ labeled witnesses},
\qquad
8\text{ operation-preserving isomorphism classes}
\]

remains a theorem candidate pending hostile audit; the corrected `n=2` witness does not invalidate this conditional three-cell classification.

## 11. Revised minimality table

| mechanism / semantics | minimum active points | minimum total cells | status |
|---|---:|---:|---|
| balanced shared-output hybrid, any cell cost | 2 | 4 at `n=2` | sharp carrier minimum |
| DD absolute cell minimum | 3 | 2 = 1+1 | sharp cell minimum |
| DV, independent outputs | 3 | 4 = 1+3 | sharp under stated semantics |
| VV, independent outputs | 3 | 6 = 3+3 | sharp under stated semantics |
| shared-output value synchronization, absolute cell minimum | 3 | 3 = 1+2 | sharp cell minimum |

## 12. Structural conclusion

Hybrid memory has at least two distinct mechanisms:

1. **transverse carrier stabilizers**;
2. **incompatible lifts of the same carrier symmetry to shared sorts**.

The second mechanism invalidates any lower-bound argument based only on intersections of carrier projections.

The correct general target is a lift-compatibility theorem for automorphisms across all shared sorts.

## 13. Arithmetic leakage

All finite witnesses above remain below the main-line AL0 order wall in the only defensible sense available here: no unbounded uniform family has been supplied that recovers order, successor, EqGap, addition, or multiplication.

Rigidity of a fixed finite witness must not be reported as arithmetic or order recovery.
