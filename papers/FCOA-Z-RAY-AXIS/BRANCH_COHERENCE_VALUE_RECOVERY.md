# FCOA-Z — Recovering the One-Bit Branch Connection from Operation Values

Status: theorem package v0.1  
Date: 2026-08-31

This note continues the hostile-audit corrected `MINIMAL_BRANCHING_NONABELIAN_TRANSPORT.md`.

The corrected branching theorem found that the minimal seven-vertex binary carrier has ambient group

\[
\operatorname{Aut}(T)\cong D_8,
\]

but that a preferred lift between the two isomorphic cherries is not canonically determined by the unlabeled carrier. The lift set is a `C_2` torsor, so exactly one coherence bit must be supplied.

The present theorem asks whether that bit can be **compiled into FCOA operation values and recovered after the explicit connection is erased**.

The answer is yes. Moreover:

\[
\boxed{
\text{one anonymous output is impossible; two anonymous outputs plus one canonical anchor cell suffice.}
}
\]

The value layer reduces the active symmetry by index exactly two — no more and no less.

---

## 1. FCOA framework

The ambient framework is FCOA Definition 1.0:

A. Malachevsky, *Fixed-Carrier Oriented Algebra (FCOA): Definition, Typed Partial Operations, Carrier Erasure, and the Canonical M0 Baseline*, Zenodo, 2026, DOI `10.5281/zenodo.22164246`.

We use the seven-vertex rooted binary tree

\[
T=\{o,u,v,a_0,a_1,b_0,b_1\},
\]

where

- `o` is the root;
- `u,v` are its children;
- `a_0,a_1` are the leaves below `u`;
- `b_0,b_1` are the leaves below `v`.

The explicit labels are expository. The retained radial operation/reduct recovers the parent map and hence has active automorphism group

\[
G=\operatorname{Aut}(T,o,\rho)\cong D_8.
\]

The connection datum itself will be erased.

---

## 2. The two possible coherence choices

A rooted isomorphism between the two cherries is determined by a bijection between their two leaf sets.

There are exactly two possibilities:

\[
M_0=\{\{a_0,b_0\},\{a_1,b_1\}\},
\]

\[
M_1=\{\{a_0,b_1\},\{a_1,b_0\}\}.
\]

These are the two cross-branch perfect matchings.

They are precisely the two points of the lift torsor found in the preceding theorem package.

### Proposition 2.1 — Connection Action

The group `G ~= D_8` acts transitively on

\[
\{M_0,M_1\}.
\]

The stabilizer of either chosen matching has order four and index two.

For `M_0`, one convenient description is

\[
\operatorname{Stab}_G(M_0)
=
\{1,s_us_v,r,rs_us_v\}
\cong C_2\times C_2,
\]

for a compatible choice of one branch-exchange lift `r`.

Hence

\[
\boxed{
[G:\operatorname{Stab}_G(M_i)]=2.
}
\]

#### Proof

A lower swap in only one cherry changes parallel matching to crossed matching, so the two matchings lie in one orbit. Orbit-stabilizer then gives stabilizer order `8/2=4`. The displayed subgroup preserves `M_0` and has four elements, so it is the full stabilizer. □

Thus the connection is literally one group-theoretic bit.

---

## 3. Why one output cannot store the bit in values

Suppose a new pure terminal partial operation has a fixed domain `D`, and every defined cell has the same terminal value `Omega`.

Then every active automorphism preserving `D` automatically preserves the operation value pattern.

This is exactly the One-Output Collapse theorem of the published Value-Rigidity line:

\[
|O|=1\Longrightarrow VRI=1.
\]

### Theorem 3.1 — One-Output Impossibility

If the connection scaffold is erased and its two choices are required to differ only through operation **values on one fixed domain**, a one-element anonymous terminal alphabet cannot distinguish `M_0` from `M_1`.

#### Proof

With one output, the operation graph contains no information beyond definedness. Since the domain is fixed independently of the connection choice, the two value tables coincide. □

So at least two terminal values are necessary for value-only recovery.

---

## 4. Equal-fiber trap for two anonymous outputs

Two outputs are not automatically enough.

Let the fixed cross-branch directed domain be

\[
D_\times=
(A\times B)\cup(B\times A),
\]

