# Alice Throws Away the Ruler III — research status

**Branch:** `research/alice-ruler-edit-rigidity`  
**Working folder:** `alice-ruler-edit-rigidity/`  
**Status date:** 2026-09-13  
**Parent publication:** *Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects*  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22722951

## STATUS: RESEARCH OPEN — PROJECTIVE LOCAL BRIDGE CLOSED; ULTRA-LOW EDIT RIGIDITY CLOSED; POST-GROUP ALGEBRA CLOSED; WRONG-ORDER OBSTRUCTION CLOSED; PASCH LOCALIZATION CLOSED; NEAR-CARRIER OBSTRUCTION CLOSED; PARTIAL-CORE METRIC CLOSED; ADD-4 CORE AUDIT CLOSED

Primary target is now refined to **partial projective-core stability**. Exact same-order rigidity, near-supercarrier rigidity, and literal large exact projective subsystem formulations are too strong in general.

## Closed step 1 — `PROJECTIVE_ASSOCIATOR_BRIDGE`

Full proof:

`notes/PROJECTIVE_ASSOCIATOR_BRIDGE.md`

Commit:

`f959fd2a27233d80e26f994d43cb5bfa11dca87a`

For the Steiner loop `L=X∪{0}` of `STS(v)`, with P-phase density `rho_P`, if

```math
F_assoc
=
|{(x,y,z)∈L^3 : (x∘y)∘z ≠ x∘(y∘z)}|,
```

and

```math
delta_ind=F_assoc/[v(v-1)(v-3)],
```

then

```math
\boxed{(1-rho_P)/3 <= delta_ind <= 1-rho_P}.
```

Moreover a root is P-phase iff three explicit associativity identities hold: two on the root and one derived identity. An explicit Pasch-traded `PG(3,2)` gives a D-root for which all six permutations of the root associate, so the naive root-only criterion is false.

---

## Closed step 2 — `PROJECTIVE_DRAPAL_EDIT_RIGIDITY`

Full proof:

`notes/PROJECTIVE_DRAPAL_EDIT_RIGIDITY.md`

Commit:

`5ab6870d986b3c94bbad6717bf6496b411a65ff8`

If

```math
F_assoc < 3(v+1)^2/32,
```

then `v+1` is a power of `2` and there exists a projective STS `T` on the same point set with explicit block-edit control. Thus exact same-order rigidity is proved in an explicit small-constant `1/v` scale.

---

## Closed step 3 — `ROBUST_BOOLEAN_RECOVERY_FROM_GROUP_DISTANCE`

Full proof:

`notes/ROBUST_BOOLEAN_RECOVERY_FROM_GROUP_DISTANCE.md`

Commit:

`4dd80fc1ffbfc25dcb6e213ac75321f30fbd4b33`

Any same-set group law at Hamming distance

```math
t<n^2/8
```

from a Steiner loop is automatically elementary abelian `2`; after aligning identities at `O(n)` cost, it yields a projective STS with exact conversion from table distance to block distance.

---

## Closed step 4 — `PROJECTIVE_WRONG_ORDER_OBSTRUCTION`

Full proof:

`notes/PROJECTIVE_WRONG_ORDER_OBSTRUCTION.md`

Commit:

`0f9b7222388fd6d176257dd9239be52877b4b7d2`

The Grannell--Lovegrove Add-4 maxi-Pasch construction gives an explicit wrong-order sequence of STS of order

```math
w_k=2^{2k}+3
```

with exact associativity defect

```math
\boxed{s_k=4(w_k-7)(7w_k-48).}
```

Hence `s_k/(w_k+1)^3 -> 0` and `rho_P -> 1`, while every group law on the same carrier remains at normalized table distance at least `1/8`. This disproves uniform same-carrier 99% reconstruction and shows the exact projective order-rigidity scale is `Theta(1/v)` up to constants.

---

## Closed step 5 — `PROJECTIVE_PASCH_LOCALIZATION_AND_CARRIER_GAP`

Full proof:

`notes/PROJECTIVE_PASCH_LOCALIZATION_AND_CARRIER_GAP.md`

Commit:

`39d81ee754208e416fe003817fead0df33b118ba`

### Exact blockwise defect geometry

For a block

```math
B={x,y,x∘y},
```

if `p(B)` is the number of Pasch configurations through `B`, then

```math
\boxed{r_{xy}=r_{x,x∘y}=r_{y,x∘y}=(v-3)-p(B).}
```

Hence associator defect is exactly local Pasch-incidence deficit.

Globally,

```math
\boxed{s=v(v-1)(v-3)-24P(S)=24(M(v)-P(S)).}
```

and, for the classical four-block configuration `C14`,

```math
\boxed{s=4c_{14}.}
```

Thus the projective stability problem is exactly an STS-relative sparse `C14` stability/removal problem.

### Near-supercarrier obstruction

If `phi:L->G` is injective and preserves all but `t_phi` products, then `G` contains at least `n-2t_phi/n` involutions. For a non-Boolean ambient group of size `m=lambda n`,

```math
\boxed{t_phi/n^2 >= 1/2-3lambda/8.}
```

Therefore vanishing-error embeddings of all points into groups of size `(1+o(1))n` would force the ambient group to be Boolean. The Add-4 sequence shows this is impossible: the smallest Boolean supercarrier has asymptotic size ratio `2`.

---

## Closed step 6 — `PROJECTIVE_PARTIAL_CORE_METRIC_AND_ADD4_AUDIT`

