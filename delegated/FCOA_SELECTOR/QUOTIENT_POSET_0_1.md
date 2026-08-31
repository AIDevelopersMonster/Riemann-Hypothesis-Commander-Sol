# SOL-SELECTOR — Quotient Poset 0.1

**Branch:** `director/fcoa-selector`  
**Date:** 2026-08-31  
**Status:** PROVED CORE / FIRST NONCHAIN STRUCTURE FOUND

---

## 0. Executive result

The pure terminal-event quotient spectrum of `F_mix` is not a chain.

After mixed commutativity, every mixed event can be written uniquely as

\[
p_{ij}=\{P_i^+,P_j^-\},\qquad i,j\ge 1.
\]

Zero reflection acts by

\[
\nu(p_{ij})=p_{ji}.
\]

Hence pure quotients of `F_mix` are exactly equivalence relations on

\[
\mathbb N_{>0}^2
\]

that are invariant under coordinate transposition.

Two canonical radial quotients are:

\[
N_{\Sigma}: p_{ij}\mapsto i+j,
\]

and

\[
N_{\Delta}: p_{ij}\mapsto |i-j|.
\]

Their kernels are incomparable.

Moreover,

\[
\ker N_{\Sigma}\wedge\ker N_{\Delta}
=\ker N_{\{\cdot,\cdot\}},
\]

where `N_{\{.,.\}}` remembers only the unordered radius multiset `\{i,j\}`, while

\[
\ker N_{\Sigma}\vee\ker N_{\Delta}
=\ker N_{\mathrm{par}},
\]

where `N_par` remembers only the parity of `i+j`.

Thus the quotient lattice already contains a genuine diamond-like interval before any numerical cost functor is introduced.

When event classes are allowed to anchor to old core points, the situation becomes strictly less lattice-like: distinct incompatible anchors can have no common admissible upper bound because the old core must remain pointwise separated.

---

# 1. Coordinate model for mixed-commutative events

The signed parent line has base points

\[
P_0,\quad P_n^+,\quad P_n^-\qquad(n\ge1)
\]

with reflection

\[
\nu(P_n^+)=P_n^-,
\qquad
\nu(P_n^-)=P_n^+.
\]

In `F_mix`, transposition of the two operation arguments has already been quotiented out. Therefore each fresh mixed event has the form

\[
p_{ij}
:=
\{P_i^+,P_j^-\}
=
\{P_j^-,P_i^+\}.
\]

The map

\[
(i,j)\longmapsto p_{ij}
\]

is a bijection from `N_{>0}^2` onto the fresh event index set.

### Lemma 1.1 — reflection is coordinate swap

\[
\boxed{
\nu(p_{ij})=p_{ji}.
}
\]

### Proof

By simultaneous reflection,

\[
\nu(p_{ij})
=
\{P_i^-,P_j^+\}.
\]

Reordering the unordered event pair gives

\[
\{P_j^+,P_i^-\}=p_{ji}.
\]

`\square`

This reduction converts the pure selector problem into an invariant-partition problem for the involution

\[
\sigma(i,j)=(j,i).
\]

---

# 2. Pure event quotients form a complete invariant-equivalence lattice

Let

\[
E=\mathbb N_{>0}^2.
\]

Call an equivalence relation `theta` on `E` **reflection-admissible** if

\[
(i,j)\mathrel\theta(k,l)
\Longrightarrow
(j,i)\mathrel\theta(l,k).
\]

This is exactly invariance under the involution `sigma`.

### Theorem 2.1 — Pure Quotient Classification

Pure terminal-event quotients of `F_mix` are in canonical bijection with reflection-admissible equivalence relations on `E`.

### Proof

The one-step mixed generators have no re-entry operations. Thus, outside the old fixed core, their only inherited structure is reflection. Identifying fresh generators is therefore compatible exactly when the identification is stable under reflection. Conversely every such stable equivalence relation defines a quotient in which operation values are the corresponding event classes. `\square`

### Theorem 2.2 — Complete lattice theorem

The pure quotient kernels form a complete lattice under inclusion.

For any family `\{theta_a\}` of reflection-admissible equivalence relations,

\[
\bigwedge_a\theta_a
=
\bigcap_a\theta_a,
\]

and

\[
\bigvee_a\theta_a
=
\operatorname{EqCl}\left(\bigcup_a\theta_a\right),
\]

where `EqCl` is equivalence closure.

Both are reflection-admissible.

### Proof

Intersection of equivalence relations is an equivalence relation, and reflection stability is preserved under intersection.

For the join, the union is reflection-stable, and every finite chain witnessing membership in its equivalence closure remains a valid chain after applying coordinate swap. Therefore the equivalence closure is again reflection-stable. `\square`

Hence before anchoring to the old core, the quotient spectrum is much richer than a chain but still very well behaved: it is a complete lattice.

