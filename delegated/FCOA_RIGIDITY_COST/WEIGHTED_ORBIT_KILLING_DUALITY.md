# FCOA Rigidity Cost — Weighted Orbit–Killing Duality

**Status:** post-publication theorem note and correction of an overly strong heuristic.

## 1. The naive fixed-point/shell monotonicity is false

There is no universal implication

\[
\text{large fixed-point set of an old bad symmetry}
\Longrightarrow
\text{small defect-one orbit shell}.
\]

### Counterexample family

Let

\[
G=\{0,1,\dots,n-1\}
\]

with `n>=6`, fix an integer `k` with `3<=k<=n-2`, and let

\[
D=\{(0,i):1\le i\le k\}.
\]

Thus `D` is an outward directed star with `k` leaves. Let

\[
g=(1\ 2).
\]

Then `gD=D` and `g` fixes `n-2` carrier points.

Color

\[
c(0,1)=0,\qquad c(0,2)=1,
\]

and give at least one further star cell, say `(0,3)`, color `0`.

The ordered-cell incidence graph `Lambda(D)` is edgeless: no two star cells are composable. Hence every domain automorphism preserves the ternary reduct. The discrepancy of `g` is `1` on the two exchanged cells and `0` on every fixed star cell, so

\[
\boxed{g\in B_{old}.}
\]

Nevertheless the defect-one orbit shell is large. Keeping the center `0` and replacing one selected leaf by one unused leaf gives

\[
\boxed{|\mathcal O_1(D)|\ge k(n-1-k).}
\]

For `k` near `(n-1)/2`, this is quadratic in `n`, while

\[
f(g)=n-2.
\]

Therefore large old-bad fixed-point mass and large defect-one mobility can coexist.

This kills the proposed universal monotone route.

## 2. The correct refinement: positive-defect mass on anchored cells

Let

\[
M=\Omega\setminus D,
\qquad
M_{anch}=\{e\in M:T_D(e)\ne\varnothing\}.
\]

Recall

\[
m_D(e)=
|\{p\in D:D-\{p\}+\{e\}\in\mathcal O_1(D)\}|.
\]

Define the **anchored shell mass**

\[
\boxed{
\Sigma_{anch}(D)
=
\sum_{e\in M_{anch}}m_D(e).
}
\]

This counts defect-one orbit neighbours with multiplicity by their positive defect cell, but only when that positive defect cell is anchored to the old incidence geometry.

Clearly

\[
\boxed{
\Sigma_{anch}(D)\le |\mathcal O_1(D)|.
}
\]

The inequality can be strict when many defect-one orbit neighbours add isolated cells.

## 3. Killing-restricted shell mass

Let

\[
W_{anch}=W_{kill}\cap M_{anch}.
\]

Define

\[
\boxed{
\Sigma_{kill}(D,c)
=
\sum_{e\in W_{anch}}m_D(e).
}
\]

Then

\[
\boxed{
\Sigma_{kill}\le\Sigma_{anch}\le|\mathcal O_1(D)|.
}
\]

This is the shell quantity actually relevant to anchored beta-one fatality.

## 4. Exact local capacity weighting

For anchored beta-killing `e`, recall

\[
s(e)=[A_e:H_e]
\]

and the exact replacement-coset capacity

\[
\tau(e)=|P(e)|s(e).
\]

Since

\[
|P(e)|\le m_D(e),
\]

we have

\[
\boxed{
\tau(e)\le m_D(e)s(e).
}
\]

Persistent Exclusion implies that if `e` is fatal for both colors, then

\[
\tau(e)\ge2.
\]

Therefore every fatal anchored beta-killing cell satisfies

\[
\boxed{
m_D(e)s(e)\ge2.}
\]

## 5. Weighted Capacity Theorem

### Theorem 5.1

If

\[
\boxed{
\sum_{e\in W_{anch}}m_D(e)s(e)
<
2|W_{anch}|,
}
\]

then at least one anchored beta-killing cell is not fatal, hence one of its binary colors gives an exact singleton repair and

\[
\boxed{\alpha(D,c)=\beta(D,c)=1.}
\]

### Proof
If every anchored beta-killing cell were fatal, the local inequality above would give

\[
m_D(e)s(e)\ge2
\]

