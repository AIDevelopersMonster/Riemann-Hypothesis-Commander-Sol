# H20-EXT · Final assessment
## Computational Structure Mining

Status: **RESEARCH BRANCH CLOSED / PUBLICATION THRESHOLD NOT REACHED**

## 1. Research question

The branch asked:

[
oxed{
	ext{Do exact finite prime / primality objects expose a reproducible structural law}
atop
	ext{strong enough to justify independent theorem or publication status?}
}
]

The branch was deliberately evidence-first:

[
	ext{COMPUTE}
	o
	ext{OBSERVE}
	o
	ext{FALSIFY}
	o
	ext{FORMULATE}
	o
	ext{PROVE}.
]

No RH claim was permitted.

## 2. What was found

### 2.1 Continuation-quotient signal

The raw prime indicator had substantially smaller exact continuation quotients
than density-matched random and shuffled-prime baselines.

This looked promising.

### 2.2 Continuation signal falsified

Wheel-conditioning by mod 30 and mod 210 removed the compression advantage to
baseline scale.

Therefore the continuation-compressibility candidate was closed.

This was a successful negative result.

### 2.3 Walsh low-degree signal

A second, genuinely different observer was introduced:

[
L_W(4)
=
2^{-2W}
sum_{1le|S|le4}widehat f_W(S)^2.
]

A low-degree Walsh-energy deficit was found relative to increasingly strong
conditioned randomization baselines.

### 2.4 Fresh hold-out passed

After isolating the low-degree deficit, a fresh hold-out was frozen before
computing W=17,18, with W=19 as extrapolation.

The candidate passed.

### 2.5 Exact expectation derived

Monte Carlo dependence was removed.

For each conditioning stratum G, with

[
m_G=|G|,
quad
s_G=sum_{xin G}f(x),
quad
A_{G,S}=sum_{xin G}chi_S(x),
]

the exact conditional coefficient-square expectation is

[
mathbb E[widehat f(S)^2]
=
left(
sum_Grac{s_GA_{G,S}}{m_G}
ight)^2
+
sum_{G:m_G>1}
rac{(m_G^2-s_G^2)(m_G^2-A_{G,S}^2)}
{m_G^2(m_G-1)}.
]

This converts the conditioned baseline from a simulation object into an exact
finite combinatorial quantity.

### 2.6 Exact deficit under mod210 + local density

For W=17,18,19 the prime low-degree energy remained below exact expectation
when conditioning jointly by

[
(nmod210,lfloor n/Bfloor)
]

for

[
B=16384,8192,4096.
]

All nine predeclared discrepancies were negative.

### 2.7 Conditional-tail separation

Under the strongest mod210 x block4096 null model, 2048 fresh conditional
permutations were generated for each W=17,18,19.

No sampled null realization had low-degree energy at or below the prime value:

[
K_{17}=K_{18}=K_{19}=0.
]

Descriptive standardized separations were approximately

[
-6.12,quad -8.52,quad -8.21.
]

The corrected finite empirical tail probability was

[
widehat p=rac1{2049}approx4.88	imes10^{-4}.
]

### 2.8 Arithmetic controls

The same exact conditioned comparison was run for squarefree and semiprime
indicators.

On W=17,18,19:

- PRIME showed a low-degree deficit;
- SQUAREFREE showed a large low-degree excess;
- SEMIPRIME showed a low-degree excess.

Thus the observed sign was not reproduced by these two natural arithmetic
controls.

### 2.9 Extended wheel mod2310 passed

Adding explicit divisibility-by-11 conditioning via

[
2310=2cdot3cdot5cdot7cdot11
]

did not remove the deficit.

All nine predeclared mod2310 x local-block tests were negative.

## 3. Where the candidate failed

### 3.1 Final practical wheel mod30030

The next wheel

[
30030=2cdot3cdot5cdot7cdot11cdot13
]

produced the first genuine falsification.

