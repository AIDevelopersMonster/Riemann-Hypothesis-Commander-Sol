# Alice Throws Away the Ruler III
## From Local Fano Phase to Partial Projective Geometry: Sharp Obstructions and Rank-2 Boolean Fiberization

**Malachevsky, A.A.**  
ORCID: **0009-0008-6009-3196**  
Preprint manuscript v1.0 — 13 September 2026

---

## Abstract

We study structural stability on the projective side of the Hall--projective phase dichotomy for Steiner triple systems. For an `STS(v)`, let `rho_P` be the density of independent triples generating a Fano subsystem. The associated Steiner loop converts this local phase statistic into associativity defect: if `s` is the number of failed ordered associativity triples and `N=v(v-1)(v-3)/6`, then

```math
\frac{1-\rho_P}{3}
\le
\frac{s}{6N}
\le
1-\rho_P.
```

We first prove an exact local certificate for the projective phase and show by an explicit Pasch trade that associativity of all six permutations of a root does not characterize the Fano phase. In the ultra-low regime `s<3(v+1)^2/32`, Drápal's theorem on quasigroups rich in associative triples yields same-carrier edit rigidity: the loop is close to a group, that group is forced to be elementary abelian `2`, and the Steiner system is close to a projective system on the same point set.

This exact-order picture is asymptotically sharp. Using the Grannell--Lovegrove Add-4 maxi-Pasch construction we exhibit an explicit infinite sequence of wrong projective orders with `rho_P->1` and associativity defect `Theta(1/v)`. Hence arbitrary `o(1)` projective phase impurity does not force the projective order spectrum, and same-carrier or `(1+o(1))` supercarrier reconstruction is false. This establishes `Theta(1/v)` as the correct scale of exact order rigidity up to absolute constants.

To describe the surviving geometry we introduce a cross-order partial-core cost `D_pc`, which extends ordinary block edit distance and allows a small exceptional set together with a small number of pair-completion errors. We prove a universal linear converse

```math
D_{pc}(S,\mathcal P)
\ge
\frac{1-\rho_P}{12+o(1)}
```

whenever `D_pc->0`. Two independent benchmark families, Add-4 systems and direct products of projective systems, satisfy `D_pc=Theta(1-rho_P)`.

The main constructive theorem recovers the first two Boolean coordinates. Writing `epsilon=1-rho_P`, there exists a block `B={a,b,c}` such that `H={0,a,b,c}\cong F_2^2`; after deleting at most `2 epsilon (v-3)` points, the remaining Steiner loop splits exactly into four-point `H`-torsors, each extending `H` to a Fano subloop. Moreover, after symmetrizing the associativity audit, at most `40 epsilon v^2` ordered point pairs are contaminated, and every clean pair of fibers obeys the exact affine law

```math
(h\circ x)\circ(k\circ y)
=
(h\circ k)\circ(x\circ y).
```

Thus near-purity of the local Fano phase forces an exact rank-2 Boolean coordinate layer on a `1-O(epsilon)` fraction of the carrier, with only `O(epsilon)` interaction loss. Full linear partial-core rigidity is reduced to a quotient completion problem for the induced almost-Steiner multiplication on the set of fibers.

---

## 1. Introduction

The previous paper in this series established a quantitative Hall--projective phase theorem for Steiner triple systems. An independent triple was assigned phase `P` when it generated a Fano subsystem, phase `H` when it generated an affine plane of order `3`, and defect phase `D` otherwise. A small normalized anti-mitre count was shown to force one of the two pure phases to dominate.

That result was intentionally a phase-profile theorem. It did not claim that a system with `rho_P` close to `1` must be close, in block edit distance, to a projective Steiner triple system. The present paper addresses exactly that missing structural question.

A first guess is natural but wrong:

> if almost every independent triple is projective, then the whole system should be close to a projective system on the same point set.

The obstruction is arithmetic. Projective Steiner triple systems exist only at orders `2^m-1`, while there are wrong-order systems whose local projective phase tends to purity. Therefore any valid stability statement must separate local geometric purity from exact carrier order.

