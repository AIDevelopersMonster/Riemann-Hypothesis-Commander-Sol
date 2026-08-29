# Reflections on Value-Rigidity with Commander Sol: Two Anonymous Outputs, Identity Digraphs, and Sparse Rigid Fibers

**Alex Malachevsky · Commander Sol**  
**Version:** 1.0-preprint  
**Date:** 2026-08-29  
**Status:** publication-ready companion note; DOI metadata pending

## Abstract

We study how much symmetry can be destroyed by the **values** of a finite partial operation once its domain of definition is fixed. For a partial operation `star` on an active carrier `X`, let `D_star` denote its definedness relation and define the active-sort Value-Rigidity Index

`VRI(star)=[Aut(D_star|X):pi_X Aut(star)]`.

A singleton terminal-output alphabet carries no value information beyond definedness: `|O|=1` forces `VRI=1`. In sharp contrast, two anonymous terminal outputs suffice to attain the absolute maximum `VRI=n!` on `n` active points. The extremal construction colors a rigid directed relation with one output and its complement with the other while leaving definedness maximally symmetric.

This reduces the problem of minimizing the number of specially colored cells in a maximally value-rigid two-output operation to the classical minimum-size identity-digraph problem. Using the classical identity-oriented-tree decomposition, we give a self-contained exact threshold formula for the extremal size, derive its second-order asymptotics from the rooted identity-oriented-tree generating function, and identify a nonvanishing partial-layer phase oscillation which prevents the bounded denominator correction from converging to a universal constant.

The graph-theoretic minimum-size identity-digraph problem, identity oriented trees, and distinguishing edge colorings are classical; no priority claim is made for them. The purpose of this note is the FCOA translation: domain symmetry versus value-fiber symmetry, the exact one-output/two-output threshold for value-induced rigidity, and the resulting bridge to classical identity-digraph extremals.

## 1. Domain symmetry versus value symmetry

Let `X` be a finite active set and `O` a disjoint terminal-output set. A pure terminal partial operation is a partial map

`star : X x X partial-> O`.

Its definedness relation is

`D_star(x,y) <=> Def(x star y)`.

We measure only the symmetry lost **after the domain has already been fixed**.

### Definition 1.1 — Value-Rigidity Index

Let `pi_X Aut(star)` be the action induced by full operation automorphisms on `X`. Define

`VRI(star)=[Aut(D_star|X):pi_X Aut(star)]`.

Thus `VRI=1` means that values destroy no additional active-sort symmetry beyond definedness.

## 2. One output cannot create value-rigidity

### Theorem 2.1 — One-Output Collapse

If `O={Omega}`, then

`pi_X Aut(star)=Aut(D_star|X)`

and therefore

`VRI(star)=1`.

### Proof

The inclusion `pi_X Aut(star) <= Aut(D_star|X)` is automatic because every operation automorphism preserves the operation domain.

Conversely, let `g in Aut(D_star|X)`. Since the terminal sort contains only `Omega`, the only possible action on `O` fixes `Omega`. For every `(x,y)` we have

`x star y = Omega <=> D_star(x,y)`.

Because `g` preserves `D_star`, `(x,y)` is defined exactly when `(gx,gy)` is defined; whenever defined, both values are `Omega`. Hence `g` extends uniquely to an automorphism of `star`. Therefore the two active-sort groups coincide. ∎

### Corollary 2.2

A one-output layer may rigidify a structure through the **geometry of its domain**, but it cannot produce any incremental value-induced rigidity.

## 3. Two outputs attain maximal VRI

Let `X_n={x_1,...,x_n}`, `n>=3`, and let

`O={Omega_+,Omega_-}`.

Define the operation on every off-diagonal pair, so

`D(x_i,x_j) <=> i != j`.

Hence

`Aut(D|X_n) ~= S_n`.

Choose a rigid directed Hamilton path

`F={(x_i,x_{i+1}):1<=i<n}`.

Set

- `x_i star x_j=Omega_+` for `(x_i,x_j) in F`;
- `x_i star x_j=Omega_-` for every other off-diagonal pair.

### Theorem 3.1 — Two-Output Maximum VRI

For every `n>=3`, the above operation satisfies

`Aut(star)=1`

and

`VRI(star)=n!`.

### Proof

The two value fibers have sizes

`|F|=n-1`

