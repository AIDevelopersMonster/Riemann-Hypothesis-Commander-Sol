# FCOA Rigidity Cost — Replacement Capacity Bound

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** post-publication theorem note.

## 1. Domain orbit and defect-one shell

Let

\[
\Omega=G^2\setminus\Delta
\]

and let the carrier symmetric group `K=S_G` act on subsets of `Omega` by

\[
hD=\{h(p):p\in D\}.
\]

Write

\[
A=\operatorname{Stab}_K(D)=\operatorname{Aut}(G;D)
\]

for the uncolored domain automorphism group.

Define the defect-one orbit shell

\[
\mathcal O_1(D)
=
\{D'\in K\cdot D:
|D\setminus D'|=|D'\setminus D|=1\}.
\]

For a missing cell `e in Omega\D`, define its shell multiplicity

\[
m_D(e)
=
|\{p\in D:D-\{p\}+\{e\}\in\mathcal O_1(D)\}|.
\]

### Theorem 1.1 — Orbit-shell count

\[
\boxed{
|\mathcal O_1(D)|
=
\sum_{e\notin D}m_D(e).
}
\]

Moreover the number of carrier permutations `h in K` with defect

\[
d_D(h)=1
\]

is exactly

\[
\boxed{
|A|\,|\mathcal O_1(D)|.
}
\]

### Proof
Every defect-one orbit neighbour has a unique positive defect cell `e` and a unique deleted old cell `p`, so the first identity is just partition by the positive defect cell.

For fixed `D' in K.D`, the transporter set

