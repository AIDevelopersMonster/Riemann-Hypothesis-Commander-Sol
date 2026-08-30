# Prior-Art Audit — Mixed-Sector Algebraic Systems

**Branch:** `director/fcoa-z-symmetric-line`  
**Date:** 2026-08-30  
**Status:** LITERATURE AUDIT / NOVELTY BOUNDARY, NOT A NOVELTY CLAIM

---

## 1. Question

Does mathematics or physics already contain systems in which algebraic laws such as commutativity, associativity, or composition rules depend on a sign/grade/sector, with especially important structure concentrated in interactions between opposite sectors?

Short answer:

\[
\boxed{\text{Yes, the broad phenomenon is classical.}}
\]

But no exact match was found in this audit for the current FCOA-Z package:

- rigid signed coordinate line;
- legacy noncommutative/nonassociative partial operations inherited separately on same-sign branches;
- negative branch forced by reflection;
- all new binary base freedom localized in mixed-sign sectors;
- typed terminal/output fibers;
- explicit erasure/automorphism/FO-leakage diagnostics;
- future directed-displacement and inter-line transport interpretation.

Therefore the safe present position is:

\[
\boxed{
\text{sector-dependent algebra is not new; the exact FCOA-Z architecture may be new, but requires a deeper priority search before publication.}
}
\]

---

## 2. Associative pairs — closest associativity precedent

An associative pair is a pair

\[
(A^+,A^-)
\]

with alternating trilinear products

\[
A^\sigma\times A^{-\sigma}\times A^\sigma\to A^\sigma
\]

satisfying para-associative identities.

This is conceptually close to the FCOA-Z intuition that associativity need not be a global law on one total binary product but can instead be meaningful only on selected sign patterns.

Associative pairs are also described as abstract off-diagonal Peirce spaces of associative algebras. For a Peirce decomposition

\[
E=E_{11}\oplus E_{12}\oplus E_{21}\oplus E_{22},
\]

the pair

\[
(E_{12},E_{21})
\]

is the basic off-diagonal object. Alternating products such as

\[
E_{12}E_{21}E_{12}\subseteq E_{12}
\]

are natural, while the two signs are not merely copies of one ordinary algebra.

Relevant literature:

- O. Loos, *Jordan Pairs* / associative-pair framework, 1970s.
- G. Aranda Pino and M. Siles Molina, *Associative systems of left quotients*, Journal of Algebra 294 (2005), 408–430.
- F. Montaner and I. Paniello, *PI theory for Associative Pairs*, arXiv:1901.08833.

### Relation to FCOA-Z

Very close in the idea that algebraic laws may live on alternating sign words rather than globally.

Major differences:

- associative pairs are linear and ternary;
- their para-associativity is built into the structure;
- FCOA-Z begins with binary partial operations whose same-sign sectors already carry nonassociative/noncommutative legacy behavior;
- FCOA-Z has absolute coordinate position, terminal output sorts, erasure memory, and arithmetic-leakage diagnostics.

---

## 3. Jordan pairs — closest symmetry/mixed-interaction precedent

A Jordan pair

\[
(V^+,V^-)
\]

has products of the form

\[
V^\sigma\times V^{-\sigma}\times V^\sigma\to V^\sigma,
\]

with symmetry in the two outer same-sign variables and Jordan identities involving the opposite-sign middle variable.

Ottmar Loos's 1974 structure-theory paper explicitly treats a pair of modules \(V^+,V^-\), building on earlier work of K. Meyberg.

This is strong prior art for the general principle:

\[
\boxed{\text{the two signs need not carry independent total algebras; the meaningful identities may intrinsically involve cross-sign interaction.}}
\]

Relevant literature:

- O. Loos, *A Structure Theory of Jordan Pairs*, Bulletin of the AMS 80 (1974), 67–71.
- modern Jordan-pair literature including root-graded and super variants.

### Current physics relevance

In July 2026 John C. Baez, Endre Bokor, and Latham Boyle posted

*Jordan Pair Quantum Theory and the Standard Model*, arXiv:2607.10833,

arguing that ordinary quantum mechanics may be reformulated/generalized using hermitian Jordan triples and pointing to a correspondence between a doubly exceptional hermitian Jordan triple and Standard Model structure.

This does not validate FCOA-Z physically, but it shows that pair/triple systems with two-sector structure are an active mathematical-physics direction.

---