This paper develops that separation in three stages.

1. **Associator bridge.** The projective phase is converted into a quantitatively equivalent associativity defect in the associated Steiner loop.
2. **Sharp obstruction.** Same-carrier and near-supercarrier reconstruction are shown to fail beyond the `Theta(1/v)` exact-order scale.
3. **Partial geometry recovery.** A robust cross-order cost is introduced, and a constructive rank-2 Boolean fiberization theorem recovers exact local binary coordinates on almost all points.

The final result is not yet a complete edit-rigidity theorem. Rather, it identifies and proves the first nontrivial coordinate layer and isolates one sharply formulated remaining obstruction: quotient completion.

### 1.1 Main contributions

The new results proved here are:

- an exact three-associator certificate for a local Fano root;
- an explicit D-phase counterexample for which all six permutations of the root associate;
- an ultra-low same-carrier projective edit-rigidity theorem via Drápal's quasigroup theorem;
- a wrong-order sequence with `rho_P->1`, proving sharp `Theta(1/v)` exact-order scale up to constants;
- exact localization of associator defect as blockwise Pasch deficit and as the count of the classical `C14` configuration;
- obstruction to embedding all points with vanishing error into a group of size `(1+o(1))n`;
- a partial-core projective cost extending ordinary block edit distance;
- a universal linear lower bound for that cost;
- exact Add-4 and projective-product benchmark computations;
- an exact rank-2 Fano fiberization theorem with linear exceptional-set and interaction bounds.

The final linear upper bound

```math
D_{pc}(S,\mathcal P)
\le C(1-\rho_P)
```

remains open.

---

## 2. Steiner loops and the projective phase

Let `S=(X,\mathcal B)` be an `STS(v)`. Adjoin an identity `0` and define the associated Steiner loop

```math
L=X\sqcup\{0\}
```

by

```math
0\circ x=x,
\qquad
x\circ x=0,
```

and, for distinct `x,y\in X`, let `x\circ y` be the third point on their block.

Then

```math
x\circ y=y\circ x,
\qquad
x\circ(x\circ y)=y.
\tag{2.1}
```

Let

```math
N=\frac{v(v-1)(v-3)}6
```

be the number of independent triples of `S`. Let `rho_P` be the fraction of those triples that generate a Fano subsystem.

For an ordered independent triple `(x,y,z)`, write

```math
a=x\circ y,
\qquad
b=y\circ z,
\qquad
c=z\circ x.
```

The Fano closure is equivalent to the existence of the seventh point completing the three derived lines.

### Theorem 2.1 (exact local projective certificate)

An ordered independent root `(x,y,z)` is P-phase if and only if all three identities hold:

```math
Assoc(x,y,z),
\qquad
Assoc(y,z,x),
\qquad
Assoc(x\circ y,y,z).
\tag{2.2}
```

The third identity is precisely

```math
(x\circ y)\circ(y\circ z)=x\circ z.
\tag{2.3}
```

### Proof

The first two associativity identities identify a common seventh point `t` through

```math
(x\circ y)\circ z
=x\circ(y\circ z)
```

and its cyclic counterpart. The derived identity (2.3) supplies the missing line among `a,b,c`. The seven points

```math
x,y,z,a,b,c,t
```

then support the seven blocks of the Fano plane. Conversely every Fano subsystem is the nonzero part of `F_2^3`, so all three identities hold. `\square`

### 2.2 Root associativity alone is not enough

A Pasch trade inside `PG(3,2)` gives an explicit D-phase root for which all six permutations of `(x,y,z)` associate, while the derived condition (2.3) fails. Thus no criterion using only the six root permutations can characterize the projective phase.

This is why the bridge to global associativity must use derived triples as well.

---

## 3. Quantitative associator bridge

Let

```math
s
=
|\{(p,q,r)\in L^3:(p\circ q)\circ r\ne p\circ(q\circ r)\}|.
```

