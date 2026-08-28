# Prepublication Audit — FCOA Value-Rigidity / Identity Digraphs

**Audit date:** 2026-08-29  
**Target format:** bilingual Commander Sol / Zenodo companion note (strict proofs, expository framing)  
**Verdict:** **READY FOR PUBLICATION AFTER DOI/METADATA INSERTION** in the companion-note / Reflections category; **NOT READY for any claim that the classical minimum-size identity-digraph problem itself is new.**

## 1. Scope audited

The publication package consolidates the research chain:

1. one-output collapse for pure terminal-output partial operations;
2. two-output maximal Value-Rigidity Index (VRI);
3. reduction of the sparsest maximally rigid two-output fiber to a minimum-size identity digraph;
4. exact finite threshold formula for `m(n)` in terms of identity oriented-tree counts;
5. second-order asymptotics derived from the generating function;
6. bounded partial-layer phase oscillation and nonexistence of a universal denominator constant `K_0`;
7. an exact calculator based on the rooted/unrooted identity-oriented-tree recurrence.

## 2. Prior-art audit

### Classical material — must be attributed

The following are **not novelty claims** of FCOA:

- Frank Harary and Robert W. Robinson, *Identity Digraphs of Minimum Size*, Congressus Numerantium 152 (2001), 139–147. Available bibliographic/abstract records explicitly state that the minimum size `sigma(n)` is determined efficiently and that `sigma(n)=n-delta(n)` with `delta(n)=Theta(n/log n)`.
- Frank Harary and Michael S. Jacobson, *Destroying symmetry by orienting edges: complete graphs and complete bigraphs*, Discussiones Mathematicae Graph Theory 21 (2001), 149–158, DOI `10.7151/dmgt.1139`. The paper relates complete-graph symmetry destruction to identity oriented forests/trees.
- Rodica Simion, *Trees with 1-factors and oriented trees*, Discrete Mathematics 88 (1991), 93–104, DOI `10.1016/0012-365X(91)90061-6`, supplies classical enumeration links for oriented-tree species.
- OEIS A102755 records the number of asymmetric/identity oriented trees, the relation `A(x)=B(x)-B(x)^2`, and the numerical constants used for validation.
- The distinguishing-index literature treats symmetry breaking by edge colourings; in particular, Kalinowski and Pilśniak, *Distinguishing graphs by edge-colourings*, European Journal of Combinatorics 45 (2015), 124–131, DOI `10.1016/j.ejc.2014.11.003`.

### Safe FCOA contribution statement

The publication does **not** claim priority for identity digraphs, asymmetric oriented trees, distinguishing colourings, or the `Theta(n/log n)` minimum-size scale.

The defensible contribution is:

- the FCOA formulation separating domain symmetry from value-fiber symmetry through the active-sort index
  `VRI=[Aut(D):pi Aut(star)]`;
- the exact one-output versus two-output threshold in that formulation;
- the identification of the sparsest maximally value-rigid two-output layer with the classical minimum identity-digraph problem;
- a self-contained derivation of the leading and logarithmic corrections from the rooted identity-oriented-tree functional equation;
- the explicit partial-layer phase law showing that the bounded denominator correction does not converge to a single constant.

No priority claim is made for the last two deductions until a full historical comparison with the complete Harary–Robinson text and subsequent literature is possible.

## 3. Proof-completeness audit

### PASS — One-output collapse

If the terminal alphabet is a singleton `{Omega}`, then the operation is equivalent to its domain indicator. Every domain automorphism extends uniquely over the terminal output, so active-sort VRI is exactly 1. Proof is elementary and complete.

### PASS — Two-output maximum VRI

On `n>=3` active points, use complete off-diagonal definedness and color a rigid directed Hamilton path with one output, its complement with the other. The unequal fiber sizes prevent output exchange and the path has trivial stabilizer. Hence the full operation is rigid while the definedness group is `S_n`, giving `VRI=n!`, the absolute maximum. Proof is complete.

### PASS — Exact reduction to `m(n)`

For complete off-diagonal definedness, a two-output operation is rigid whenever one fiber `F` has trivial `S_n` stabilizer and no permutation carries `F` to its complement. At the minimum, `|F|=m(n)<=n-1<n(n-1)/2` for `n>=3`, so complement exchange is impossible by cardinality. Thus the minimum number of special cells for maximum active-sort VRI is exactly the classical minimum identity-digraph size `m(n)`. Proof is complete.

### PASS — Exact finite threshold formula

Let `a_k` count nonisomorphic identity oriented trees of order `k`, with

`A_K=sum_{j<=K} a_j`, `W_K=sum_{j<=K} j a_j`.

For the unique `K` satisfying `W_{K-1}<=n<W_K`, put

`q=floor((n-W_{K-1})/K)`.

Then

`delta(n)=n-m(n)=A_{K-1}+q`.

