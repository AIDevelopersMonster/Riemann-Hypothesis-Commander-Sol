# FCOA Rigidity Cost — Replacement Boundary Theorem (Corrected)

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** corrected post-publication theorem note.

## 1. Domain replacement defect

For a carrier permutation `g`, define

\[
P_D(g)=g(D)\setminus D,
\qquad
N_D(g)=D\setminus g(D),
\]

and

\[
d_D(g)=|P_D(g)|=|N_D(g)|.
\]

If `S=D union E`, `|E|=k`, and `g` preserves `S` but moves `D`, then

\[
\boxed{P_D(g)\subseteq E,\qquad 1\le d_D(g)\le k.}
\]

This is the Replacement Boundary Theorem and is purely a definedness statement.

## 2. Replacement hypergraph

Define

\[
\mathcal R_{\le k}(D)
=
\{P_D(g):1\le d_D(g)\le k\}.
\]

Every newly created automorphism moving the old domain in a `k`-cell extension must have one of these positive defect sets contained in `E`.

For `k=1`, define

\[
R_1(D)=\{e\notin D:\exists g,\ d_D(g)=1,\ P_D(g)=\{e\}\}.
\]

Equivalently, `e in R_1(D)` iff for some old cell `p` and carrier permutation `g`,

\[
g(D)=D-\{p\}+\{e\}.
\]

## 3. Correct safe-set criterion

The earlier version claimed that avoidance of the replacement hypergraph alone made a beta-valid extension exact. That omitted a separate phase issue: even when every surviving automorphism preserves `D`, a completely new incidence component can carry an independent phase.

The corrected statement is:

### Theorem 3.1

Let `(E,b)` be beta-valid with `|E|=beta(D,c)=k`. Assume:

1. `E` avoids every positive defect set:
   \[
   P\nsubseteq E
   \quad\text{for all }P\in\mathcal R_{\le k}(D);
   \]
2. every connected component of `Lambda(D union E)` contains an old cell from `D`.

Then

\[
\boxed{\alpha(D,c)=\beta(D,c).}
\]

### Proof

Condition 1 and the Replacement Boundary Theorem imply that every automorphism of the enlarged reduct preserves `D` setwise. Beta-validity then implies that its restriction to `D` has one global anonymous phase. By condition 2, every enlarged incidence component contains an old cell, so Componentwise Phase forces the same old phase on every component. Hence the automorphism is globally anonymous-color compatible. `square`

## 4. Correct beta=1 escape criterion

Let `W_kill(D,c)` be the missing cells whose singleton addition kills every old bad automorphism. If

\[
\beta(D,c)=1
\]

and there exists

\[
e\in W_{kill}(D,c)\setminus R_1(D)
\]

such that `e` is adjacent to at least one old cell in `Lambda(D union {e})`, then

\[
\boxed{\alpha(D,c)=1.}
\]

The adjacency hypothesis is the one-cell form of anchoring.

Thus a beta=1 positive surcharge can occur only if every **anchored** beta-killing escape cell lies in the one-cell replacement boundary, while any non-anchored candidates must also fail exactness through their independent new-component phase geometry.

## 5. Two-component theorem

If `Lambda(D)` has exactly two connected components and the old reduct is nonexact, then

\[
\boxed{\lambda(D,c)=\beta(D,c)=\alpha(D,c)=1.}
\]

Indeed, one bridge cell can join the two old components. The enlarged incidence graph is connected, so it is automatically anchored; connectivity then forces one global phase.

Thus any positive surcharge requires

\[
\boxed{\kappa(\Lambda(D))\ge3.}
\]

## 6. Minimal-counterexample conditions

Any counterexample to `alpha=beta` must now satisfy all of the following:

1. at least three old incidence components;
2. every beta-optimal beta-valid extension either contains a low-defect replacement set or fails anchoring;
3. if a beta-optimal extension avoids all replacement sets and is anchored, it is automatically safe;
4. for beta=1, every anchored beta-killing cell outside `R_1(D)` would already force `alpha=1`.

This separates two distinct dangers:

\[
\boxed{\text{domain replacement ambiguity}}
\]

and

\[
\boxed{\text{unanchored independent phase}}.
\]

## 7. Computational evidence

Targeted searches on six carrier points exhibit individual beta-killing cells that are unsafe for both binary colors because they complete a one-cell domain replacement symmetry. However alternative safe cells have always been found in the inspected layers.

A random stress search over 1,000,000 six-carrier sparse binary layers found 19,408 sampled nonexact layers with beta=1. No sampled case had an exact one-cell repair without also possessing an anchored-recognizable beta-killing one-cell repair. This is not an exhaustive theorem.

## Claim firewall

1. Replacement-boundary avoidance controls domain-moving symmetries only.
2. Anchoring is separately required in the corrected safe-set theorem.
3. Membership in a replacement boundary does not by itself imply a bad colored automorphism.
4. The two-component theorem remains valid.
5. No global proof of `alpha=beta` is claimed.
