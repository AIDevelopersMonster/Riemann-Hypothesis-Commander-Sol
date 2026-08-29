# Threshold Compression Calibration — Density Is Not Arithmetic Leakage

**Project:** FCOA Admissibility Geometry  
**Status:** classical calibration + saved central consequence  
**Scope:** no new FCOA operation cells; external functions are benchmarks, not proposed internal arithmetic

## 1. Why this matters

The Arithmetic Leakage programme currently asks for the cheapest mechanism that leaves the exact G4-A order wall, and separately for the cheapest mechanism that reaches full additive leakage.

A useful external calibration is obtained by importing a unary function \(f\) only as a benchmark and forming the threshold relation

\[
R_f(x,y)\iff f(x)\le y.
\]

This immediately exposes two independent axes which must not be conflated:

1. **interaction-support growth / compression** — how many ordered pairs satisfy the relation on the first \(N\) points;
2. **logical leakage** — what arithmetic becomes definable over the chosen background signature.

The central lesson is:

\[
\boxed{
\text{support density does not determine arithmetic leakage.}
}
\]

## 2. Exact square-threshold count

Take

\[
f(x)=x^2
\]

on \(\{1,\ldots,N\}\), and define

\[
R_2(x,y)\iff x^2\le y.
\]

Let

\[
m=\lfloor\sqrt N\rfloor.
\]

For each \(1\le x\le m\), the admissible values of \(y\) are

\[
x^2,x^2+1,\ldots,N,
\]

so their number is

\[
N-x^2+1.
\]

Therefore

\[
|R_2\cap[N]^2|
=
\sum_{x=1}^{m}(N-x^2+1)
\]

and hence

\[
|R_2\cap[N]^2|
=
m(N+1)-\frac{m(m+1)(2m+1)}6.
\]

Using \(m=\sqrt N+O(1)\),

\[
\boxed{
|R_2\cap[N]^2|
=
\frac23N^{3/2}+O(N).
}
\]

Thus a threshold relation carrying a nonlinear external scale can have genuinely subquadratic support:

\[
\boxed{
|R_2|=\Theta(N^{3/2}).
}
\]

This is **support-size compression**, not by itself an information-theoretic claim about arbitrary binary relations.

## 3. General polynomial thresholds

For fixed integer \(d\ge2\), let

\[
R_d(x,y)\iff x^d\le y.
\]

Then, with \(M=\lfloor N^{1/d}\rfloor\),

\[
|R_d\cap[N]^2|
=
\sum_{x=1}^{M}(N-x^d+1).
\]

The standard power-sum asymptotic gives

\[
\boxed{
|R_d\cap[N]^2|
=
\frac{d}{d+1}N^{1+1/d}
+O(N).
}
\]

Hence the support exponent is

\[
1+\frac1d<2.
\]

As \(d\to\infty\), these exponents approach the linear boundary.

For exponential thresholds such as

\[
R_{\exp}(x,y)\iff 2^x\le y,
\]

one obtains instead

\[
|R_{\exp}\cap[N]^2|=\Theta(N\log N).
\]

So very sparse threshold geometry can still retain a global nonlinear scale.

## 4. Threshold relation and unary function are interdefinable over order

On the standard discrete natural-number order, if

\[
R_f(x,y)\iff f(x)\le y,
\]

then the graph of \(f\) is definable from \((<,R_f)\) by taking the least threshold point:

\[
f(x)=y
\iff
R_f(x,y)
\land
\neg\exists z\,(z<y\land R_f(x,z)).
\]

Conversely, \(R_f\) is immediately definable from \((<,f)\):

\[
R_f(x,y)\iff f(x)\le y.
\]

Thus, for this calibration,

\[
\boxed{
(<,R_f)
\quad\text{and}\quad
(<,f)
\text{ are first-order interdefinable.}
}
\]

The threshold relation is therefore a sparse relational encoding of the imported unary scale.

## 5. Semenov square calibration

A. L. Semenov's 1984 paper `Logical theories of one-place functions on the set of natural numbers` explicitly gives the following calibration:

\[
\boxed{
\operatorname{Th}(\mathbb N;<,x\mapsto x^2)
\text{ is decidable,}
}
\]

whereas

\[
\boxed{
\operatorname{Th}(\mathbb N;+,x\mapsto x^2)
\text{ is undecidable.}
}
\]

In Semenov's terminology, squaring is effectively compatible with order but not with addition.

