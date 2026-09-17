# PROJECTIVE_PASCH_LOCALIZATION_AND_CARRIER_GAP

**Branch:** `research/alice-ruler-edit-rigidity`  
**Status:** closed local-defect localization + strengthened carrier obstruction, 2026-09-13  
**Depends on:** `PROJECTIVE_ASSOCIATOR_BRIDGE.md`, `PROJECTIVE_WRONG_ORDER_OBSTRUCTION.md`, `ROBUST_BOOLEAN_RECOVERY_FROM_GROUP_DISTANCE.md`

---

## 1. Purpose

After the wrong-order obstruction, the projective problem was reformulated as a possible carrier-adjusted reconstruction problem. This note does two things.

1. It identifies the associator defect of a Steiner loop **exactly and locally** with the Pasch deficit of the corresponding STS block, and equivalently with the classical four-block configuration `C14`.
2. It shows that the first carrier-adjusted formulation was still too strong: even allowing an injective map into a group on `n+o(n)` points does not rescue a vanishing-error reconstruction theorem for the explicit Add-4 sequence.

The correct remaining target must therefore allow **deleting an exceptional `o(n)` set / recovering a large projective core**, rather than requiring all original points to embed into a group whose order is `(1+o(1))n`.

---

## 2. Translation defect is a block weight

Let `S=(X,B)` be an `STS(v)` and `L=X\sqcup\{0\}` its Steiner loop, of order

```math
n=v+1.
```

For `x\in L`, write

```math
T_x(z)=x\circ z.
```

For a pair `x,y\in X`, define

```math
r_{xy}
:=
|\{z\in L:(x\circ y)\circ z\ne x\circ(y\circ z)\}|
=
d_H(T_{x\circ y},T_xT_y).
\tag{2.1}
```

If `x=y` then `r_{xx}=0`; below take `x\ne y` and put

```math
a=x\circ y,
\qquad
B=\{x,y,a\}.
```

### Lemma 2.1 (block invariance)

For the three unordered pairs of `B`,

```math
\boxed{r_{xy}=r_{xa}=r_{ya}.}
\tag{2.2}
```

The same value occurs for both orientations of every pair, so all six ordered pairs supported by `B` have the same defect.

### Proof

All Steiner translations are involutions. Hamming distance on permutations is invariant under left and right composition. Hence

```math
r_{xy}
=d_H(T_a,T_xT_y)
=d_H(T_xT_a,T_y)
=d_H(T_y,T_xT_a)
=r_{xa}.
```

The remaining equality follows symmetrically. Orientation invariance follows either by the same calculation or from the Pasch interpretation proved below. `\square`

Thus there is a well-defined nonnegative integer **block defect**

```math
d(B):=r_{xy}
```

for any pair `{x,y}\subset B`.

---

## 3. Exact local Pasch-deficit formula

Let `p(B)` be the number of Pasch configurations of `S` containing the block `B`.

### Theorem 3.1 (local Pasch localization)

For every block `B` of `S`,

```math
\boxed{d(B)=(v-3)-p(B).}
\tag{3.1}
```

Equivalently, for every ordered pair of distinct points `x,y` with block `B=\{x,y,x\circ y\}`,

```math
\boxed{r_{xy}=(v-3)-p(B).}
\tag{3.2}
```

### Proof

Fix `B={x,y,a}` with `a=x\circ y`.

Associativity is automatic for

```math
z\in\{0,x,y,a\}.
```

There remain exactly `v-3` possible points

```math
z\in X\setminus B.
```

For such a `z`, put

```math
b=y\circ z,
\qquad
t=a\circ z.
```

Then associativity at `(x,y,z)` is precisely

```math
(x\circ y)\circ z=x\circ(y\circ z),
```

that is,

```math
t=x\circ b.
\tag{3.3}
```

When (3.3) holds, the four blocks

```text
{x,y,a},
{y,z,b},
{a,z,t},
{x,b,t}
```

form a Pasch configuration containing `B`.

Conversely, fix a Pasch containing `B`. Once the ordered pair `(x,y)` in `B` is fixed, exactly one of the three points outside `B` occupies the role `z` in the displayed Pasch form; for that point (3.3) holds. Hence the successful external `z` are in bijection with the Pasches through `B`.

