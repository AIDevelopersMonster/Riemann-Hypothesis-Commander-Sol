# FCOA QGE3 — Exact Gluing Criterion for Local Multicolor Phases

**Branch:** `director/fcoa-rigidity-cost`  
**Status:** theorem note  
**Scope:** the phase sector of Model T, i.e. automorphisms for which local visible-support bijections exist

## 1. Setup

Let

\[
c:D\to O,
\qquad |O|=q\ge3,
\]

be surjective, and let

\[
\mathcal C(D)=\{C_1,\dots,C_r\}
\]

be the components of `Lambda(D)`.

Fix

\[
g\in A_T(D,c)=\operatorname{Aut}(G;D,Q_D).
\]

Assume that for every component `C_i` a local phase exists:

\[
\phi_i=
\phi_{g,C_i}:O_{C_i}\xrightarrow{\sim}O_{gC_i},
\]

with

\[
c(gp)=\phi_i(c(p))
\qquad(p\in C_i).
\]

The question is whether these local bijections are restrictions of one global anonymous color permutation

\[
\pi\in S_O.
\]

---

## 2. Union relation

Define the relation

\[
\boxed{
R_g
=
\bigcup_{i=1}^r
\{(a,\phi_i(a)):a\in O_{C_i}\}
\subseteq O\times O.
}
\]

Because `c` is globally surjective, every color `a in O` occurs in at least one component, so the first projection of `R_g` is all of `O`.

There are two possible defects.

### Source disagreement

The same source color appears in two components but receives different images:

\[
a\in O_{C_i}\cap O_{C_j},
\qquad
\phi_i(a)\ne\phi_j(a).
\]

Then `R_g` is not a function.

### Target collision

Two different source colors, possibly visible in disjoint component supports, receive the same image:

\[
a\ne b,
\qquad
\phi_i(a)=\phi_j(b).
\]

Then the function represented by `R_g` is not injective.

Both defects obstruct a global permutation.

---

## 3. Exact gluing theorem

### Theorem 3.1 — global phase criterion

Under the setup above, the following are equivalent.

1. There exists

\[
\pi\in S_O
\]

such that

\[
c(gp)=\pi(c(p))
\qquad\forall p\in D.
\]

2. `R_g` is the graph of a bijection `O->O`.

3. Both conditions hold:

   **(F) overlap agreement**
   \[
   \phi_i(a)=\phi_j(a)
   \quad
   \forall a\in O_{C_i}\cap O_{C_j};
   \]

   **(I) cross-support injectivity**
   \[
   a\ne b
   \Longrightarrow
   \phi_i(a)\ne\phi_j(b)
   \]
   whenever the two sides are defined.

When these conditions hold, the global phase is unique.

### Proof

`1=>2`: if a global permutation `pi` realizes `g`, each `phi_i` is the restriction of `pi` to `O_{C_i}`, hence `R_g` is exactly the graph of `pi`.

`2=>1`: the first projection of `R_g` is all of `O` by global surjectivity. If it is the graph of a bijection `pi`, then for every cell `p in C_i`,

\[
c(gp)=\phi_i(c(p))=\pi(c(p)).
\]

Thus `pi` realizes `g` globally.

`2<=>3`: condition (F) is exactly the statement that `R_g` is single-valued on each source color. Condition (I) is injectivity. A total injective self-map of finite `O` is bijective. `square`

---

## 4. Why overlap agreement alone is insufficient

For binary components with full two-color support, agreement on one color determines agreement on the other. For `q>=3` this is false.

Even if local phases agree wherever component supports overlap, two colors that are never simultaneously visible in an overlap may be sent to the same target color by different local maps.

Therefore the naive condition

\[
\phi_i|_{O_{C_i}\cap O_{C_j}}
=
\phi_j|_{O_{C_i}\cap O_{C_j}}
\]

is necessary but not sufficient in general.

The missing condition is cross-support injectivity.

---

## 5. A support-overlap sufficient criterion

