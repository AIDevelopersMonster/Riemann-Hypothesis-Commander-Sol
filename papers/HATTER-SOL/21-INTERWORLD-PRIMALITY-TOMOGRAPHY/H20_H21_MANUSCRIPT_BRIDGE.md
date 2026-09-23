# HATTER-SOL 20–21 · MANUSCRIPT BRIDGE

Status: **PUBLICATION ARCHITECTURE FROZEN**

## 1. Why the paper is numbered 20–21

HATTER-SOL 20 and HATTER-SOL 21 form one continuous representation-to-observer
story, but they did not independently cross the same publication threshold.

H20 established a physical fact about **equivalent arithmetic presentations**.

H21 established an exact compiler rule that **changes the implementation
presentation while preserving the declared observer semantics**.

Therefore the combined paper should be numbered

\[
\boxed{\text{HATTER-SOL 20–21}}
\]

rather than presenting H21 as if H20 had disappeared from the programme.

## 2. H20 contribution retained in the paper

The retained H20 result is the finite arithmetic presentation-separation
experiment.

For the strict next-prime function

\[
S_W(x)=\min\{p>x:p\text{ prime}\},
\]

three formally equivalent presentations were compared:

- DIRECT;
- BALANCED;
- LINEAR.

Formal SAT equivalence established

\[
D_W\equiv B_W\equiv L_W.
\]

Yet their synthesized and physical realizations remained distinct.

At the Boolean synthesis layer over \(W=4,\dots,10\),

\[
\mathcal P_W^{\rm sem}
=
\{\{D,B,L\}\}
\]

while

\[
\mathcal P_W^{\rm ABC}
=
\{\{D\},\{B\},\{L\}\}.
\]

Thus semantic equivalence did not force structural equivalence under the
declared synthesis observer.

## 3. H20 physical result

On both Cyclone V and Gowin GW5A-25, DIRECT was mapped to hard memory while
BALANCED and LINEAR remained in logic fabric.

Moreover the BALANCED/LINEAR ranking changed with width and backend.

Cyclone V:

\[
L_8<B_8,
\qquad
B_9<L_9,
\qquad
B_{10}<L_{10}.
\]

Gowin:

\[
L_8<B_8,
\qquad
L_9<B_9,
\qquad
B_{10}<L_{10}.
\]

Hence the crossover location itself was backend dependent.

The H20 physical lesson is therefore:

\[
\boxed{
\text{physical realization depends on arithmetic presentation, width,
backend, and observer}
}
\]

even when semantics are frozen.

## 4. Why H20 did not become its own paper

The later H20-EXT computational structure-mining branch searched for a stronger
prime-specific invariant.

It found finite continuation/Walsh effects, but the strongest candidate failed
null-model invariance under stronger sieve conditioning and failed a fresh
cross-width crossover test.

Therefore H20-EXT was correctly closed with

\[
\boxed{\text{NO PAPER}}.
\]

The combined H20–21 manuscript must not revive those failed candidates as
positive claims.

At most, H20-EXT may be mentioned briefly as a falsification stage showing why
the programme moved away from mining a putative prime-specific Boolean
signature.

## 5. H20 to H21 transition

H20 asked:

> If semantics are fixed, can different arithmetic presentations produce
> measurably different physical realizations?

Answer:

\[
\boxed{\text{yes, in the measured finite families}.}
\]

H21 asks the stronger constructive question:

> Can the algebraic world descriptor itself determine a semantics-preserving
> implementation lowering?

For the canonical quadratic-world family,

\[
A_n=(\mathbf Z/n\mathbf Z)[x]/(x^2-Bx-C),
\]

H21 proves that

\[
B=0
\]

collapses exactly to a scalar Euler-Jacobi observer.

Thus H21 changes the role of presentation from an experimental independent
variable into a compiler decision justified by an exact theorem.

This is the conceptual bridge:

\[
\boxed{
\text{H20: presentation affects physical geometry}
\quad\Longrightarrow\quad
\text{H21: compile the mathematics into the right presentation}.
}
\]

## 6. Recommended combined paper claim

The paper should not claim a new primality test.

Its central claim is:

\[
\boxed{
\begin{array}{c}
\text{Equivalent finite arithmetic descriptions can induce measurably different}\\
\text{physical FPGA realizations, and algebraic structure can be used to select}\\
\text{a semantics-preserving lower-cost realization automatically.}
\end{array}
}
\]

H20 supplies the first half experimentally.

H21 supplies the second half by theorem, compiler rule, matched RTL, and
Cyclone V measurement.

## 7. What to include from H20

### Include

1. formal semantic equivalence of DIRECT/BALANCED/LINEAR;
2. synthesis-level structural separation;
3. two-vendor physical separation;
4. backend-dependent BALANCED/LINEAR crossover;
5. the conclusion that the physical observer must be vector-valued.

### Do not make central

- continuation quotient;
- Walsh spectra;
- wheel-conditioned deficits;
- H20-EXT exploratory statistics.

### Mention only in programme-history / negative-results note

H20-EXT was a closed falsification branch and did not meet its own publication
threshold.

## 8. Combined manuscript spine

### Part I — H20: finite arithmetic presentation transport

1. finite arithmetic function and equivalent presentations;
2. formal equivalence;
3. Boolean synthesis separation;
4. Cyclone V and Gowin physical observers;
5. backend-dependent crossover;
6. lesson: semantics does not determine physical presentation.

### Part II — H21: world-aware compiler lowering

7. quadratic-world observer family;
8. exact \(B=0\) collapse theorem;
9. semantics-preserving lowering rule;
10. exhaustive software equivalence;
11. matched sequential RTL;
12. generic Yosys comparison;
13. Cyclone V LAB-28 comparison;
14. claim boundary and prior-art audit.

### Conclusion

H20 measures presentation sensitivity.

H21 turns that sensitivity into a theorem-guided compiler action.

## 9. Publication status

The inclusion of H20 does not depend on reopening H20 publication claims.

H20 is used as the experimentally established precursor and motivation for the
H21 compiler result.

The combined paper therefore has a coherent historical and technical sequence
without inventing a missing standalone H20 publication.
