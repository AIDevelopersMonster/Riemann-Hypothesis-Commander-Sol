# PROJECTIVE_PARTIAL_CORE_METRIC_AND_ADD4_AUDIT

**Branch:** `research/alice-ruler-edit-rigidity`  
**Status:** closed metric/formulation step + exact Add-4 core audit, 2026-09-13  
**Depends on:** `PROJECTIVE_WRONG_ORDER_OBSTRUCTION.md`, `PROJECTIVE_PASCH_LOCALIZATION_AND_CARRIER_GAP.md`

---

## 1. Why the previous `large projective subsystem` wording is still too strong

The previous note correctly showed that neither of the following can be the uniform stability target:

1. approximation by a Boolean group on the identical carrier;
2. injective approximation of **all** points inside a Boolean/group carrier of size `(1+o(1))n`.

It then suggested deleting `o(n)` exceptional points and recovering a large projective core. One further distinction is essential.

A projective Steiner triple system has order

```math
2^m-1.
```

Therefore requiring the retained set itself to be an exact projective subsystem of order `v-o(v)` is generally too rigid. If `v+1=2^m`, the next smaller projective loop order is `2^{m-1}`, a loss of order `v/2`, not `o(v)`.

Even a local perturbation of a projective STS may destroy the exact full projective subsystem while remaining only `O(v)` block edits away from the original projective model.

Thus the first robust target must be **partial-core agreement with a full projective model**, not necessarily an exact projective subsystem on the retained points.

---

## 2. Partial-core comparison between different orders

Let

```math
S=(X,\mathcal B_S),
\qquad |X|=v,
```

be an arbitrary Steiner triple system, and let

```math
P=(Y,\mathcal B_P),
\qquad |Y|=q-1,
\qquad q=2^m,
```

be a projective Steiner triple system.

For distinct points of an STS write

```math
x\oplus_S y
```

for the third point of their block, and similarly `u\oplus_P v` in `P`.

Choose a subset

```math
U\subseteq X
```

and an injection

```math
\phi:U\hookrightarrow Y.
```

We compare pair completions on all unordered pairs inside `U`. A pair `{x,y}\subset U` is called **bad** if either

```math
x\oplus_S y\notin U,
```

or

```math
\phi(x\oplus_S y)
\ne
\phi(x)\oplus_P\phi(y).
```

Let

```math
E_S^P(U,\phi)
```

be the number of bad unordered pairs.

The first alternative deliberately counts products that leave the retained core as errors; deleting points is therefore not a way to hide an arbitrarily large multiplication boundary.

Put

```math
N_*:=\max\{|X|,|Y|\}.
```

### Definition 2.1 (partial-core projective cost)

Define

```math
\boxed{
D_{pc}(S;P,U,\phi)
:=
\frac{|X\setminus U|+|Y\setminus\phi(U)|}{N_*}
+
\frac{2E_S^P(U,\phi)}{N_*(N_*-1)}.
}
\tag{2.1}
```

Then define

```math
D_{pc}(S,P)
:=
\inf_{U,\phi}D_{pc}(S;P,U,\phi),
\tag{2.2}
```

and distance to the projective family by

```math
D_{pc}(S,\mathcal P)
:=
\inf_{P\ \text{projective}}D_{pc}(S,P).
\tag{2.3}
```

We call this a **cost**, not yet a metric: no triangle inequality is asserted or needed. Its purpose is to encode exactly the notion required by the obstruction analysis.

The two summands have distinct meanings:

- the first penalizes deleted points of `S` and unused points of the comparison projective model;
- the second penalizes pair-completion disagreement on the retained core, including products leaving the core.

Hence

```math
D_{pc}(S,\mathcal P)=o(1)
```

means precisely that there is a projective model of asymptotically the same size, a common core occupying `1-o(1)` of both point sets, and only `o(v^2)` bad pair completions on that core.

---

## 3. Same-order consistency with the branch block metric

The new cost genuinely extends the old block-edit normalization.

### Lemma 3.1

Let `S,T` be two Steiner triple systems on the same `v`-point set `X`. Take

```math
U=X,
\qquad
\phi=\operatorname{id}_X.
```

Let

```math
E
=
|\{\{x,y\}\subset X:x\oplus_S y\ne x\oplus_T y\}|.
```