Associativity is automatic whenever one argument is `0`, two arguments coincide, or the three nonzero arguments are collinear. Hence all failures lie on ordered independent triples.

Put

```math
\delta_{ind}
=\frac{s}{v(v-1)(v-3)}.
\tag{3.1}
```

### Theorem 3.1 (phase/associator equivalence)

```math
\boxed{
\frac{1-\rho_P}{3}
\le
\delta_{ind}
\le
1-\rho_P.
}
\tag{3.2}
```

### Proof

A P-root contributes no associativity failures. This gives the upper bound.

For the lower bound, Theorem 2.1 says every ordered non-P root forces at least one of three associativity failures: at the root, at its cyclic shift, or at the derived triple `(x\circ y,y,z)`. The three maps on ordered independent triples are bijective, so the total number of ordered non-P roots is at most `3s`. Dividing by `v(v-1)(v-3)` gives (3.2). `\square`

Thus local projective impurity and global associativity defect are equivalent up to an absolute factor `3`.

---

## 4. Ultra-low exact edit rigidity

Let `n=v+1` be the loop order. Drápal proved that if a quasigroup of order `n` has `s` nonassociative triples and

```math
1\le s<\frac{3n^2}{32},
```

then there is a group operation on the same set at Hamming distance `t` satisfying

```math
3tn<s.
\tag{4.1}
```

For Steiner loops, closeness to an arbitrary group automatically upgrades to closeness to a Boolean group.

### Lemma 4.1 (Boolean recovery)

If a group law on the same `n`-point set is at table distance `t<n^2/8` from a Steiner loop, then the group is elementary abelian `2`.

### Proof sketch

If the group row of `a` differs from the Steiner involutive translation in fewer than `n/2` positions, then `a^2=e`. Hence at most `2t/n` group elements can fail to be involutions. If `t<n^2/8`, more than `3n/4` group elements are involutions. A finite group with more than `3/4` involutions is elementary abelian `2`. `\square`

Combining this with Drápal gives:

### Theorem 4.2 (ultra-low projective edit rigidity)

If

```math
s<\frac{3(v+1)^2}{32},
```

then `v+1` is a power of `2` and there exists a projective Steiner triple system `T` on the same point set such that

```math
\boxed{
d_{blk}(S,T)
<
\frac{s}{3(v+1)v(v-1)}.
}
\tag{4.2}
```

Here `d_blk` is normalized block symmetric-difference distance.

This proves exact same-order rigidity in an explicit small-constant `1/v` phase-impurity regime.

---

## 5. Wrong-order obstruction and sharp scale

The preceding theorem cannot be extended to arbitrary `rho_P->1` while preserving the carrier.

Grannell and Lovegrove construct, for every `k>=2`, an Add-4 Steiner triple system `T_k` of order

```math
w_k=2^{2k}+3.
```

The corresponding loop order is

```math
n_k=2^{2k}+4,
```

which is not a power of `2`.

Their exact Pasch count, combined with the associative-triple/Pasch identity for Steiner loops, gives

### Theorem 5.1 (exact Add-4 associator defect)

```math
\boxed{
s_k=4(w_k-7)(7w_k-48).}
\tag{5.1}
```

Hence

```math
\frac{s_k}{(w_k+1)^3}
=
\frac{28}{w_k}+O(w_k^{-2})
\to0.
```

By Theorem 3.1,

```math
1-\rho_P(T_k)=\Theta(1/w_k).
\tag{5.2}
```

Nevertheless every group law on the same carrier stays at normalized table distance at least `1/8`; otherwise Lemma 4.1 would force the wrong loop order to be a power of `2`.

### Corollary 5.2 (sharp exact-order scale)

The smallest possible projective phase impurity compatible with a wrong projective order has asymptotic scale

```math
\boxed{\Theta(1/v)}
```

up to absolute constants.

The lower bound follows from Theorem 4.2; the Add-4 sequence supplies the matching upper-order construction.

---

## 6. Pasch localization and the `C14` defect

