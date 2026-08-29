# Head-Synchronization Threshold — From Finite-State Interval Tests to Additive Transport

**Project:** FCOA Admissibility Geometry  
**Status:** central theorem candidate; full proof included; hostile audit required before promotion  
**Scope:** central Arithmetic Leakage programme after the unary U1 wall

## 1. Motivation

The unary finite-state wall separates finite phase memory from variable displacement memory:

\[
AL0<AL\text{-}FS<AL1.
\]

The next question is whether the decisive resource is more internal state or something qualitatively different.

The answer is sharper:

\[
\boxed{
\text{one moving finite-state head is still below EqGap,}
}
\]

while

\[
\boxed{
\text{two synchronized moving heads already generate EqGap exactly.}
}
\]

Thus the first additive threshold is a **synchronization dimension** threshold rather than a state-count threshold.

## 2. One-head interval generators

Work on the generic chain

\[
G_m=\{0<1<\cdots<m-1\}
\]

as metamathematical notation for the recovered G4-A order.

A **one-head finite-state interval predicate** is any binary relation \(R(x,y)\), with \(x\le y\), recognized by a fixed finite automaton that starts at \(x\), walks right by successor one step at a time, may read any fixed ultimately-periodic unary background colors, and accepts/rejects when it reaches \(y\).

The automaton, its state set, transition rule, and accepted states are independent of \(m\).

A finite collection of such predicates may be added to the order, and any further fixed FO-definitional FCOA compilation is allowed.

This class strictly contains the earlier unary phase markers: a unary marker can be represented by running one head from the least point to the queried point.

## 3. Marked-word regularity of one-head predicates

Encode a finite chain as a finite word over a finite alphabet containing:

- the finitely many ultimately-periodic background colors;
- marker tracks for the free variables.

For each one-head interval predicate \(R(x,y)\), the set of marked words satisfying \(R(x,y)\) is regular: a finite automaton ignores the prefix before the `x` marker, simulates the interval machine from `x` through `y`, and then ignores the suffix.

Order, equality, minimum, maximum, and successor between marked variables are also regular marked-word conditions.

### Lemma 3.1 — regular closure under FO

Let a finite positional signature on finite chains consist only of relations whose marked-word encodings are regular. Then every first-order formula in that signature has a regular marked-word encoding.

### Proof

Atomic formulas are regular by assumption. Regular languages are closed under Boolean operations. Existential quantification over one position is projection of the corresponding marker track, and regular languages are closed under projection. Universal quantification follows by complement. Induction on formulas completes the proof. \(\square\)

Therefore every relation first-order definable from finite order plus finitely many one-head interval predicates is regular in positional marker encoding.

## 4. EqGap has a nonregular positional skeleton

For forward intervals define

\[
\operatorname{EqGap}(a,b;c,d)
\iff
b-a=d-c
\]

in external rank notation only.

Restrict to tuples satisfying

\[
a=\min,
\qquad
c=\operatorname{Succ}(b),
\qquad
 d=\max.
\]

If \(b\) has rank \(n\ge1\), then \(c\) has rank \(n+1\). EqGap becomes

\[
n=(m-1)-(n+1),
\]

so

\[
m=2n+2.
\]

Erase all background colors and retain only the four positional markers. Up to harmless fixed endpoint-marker conventions, the resulting skeleton language has the form

\[
L_{\mathrm{gap}}
=
\{A\,a^{n-1}B\,C\,a^{n-1}D:n\ge1\}.
\]

### Lemma 4.1

\(L_{\mathrm{gap}}\) is not regular.

### Proof

After intersecting with the displayed fixed marker pattern and applying a homomorphism deleting the fixed marker letters, one obtains the classical equal-block language

\[
\{a^n b^n:n\ge0\},
\]

which is not regular. Since regular languages are closed under intersection and homomorphism, \(L_{\mathrm{gap}}\) cannot be regular. \(\square\)

## 5. One-Head Wall Theorem

### Theorem 5.1

No finite expansion of finite linear order by one-head finite-state interval predicates, even with finitely many ultimately-periodic unary background colors, can uniformly first-order define EqGap.

### Proof

If EqGap were definable, then after imposing the regular restrictions

\[
a=\min,
\quad
c=\operatorname{Succ}(b),
\quad
 d=\max,
\]

Lemma 3.1 would make the corresponding marked-word language regular. Lemma 4.1 says that language is nonregular. Contradiction. \(\square\)

Because truncated addition and EqGap are already known to be FO-interdefinable over the ordered generic sector, we also obtain

\[
\boxed{
\operatorname{Add}
\text{ is not uniformly FO-definable from any finite one-head finite-state interval layer.}
}
\]