where

\[
A=\{a_0,a_1\},\qquad B=\{b_0,b_1\}.
\]

This domain contains eight ordered cells.

If one colors exactly the four directed cells belonging to a chosen matching by `Omega_+` and the four belonging to its complement by `Omega_-`, the two fibers have equal cardinality.

Because the complement of `M_0` inside the cross domain is exactly `M_1`, an active automorphism exchanging the two connection choices may be accompanied by

\[
\Omega_+\leftrightarrow\Omega_-.
\]

Therefore anonymous output exchange can hide the bit.

### Proposition 4.1 — Equal-Fiber Failure

The balanced `4+4` two-output coloring does not force the active stabilizer down to `Stab_G(M_i)` when permutations of the two anonymous terminal values are admitted.

This is the same output-exchange issue already encountered in the Value-Rigidity programme.

---

## 5. Anchored two-output readout

Introduce one new partial binary operation symbol

\[
\chi:T\times T\rightharpoonup\{\Omega_+,\Omega_-\},
\]

with two anonymous terminal outputs.

Its domain is fixed independently of the coherence bit:

\[
D_\chi=D_\times\cup\{(o,o)\}.
\]

Thus

\[
|D_\chi|=9.
\]

Choose one connection matching `M`.

Define:

1. the root anchor

\[
\chi(o,o)=\Omega_+;
\]

2. for a directed cross-branch cell `(x,y)`, set

\[
\chi(x,y)=\Omega_+
\]

iff the underlying unordered pair `{x,y}` belongs to `M`;

3. all other cells of `D_xi` receive `Omega_-`.

Then the fiber sizes are

\[
|\chi^{-1}(\Omega_+)|=5,
\qquad
|\chi^{-1}(\Omega_-)|=4.
\]

No automorphism can exchange the two terminal outputs because their fibers have different cardinalities.

---

## 6. Exact Value-Rigidity Theorem

### Theorem 6.1 — One-Bit Value Compilation

Relative to the retained radial carrier structure with active automorphism group `G ~= D_8`, the anchored two-output operation `chi` has active automorphism group

\[
\boxed{
\pi_T\operatorname{Aut}(\rho,\chi)
=\operatorname{Stab}_G(M).
}
\]

Consequently

\[
\boxed{
VRI_{G}(\chi)
=[G:\operatorname{Stab}_G(M)]
=2.
}
\]

Thus the value layer stores exactly one bit of additional structure.

#### Proof

The root anchor is preserved because `o` is already the unique radial root. The two output fibers have unequal sizes `5` and `4`, so no full automorphism can exchange `Omega_+` and `Omega_-`.

Therefore every operation automorphism must preserve the `Omega_+` cross-cell set. Removing the fixed root anchor from that fiber leaves exactly the directed realization of the chosen matching `M`. Hence the active carrier action must stabilize `M`.

Conversely every element of `Stab_G(M)` preserves the fixed cross domain, the root anchor, and both value fibers, so it extends to an automorphism of the two-output operation fixing each terminal value.

Thus the active automorphism group is exactly the matching stabilizer. Proposition 2.1 gives index two. □

### Interpretation

The construction does not rigidify the carrier completely:

\[
|G|=8\longrightarrow|\operatorname{Stab}_G(M)|=4.
\]

It destroys exactly the symmetry that exchanges the two possible branch connections and preserves all symmetry internal to the chosen connection.

This is **selective value-rigidity**, not maximal rigidity.

---

## 7. Recovery after erasing the explicit connection

Now erase the primitive matching `M` from the presentation. Retain only the radial FCOA structure and the operation `chi`.

### Theorem 7.1 — Definable Connection Recovery

The chosen connection matching is recoverable from the operation table.

In relationalized form, let

\[
T_\chi(x,y,z)
\iff
\chi(x,y)=z.
\]

The root is already recoverable from the radial structure; moreover it is the unique point with a `chi`-defined diagonal cell.

Let `z_*` be the unique terminal value satisfying

\[
T_\chi(o,o,z_*).
\]

Then for distinct non-root participating leaves `x,y`, the selected connection relation is

\[
\boxed{
M(x,y)
\iff
T_\chi(x,y,z_*)\lor T_\chi(y,x,z_*).
}
\]

