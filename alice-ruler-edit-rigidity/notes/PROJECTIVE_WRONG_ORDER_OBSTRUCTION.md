# PROJECTIVE_WRONG_ORDER_OBSTRUCTION

**Branch:** `research/alice-ruler-edit-rigidity`  
**Status:** closed negative theorem + sharp order-scale result, 2026-09-13  
**Depends on:** `PROJECTIVE_ASSOCIATOR_BRIDGE.md`, `PROJECTIVE_DRAPAL_EDIT_RIGIDITY.md`, `ROBUST_BOOLEAN_RECOVERY_FROM_GROUP_DISTANCE.md`

## 1. Purpose

The previous status isolated the putative uniform same-set implication

```math
s/n^3\to0
\quad\Longrightarrow?\quad
t/n^2\to0,
```

where `s` is the number of nonassociative triples in a Steiner loop of order `n`, and `t` is the minimum Hamming distance of its multiplication table from a group law on the same set.

This note shows that this implication is **false**, even for Steiner loops. The obstruction is not pathological: classical maxi-Pasch constructions give an explicit infinite wrong-order sequence with associativity defect tending to zero.

At the same time, combining this construction with the previously proved Drápal-regime lower bound shows that the projective **order-rigidity scale `1/v` is asymptotically sharp up to absolute constants**.

---

## 2. Two classical inputs

### 2.1 Associative triples and Pasch configurations

Let `S` be an `STS(w)` and let `L` be its Steiner loop of order

```math
n=w+1.
```

Let `P(S)` be the number of Pasch configurations. Kozlik, Proposition 3.1, gives

```math
|A(L)|
=
n^3-(n-1)(n-2)(n-4)+24P(S),
```

where `A(L)` is the set of associative ordered triples.

Therefore the number of nonassociative ordered triples is

```math
s(S)
=(n-1)(n-2)(n-4)-24P(S)
=w(w-1)(w-3)-24P(S).
\tag{2.1}
```

Put

```math
M(w)=\frac{w(w-1)(w-3)}{24}.
```

Then (2.1) is exactly

```math
\boxed{s(S)=24\bigl(M(w)-P(S)\bigr).}
\tag{2.2}
```

Reference: A. R. Kozlik, *The centre of a Steiner loop and the maxi-Pasch problem*, Comment. Math. Univ. Carolin. 61 (2020), 535--545, DOI `10.14712/1213-7243.2020.035`, Proposition 3.1.

### 2.2 Explicit wrong-order high-Pasch systems

Grannell--Lovegrove construct, for every `k>=2`, an STS `T_k` by their Add 4 construction applied to the projective system of order `2^{2k}-1`.

The resulting order is

```math
w_k=2^{2k}+3.
\tag{2.3}
```

Their Theorem 2.1 gives, writing `w=w_k`,

```math
\boxed{
P(T_k)
=
\frac{(w-7)(w^2-25w+216)}{24}+7.
}
\tag{2.4}
```

Reference: M. J. Grannell and G. J. Lovegrove, *Maximizing the number of Pasch configurations in a Steiner triple system*, Bull. Inst. Combin. Appl. 69 (2013), 23--35, Theorem 2.1.

These orders are not projective orders. Indeed the corresponding loop order is

```math
n_k=w_k+1=2^{2k}+4
=4\bigl(2^{2k-2}+1\bigr),
```

and for `k>=2` the factor `2^{2k-2}+1` is odd and greater than `1`. Hence

```math
\boxed{n_k\ne2^m.}
\tag{2.5}
```

---

## 3. Exact associativity defect of the Add 4 sequence

### Theorem 3.1

For the Steiner loop `L_k` associated with `T_k`, the exact number of failed associativity triples is

```math
\boxed{
s_k=4(w_k-7)(7w_k-48).
}
\tag{3.1}
```

Consequently

```math
\frac{s_k}{(w_k+1)^3}\to0,
```

indeed

```math
\frac{s_k}{(w_k+1)^3}
=\frac{28}{w_k}+O(w_k^{-2}).
\tag{3.2}
```

### Proof

From (2.4),