Full proof:

`notes/PROJECTIVE_PARTIAL_CORE_METRIC_AND_ADD4_AUDIT.md`

Commit:

`86d43167ea9ba8ea42501443d8b65fe413ea2749`

### Literal large exact projective subsystem is too strong

Because projective orders are `2^m-1`, the next smaller admissible projective order may be only about half as large. Therefore even a local perturbation of a projective STS need not leave an exact projective subsystem on `v-o(v)` points.

The robust notion must compare a large retained subset with a full projective model of nearby order, without requiring the retained set itself to be closed.

### Partial-core projective cost

For `S=(X,B_S)`, a projective model `P=(Y,B_P)`, a retained subset `U⊂X`, and an injection `phi:U->Y`, define a bad unordered pair `{x,y}⊂U` when either its completion leaves `U` or the completion disagrees with the projective model under `phi`.

With `N_*=max{|X|,|Y|}`, define

```math
\boxed{
D_pc(S;P,U,phi)
=
(|X\U|+|Y\phi(U)|)/N_*
+
2E/(N_*(N_*-1)).
}
```

This exactly recovers the branch block metric `d_blk` in the same-order/full-core case.

Deleting `r` points creates at most

```math
r(v-1)/2
```

boundary pair errors, so `r=o(v)` is compatible with `o(v^2)` pair error.

### Correct audit of Add-4

The previous shorthand that the Add-4 system simply contains the old projective STS plus four points was too crude. The actual construction removes three infinity points, introduces seven new points, and reroutes old pairs along a 7-regular graph `G_7` on `v-3` old points.

Comparing the resulting wrong-order system `T` of order `w=v+4` with its source projective STS on the common old core gives exactly

```math
\boxed{
D_pc(T;P_v,V',id)
=
10/w + 7(w-7)/[w(w-1)].
}
```

Hence

```math
\boxed{D_pc(T,\mathcal P)=O(1/w)->0.}
```

So Add-4 obstructs carrier identity, but not partial projective geometry.

### Almost-medial consequence

For a commutative loop, five associativity identities connect

```math
(x∘y)∘(z∘w)
```

to

```math
(x∘z)∘(y∘w).
```

Therefore if `M_med` counts failed medial/parallelogram identities,

```math
\boxed{M_med <= 5ns.}
```

Thus normalized medial defect is at most five times normalized associator defect. Exact mediality in a unital loop implies exact associativity by setting one variable to the identity.

No publication-grade quantitative repair theorem for almost-medial quasigroups has yet been located.

---

## Current projective conjecture — PARTIAL PROJECTIVE-CORE STABILITY

The first formulation surviving all destructive audits is:

> If `1-rho_P=o(1)`, then `D_pc(S,\mathcal P)=o(1)`.

Equivalently: after deleting `o(v)` points from `S`, allowing `o(v)` unused points in a nearby projective model, and permitting `o(v^2)` bad pair completions on the common core, the structure should become asymptotically projective.

This is **open**.

### Why this formulation is presently preferred

- same-carrier reconstruction: false;
- `(1+o(1))` supercarrier embedding of all points: false;
- exact projective subsystem on `v-o(v)` points: too rigid because of discrete projective orders;
- partial-core comparison: survives the Add-4 extremal test with explicit `O(1/v)` cost.

### Literature boundary

Generic dense hypergraph removal has the wrong normalization because an STS has `Theta(v^2)` blocks inside a `Theta(v^3)` host. General Latin-square repair is also not presently available as a black box: a strong removal/repair statement for Latin squares is still formulated as a conjectural direction in the modern limits literature. Therefore any proof here must use additional Steiner structure: commutativity, involutory translations, exact `C14` localization, local Pasch deficits, or the almost-medial law.

## Next attack

1. Try to prove partial-core stability directly from the block weights
   ```math
   d(B)=(v-3)-p(B).
   ```
2. Study concentration/regularization of low-defect blocks and whether their pair-completion graph admits a global Boolean coordinate system.
3. Exploit the almost-medial estimate `M_med<=5ns` and search for a Steiner-specific quantitative Toyoda--Bruck repair argument.
4. Audit Add-6 and sparse projective trades in `D_pc` to determine lower bounds on the best possible `F(delta)`.
5. If partial-core stability resists proof, close Article III around the established positive theorem + sharp obstruction + exact defect geometry + corrected conjecture.

## Publication threshold

The branch is already publication-ready as a substantial Article III. The new partial-core metric and exact Add-4 audit significantly improve the paper architecture by turning the previous obstruction into a precise corrected stability conjecture.

Hold final PDF/Zenodo only while the partial-core conjecture receives the current serious proof attack. If this next attack does not close the conjecture, prepare the paper as:

- exact local associator certificate;
- ultra-low exact projective rigidity;
- sharp `Theta(1/v)` wrong-order obstruction;
- exact Pasch / `C14` defect geometry;
- impossibility of same-carrier and near-supercarrier reconstruction;
- partial-core cost and Add-4 compatibility;
- partial projective-core stability conjecture.

## Research discipline

- no theorem without proof;
- attack counterexamples first;
- keep order-spectrum assumptions explicit;
- distinguish same-order, supercarrier, exact subsystem, and partial-core notions of rigidity;
- distinguish phase-profile stability from edit-distance stability;
- no intermediate PDFs;
- update this file after each closed mathematical step.