---

# 3. Canonical radial quotients

The repository previously referred generically to radial `N_j` candidates without freezing a precise family. The present note therefore introduces canonical representatives derived directly from intrinsic radius statistics.

They are not declared the final historical meaning of every earlier `N_j` label; they are the first rigorously specified radial quotient family.

## 3.1 Full signed-side radial memory

Define

\[
N_{\mathrm{id}}(i,j)=(i,j).
\]

Its kernel is equality, so this is just `F_mix` itself at the event-index level.

## 3.2 Reflection-orbit radial memory

Define

\[
N_{\mathrm{orb}}(i,j)=\{i,j\}.
\]

Thus

\[
(i,j)\sim_{\mathrm{orb}}(k,l)
\iff
\{i,j\}=\{k,l\}.
\]

It forgets which radius lies on which branch but keeps both radii.

## 3.3 Span/sum quotient

Define

\[
N_{\Sigma}(i,j)=i+j.
\]

Its kernel is

\[
(i,j)\sim_{\Sigma}(k,l)
\iff
i+j=k+l.
\]

Geometrically this remembers the total cross-origin span.

## 3.4 Imbalance/gap quotient

Define

\[
N_{\Delta}(i,j)=|i-j|.
\]

Its kernel is

\[
(i,j)\sim_{\Delta}(k,l)
\iff
|i-j|=|k-l|.
\]

This remembers radial imbalance but not total span.

## 3.5 Parity quotient

Define

\[
N_{\mathrm{par}}(i,j)=(i+j)\bmod 2.
\]

Because

\[
i+j\equiv |i-j|\pmod 2,
\]

this is simultaneously the parity shadow of both span and gap.

## 3.6 Relation-only quotient

Define

\[
N_0(i,j)=*.
\]

Its kernel is the universal equivalence relation on `E`. This is exactly the pure-event quotient `B0`.

Thus a canonical radial naming ladder may be organized as

\[
F_{\mathrm{mix}}
=N_{\mathrm{id}},
\quad
N_{\mathrm{orb}},
\quad
N_{\Sigma},
\quad
N_{\Delta},
\quad
N_{\mathrm{par}},
\quad
N_0=B0,
\]

without implying that these lie on one chain.

---

# 4. First incomparable kernels

### Theorem 4.1 — Span/Gap Incomparability

\[
\boxed{
\ker N_{\Sigma}
\not\subseteq
\ker N_{\Delta}
}
\]

and

\[
\boxed{
\ker N_{\Delta}
\not\subseteq
\ker N_{\Sigma}.
}
\]

Hence neither quotient factors through the other.

### Proof

Take

\[
(1,4),\qquad(2,3).
\]

They have equal sum:

\[
1+4=2+3=5,
\]

but unequal gaps:

\[
|1-4|=3,
\qquad
|2-3|=1.
\]

Therefore

\[
(1,4)\sim_{\Sigma}(2,3)
\]

but

\[
(1,4)\not\sim_{\Delta}(2,3).
\]

So `ker N_Sigma` is not contained in `ker N_Delta`.

Conversely take

\[
(1,2),\qquad(2,3).
\]

Both have gap `1`, but their sums are `3` and `5`. Hence

\[
(1,2)\sim_{\Delta}(2,3)
\]

while

\[
(1,2)\not\sim_{\Sigma}(2,3).
\]

Thus the reverse inclusion also fails. By the kernel/factorization theorem from the category audit, neither quotient maps canonically to the other. `\square`

This is the first exact proof that the selector information order is not a chain.

---

# 5. Exact meet of span and gap

### Theorem 5.1 — Span/Gap Meet

\[
\boxed{
\ker N_{\Sigma}
\cap
\ker N_{\Delta}
=
\ker N_{\mathrm{orb}}.
}
\]

### Proof

Suppose

\[
i+j=k+l
\]

and

\[
|i-j|=|k-l|.
\]

For positive integers, the pair consisting of sum `s` and absolute difference `d` determines the unordered multiset

\[
\left\{\frac{s+d}{2},\frac{s-d}{2}\right\}.
\]

Therefore

\[
\{i,j\}=\{k,l\}.
\]

The converse is immediate: equal unordered radius multisets have equal sum and equal absolute difference. `\square`

Thus the greatest common refinement of the two radial statistics is exactly the quotient that forgets only branch assignment of the two radii.

---

# 6. Exact join of span and gap

### Theorem 6.1 — Span/Gap Join

\[
\boxed{
\ker N_{\Sigma}
\vee
\ker N_{\Delta}
=
\ker N_{\mathrm{par}}.
}
\]

### Proof

Every `Sigma`-equivalence preserves parity of `i+j`. Every `Delta`-equivalence also preserves parity because

\[
i+j\equiv i-j\equiv |i-j|\pmod2.
\]

