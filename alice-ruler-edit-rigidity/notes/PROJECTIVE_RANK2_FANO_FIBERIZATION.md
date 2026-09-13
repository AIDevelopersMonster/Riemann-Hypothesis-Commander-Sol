# PROJECTIVE_RANK2_FANO_FIBERIZATION

**Branch:** `research/alice-ruler-edit-rigidity`  
**Status:** closed first constructive Boolean-coordinate layer; publication-audited 2026-09-13  
**Depends on:** `PROJECTIVE_ASSOCIATOR_BRIDGE.md`, `PROJECTIVE_PASCH_LOCALIZATION_AND_CARRIER_GAP.md`, `PROJECTIVE_LINEAR_COST_AND_PRODUCT_BENCHMARK.md`

> **Publication-audit correction.** The first draft of Sections 7--8 used a one-sided contamination condition and quoted the convenient constant `20`. To derive the affine identity for `(h∘x)∘(k∘y)` one also needs the reverse orientation `(y,x)`. The definition below is symmetrized, the proof is complete, and the safe constant is `40`. All qualitative and linear conclusions are unchanged.

---

## 1. Purpose

Let `S` be an `STS(v)` and let

```math
\varepsilon:=1-\rho_P,
```

where `rho_P` is the density of independent triples generating a Fano subsystem. We prove that one can choose a block

```math
B=\{a,b,c\}
```

whose order-4 Steiner subloop

```math
H=\{0,a,b,c\}\cong C_2^2
```

acts exactly on all but `O(\varepsilon v)` points in four-point Fano fibers, and such that multiplication between all but `O(\varepsilon v^2)` point pairs is exactly `H`-affine. Thus the first two Boolean coordinates are recovered with linear loss; the remaining obstruction is quotient completion/repair.

---

## 2. Fano count and blockwise Fano-extension defect

Let

```math
N=\frac{v(v-1)(v-3)}6
```

be the number of independent triples. Every P-root generates one unique Fano subsystem, while a Fano subsystem contains

```math
\binom73-7=28
```

independent triples. Hence, if `F(S)` is the number of Fano subsystems,

```math
\boxed{F(S)=\frac{\rho_P N}{28}.}
\tag{2.1}
```

For a block `B`, let `f(B)` be the number of Fano subsystems containing `B`. Distinct such Fanos have disjoint four-point complements outside `B`, so `4f(B)\le v-3`. Define

```math
\boxed{e(B):=(v-3)-4f(B).}
\tag{2.2}
```

Equivalently, `e(B)` counts external points `z\notin B` for which `B\cup\{z\}` does not generate a Fano subsystem.

### Lemma 2.1

```math
\boxed{\sum_{B\in\mathcal B(S)}e(B)=N(1-\rho_P)=N\varepsilon.}
\tag{2.3}
```

### Proof

Every Fano contains seven blocks, so `\sum_B f(B)=7F(S)`. Therefore

```math
4\sum_B f(B)=28F(S)=\rho_PN.
```

Since the number of STS blocks is `b(v)=v(v-1)/6` and `b(v)(v-3)=N`, summing (2.2) gives (2.3). `\square`

If `p(B)` is the number of Pasch configurations through `B`, then every Fano through `B` contributes four Pasches through `B`. Hence `p(B)\ge4f(B)` and the local Pasch defect

```math
d(B)=(v-3)-p(B)
```

satisfies

```math
\boxed{d(B)\le e(B).}
\tag{2.4}
```

---

## 3. Translation commutator defect

Let `L=X\sqcup\{0\}` be the associated Steiner loop and

```math
T_x(z)=x\circ z.
```

Let

```math
s=|\{(x,y,z)\in L^3:(x\circ y)\circ z\ne x\circ(y\circ z)\}|.
```

### Lemma 3.1

```math
\boxed{\sum_{x,y\in L}d_H(T_xT_y,T_yT_x)=s,}
\tag{3.1}
```

where `d_H` is unnormalized Hamming distance.

### Proof

For fixed `x,y`, the two permutations differ at `z` exactly when

```math
x\circ(y\circ z)\ne y\circ(x\circ z).
```

By commutativity the right side is `(x\circ z)\circ y`; hence this is precisely the associativity failure at `(x,z,y)`. Summing merely permutes coordinates. `\square`

Thus almost-projective phase gives an average almost-commuting family of involutive translations with no loss of defect.

---

## 4. Choosing a clean base block

For `x\in L`, define

```math
A_x:=|\{(y,z):(x\circ y)\circ z\ne x\circ(y\circ z)\}|.
\tag{4.1}
```

Then `\sum_xA_x=s`. The associator bridge gives

```math
s\le\varepsilon v(v-1)(v-3).
\tag{4.2}
```

Call `x\in X` row-bad if

```math
A_x>6\varepsilon(v-1)(v-3).
```

