# FCOA Rigidity Cost — Component Compensation Bound

**Status:** post-publication theorem note.

## 1. Setup
Let `Lambda(D)` be the ordered-cell incidence graph of the old sparse domain `D`. For an old cell `p in D`, define the deletion defect

\[
\Delta_D(p)=\kappa(\Lambda(D\setminus\{p\}))-\kappa(\Lambda(D)),
\]

where `kappa` denotes the number of connected components.

For a missing cell `e notin D` and a candidate replacement `p in D`, let

\[
r_{D-p}(e)
\]

be the number of connected components of `Lambda(D\setminus\{p\})` which contain at least one neighbour of `e` in the enlarged incidence graph obtained by adding `e`.

## 2. Exact component compensation identity

### Theorem 2.1
If

\[
D' = D\setminus\{p\}\cup\{e\}
\]

is carrier-isomorphic to `D`, then

\[
\boxed{
r_{D-p}(e)=1+\Delta_D(p).}
\]

### Proof
Adding one new vertex `e` to `Lambda(D-p)` and joining it to exactly `r=r_{D-p}(e)` connected components changes the component count by `1-r`. Hence

\[
\kappa(\Lambda(D'))
=
\kappa(\Lambda(D-p))+1-r.
\]

Since `D'` is carrier-isomorphic to `D`, their incidence graphs are isomorphic and have the same component count. Therefore

\[
\kappa(\Lambda(D))
=
\kappa(\Lambda(D-p))+1-r,
\]

which rearranges to the formula. `square`

## 3. Replacement targets must be articulation-compatible
For a missing cell `e`, define

\[
R_e=\{p\in D: D-p+e\in S_G\cdot D\}.
\]

Then

\[
\boxed{m_D(e)=|R_e|.}
\]

Theorem 2.1 gives the exact restriction

\[
\boxed{
R_e\subseteq\{p\in D:\Delta_D(p)=r_{D-p}(e)-1\}.
}
\]

Thus every replacement target must compensate exactly the component merging caused by `e`.

## 4. Multi-component touch bound
Let

\[
t_D(e)
\]

be the number of connected components of `Lambda(D)` touched by `e`.

Deleting one old cell can affect only the old component containing that cell. Hence for every `p in R_e`,

\[
r_{D-p}(e)\ge t_D(e)-1.
\]

Therefore

\[
\boxed{\Delta_D(p)\ge t_D(e)-2.}
\]

for every replacement target `p`.

Consequently

\[
\boxed{
m_D(e)
\le
|\{p\in D:\Delta_D(p)\ge t_D(e)-2\}|.}
\]

This converts replacement multiplicity into an articulation-count bound.

## 5. Robust-touch refinement
Call a touched old component `C` **robust for e relative to p** if `e` has a neighbour in `C` other than `p`. If every one of the `t_D(e)` touched components is robust relative to `p`, then deleting `p` does not erase any touched component from the neighbour set of `e`, so

\[
r_{D-p}(e)\ge t_D(e).
\]

Hence every such replacement target satisfies

\[
\boxed{\Delta_D(p)\ge t_D(e)-1.}
\]

In particular, if `e` robustly touches two old incidence components, any replacement target must be a genuine articulation cell:

\[
\boxed{\Delta_D(p)\ge1.}
\]

## 6. Immediate zero-multiplicity criteria

### Corollary 6.1
If `e` touches at least three old incidence components and no old cell satisfies

\[
\Delta_D(p)\ge t_D(e)-2,
\]

then

\[
\boxed{m_D(e)=0.}
\]

### Corollary 6.2
If `e` robustly touches two old components and `Lambda(D)` has no articulation cells, then

\[
\boxed{m_D(e)=0.}
\]

### Corollary 6.3
More generally, if every old incidence component is 2-vertex-connected and `e` robustly touches at least two old components, then `e` lies outside the defect-one replacement boundary.

## 7. Consequence for beta-one repair
Suppose `beta(D,c)=1` and `e in W_kill^anch`.

If the component-compensation criterion forces

\[
m_D(e)=0,
\]

then no domain-moving defect-one replacement symmetry can preserve `D union {e}`. Since `e` is anchored and beta-killing, every surviving D-preserving reduct automorphism is globally anonymous. Therefore either binary color on `e` is exact, and

\[
\boxed{\alpha(D,c)=\beta(D,c)=1.}
\]

Thus any beta-one counterexample must satisfy, for every anchored killing cell,

\[
\boxed{m_D(e)\ge1.}
\]

Combining with the weighted capacity theorem, a fully fatal anchored killing orbit must in fact satisfy

\[
\boxed{m_D(e)[A_e:H_e]\ge2.}
\]

## 8. Articulation budget
Define

\[
N_j(D)=|\{p\in D:\Delta_D(p)\ge j\}|.
\]

Then for every missing cell touching `t` old components,

\[
\boxed{m_D(e)\le N_{t-2}(D),}
\]

and under robust touch,

\[
\boxed{m_D(e)\le N_{t-1}(D).}
\]

This provides a direct bridge between the component geometry of `Lambda(D)` and the replacement weight appearing in Orbit–Killing Duality.

## 9. Structural interpretation
A defect-one replacement can imitate a phase-bridging repair only if deletion of one old operation cell creates exactly enough incidence-component freedom to compensate the components merged by the new cell.

Hence replacement danger is concentrated on articulation-rich sparse domains. In articulation-poor domains, multi-component beta-killing bridges automatically escape the replacement boundary and are safe.

## 10. Next target
The remaining hard sector is now forced toward domains where `Lambda(D)` contains enough articulation cells to support every anchored killing cell. The next natural target is an **Articulation–Killing Duality**:

> show that if articulation mass is large enough to give `m_D(e)>=1` (or weighted capacity >=2) on every anchored beta-killing orbit, then the same articulation geometry produces additional beta-killing cells or lowers the stabilizer splitting factor.

That would close another broad class of the beta-one problem.

## Claim firewall
1. The component compensation identity is exact.
2. The multi-component and robust-touch inequalities are necessary conditions for replacement, not sufficient conditions.
3. Zero multiplicity immediately gives a safe anchored beta-one repair.
4. No global proof of `beta=1 => alpha=1` is claimed here.