Upper bound: every weak component contributes at most 1 to `n-|F|`; equality occurs only for an oriented tree. Identity forces all positive-deficit tree components to be identity and pairwise nonisomorphic, so the cheapest `t` such components are the smallest available tree types.

Lower bound: take all types below `K`, any `q` types of order `K`, and absorb the remainder `<K` by replacing one retained component by a longer directed path of fresh order. This preserves component count and identity. Proof is complete.

### PASS — Enumerative asymptotic no longer taken on faith from OEIS

The publication manuscript proves the `n^{-5/2}` law from the rooted functional equation

`B(z)=z exp(2 sum_{r>=1} (-1)^(r+1) B(z^r)/r)`.

Writing

`H(z)=2 sum_{r>=2} (-1)^(r+1) B(z^r)/r`,

the equation becomes

`B=z exp(2B+H)`.

The dominant positive singularity `rho` is characterized by `B(rho)=1/2`; `H` is analytic at `rho` because `rho<1`. The smooth implicit-function singularity gives

`B(z)=1/2-beta X+(2/3)beta^2 X^2+O(X^3)`, `X=sqrt(1-z/rho)`, `beta>0`.

Since the unrooted series is `A=B-B^2`, the square-root term cancels and

`A(z)=analytic +(4/3)beta^3(1-z/rho)^(3/2)+O((1-z/rho)^2)`.

Transfer gives

`a_k ~ c lambda^k k^(-5/2)`,

where `lambda=rho^(-1)` and `c=beta^3/sqrt(pi)>0`.

Thus the publication no longer promotes an OEIS numerical asymptotic without proof; OEIS is used only to validate numerical constants and coefficients.

### PASS — Second-order and phase laws

From the proven exponential-polynomial tree asymptotic, geometric-tail summation and exact threshold packing yield

`n-m(n)=L n/[log n+(3/2)log log n+O(1)]`, `L=log lambda`.

The final layer contains a nonvanishing fraction of all cheaper types. Parameterizing its occupation by `theta in [0,1]` yields the explicit phase

`Phi(theta)=-(3/2)log L-log c-log(r+theta)-L u/(r+theta)`,

where `r=1/(lambda-1)` and `u=lambda/(lambda-1)^2`.

Hence the normalized bounded correction has multiple subsequential limits, so no universal constant `K_0` exists. The exact finite threshold theorem removes the previous conditional wording about the packing characterization.

## 4. Computational audit

### PASS — sequence generation

The repository calculator `experiments/fcoa_identity_exact_m.py` generates rooted coefficients from the functional equation and obtains unrooted counts from `A=B-B^2`. Its prefix matches OEIS A102755:

`1,1,1,4,10,37,135,522,2060,8430,35115,149286,...`.

### PASS — independent small-case check

Direct exhaustive enumeration of loopless directed relations gives:

- `m(1)=0`;
- `m(2)=1`;
- `m(3)=1`;
- `m(4)=2`;
- `m(5)=3`.

These agree with the threshold formula.

### PASS — large exact values

Independent recurrence/threshold evaluation reproduces:

- `m(10)=6`;
- `m(1000)=846`;
- `m(10^6)=911561`;
- `m(10^12)=950477504026`.

## 5. Sorting / one-sorted audit

The manuscript makes the primary VRI statement on the active/base sort. In one-sorted presentations, terminal outputs are recoverable when active elements occur as operation arguments and terminal elements do not. Full one-sorted automorphism ratios are explicitly separated from active-sort VRI. **PASS.**

## 6. Claim-discipline audit

- No claim that `m(n)` or identity digraphs were discovered by FCOA. **PASS.**
- No claim that distinguishing colorings are new. **PASS.**
- No arithmetic or number-theoretic import. **PASS.**
- No theorem is included without a proof or an explicitly cited standard analytic transfer principle whose hypotheses are checked. **PASS.**
- Numerical constants are labeled as numerical evaluations of analytically defined constants. **PASS.**

## 7. Publication classification

### Recommended

Publish as a **Commander Sol / FCOA companion note or “Reflections” paper**, with the classical graph-theory results prominently credited and the main purpose stated as structural translation and refinement.

Suggested English title:

**Reflections on Value-Rigidity with Commander Sol: Two Anonymous Outputs, Identity Digraphs, and Sparse Rigid Fibers**

Suggested Russian title:

**Размышлизмы о ценностной жёсткости с Commander Sol: два анонимных выхода, identity-орграфы и разреженные жёсткие волокна**

### Not recommended

Do not market the paper as a discovery of the minimum-size identity-digraph problem, its exact finite computation, or the classical `Theta(n/log n)` scale.

## 8. Remaining release gate

Mathematical and bibliographic publication threshold: **PASSED**.

Only release metadata remains:

- assign/fill Zenodo DOI;
- freeze release date/version;
- insert author/ORCID metadata according to project convention;
- render PDF/DOCX/HTML only after those metadata are fixed.

The current repository state is therefore **publication-ready, pending DOI metadata only**.