The second statement is also transparent from definability. With addition and squaring,

\[
z=xy
\]

is definable by

\[
(x+y)^2=x^2+y^2+z+z.
\]

Therefore multiplication is recovered and full arithmetic strength appears.

By Section 4 the same contrast applies if the square function is supplied through the threshold relation \(R_2(x,y)\iff x^2\le y\).

Thus the **same subquadratic relation** can be tame over order and explosive over an additive background.

## 6. Growth rate alone is not the criterion

The phenomenon must not be summarized as “fast growth causes decidability over order and undecidability over addition.” Semenov's results are subtler.

For example, the exponential function

\[
x\mapsto2^x
\]

is effectively compatible with addition in Semenov's sense, and the expansion

\[
(\mathbb N;+,2^x)
\]

is decidable.

Thus:

\[
\boxed{
\text{logical strength depends on the function/background interaction, not growth rate alone.}
}
\]

This is particularly relevant for FCOA, where the same operation cell or value can have different structural force depending on the surrounding signature and available recovery mechanisms.

## 7. Concrete intermediate layer beyond the order wall

The square calibration shows that the intermediate zone between pure order and additive leakage is not merely a hypothetical modular/counting layer.

There are natural nonlinear unary enrichments whose theory over order remains decidable while they are not intended to be treated as addition.

Accordingly, the central leakage map should be read broadly:

- **AL0:** exact G4-A order wall, generic uniform FO power exactly FO[<];
- **AL-INT:** intermediate non-order enrichment, potentially including modular/counting predicates, sparse unary scales, threshold geometries, or other structures not yet recovering addition;
- **AL1:** full additive gateway, represented canonically by EqGap / truncated rank addition;
- **AL2:** full-arithmetic gateway.

`AL-INT` is a working umbrella, not a claim that all intermediate enrichments have the same expressive strength.

## 8. Density-Leakage Orthogonality

This calibration motivates keeping a separate support-growth invariant.

For a family of binary relations \(R_N\subseteq[N]^2\), define the working support exponent

\[
\gamma(R)
=
\limsup_{N\to\infty}
\frac{\log |R_N|}{\log N}.
\]

Then

\[
\gamma(R_{x^d})=1+\frac1d,
\]

while the exponential threshold has exponent \(1\) with an \(N\log N\) correction.

This invariant measures only support growth. It does **not** classify logical strength.

The square example gives

\[
\gamma(R_2)=\frac32
\]

both when the relation is considered over order and when the same relation is placed over an additive background, despite the dramatic change in definability strength.

Hence:

\[
\boxed{
\text{support-growth complexity and arithmetic-leakage complexity are orthogonal axes.}
}
\]

## 9. Consequence for FCOA optimization

A single scalar notion of “cheapest extension” is therefore unsafe.

Future FCOA candidates should be compared by a cost vector including at least:

\[
\boxed{
(
\text{domain/support growth},
\text{output alphabet},
\text{anchor cost},
\text{arity},
\text{background signature},
\text{logical leakage level},
\text{external-import cost}
).
}
\]

The last coordinate is essential. The threshold examples deliberately import \(x^2\), \(x^d\), or \(2^x\) externally. They are **benchmarks**, not accepted solutions to the FCOA search for internally generated structure.

## 10. New central questions suggested by the calibration

The external examples suggest three distinct questions:

1. Can an FCOA-native domain/value mechanism produce subquadratic support growth without importing a numerical function?
2. Can such a mechanism genuinely leave FO[<] while remaining below EqGap/addition?
3. Can two mechanisms with comparable support exponent have radically different arithmetic leakage because of their interaction with the background FCOA signature?

These questions sharpen, but do not replace, the current main-line Arithmetic Leakage programme.

## 11. Status

The pair-count asymptotics are elementary and fixed.

The logical calibration is classical: Semenov proves decidability results for broad classes of monotone unary functions and explicitly notes the contrast between squaring over order and squaring over addition.

The FCOA interpretation of this calibration — `Density-Leakage Orthogonality`, the support exponent \(\gamma\), and the multi-axis cost vector — is working terminology / programme design only.

\[
\boxed{
\mathbf F:\ \text{threshold pair counts and classical square/order-vs-addition calibration}
}
\]

\[
\boxed{
\mathbf W:\ \text{Density-Leakage Orthogonality terminology and FCOA cost-vector programme}
}
\]