and

`n(n-1)-(n-1)=(n-1)^2`.

For `n>=3` these sizes differ, so no automorphism can exchange the two terminal outputs. Thus every operation automorphism preserves `F` setwise. But `F` is a directed path and has trivial automorphism group. Hence every active point is fixed and `Aut(star)=1`.

Since `Aut(D|X_n)=S_n`, the index is `n!`. No active-sort VRI on `n` points can exceed `n!`, so the bound is sharp. ∎

### Corollary 3.2 — Exact output-cardinality threshold

In the pure terminal-output setting:

- one terminal output implies `VRI=1`;
- two anonymous terminal outputs already permit maximal `VRI=n!`.

Thus two terminal outputs are simultaneously minimal for nontrivial value-rigidity and sufficient for the absolute maximum.

## 4. Sparse maximally rigid fibers

The preceding construction uses `n-1` cells in the small fiber `F`. This raises the extremal question

`m(n)=min{|F| : F subset X_n^2\Delta, Stab_{S_n}(F)=1}`.

This is exactly the classical minimum-size identity-digraph problem: `F` is a loopless digraph relation with trivial automorphism group.

For `n>=3`, a minimum such `F` has `|F|<=n-1<n(n-1)/2`. Therefore `F` and its complement inside the complete off-diagonal domain have different cardinalities. Consequently, using `F` as one value fiber and the complement as the other gives a two-output operation whose outputs cannot be exchanged. Hence the minimum number of special cells needed for maximal two-output VRI is precisely `m(n)`.

The graph-theoretic problem itself is classical and is credited below.

## 5. Why identity oriented trees control `n-m(n)`

Let an identity digraph `G` have weak components `C_i`. Write

`v_i=|V(C_i)|`, `a_i=|A(C_i)|`.

Weak connectivity implies

`a_i>=v_i-1`,

so

`v_i-a_i<=1`.

Equality holds precisely when `C_i` is an oriented tree: a connected underlying graph with `v_i-1` edges and no antiparallel pair.

Because the whole digraph is identity:

1. each weak component is identity;
2. no two weak components are isomorphic.

Therefore every positive unit of

`delta(n)=n-m(n)`

must come from a distinct identity oriented-tree component.

Let

`a_k = number of nonisomorphic identity oriented trees of order k`.

Define cumulative counts and vertex weights

`A_K=sum_{j<=K} a_j`,

`W_K=sum_{j<=K} j a_j`.

## 6. Exact finite threshold formula

Let `K` be the unique integer satisfying

`W_{K-1}<=n<W_K`

and put

`q=floor((n-W_{K-1})/K)`.

### Theorem 6.1 — Exact finite structure

For every positive integer `n`,

`delta(n)=A_{K-1}+q`

and hence

`m(n)=n-A_{K-1}-floor((n-W_{K-1})/K)`.

### Proof

**Upper bound.** Any weak component contributes at most one to `n-|A(G)|`, and a contribution of one requires an identity oriented tree. To obtain `t` positive units one therefore needs `t` distinct identity oriented-tree types. The least possible vertex cost of `t` such types is obtained by taking them in nondecreasing order of size. Before order `K`, all available types cost `W_{K-1}` vertices and provide `A_{K-1}` units; each further unit costs at least `K` vertices. Therefore no order-`n` identity digraph can have deficit exceeding `A_{K-1}+q`.

**Construction.** Take every identity oriented-tree type of order `<K` and any `q` distinct types of order `K`. They use

`N_0=W_{K-1}+qK`

vertices and have exactly `A_{K-1}+q` components. Let `r=n-N_0`, so `0<=r<K`. If `r=0` we are done. If `r>0`, replace one retained tree component by a longer directed path of a fresh order obtained by adding `r` vertices. A directed path is identity; choosing a fresh order keeps all components pairwise nonisomorphic. Vertices and arcs both increase by `r`, so the deficit is unchanged. Thus the upper bound is attained. ∎

### Algorithmic consequence

Once the counts `a_k` are known, exact evaluation of `m(n)` is a threshold scan, not a general subset-sum problem.

## 7. Rooted generating function and exact recurrence

Let

`B(z)=sum_{n>=1} b_n z^n`

be the generating function for rooted identity oriented trees. The classical species decomposition gives

