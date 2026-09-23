# H20-EXT-C1 · Prior-art and novelty audit

Status: **TARGETED FIRST PASS COMPLETE / NOVELTY UNRESOLVED**

## 1. Closest established literature

The nearest established research line is Fourier/Walsh analysis of arithmetic functions in binary representation, especially Jean Bourgain's work.

Relevant neighboring results include:

- *Prescribing the binary digits of primes* and *Prescribing the binary digits of primes, II*;
- *Monotone Boolean functions capture their primes*;
- Fourier-Walsh estimates for the von Mangoldt function used to control correlations with Boolean functions;
- *On the Fourier-Walsh spectrum of the Moebius function* and its sequel;
- later work on primes/restricted digits using Fourier structure.

These works show that the interaction between primes, binary digits, and low-complexity Fourier/Walsh structure is not a new subject.

## 2. What C1 is not

C1 must not be presented as novelty of:

- representing primes as a Boolean function;
- computing a Walsh transform of the prime indicator;
- studying low-degree Fourier coefficients of primes/von Mangoldt;
- observing that primes correlate weakly or nontrivially with binary digit functions;
- prescribing binary digits of primes.

All of those are known or directly adjacent to known work.

## 3. Narrow C1 object

The current H20-EXT object is more specific.

It compares the exact finite statistic

[
L_W(4)
=
2^{-2W}
sum_{1le|S|le4}widehat f_W(S)^2
]

against an **exact conditional permutation expectation** preserving fixed prime counts inside every joint arithmetic/magnitude cell, including the fine partition

[
(nmod210,lfloor n/Bfloor).
]

The current finite statement is a *deficit relative to that conditioned null ensemble*, not an absolute upper bound on individual Walsh coefficients.

## 4. Search outcome

The targeted first-pass search located extensive prior work on:

- Walsh/Fourier coefficients of von Mangoldt and Möbius;
- primes with prescribed or restricted digits;
- correlations of primes with Boolean functions;
- digital distribution of primes.

It did **not** locate a direct formulation matching all of:

1. degree-aggregated energy through degree four;
2. exact finite prime indicator on ([0,2^W));
3. exact conditional randomization preserving mod-210 counts;
4. simultaneous local magnitude-block count preservation;
5. comparison to the exact conditional expectation.

Absence from this search is not evidence of novelty.

## 5. Novelty classification

Current classification:

[
oxed{
	ext{known surrounding theory}
+
	ext{apparently distinct finite conditioned statistic}
+
	ext{novelty unresolved}.
}
]

## 6. Publication implication

The mathematical/empirical threshold is stronger after LAB-07, but publication should still be deferred until at least:

1. a more systematic literature audit of Bourgain's exact low-level estimates and related Boolean-prime papers;
2. analysis of whether C1 is an immediate finite corollary of known coefficient bounds;
3. ideally an exact or rigorous tail/concentration statement for the conditioned permutation ensemble;
4. a decision whether the finite deficit itself has an interpretable theorem mechanism rather than being only a certified table.

## 7. RH boundary

No RH claim is opened.