## 4. Jordan pair disystems / Leibniz direction — very recent relaxation

A paper posted 2026-08-23,

E. García, M. Gómez Lozano, R. Muñoz Alcázar, G. Vera de Salas,
*Leibniz algebras and their connection to Jordan pair disystems*, arXiv:2608.22385,

introduces Jordan pair disystems as a generalization of Jordan pairs arising from finite \(\mathbb Z\)-gradings of Leibniz algebras.

This is particularly relevant because Leibniz-type structures relax antisymmetry, and the pair-disystem construction again separates interaction laws by graded wings.

It strengthens the conclusion that there is an active research corridor around graded two-wing systems in which classical global symmetry laws are weakened or redistributed.

---

## 5. Categories and groupoids — closest binary partial-composition precedent

A category has a partial binary composition: two arrows compose only when source/target match, and associativity is required only for composable triples.

A groupoid is a category in which every arrow is invertible. In algebraic form it is a set with a partial binary multiplication satisfying associativity wherever the products are composable.

This gives an important binary precedent for the FCOA idea:

\[
\boxed{\text{associativity need not even be a meaningful global equation on all pairs/triples.}}
\]

With two objects/regions, arrows in one direction and arrows in the reverse direction behave like two opposite sectors. Two arrows of the same direction need not compose, whereas opposite directions can compose into loops.

Relevant literature:

- H. Brandt's groupoid concept (1920s);
- Encyclopedia of Mathematics entries on Category and Groupoid;
- P. J. Higgins, *Categories and Groupoids* (1971).

### Relation to FCOA-Z

This is close to FCOA partiality and future transport channels, but FCOA differs because:

- its operations need not be associative even when both bracketings are meaningful;
- its inputs are coordinate points, not only arrows;
- outputs may leave the active sort into terminal fibers;
- absolute position and arithmetic leakage are central observables.

---

## 6. Morita contexts / linking algebras — closest cross-sector binary-product precedent

A Morita context has two algebras \(A,B\), two opposite bimodules \(M,N\), and cross pairings

\[
M\otimes_B N\to A,
\qquad
N\otimes_A M\to B.
\]

In block form this is the structure behind

\[
\begin{pmatrix}
A&M\\
N&B
\end{pmatrix}.
\]

Thus the off-diagonal sectors interact with each other and produce diagonal outputs.

This is very close in spirit to the possible FCOA-Z pattern

\[
(+,-)\to \text{one output channel},
\qquad
(-,+)\to \text{another output channel}.
\]

Relevant literature:

- Morita contexts since the 1950s;
- operator-algebra versions and linking algebras;
- Blecher, Muhly, Paulsen, *Categories of Operator Modules — Morita Equivalence and Projective Modules*, Memoirs AMS 143 (2000).

### Main difference

Morita contexts are designed so that the full block multiplication is associative. FCOA-Z is explicitly interested in retaining nonassociative/partial behavior and measuring where associativity may emerge only locally or by sign pattern.

---

## 7. Superalgebras and color algebras — closest sector-dependent commutativity precedent

In a \(\mathbb Z_2\)-graded superalgebra, the exchange law depends on parity. For homogeneous elements,

\[
ab=(-1)^{|a||b|}ba
\]

in the supercommutative case, and the supercommutator is

\[
[a,b]_s=ab-(-1)^{|a||b|}ba.
\]

Thus ordinary commutation versus anticommutation is not one universal rule; it depends on the grades of the interacting elements.

Color Lie algebras generalize this further using a commutation factor / bicharacter

\[
\varepsilon(g,h),
\]

so the exchange law can depend on the ordered pair of grades.

This is strong prior art for the idea of a **commutation table indexed by sectors** rather than one global commutativity axiom.

Relevant literature:

- standard Lie-superalgebra / superalgebra theory;
- Lie color algebras and bicharacter commutation factors;
- D. S. Passman, *Simple Lie Color Algebras of Witt Type*, Journal of Algebra 208 (1998), 698–721.

---

## 8. Physics: graded statistics and sector-dependent exchange

Supersymmetry divides degrees of freedom into bosonic and fermionic sectors. Graded commutators encode different exchange behavior depending on the sectors.

More elaborate \(\mathbb Z_2\times\mathbb Z_2\)-graded mechanics has four particle grades. In one studied model there are ordinary bosons, two classes of fermions, and exotic bosons; fermions from different classes can obey exchange behavior different from fermions in the same class.