for every `e in W_anch`. Summing contradicts the displayed strict inequality. `square`

This is strictly sharper than using a global maximum `s_max` and the full orbit shell.

## 6. Anchored-shell corollary

Let

\[
s_{max}=\max_{e\in W_{anch}}s(e).
\]

Since

\[
\sum_{e\in W_{anch}}m_D(e)s(e)
\le
s_{max}\Sigma_{kill}
\le
s_{max}\Sigma_{anch},
\]

we obtain:

### Corollary 6.1

If

\[
\boxed{
s_{max}\Sigma_{anch}(D)<2|W_{anch}|,}
\]

then

\[
\boxed{\alpha=\beta=1.}
\]

This improves the previous sufficient condition

\[
s_{max}|\mathcal O_1(D)|<2|W_{anch}|.
\]

## 7. Exact killing-set substitution

From the singleton survival theorem,

\[
W_{anch}
=
M_{anch}\setminus
\bigcup_{g\in B_{old}}(S_g\cap M_{anch}).
\]

Hence the right-hand side in Corollary 6.1 is exactly

\[
2\left|
M_{anch}\setminus
\bigcup_{g\in B_{old}}(S_g\cap M_{anch})
\right|.
\]

Thus a completely explicit sufficient criterion is

\[
\boxed{
 s_{max}\Sigma_{anch}(D)
<
2\left|
M_{anch}\setminus
\bigcup_{g\in B_{old}}(S_g\cap M_{anch})
\right|
\Longrightarrow
\alpha=\beta=1.
}
\]

This is the current cleanest direct comparison between replacement mobility and old-obstruction killing capacity.

## 8. Equivariance of replacement multiplicities

Let `a in Aut(G;D)`. Then

\[
\boxed{m_D(ae)=m_D(e).}
\]

Indeed

\[
D-\{p\}+\{e\}\in K\cdot D
\]

iff

\[
D-\{ap\}+\{ae\}=a(D-\{p\}+\{e\})\in K\cdot D.
\]

Thus `m_D` is constant on `Aut(D)`-orbits of missing cells, and in particular on `A^+`-orbits of `W_anch`.

The same holds for `s(e)` under `A^+`. Therefore the weighted quantity

\[
\boxed{w(e)=m_D(e)s(e)}
\]

is constant on every phase-0 killing orbit.

## 9. Orbit form of the weighted theorem

Let

\[
W_{anch}=O_1\sqcup\cdots\sqcup O_t
\]

be its decomposition into `A^+`-orbits, and let `w_i` be the common value of `w(e)` on `O_i`.

Then Theorem 5.1 becomes

\[
\boxed{
\sum_{i=1}^t |O_i|w_i
<
2\sum_{i=1}^t|O_i|
\Longrightarrow
\alpha=\beta=1.
}
\]

Since every `w_i` is a nonnegative integer, a beta-one counterexample requires

\[
\boxed{w_i\ge2\quad\text{for every anchored killing orbit }O_i.}
\]

This orbitwise integer threshold is stronger conceptually than a global average condition.

## 10. New counterexample profile

A counterexample to

\[
\beta=1\Longrightarrow\alpha=1
\]

must now satisfy, on every anchored beta-killing orbit,

\[
\boxed{m_D(e)s(e)\ge2.}
\]

Therefore every such orbit must exhibit at least one of two forms of excess structure:

1. **replacement multiplicity:**
   \[
   m_D(e)\ge2;
   \]
2. **stabilizer splitting:**
   \[
   s(e)=[A_e:H_e]\ge2.
   \]

So the remaining obstruction is no longer merely “large shell”. It is the much sharper statement that **every killing orbit must have replacement weight at least two**.

This suggests the next target:

> prove that beta one forces at least one anchored killing orbit with replacement weight `w=1`.

Such an orbit would immediately give a safe singleton repair.

## 11. Claim firewall

1. The naive fixed-point/shell monotonicity is explicitly false.
2. The star family above is used only to refute that heuristic; it is not claimed to be a beta-one counterexample family.
3. The weighted capacity theorem is theorem-level.
4. `m_D(e)s(e)>=2` is necessary for fatality, not sufficient.
5. The global theorem `beta=1 => alpha=1` remains open.
