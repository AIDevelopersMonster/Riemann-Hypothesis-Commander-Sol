# PROJECTIVE_DRAPAL_EDIT_RIGIDITY

**Branch:** `research/alice-ruler-edit-rigidity`  
**Status:** closed ultra-low-defect projective reconstruction step, 2026-09-12  
**Depends on:** `PROJECTIVE_ASSOCIATOR_BRIDGE.md`

## 1. Purpose

The associator bridge converts projective phase impurity into the number of failed associativity tests in the associated Steiner loop. The next question is whether a published almost-associativity theorem gives actual multiplication-table/edit-distance control.

The best exact same-set theorem located in the first literature audit is Aleš Drápal, *On quasigroups rich in associative triples*, Discrete Mathematics 44 (1983), 251–265, DOI `10.1016/0012-365X(83)90189-9`.

For a quasigroup `Q` of order `n`, let

```math
s(Q)=|\{(x,y,z)\in Q^3:(xy)z\ne x(yz)\}|,
```

and let

```math
t(Q)=\min_G |\{(x,y)\in Q^2:x*y\ne x\cdot_G y\}|,
```

where the minimum is over group operations on the **same underlying set**.

Drápal proves, in particular,

```math
4tn-2t^2-24t\le s\le4tn,
```

and the stronger implication

```math
1\le s<\frac{3n^2}{32}
\quad\Longrightarrow\quad
3tn<s.
\tag{D}
```

The second estimate is exactly useful to us, but only in an ultra-low-defect regime: `s=O(n^2)`, not merely `s=o(n^3)`.

---

## 2. Boolean recovery from a very close group

Let `(L,\circ)` be a Steiner loop of order `n`, with identity `0`. Thus every left translation

```math
Q_a:y\mapsto a\circ y
```

is an involution:

```math
Q_a^2=\mathrm{id}.
\tag{2.1}
```

Suppose a group operation `*` on the same set `L` differs from `\circ` in `t<n/2` table cells.

### Lemma 2.1

The group `(L,*)` is an elementary abelian `2`-group and its identity is the Steiner-loop identity `0`.

### Proof

For each `a\in L`, let

```math
P_a:y\mapsto a*y
```

and let

```math
r_a=|\{y:a*y\ne a\circ y\}|.
```

Then `r_a\le t<n/2`. Both `P_a` and `Q_a` are permutations. Hamming distance on permutations is invariant under composition by a permutation, so

```math
d_H(P_a^2,Q_a^2)
\le d_H(P_a^2,P_aQ_a)+d_H(P_aQ_a,Q_a^2)
=2r_a<n.
```

By (2.1), `Q_a^2=id`. In the group,

```math
P_a^2(y)=(a*a)*y.
```

If `a*a` were not the group identity `e`, the left translation by `a*a` would have no fixed points, hence would have Hamming distance exactly `n` from `id`. This contradicts the strict bound above. Therefore

```math
a*a=e
```

for every `a`. A group in which every element has square `e` is abelian, hence `(L,*)` is elementary abelian of exponent `2`.

It remains to identify the identity. If `e\ne0`, then the group row of `e` is the identity permutation, whereas the Steiner translation `Q_e` has no fixed point: `e\circ y=y=0\circ y` would imply `e=0` by cancellation. Thus the entire row would differ and `t\ge n`, contradicting `t<n/2`. Hence `e=0`. `\square`

This lemma is stronger than merely recovering commutativity: closeness below `n/2` cells forces exponent `2` and the correct identity automatically.

---

## 3. Exact conversion from loop-table distance to STS block distance

Let `S` be the STS on

```math
X=L\setminus\{0\},
\qquad v=|X|=n-1.
```

If `*` is the Boolean group operation from Lemma 2.1, let `T` be the projective STS whose blocks are

```math
\{x,y,x*y\}
```

for distinct nonzero `x,y`.

Because both operations have identity `0` and exponent `2`, they agree on every cell involving `0` and every diagonal cell. Both are commutative, so the `t` erroneous ordered cells come in symmetric pairs. Hence the number of unordered pairs `{x,y}` whose third-point completion differs between `S` and `T` is

```math
E=t/2.
```

Let `b=v(v-1)/6` be the number of blocks. If `m=|\mathcal B(S)\setminus\mathcal B(T)|`, every missing block contributes exactly its three pairs to the mismatch set, and every mismatched pair belongs to exactly one such block. Thus

```math
E=3m.
```

With the branch normalization

```math
d_{blk}(S,T)
=\frac{|\mathcal B(S)\triangle\mathcal B(T)|}{2b}
=\frac{m}{b},
```

we obtain the exact identity

```math
\boxed{
d_{blk}(S,T)=\frac{t}{v(v-1)}.
}
\tag{3.1}
```

---

## 4. Drápal-regime projective edit rigidity

Let

```math
s=F_{assoc}
```

be the total number of failed associativity triples in the Steiner loop `L`.

### Theorem 4.1

If

```math
s<\frac{3(v+1)^2}{32},
\tag{4.1}
```

then `v+1` is a power of `2` and there exists a projective Steiner triple system `T` on the same point set `X` such that, when `s>0`,

```math
\boxed{
d_{blk}(S,T)
<\frac{s}{3(v+1)v(v-1)}.
}
\tag{4.2}
```

If `s=0`, then `S` itself is projective and the distance is zero.

### Proof

If `s=0`, the Steiner loop is associative. An associative quasigroup is a group, and a Steiner loop that is a group is elementary abelian of exponent `2`; therefore its nonzero elements form the projective STS.

Assume `s>0`. Apply Drápal's estimate (D) with `n=v+1`. There is a group operation `*` on the same set with table distance `t` satisfying

```math
3t(v+1)<s.
```

By (4.1),

