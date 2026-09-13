# Alice Throws Away the Ruler III — research status

**Branch:** `research/alice-ruler-edit-rigidity`  
**Working folder:** `alice-ruler-edit-rigidity/`  
**Status date:** 2026-09-13  
**Parent publication:** *Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects*  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22722951

## STATUS: RESEARCH OPEN — PROJECTIVE LOCAL BRIDGE CLOSED; ULTRA-LOW EDIT RIGIDITY CLOSED; POST-GROUP ALGEBRA CLOSED; WRONG-ORDER OBSTRUCTION CLOSED; PASCH LOCALIZATION CLOSED; NEAR-CARRIER OBSTRUCTION CLOSED; PARTIAL-CORE METRIC CLOSED; ADD-4 CORE AUDIT CLOSED; LINEAR COST NECESSITY CLOSED; PROJECTIVE PRODUCT BENCHMARK CLOSED

Primary target is **linear partial projective-core stability**. Exact same-order rigidity, near-supercarrier rigidity, and literal large exact projective subsystem formulations are too strong in general.

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

For a block

```math
B={x,y,x∘y},
```

if `p(B)` is the number of Pasch configurations through `B`, then

```math
\boxed{r_{xy}=r_{x,x∘y}=r_{y,x∘y}=(v-3)-p(B).}
```

Thus associator defect is exactly local Pasch-incidence deficit. Globally,

```math
\boxed{s=v(v-1)(v-3)-24P(S)=24(M(v)-P(S))}
```

and for the classical four-block configuration `C14`,

```math
\boxed{s=4c_{14}.}
```

If `phi:L->G` is injective and preserves all but `t_phi` products, then for a non-Boolean group of size `m=lambda n`,

```math
\boxed{t_phi/n^2 >= 1/2-3lambda/8.}
```

The Add-4 sequence therefore also obstructs vanishing-error embeddings of all points into groups of size `(1+o(1))n`.

---

## Closed step 6 — `PROJECTIVE_PARTIAL_CORE_METRIC_AND_ADD4_AUDIT`

Full proof:

`notes/PROJECTIVE_PARTIAL_CORE_METRIC_AND_ADD4_AUDIT.md`

Commit:

`86d43167ea9ba8ea42501443d8b65fe413ea2749`

A cross-order partial-core cost `D_pc` was defined. It allows deletion of `o(v)` exceptional source points, `o(v)` unused points in a nearby projective model, and `o(v^2)` bad pair completions on the common core. In the same-order/full-core case it recovers `d_blk` exactly.

For the actual Grannell--Lovegrove Add-4 construction, after a corrected audit of its seven one-factors and three removed infinity points,

```math
\boxed{
D_pc(T;P_v,V',id)
=
10/w + 7(w-7)/[w(w-1)].
}
```

Hence `D_pc(T,\mathcal P)=O(1/w)->0` despite the same-carrier and near-supercarrier obstructions.

Also, if `M_med` counts failed medial/parallelogram identities, then

```math
\boxed{M_med<=5ns.}
```

Thus almost associativity implies almost mediality with constant-factor loss.

---

## Closed step 7 — `PROJECTIVE_LINEAR_COST_AND_PRODUCT_BENCHMARK`

Full proof:

`notes/PROJECTIVE_LINEAR_COST_AND_PRODUCT_BENCHMARK.md`

Commit:

`717094726c33d7420b32dd6f56d49e1bf79295a7`

### Universal linear converse for `D_pc`

For any projective comparison `(P,U,phi)` with

```math
D=D_pc(S;P,U,phi)<1,
```

every associativity failure entirely inside the core forces one of four pair-completion errors. Counting the fibers gives

```math
\boxed{s(S)<=3rv^2+8Ev,}
```

where `r=|X\setminus U|` and `E` is the number of bad retained pairs.

Consequently

```math
\boxed{
\delta_ind(S)
<=
\frac{4v^2}{(v-1)(v-3)}
\frac{D}{(1-D)^2},
}
```

and therefore

```math
\boxed{
1-rho_P(S)
<=
\frac{12v^2}{(v-1)(v-3)}
\frac{D}{(1-D)^2}.
}
```

