# FCOA Rigidity Cost — Replacement Boundary Theorem

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.  
**Status:** post-publication theorem note.

---

## 1. Purpose

The only possible gap between

\[
\beta(D,c)
\]

(the minimum real-cell cost of killing all old bad automorphisms) and

\[
\alpha(D,c)
\]

(the minimum cost of making the enlarged reduct exact) is creation of a **new** bad automorphism which does not preserve the old domain `D`.

This note identifies the precise domain-level combinatorial object in which every such new symmetry must live.

---

## 2. Defect sets of carrier permutations

Let

\[
D\subseteq G^2\setminus\Delta.
\]

For a carrier permutation \(g\in S_G\), define

\[
P_D(g)=g(D)\setminus D,
\]

\[
N_D(g)=D\setminus g(D).
\]

Because \(|g(D)|=|D|\),

\[
\boxed{|P_D(g)|=|N_D(g)|.}
\]

Call

\[
d_D(g):=|P_D(g)|=|N_D(g)|
\]

the **domain replacement defect** of `g`.

Defect zero means `g` is an automorphism of the definedness domain.

---

## 3. Replacement Boundary Theorem

### Theorem

Let

\[
S=D\cup E,
\qquad E\cap D=\varnothing,
\qquad |E|=k.
\]

Suppose

\[
g\in\operatorname{Aut}(G;S,Q_S)
\]

but

\[
g(D)\ne D.
\]

Then

\[
\boxed{
P_D(g)\subseteq E,
\qquad
1\le d_D(g)\le k.
}
\]

Moreover

\[
g(D)=D-N_D(g)+P_D(g).
\]

### Proof

Since `g` preserves the enlarged definedness domain `S`,

\[
g(D)\subseteq S=D\cup E.
\]

Therefore every cell in

\[
g(D)\setminus D
\]

must lie in `E`, giving

\[
P_D(g)\subseteq E.
\]

Since `g(D) != D`, the defect is positive. Since `P_D(g) subseteq E`, its cardinality is at most `k`. Equal cardinality of the positive and negative defect sets follows from \(|g(D)|=|D|\). \(\square\)

The theorem is independent of colors and of the phase cocycle. It is a pure definedness constraint on every symmetry-creation event.

---

## 4. The one-cell replacement boundary

Define

\[
\boxed{
R_1(D)=
\{e\notin D:\exists g\in S_G,\ d_D(g)=1,\ P_D(g)=\{e\}\}.
}
\]

Equivalently, `e` belongs to `R_1(D)` exactly when there are an old cell `p in D` and a carrier permutation `g` such that

\[
\boxed{
g(D)=D-\{p\}+\{e\}.}
\]

Thus `R_1(D)` is the set of missing operation cells that can complete a one-cell deletion symmetry of the old domain.

---

## 5. Exact beta=1 escape criterion

Let

\[
W_{\rm kill}(D,c)
\]

be the set of undefined cells which, when added, destroy every **old** bad automorphism. By definition,

\[
\beta(D,c)=1
\iff
W_{\rm kill}(D,c)\ne\varnothing.
\]

### Theorem — Replacement-boundary escape

If

\[
\beta(D,c)=1
\]

and there exists

\[
e\in W_{\rm kill}(D,c)\setminus R_1(D),
\]

then

\[
\boxed{\alpha(D,c)=1.}
\]

### Proof

Add `e` with either binary color. The cell kills every old bad automorphism by assumption.

Suppose the resulting reduct had a new bad automorphism `g` moving the old domain. By the Replacement Boundary Theorem with `k=1`,

\[
P_D(g)=\{e\},
\]

so

\[
e\in R_1(D),
\]

contrary to assumption.

Hence no new bad automorphism can move `D`. No-old-obstruction then implies the extension is exact. Therefore `alpha=1`. \(\square\)

This theorem is stronger than any particular signature-based escape criterion: it uses the complete domain replacement geometry rather than one chosen cell invariant.

---

## 6. Necessary condition for a beta=1 surcharge

A positive surcharge

\[
\beta=1<\alpha
\]

is possible only if

\[
\boxed{
W_{\rm kill}(D,c)\subseteq R_1(D).
}
\]

Thus every old-obstruction-killing cell must simultaneously be a one-cell symmetry-completion cell of the definedness domain.

Call such a layer **replacement-saturated at level one**.

This is now the exact domain-level search target for a minimal positive surcharge.

---

## 7. General replacement hypergraph

For an integer `k>=1`, define the family

\[
\boxed{
\mathcal R_{\le k}(D)=
\{P_D(g):g\in S_G,\ 1\le d_D(g)\le k\}.
}
\]

This is a hypergraph on the undefined cell set

\[
\overline D=(G^2\setminus\Delta)\setminus D.
\]

Every hyperedge is the positive defect set of a carrier permutation that moves the old domain by at most `k` cell replacements.