```math
t<\frac{s}{3(v+1)}<\frac{v+1}{32}<\frac{v+1}{2}.
```

Lemma 2.1 therefore makes `(L,*)` an elementary abelian `2`-group with identity `0`. In particular `v+1=2^m` for some `m`, and its nonzero points define a projective STS `T` on the same `X`.

Finally (3.1) and `t<s/[3(v+1)]` give (4.2). `\square`

---

## 5. Phase-density form

The closed associator bridge proves

```math
s
\le
v(v-1)(v-3)(1-\rho_P).
\tag{5.1}
```

Therefore the following purely phase-theoretic sufficient condition implies (4.1):

```math
1-\rho_P
<
\theta_v
:=
\frac{3(v+1)^2}{32v(v-1)(v-3)}.
\tag{5.2}
```

### Corollary 5.1

If (5.2) holds, then `v+1` is a power of `2` and there is a projective STS `T` on the same point set with

```math
\boxed{
d_{blk}(S,T)
<
\frac{v-3}{3(v+1)}(1-\rho_P).
}
\tag{5.3}
```

### Proof

Equation (5.1) and (5.2) imply (4.1). Apply Theorem 4.1 and then (5.1):

```math
d_{blk}(S,T)
<
\frac{s}{3(v+1)v(v-1)}
\le
\frac{v-3}{3(v+1)}(1-\rho_P).
```

`\square`

### Corollary 5.2 (order-gap consequence)

If `v+1` is not a power of `2`, then necessarily

```math
\boxed{
1-\rho_P\ge
\frac{3(v+1)^2}{32v(v-1)(v-3)}.
}
\tag{5.4}
```

This is the first explicit order-rigidity statement in the branch: wrong projective order has a nonzero phase-impurity gap of order `1/v`.

---

## 6. Consequence for the anti-mitre parameter

On the P-dominant branch, Article II gives

```math
1-\rho_P=O(\varepsilon),
\qquad
\varepsilon=c_A/N.
```

Consequently, any P-dominant sequence satisfying

```math
\varepsilon=o(1/v)
```

lies eventually in the Drápal regime and obeys

```math
d(S,\mathcal P_v)=O(\varepsilon).
```

Moreover `v+1` is eventually a power of `2`.

This is a genuine edit-distance reconstruction theorem, but only in the ultra-low-defect scale. It does **not** yet prove the desired size-uniform statement `F(\varepsilon)\to0` for arbitrary `\varepsilon\to0` independent of `v`.

---

## 7. Stability-theorem audit

### Drápal 1983

Best exact fit found so far:

- quasigroup/Latin hypothesis: yes;
- group on the same underlying set: yes;
- explicit Hamming distance: yes;
- strong converse from associativity failures: only in the regime `s<3n^2/32`.

Thus it closes the ultra-low-defect theorem above but not the full branch target.

### Levi 99% theorem as reported by Gowers–Long

Gowers and Long, *Partial associativity and rough approximate groups*, GAFA 30 (2020), state that Elad Levi proved the 99% case: if almost all triples associate, the table agrees almost everywhere with a group operation after an injection into a group of approximately the same size. However their cited source is a master's thesis/private communication. Until an accessible proof with quantitative constants and the precise same-set conclusion is source-checked, it is not suitable as a publication-grade imported theorem for this branch.

### Gowers–Long 2020

Their published theorem treats even the positive-density ('1%') regime but returns a dense portion approximated by a metric group. That is substantially weaker than global Hamming/edit closeness of the entire Latin square, so it does not directly finish projective edit rigidity.

### Property-testing results

Modern group/abelian-group testers, including Bshouty (MFCS 2026), distinguish exact group tables from tables far in Hamming distance. They do not by themselves give a bound of Hamming distance in terms of the **uniform associativity-failure density**; the 2026 algorithm explicitly uses a different reconstruction strategy rather than an associativity test. Therefore no implication is imported from those testers without an additional proof.

---

## 8. Next proof obligation

The remaining projective bottleneck is now sharply separated into two scales.

1. **Ultra-low scale `1-\rho_P=O(1/v)`: CLOSED** by Theorem 4.1 / Corollary 5.1.
2. **Uniform 99% scale `1-\rho_P=o(1)`: OPEN.** Need either:
   - a published quantitative same-set almost-associative quasigroup theorem with `t/n^2\to0` as `s/n^3\to0`; or
   - an in-house proof specialized to Steiner loops.

The special Steiner identities should be exploited before attempting a general quasigroup theorem: all translations are involutions, the loop is commutative, and the identity/exponent-2 recovery above is automatic once any same-set group approximation is `o(n)` in absolute table distance, or can be adapted to row-wise control in a weaker approximation.

---

## References checked

1. A. Drápal, *On quasigroups rich in associative triples*, Discrete Mathematics 44 (1983), 251–265. DOI: `10.1016/0012-365X(83)90189-9`.
2. W. T. Gowers, J. Long, *Partial associativity and rough approximate groups*, Geometric and Functional Analysis 30 (2020), 1583–1647. DOI: `10.1007/s00039-020-00553-1`.
3. A. R. Kozlik, *The centre of a Steiner loop and the maxi-Pasch problem*, Comment. Math. Univ. Carolin. 61 (2020), 535–545. DOI: `10.14712/1213-7243.2020.035`.
4. N. H. Bshouty, *Sublinear Time Algorithms for Abelian Group Property Testing*, MFCS 2026, LIPIcs 386, Article 89. DOI: `10.4230/LIPIcs.MFCS.2026.89`.

The literature audit found earlier work linking Steiner-loop associative triples to Pasch counts and citing Drápal, but no checked source yet containing the specific `P`-phase-density -> same-set Boolean-group -> STS block-distance theorem above. This is a novelty assessment, not a formal priority guarantee.