Asymptotically, whenever `D_pc->0`,

```math
\boxed{D_pc(S,\mathcal P) >= (1-rho_P)/(12+o(1)).}
```

Thus any true projective stability theorem has an unavoidable linear defect scale.

### Infinite projective-product benchmark

Let

```math
m=2^a-1,
\qquad
n=2^b-1,
```

and form the direct product of the two projective Steiner quasigroups. Its order is

```math
V=mn,
```

generally a wrong projective order.

The blockwise Pasch audit yields the exact associator defect

```math
\boxed{
s=3mn(m-1)(n-1)(m+n-2).
}
```

Hence

```math
\boxed{
\delta_ind
=
3(m-1)(n-1)(m+n-2)/[(mn-1)(mn-3)].
}
```

If both factors grow,

```math
\delta_ind
=
3(1/m+1/n)+o(1/m+1/n)
->0,
```

so `rho_P->1`.

There is a canonical comparison with the projective system in

```math
F_2^{a+b}\setminus\{0\},
```

of order

```math
W=mn+m+n.
```

The product carrier is exactly the set of vectors with both coordinate components nonzero. The omitted projective points are the two coordinate axes, `m+n` points in total. Pair completions disagree exactly when two product points share one coordinate. Therefore

```math
\boxed{
D_pc
=
\frac{m+n}{mn+m+n}
+
\frac{mn(m+n-2)}{(mn+m+n)(mn+m+n-1)}.
}
```

As both factors grow,

```math
\boxed{
D_pc
<=
2(1/m+1/n)+o(1/m+1/n),
}
```

and for this natural comparison

```math
\boxed{D_pc/\delta_ind -> 2/3.}
```

So the projective-product family gives a second broad wrong-order sequence, beyond Add-4, in which structural distance and associator defect have the same linear scale.

---

## Current sharpened conjecture — LINEAR PARTIAL PROJECTIVE-CORE STABILITY

The natural target is now:

> There exist absolute constants `C>0` and `epsilon_0>0` such that every sufficiently large STS with
>
> ```math
> 1-rho_P<=epsilon_0
> ```
>
> satisfies
>
> ```math
> \boxed{D_pc(S,\mathcal P)<=C(1-rho_P).}
> ```

A weaker qualitative form is

```math
1-rho_P=o(1)
=>
D_pc(S,\mathcal P)=o(1).
```

Both are open.

### Evidence / lower scale

- universal converse: `D_pc >= (1-rho_P)/(12+o(1))`;
- Add-4: both quantities have order `1/v`;
- direct products of projective systems: both have order `1/m+1/n`;
- sparse projective trades are expected to have the same linear behavior.

Hence, if the upper theorem is true, the correct asymptotic relation is

```math
D_pc=Theta(1-rho_P)
```

up to absolute constants.

## Current bottleneck / next attack

1. Attempt a constructive upper bound using the low-defect block weights `d(B)=(v-3)-p(B)`.
2. Propagate Boolean coordinates from a low-defect Fano root and bound inconsistency by charged `C14` defects.
3. Use the almost-medial estimate `M_med<=5ns` as an alternate route to an approximate affine representation.
4. Test asymmetric product families and sparse trades to stress the conjectured linear constant.
5. If no upper theorem closes in the next attack, stop expanding the theorem target and prepare Article III around the proven positive/negative dichotomy plus the sharpened linear conjecture.

## Publication threshold

The branch is decisively publication-ready. The new universal linear converse and projective-product benchmark strengthen the paper materially: the corrected conjecture now has a proved necessary scale and two independent infinite benchmark families supporting that scale.

One final constructive upper-bound attack is justified. If it does not close, proceed to Article III manuscript preparation rather than leaving the branch indefinitely open.

## Research discipline

- no theorem without proof;
- attack counterexamples first;
- keep order-spectrum assumptions explicit;
- distinguish same-order, supercarrier, exact subsystem, and partial-core notions of rigidity;
- distinguish phase-profile stability from edit-distance stability;
- no intermediate PDFs;
- update this file after each closed mathematical step.