with the root anchor excluded.

#### Proof

By construction the terminal value appearing at `(o,o)` is `Omega_+`. Because the two values are not named externally, the root cell internally names the required fiber. Exactly the directed matching cells share that output value apart from the root anchor. Therefore the formula recovers the matching. □

Thus the coherence bit survives explicit connection erasure.

---

## 8. Recovering the branch partition from definedness

Even if the explicit tree relation were hidden at the leaf layer, the fixed cross-domain itself carries the two-by-two branch partition.

Among the four participating leaves, two distinct leaves lie in the same branch iff neither orientation of their pair belongs to `D_xi`.

Hence the cross-domain graph is `K_{2,2}` and its bipartition is unique up to global side exchange.

### Corollary 8.1

At the leaf layer, the pair

\[
(D_\chi,\text{value fiber selected by the root anchor})
\]

recovers both:

1. the unordered two-branch partition;
2. the selected perfect matching across the branches.

The only remaining side exchange is an actual symmetry of the connected structure, not loss of the coherence bit.

---

## 9. Minimal alphabet theorem

### Theorem 9.1

For value-only encoding on a fixed connection-independent domain:

\[
\boxed{
2\text{ anonymous terminal values are minimal and sufficient}
}
\]

for recovery of the seven-vertex one-bit branch connection, provided one canonically fixed anchor cell is available to break output-label exchange.

#### Proof

Necessity of at least two values is Theorem 3.1.

Sufficiency is Theorems 6.1 and 7.1. □

### Scope caution

The theorem proves minimal **output alphabet cardinality**, not minimal total number of defined operation cells. The present symmetric construction uses eight directed cross cells plus one anchor. Support-minimization is a separate extremal problem.

---

## 10. Why the anchor is structurally natural

The extra cell does not store a second independent bit.

Its only role is to make one anonymous output fiber internally nameable and to prevent a global output swap.

The root is already distinguished by radial FCOA geometry, so `(o,o)` is a canonical active pair. Using it as a readout anchor does not introduce a new carrier orientation or branch label.

Thus the additional resource is better described as

\[
\boxed{
\text{two anonymous values + one zero-information canonical anchor}
}
\]

rather than “three colors” or “an externally named color”.

---

## 11. Relation to the Value-Rigidity programme

The earlier publication established two extremes:

\[
|O|=1\Rightarrow VRI=1,
\]

while two outputs can attain maximal active rigidity.

The present result supplies an intermediate exact example:

\[
\boxed{
|O|=2,\qquad VRI=2,\qquad |G|=8\to4.
}
\]

So two outputs need not destroy all symmetry. They can encode exactly one selected quotient bit of the automorphism group.

This suggests a broader programme of **targeted value-rigidity**:

> given `H <= G = Aut(D)`, what is the minimum output alphabet and support required for a partial operation with active automorphism group exactly `H`?

The branch-coherence problem is the first `index-2` instance.

---

## 12. Consequence for non-Abelian holonomy

Once the connection matching `M` is recovered, a preferred isomorphism between the two cherries is fixed up to the convention represented by that matching. The upper branch lift therefore becomes operationally available rather than externally supplied.

Combining it with the intrinsic lower cherry swap yields definite noncommuting elements of `D_8`.

Thus the chain is now:

\[
\boxed{
\text{branching carrier}
\to
\text{one-bit lift ambiguity}
\to
\text{two-value compilation}
\to
\text{connection recovery}
\to
\text{definite noncommuting transport word}.
}
\]

The non-Abelian transport is not produced by bare geometry alone; it is produced by geometry plus the **minimal recoverable coherence memory**.

---

## 13. Next strike — support cost of one-bit coherence

The output-cardinality question is solved:

\[
|O|_{\min}=2.
\]

The next extremal question is finer:

\[
\boxed{
\text{how many operation cells are minimally necessary to reduce }D_8\text{ to the connection stabilizer }V_4?
}
\]

Equivalently, for the transitive action of `D_8` on the two connection choices, find the sparsest value fiber whose stabilizer is exactly the desired index-two subgroup, under the restriction that definedness itself remain connection-independent.

This is a small exact targeted-value-rigidity problem and should be solvable completely by orbit/stabilizer analysis before any larger-tree generalization.