There is a useful stronger situation where gluing simplifies.

Suppose the component supports form a family

\[
\mathcal O=\{O_C:C\in\mathcal C(D)\}
\]

such that for every pair of distinct global colors `a,b in O`, some component support contains both:

\[
\boxed{
\forall a\ne b\in O,
\quad
\exists C:
\{a,b\}\subseteq O_C.
}
\]

Call this the **pair-cover property**.

### Corollary 5.1

If the pair-cover property holds, then overlap agreement (F) alone implies the injectivity condition (I), and hence implies global gluing.

### Proof

Assume local phases agree on overlaps and suppose distinct colors `a,b` had the same global image. By pair-cover, there is a component `C` containing both. Inside `C`, `phi_C` is a bijection, so

\[
\phi_C(a)\ne\phi_C(b).
\]

Overlap agreement identifies these values with the values assigned to `a,b` in every other component where they occur, contradicting the alleged collision. `square`

Thus sufficiently rich visible-color overlap converts the gluing problem into ordinary restriction agreement.

---

## 6. Full-support components

If every comparison component sees the full alphabet,

\[
O_C=O
\qquad\forall C,
\]

then every local phase lies in `S_O` and the criterion becomes especially simple:

\[
\boxed{
\text{global phase exists}
\iff
\phi_{g,C_1}=\cdots=\phi_{g,C_r}.
}
\]

This is the closest direct analogue of the binary diagonal-phase criterion.

The “diagonal” is now the diagonal copy

\[
\boxed{
\Delta(S_q)
=\{(\pi,\dots,\pi):\pi\in S_q\}
\subseteq S_q^r.
}
\]

but this description is valid only in the full-support phase sector.

---

## 7. Partial-support groupoid formulation

For arbitrary supports, the local phases are arrows between subsets of the global alphabet:

\[
\phi_{g,C}:O_C\to O_{gC}.
\]

The exact global obstruction is the failure of these arrows to be restrictions of one permutation of `O`.

This may be formulated as an extension problem in the finite groupoid of subsets of `O` and bijections between them:

\[
\boxed{
\{\phi_{g,C}\}_C
\text{ glues globally }
\iff
\bigcup_C\operatorname{graph}(\phi_{g,C})
\text{ is the graph of an element of }S_O.
}
\]

No cohomological terminology is needed for this criterion.

---

## 8. Composition and gluing

Assume `g,h,gh` lie in the phase sector componentwise. Then

\[
\phi_{gh,C}
=
\phi_{g,hC}\circ\phi_{h,C}.
\]

If both `g` and `h` glue globally to `pi_g,pi_h in S_O`, then `gh` glues and

\[
\boxed{
\pi_{gh}=\pi_g\circ\pi_h.
}
\]

Thus the full anonymous carrier group is exactly the subgroup of phase-sector ternary automorphisms whose local groupoid arrows satisfy the gluing criterion.

---

## 9. Exactness criterion for Model T

Combining the local phase criterion from `NONABELIAN_PHASE_LAW.md` with the gluing theorem gives:

### Theorem 9.1 — complete ternary exactness criterion

The sparse ternary reduct is carrier-exact,

\[
\operatorname{Aut}(G;D,Q_D)
=
\operatorname{Aut}^{\rm an}(D,c),
\]

if and only if every `g in Aut(G;D,Q_D)` satisfies both:

1. **local fiber preservation:** on every comparison component `C`,
   \[
   c(p)=c(q)
   \iff
   c(gp)=c(gq)
   \qquad(p,q\in C);
   \]
2. **global gluing:** the induced local phases satisfy (F) and (I), equivalently their union relation is a permutation of `O`.

This separates the two genuinely different multicolor obstructions:

\[
\boxed{
\text{local proper-coloring ambiguity}
\quad+
\text{inter-component gluing ambiguity}.
}
\]

For `q=2`, the first obstruction disappears on connected comparison components and the second reduces to the binary diagonal-phase condition of Article B.
