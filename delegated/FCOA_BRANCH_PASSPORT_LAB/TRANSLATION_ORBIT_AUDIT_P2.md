# Translation Profiles & Output-Orbit Audit — P2

**Laboratory:** FCOA — SOL-PASSPORT  
**Target:** G3-S/G3-C/G3-A and G4-C/G4-A  
**Status:** exact structural audit; formulas cross-checked for `N=3,4,5,6`

## 1. Translation-profile convention

For a base point `x`, write

`L_x(y)=x star y`, `R_x(y)=y star x`.

For anonymous output values, profile information must be separated into:

- ordered fiber multiplicities when the outputs are internally distinguished;
- unordered multiplicity data when an automorphism may exchange the anonymous outputs.

This distinction is essential in G4-C.

## 2. G4-C generic translation fingerprints

For every generic point `P_i`, `2 <= i <= N`, the left translation is defined on every base point and contains:

- one `E_i^*` value at argument `P_0`;
- one base value `P_i` at argument `P_1`;
- one `E_i^x` value at argument `P_i`;
- `i-2` occurrences of `Omega_-` from lower generic arguments;
- `N-i` occurrences of `Omega_+` from higher generic arguments.

Hence the exact orientation multiplicity pair is

`(m_-(i),m_+(i)) = (i-2, N-i)`.

The right translation has the reversed pair:

`(m_-(R_i),m_+(R_i)) = (N-i, i-2)`.

Because `Omega_+` and `Omega_-` are anonymous in G4-C, only the unordered pair

`{i-2, N-i}`

is invariant under the full operation.

This unordered pair determines `i` exactly up to

`i <-> N+2-i`.

Therefore translation fingerprints alone prove that every full-operation automorphism maps each generic point either to itself or to its reflected partner. Compatibility across all generic points leaves only the global identity and the global reversal.

This yields an independent local proof route to

`Aut(G4-C) ~= C2`.

### Midpoint case

When `N` is even, the generic point with `i=(N+2)/2` is fixed by reversal because its multiplicities are equal. This is consistent with the global `C2` action and introduces no extra symmetry.

## 3. G4-A anchor converts an unordered fingerprint into an ordered rank coordinate

G4-A adds

`P_1 star P_0 = Omega_+`.

The inherited M0 operation distinguishes the ordered boundary pair `(P_1,P_0)` at the full-operation level. Therefore the new anchor structurally singles out the `Omega_+` fiber. `Omega_+` can no longer be exchanged with `Omega_-`.

Consequently the generic translation fingerprint becomes the ordered pair

`(i-2, N-i)`.

This pair determines `i` uniquely. Every generic `P_i` is therefore fixed pointwise.

Once all base points are fixed, all inherited and new output fibers are fixed by their preimage cells. Hence translation-profile rigidity gives a direct second proof of

`Aut(G4-A)=1`.

This proof is independent in mechanism from the Fiber-Transport theorem: it uses local translation multiplicities rather than global partition stabilization.

## 4. G3 comparison

The same translation coordinate separates the G3 mechanisms more weakly.

### G3-S

For a generic `P_i`, the number of adjacency-output occurrences in `L_i` equals its degree in the finite undirected path:

- `1` at the two endpoints;
- `2` at interior generic points.

Thus translation degree profiles distinguish endpoints from interior points but do not recover generic rank. Path reversal survives.

### G3-C

At a generic endpoint one orientation fiber occurs once and the other zero times; at an interior point each occurs once. Because the two outputs are anonymous, translation profiles again retain reflection symmetry.

### G3-A

The anchor fixes `Omega_+`, preventing the global output swap. Together with the inherited M0 backbone this removes the residual full-operation reflection, in agreement with the hostile-audited result.

## 5. Terminal-output orbits

### G4-C

Under the nontrivial full-operation automorphism (generic reversal):

- `Omega_+ <-> Omega_-` is one two-element orbit;
- inherited `E_i^*` outputs are transported to `E_{N+2-i}^*`;
- inherited `E_i^x` outputs are transported to `E_{N+2-i}^x`;
- generic base values `P_i` are transported to reflected generic base values.

Thus the two new orientation outputs are internally distinguishable as a set from the inherited E-families by preimage geometry, but not distinguishable from each other individually.

### G4-A

The full automorphism group is trivial. Every terminal output is therefore a singleton orbit. In particular `Omega_+` is internally distinguished from `Omega_-` by the boundary anchor.

## 6. Main theorem-scope finding: total terminal-output alphabet is not bounded

The current G4 note repeatedly uses formulations such as:

- `fixed finite anonymous output alphabet`;
- `bounded output alphabet`;
- `output alphabet remains fixed at exactly two anonymous values`.

Taken as statements about the **entire partial operation**, these are too strong.

The inherited M0 backbone contains, for every generic index `i`, distinct terminal outputs

`E_i^*`, `E_i^x`.

There are `N-1` outputs in each inherited family. G4 then adds exactly two new anonymous orientation outputs.

Therefore the number of terminal outputs of the complete G4 operation is

`|T_4C| = |T_4A| = 2(N-1)+2 = 2N`.

It grows with `N`.

### Correct theorem scope

What the construction actually proves is:

> Over the M0 backbone family, a fixed **two-element added anonymous orientation-output alphabet** can induce an unbounded, factorially growing value-rigidity index relative to definedness.

Equivalently:

`bounded added value alphabet over the backbone != bounded incremental value-induced rigidity`.

This remains a strong statement, but it is not the same as existence of a family of full operations whose total output alphabet is bounded independently of `N`.

### What is not yet proved

The current G4 construction does **not** prove:

> there exists a family with a globally bounded total terminal-output carrier and factorial VRI.

Obtaining that stronger theorem would require a new construction, for example one in which the inherited `E_i^*`,`E_i^x` terminal families are collapsed, removed, or replaced without destroying the backbone role distinctions needed by the argument.

No such construction is established here.

## 7. Audit verdict

The automorphism and VRI formulas of G4 survive this audit. Translation fingerprints provide an additional independent proof mechanism.

However, the headline theorem language requires a scope repair:

- **safe:** `two new anonymous orientation values`, `bounded added value alphabet`, `fixed two-value fiber layer over M0`;
- **unsafe without qualification:** `bounded output alphabet` when referring to the whole operation.

This finding is theorem-level and belongs upstream before G4 promotion.