For a block

```math
B=\{x,y,x\circ y\},
```

let `p(B)` be the number of Pasch configurations containing `B`. Define

```math
r_{xy}
=d_H(T_{x\circ y},T_xT_y),
```

where `T_x(z)=x\circ z`.

### Theorem 6.1 (blockwise Pasch localization)

```math
\boxed{
r_{xy}=r_{x,x\circ y}=r_{y,x\circ y}=(v-3)-p(B).
}
\tag{6.1}
```

### Proof

There are `v-3` points outside `B`. For such a point `z`, associativity at `(x,y,z)` holds exactly when the four blocks determined by `B`, `z`, and the two bracket completions form a Pasch configuration through `B`. Thus successful external points are in bijection with Pasches through `B`. `\square`

Summing over blocks yields

```math
\boxed{
s=v(v-1)(v-3)-24P(S),
}
\tag{6.2}
```

where `P(S)` is the total Pasch count.

The same defect is exactly the count of the classical seven-point four-block configuration `C14`:

```math
\boxed{s=4c_{14}.}
\tag{6.3}
```

Thus the projective stability problem is equivalently a sparse `C14` stability problem internal to an STS.

---

## 7. Why near-supercarrier reconstruction also fails

Suppose `phi:L->G` is injective into a finite group and all but `t_phi` ordered products satisfy

```math
\phi(x\circ y)=\phi(x)\phi(y).
```

If a row has fewer than `n/2` errors, then `phi(x)^2=e_G`; therefore `G` contains at least

```math
n-\frac{2t_\phi}{n}
```

involutions.

If `|G|=\lambda n` and `G` is non-Boolean, it has at most `3|G|/4` involutions, so

```math
\boxed{
\frac{t_\phi}{n^2}
\ge
\frac12-\frac{3\lambda}{8}.
}
\tag{7.1}
```

Hence vanishing product error into groups of size `(1+o(1))n` would force the ambient group to be Boolean.

For the Add-4 sequence the smallest Boolean supercarrier has asymptotic size ratio `2`, not `1`. Therefore even `(1+o(1))` enlargement of the carrier cannot support a vanishing-error embedding of all points.

This motivates a comparison notion that allows both a small exceptional source set and a small unused model set.

---

## 8. Partial-core projective cost

Let `S=(X,\mathcal B_S)` and let `P=(Y,\mathcal B_P)` be projective. Choose `U\subseteq X` and an injection

```math
\phi:U\hookrightarrow Y.
```

For an unordered pair `{x,y}\subset U`, call the pair bad if either its `S`-completion leaves `U` or the completion disagrees with the projective completion under `phi`.

Let `E` be the number of bad unordered pairs and

```math
N_*=\max\{|X|,|Y|\}.
```

Define

```math
\boxed{
D_{pc}(S;P,U,\phi)
=
\frac{|X\setminus U|+|Y\setminus\phi(U)|}{N_*}
+
\frac{2E}{N_*(N_*-1)}.
}
\tag{8.1}
```

Finally let `D_pc(S,\mathcal P)` be the infimum over all projective models and comparisons.

When `X=Y`, `U=X`, and `phi=id`, this is exactly ordinary normalized block edit distance.

### Theorem 8.1 (linear converse)

If `D=D_pc(S;P,U,phi)<1`, then

```math
\boxed{
1-\rho_P(S)
\le
\frac{12v^2}{(v-1)(v-3)}
\frac{D}{(1-D)^2}.
}
\tag{8.2}
```

Hence whenever `D_pc->0`,

```math
\boxed{
D_{pc}(S,\mathcal P)
\ge
\frac{1-\rho_P}{12+o(1)}.
}
\tag{8.3}
```

### Proof sketch

Every associativity failure entirely inside the retained core forces at least one of four bad pair completions. A bad pair supports at most `8v` such ordered failures. Triples meeting the exceptional source set contribute at most `3rv^2`. This gives

```math
s\le3rv^2+8Ev,
```

