# Commander Sol Hostile Audit — QGE3

**Date:** 29 August 2026  
**Branch:** `director/fcoa-rigidity-cost`  
**Scope:** sparse anonymous terminal alphabets `q>=3`  
**Decision:** **ACCEPT WITH TWO LOCAL REPAIRS — UPSTREAM THEOREM PACKAGE APPROVED**

## 1. Audit verdict

The central QGE3 result survives hostile audit.

The mathematically strong statement is not merely that `S_q` is nonabelian. The real obstruction occurs earlier: Model T remembers only adjacent-cell equality/inequality, so after contraction of equality edges it remembers a constraint graph but not necessarily its original color partition. For `q>=3`, a connected constraint graph may admit inequivalent proper colorings. Hence a ternary-reduct automorphism need not induce any color map on a connected comparison component.

The replacement architecture is correct:

`Model T -> T-equality atoms -> H_T(C) -> proper-coloring transport -> phase-admissible sector -> visible-support groupoid -> global gluing`.

The package is suitable for inclusion in the main Rigidity Theory and for a focused companion paper after the repairs below.

## 2. Sharp q=3 witness — PASS

For

`G={0,1,2}`,

`D={(0,1),(0,2),(1,0),(1,2)}`,

with colors

`c(0,1)=c(0,2)=0`, `c(1,0)=1`, `c(1,2)=2`,

the comparison graph is connected and `Q_D` is empty. The involution `g=(0 1)` preserves `D` and Model T but sends the two occurrences of source color `0` to colors `1` and `2`. Therefore no local color function exists.

The domain-size minimality proof is valid: surjective `q=3` with `|D|=3` uses each color exactly once, so every domain-preserving carrier permutation automatically induces a color permutation. Thus the overall connected minimum is exactly `|D|=4`.

Status: **theorem accepted**.

## 3. Non-vacuous six-cell witness — PASS AS WITNESS; MINIMALITY REMAINS COMPUTATIONAL

The complete off-diagonal three-point example in `TERNARY_FAILURES.md` has nonempty `Q_D`; direct audit confirms that `g=(1 2)` preserves the ternary relation while failing anonymous color compatibility.

The statement that no connected non-vacuous failure occurs below six cells is currently supported by the exhaustive verifier, not by an independent mathematical proof. The existing claim firewall correctly says so.

Status: **witness accepted; six-cell minimality not promoted to theorem**.

## 4. Proper-coloring transport theorem — PASS

Preservation of `D` gives an automorphism of `Lambda(D)`. Preservation of `Q_D`, together with known composability from `D`, preserves both equality and inequality comparison edges. Therefore T-equality atoms are transported to T-equality atoms and `g` induces

`bar g_C : H_T(C) -> H_T(gC)`.

The pulled-back target coloring is a proper coloring of `H_T(C)`. A local visible-support bijection exists exactly when the source and transported fiber partitions coincide, equivalently when the two colorings lie in the same color-relabeling orbit.

Status: **Theorems 2.1 and 6.1 accepted**.

## 5. Color-rigidity theorem — PASS

The relative notion used in QGE3 is stronger/more tailored than standard unique chromatic coloring when the actual number of visible colors is not `chi(H_T(C))`. Under the stated equal-support-cardinality hypothesis, color-rigidity forces the transported coloring into the same relabeling orbit. Surjectivity onto the visible support makes the induced label bijection unique.

Status: **accepted with terminology boundary preserved**.

## 6. Nonabelian phase law — PASS

Where local phases exist,

`phi_{gh,C}=phi_{g,hC} o phi_{h,C}`

follows directly by applying the two maps successively to every cell in `C` and using uniqueness on the visible support.

The groupoid formulation is the correct intrinsic one for partial supports. Full `S_q` coefficients are justified only when every relevant support is the whole alphabet.

Status: **accepted**.

## 7. Exact gluing theorem — PASS

The union relation

`R_g = union_C graph(phi_{g,C})`

is the graph of a global anonymous permutation iff it is single-valued and injective. Global surjectivity of `c` makes its first projection all of `O`; finiteness then turns a total injective self-map into a bijection.

The separation into source disagreement and target collision is exact. The pair-cover corollary is also valid.

Status: **Theorems 3.1 and 9.1 accepted**.