Then

```math
\boxed{
\frac{2E}{v(v-1)}=d_{blk}(S,T),
}
\tag{3.1}
```

where

```math
d_{blk}(S,T)
=
\frac{|\mathcal B_S\triangle\mathcal B_T|}{2b(v)},
\qquad
b(v)=\frac{v(v-1)}6.
```

Consequently

```math
D_{pc}(S;T,X,\operatorname{id})=d_{blk}(S,T).
\tag{3.2}
```

### Proof

Let

```math
m=|\mathcal B_S\setminus\mathcal B_T|.
```

Since the two systems have the same number of blocks,

```math
|\mathcal B_S\triangle\mathcal B_T|=2m.
```

Every block of `S` missing from `T` contributes its three unordered pairs to the completion-mismatch set. Distinct STS blocks have disjoint pair sets, and every mismatched pair belongs to exactly one missing `S`-block. Therefore

```math
E=3m.
```

Hence

```math
\frac{2E}{v(v-1)}
=
\frac{6m}{v(v-1)}
=
\frac{m}{b(v)}
=d_{blk}(S,T).
```

The point-loss term in (2.1) is zero, proving (3.2). `\square`

Thus no normalization is being changed on the already solved same-order regime.

---

## 4. Boundary cost of deleting points

The definition counts products that leave the retained core. For an STS this boundary has a sharp elementary upper bound.

### Lemma 4.1 (vertex deletion boundary)

Let `R\subseteq X` and `U=X\setminus R`, with `|R|=r`. The number of unordered pairs

```math
\{x,y\}\subset U
```

whose Steiner completion lies in `R` is at most

```math
\boxed{\frac{r(v-1)}2.}
\tag{4.1}
```

### Proof

Fix `z\in R`. The blocks through `z` partition `X\setminus\{z\}` into

```math
\frac{v-1}{2}
```

unordered pairs `{x,y}` satisfying

```math
x\oplus_S y=z.
```

At most that many of these pairs have both endpoints in `U`. Summing over `z\in R` proves (4.1). Distinct completion points cannot count the same pair twice. `\square`

### Corollary 4.2

Deleting `r=o(v)` points creates at most

```math
O(rv)=o(v^2)
```

boundary pair errors.

Therefore the partial-core normalization is quantitatively compatible with vertex deletion.

---

## 5. Exact audit of the Grannell--Lovegrove Add-4 construction

The previous shorthand that the Add-4 example is obtained by merely adding four points to an intact projective subsystem was too crude and must not be used.

We now audit the actual construction.

Let the source be a projective Steiner triple system

```math
P_v
```

of order

```math
v=2^{2k}-1.
```

Grannell--Lovegrove choose two parallel classes in the derived affine structure that share the distinguished infinity block

```math
I=\{\infty_1,\infty_2,\infty_3\}.
```

They remove the three infinity points and a family of affected blocks, obtaining

```math
V'=V\setminus I,
\qquad |V'|=v-3.
```

The affected old pairs on `V'` form a `7`-regular graph

```math
G_7
```

on `V'`. Decompose `G_7` into seven one-factors and introduce seven new points

```math
A=\{\alpha_1,\ldots,\alpha_7\}.
```

For every edge `{x,y}` in the `j`-th one-factor, replace its old completion by `\alpha_j`; finally place a Fano `STS(7)` on `A`.

The new Steiner triple system `T` has point set

```math
X_T=V'\sqcup A
```

and order

```math
w=(v-3)+7=v+4=2^{2k}+3.
\tag{5.1}
```

This is the wrong-order sequence used in `PROJECTIVE_WRONG_ORDER_OBSTRUCTION.md`.

The important fact for core comparison is:

> on pairs of old points in `V'`, the completion in `T` differs from the source projective completion **exactly on the edges of `G_7`**.

Indeed affected pairs are precisely those moved into the seven one-factors; every other old pair keeps its original projective block and its third point lies in `V'`.

Since `G_7` is `7`-regular,

```math
|E(G_7)|
=
\frac{7(v-3)}2.
\tag{5.2}
```

---

## 6. Add-4 is close in the partial-core sense

Compare the new wrong-order STS `T` of order `w=v+4` with its source projective STS `P_v`.

Take

```math
U=V'\subseteq X_T
```