### Safe-set corollary

Let `E` be a beta-optimal extension with

\[
|E|=\beta(D,c)=k.
\]

If

\[
\boxed{
P\nsubseteq E
\qquad\text{for every }P\in\mathcal R_{\le k}(D),
}
\]

then

\[
\boxed{
\alpha(D,c)=\beta(D,c).
}
\]

Indeed, any new automorphism moving `D` would, by the Replacement Boundary Theorem, have a nonempty positive defect set `P_D(g)` contained in `E`, contradicting the avoidance condition. Since the extension already kills every old bad automorphism, it is exact.

Thus the Strong Safe-Extension Conjecture becomes the following finite avoidance problem:

> Does every sparse binary layer admit a beta-optimal old-obstruction-killing extension which avoids all low-defect replacement hyperedges of its old domain?

---

## 8. Relation to deletion symmetry

For `k=1`, an unsafe cell `e` creates an enlarged domain

\[
S=D\cup\{e\}
\]

with an automorphism sending `e` to some old cell `p`. Equivalently, two single-cell deletions

\[
S\setminus\{e\}=D
\]

and

\[
S\setminus\{p\}
\]

lie in the same carrier orbit.

For general `k`, positive defect sets encode the analogous multi-cell deletion ambiguity.

The replacement hypergraph is therefore a concrete finite version of the deletion-symmetry obstruction isolated in Article B.

---

## 9. Two-component theorem

A separate structural consequence closes an entire class.

### Theorem

If the ordered-cell incidence graph \(\Lambda(D)\) has exactly two connected components and the sparse ternary reduct is not exact, then

\[
\boxed{
\lambda(D,c)=\beta(D,c)=\alpha(D,c)=1.
}
\]

### Proof

With exactly two components, every non-diagonal binary phase signature is either `(0,1)` or `(1,0)`. Thus one equality link between the two components kills every old bad signature, so `lambda=1` and `beta<=1`. Since the original layer is not exact, `beta>=1`, hence `beta=1`.

By the One-Cell Bridge Lemma, one undefined cell can join the two incidence components. The enlarged incidence graph is then connected. By the Sparse-Domain Phase Theorem, the enlarged ternary reduct is exact for either color of the bridge. Hence `alpha=1`. \(\square\)

Therefore any positive symmetry-creation surcharge requires

\[
\boxed{\kappa(\Lambda(D))\ge3.}
\]

---

## 10. Sharpened minimal-counterexample conditions

Any counterexample to the Strong Safe-Extension Conjecture

\[
\alpha(D,c)=\beta(D,c)
\]

must now satisfy:

1. at least three connected components of \(\Lambda(D)\);
2. every beta-optimal old-obstruction-killing extension contains a positive defect hyperedge from \(\mathcal R_{\le\beta}(D)\);
3. in the special `beta=1` case,
   \[
   W_{\rm kill}(D,c)\subseteq R_1(D);
   \]
4. the resulting replacement symmetry must also be non-global with respect to the extended binary coloring; domain deletion ambiguity alone is not enough.

This is substantially narrower than the original `symmetry creation under extension` formulation.

---

## 11. Computational observation

Targeted `n=6, |D|=8` searches already exhibit individual beta-killing cells that are unsafe for **both** binary color choices: adding such a cell can complete a one-cell domain symmetry and create the same new bad carrier permutation under both colors.

However, in the inspected layers other beta-killing cells lie outside the dangerous replacement completion and give exact one-cell extensions. Thus unsafe witnesses exist, but no replacement-saturated layer with `beta=1<alpha` has yet been found.

This distinction is important:

\[
\boxed{
\text{“some beta witness is unsafe”}
\not\Rightarrow
\text{positive surcharge}.
}
\]

A genuine counterexample requires **all** beta-optimal witnesses to be trapped by the replacement hypergraph.

---

## 12. Next target

The next theorem target is now purely combinatorial at level `beta=1`:

> Can a nonexact sparse binary layer with at least three incidence components satisfy
> \[
> W_{\rm kill}(D,c)\subseteq R_1(D)?
> \]
> and have every such completion produce a bad extended symmetry?

If the answer is no, then

\[
\boxed{\beta=1\Longrightarrow\alpha=1}
\]

in full generality.

Only after resolving this one-cell saturation problem is it efficient to attack replacement hypergraphs at `beta>=2`.

---

## Claim firewall

1. `R_1(D)` and `R_{<=k}(D)` are pure domain-replacement objects; membership does not by itself imply a bad colored automorphism.
2. Avoiding the replacement hypergraph is sufficient for a beta-optimal extension to be exact, not claimed necessary in the colored setting.
3. The two-component theorem is general and theorem-level.
4. No exhaustive `n=6, |D|=8` theorem is claimed here.
5. Articles A and B remain frozen publications.