Therefore exactly `p(B)` of the `v-3` external choices associate, and the other `(v-3)-p(B)` fail. This proves (3.1)--(3.2). `\square`

### Corollary 3.2

A block has zero associator defect iff it is contained in the maximum possible number `v-3` of Pasch configurations.

Thus the global almost-associativity problem has a concrete local interpretation:

> almost all translation identities hold exactly when the total deficit from the maximal Pasch incidence profile is small.

---

## 4. Global sum rule

Let `P(S)` denote the total number of Pasch configurations. Every Pasch contains four blocks, so

```math
\sum_{B\in\mathcal B}p(B)=4P(S).
\tag{4.1}
```

There are

```math
b(v)=v(v-1)/6
```

blocks. Since every block supports six ordered pairs and all six have defect `d(B)`, the total number `s` of nonassociative ordered triples satisfies

```math
s=6\sum_{B\in\mathcal B}d(B).
\tag{4.2}
```

Using Theorem 3.1 and (4.1),

```math
\boxed{
s
=6\left[b(v)(v-3)-4P(S)\right]
=v(v-1)(v-3)-24P(S).
}
\tag{4.3}
```

Equivalently, with

```math
M(v)=\frac{v(v-1)(v-3)}{24},
```

```math
\boxed{s=24(M(v)-P(S)).}
\tag{4.4}
```

This recovers the known global Steiner-loop/Pasch formula, but now as a sum of exact **blockwise** identities rather than only a global count.

---

## 5. `C14` is exactly the associator-failure configuration

Use the standard seven-point four-block configuration

```text
{xi,alpha1,alpha2},
{xi,beta1,beta2},
{alpha1,beta1,gamma1},
{alpha2,beta2,gamma2},
```

with all seven points distinct and `gamma1 != gamma2`. This is the classical configuration `C14`; when the two last completion points coincide one gets the Pasch configuration `C16` instead.

### Proposition 5.1

There is a natural `4`-to-`1` map from failed ordered associativity triples to occurrences of `C14`. Consequently

```math
\boxed{s=4c_{14}.}
\tag{5.1}
```

### Proof

Take a failed ordered independent triple `(x,y,z)` and write

```math
a=x\circ y,
\qquad b=y\circ z,
\qquad u=a\circ z,
\qquad v=x\circ b.
```

Failure means `u!=v`. Cancellation in the Steiner loop shows that

```math
x,y,z,a,b,u,v
```

are seven distinct points. The four blocks

```text
{y,x,a},
{y,b,z},
{x,b,v},
{a,z,u}
```

are therefore an occurrence of `C14`, with central point `xi=y`.

Conversely, from an occurrence of `C14`, the two blocks not containing either degree-one point meet in a uniquely determined central point `xi`. The configuration then forces exactly the four ordered failures

```text
(alpha1,xi,beta2),
(beta2,xi,alpha1),
(alpha2,xi,beta1),
(beta1,xi,alpha2).
```

Indeed the two bracketings complete to `gamma1` and `gamma2`, which are distinct. These four ordered triples recover the same `C14`, and no other ordered associator failure maps to that occurrence. Thus every `C14` has exactly four preimages. `\square`

The classical four-line count

```math
c_{14}=\frac{v(v-1)(v-3)}4-6P(S)
=6(M(v)-P(S))
```

is therefore equivalent to (4.4).

### Consequence 5.2

The projective associativity-defect problem can be restated exactly as a **`C14`-defect problem inside an STS**:

```math
\delta_{assoc}=o(1)
\quad\Longleftrightarrow\quad
c_{14}=o(v^3).
```

This is more specific than a generic almost-associative Latin-square problem.

---

## 6. A rigorous regularized-core lemma

For `x\in L`, define the row associator load

```math
A_x
:=
|\{(y,z)\in L^2:(x\circ y)\circ z\ne x\circ(y\circ z)\}|.
```

Then

```math
\sum_{x\in L}A_x=s.
\tag{6.1}
```

Put

```math
\delta=s/n^3.
```

### Lemma 6.1

For every `eta>0`, the set

```math
R_eta=\{x:A_x>eta n^2\}
```

satisfies

```math
\boxed{|R_eta|<\frac{\delta}{\eta}n.}
\tag{6.2}
```

In particular, taking `eta=sqrt(delta)`, after deleting at most