At W=19 under global mod30030 conditioning,

[
L_{19}^{m prime}
>
mathbb E[L_{19}(4)].
]

Numerically,

[
Delta=+0.000129799949.
]

Therefore the robust statement

[
L_W^{m prime}(4)<mathbb E[L_W(4)]
]

is **not invariant under stronger sieve conditioning**.

### 3.2 Conditioning refinement reverses the sign

At the same W=19 and the same modulus 30030:

- one magnitude block: positive discrepancy;
- two magnitude blocks: negative discrepancy;
- four magnitude blocks: negative discrepancy.

Thus the sign itself depends on null-model resolution.

### 3.3 Fresh crossover law failed

A frozen W=19 sign pattern

[
(+,-,-)
]

for 1/2/4 blocks was tested on fresh W=20,21.

Both fresh widths produced

[
(+,+,-).
]

Hence the W=19 crossover threshold does not transport unchanged.

No post-hoc replacement threshold is fitted.

## 4. Exact finite results that remain valid

The negative publication decision does not erase the exact finite facts.

The branch has established reproducibly:

1. continuation-quotient prime compression is largely explained by low-prime
   wheel structure on the tested range;
2. exact conditional expectation formulas for low-degree Walsh energy under
   fixed-count stratum permutations;
3. a strong finite prime low-degree deficit under several mod210 and mod2310
   local-density conditioned ensembles;
4. strong finite conditional-tail separation for the mod210 x block4096 null;
5. opposite-sign behavior for squarefree and semiprime controls;
6. a concrete sign reversal under stronger mod30030 conditioning;
7. failure of a simple cross-width conditioning-crossover law.

These are valid finite computational results.

## 5. Why publication threshold is not reached

### Theorem threshold

No new asymptotic theorem has been proved.

The exact conditional-moment identity is elementary sampling-without-replacement
combinatorics.

The finite inequalities are certified computations, but novelty relative to
the surrounding Fourier-Walsh prime literature remains unresolved.

### Empirical-law threshold

A strong empirical law was found under several baselines, but it failed to be
null-model invariant.

In particular its sign changes under reasonable strengthening/refinement of
the conditioning observer.

### Impossibility threshold

No broad natural impossibility class has been proved.

### Representation-transport threshold

Observer/null-model dependence was demonstrated, but no new
technology/representation-independent arithmetic invariant was established.

Therefore:

[
oxed{	ext{PUBLICATION THRESHOLD NOT REACHED}.}
]

## 6. Literature boundary

Fourier-Walsh analysis of primes, von Mangoldt and binary digits is established
literature, including work of Bourgain and later restricted-digit prime
research.

The H20-EXT conditioned statistic appears more specialized than the standard
objects found in the first-pass audit, but absence of an exact literature match
does not establish novelty.

Because the strongest candidate already fails null-model invariance, a deeper
novelty campaign is not justified at present.

## 7. Final scientific conclusion

[
oxed{
	ext{No structural object strong enough for an independent H20 theorem/article}
atop
	ext{was established in the explored computational observers.}
}
]

More specifically:

> A reproducible low-degree Walsh-energy deficit exists for the finite prime
> indicator under several carefully controlled conditional null models and can
> be highly significant within those models. However, the sign of the
> discrepancy is not invariant under stronger sieve conditioning and its
> conditioning-resolution crossover does not validate as a stable cross-width
> law. Therefore the effect is classified as observer/null-model dependent,
> not as a new prime invariant.

This is a successful outcome of the evidence-first branch.

## 8. Branch disposition

[
oxed{	ext{H20-EXT CLOSED}.}
]

Do not reopen by:

- fitting a new block-count recurrence to W=19,20,21;
- enlarging wheel modulus at the current widths until conditioning becomes
  nearly deterministic;
- renaming the same Walsh discrepancy as a new geometry;
- invoking RH.

Reopen only if a genuinely new external theorem, representation, or
computational witness gives an independent reason.