`B(z)=z product_{j>=1}(1+z^j)^(2b_j)`

or equivalently

`B(z)=z exp(2 sum_{r>=1} (-1)^(r+1) B(z^r)/r)`.

For unrooted identity oriented trees,

`A(z)=B(z)-B(z)^2`,

so

`a_n=b_n-sum_{i=1}^{n-1}b_i b_{n-i}`.

Define

`s_m=2 sum_{d|m} (-1)^(m/d+1) d b_d`.

The standard exponential-series recurrence gives

`m b_{m+1}=sum_{k=1}^m s_k b_{m-k+1}`.

This yields exact integer coefficients and reproduces

`1,1,1,4,10,37,135,522,2060,8430,35115,149286,...`

for the unrooted identity oriented-tree counts.

## 8. Self-contained asymptotic derivation

We now derive the coefficient shape needed for the sparsity asymptotics rather than taking it as a numerical OEIS assertion.

Write

`H(z)=2 sum_{r>=2} (-1)^(r+1) B(z^r)/r`.

Then

`B=z exp(2B+H(z))`.

Let `rho` be the dominant positive singularity. Since `rho<1`, the functions `B(z^r)` with `r>=2` are analytic at `rho`, so `H` is analytic there. Set

`F(z,y)=y-z exp(2y+H(z))`.

At the dominant smooth implicit singularity,

`F(rho,tau)=0`, `F_y(rho,tau)=0`.

But

`F_y=1-2z exp(2y+H)`,

and `z exp(2y+H)=y` on the solution curve, hence

`1-2tau=0`,

so

`tau=B(rho)=1/2`.

Moreover `F_{yy}(rho,tau)=-4tau=-2 !=0` and the positive-coefficient structure gives `F_z(rho,tau)!=0`. The smooth implicit-function schema therefore yields a square-root expansion

`B(z)=1/2-beta X+(2/3)beta^2 X^2+gamma X^3+O(X^4)`,

where

`X=sqrt(1-z/rho)`, `beta>0`.

Now

`A=B-B^2 = 1/4-(B-1/2)^2`.

The square-root term cancels. Substituting the expansion gives

`A(z)=analytic +(4/3)beta^3 X^3+O(X^4)`

that is,

`A(z)=analytic +(4/3)beta^3(1-z/rho)^(3/2)+O((1-z/rho)^2)`.

By singularity transfer,

`a_k ~ c lambda^k k^(-5/2)`,

where

`lambda=rho^(-1)`

and

`c=beta^3/sqrt(pi)>0`.

Numerically the recurrence gives

`lambda=5.249032491228170579...`,

`c=0.178071039140784246...`.

## 9. Second-order asymptotics of `m(n)`

Because `a_k` has exponential factor `lambda^k`, the cumulative sums are dominated geometrically by the final layer. Let

`L=log lambda`.

Then

`A_K ~ (lambda/(lambda-1)) c lambda^K K^(-5/2)`

and

`W_K=A_K(K+O(1))`.

At the threshold corresponding to order `n`,

`n asymp lambda^K K^(-3/2)`.

Therefore

`log n = KL-(3/2)log K+O(1)`

and hence

`K=[log n+(3/2)log log n+O(1)]/L`.

Since the number of positive-deficit components is `n/(K+O(1))`, we obtain

### Theorem 9.1 — Second-order sparsity

`n-m(n)= L n/[log n+(3/2)log log n+O(1)]`.

Equivalently,

`m(n)=n-L n/log n+(3/2)L n log log n/(log n)^2+O(n/(log n)^2)`.

Numerically,

`L=1.6580437722354153...`.

## 10. The bounded term does not converge

The `O(1)` term in the denominator is not a hidden universal constant.

Let

`r=1/(lambda-1)`,

`u=lambda/(lambda-1)^2`.

Suppose at size layer `K` we choose a fraction `theta in [0,1]` of the `a_K` available identity oriented-tree types. Then asymptotically

`A_{K-1}/a_K -> r`

and the corresponding weighted deficit satisfies

`R_{K-1}/a_K -> u`,

where

`R_{K-1}=sum_{j<K}(K-j)a_j`.

Define

`E(n)=L n/[n-m(n)]-log n-(3/2)log log n`.

Along a subsequence whose last-layer occupation tends to `theta`, one obtains

`E(n) -> Phi(theta)`