```math
\boxed{\sqrt\delta\,n}
```

points, every remaining point participates as first coordinate in at most

```math
\boxed{\sqrt\delta\,n^2}
```

associator failures.

### Proof

Immediate from (6.1) and Markov's inequality:

```math
|R_eta|eta n^2 < s=delta n^3.
```

`\square`

This is only a regularization statement, not yet a projective-core theorem. Sparse defects can in principle remain distributed over every row of the core.

---

## 7. Near-carrier injection theorem: a second obstruction

The wrong-order note disproved reconstruction by a group law on the identical carrier. One might try to repair it as follows:

> inject all `n` loop elements into a group `G` of order `m=n+o(n)` and require the product law to agree on `1-o(1)` of the pairs.

Even this is false for the Add-4 sequence.

Let `phi:L->G` be injective and define the product error

```math
t_phi
:=
|\{(x,y)\in L^2:
phi(x\circ y)\ne phi(x)phi(y)\}|.
\tag{7.1}
```

For each `x`, let

```math
r_x
:=
|\{y:phi(x\circ y)\ne phi(x)phi(y)\}|,
```

so `sum_x r_x=t_phi`.

### Lemma 7.1 (many injected points are involutions)

The ambient group `G` contains at least

```math
\boxed{n-\frac{2t_phi}{n}}
\tag{7.2}
```

involutions (identity included).

### Proof

If `r_x<n/2`, then there is a `y` for which both pairs

```math
(x,y)
```

and

```math
(x,x\circ y)
```

are good: each bad set has size `r_x`, and `y->x\circ y` is a permutation.

For such `y`, using the Steiner identity `x\circ(x\circ y)=y`,

```math
phi(x\circ y)=phi(x)phi(y),
```

and

```math
phi(y)
=phi(x\circ(x\circ y))
=phi(x)phi(x\circ y)
=phi(x)^2phi(y).
```

Hence `phi(x)^2=e_G`.

There are at most `2t_phi/n` elements `x` with `r_x>=n/2`. Since `phi` is injective, the remaining images are distinct involutions of `G`. `\square`

Recall the elementary group lemma proved in `ROBUST_BOOLEAN_RECOVERY_FROM_GROUP_DISTANCE.md`:

> a finite group of order `m` with more than `3m/4` involutions is elementary abelian `2`.

### Theorem 7.2 (quantitative near-carrier dichotomy)

Let

```math
lambda=m/n.
```

If `G` is not elementary abelian `2`, then every injective approximate homomorphism `phi:L->G` satisfies

```math
\boxed{
\frac{t_phi}{n^2}
\ge
\frac12-\frac{3lambda}{8}.
}
\tag{7.3}
```

whenever the right-hand side is positive.

### Proof

If `G` is non-Boolean, it has at most `3m/4` involutions. Combine this with Lemma 7.1:

```math
n-2t_phi/n
\le3m/4.
```

Rearranging gives (7.3). `\square`

In particular, if

```math
m=(1+o(1))n,
```

then every non-Boolean ambient group has

```math
\boxed{t_phi/n^2\ge1/8-o(1).}
\tag{7.4}
```

So vanishing pair error forces the ambient group itself to be Boolean.

---

## 8. Add-4 kills `(1+o(1))` carrier enlargement

Take the explicit wrong-order Add-4 sequence from `PROJECTIVE_WRONG_ORDER_OBSTRUCTION.md`.

Its Steiner loops have order

```math
n_k=2^{2k}+4.
\tag{8.1}
```

They satisfy

```math
s_k/n_k^3\to0
```

and therefore `rho_P->1`.

Suppose there existed groups `G_k` and injections

```math
phi_k:L_k->G_k
```

such that

```math
|G_k|/n_k->1
```

and

```math
t_{phi_k}/n_k^2->0.
```

By (7.4), `G_k` is eventually elementary abelian `2`, so `|G_k|` is a power of `2`.

But the smallest power of `2` at least `n_k=2^{2k}+4` is

```math
2^{2k+1}.
```

Therefore every Boolean group large enough to contain `L_k` injectively has

```math
\frac{|G_k|}{n_k}
\ge
\frac{2^{2k+1}}{2^{2k}+4}
=2-\frac{8}{n_k}
\to2,
```

contradicting `|G_k|/n_k->1`.

### Theorem 8.1 (near-carrier obstruction)

