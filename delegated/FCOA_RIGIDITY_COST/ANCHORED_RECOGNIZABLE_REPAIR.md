# FCOA Rigidity Cost — Anchored-Recognizable Repair Criterion

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** new post-publication theorem plus exhaustive five-carrier evidence.

## 1. Setup

Let `D` be the old sparse binary domain with coloring `c`, and let `(E,b)` be an admissible extension. Put

\[
X=D\cup E.
\]

Call `E` **domain-recognizable relative to D** if every automorphism of the uncolored extended domain preserves the old domain setwise:

\[
\boxed{
\forall h\in\operatorname{Aut}(G;X),\qquad hD=D.
}
\]

Equivalently, the new-cell set `E=X\setminus D` is setwise invariant under the uncolored domain automorphism group.

Call the extension **D-anchored** if every connected component of the ordered-cell incidence graph

\[
\Lambda(X)
\]

contains at least one old cell from `D`.

Finally, call `(E,b)` **beta-valid** if every old bad automorphism is destroyed by the extended ternary reduct.

## 2. Why recognizability alone is not enough

Recognizability forbids genuinely domain-moving new symmetries, but by itself it does not force a surviving old-good anonymous automorphism to use the same phase on a completely new incidence component containing only cells from `E`.

Thus the correct sufficient condition needs the anchoring hypothesis.

## 3. Main theorem

### Theorem 3.1 — Anchored-Recognizable Safe Repair

If `(E,b)` is

1. beta-valid;
2. domain-recognizable relative to `D`;
3. D-anchored;

then the extended ternary reduct is exact:

\[
\boxed{
\operatorname{Aut}(G;X,Q_X)
=
\operatorname{Aut}^{\pm}(X,c\cup b).
}
\]

### Proof

Let

\[
h\in\operatorname{Aut}(G;X,Q_X).
\]

Because every reduct automorphism preserves the defined-cell relation, it belongs to `Aut(G;X)`. Domain recognizability therefore gives

\[
hD=D.
\]

Hence the restriction of `h` to the old layer belongs to

\[
A_Q(D,c).
\]

Because the extension is beta-valid, no old bad automorphism survives. Therefore the restriction of `h` to `D` is old-anonymous: there is one bit

\[
\epsilon\in\mathbf F_2
\]

such that

\[
c(hp)\oplus c(p)=\epsilon
\qquad\forall p\in D.
\]

Now apply the Componentwise Phase Theorem on the enlarged domain `X`. The discrepancy of `h` is constant on each connected component of `Lambda(X)`. By D-anchoring, every such component contains an old cell `p in D`, and on that old cell the discrepancy is `epsilon`. Hence every component of `Lambda(X)` has phase `epsilon`.

Therefore

\[
(c\cup b)(hp)\oplus(c\cup b)(p)=\epsilon
\qquad\forall p\in X,
\]

so `h` is a full anonymous automorphism of the extended colored layer. The reverse inclusion is automatic. `square`

## 4. Immediate consequence for alpha=beta

If a beta-minimal extension can be chosen domain-recognizable and D-anchored, then

\[
\boxed{\alpha(D,c)=\beta(D,c).}
\]

Thus the Safe-Minimizer conjecture follows from the stronger geometric statement:

> every sparse binary layer has at least one beta-minimal extension whose old domain is recognizable and whose new incidence components are all anchored to old cells.

This stronger statement is not yet proved globally.

## 5. One-cell specialization

For `E={e}`, D-anchoring simply means that the new cell `e` is adjacent in `Lambda(D union {e})` to at least one old cell.

Domain recognizability is equivalent to saying that every automorphism of the uncolored domain `D union {e}` fixes the unique new cell `e` setwise, or equivalently preserves `D`.

Hence a one-cell beta-valid repair with these two properties is automatically exact, independently of any further phase analysis.

## 6. Exhaustive five-carrier result

A fresh independent exhaustive verifier was run over the complete five-carrier candidate space used in the post-Article-B audit.

The theorem-level domain filters leave exactly

\[
\boxed{10,095}
\]

potentially nontrivial domains and

\[
\boxed{1,629,945}
\]

normalized surjective binary colorings.

Among these,

\[
\boxed{89,880}
\]

layers are nonexact.

For **every** one of those 89,880 nonexact layers, the verifier found a one-cell extension `e` such that:

1. `e` is adjacent to an old cell, so the extension is D-anchored;
2. every automorphism of the uncolored domain `D union {e}` fixes `e`, so the old domain is recognizable;
3. one of the two binary values on `e` gives an exact extension.

In fact the theorem then explains exactness structurally once beta-validity is verified.

Therefore the stronger geometric safe-minimizer property holds exhaustively on five carrier points.

## 7. Relation to the known unsafe witness

`UNSAFE_BETA_WITNESS.md` shows that some beta-minimal cells are not recognizable: their addition makes an old and a new cell structurally exchangeable and creates domain-moving bad symmetries.

The same old layer nevertheless has alternative one-cell beta-minimizers that are recognizable and anchored. The theorem above explains why those alternatives are automatically safe.

Thus the correct phenomenon is not “all beta-minimizers are safe” but rather:

\[
\boxed{
\text{unsafe minimizers coexist with geometrically recognizable safe minimizers.}
}
\]

## 8. Next proof target

The global Safe-Minimizer problem has now been reduced further. A sufficient route to

\[
\alpha=\beta
\]

is to prove an **Anchored Recognizable Minimizer Theorem**:

> among all beta-minimal extensions, one can choose `(E,b)` such that `E` is D-anchored and `D` is setwise invariant under `Aut(G;D union E)`.

If this stronger theorem is false, the affine-rank machinery in `AFFINE_RANK_GEOMETRY.md` remains available for beta-minimal geometries with residual positive-rank domain-moving symmetries.

Thus the proof programme naturally splits:

\[
\boxed{
\text{recognizable/anchored geometry if possible}
\quad\text{else}\quad
\text{positive-rank affine avoidance}.
}
\]

## 9. Claim firewall

1. Domain recognizability alone is not claimed sufficient; D-anchoring is also required.
2. The global existence of an anchored-recognizable beta-minimizer remains open.
3. The five-carrier statement is exhaustive computational evidence plus theorem-level verification of the sufficient criterion.
4. Articles A and B remain frozen publications.