which converts directly to (8.2) using Theorem 3.1. `\square`

Thus any possible upper stability theorem must have at least linear defect scale.

---

## 9. Benchmark families

### 9.1 Add-4

A corrected audit of the Grannell--Lovegrove construction shows that the old projective system is not literally retained as a subsystem. Three infinity points are removed, seven new points are introduced, and the affected old pairs form a `7`-regular graph.

Nevertheless, in the partial-core cost one obtains the exact comparison

```math
\boxed{
D_{pc}
=
\frac{10}{w}
+
\frac{7(w-7)}{w(w-1)}
=O(1/w).
}
\tag{9.1}
```

Thus Add-4 destroys carrier identity but remains asymptotically projective in partial geometry.

### 9.2 Direct products of projective systems

Let

```math
m=2^a-1,
\qquad
n=2^b-1,
```

and take the direct product of the two projective Steiner quasigroups. Its order is `V=mn`, generally a wrong projective order.

A block-type calculation gives

```math
\boxed{
s
=3mn(m-1)(n-1)(m+n-2).
}
\tag{9.2}
```

Hence, when both factors grow,

```math
\delta_{ind}
=3\left(\frac1m+\frac1n\right)
+o\left(\frac1m+\frac1n\right).
```

The natural embedding into

```math
F_2^{a+b}\setminus\{0\}
```

omits exactly the two coordinate axes, `m+n` model points. Pair completions disagree exactly when the two product points share one coordinate, giving

```math
\boxed{
D_{pc}
=
\frac{m+n}{mn+m+n}
+
\frac{mn(m+n-2)}{(mn+m+n)(mn+m+n-1)}.
}
\tag{9.3}
```

For this natural comparison,

```math
\frac{D_{pc}}{\delta_{ind}}\to\frac23.
\tag{9.4}
```

Thus both Add-4 and projective-product families exhibit linear structural cost.

---

## 10. Fano-extension defect

The preceding results motivate a direct Fano-counting argument.

A Fano subsystem contains `28` independent triples, and every P-root lies in a unique Fano subsystem. Therefore

```math
\boxed{
F(S)=\frac{\rho_P N}{28}.
}
\tag{10.1}
```

For a block `B`, let `f(B)` be the number of Fano subsystems containing it. Define

```math
\boxed{e(B)=(v-3)-4f(B).}
\tag{10.2}
```

Then `e(B)` counts exactly the external points that fail to extend `B` to a Fano subsystem.

### Lemma 10.1

```math
\boxed{
\sum_Be(B)=N(1-\rho_P).
}
\tag{10.3}
```

Thus near-purity of the P-phase forces low average Fano-extension defect per block.

---

## 11. Rank-2 Fano fiberization

Set

```math
\varepsilon=1-\rho_P.
```

For `x\in L`, let

```math
A_x
=|\{(y,z):(x\circ y)\circ z\ne x\circ(y\circ z)\}|.
```

Since `\sum_xA_x=s` and `s\le\varepsilon v(v-1)(v-3)`, fewer than `v/6` points can satisfy

```math
A_x>6\varepsilon(v-1)(v-3).
```

Combining this row regularization with (10.3) yields a block `B={a,b,c}` such that

```math
A_a,A_b,A_c\le6\varepsilon(v-1)(v-3)
```

and

```math
e(B)\le2\varepsilon(v-3).
```

Put

```math
H=\{0,a,b,c\}\cong F_2^2.
```

Let `R_B` be the external points not extending `B` to a Fano subsystem. Then

```math
|R_B|=e(B)\le2\varepsilon(v-3).
\tag{11.1}
```

### Theorem 11.1 (exact rank-2 fiberization)

After deleting `R_B`, the loop decomposes exactly as

```math
\boxed{
L\setminus R_B
=H\sqcup C_1\sqcup\cdots\sqcup C_q,
}
\tag{11.2}
```

where every `C_i` has four points and `H\cup C_i` is an elementary abelian group of order `8` under the original multiplication.

