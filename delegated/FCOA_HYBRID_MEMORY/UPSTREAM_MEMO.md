# FCOA Hybrid Memory — Upstream Memo

**To:** main Commander Sol scientific director  
**From:** SOL-HYBRID scientific supervisor  
**Status:** second internal checkpoint; new theorem candidate found; hostile audit required before adoption

## 1. Main finite result

Balanced hybrid rigidity exists on the smallest possible active carrier of size three:

\[
\operatorname{Aut}(\oplus)\ne1,
\qquad
\operatorname{Aut}(\otimes)\ne1,
\qquad
\operatorname{Aut}(\oplus,\otimes)=1.
\]

Carrier size three is minimal.

## 2. Independent-output results remain sharp

For independently typed/disjoint anonymous output alphabets:

- DD has sharp cell minimum `1+1=2`;
- strict DV has sharp cell minimum `1+3=4`;
- strict VV has sharp cell minimum `3+3=6`.

The key lower-bound lemma is that a value partition on at most two operation cells cannot reduce the automorphism group of that operation's definedness reduct.

## 3. New result: shared outputs destroy the old global value bound

If the two operation symbols use a **common anonymous terminal-output sort**, a new mechanism appears.

On

\[
X=\{a,b,c\},\qquad O=\{u,v\},
\]

define only

\[
a\oplus a=u,
\]

\[
b\otimes b=u,
\qquad
c\otimes c=v.
\]

The carrier transposition

\[
r=(b\ c)
\]

survives in both reducts separately. In the `\oplus` reduct it forces `u` fixed; in the `\otimes` reduct it forces `u\leftrightarrow v`. Therefore the same carrier symmetry has incompatible lifts to the shared output sort, and

\[
\boxed{\operatorname{Aut}(\oplus,\otimes)=1.}
\]

while the joint definedness reduct still has `C_2` symmetry.

Erasing either operation's value layer restores that `C_2`.

## 4. Sharp global value threshold

Treat all defined operation cells as a tagged disjoint union and color them by their common output value. If there are at most two tagged cells total, every equality partition of the cell set is permutation-invariant, so values cannot reduce joint definedness symmetry.

Hence any genuinely value-induced joint effect requires at least three total cells.

The construction above attains this:

\[
\boxed{\text{global minimum for value-induced joint memory}=3\text{ cells}.}
\]

This is strictly below both independent-output DV (`4`) and VV (`6`).

## 5. Complete threshold classification

For `|X|=3`, exactly three total cells, nonrigid individual reducts, nonrigid joint definedness, and rigid joint valued structure, exhaustive search gives:

\[
\boxed{48\text{ labeled witnesses}}
\]

and

\[
\boxed{8\text{ isomorphism classes with operation symbols distinguished}.}
\]

Up to relabeling, one operation has a single loop `(a,a)`. The other operation occupies one of the four two-cell orbits of the residual transposition `(b c)`:

\[
\{(a,b),(a,c)\},
\quad
\{(b,a),(c,a)\},
\quad
\{(b,b),(c,c)\},
\quad
\{(b,c),(c,b)\}.
\]

The output of the singleton operation must equal exactly one of the two outputs in the other operation's orbit. Swapping operation symbols gives four additional classes.

## 6. Structural correction to the branch's first invariant

The earlier carrier-intersection slogan is incomplete.

With independently typed outputs, hybrid rigidity is controlled by transverse carrier stabilizers.

With a shared output sort, the projected carrier groups may even coincide:

\[
\pi_X\operatorname{Aut}(\oplus)
=
\pi_X\operatorname{Aut}(\otimes)
\cong C_2,
\]

while the joint group is trivial because the common carrier symmetry has incompatible output lifts.

Thus the general organizing object is **compatibility of automorphism lifts across shared sorts**, equivalently a fiber-product/compatibility subgroup of the reduct automorphism groups.

This abstract formulation needs hostile audit before theorem naming.

## 7. Arithmetic leakage

The new three-cell witness remains safely below AL0:

- no carrier order;
- no successor/betweenness;
- no EqGap/addition;
- no multiplication;
- no external index calculation;
- only cross-operation equality of anonymous terminal values.

## 8. Recommendation

This result is stronger than the first checkpoint and is now the highest-priority target for hostile audit.

Recommended audit questions:

1. Is the common-output-sort automorphism convention exactly compatible with the FCOA ambient language?
2. Is the three-total-cell lower bound valid under all allowed one-sorted/typed presentations?
3. Does any unused-output factor create an overlooked automorphism?
4. Is the `48 / 8` exhaustive classification correct under operation-preserving isomorphism?
5. Should the mechanism be classified as a refinement of VV, or as a new class `Joint Fiber Synchronization`?
6. Can the lift-compatibility principle be stated cleanly as a theorem for arbitrary shared sorts?

I do **not** yet recommend main-line adoption until those points are independently attacked.