There are fewer than `v/6` row-bad points; otherwise their loads alone exceed (4.2). Every point lies in `(v-1)/2` blocks, so fewer than half of all blocks meet a row-bad point. Combining this with (2.3) yields the following.

### Theorem 4.1 (clean base block)

There exists a block

```math
B=\{a,b,c\}
```

such that

```math
\boxed{A_a,A_b,A_c\le6\varepsilon(v-1)(v-3)}
\tag{4.3}
```

and

```math
\boxed{e(B)\le2\varepsilon(v-3).}
\tag{4.4}
```

### Proof

At least `b(v)/2` blocks contain no row-bad point. Since the total `e`-mass is `N\varepsilon`, one of these blocks has

```math
e(B)\le\frac{N\varepsilon}{b(v)/2}=2\varepsilon(v-3).
```

`\square`

---

## 5. Exact rank-2 Fano fiberization

Fix the block from Theorem 4.1 and put

```math
H=\{0,a,b,c\}.
```

Then `H\cong C_2^2`. Let

```math
R_B=\{z\in X\setminus B:\langle B\cup\{z\}\rangle\not\cong S_7\}.
```

By definition `|R_B|=e(B)`, so

```math
\boxed{|R_B|\le2\varepsilon(v-3).}
\tag{5.1}
```

Put `U=L\setminus R_B`. Every Fano containing `B` is an order-8 Boolean subloop containing `H`; its four points outside `H` form a regular `H`-orbit. Distinct such Fanos have disjoint external four-sets.

### Theorem 5.1 (rank-2 Fano fiberization)

There is an exact disjoint decomposition

```math
\boxed{U=H\sqcup C_1\sqcup\cdots\sqcup C_q,}
\tag{5.2}
```

where each `C_i` has four points and `H\cup C_i` is an elementary abelian group of order `8` under the original multiplication. In particular, `H` acts regularly on each `C_i`. Moreover

```math
q=f(B)=\frac{v-3-e(B)}4.
```

### Proof

Every point outside `R_B\cup B` extends `B` to a unique Fano subsystem. The four external points of each such Fano form one `H`-orbit, and uniqueness/disjointness gives (5.2). Inside each Fano plus the loop identity, the Steiner multiplication is the Boolean group law of `C_2^3`. `\square`

Thus the first two Boolean coordinates are recovered **exactly** on all but `O(\varepsilon v)` points.

---

## 6. Symmetric contamination and its linear bound

To propagate the `H`-coordinates across two fibers we need associativity in both orientations of a point pair.

Call an ordered pair `(x,y)\in U^2` **contaminated** if at least one of the following holds:

1. `x\circ y\notin U`;
2. for some `h\in H`,

```math
(h\circ x)\circ y\ne h\circ(x\circ y);
\tag{6.1}
```

3. for some `h\in H`,

```math
(h\circ y)\circ x\ne h\circ(y\circ x).
\tag{6.2}
```

Let `Z` be the set of contaminated ordered pairs. This definition is symmetric: `(x,y)\in Z` iff `(y,x)\in Z`.

### Lemma 6.1 (publication-audited contamination bound)

```math
\boxed{|Z|<40\varepsilon v^2.}
\tag{6.3}
```

### Proof

For condition 1, each `r\in R_B` occurs exactly once in every row of the loop table, hence is the product of exactly `v+1` ordered pairs. Thus the number of pairs whose product leaves `U` is at most

```math
|R_B|(v+1)\le2\varepsilon(v-3)(v+1).
\tag{6.4}
```

For conditions 2 and 3, `h=0` never fails. For each of `h=a,b,c`, condition 2 fails on exactly `A_h` ordered pairs. After swapping the last two coordinates, condition 3 also fails on exactly `A_h` ordered pairs. Hence the union of orientation failures has size at most

```math
2(A_a+A_b+A_c)
\le36\varepsilon(v-1)(v-3).
\tag{6.5}
```

Adding (6.4) and (6.5),

```math
|Z|
\le2\varepsilon(v-3)(v+1)+36\varepsilon(v-1)(v-3)
```

```math
=2\varepsilon(v-3)(19v-17)
<38\varepsilon v^2
<40\varepsilon v^2.
```

`\square`

---

## 7. Clean fiber pairs are exactly `H`-affine

Treat `H` itself as a distinguished fiber. For `x\in U`, write `[x]` for its unique fiber in

```math
\mathcal Q_B=\{H,C_1,\ldots,C_q\}.
```

Call an ordered fiber pair `(C,D)` **clean** if every ordered point pair in `C\times D` is uncontaminated. Because contamination is symmetric, clean `(C,D)` also gives the reverse orientation needed below.

### Theorem 7.1 (exact affine law on a clean fiber pair)

Let `(C,D)` be clean, choose `x\in C`, `y\in D`, and put `z=x\circ y`. Then `z\in U`, and for every `h,k\in H`,

