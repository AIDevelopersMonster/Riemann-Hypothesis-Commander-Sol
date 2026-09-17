# FCOA Hybrid Memory — Linear Cost of AL1 via CRT Coordinates

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** theorem candidate; constructive upper bound proved; asymptotic lower bound inherited from bounded-arity cell accounting  
**External calibration:** Chinese remainder representation and the standard finite-model-theory fact that arithmetic can be defined from suitable numerical predicates are background only; the construction below is explicit.

## 1. Question

The Sparse Order Wall established exact AL0 with `Theta(N)` operation-cell resources. The next question was whether the transition

\[
AL0\to AL1
\]

requires a superlinear increase.

It does not.

## 2. Two-modulus representation

Let the target data sector be

\[
X_N=\{0,1,\ldots,N-1\}.
\]

Choose two coprime integers `p_N,q_N` satisfying

\[
p_Nq_N>2N
\]

and

\[
p_N,q_N=\Theta(\sqrt N).
\]

For example, for all sufficiently large `N`, Bertrand's postulate supplies distinct primes in two fixed intervals of lengths comparable to `sqrt N`; finite exceptional values can be handled separately.

Introduce residue sorts

\[
R_p=\mathbb Z/p_N\mathbb Z,
\qquad
R_q=\mathbb Z/q_N\mathbb Z.
\]

For every `x\in X_N`, store its two residues

\[
\rho_p(x)=x\bmod p_N,
\qquad
\rho_q(x)=x\bmod q_N.
\]

This uses exactly `2N` functional incidence records.

## 3. Modular addition tables

On each residue sort store cyclic addition:

\[
A_p(a,b,c)\iff a+b\equiv c\pmod {p_N},
\]

\[
A_q(a,b,c)\iff a+b\equiv c\pmod {q_N}.
\]

Each ordered pair of residues determines exactly one sum, so the number of table entries is

\[
p_N^2+q_N^2=\Theta(N).
\]

Thus the complete residue-memory layer has linear size.

## 4. Exact recovery of truncated integer addition

Define

\[
\operatorname{Add}_N(x,y,z)
\]

by the first-order condition that the residues of `z` are the modular sums of the residues of `x` and `y` in both coordinate rings.

Explicitly,

\[
\begin{aligned}
\operatorname{Add}_N(x,y,z)\iff
&\exists a_x,a_y,a_z\in R_p\;\exists b_x,b_y,b_z\in R_q\\
&\rho_p(x)=a_x\land\rho_p(y)=a_y\land\rho_p(z)=a_z\\
&\land A_p(a_x,a_y,a_z)\\
&\land\rho_q(x)=b_x\land\rho_q(y)=b_y\land\rho_q(z)=b_z\\
&\land A_q(b_x,b_y,b_z).
\end{aligned}
\]

Suppose this formula holds. Then

\[
x+y-z\equiv0\pmod {p_N}
\]

and

\[
x+y-z\equiv0\pmod {q_N}.
\]

Since the moduli are coprime,

\[
x+y-z\equiv0\pmod {p_Nq_N}.
\]

But

\[
-(N-1)\le x+y-z\le2N-2,
\]

so

\[
|x+y-z|<2N<p_Nq_N.
\]

The only multiple of `p_Nq_N` in this interval is zero. Therefore

\[
\boxed{x+y=z.}
\]

Conversely ordinary equality `x+y=z` obviously implies both modular equalities.

Hence the formula defines exactly the truncated rank-addition graph on `X_N`.

## 5. EqGap and AL1

Once addition is uniformly definable, directed equal-gap geometry is uniformly definable by

\[
\operatorname{EqGap}(a,b;c,d)
\iff
\exists s\,
\bigl(
\operatorname{Add}(a,s,b)
\land
\operatorname{Add}(c,s,d)
\bigr)
\]

on forward intervals.

Thus the construction reaches at least

\[
\boxed{AL1.}
\]

If the exact AL0 sparse-order scaffold is retained in parallel, the resulting family has both the canonical total order and canonical rank addition.

## 6. Resource count

The extra AL1 layer costs:

- two residue maps: `2N`;
- modular addition table on `R_p`: `p_N^2`;
- modular addition table on `R_q`: `q_N^2`.

Therefore

\[
M_{AL1}=2N+p_N^2+q_N^2=\Theta(N).
\]

Adding the previous exact-AL0 scaffold, also of size `Theta(N)`, preserves the total asymptotic:

\[
\boxed{M_{AL0+AL1}=\Theta(N).}
\]

Thus there is no asymptotic resource jump between order and additive memory in the auxiliary-carrier bounded-arity model.

## 7. Compilation into a fixed partial-operation signature

The residue maps and modular-addition tables are finite relational data of bounded arity.

To compile them into the fixed two-operation FCOA framework, represent each functional or ternary table entry by a bounded-size incidence gadget with an entry-node and fixed role markers for argument/result positions. The number of gadget incidences is a fixed constant multiple of the number of source table entries.

Then apply the same incidence compilation pattern

\[
e\oplus e=\ell(e),
\qquad e\otimes e=r(e)
\]

(or an equivalent fixed-role gadget variant).

Because every source record expands by only `O(1)` cells, the fixed-signature operation cost remains

\[
\boxed{\Theta(N).}
\]

No claim is made here about the optimal leading constant.

## 8. Linear lower bound

The coarse bounded-arity cell lower bound from `ORDER_EMERGENCE_COST.md` applies a fortiori to AL1.

Any structure that uniformly recovers canonical addition on an `N`-point target sector also recovers enough distinctions to prevent two completely untouched target points from remaining exchangeable. With fixed bounded arity, `o(N)` nontrivial cells cannot even touch all but at most one target point.

Therefore

\[
\boxed{M=\Omega(N).}
\]

Together with the CRT construction:

\[
\boxed{
\text{AL1 cell cost}=\Theta(N)
}
\]

in the same auxiliary-carrier bounded-arity accounting model used for the Sparse Order Wall.

This is an asymptotic theorem, not a sharp-constant theorem.

## 9. Why two moduli are enough

The important compression is that addition does not need to be stored on `N` elements directly.

A full truncated addition table on `X_N` has `Theta(N^2)` graph entries. Instead, the pair of residue systems compresses the arithmetic to two coordinate rings of size `Theta(sqrt N)`.

Their full addition tables cost only

\[
\Theta((\sqrt N)^2)+\Theta((\sqrt N)^2)=\Theta(N).
\]

Chinese-remainder uniqueness over a modulus product larger than the full possible error range reconstructs the exact integer sum.

Thus

\[
\boxed{
\text{quadratic arithmetic table}
\rightsquigarrow
\text{two linear-size modular tables}.
}
\]

## 10. Comparison with BIT coding

A standard alternative is to provide a BIT predicate and use a carry-look-ahead first-order definition of addition. Explicit BIT incidence uses `Theta(N\log N)` records.

The two-modulus construction is asymptotically sparser because residue addition has no carry propagation: each coordinate combines independently. This is the classical computational advantage of residue-number systems, now used as an FCOA memory-compression device.

The standard fact that FO with BIT can define addition is background calibration, not needed for the CRT proof itself.

## 11. What is not yet proved

The present construction proves the cost of **reaching AL1**, not that the resulting scaffold is exactly AL1 rather than accidentally AL2.

The residue rings carry extra modular structure. Whether the combined sparse order + two-residue-addition scaffold uniformly defines canonical multiplication on `X_N` requires a separate hostile audit.

Therefore the current classification is

\[
\boxed{\text{at least AL1; AL2 status open}.}
\]

This does not affect the asymptotic upper bound for crossing `AL0->AL1`.

## 12. Main conclusion

The suspected superlinear barrier does not exist in this resource model:

\[
\boxed{
\operatorname{Cost}(AL0)=\Theta(N),
\qquad
\operatorname{Cost}(AL1)=\Theta(N).
}
\]

The qualitative logical jump from order to variable displacement/addition is real, but its sparse memory cost need not jump asymptotically.

What changes is the **kind of nonlocal information**, not its order of growth:

- AL0 needs sparse global coordinates;
- AL1 needs sparse additive coordinates, efficiently supplied by two CRT residue systems.

## 13. Next boundary

The next resource question is now sharper:

\[
\boxed{AL1\to AL2.}
\]

Does multiplication/full arithmetic also admit `Theta(N)` sparse compilation, perhaps by residue multiplication tables of the same two moduli, or does the need to disambiguate products on the range `0\le xy<N` introduce a different threshold?

A first observation is provocative: modular multiplication tables on the same two `Theta(sqrt N)` residue rings also cost only `Theta(N)`. Therefore AL2 may also have a linear upper bound. The crucial issue is exact reconstruction and overflow/range control, not raw table size.