Thus `H` acts regularly on every `C_i`, recovering two exact Boolean coordinates on a `1-O(\varepsilon)` fraction of the carrier.

---

## 12. Exact affine interaction on clean fiber pairs

The final audit must be symmetric in the two input orientations.

Call `(x,y)` contaminated if:

- `x\circ y` leaves the retained set; or
- for some `h\in H`, `(h\circ x)\circ y\ne h\circ(x\circ y)`; or
- for some `h\in H`, `(h\circ y)\circ x\ne h\circ(y\circ x)`.

### Lemma 12.1

The number of contaminated ordered point pairs is less than

```math
\boxed{40\varepsilon v^2.}
\tag{12.1}
```

### Proof

Products leaving the retained set contribute at most

```math
2\varepsilon(v-3)(v+1)
```

pairs. The two orientation conditions contribute at most

```math
2(A_a+A_b+A_c)
\le36\varepsilon(v-1)(v-3).
```

The sum is less than `40\varepsilon v^2`. `\square`

Call a fiber pair `(C,D)` clean if every ordered pair in `C\times D` is uncontaminated.

### Theorem 12.2 (exact affine law)

Let `(C,D)` be clean, choose `x\in C`, `y\in D`, and put `z=x\circ y`. Then for all `h,k\in H`,

```math
\boxed{
(h\circ x)\circ(k\circ y)
=(h\circ k)\circ z.
}
\tag{12.2}
```

In particular, all products from `C\times D` lie in the single output fiber `[z]`.

### Proof

The reverse-orientation cleanliness gives

```math
x\circ(k\circ y)=k\circ(x\circ y)=k\circ z.
```

Cleanliness of `(x,k\circ y)` then gives

```math
(h\circ x)\circ(k\circ y)=h\circ(k\circ z).
```

Since `z` lies in a Boolean `H`-fiber, the last expression equals `(h\circ k)\circ z`. `\square`

This proves the main constructive statement: near Fano-phase purity forces an exact two-bit affine layer on almost all points and almost all fiber interactions.

---

## 13. Almost-medial and almost-commuting viewpoints

The same defect has two useful alternative formulations.

First, five associativity identities connect the two sides of the medial law

```math
(x\circ y)\circ(z\circ w)
=(x\circ z)\circ(y\circ w).
```

If `M_med` is the number of failed ordered medial quadruples, then

```math
\boxed{M_{med}\le5(v+1)s.}
\tag{13.1}
```

Second, the translation family satisfies the exact commutator identity

```math
\boxed{
\sum_{x,y}d_H(T_xT_y,T_yT_x)=s.
}
\tag{13.2}
```

Hence near-projective phase implies both almost-mediality and average almost-commutation of the involutive translations.

Known permutation-stability results do not presently close the argument uniformly in the growing Boolean rank, so these viewpoints remain supporting structure rather than black-box completion theorems.

---

## 14. The quotient barrier

The rank-2 fiberization reduces the remaining problem to a quotient set

```math
\mathcal Q_B=\{H,C_1,\ldots,C_q\}.
```

On all but `O(\varepsilon)` of the fiber pairs there is an exact well-defined quotient multiplication `C\diamond D`, and the original multiplication is exactly `H`-affine above those pairs.

What is missing is a completion theorem of the following form:

> an almost-Steiner multiplication on `q` symbols with `O(\varepsilon q^2)` missing or inconsistent cells can be repaired to an exact Steiner quasigroup after `O(\varepsilon q^2)` changes, with constants uniform in `q`.

This is not supplied by current general Latin-square repair results. Dense hypergraph removal has the wrong normalization for an STS, and the repaired-Latin form of pattern removal remains conjectural in the relevant generality.

Accordingly, the full linear upper bound remains a conjecture.

### Conjecture 14.1 (linear partial projective-core stability)

There exist absolute constants `C>0` and `epsilon_0>0` such that, for all sufficiently large Steiner triple systems,

```math
1-\rho_P\le\epsilon_0
```

implies