and use the identity injection

```math
\phi:V'\hookrightarrow V(P_v).
```

Then

```math
|X_T\setminus U|=7,
```

while

```math
|V(P_v)\setminus\phi(U)|=3.
```

Thus the point-loss term is exactly

```math
\frac{10}{w}.
\tag{6.1}
```

By the construction audit, the bad pair set is exactly `E(G_7)`. Hence

```math
E_T^{P_v}(U,\phi)
=
\frac{7(v-3)}2
=
\frac{7(w-7)}2.
\tag{6.2}
```

### Theorem 6.1 (exact Add-4 partial-core cost)

For the Grannell--Lovegrove Add-4 system `T` of order `w=2^{2k}+3` and its projective source `P_v`, `v=w-4`,

```math
\boxed{
D_{pc}(T;P_v,V',\operatorname{id})
=
\frac{10}{w}
+
\frac{7(w-7)}{w(w-1)}.
}
\tag{6.3}
```

In particular,

```math
\boxed{
D_{pc}(T,\mathcal P)=O(1/w)\to0.
}
\tag{6.4}
```

### Proof

Here `N_*=w`. Equations (6.1) and (6.2) substituted in Definition 2.1 give

```math
D_{pc}
=
\frac{10}{w}
+
\frac{2\cdot 7(w-7)/2}{w(w-1)},
```

which is (6.3). `\square`

This is exactly the behavior wanted from the corrected notion of structural closeness:

- the system cannot be close to any group on the same carrier;
- it cannot inject all its points into a Boolean carrier of size `(1+o(1))w`;
- nevertheless it is only `O(1/w)` away, after discarding seven new points and allowing three unused model points, from the original projective geometry on the common core.

Thus the wrong-order obstruction is an obstruction to **carrier identity**, not to partial projective geometry.

---

## 7. A five-associator route to mediality

There is a second useful reformulation that stays internal to the Steiner loop.

For a commutative loop write the medial/parallelogram identity as

```math
(x\circ y)\circ(z\circ w)
=
(x\circ z)\circ(y\circ w).
\tag{7.1}
```

Let

```math
M_{med}
```

be the number of ordered quadruples `(x,y,z,w)` on which (7.1) fails, and let

```math
s
```

be the number of ordered associativity failures.

### Lemma 7.1 (associator-to-medial charging)

For every commutative quasigroup/loop,

```math
\boxed{M_{med}\le5ns,}
\tag{7.2}
```

where `n` is the order.

For a unital commutative loop, exact mediality implies exact associativity.

### Proof

Starting from the left side of (7.1), the following five associativity identities give a path to the right side:

```math
(xy)(zw)
= x(y(zw))
= x((yz)w)
= (x(yz))w
= ((xz)y)w
= (xz)(yw).
\tag{7.3}
```

The five required associativity tests are respectively

```math
\operatorname{Assoc}(x,y,z\circ w),
```

```math
\operatorname{Assoc}(y,z,w),
```

```math
\operatorname{Assoc}(x,y\circ z,w),
```

```math
\operatorname{Assoc}(x,z,y),
```

and

```math
\operatorname{Assoc}(x\circ z,y,w).
```

In the fourth step we also use commutativity `y\circ z=z\circ y`.

Therefore every failed medial quadruple forces at least one of these five associativity tests to fail.

When summed over all `n^4` quadruples, each of the five test templates covers every ordered triple exactly `n` times:

- in templates containing `z\circ w`, `y\circ z`, or `x\circ z`, the quasigroup property gives exactly `n` decompositions of the specified product;
- in templates omitting one variable, that variable has `n` free choices.

Hence the union bound gives `M_med<=5ns`.

Finally, if the loop has identity `0`, substitute `z=0` into exact mediality:

```math
(x\circ y)\circ(0\circ w)
=
(x\circ0)\circ(y\circ w),
```

so

```math
(x\circ y)\circ w=x\circ(y\circ w).
```

Thus exact mediality implies associativity. `\square`

### Corollary 7.2

If

```math
\delta_{assoc}=s/n^3,
\qquad
\delta_{med}=M_{med}/n^4,
```

then

```math
\boxed{\delta_{med}\le5\delta_{assoc}.}
\tag{7.4}
```