This strictly strengthens the unary U1 finite-state wall.

## 6. Two synchronized heads

Now allow two moving heads and no unbounded internal memory.

Given two forward intervals

\[
[a,b],
\qquad
[c,d],
\]

place head \(H_1\) at \(a\) and head \(H_2\) at \(c\).

Repeat the single local transition

\[
(H_1,H_2)\mapsto
(\operatorname{Succ}(H_1),\operatorname{Succ}(H_2))
\]

while neither target has been passed.

Accept exactly when the two heads hit \(b\) and \(d\) simultaneously.

Only equality with the two fixed targets and the successor relation are consulted. No numerical rank, counter, arithmetic operation, or carrier-size predicate is available to the machine.

The internal control can be taken to have one running state plus terminal accept/reject status.

## 7. Synchronized-Product Theorem

### Theorem 7.1

For all forward intervals,

\[
\boxed{
\text{the two-head synchronized machine accepts }(a,b;c,d)
\iff
\operatorname{EqGap}(a,b;c,d).
}
\]

### Proof

After exactly \(k\) synchronized transitions, the two heads are at the \(k\)-th successors of \(a\) and \(c\), respectively.

They hit the targets simultaneously exactly when there exists the same \(k\ge0\) such that

\[
S^k(a)=b
\qquad\text{and}\qquad
S^k(c)=d.
\]

On a finite linear order this is equivalent to

\[
\operatorname{rk}(b)-\operatorname{rk}(a)
=
\operatorname{rk}(d)-\operatorname{rk}(c).
\]

That is EqGap. \(\square\)

This can be expressed graph-theoretically without mentioning ranks. On the product carrier \(G_m^2\), define the local product-successor edge

\[
(a,c)\Rightarrow(b,d)
\iff
\operatorname{Succ}(a,b)
\land
\operatorname{Succ}(c,d).
\]

Then

\[
\boxed{
\operatorname{EqGap}(a,b;c,d)
\iff
(a,c)\Rightarrow^*(b,d),
}
\]

where \(\Rightarrow^*\) is reflexive-transitive closure.

Thus additive leakage appears exactly when local successor is allowed to propagate through **two synchronized coordinates with unbounded traversal depth**.

## 8. Direct synchronized transport operation

The same mechanism generates truncated addition without importing an addition table.

Let \(0_G\) be the least generic point. For inputs \(x,y\in G_m\):

1. place \(H_1\) at \(0_G\) with target \(y\);
2. place \(H_2\) at \(x\);
3. advance both heads synchronously;
4. when \(H_1\) reaches \(y\), output the current position \(z\) of \(H_2\);
5. if \(H_2\) would leave the finite chain first, the operation is undefined.

Call the generated partial operation \(\triangleplus\).

Then

\[
x\triangleplus y=z
\iff
\operatorname{EqGap}(0_G,y;x,z),
\]

hence

\[
\boxed{
\operatorname{rk}(z)
=
\operatorname{rk}(x)+\operatorname{rk}(y)<m.
}
\]

So \(\triangleplus\) is exactly canonical truncated rank addition, but its generator uses only local successor synchronization and unbounded iteration.

The arithmetic appears in the **result of closure**, not in the local transition rule.

## 9. Uniformity / import audit

The synchronized generator does not inspect the final size \(m\) and does not use an external unary numerical function.

There is one subtlety: on a short finite prefix, an input pair \((x,y)\) may have no output because the required \(z\) lies beyond the current carrier; after extending the carrier, that same pair may become defined.

This is not a size oracle. The correct consistency notion is graph-prefix consistency:

\[
\operatorname{Graph}(\triangleplus_m)
=
\operatorname{Graph}(\triangleplus_\infty)
\cap G_m^3.
\]

Thus membership of every old triple \((x,y,z)\) is stable under extension. Only the existential projection forming the finite partial-function domain can grow when a previously absent output point enters the carrier.

The EqGap relation itself is fully prefix-stable on old quadruples.

## 10. Exact synchronization threshold

Combine Theorems 5.1 and 7.1.

Within the declared finite-state traversal hierarchy:

\[
\boxed{
\text{one moving head}
\;<\;
\text{two synchronized moving heads}
}
\]

with respect to additive leakage.

More explicitly:

\[
\boxed{
H_1:\ \text{finite-state interval tests cannot define EqGap},
}
\]

while

\[
\boxed{
H_2^{\mathrm{sync}}:\ \text{a one-state synchronized product walk defines EqGap exactly}.
}
\]

Therefore the minimum number of simultaneously moving coordinates in this traversal model is

\[
\boxed{2.}
\]