```math
\boxed{
D_{pc}(S,\mathcal P)
\le C(1-\rho_P).
}
\tag{14.1}
```

Theorem 8.1 shows that this would be sharp in order of magnitude.

---

## 15. Discussion

The projective phase is more rigid than a local closure label but less rigid than exact carrier order.

Three distinct scales emerge.

1. At defect below a sufficiently small constant multiple of `1/v`, exact order and same-carrier projective edit rigidity hold.
2. At defect `Theta(1/v)`, wrong projective orders already occur.
3. At arbitrary small constant defect, exact carrier information is lost, but a large amount of binary geometry survives: a rank-2 Boolean coordinate layer can still be recovered with linear loss.

The Add-4 and direct-product examples suggest that wrong-order systems near the projective phase may often be understood as genuine binary geometries with a thin algebraic boundary removed or modified. The partial-core cost formalizes that intuition without pretending that all points can remain on the same carrier.

The rank-2 theorem supplies a first rigorous coordinate manifestation of this picture. It also explains why the remaining problem is naturally recursive: once one exact `F_2^2` layer has been extracted, the unresolved information lives in a quotient multiplication.

---

## 16. Conclusion

Near-projective phase purity in a Steiner triple system does not imply exact projective order, and it does not imply closeness to a group on the same or asymptotically equal larger carrier. These failures occur already at the sharp `Theta(1/v)` order-rigidity scale.

What does survive is partial binary geometry. The associator defect is exactly localized by Pasch deficits and `C14` configurations; partial-core structural distance has an unavoidable linear scale; and, most importantly, almost all points admit an exact decomposition into Fano fibers over one Boolean rank-2 subloop. Almost all interactions between those fibers are exactly affine over `F_2^2`.

Thus the transition from phase stability to structural stability is neither automatic nor absent. The first two Boolean coordinates are rigid; the remaining difficulty is quotient completion.

---

## References

1. A. Drápal, *On quasigroups rich in associative triples*, Discrete Mathematics **44** (1983), 251--265. DOI: `10.1016/0012-365X(83)90189-9`.
2. M. J. Grannell, G. J. Lovegrove, *Maximizing the number of Pasch configurations in a Steiner triple system*, Bulletin of the Institute of Combinatorics and its Applications **69** (2013), 23--35.
3. A. R. Kozlik, *The centre of a Steiner loop and the maxi-Pasch problem*, Commentationes Mathematicae Universitatis Carolinae **61** (2020), 535--545. DOI: `10.14712/1213-7243.2020.035`.
4. W. T. Gowers, J. Long, *Partial associativity and rough approximate groups*, Geometric and Functional Analysis **30** (2020), 1583--1647. DOI: `10.1007/s00039-020-00553-1`.
5. G. Arzhantseva, L. Păunescu, *Almost commuting permutations are near commuting permutations*, Journal of Functional Analysis **269** (2015), 745--757. DOI: `10.1016/j.jfa.2015.02.013`.
6. O. Becker, J. Mosheiff, *Abelian Groups Are Polynomially Stable*, International Mathematics Research Notices **2021** (20), 15574--15632. DOI: `10.1093/imrn/rnaa017`.
7. F. Garbe, R. Hancock, J. Hladký, M. Sharifzadeh, *Limits of Latin squares*, Discrete Analysis **2023**:8. DOI: `10.19086/da.83253`.
8. M. Aryapoor, *The Pasch configuration and Steiner triple systems*, arXiv:1306.1257 (2013).
9. A. A. Malachevsky, *Phase Rigidity in Steiner Triple Systems: Quantitative Hall--Projective Stability from Anti-Mitre Defects*, Alice Throws Away the Ruler II, Zenodo (2026). DOI: `10.5281/zenodo.22722951`.

---

## Author note

This manuscript is the third paper in the *Alice Throws Away the Ruler* sequence. All statements labelled theorem, lemma, or corollary above are proved in the accompanying branch notes. Conjecture 14.1 and the quotient-completion problem are explicitly open.