\[
\{h\in K:hD=D'\}
\]

is any one transporter `h_0` times the stabilizer `A`; hence it has size `|A|`. Summing over the defect-one shell proves the second identity. `square`

This shows why raw permutation counting is too coarse: the natural geometric capacity unit is an orbit neighbour, not an individual carrier permutation.

## 2. Exact lower description of beta-killing cells

Assume the old layer `(D,c)` is nonexact and write

\[
B_{old}=A_Q(D,c)\setminus A_{an}(D,c).
\]

Let

\[
M=\Omega\setminus D
\]

be the missing-cell set.

For `g in B_old`, let the old component phase on a component `C` of `Lambda(D)` be

\[
\epsilon_g(C)\in F_2.
\]

For a missing singleton cell `e`, let

\[
T_D(e)\subseteq\pi_0(\Lambda(D))
\]

be the set of old incidence components touched by `e`.

Define the singleton-survival set

\[
\boxed{
S_g
=
\{e\in M:
 g(e)=e
\text{ and }
\epsilon_g(C)=0\text{ for every }C\in T_D(e)
\}.
}
\]

For an isolated missing cell the touch set is empty, so the phase condition is vacuous.

### Theorem 2.1 — Exact beta-killing complement

A missing singleton cell kills every old bad automorphism iff it lies outside every `S_g`. Hence

\[
\boxed{
W_{kill}
=
M\setminus\bigcup_{g\in B_{old}}S_g.
}
\]

### Proof
Fix an old bad `g`. Since `gD=D`, the singleton extension can preserve the enlarged domain only if `g(e)=e`. In that case the new cell has discrepancy 0. The old discrepancy is already constant on each old incidence component. The singleton extension preserves the ternary reduct exactly when every old component joined to the fixed new cell has old phase 0. This is precisely `e in S_g`. Therefore `e` fails to kill at least one old bad automorphism iff it lies in the union of the `S_g`. `square`

Consequently

\[
\boxed{
|W_{kill}|
=|M|-\left|\bigcup_{g\in B_{old}}S_g\right|
}
\]

and the union bound gives

\[
\boxed{
|W_{kill}|
\ge
|M|-\sum_{g\in B_{old}}|S_g|.
}
\]

## 3. Crude carrier-fixed-point lower bound

Let `f(g)` be the number of carrier points fixed by `g`.

A fixed ordered non-loop cell must have both endpoints fixed by `g`. Therefore

\[
|S_g|
\le
f(g)(f(g)-1).
\]

Hence

\[
\boxed{
|W_{kill}|
\ge
|M|-
\sum_{g\in B_{old}}f(g)(f(g)-1).
}
\]

This estimate is intentionally crude but completely group-theoretic. The exact `S_g` formula is normally much sharper because phase-1 touched components remove many fixed missing cells from `S_g`.

## 4. Anchored beta-killing cells

Let

\[
M_{anch}=\{e\in M:T_D(e)\ne\varnothing\},
\qquad
W_{anch}=W_{kill}\cap M_{anch}.
\]

Then exactly

\[
\boxed{
W_{anch}
=
M_{anch}\setminus
\bigcup_{g\in B_{old}}(S_g\cap M_{anch}).
}
\]

and therefore

\[
|W_{anch}|
\ge
|M_{anch}|-
\sum_{g\in B_{old}}|S_g\cap M_{anch}|.
\]

Only `W_anch` is needed for the anchored escape argument.

## 5. Local replacement capacity

Fix an anchored missing cell `e` and put

\[
S_e=D\cup\{e\}.
\]

Let

\[
\Gamma_e=\operatorname{Aut}(G;S_e)
\]

and

\[
A_e=\{a\in A:a(e)=e\}
=\Gamma_e\cap A.
\]

Define the replacement-target set

\[
P(e)=\{p\in D:\exists h\in\Gamma_e,\ h(e)=p\}.
\]

### Theorem 5.1 — Target/index identity

The nontrivial cosets of `A_e` in `Gamma_e` are in bijection with the replacement targets `P(e)`. Therefore

\[
\boxed{
|P(e)|=[\Gamma_e:A_e]-1.
}
\]

### Proof
For `h in Gamma_e`,

\[
hD=h(S_e\setminus\{e\})=S_e\setminus\{h(e)\}.
\]

Thus `h` moves `D` iff `h(e) in D`. Two domain-moving elements `h,k` have the same target `h(e)=k(e)` iff `k^{-1}h` fixes `e` and preserves `D`, i.e. iff they lie in the same `A_e`-coset. `square`

Moreover every target `p in P(e)` yields the orbit neighbour

\[
D-\{p\}+\{e\}\in\mathcal O_1(D),
\]

so

\[
\boxed{
|P(e)|\le m_D(e).
}
\]

## 6. Color-refined capacity

For an anchored beta-killing `e`, let

\[
H_e=\{a\in A^+(D,c):a(e)=e\}
\]

be the common D-preserving phase-0 core from `BETA_ONE_FATAL_GEOMETRY_CLASSIFICATION.md`.

Put

\[
s(e)=[A_e:H_e].
\]

For any fixed replacement target `p`, all carrier transporters with target `p` form one `A_e`-coset, and hence split into at most `s(e)` different `H_e`-cosets.

Thus the number of distinct replacement `H_e`-cosets available over `e` is at most

\[
\boxed{
\operatorname{cap}(e)
:=|P(e)|s(e)
\le m_D(e)s(e).
}
\]

Persistent Exclusion says one bad `H_e`-coset cannot cover both colors. Therefore a split-fatal anchored beta-killing cell necessarily satisfies

\[
\boxed{
\operatorname{cap}(e)\ge2.
}
\]

### Corollary 6.1 — Local capacity escape

If an anchored beta-killing cell satisfies

\[
\boxed{m_D(e)s(e)\le1,}
\]

then at least one of its two colors is exact and hence

\[
\boxed{\alpha=\beta=1.}
\]

This is a theorem-level escape criterion.

## 7. Global normalized capacity bound

Let

\[
s_{max}=\max_{e\in W_{anch}}s(e).
\]

Since

\[
\sum_{e\in M}m_D(e)=|\mathcal O_1(D)|,
\]

we have

\[
\sum_{e\in W_{anch}}\operatorname{cap}(e)
\le
s_{max}|\mathcal O_1(D)|.
\]

If every anchored beta-killing cell were split-fatal, each would require capacity at least 2. Hence:

### Theorem 7.1 — Replacement Capacity Bound

If

\[
\boxed{
s_{max}|\mathcal O_1(D)|<2|W_{anch}|,}
\]

then some anchored beta-killing cell is not split-fatal. Since Persistent Exclusion removes the only other anchored fatal mechanism, one of its colors is exact. Therefore

\[
\boxed{\alpha(D,c)=\beta(D,c)=1.}
\]

This is the desired orbit-normalized capacity theorem.

## 8. Combined lower-bound criterion

Using the exact/union-bound estimate for `W_anch`, a sufficient purely checkable condition is

\[
\boxed{
s_{max}|\mathcal O_1(D)|
<
2\left(
|M_{anch}|-
\sum_{g\in B_{old}}|S_g\cap M_{anch}|
\right).
}
\]

Whenever this holds,

\[
\boxed{\alpha=\beta=1.}
\]

A still coarser carrier-fixed-point version follows by replacing each survival-set size by the number of fixed ordered cells of `g`.

## 9. Phase-clean stabilizer corollary

Suppose for every anchored beta-killing cell

\[
A_e=H_e,
\]

so `s(e)=1`. Then

\[
s_{max}=1
\]

and the global criterion simplifies to

\[
\boxed{
|\mathcal O_1(D)|<2|W_{anch}|
\Longrightarrow
\alpha=\beta=1.
}
\]

Thus in the phase-clean stabilizer sector, the problem is a direct comparison between:

- the number of defect-one orbit neighbours of the old definedness domain;
- twice the number of anchored singleton cells which kill every old bad phase symmetry.

## 10. Why raw permutation capacity is the wrong invariant

The earlier provisional bound used the number of defect-one carrier permutations. By Theorem 1.1 this equals

\[
|A|\,|\mathcal O_1(D)|,
\]

which can be arbitrarily inflated by internal automorphisms of the old domain without creating new replacement geometries.

The correct first-order capacity invariant is therefore the orbit shell

\[
\boxed{|\mathcal O_1(D)|,}
\]

with local stabilizer correction `s(e)` only where opposite-color split transporters can occur.

## 11. Current boundary

The global theorem

\[
\beta=1\Longrightarrow\alpha=1
\]

is not yet proved. But any counterexample must now evade all of the following:

1. Beta-One Escape / danger-saturation criterion;
2. Persistent Exclusion;
3. Local capacity escape `m_D(e)s(e)<=1` for every anchored killing cell;
4. Global orbit-shell inequality of Theorem 7.1;
5. all existing exhaustive and targeted finite audits.

Thus a remaining counterexample must simultaneously have a large defect-one orbit shell, unusually small anchored killing set, and enough stabilizer complexity to provide two distinct color-specific replacement cosets over every anchored beta-killing cell.

## Claim firewall

1. The orbit-shell identities are exact.
2. The singleton survival-set description of `W_kill` is exact.
3. The fixed-point estimate is only a lower bound.
4. `cap(e)` is an upper bound on available replacement `H_e`-cosets, not a claim that all such cosets are bad.
5. The global capacity inequality is sufficient, not necessary.
6. The general beta-one theorem remains open.