So almost projective phase also gives an almost-medial/parallelogram law with only constant-factor loss.

No publication-grade theorem has yet been located that turns (7.4) into an `o(n^2)` repair theorem for medial quasigroups. Exact Toyoda--Bruck structure is not enough; a quantitative stability theorem would still be needed.

---

## 8. Why generic Latin-square removal cannot simply be imported

The natural general repair statement for Latin squares is itself presented as a conjecture in Garbe--Hancock--Hladky--Sharifzadeh, *Limits of Latin squares* (Discrete Analysis 2023): few copies of a fixed pattern should permit `o(n^2)` entry changes removing all copies, with an even stronger conjecture asking that the repaired object remain a Latin square.

Our problem is more structured than a generic Latin square because we have:

```math
x\circ y=y\circ x,
\qquad
x\circ(x\circ y)=y,
\qquad
x\circ x=0,
```

and exact defect localization

```math
associator failures
\longleftrightarrow
C14
\longleftrightarrow
\text{block Pasch deficits}.
```

But until these extra identities are exploited in a proof, the general Latin removal conjecture cannot be used as a black box.

Likewise dense hypergraph removal has the wrong normalization: an STS has only `Theta(v^2)` blocks among `Theta(v^3)` possible triples. The required repair theorem is relative to the sparse pair-completion host.

---

## 9. Corrected projective-core conjecture

The first robust formulation surviving all obstruction tests is now the following.

### Conjecture 9.1 (partial projective-core stability)

For every `epsilon>0` there exists `delta>0` such that, for all sufficiently large `STS(v)` `S`,

```math
1-\rho_P(S)<\delta
```

implies

```math
\boxed{D_{pc}(S,\mathcal P)<\epsilon.}
\tag{9.1}
```

Equivalently, asymptotically:

```math
1-\rho_P=o(1)
\quad\Longrightarrow?\quad
D_{pc}(S,\mathcal P)=o(1).
\tag{9.2}
```

This allows:

- deletion of `o(v)` exceptional points from `S`;
- `o(v)` unused points in a nearby projective model;
- `o(v^2)` pair-completion errors on the retained core, including boundary products.

It does **not** demand that the retained set itself be closed under the projective operation.

The Add-4 sequence is compatible with the conjecture by Theorem 6.1.

This is an open conjecture, not a theorem.

---

## 10. What is now closed and what remains open

### Closed in this note

1. A cross-order partial-core cost that exactly recovers `d_blk` in the same-order/full-core case.
2. A sharp `O(rv)` bound on the pair-completion boundary created by deleting `r` points.
3. A corrected audit of the actual Add-4 construction: the projective source is not left intact as a literal subsystem.
4. An exact partial-core cost for Add-4:

```math
D_{pc}
=
10/w+7(w-7)/[w(w-1)]
=O(1/w).
```

5. A constant-loss implication from associativity defect to medial/parallelogram defect:

```math
M_{med}\le5ns.
```

6. Exact mediality of a unital Steiner loop implies exact associativity and hence a Boolean group.

### Open

1. Prove or refute Conjecture 9.1.
2. Find a Steiner-specific repair theorem for sparse `C14` / local Pasch deficit.
3. Determine whether almost-medial Steiner loops admit a direct quantitative repair theorem.
4. Test other near-maxi-Pasch constructions (Add-6, trades, switched projective systems) in `D_pc`.
5. Determine the best quantitative dependence `D_pc <= F(1-rho_P)` if a theorem holds.

---

## References

1. M. J. Grannell, G. J. Lovegrove, *Maximizing the number of Pasch configurations in a Steiner triple system*, Bulletin of the Institute of Combinatorics and its Applications 69 (2013), 23--35.
2. A. R. Kozlik, *The centre of a Steiner loop and the maxi-Pasch problem*, Comment. Math. Univ. Carolin. 61 (2020), 535--545. DOI `10.14712/1213-7243.2020.035`.
3. F. Garbe, R. Hancock, J. Hladky, M. Sharifzadeh, *Limits of Latin squares*, Discrete Analysis 2023:8. DOI `10.19086/da.83253`.
4. W. T. Gowers, J. Long, *Partial associativity and rough approximate groups*, Geom. Funct. Anal. 30 (2020), 1583--1647. DOI `10.1007/s00039-020-00553-1`.
