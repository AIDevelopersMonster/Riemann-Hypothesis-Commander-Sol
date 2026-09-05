# FCOA QGE3 — Ternary Failures for q >= 3

**Branch:** `director/fcoa-rigidity-cost`  
**Status:** theorem/counterexample note; hostile-audit repairs applied  
**Model:** `\mathcal T(D,c)=(G;D,Q_D)` from `MODEL_DEFINITIONS.md`

## 1. The naive componentwise S_q-phase statement is false

A tempting multicolor analogue of the binary theorem would be:

> If a comparison component `C` of `Lambda(D)` is connected, every `g in Aut(G;D,Q_D)` induces one permutation of the colors visible on `C`.

This is false already for `q=3` on three carrier points.

---

## 2. Smallest sparse connected counterexample

Let

\[
G=\{0,1,2\},
\]

and

\[
D=\{(0,1),(0,2),(1,0),(1,2)\}.
\]

Use three anonymous colors, temporarily denoted `0,1,2`, and set

\[
c(0,1)=0,\qquad c(0,2)=0,
\]

\[
c(1,0)=1,\qquad c(1,2)=2.
\]

The comparison graph `Lambda(D)` is connected. For example,

\[
(0,2)\sim(1,0)\sim(0,1)\sim(1,2),
\]

where adjacency is understood in the undirected composability sense.

Let

\[
g=(0\ 1)\in S_G.
\]

Then `gD=D` and the four cells are permuted as

\[
(0,1)\leftrightarrow(1,0),
\qquad
(0,2)\leftrightarrow(1,2).
\]

### Ternary reduct

There is no composable equal-colored pair in this example, hence

\[
Q_D=\varnothing.
\]

Therefore `g` preserves `(G;D,Q_D)`.

### Failure of a local color permutation

If a local phase `phi` existed on the unique connected component, then from

\[
c(0,1)=0,\qquad c(g(0,1))=c(1,0)=1
\]

we would have

\[
\phi(0)=1.
\]

But from

\[
c(0,2)=0,\qquad c(g(0,2))=c(1,2)=2
\]

we would also have

\[
\phi(0)=2,
\]

a contradiction.

Thus

\[
\boxed{
g\in\operatorname{Aut}(G;D,Q_D)
\quad\text{but no local phase }O_C\to O_C\text{ exists}.}
\]

In fact

\[
\operatorname{Aut}(G;D,Q_D)\cong C_2,
\qquad
\operatorname{Aut}^{\rm an}(D,c)=1.
\]

This is a genuinely sparse obstruction: it occurs on three carrier points, below the five-point complete-domain ternary obstruction recorded in Article A.

---

## 3. Minimality

### Proposition

Among surjective `q=3` sparse layers with connected `Lambda(D)`, the counterexample above has minimum domain size:

\[
\boxed{|D|_{\min}=4.}
\]

### Proof

Surjectivity onto three colors forces

\[
|D|\ge3.
\]

If `|D|=3`, each of the three colors occurs exactly once. Any carrier permutation `g` preserving `D` therefore sends the three cells to the same three cells, and the rule

\[
\pi(c(p)):=c(gp)
\]

is automatically a well-defined permutation of the three colors, because every source color occurs on exactly one cell.

Hence every domain-preserving carrier symmetry is already anonymous-color compatible. No false ternary automorphism can occur at `|D|=3`.

The four-cell construction above therefore proves minimality. \(\square\)

### Exhaustive finite verification

A direct exhaustive search over all off-diagonal domains on `|G|=3`, all surjective three-colorings, and all carrier permutations found no connected counterexample with `|D|<=3` and found the displayed witness at `|D|=4`.

The mathematical minimality proof above does not depend on the computation.

---

## 4. Non-vacuous ternary failure

The minimum example has `Q_D=empty`, so it is useful to separate that extreme sparse phenomenon from failures where ternary equality carries nontrivial information.

On the same three-point complete off-diagonal domain

\[
D=G^2\setminus\Delta,
\]

set

\[
c(0,1)=0,\ c(0,2)=1,\ c(1,0)=1,
\]

\[
c(1,2)=1,\ c(2,0)=0,\ c(2,1)=2.
\]

Let

\[
g=(1\ 2).
\]

Then `gD=D`, `Lambda(D)` is connected, and `Q_D` is nonempty; explicitly it contains equal-color composable comparisons such as

\[
(1,0)\sim(0,2)
\]

and its transported partner. Nevertheless `g` preserves the ternary reduct while no global anonymous permutation realizes `g` on the coloring.

Thus the failure is not confined to the case where `Q_D` is empty.