Hence the join is contained in parity equivalence.

It remains to prove connectivity inside each parity class under alternating `Sigma` and `Delta` moves.

If `i+j` is even, then `(i,j)` is `Sigma`-equivalent to the diagonal point

\[
\left(\frac{i+j}{2},\frac{i+j}{2}\right).
\]

All diagonal points have gap `0`, so they are mutually `Delta`-equivalent. Therefore every even-sum pair belongs to one join class.

If `i+j` is odd, then `(i,j)` is `Sigma`-equivalent to

\[
\left(\frac{i+j-1}{2},\frac{i+j+1}{2}\right),
\]

which has gap `1`. All positive pairs of the form `(n,n+1)` have gap `1`, hence are mutually `Delta`-equivalent. Therefore every odd-sum pair belongs to one join class.

No even pair can connect to an odd pair because parity is preserved by every generating relation. Hence exactly two join classes remain. `\square`

---

# 7. The first internal diamond

Combining the previous theorems gives the interval

\[
\ker N_{\mathrm{orb}}
\subsetneq
\ker N_{\Sigma},\ker N_{\Delta}
\subsetneq
\ker N_{\mathrm{par}},
\]

with `N_Sigma` and `N_Delta` incomparable.

In quotient-arrow notation:

\[
N_{\mathrm{orb}}
\longrightarrow
N_{\Sigma},N_{\Delta}
\longrightarrow
N_{\mathrm{par}}.
\]

Neither middle object maps to the other.

Further,

\[
F_{\mathrm{mix}}\to N_{\mathrm{orb}}
\]

and

\[
N_{\mathrm{par}}\to B0.
\]

So the earlier simple ladder

\[
F_{\mathrm{mix}}\to B0
\]

contains a nontrivial internal lattice geometry.

This is the first intrinsic selector branching obtained without any external cost vector.

---

# 8. `B1` placement

The parent FCOA-Z file defines `B1` by giving each unoriented mixed bridge its own terminal output.

At the current `F_mix` stage, the operation arguments are already unordered, so `B1` retains full mixed-event identity.

Therefore, up to notation of the terminal outputs,

\[
\boxed{B1\cong F_{\mathrm{mix}}}
\]

in the one-step mixed-commutative selector category.

This does not say the original parent construction was redundant. It says that once the selector branch has explicitly chosen mixed commutativity and one generator per unordered bridge, the parent `B1` construction is precisely that free object rather than a distinct further quotient.

This resolves the structural position of `B1`.

---

# 9. Event-to-core anchoring

Pure event quotients never identify a fresh event with an old core point. Now allow such identifications.

Let the old core be `C0`, fixed pointwise by all morphisms.

An admissible equivalence relation on

\[
C_0\sqcup E
\]

must satisfy:

1. distinct old core points remain inequivalent;
2. reflection stability;
3. weak partial-operation compatibility;
4. protected core holes remain protected as object data.

Because fresh one-step events are terminal, weak operation compatibility imposes no additional re-entry equation when an event is identified with a core point.

### Theorem 9.1 — Core-Separating Partition Classification

At the one-step weak level, anchored quotients are exactly reflection-stable equivalence relations on `C0 sqcup E` whose restriction to `C0` is equality.

### Proof

Necessity follows from core fixation and reflection equivariance.

For sufficiency, terminal fresh events have no source-defined operation with themselves as inputs. Therefore the only nontrivial preservation equations are those that generated the events from their mixed core inputs; quotienting their output symbols according to a reflection-stable core-separating equivalence is compatible with those equations. `\square`

Each equivalence class contains at most one old core point. Hence an anchored event block has a uniquely determined core anchor.

---

# 10. Reflection constraints on anchors

Suppose an event block `C` is anchored to a core point `a`.

Reflection compatibility forces

\[
\nu C
\]

to be anchored to

\[
\nu a.
\]

In particular, a reflection-fixed event block can be anchored only to a reflection-fixed core point.

On the signed base line, the unique reflection-fixed base point is the root `P0`.

Therefore the one-block relation-only event quotient `B0`, whose unique event block is reflection-fixed, has exactly one base-line anchor compatible with zero reflection:

\[
E_{\mathrm{cross}}\mapsto P_0.
\]

That quotient is `BR`.

Thus among base-line anchors, `BR` is not arbitrary once `B0` has already been chosen: it is the unique reflection-compatible anchoring of the unique `B0` event block.

This is a stronger statement than merely saying `B0 -> BR` exists.

---

# 11. Anchors destroy global lattice completeness

The pure event quotient spectrum is a complete lattice. The anchored spectrum is not.

### Theorem 11.1 — Incompatible Anchor Obstruction

Let `e` be a fresh event generator and let `a,b` be distinct old core points. Suppose two admissible quotients have kernels

\[
\theta_a:\ e\sim a
\]

and