```math
M(w)-P(T_k)
=
\frac{w(w-1)(w-3)
-(w-7)(w^2-25w+216)-168}{24}.
```

Expanding the numerator gives

```math
28w^2-388w+1344
=4(7w^2-97w+336)
=4(w-7)(7w-48).
```

After division by `24`,

```math
M(w)-P(T_k)
=
\frac{(w-7)(7w-48)}6.
```

Equation (2.2) now yields

```math
s_k
=24\cdot\frac{(w-7)(7w-48)}6
=4(w-7)(7w-48).
```

This is `28w^2+O(w)`, while `(w+1)^3=w^3+O(w^2)`, proving (3.2). `\square`

---

## 4. The P-phase density also tends to one

Let

```math
\delta_{ind}(T_k)
=\frac{s_k}{w_k(w_k-1)(w_k-3)}.
```

The closed `PROJECTIVE_ASSOCIATOR_BRIDGE` proves for every STS

```math
\frac{1-\rho_P}{3}
\le\delta_{ind}
\le1-\rho_P.
```

Hence for `T_k`

```math
\boxed{
\delta_{ind}(T_k)
\le1-\rho_P(T_k)
\le3\delta_{ind}(T_k).
}
\tag{4.1}
```

Using (3.1),

```math
\delta_{ind}(T_k)
=
\frac{4(w_k-7)(7w_k-48)}
{w_k(w_k-1)(w_k-3)}
=
\frac{28}{w_k}+O(w_k^{-2}).
\tag{4.2}
```

Therefore

```math
\boxed{1-\rho_P(T_k)=\Theta(1/w_k),}
\tag{4.3}
```

and in particular

```math
\boxed{\rho_P(T_k)\to1.}
\tag{4.4}
```

Thus there are explicit Steiner triple systems of nonprojective order whose local projective phase tends to purity.

---

## 5. Same-set 99% group reconstruction is false

Recall the previously proved robust Boolean recovery theorem:

> If a group law on the same `n`-point set is at multiplication-table Hamming distance `t<n^2/8` from a Steiner loop, then that group is elementary abelian `2`; in particular `n=2^m`.

### Theorem 5.1 (wrong-order obstruction)

There is an infinite sequence of Steiner loops `L_k` such that

```math
\frac{s(L_k)}{|L_k|^3}\to0,
```

but for **every** group law `*` on the same underlying set,

```math
\boxed{
d_H(\circ_k,*)\ge\frac{|L_k|^2}{8}.
}
\tag{5.1}
```

Equivalently, if

```math
t_k
=
\min_{\text{group laws }*\text{ on }L_k}
d_H(\circ_k,*),
```

then

```math
\boxed{t_k/|L_k|^2\ge1/8}
```

although `s(L_k)/|L_k|^3->0`.

### Proof

Take `L_k` from Theorem 3.1. Its associativity-failure density tends to zero by (3.2).

Suppose for contradiction that some group law on the same `n_k`-point carrier had table distance `<n_k^2/8`. Robust Boolean recovery would force that group to be elementary abelian `2`, hence would force `n_k` to be a power of `2`.

But (2.5) proves that

```math
n_k=2^{2k}+4
```

is not a power of `2` for every `k>=2`. Contradiction. Therefore every same-set group law has distance at least `n_k^2/8`. `\square`

### Consequence 5.2

The proposed uniform same-set implication

```math
s/n^3\to0
\Longrightarrow
t/n^2\to0
```

is **false even within the class of Steiner loops**.

So the former `STATUS.md` description of this implication as the sole remaining projective bottleneck must be retired: it is not an unproved theorem but a false target.

---

## 6. Exact projective order rigidity is false at the `o(1)` phase scale

The same sequence also refutes the naive order-rigidity hope

```math
1-\rho_P=o(1)
\quad\Longrightarrow\quad
w+1=2^m.
```

Indeed (4.4) gives `rho_P(T_k)->1`, while (2.5) gives `w_k+1` non-Boolean for every `k`.

Thus the projective branch cannot have a same-order theorem of the form

```math
rho_P\to1
\Longrightarrow
 d(S,\mathcal P_w)\to0
```