A small exhaustive search shows that on `|G|=3` no connected non-vacuous failure occurs below six defined cells.

This six-cell minimality is currently computational evidence; only the four-cell overall minimum is promoted here by proof.

---

## 5. Constraint-quotient explanation

Let `C` be a connected component of `Lambda(D)` and let `H_T(C)` be the equality-atom quotient from `MODEL_DEFINITIONS.md`.

Model T remembers exactly:

1. which adjacent cells are forced equal, producing the equality atoms;
2. which distinct atoms are adjacent and therefore forced unequal.

Hence the hidden terminal assignment is a proper coloring

\[
\kappa_C:V(H_T(C))\to O_C.
\]

A ternary-reduct automorphism induces a graph isomorphism

\[
\bar g_C:H_T(C)\to H_T(gC).
\]

A local color phase exists precisely when the transported proper coloring

\[
\kappa_{gC}\circ\bar g_C
\]

is equivalent to `\kappa_C` by a permutation of the visible color names.

Therefore connectedness of `Lambda(D)` is irrelevant to the missing step: the issue is **uniqueness of the proper coloring of the quotient graph up to color permutation**.

The minimum four-cell witness has an especially degenerate quotient: every equality atom is a singleton, and the quotient graph admits enough proper-coloring freedom that two occurrences of source color `0` can be transported to different target colors.

---

## 6. Exact no-go theorem for a universal componentwise S_q phase

### Theorem — Connected-component phase no-go

For every

\[
q\ge3
\]

there exists a finite sparse anonymous `q`-color layer `(D,c)` such that

1. `Lambda(D)` is connected;
2. there is `g in Aut(G;D,Q_D)`;
3. no map

\[
\phi:O_C\to O_{gC}
\]

satisfies

\[
c(gp)=\phi(c(p))\quad\forall p\in C.
\]

In particular, there is no universal theory assigning one `S_q` phase to each connected comparison component of Model T.

### Proof

The explicit `q=3` witness above proves the theorem for three colors.

For `q>3`, start with that witness on `{0,1,2}` and the involution `g=(0 1)`. For every new color

\[
j\in\{3,\dots,q-1\},
\]

add one fresh carrier point `x_j`, fixed by `g`, and add exactly the two cells

\[
(0,x_j),\qquad(1,x_j),
\]

both colored `j`. Extend `g` by fixing every `x_j`.

The two new cells of color `j` are exchanged by `g`, so the extended domain and coloring pattern relevant to Model T are `g`-invariant. They are not composable with each other because they have the same terminal endpoint `x_j`, and color `j` occurs nowhere else. Hence adding color `j` creates no new equal-colored composable pair and therefore no new tuple of `Q_D` involving color `j`.

The new cells do lie in the original comparison component: for example,

\[
(1,0)\sim(0,x_j),
\qquad
(0,1)\sim(1,x_j).
\]

Thus the enlarged `Lambda(D)` remains connected. All `q` colors occur, and `g` still preserves `(G;D,Q_D)`. But the original four-cell subsystem is unchanged, so any putative local phase would still satisfy simultaneously

\[
\phi(0)=1
\quad\text{from }(0,1),
\qquad
\phi(0)=2
\quad\text{from }(0,2),
\]

which is impossible.

Therefore the no-go holds for every `q>=3`. \(\square\)

No optimal carrier-size claim for `q>3` is made here.

---

## 7. Failure taxonomy

The QGE3 line must distinguish four different mechanisms.

### F1. Complete-domain arity obstruction

Already frozen in Article A: for `q>=3`, even maximal anonymous equality data on at most three carrier points can fail to recover the full anonymous layer on a complete domain.

### F2. Sparse vacuity

The smallest present witness has `Q_D=empty`; sparse incidence simply fails to expose equal-valued comparisons.

### F3. Connected proper-coloring ambiguity

Even when `Lambda(D)` is connected and `Q_D` is nonempty, the quotient graph `H_T(C)` may have inequivalent proper colorings. This destroys any universal one-per-component `S_q` phase.

### F4. Disconnected gluing ambiguity

Even if each comparison component individually has a well-defined local visible-support permutation, different components may disagree on common global color names or may see insufficient subsets of `O` to determine a single global permutation. This is treated separately in `GLUING_CRITERION.md`.

---

## 8. Consequence for the research programme

The expected theorem

\[
\text{connected component}\Rightarrow\text{one local }S_q\text{ phase}
\]

is false.

The correct replacement must therefore be formulated in terms of:

\[
\boxed{\text{proper-coloring transport on }H_T(C)}
\]

with an `S_q`-valued phase appearing only under an additional color-rigidity hypothesis on the quotient.
