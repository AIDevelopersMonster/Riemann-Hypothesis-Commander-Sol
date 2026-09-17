# HATTER-SOL-15 · Fixed Prime 2 in an Explicit D6 World

**Status:** exact worked example

Take

\[
f(x)=x^3+2x+1
\]

and let

\[
K=\mathbb Q(\alpha),\qquad f(\alpha)=0.
\]

## 1. Irreducibility and Galois group

The polynomial has no rational root, hence is irreducible over `Q`.

For a depressed cubic `x^3+ax+b`, the discriminant is

\[
\Delta=-4a^3-27b^2.
\]

Here `a=2`, `b=1`, so

\[
\boxed{\Delta(f)=-59.}
\]

This is squarefree and non-square. Therefore the splitting field `L` of `f` has Galois group

\[
\operatorname{Gal}(L/\mathbb Q)\cong S_3\cong D_6.
\]

Because `Delta(f)` is squarefree, the index `[O_K:Z[alpha]]` is one, so the polynomial discriminant is the field discriminant.

## 2. Factorization of the fixed prime 2

Modulo `2`,

\[
f(x)\equiv x^3+1
=(x+1)(x^2+x+1).
\]

The two factors are distinct and irreducible of degrees `1` and `2`. Since `2` does not divide `Delta_K=-59`, the prime `2` is unramified. Dedekind factorization therefore gives

\[
\boxed{
2\mathcal O_K=\mathfrak p_1\mathfrak p_2,
\qquad
f(\mathfrak p_1/2)=1,
\qquad
f(\mathfrak p_2/2)=2.
}
\]

Thus the splitting type is

\[
\boxed{1\,2,}
\]

which is exactly the reflection cycle type in the degree-three permutation representation of `D_6`.

Equivalently, the Frobenius conjugacy class of `2` in the Galois closure consists of transpositions/reflections.

## 3. Two-port interpretation

Identify the three Schreier sectors with

\[
X=\mathbb F_3
\]

and the two ports with

\[
R(i)=i+1,
\qquad
S(i)=-i.
\]

The reflection Frobenius fixes exactly one sector and swaps the other two. In the degree-three field, this is precisely the arithmetic statement that `2` has one degree-one prime factor and one degree-two prime factor.

Hence this example realizes the chain

\[
\boxed{
\text{fixed integer prime }2
\to
\text{non-abelian Galois world }D_6
\to
\text{reflection sector action}
\to
\text{factorization }1+2.
}
\]

## 4. Claim boundary

The explicit polynomial gives a monogenic example, so the modulo-2 polynomial factorization directly reads the ideal factorization. This should not be overgeneralized: in higher-degree number fields, the existence of repeated residue-degree factors in `O_K/2O_K` is not constrained by the number of distinct irreducible polynomials of that degree in a chosen monogenic model.

In particular, the fact that `F_2` has only one irreducible quadratic polynomial does **not** by itself prohibit multiple degree-two prime ideals above `2` in a non-monogenic field.

## 5. Programme consequence

H15 now has one completely explicit fixed-prime laboratory in which the prime `2`, rather than an unspecified Chebotarev prime, exhibits the non-abelian reflection pattern. The next arithmetic target is to construct or classify higher-`p` dihedral worlds in which the fixed prime `2` has reflection decomposition group.