# FCOA Rigidity Cost — Safe Escape-Cell Theorem

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.  
**Status:** post-publication theorem note.

---

## 1. Motivation

The strong open target is

\[
\alpha(D,c)=\beta(D,c),
\]

where `beta` is the minimum number of real new cells required to destroy all **old** bad automorphisms, while `alpha` additionally requires that the enlarged reduct contain no **newly created** bad automorphisms.

The only possible gap

\[
\sigma=\alpha-\beta>0
\]

comes from a new automorphism of the extension that moves the old domain `D` into a different deletion of the enlarged domain.

Thus a beta-optimal extension is automatically exact whenever the new cells are intrinsically recognizable inside the enlarged reduct.

---

## 2. Invariant cell signatures

Let

\[
S=D\cup E
\]

be an extension domain. A **domain-invariant cell signature** is any function

\[
\chi_S:S\to\mathcal X
\]

such that every carrier automorphism of the enlarged reduct `(G;S,Q_S)` preserves the signature:

\[
\chi_S(gp)=\chi_S(p).
\]

Examples of admissible signature coordinates include:

- whether the reverse cell is defined;
- in/out-degree data of the tail and head vertices in the directed definedness domain;
- sizes of the `Lambda(S)` components containing the cell;
- any further isomorphism-invariant local incidence data definable from `(G;S,Q_S)`.

No output value is named.

---

## 3. Safe Escape-Cell Theorem

### Theorem

Let `(E,b)` be a beta-optimal extension:

\[
|E|=\beta(D,c),
\]

and suppose there exists a domain-invariant cell signature `chi_S` on `S=D union E` such that

\[
\boxed{
\chi_S(E)\cap\chi_S(D)=\varnothing.
}
\]

Then

\[
\boxed{
\alpha(D,c)=\beta(D,c).
}
\]

### Proof

Because signature values of new and old cells are disjoint, every automorphism of `(G;S,Q_S)` preserves the subset `E` setwise and therefore also preserves

\[
D=S\setminus E
\]

setwise.

The No-old-obstruction theorem from Article B then applies: since `E` is beta-optimal, all old bad automorphisms have been destroyed; any reduct automorphism preserving `D` must be globally color-admissible on the enlarged layer. Therefore the extension is exact.

Hence

\[
\alpha(D,c)\le|E|=\beta(D,c).
\]

The reverse inequality `beta<=alpha` holds by definition. Thus equality follows. \(\square\)

---

## 4. Single-cell corollary

Suppose `beta(D,c)=1`. If there exists one beta-killing cell `e` such that, in the one-cell extension `S=D union {e}`, the cell `e` has an invariant signature not realized by any old cell, then

\[
\boxed{\alpha(D,c)=1.}
\]

This gives a concrete route to the desired theorem `beta=1 => alpha=1`: a counterexample must force **every** one-cell beta witness to be signature-indistinguishable from at least one old cell in its own extension.

---

## 5. Reverse-definedness specialization

Define

\[
\rho_S(x,y)=
\mathbf 1_{(y,x)\in S}.
\]

This is preserved by every carrier automorphism of the definedness domain.

Therefore, if all old cells have reverse cells defined while every new cell has reverse undefined, then the new set `E` is intrinsically recognizable and any beta-optimal extension of this form is exact.

This is exactly the mechanism used in the disjoint-bidirected-pair construction: old cells occur in bidirected pairs, whereas the added `a-a` bridges are one-way cells.

---

## 6. Degree-signature specialization

For a cell `p=(x,y)` in a domain `S`, define

\[
\chi_{\deg,S}(p)=
(d_S^-(x),d_S^+(x),d_S^-(y),d_S^+(y),\rho_S(x,y)).
\]

Every domain automorphism preserves this tuple.

Hence a beta-optimal extension is safe whenever every new cell has a degree/reverse signature absent from the old domain.

This provides a computationally cheap sufficient certificate for `alpha=beta`.

---

## 7. Why restricted-class counterexamples may disappear in full FCOA

A targeted search produced a one-way bipartite layer in which, **if extensions are artificially restricted to the same bipartite cell class**, a one-cell old-obstruction repair necessarily creates a new bad symmetry.

However, the candidate disappears in the full FCOA model. Once arbitrary off-diagonal cells are allowed, many cross-role cells provide beta-killing one-cell extensions whose domain signatures are absent from the old bipartite layer. These are escape cells, and several are exact.

Thus a positive surcharge can be an artifact of an extension-class restriction. Any genuine FCOA counterexample must survive the entire off-diagonal complement.

This is evidence, not a theorem of universal existence of an escape cell.

---

## 8. Exact one-cell kill criterion for old bad automorphisms

Let `g` be an old bad automorphism and let `e` be one undefined cell. Consider the one-cell extension by `e` with either binary color.

Because `g(D)=D`, the complement of `D` is also `g`-invariant.

Then `g` is killed by the one-cell extension if either:

1. `g(e) != e`, in which case `g` no longer preserves the enlarged domain `D union {e}`; or
2. `g(e)=e`, but `e` becomes `Lambda`-adjacent to an old phase-1 component of `g`. Since the fixed new cell has discrepancy 0, componentwise phase constancy fails.

This criterion is independent of the chosen binary color of the new cell.

Hence, for `beta=1`, the old-obstruction part of the problem is purely geometric: one seeks a single undefined cell that kills every old bad automorphism by one of the two mechanisms above. The color choice matters only for possible **new** automorphisms of the enlarged reduct.

---

## 9. Consequence for a minimal positive surcharge

If a layer has

\[
\beta=1<\alpha,
\]

then every one-cell beta witness must simultaneously satisfy all of the following:

1. it kills every old bad automorphism by the exact one-cell criterion;
2. for both binary color choices, the enlarged reduct has a newly created bad automorphism;
3. that new automorphism moves the old domain `D`;
4. the new cell is not intrinsically recognizable by any chosen invariant cell signature sufficient to separate it from old cells.

This is substantially stronger than the deletion-symmetry condition from Article B.

---

## 10. Current computational evidence

Targeted searches on `n=6, |D|=8` were biased toward states with a prescribed transposition already acting as an old bad automorphism. Thousands of genuinely bad states with one-cell beta witnesses were examined; no case with `beta=1<alpha` was found.

A restricted bipartite candidate exhibiting a surcharge inside the restricted extension class was also tested in the full eight-carrier FCOA model. The old layer has exactly one old bad automorphism. In the full complement there are many one-cell beta witnesses, and most are already exact; the restricted surcharge therefore vanishes.

These searches are exploratory and are not exhaustive theorems.

---

## 11. Research consequence

The strong conjecture remains

\[
\boxed{\alpha(D,c)=\beta(D,c).}
\]

The Safe Escape-Cell Theorem proves it for every layer admitting a beta-optimal extension with an intrinsic new-cell signature.

A genuine counterexample must therefore be **extension-saturated** in a strong sense: every beta-optimal extension must be deletion-ambiguous and must lack any invariant signature that separates new cells from old ones.

This suggests that the next search should target highly homogeneous/saturated domains rather than generic sparse domains.

---

## Claim firewall

1. The theorem is a sufficient criterion, not a proof that safe escape cells always exist.
2. The degree signature is one convenient certificate, not a complete invariant.
3. The restricted bipartite surcharge is not an FCOA counterexample and is not reported as one.
4. The one-cell old-obstruction kill criterion concerns survival of old bad automorphisms; it does not by itself rule out newly created bad symmetries.
5. Articles A and B remain frozen publications.