Increasing finite control state is not what crosses the wall; adding the second synchronized coordinate is.

## 11. Cost of the generated relations

Let \(m=|G_m|\).

### EqGap support

For gap \(k\in\{0,\dots,m-1\}\), there are \(m-k\) forward intervals of length \(k\). Therefore

\[
|\operatorname{EqGap}_m|
=
\sum_{k=0}^{m-1}(m-k)^2
=
\sum_{j=1}^{m}j^2
\]

and hence

\[
\boxed{
|\operatorname{EqGap}_m|
=
\frac{m(m+1)(2m+1)}6
=
\Theta(m^3).
}
\]

This is a 4-ary relation of density \(\Theta(1/m)\) inside the \(m^4\) possible quadruples.

### Truncated-addition operation domain

For each ordered input pair \((x,y)\) with ranks \(i,j\), the generated output exists iff

\[
i+j<m.
\]

Therefore

\[
|\operatorname{Dom}(\triangleplus)|
=
\sum_{i=0}^{m-1}(m-i)
=
\boxed{\frac{m(m+1)}2}.
\]

Thus the first direct base-sort AL1 operation produced by synchronized transport has quadratic domain support and one active output per defined input pair.

No claim of cell-cost minimality for AL1 is made.

## 12. FCOA compilation viewpoints

There are two equivalent ways to use the mechanism.

### Base-sort view

Generate the partial operation \(\triangleplus\) directly by synchronized transport from \((0_G,x)\) to \((y,z)\).

This stays on the generic base sort but its values are active carrier points, not anonymous terminals.

### Interval-sort view

Introduce the conceptual interval sort

\[
I_m=\{(a,b):a\le b\}.
\]

Equal-gap is then an equivalence relation on intervals by length. A constant-valued partial operation on pairs of intervals can compile its domain:

\[
I\star_{\mathrm{gap}}J=\Omega
\iff
\operatorname{length}(I)=\operatorname{length}(J).
\]

This is closer to Domain Compilation but pays the explicit cost of a pair/interval sort.

The central theorem does not prefer one compilation; it identifies the generator threshold before representation optimization.

## 13. Conceptual consequence

The post-G4 hierarchy now has a dynamic interpretation:

\[
\boxed{
\text{absolute finite phase}
\;<\;
\text{one-interval regular memory}
\;<\;
\text{synchronized two-interval transport}
\;=\;
\text{variable displacement}.
}
\]

The critical resource is the ability to **transport one unbounded interval length as a synchronization invariant of a second interval**.

A finite-state controller does not store the gap numerically. The gap is stored geometrically as the number of simultaneous local transitions before termination.

This is precisely the kind of generated memory sought by the FCOA programme: the local rule is weak, but unbounded nesting/iteration of the rule creates a stronger recoverable invariant.

## 14. Arithmetic-leakage status

Because synchronized transport generates EqGap, it reaches

\[
\boxed{AL1}
\]

exactly.

No multiplication rule is introduced. Nothing in this note proves a jump to AL2.

Thus the mechanism is a clean additive-gateway witness rather than a full-arithmetic witness.

## 15. What is still open

The result answers **existence and head-threshold** in the declared traversal model, but not global FCOA minimality.

Open optimization questions include:

1. Can AL1 be encoded on the original base sort with subquadratic operation-domain support?
2. Can bounded anonymous outputs encode EqGap more cheaply than active-output truncated addition?
3. Can two ordinary FCOA partial operations jointly realize synchronized transport without adding an explicit transitive-closure/reachability primitive?
4. Is there a strictly weaker two-head mechanism that leaves the one-head wall but remains below EqGap?
5. Can the nesting/atomicity machinery supply the needed unbounded closure internally rather than as a generator semantics?

These are separate questions and no answer is assumed here.

## 16. Hostile-audit targets

Before promotion, an independent audit should attack:

- whether Lemma 3.1 correctly covers the declared one-head predicates with periodic backgrounds;
- the positional nonregularity reduction for EqGap;
- whether the two-head model accidentally smuggles EqGap in through its stopping condition;
- the distinction between local transition rule and transitive/reachability closure;
- graph-prefix consistency under finite truncation;
- whether “two heads are minimal” is stated only relative to this exact traversal hierarchy;
- whether the direct operation \(\triangleplus\) should be called generated addition rather than a primitive FCOA operation;
- whether any representation claim silently adds a Cartesian-product sort.

## 17. Status

The proofs in this note support the theorem candidate

\[
\boxed{
\mathbf W:\ H_1< H_2^{\mathrm{sync}}=AL1
\text{ with respect to EqGap/additive leakage.}
}
\]

No numbered G5 operation family is opened by this note.