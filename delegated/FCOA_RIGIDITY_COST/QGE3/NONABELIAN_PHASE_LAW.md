# FCOA QGE3 — Nonabelian Phase Law and Its Exact Domain of Validity

**Branch:** `director/fcoa-rigidity-cost`  
**Status:** theorem note  
**Model:** sparse ternary equality reduct `\mathcal T(D,c)`

## 1. Executive result

For `q>=3`, a universal componentwise `S_q` phase does **not** exist. The universally defined local object is the transport of a proper coloring of the T-constraint quotient `H_T(C)`.

An honest permutation-valued phase appears precisely on those component/automorphism pairs for which the transported proper coloring is equivalent to the original coloring by a color-name permutation.

A clean sufficient condition is unique colorability of the quotient.

---

## 2. Proper-coloring transport theorem

Let

\[
g\in A_T(D,c)=\operatorname{Aut}(G;D,Q_D)
\]

and let `C` be a connected component of `Lambda(D)`.

Because `g` preserves the domain and ternary equality relation, it maps equal-comparison edges to equal-comparison edges and unequal-comparison edges to unequal-comparison edges. Therefore it maps T-equality atoms to T-equality atoms and induces a graph isomorphism

\[
\boxed{
\bar g_C:H_T(C)\longrightarrow H_T(gC).
}
\]

Let

\[
\kappa_C:V(H_T(C))\to O_C
\]

and

\[
\kappa_{gC}:V(H_T(gC))\to O_{gC}
\]

be the proper colorings induced by the terminal fibers.

Transport the target coloring back to the source quotient:

\[
\boxed{
\kappa_C^{\,g}:=
\kappa_{gC}\circ\bar g_C.
}
\]

Then `kappa_C^g` is another proper coloring of the same abstract graph `H_T(C)`.

### Theorem 2.1 — universal local state

For every ternary-reduct automorphism `g` and comparison component `C`, the orbit

\[
\boxed{
[\kappa_C^{\,g}]
\in
\operatorname{Col}(H_T(C))/S_O
}
\]

is well-defined, where `S_O` acts by relabeling output names.

A local anonymous phase

\[
\phi_{g,C}:O_C\to O_{gC}
\]

exists if and only if

\[
\boxed{
[\kappa_C^{\,g}]=[\kappa_C].
}
\]

When it exists, it is unique on `O_C` and satisfies

\[
\kappa_C^{\,g}=\phi_{g,C}\circ\kappa_C.
\]

### Proof

The induced quotient isomorphism exists by preservation of equal versus unequal comparison edges. Hence `kappa_C^g` is a proper coloring.

If a local phase exists, then for every atom `A` and any cell `p in A`,

\[
\kappa_C^g(A)=c(gp)=\phi_{g,C}(c(p))
=\phi_{g,C}(\kappa_C(A)),
\]

so the two proper colorings differ only by a relabeling.

Conversely, if the two proper colorings differ by a bijection of visible color sets, that bijection is exactly the required local phase. Surjectivity of `kappa_C` onto `O_C` makes it unique on `O_C`. `square`

Thus the always-defined phase object is not an element of `S_q`; it is a point in a proper-coloring orbit space.

---

## 3. Color-rigid components

Call a T-component `C` **color-rigid** when every proper coloring of `H_T(C)` using exactly `|O_C|` nonempty colors belongs to the same orbit under permutation of color names as `kappa_C`.

Equivalently, the partition of `V(H_T(C))` into color classes is unique among proper `|O_C|`-color partitions.

This is the standard graph-theoretic notion of unique colorability when

\[
|O_C|=\chi(H_T(C)).
\]

For the FCOA application we keep the definition relative to the actually visible number of colors, because `kappa_C` need not be chromatic-minimal in arbitrary sparse data.

### Theorem 3.1 — color-rigidity restores local phase

Suppose `C` and `gC` have the same visible color count and `C` is color-rigid. Then every

\[
g\in A_T(D,c)
\]

induces a unique local visible-support bijection

\[
\boxed{
\phi_{g,C}:O_C\xrightarrow{\sim}O_{gC}
}
\]

satisfying

\[
c(gp)=\phi_{g,C}(c(p))
\qquad(p\in C).
\]

### Proof

The transported coloring `kappa_C^g` is a proper coloring of `H_T(C)` using exactly `|O_{gC}|=|O_C|` nonempty colors. Color-rigidity says it is equivalent to `kappa_C` under a unique permutation of the visible color classes. Apply Theorem 2.1. `square`

### Important special case

If every component quotient `H_T(C)` is uniquely `r_C`-colorable and the actual component uses exactly `r_C=chi(H_T(C))` colors, every ternary-reduct automorphism has a local permutation phase on every component.

This is the precise multicolor replacement for binary phase propagation in the color-rigid sector.

