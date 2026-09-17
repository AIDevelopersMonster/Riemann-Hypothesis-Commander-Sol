# Alice Throws Away the Ruler III — research status

**Branch:** `research/alice-ruler-edit-rigidity`  
**Working folder:** `alice-ruler-edit-rigidity/`  
**Status date:** 2026-09-13  
**Parent publication:** *Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects*  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22722951

## STATUS: RESEARCH OPEN — PROJECTIVE LOCAL BRIDGE CLOSED; ULTRA-LOW EDIT RIGIDITY CLOSED; POST-GROUP ALGEBRA CLOSED; WRONG-ORDER OBSTRUCTION CLOSED; PASCH LOCALIZATION CLOSED; NEAR-CARRIER OBSTRUCTION CLOSED; PARTIAL-CORE METRIC CLOSED; ADD-4 CORE AUDIT CLOSED; LINEAR COST NECESSITY CLOSED; PROJECTIVE PRODUCT BENCHMARK CLOSED; RANK-2 FANO FIBERIZATION CLOSED

Primary target remains **linear partial projective-core stability**, but the branch now contains a constructive positive coordinate-recovery theorem: the first two Boolean coordinates can be recovered on a `1-O(epsilon)` fraction of the carrier with `O(epsilon v^2)` interaction loss, where `epsilon=1-rho_P`.

---

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

For the actual Grannell--Lovegrove Add-4 construction,

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

every associativity failure entirely inside the core forces one of four pair-completion errors. Counting gives

```math
\boxed{s(S)<=3rv^2+8Ev,}
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

Asymptotically,

```math
\boxed{D_pc(S,\mathcal P) >= (1-rho_P)/(12+o(1)).}
```

Thus any true projective stability theorem has an unavoidable linear defect scale.

### Infinite projective-product benchmark

For projective factors of orders

```math
m=2^a-1,
\qquad
n=2^b-1,
```

their direct-product STS has exact associator defect

```math
\boxed{
s=3mn(m-1)(n-1)(m+n-2).
}
```

There is a canonical comparison with the projective system in `F_2^{a+b}\setminus\{0\}`. For this comparison

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
D_pc/\delta_ind -> 2/3.
```

So structural distance and associator defect have the same linear scale in a second infinite wrong-order family.

---

## Closed step 8 — `PROJECTIVE_RANK2_FANO_FIBERIZATION`

Full proof:

`notes/PROJECTIVE_RANK2_FANO_FIBERIZATION.md`

Commit:

`b47765b67c38cfa1568828f94819576af4354d58`

This is the first constructive positive coordinate-recovery theorem beyond the ultra-low exact-rigidity regime.

Put

```math
\varepsilon=1-\rho_P.
```

### Exact Fano density identity

Every P-root lies in one unique Fano subsystem and every Fano subsystem contains exactly `28` independent triples. Therefore

```math
\boxed{
F(S)=\rho_P N/28.
}
```

Thus `rho_P` is literally the density of the maximal possible Fano-plane count.

For a block `B`, let `f(B)` be the number of Fano subsystems containing it and define

```math
\boxed{e(B)=(v-3)-4f(B).}
```

Then `e(B)` is exactly the number of external points failing to extend `B` to a Fano subsystem, and

```math
\boxed{
\sum_B e(B)=N(1-\rho_P)=N\varepsilon.
}
```

### Exact translation commutator identity

For Steiner-loop translations `T_x`,

```math
\boxed{
\sum_{x,y} d_H(T_xT_y,T_yT_x)=s.
}
```

So almost projective phase gives an average almost-commuting involutive translation family with no constant loss.

### Clean base block

There exists a block

```math
B=\{a,b,c\}
```

such that all three of its point translations have row associator load at most

```math
6\varepsilon(v-1)(v-3)
```

and

```math
\boxed{e(B)\le2\varepsilon(v-3).}
```

### Rank-2 Fano fiberization

Put

```math
H=\{0,a,b,c\}\cong C_2^2.
```

After deleting at most

```math
\boxed{2\varepsilon(v-3)}
```

nonzero points, the remaining loop decomposes exactly as

```math
U=H\sqcup C_1\sqcup\cdots\sqcup C_q,
```

where each `C_i` has four points, `H\cup C_i` is an exact Boolean group of order `8`, and `H` acts regularly on every `C_i`.

Thus the first two Boolean coordinates are recovered exactly on a `1-O(\varepsilon)` fraction of the carrier.

### Exact affine multiplication on almost all fiber pairs

Define contaminated ordered point pairs by either leaving `U` under multiplication or violating one of the three nontrivial `H`-associativity identities. The total number is bounded by

```math
\boxed{|Z|<20\varepsilon v^2.}
```

If an ordered pair of fibers `(C,D)` contains no contaminated point pair, then for every `x\in C`, `y\in D`, and `h,k\in H`,

```math
\boxed{
(h\circ x)\circ(k\circ y)
=(h\circ k)\circ(x\circ y).
}
```

In particular all products `C\times D` lie in one output fiber and multiplication is exactly `H`-affine on that fiber pair.

Therefore, outside `O(\varepsilon v^2)` point-pair interactions, the loop has an exact two-bit affine coordinate layer.

### Remaining obstruction

The quotient set of 4-point Fano fibers has a multiplication law defined coherently on all but `O(\varepsilon)` of its pairs. What is not yet proved is a rank-uniform **Steiner quotient completion/repair theorem** saying that this partial quotient can be repaired to an exact Steiner/Boolean quotient with only `O(\varepsilon q^2)` changes.

This quotient-repair problem is now the sole obstruction to iterating the rank-2 fiberization to a full linear upper bound for `D_pc`.

---

## Current sharpened conjecture — LINEAR PARTIAL PROJECTIVE-CORE STABILITY

The target remains:

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

The branch now proves a substantial first half of the constructive direction: an exact rank-2 Boolean/Fano fiberization with linear exceptional-set and interaction bounds.

## Remaining mathematical bottleneck

The next unresolved step is no longer vague coordinate propagation. It is specifically:

```math
ALMOST-STEINER QUOTIENT
        |
        v
O(epsilon q^2) REPAIR
        |
        v
EXACT BOOLEAN/PROJECTIVE QUOTIENT
```

or a counterexample showing that such a rank-uniform repair statement is false.

Known almost-commuting permutation stability does not directly close this because published constants are for fixed tuples/groups and are not presently uniform in the growing Boolean rank needed here.

## Publication threshold — CROSSED

Article III is now publication-ready even without a quotient-repair theorem. The mathematically proved package contains:

1. exact local P-phase / associator certificate and destructive counterexample;
2. ultra-low exact projective edit-rigidity;
3. robust Boolean recovery from group distance;
4. explicit wrong-order obstruction and sharp `Theta(1/v)` exact-order scale;
5. exact Pasch / `C14` defect geometry;
6. impossibility of same-carrier and near-supercarrier reconstruction;
7. cross-order partial-core metric with exact Add-4 audit;
8. universal linear lower bound for partial-core distance;
9. exact projective-product benchmark with linear scaling;
10. **constructive rank-2 Fano fiberization with linear losses and exact affine fiber interactions on almost all pairs**;
11. sharpened linear partial-core stability conjecture with the remaining obstruction isolated to quotient repair.

Research policy from this point:

- do not hold Article III publication waiting indefinitely for quotient repair;
- prepare the manuscript around the proved positive/negative dichotomy and rank-2 fiberization theorem;
- keep quotient repair as the next research branch / possible Article IV theorem if it does not close quickly;
- no theorem without proof;
- no intermediate PDFs unless requested; final publication artifacts only after manuscript audit.