There exists an explicit infinite sequence of Steiner loops with

```math
s/n^3->0
```

(and `rho_P->1`) for which there is **no** sequence of groups `G` satisfying simultaneously

```math
|G|=(1+o(1))n,
```

an injection `L->G`, and

```math
phi(x\circ y)=phi(x)phi(y)
```

on `1-o(1)` of all pairs.

Thus the first carrier-adjusted target is false as stated.

---

## 9. What the obstruction does *not* kill

The Add-4 construction does **not** obstruct a vertex-deletion/projective-core theorem.

Indeed its order is four points larger than the projective source order. This motivates the genuinely compatible target:

> if `s/n^3=o(1)` (or on the P-dominant branch `1-rho_P=o(1)`), can one delete `o(n)` exceptional points and obtain a set of `n-o(n)` points whose induced/retained multiplication or block structure agrees on `1-o(1)` of pairs with a Boolean group / projective STS of a nearby **smaller** projective order?

The exact formulation must distinguish two notions:

1. **partial-core agreement:** after deleting points, compare only products/pairs that remain inside the core;
2. **subsystem reconstruction:** require the retained points themselves to form (after `o(n^2)` block repairs) a projective STS.

The first is weaker and should be attacked first.

This target is recorded as open, not as a theorem.

---

## 10. Literature audit and warning about the Levi phrase

Gowers--Long (GAFA 2020) state in their introduction that Elad Levi proved the `99%` case: for `c` close to `1`, there is a group `G` of size “approximately equal” to `|X|` and an injection preserving almost all products. Their cited source is an M.A. thesis/private communication, and the introduction does not quantify “approximately equal” in the statement quoted there.

Theorem 8.1 proves that, for Steiner loops, that phrase **cannot be imported as the stronger asymptotic assertion**

```math
|G|=(1+o(1))|X|
```

together with `o(n^2)` product error along every sequence with associativity density tending to `1`.

This is not a contradiction with the published Gowers--Long text; it is a warning that the informal phrase must not be strengthened without the unavailable quantitative statement/proof.

Likewise, ordinary dense hypergraph removal lemmas do not directly solve the present problem: an STS has only `Theta(v^2)` blocks inside the `Theta(v^3)` possible triples, so a theorem normalized to the complete 3-uniform host has the wrong sparsity scale. Any removal input must be checked in an STS-relative/linear-host normalization and must preserve or repair the pair-completion property.

---

## 11. Corrected next target

The projective branch is now reduced to a more faithful structural question.

### PROJECTIVE CORE STABILITY (open)

Given a sequence of `STS(v)` with

```math
1-rho_P=o(1),
```

does there exist a set `R` of exceptional points with

```math
|R|=o(v)
```

and a projective order `q-1` with

```math
q=2^m,
\qquad
q=v+1-o(v),
```

such that after deleting `R` and changing `o(v^2)` pair completions/blocks, the retained structure agrees with `PG(m-1,2)`?

The Add-4 sequence is compatible with this formulation (`|R|=4` at the carrier level), whereas both same-carrier and `(1+o(1))` supercarrier injection formulations are not.

The next proof attack should therefore use the exact defect geometry established here:

```math
associator failures
<-> block Pasch deficits
<-> C14 occurrences,
```

and ask whether `o(v^3)` total `C14` defect forces all but `o(v)` points into a projective core after `o(v^2)` repairs.

---

## 12. References

1. W. T. Gowers, J. Long, *Partial associativity and rough approximate groups*, Geom. Funct. Anal. 30 (2020), 1583--1647, DOI `10.1007/s00039-020-00553-1`.
2. A. R. Kozlik, *The centre of a Steiner loop and the maxi-Pasch problem*, Comment. Math. Univ. Carolin. 61 (2020), 535--545, DOI `10.14712/1213-7243.2020.035`.
3. M. J. Grannell, T. S. Griggs, C. A. Whitehead, *The resolution of the anti-Pasch conjecture*, J. Combin. Des. 8 (2000), and standard four-line configuration enumerations; in particular `C14`/Pasch (`C16`) terminology.
4. M. J. Grannell, G. J. Lovegrove, *Maximizing the number of Pasch configurations in a Steiner triple system*, Bull. Inst. Combin. Appl. 69 (2013), 23--35.