---

## 4. Why binary is exceptional

In the binary branch, after equality atoms are contracted, a connected comparison component produces a connected bipartite quotient whose two-color partition is unique up to swapping the two sides.

Therefore its proper-coloring orbit space has one binary state, and every ternary-reduct automorphism necessarily remains in that state. This is exactly why a phase bit exists automatically.

For `q>=3`, a connected graph can have many inequivalent proper `q`-color partitions. Connectedness therefore no longer collapses the local state space.

So the conceptual transition is

\[
\boxed{
q=2:\ \text{connected comparison geometry forces unique coloring orbit};
}
\]

\[
\boxed{
q\ge3:\ \text{connected comparison geometry need not force a unique coloring orbit}.
}
\]

This is stronger than merely saying that `S_q` is nonabelian: the primary obstruction occurs **before** a group-valued phase is available.

---

## 5. Nonabelian composition law when phases exist

Assume local phases exist for the relevant pairs. Let

\[
g,h\in A_T(D,c)
\]

and let `C` be a comparison component.

Then

\[
h:C\to hC,
\qquad
g:hC\to ghC.
\]

For every `p in C`,

\[
c(ghp)
=\phi_{g,hC}(c(hp))
=\phi_{g,hC}(\phi_{h,C}(c(p))).
\]

By uniqueness of the phase on the visible support,

\[
\boxed{
\phi_{gh,C}
=
\phi_{g,hC}\circ\phi_{h,C}.
}
\]

This is the exact composition law.

It is generally noncommutative because the phase maps are permutations or partial visible-support bijections and composition order matters.

### Interpretation

The natural domain of the phase law is a **groupoid**:

- objects: visible supports `O_C` attached to comparison components;
- arrows: the local bijections `phi_{g,C}:O_C -> O_{gC}` realized by ternary-reduct automorphisms;
- composition: the formula above.

If every component sees the whole alphabet `O`, the arrows lie in `S_O`, and the law can be written

\[
\boxed{
\phi_{gh}(C)=\phi_g(hC)\,\phi_h(C).
}
\]

This is the nonabelian analogue of the binary twisted component law. We call it a cocycle/crossed law only after fixing the induced action on components, because the coefficient system is transported with the component.

---

## 6. Exact phase-existence criterion without unique colorability

Unique colorability is sufficient but not necessary.

For a fixed `g,C`, define the source color partition

\[
\mathcal P_C=\{\kappa_C^{-1}(a):a\in O_C\}
\]

and the transported target partition pulled back along `bar g_C`:

\[
\mathcal P_C^g
=\{(\kappa_C^g)^{-1}(b):b\in O_{gC}\}.
\]

### Theorem 6.1

A local phase exists for `(g,C)` if and only if

\[
\boxed{\mathcal P_C^g=\mathcal P_C}
\]

as set partitions of `V(H_T(C))`.

Equivalently, for all cells `p,q in C`,

\[
\boxed{
c(p)=c(q)
\iff
c(gp)=c(gq).}
\]

### Proof

A bijection of color labels exists exactly when the fiber partition is transported to the fiber partition. `square`

This criterion is exact and contains no group-theoretic assumption.

---

## 7. Sharp no-go conclusion

The full ternary sparse theory therefore has two layers:

### Universal layer

\[
\boxed{
\text{T-reduct automorphism}
\Longrightarrow
\text{proper-coloring transport on }H_T(C).
}
\]

### Phase sector

\[
\boxed{
\text{fiber partition preserved on }C
\Longleftrightarrow
\text{local visible-support permutation exists}.
}
\]

Only in the phase sector is an `S_q`/partial-permutation cocycle meaningful.

Thus the correct answer to the first delegated question is:

\[
\boxed{
\textbf{The universal q>=3 local phase object is a proper-coloring orbit, not an }S_q\textbf{ element.}
}
\]

`S_q` appears as the symmetry group of a color-rigid orbit or for individual automorphisms that preserve the component fiber partition.

---

## 8. Relation to Model E

For Model E, arbitrary cell equality is retained. Therefore every carrier automorphism preserving `E_D` automatically satisfies the criterion of Theorem 6.1 simultaneously on all cells, not merely componentwise.

Consequently Model E skips the proper-coloring ambiguity and directly yields one global

\[
\pi\in S_O.
\]

This is the structural meaning of the arity-3 versus arity-4 distinction in the sparse setting.

---

## 9. Claim firewall

1. No universal `S_q` component phase is claimed for Model T.
2. The proper-coloring orbit statement is exact.
3. Unique colorability is a sufficient structural hypothesis, not claimed necessary.
4. The nonabelian phase composition law is asserted only where local phases exist.
5. No novelty claim about uniquely colorable graphs or gain/switching theory is made; literature positioning is separate.