\[
\theta_b:\ e\sim b,
\]

with any additional reflection-forced identifications included.

If both quotients are admissible individually, then they have no common admissible upper bound in the core-fixed quotient order.

### Proof

Any equivalence relation containing both `theta_a` and `theta_b` contains

\[
a\sim e\sim b.
\]

By transitivity,

\[
a\sim b.
\]

But admissibility requires distinct old core points to remain separated. Therefore no admissible kernel can contain both. `\square`

Hence once anchoring is admitted, the quotient spectrum is generally only a poset with meets where compatible; joins may fail to exist.

This is the first intrinsic non-lattice bifurcation in the weak selector architecture.

---

# 12. Concrete reflection-paired anchor branches

Take a non-diagonal event

\[
p_{ij},\qquad i\ne j.
\]

Its reflection mate is

\[
p_{ji}.
\]

Choose any depth `n>=1` and anchor

\[
p_{ij}\mapsto P_n^+,
\qquad
p_{ji}\mapsto P_n^-.
\]

This is reflection-compatible.

Choosing another depth `m\ne n` yields a second individually reflection-compatible anchored quotient, but the two quotients have no common admissible upper bound, because a common upper bound would force

\[
P_n^+\sim P_m^+.
\]

Thus even before re-entry, there are infinitely many mutually incompatible anchor branches indexed by radial depth.

This supplies a natural rigorous interpretation for an `N_j`-style anchored family if the programme wants such notation:

\[
N_j^{\mathrm{anchor}}:
(p_{ij},p_{ji})
\mapsto
(P_j^+,P_j^-)
\]

for a selected reflection orbit of events.

However the repository did not previously freeze a unique formula for `N_j`, so this notation should not be retroactively imposed on older notes without an explicit naming decision.

---

# 13. Selector geometry obtained so far

The quotient geometry now has two qualitatively different regions.

## Region A — pure event forgetting

A complete lattice:

\[
\boxed{
\operatorname{Eq}_{C_2}(\mathbb N_{>0}^2)
}
\]

where the `C2` action is coordinate swap.

It contains, among many others,

\[
F_{\mathrm{mix}}
\to
N_{\mathrm{orb}}
\to
\{N_{\Sigma},N_{\Delta}\}
\to
N_{\mathrm{par}}
\to
B0.
\]

## Region B — event-to-core anchoring

A core-separating reflection-stable quotient poset in which joins can fail.

`BR` lies here as the unique reflection-compatible base anchor of the one-block `B0` event quotient.

Thus the structural transition

\[
\boxed{
\text{pure forgetting}
\longrightarrow
\text{semantic anchoring into the old carrier}
}
\]

is mathematically visible as a transition from complete-lattice behavior to possible incompatibility/no-join behavior.

---

# 14. Cost functor decision

The original plan said to introduce a numerical multi-component cost only if genuinely incomparable kernels survive.

They do survive:

\[
N_{\Sigma}\parallel N_{\Delta}.
\]

But this does **not** yet mean a numerical cost should be introduced immediately.

The factorization lattice itself already records more information than a scalar cost could preserve. A scalar ranking would arbitrarily linearize incomparable quotients.

Therefore the next stage should first exploit intrinsic order-theoretic invariants:

- height above `F_mix`;
- coheight below `B0`;
- meet/join profiles;
- number/type of reflection-fixed classes;
- orbit structure of quotient blocks;
- existence of admissible core anchors;
- anchor incompatibility graph.

Only after these are computed should any Pareto vector be considered.

---

# 15. Immediate next strike

The first nonchain and nonlattice phenomena are now proved.

The next decisive question is no longer whether incomparable quotients exist. It is:

\[
\boxed{
\text{which quotient statistics are intrinsic to the FCOA structure,}
\text{ rather than imported coordinate functions }i+j,|i-j|?
}
\]

The strongest next attack is therefore an **intrinsic-definability audit** of the radial quotient statistics:

1. determine whether `N_orb`, `N_Sigma`, `N_Delta`, and `N_par` can be defined from the inherited rooted/reflected FCOA structure without invoking external integer arithmetic;
2. reject any quotient whose statistic requires importing forbidden `+` or subtraction as primitive background structure;
3. identify the weakest intrinsic generator that realizes the first genuine incomparable pair;
4. only then compare arithmetic leakage.

This is now the publication-critical bottleneck.

---

## Dependency ledger

This note depends on:

- `CATEGORY_CLOSURE_AUDIT_0_1.md`;
- parent signed reflection formulas in `SIGNED_COMPLETION_FOUNDATION_0_1.md`;
- the parent `B0/B1` construction in `MIXED_COMMUTATIVE_BRIDGE_GENERATOR_0_1.md`.

No external cost functor, re-entry rule, output-sort predicate, or ordinary signed addition/multiplication is assumed as primitive selector data.