without an explicit order hypothesis, because for these `w_k` the family `\mathcal P_{w_k}` is empty.

---

## 7. Sharp scale of projective order rigidity

The negative result matches the positive Drápal regime at the level of asymptotic scale.

From `PROJECTIVE_DRAPAL_EDIT_RIGIDITY.md`, every `STS(w)` with `w+1` not a power of `2` satisfies

```math
1-\rho_P
\ge
\frac{3(w+1)^2}{32w(w-1)(w-3)}
=
\frac{3}{32w}+O(w^{-2}).
\tag{7.1}
```

On the other hand, the explicit wrong-order sequence `T_k` satisfies by (4.1)--(4.2)

```math
1-\rho_P(T_k)
\le
\frac{12(w_k-7)(7w_k-48)}
{w_k(w_k-1)(w_k-3)}
=
\frac{84}{w_k}+O(w_k^{-2}).
\tag{7.2}
```

Therefore:

### Theorem 7.1 (sharp order-rigidity scale)

The smallest possible projective phase impurity compatible with a wrong projective order has asymptotic scale `Theta(1/w)` in the following precise sense:

1. every wrong-order STS obeys a universal lower bound `Omega(1/w)` from (7.1);
2. an explicit infinite wrong-order sequence obeys an upper bound `O(1/w)` from (7.2).

Thus the `1/w` scale is sharp up to absolute constants.

This also corrects the earlier shorthand “the `O(1/v)` regime is closed.” The proved positive theorem is an **explicit small-constant `1/v` regime** (and hence certainly every `o(1/v)` regime), not arbitrary `O(1/v)`.

---

## 8. Corrected target after the obstruction

The natural projective stability target must allow the carrier size to move.

The Grannell--Lovegrove sequence itself is instructive: `T_k` is built from the projective order

```math
2^{2k}-1
```

and has order

```math
2^{2k}+3,
```

a difference of only `4` points. Thus its failure of exact same-order reconstruction is an **order/carrier obstruction**, not evidence that the object is macroscopically unrelated to a projective model.

The corrected uniform question is therefore of the following form.

> If a Steiner loop has `s/n^3=o(1)` (equivalently on the P-dominant branch `1-rho_P=o(1)`), does there exist a Boolean group / projective STS on a carrier of size `n'=n+o(n)` and an injection or deletion/addition model under which the original multiplication/block structure agrees on `1-o(1)` of the relevant pairs/blocks?

This is deliberately recorded as an **open target, not a theorem**.

It matches the qualitative shape of the “99%” result attributed to Elad Levi in Gowers--Long: the recovered group is allowed to have approximately, rather than exactly, the original cardinality.

---

## 9. Research consequences

Closed:

1. explicit wrong-order sequence with `rho_P->1`;
2. exact associativity defect formula for that sequence;
3. refutation of same-set `99% associativity => o(n^2) group distance` for Steiner loops;
4. refutation of exact projective order rigidity at the `o(1)` phase scale;
5. proof that the `1/v` phase-impurity scale for exact order rigidity is sharp up to constants.

Open:

1. carrier-adjusted / nearby-order reconstruction;
2. quantitative control of the required point additions/deletions in terms of associativity or P-phase defect;
3. whether the Add 4/Add 6 constructions are extremal for the constant in the `1/v` order gap;
4. Hall-branch analogue.

---

## References

1. M. J. Grannell, G. J. Lovegrove, *Maximizing the number of Pasch configurations in a Steiner triple system*, Bulletin of the Institute of Combinatorics and its Applications 69 (2013), 23--35.
2. A. R. Kozlik, *The centre of a Steiner loop and the maxi-Pasch problem*, Commentationes Mathematicae Universitatis Carolinae 61 (2020), 535--545. DOI `10.14712/1213-7243.2020.035`.
3. A. Drápal, *On quasigroups rich in associative triples*, Discrete Mathematics 44 (1983), 251--265. DOI `10.1016/0012-365X(83)90189-9`.
4. W. T. Gowers, J. Long, *Partial associativity and rough approximate groups*, Geometric and Functional Analysis 30 (2020), 1583--1647. DOI `10.1007/s00039-020-00553-1`.