with

`Phi(theta)=-(3/2)log L-log c-log(r+theta)-L u/(r+theta)`.

### Theorem 10.1 — Partial-layer phase oscillation

The function `Phi` is nonconstant, hence `E(n)` does not converge. Therefore no universal constant `K_0` exists for an expansion

`n-m(n)=L n/[log n+(3/2)log log n+K_0+o(1)]`.

### Proof

Differentiate:

`Phi'(theta)=[Lu-(r+theta)]/(r+theta)^2`.

The critical point

`theta_*=Lu-r`

lies strictly inside `(0,1)`. Consequently `Phi` is not constant. In fact

`Phi(0)=Phi(1)=0.3655457832739746...`

while

`Phi(theta_*)=0.6968154130981610...`.

Thus two subsequences yield different bounded corrections. ∎

The correct phase-sensitive form is therefore

`n-m(n)=L n/[log n+(3/2)log log n+Phi(theta_n)+o(1)]`,

where `theta_n` records the fractional occupation of the current extremal layer.

## 11. Computational verification

The repository script

`experiments/fcoa_identity_exact_m.py`

implements the rooted recurrence and exact threshold formula using arbitrary-precision integers.

It reproduces the initial identity-oriented-tree counts and gives, for example,

- `m(10)=6`;
- `m(1000)=846`;
- `m(10^6)=911561`;
- `m(10^12)=950477504026`.

Direct exhaustive enumeration of loopless directed relations independently gives

`m(1)=0, m(2)=1, m(3)=1, m(4)=2, m(5)=3`,

in agreement with the threshold formula.

## 12. One-sorted caveat

The VRI in this note is an active-sort invariant. In a one-sorted realization containing both active points and terminal outputs, one must distinguish active-sort automorphisms from symmetries created by isolated output elements after value erasure.

In the two-output construction above, active elements occur as operation arguments whereas terminal outputs do not, so the active/output partition is internally recoverable. The active-sort VRI remains the quantity relevant to value-induced rigidity.

## 13. What is classical and what is FCOA-specific

The following are classical and are **not** claimed as new:

- identity/asymmetric digraphs;
- minimum-size identity digraphs;
- identity oriented trees and their enumeration;
- distinguishing colorings and symmetry destruction by edge orientations;
- the classical `Theta(n/log n)` scale for minimum-size identity digraphs.

The FCOA-specific contribution is the structural translation:

1. separate domain symmetry from value-fiber symmetry;
2. quantify the latter by VRI;
3. prove the exact one-output/two-output threshold in this formulation;
4. identify the sparsest maximally value-rigid two-output layer with the classical identity-digraph extremal;
5. derive the exact threshold, second-order asymptotics, and phase law in a unified value-rigidity language.

Priority is **not claimed** for the exact threshold or phase law until full historical comparison with the complete classical literature is completed.

## 14. References

1. F. Harary and R. W. Robinson, **Identity Digraphs of Minimum Size**, *Congressus Numerantium* 152 (2001), 139–147.
2. F. Harary and M. S. Jacobson, **Destroying symmetry by orienting edges: complete graphs and complete bigraphs**, *Discussiones Mathematicae Graph Theory* 21 (2001), 149–158. DOI: `10.7151/dmgt.1139`.
3. R. Simion, **Trees with 1-factors and oriented trees**, *Discrete Mathematics* 88 (1991), 93–104. DOI: `10.1016/0012-365X(91)90061-6`.
4. R. Kalinowski and M. Pilśniak, **Distinguishing graphs by edge-colourings**, *European Journal of Combinatorics* 45 (2015), 124–131. DOI: `10.1016/j.ejc.2014.11.003`.
5. OEIS A102755, **Number of asymmetric oriented trees with n nodes**.
6. OEIS A005753, rooted asymmetric oriented-tree sequence used by the functional equation.

## 15. Reproducibility

Repository:

`AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol`

Exact calculator:

`experiments/fcoa_identity_exact_m.py`

Prepublication audit:

`papers/FCOA-VALUE-RIGIDITY-IDENTITY-DIGRAPHS/PREPUBLICATION_AUDIT.md`

---

**Release note.** Mathematical content is frozen for v1.0. Zenodo DOI, final release date, and publication metadata are intentionally left to the release record and should be inserted without changing theorem statements.
