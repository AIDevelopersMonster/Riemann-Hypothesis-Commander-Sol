# HATTER-SOL-12 · MAXIMAL-FACTOR BIT OBSERVER

**Status:** exact elementary observer layer / theorem seed

## 1. Integer prototype

Let `n` be composite and let `p_min(n)` be its smallest prime divisor. The largest proper divisor is

\[
M(n)=\frac{n}{p_{\min}(n)}.
\]

Define the maximal-factor bit

\[
\beta(n)=
\begin{cases}
0,&M(n)\text{ is prime},\\
1,&M(n)\text{ is composite}.
\end{cases}
\]

### Proposition MF12.1

For composite `n`,

\[
\boxed{\beta(n)=0\iff \Omega(n)=2,}
\]

and

\[
\boxed{\beta(n)=1\iff \Omega(n)\ge3.}
\]

Thus the single bit is exactly a threshold test for factorization depth.

**Proof.** Removing one prime factor from the complete factorization of `n` leaves `\Omega(n)-1` prime factors counted with multiplicity. The remainder is prime exactly when `\Omega(n)-1=1`. QED.

## 2. Why one bit is not enough

If `n` is prime there is no nontrivial proper factor. Therefore assigning the same value `0` to both prime numbers and semiprimes would conflate two distinct structural cases.

Define the two-bit observer

\[
s(n)=\mathbf 1_{\{\Omega(n)\ge2\}},
\qquad
b(n)=\mathbf 1_{\{\Omega(n)\ge3\}}.
\]

Then

\[
\Omega(n)=1\Rightarrow(s,b)=(0,0),
\]

\[
\Omega(n)=2\Rightarrow(s,b)=(1,0),
\]

\[
\Omega(n)\ge3\Rightarrow(s,b)=(1,1).
\]

This is the minimal binary observer that separates irreducible, exactly-two-factor, and deeper-factorization regimes.

## 3. World version

Let `W` be an arithmetic world in which the chosen HATTER factor object has a canonical factorization depth `\Omega_W(n)` (for example irreducible-element multiplicity in a UFD, or prime-ideal multiplicity in the ideal formulation).

Define

\[
\boxed{
s_W(n)=\mathbf 1_{\{\Omega_W(n)\ge2\}},
\qquad
b_W(n)=\mathbf 1_{\{\Omega_W(n)\ge3\}}.
}
\]

The map

\[
W\longmapsto (s_W(n),b_W(n))
\]

is a two-bit world signal of the same integer.

This observer is deliberately much coarser than the polynomial response `Z_W(n;X,Y)`: it asks only whether factorization exists and whether one maximal proper factor remains reducible.

## 4. Threshold filtration

For every integer `j>=2`, define

\[
\boxed{
\tau_j(W,n)=\mathbf 1_{\{\Omega_W(n)\ge j\}}.
}
\]

Then

\[
\tau_2\ge\tau_3\ge\tau_4\ge\cdots
\]

pointwise, and for finite factorization depth `m=\Omega_W(n)` the threshold word is

\[
(\tau_2,\tau_3,\ldots)=(1,1,\ldots,1,0,0,\ldots)
\]

with the last `1` at position `m`.

Hence the complete threshold family recovers the factorization depth exactly:

\[
\boxed{
\Omega_W(n)=1+\sum_{j\ge2}\tau_j(W,n).
}
\]

The user's proposed maximal-factor bit is precisely `\tau_3`.

## 5. Observer hierarchy

The sequence

\[
\tau_2,\tau_3,\ldots
\]

provides a canonical family of progressively deeper observers. A truncated observer

\[
\mathcal O_L(W,n)=(\tau_2,\ldots,\tau_L)
\]

recovers

\[
\min\{\Omega_W(n),L\}
\]

and therefore gives a controlled finite-depth view of the world structure.

This realizes the idea of limiting the number of readout digits without choosing an arbitrary external compression rule.

## 6. Coupling to the prime-toggle world grid

On a finite prime-toggle cube `A subset Q`, define

\[
B_Q(n;A)=b_{T_AW_0}(n),
\]

or the richer pair

\[
S_Q(n;A)=(s_{T_AW_0}(n),b_{T_AW_0}(n)).
\]

Thus one integer produces a binary (or two-bit) codeword indexed by canonical world addresses.

World derivatives can then be applied to this coarse signal exactly as to the polynomial response. The resulting bit field is a low-cost projection of the richer HATTER world-response field.

## 7. Important limitation

Repeatedly taking the largest proper factor and recording only whether it is prime or composite does **not** create a new high-capacity code in ordinary integer arithmetic. It recovers only the number of prime factors counted with multiplicity, `\Omega(n)`, in unary threshold form.

Its research value appears when `\Omega_W(n)` varies with the arithmetic world, when the factor object is richer than ordinary integer factorization, or when the bit observer is combined with orbital/network/carrier response.

## 8. Next theorem target

Find an explicit integer `n` and a canonical finite family of arithmetic worlds for which the two-bit signal

\[
W\mapsto(s_W(n),b_W(n))
\]

separates worlds that collide under a simpler scalar observer, and compare its separating power with the full polynomial signal `Z_W(n;X,Y)`.