## 8. Cost theory — PASS WITH ONE WORDING REPAIR

The bound

`0 <= lambda_q^ph(D,c) <= (q-1)(r-1)`

is correct in the full-support phase sector: on every edge of a spanning tree, equality on `q-1` point images forces equality of the two permutations.

For worst-case capacity,

`r-1 <= L_q(r) <= (q-1)(r-1)`

is also correct. However the lower-bound explanation in `COST_THEORY.md` says that a disconnected block may be **right-composed** by an independent permutation while preserving its point-image equality constraints. The safe invariant operation is **left composition** by the same permutation on all phases in that disconnected block:

`pi_i -> sigma o pi_i`.

This preserves every equality `pi_i(a)=pi_j(a)` internal to the block. Right composition changes the source argument and need not preserve an arbitrary selected family of point-image constraints.

**Required repair 1:** replace “right-composed” by “left-composed” and write the one-line verification.

The theorem itself is unaffected.

## 9. q>3 extension of the no-go — CORRECT IDEA, PROOF MUST BE MADE EXPLICIT

The current proof says to add colors on cells fixed setwise by the involution and connect them without destroying the contradiction. This is plausible but too existence-level for an upstream theorem advertised for every `q>=3`.

Use the following explicit extension.

Start from the q=3 witness on carrier `{0,1,2}` with `g=(0 1)`. For every new color `j=3,...,q-1`, add a fresh carrier point `x_j`, fixed by `g`, and add the two cells

`(0,x_j)` and `(1,x_j)`,

both colored `j`.

Extend `g` by fixing every `x_j`. Each new two-cell set is a g-orbit. It creates no new equal-colored composable pair: the two cells have the same terminal endpoint `x_j` and are not composable with each other, and color `j` occurs nowhere else. Hence no new `Q_D` tuple is introduced by color `j`. The new cells are nevertheless attached to the old comparison component because, for example,

`(1,0) ~ (0,x_j)` and `(0,1) ~ (1,x_j)`.

Thus `Lambda(D)` remains connected, `g` preserves Model T, all `q` colors occur, and the original contradiction remains:

`phi(0)=1` from `(0,1)` but `phi(0)=2` from `(0,2)`.

**Required repair 2:** replace the current informal q>3 extension paragraph by this explicit construction.

After this repair the theorem for every `q>=3` is fully accepted.

## 10. Literature/priority audit

The package correctly avoids broad priority claims. Unique colorability is classical (Harary–Hedetniemi–Robinson, 1969; Bollobas, 1978 and later work). Permutation voltage assignments and nonabelian/switching structures are also classical. Therefore the publishable novelty claim must remain model-specific.

Safe contribution:

`sparse ternary anonymous equality -> canonical equality-atom quotient -> proper-coloring transport obstruction -> sharp sparse local-phase no-go -> conditional visible-support groupoid -> exact global gluing criterion`.

Do not claim discovery of unique colorability, nonabelian switching, groupoids, or permutation-valued transport as such.

## 11. Upstream decision

Approved for the main Rigidity Theory as a theorem package, not as a modification of frozen Articles A or B.

Recommended upstream theorem block:

### Multicolor Sparse Ternary Transport Theorem

For anonymous `q>=3` sparse terminal layers, connectedness of the ordered-cell comparison graph does not force a componentwise color permutation. The universal local invariant of Model T is the proper-coloring state of the T-constraint quotient. A local phase exists exactly when the transported fiber partition is preserved; where phases exist they form a visible-support groupoid satisfying the crossed composition law; global anonymous compatibility is exactly the permutation-graph gluing condition.

The q=3 four-cell construction is the sharp minimum-domain witness, and the explicit extension above gives the no-go for every `q>=3`.

## 12. Publication decision

**Separate QGE3 article: approved for drafting.**

The article should lead with the sharp four-cell no-go, explain why the obstruction is proper-coloring ambiguity rather than noncommutativity, prove the transport/groupoid/gluing theorems, and end with the safe full-support cost theory and the open extremal problem `L_q(r)`.

The real-cell multicolor extension cost must remain open; no `alpha_q` should be invented in this version.

## Final status

**QGE3 ACCEPTED WITH TWO LOCAL REPAIRS.**  
**UPSTREAM INCLUSION APPROVED.**  
**ARTICLE DRAFTING APPROVED.**