```math
\boxed{(h\circ x)\circ(k\circ y)=(h\circ k)\circ z.}
\tag{7.1}
```

Consequently every product from `C\times D` lies in the single output fiber `[z]`, and multiplication on this fiber pair is exactly the standard affine/torsor law over `H\cong\mathbb F_2^2`.

### Proof

Since `(x,y)` is uncontaminated, `z\in U`. Condition (6.2) for `(x,y)` with `h=k` gives, using commutativity,

```math
x\circ(k\circ y)=k\circ(x\circ y)=k\circ z.
\tag{7.2}
```

Because `k\circ y\in D`, the pair `(x,k\circ y)` is also uncontaminated. Condition (6.1) for this pair gives

```math
(h\circ x)\circ(k\circ y)
=h\circ\bigl(x\circ(k\circ y)\bigr)
=h\circ(k\circ z).
\tag{7.3}
```

Finally `z\in U`, so `z` lies in `H` or in a Fano fiber. In either case `H\cup[z]` is Boolean, hence

```math
h\circ(k\circ z)=(h\circ k)\circ z.
```

Combining with (7.3) proves (7.1). `\square`

### Corollary 7.2 (linear rank-2 quotient error)

All but at most

```math
\boxed{40\varepsilon v^2}
```

ordered fiber pairs carry an exact well-defined `H`-affine multiplication law. Since `|\mathcal Q_B|=(v+1-e(B))/4=\Theta(v)`, this is an `O(\varepsilon)` fraction of fiber pairs.

The constant `40` is deliberately non-optimized; the theorem is about linear dependence and exact affine structure on the clean pairs.

---

## 8. Structural interpretation

After deleting at most `2\varepsilon(v-3)` points, the loop is partitioned into exact copies of the two-bit torsor `H\cong\mathbb F_2^2`. On every clean pair of fibers, after choosing one origin in each fiber, multiplication has the exact form

```math
(h,C)\circ(k,D)=(h+k,\ C\diamond D).
\tag{8.1}
```

Thus the original reconstruction problem has been reduced, with linear loss, to completing or repairing an almost-Steiner multiplication on the quotient set of fibers.

This is a positive coordinate-recovery theorem: the first two Boolean coordinates are not guessed or approximately represented; they are recovered as exact internal Fano geometry on a `1-O(\varepsilon)` fraction of the carrier.

---

## 9. Why the proof does not yet iterate automatically

The quotient operation `C\diamond D` is coherently defined only on all but `O(\varepsilon)` of the fiber pairs. We have not proved that the missing/inconsistent quotient cells can be repaired to an exact Steiner quasigroup while changing `O(\varepsilon q^2)` entries. That is the remaining quotient-completion problem.

General results do not presently provide this step as a black box. Arzhantseva--Păunescu prove permutation-Hamming stability of the commutator for every fixed finite tuple of permutations, while the relevant translation family/rank here grows with the order. Becker--Mosheiff prove polynomial permutation stability for abelian groups, but this does not immediately yield a rank-uniform completion theorem for the entire growing Steiner quotient. General Latin-square removal in the needed repaired-Latin form remains conjectural in the modern limits literature.

Therefore the remaining obstruction is sharply localized:

> **quotient completion/repair, not recovery of the first Boolean coordinate layer.**

---

## 10. Closed conclusions

For every `STS(v)` with `\varepsilon=1-\rho_P`, there exists a block `B` such that:

1. `H=\{0\}\cup B\cong C_2^2` is exact Boolean;
2. at most `2\varepsilon(v-3)` points fail to belong to a Fano extension of `B`;
3. all remaining points split exactly into four-point `H`-torsors;
4. at most `40\varepsilon v^2` ordered point pairs are contaminated;
5. every clean fiber pair obeys the exact affine law (7.1);
6. therefore the first two Boolean coordinates are recovered with linear vertex and pair loss;
7. full linear partial-core rigidity is reduced to quotient completion/repair.

---

## References checked for the completion barrier

1. G. Arzhantseva, L. Păunescu, *Almost commuting permutations are near commuting permutations*, J. Funct. Anal. 269 (2015), 745--757. DOI `10.1016/j.jfa.2015.02.013`.
2. O. Becker, J. Mosheiff, *Abelian Groups Are Polynomially Stable*, Int. Math. Res. Not. 2021 (20), 15574--15632. DOI `10.1093/imrn/rnaa017`.
3. A. R. Kozlik, *The centre of a Steiner loop and the maxi-Pasch problem*, Comment. Math. Univ. Carolin. 61 (2020), 535--545. DOI `10.14712/1213-7243.2020.035`.
4. F. Garbe, R. Hancock, J. Hladký, M. Sharifzadeh, *Limits of Latin squares*, Discrete Analysis 2023:8. DOI `10.19086/da.83253`.
