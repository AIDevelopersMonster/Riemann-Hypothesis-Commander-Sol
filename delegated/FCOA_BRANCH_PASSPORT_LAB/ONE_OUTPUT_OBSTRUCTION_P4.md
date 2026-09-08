# One-Output Obstruction and Exact Two-Output Minimality — P4

**Laboratory:** FCOA — SOL-PASSPORT  
**Question:** can a single terminal output produce positive value-induced rigidity?  
**Status:** theorem-level result in the pure terminal-output setting

## 1. Setup

Let `X` be an active/base structure and let `O={Omega}` be a singleton terminal-output set. Let

`star : X x X partial-> O`

be any partial operation whose values, whenever defined, are always `Omega`.

Write

`D_star(x,y) <=> Def(x star y)`.

Then necessarily

`x star y = Omega <=> D_star(x,y)`.

Thus the operation table is completely determined by its definedness relation.

## 2. One-Output Collapse Theorem

### Theorem

In the typed setting where `X` and `O={Omega}` are distinguished sorts,

`Aut(X,O;star) ~= Aut(X;D_star)`.

Equivalently, on the active sort,

`pi_X Aut(star) = Aut(D_star|X)`.

Hence

`VRI(star)=1`.

### Proof

Every automorphism of the full operation preserves definedness, so restriction gives

`pi_X Aut(star) <= Aut(D_star|X)`.

Conversely, let `g in Aut(D_star|X)`. The singleton output sort has only one permutation, so `Omega` is fixed. For every pair `(x,y)`,

`x star y` is defined iff `D_star(x,y)`,

which holds iff `D_star(gx,gy)`,

which holds iff `(gx) star (gy)` is defined. Whenever either side is defined, both values equal `Omega`. Therefore `g`, together with the fixed action on `Omega`, is an automorphism of `star`.

Thus the groups are equal. QED.

## 3. Fiber-Transport interpretation

The value-fiber partition of the domain has exactly one block: the whole domain `D_star`.

Every automorphism of the definedness structure preserves this one-block partition automatically. Hence the fiber-partition stabilizer is the entire definedness group.

This is the one-output degeneration of Fiber Transport.

## 4. One-sorted version

Consider the one-sorted universe

`U = X disjoint_union {Omega}`

with no operation involving `Omega` as an argument.

An unqualified statement about `Aut(U;star)` versus the full one-sorted definedness group requires a carrier-separation hypothesis, because after value erasure `Omega` may become indistinguishable from unused base elements.

A sufficient intrinsic hypothesis is:

> every base element occurs as an argument in at least one defined operation cell.

Then `X` is internally recoverable as

`Arg(z) <=> exists y [D(z,y) or D(y,z)]`,

while `Omega` is the unique element outside the active argument set if there are no other inactive elements.

Under this hypothesis every one-sorted automorphism preserves `X` and fixes `Omega`; therefore the same collapse theorem holds:

`pi_X Aut(star)=Aut(D_star|X)`

and active-sort `VRI=1`.

If inactive base elements are present, the active-sort formulation remains the correct invariant and the full one-sorted group may gain carrier-mixing symmetries. This is a sorting caveat, not value-induced rigidity.

## 5. Stronger formulation over an arbitrary fixed backbone

Let `B` be any already fixed base structure on active sort `X`. Add a singleton terminal-output layer

`star_D(x,y)=Omega <=> D(x,y)`.

Then

`Aut(B,D,O;star_D) ~= Aut(B,D)`.

So a one-output terminal layer can reduce symmetry only through **where it is defined**, never through its values.

Therefore its incremental Value-Rigidity Index is always 1.

This statement covers one-output domain compilation such as G2: G2 can create strong internal memory, but that memory lies entirely in domain geometry, not in value geometry.

## 6. Exact minimality consequence

P3 constructs, for every `n>=3`, a pure partial operation with exactly two terminal outputs such that

`Aut(D|X_n) ~= S_n`,

`Aut(star) ~= C2`,

and

`VRI(star)=n!/2 > 1`.

P4 proves that with exactly one terminal output,

`VRI(star)=1`

for every pure terminal-output operation in the typed/active-sort setting.

Therefore the minimum terminal-output cardinality required for any positive value-induced rigidity is exactly

`min |O| = 2`.

Since P3 already achieves factorial growth with `|O|=2`, the same cardinality is also minimal for unbounded and factorial VRI.

### Exact Two-Output Minimality Theorem

In the class of finite partial operations whose active/base sort is separated from a pure terminal-output sort and whose VRI is measured relative to the active-sort definedness reduct:

1. `|O|=1` implies `VRI=1`;
2. `|O|=2` permits `VRI=n!/2` on `n` active points.

Hence two terminal outputs are necessary and sufficient for nontrivial value-induced rigidity, and already sufficient for factorial amplification.

## 7. What this theorem does not say

It does not claim that a one-output extension cannot make a structure rigid. It can, by encoding a rigid relation into definedness. G2 is exactly this phenomenon.

The theorem says something sharper:

> with one output, any rigidity gained is domain-induced, never value-induced beyond definedness.

It also does not apply to structures that already contain additional nonterminal values whose equality pattern contributes independent value information. The cardinality statement concerns the pure terminal-output alphabet responsible for the value layer being measured.

## 8. Programme consequence

The output-cardinality hierarchy is now exact:

- zero/one value fiber: domain geometry only;
- two anonymous value fibers: first possible genuinely value-induced rigidity;
- two fibers already suffice for factorial amplification.

Thus the cardinality threshold is not asymptotic or merely experimental:

`1 -> impossible`, `2 -> factorially sufficient`.