Relevant examples:

- N. Aizawa, Z. Kuznetsova, F. Toppan, *\(\mathbb Z_2\times\mathbb Z_2\)-graded mechanics: the classical theory*, arXiv:2003.06470.
- F. Toppan, work on \(\mathbb Z_2\times\mathbb Z_2\)-graded parastatistics and multiparticle quantum Hamiltonians.

This is perhaps the clearest physics precedent for the statement:

\[
\boxed{\text{the algebraic exchange law may depend on which sectors interact.}}
\]

It is not, however, the same as FCOA-Z's rigid signed coordinate branches.

---

## 9. Explicitly mixed / ordered graded associativity

There are also more specialized attempts to define associativity laws intermediate between global associativity and global antiassociativity. For example:

- I. Raptis, *Mixed Jordan-Lie Superalgebra*, arXiv:math-ph/0110030 (2001), introduces an "ordered graded associativity" in a particular graded quaternion-like system.
- literature on compatible dialgebras imposes separate individual and mixed associativity conditions on multiple binary operations.
- partially associative ternary algebras and operads replace a single global associativity equation by weaker multi-bracketing identities.

These show that "associativity depending on ordering/grade/mode" is already a recognized mathematical possibility, though there is no single universal theory capturing exactly the FCOA-Z setup.

---

## 10. Safe novelty boundary for FCOA-Z

### Definitely not new

FCOA-Z must not claim novelty for:

- plus/minus or even/odd gradings;
- sector-dependent commutation signs;
- partial associative composition;
- Jordan/associative pairs;
- off-diagonal block / Morita-context interactions;
- nonassociative graded algebras;
- the general idea that cross-sector interactions can carry special structure.

### Potentially distinctive

The current audit found no standard construction combining all of the following:

1. a **coordinate-rigid signed line** obtained as a reflection completion of a rooted ray;
2. a fixed legacy binary partial algebra on the positive branch;
3. the negative same-sign sector forced by reflection rather than independently axiomatized;
4. **Mixed-Sector Localization:** all remaining binary base freedom lies in \((+-)\cup(-+)\);
5. old same-sign operations remain noncommutative and partial-nonassociative;
6. mixed sectors may later obey stronger/local laws without forcing those laws globally;
7. typed output fibers may record cross-sector events instead of returning a base value;
8. finite-window automorphism and support cost are measured exactly;
9. coordinate/orientation/additive/multiplicative memory are separated by FO definability after erasure;
10. output fibers are intended eventually to become transport channels between distinct rigid lines.

This ten-part conjunction is the current candidate novelty locus.

No publication should state priority until MathSciNet/zbMATH/Google Scholar/arXiv and exact-keyword searches for binary partial graded algebras, generalized pairs, partial quasigroups/groupoids, colored operads and many-sorted partial algebras are completed.

---

## 11. New research invariant suggested by the audit

The literature comparison suggests that FCOA-Z should stop asking only whether an operation is globally commutative or associative.

Instead define a **sign-word law spectrum**.

For commutation, record separately

\[
C_{++},\quad C_{+-},\quad C_{-+},\quad C_{--}.
\]

For association, record the eight nonzero sign words

\[
A_{+++},A_{++-},A_{+-+},A_{+--},A_{-++},A_{-+-},A_{--+},A_{---},
\]

plus words involving the origin when needed.

Each entry records the FCOA association statuses (`EQ`, `NEQ`, `LEFT`, `RIGHT`, `NONE`) restricted to triples of that sign pattern.

This allows worlds in which, for example:

\[
A_{+++}\text{ is strongly nonassociative},
\qquad
A_{+-+}\text{ is associative},
\]

without imposing a global law.

This is a natural next invariant for the branch and gives a direct bridge to associative/Jordan pairs while retaining FCOA partiality.

---

## 12. Current conclusion

The strongest defensible statement after this audit is:

\[
\boxed{
\text{FCOA-Z is entering a well-populated mathematical neighbourhood, not an empty continent.}
}
\]

But that is good news rather than bad news. The neighbourhood supplies mature comparison theories and shows that sector-local laws are mathematically serious.

The open opportunity is to develop a distinct **binary partial interaction geometry** in which global algebraic laws are replaced by sign-pattern-specific laws, coordinate memory, output-channel transitions and erasure/leakage phases.

That is the research direction worth testing for genuine novelty.