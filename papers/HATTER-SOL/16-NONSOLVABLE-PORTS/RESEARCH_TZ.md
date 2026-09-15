# HATTER-SOL-16 · NONSOLVABLE PORTS

## Research task

**Working title:** *Beyond the Dihedral Lab: Nonsolvable Ports, Matrix-Valued Observers, and Artin-Type Spectral Channels*

**Status:** new research branch.  
**Parent layer:** HATTER-SOL-15 · NON-ABELIAN PORTS.  
**Goal:** determine which parts of the HATTER-SOL-15 mechanism survive when the port group is no longer solvable and the scalar/even-character observer is replaced by higher-dimensional irreducible representations.

---

## 1. Publication question

HATTER-SOL-15 proves a very rigid chain in the prime dihedral laboratory:

`noncommuting ports -> commutator square -> primitive mirror observer -> positive Mahler harmonics -> first-harmonic dominance -> nonvanishing character channels -> full linear tomography`.

HATTER-SOL-16 asks which arrows are genuinely dihedral and which are representation-theoretic.

The target is **not** to claim a universal extension before evidence. The first objective is to build the smallest nonsolvable laboratories in which every step can be computed exactly or certified numerically.

---

## 2. First laboratory: A5

Use the smallest nonsolvable finite group

`A5 ~= PSL(2,4) ~= PSL(2,5)`.

Reasons for starting here:

- order 60 is small enough for complete enumeration;
- conjugacy classes and irreducible characters are explicit;
- faithful permutation and low-dimensional matrix representations are available;
- commutator distributions can be exhaustively computed;
- it is the first place where the port response is not reducible to a single cyclic coordinate.

### Required computations

For generating pairs `(A,B)` up to simultaneous conjugacy:

1. compute `K=[A,B]` and its conjugacy class;
2. record cycle type in natural permutation actions;
3. evaluate irreducible traces `Tr rho(K)` for each nontrivial irrep `rho`;
4. build the two-port operator

   `L_rho(z,w)=c I - z rho(A)-z^{-1}rho(A)^* - w rho(B)-w^{-1}rho(B)^*`;

5. compute determinant/Mahler response on a torus grid;
6. identify the first channel-dependent term in the large-`mu` expansion;
7. test whether an analogue of first-harmonic dominance exists representation-by-representation.

The first theorem target is deliberately finite:

> Classify the simultaneous-conjugacy classes of generating pairs in A5 by the vector of commutator traces across irreducible representations, and determine whether this observer separates all commutator conjugacy classes.

---

## 3. Second laboratory: PSL(2,7)

Move next to the simple group of order 168.

It offers:

- a natural action on the projective line over `F_7`;
- low-dimensional irreducible representations;
- exact finite-field matrix realizations suited to hardware;
- a genuinely non-dihedral commutator geometry with several conjugacy classes.

The aim is to test whether the A5 observer architecture survives a larger simple group before attempting a family `PSL(2,q)`.

---

## 4. Third laboratory: S5 and permutation families

`S5` is the smallest symmetric group that is nonsolvable. It is useful because permutation ports admit an immediate hardware realization as lookup-table permutations.

Questions:

- how much of a hidden port pair is reconstructed from the family of commutator cycle observables;
- whether higher spectral moments recover the full commutator cycle type;
- how the answer changes after passing to irreducible Specht modules;
- which observer labels are destroyed by conjugation-invariant aggregation.

Do not jump directly to generic `S_n` until `S5` is completely understood.

---

## 5. Artin spectral bridge

For a finite Galois group `G` and an irreducible complex representation `rho`, the local unramified Artin factor is

`det(I-rho(Frob_q) T)^{-1}`.

This is the correct first non-Abelian replacement for the scalar Dirichlet Euler factor used in HATTER-SOL-15.

The H16 program should therefore compare three objects attached to the same conjugacy class:

1. commutator holonomy `K=[A,B]`;
2. spectral response `Tr rho(K^m)` / determinant channels;
3. Artin local data `det(I-rho(K)T)^{-1}` when the group is realized arithmetically.

### Claim boundary

Do **not** identify this automatically with an automorphic `L`-function. The Artin `L`-function exists representation-theoretically; automorphy is known only in particular settings and is conjectural in general. H16 will state explicitly when an automorphic interpretation is known, conditional, or absent.

---

## 6. Matrix-valued Mahler observer

For a unitary representation `rho:G->U(d)` define a matrix-valued two-port Bloch operator

`L_rho(theta,phi;mu)`

and the scalar determinant observer

`M_rho(mu)=(2pi)^{-2} int int log det L_rho dtheta dphi`

whenever the determinant is positive/nonzero on the integration torus.

The key H15 question becomes:

> Is there a preferred low-order harmonic or closed-word contribution whose magnitude dominates all higher-order terms for a non-Abelian matrix representation?

Possible outcomes are all valuable:

- universal dominance survives;
- dominance depends on the irrep;
- several leading harmonics form a dominant block;
- simple groups furnish a counterexample to the H15 pattern.

A counterexample is a result, not a failure.

---

## 7. Continuum limit

The `p -> infinity` / operator-algebra direction is postponed until the finite simple laboratories are understood.

Candidate limiting objects:

- Toeplitz-type operators generated by limiting port symbols;
- group von Neumann algebra observables;
- Fuglede-Kadison determinants;
- measured/continuous boundary observers.

The continuum statement must be derived as a limit of a specified finite family, not introduced by analogy alone.

---

## 8. Computational deliverables

The H16 branch should contain:

- exact group/representation data generators;
- exhaustive generating-pair enumeration for A5;
- conjugacy-class and commutator tables;
- matrix observer code;
- reproducible spectral/Mahler sweeps;
- machine-readable certificates for any sign/nonvanishing theorem;
- a hardware-friendly test-vector format shared with HATTER-SOL-17.

---

## 9. First theorem gate

Do not write the H16 article before at least one of the following is closed rigorously:

1. complete A5 commutator-observer classification;
2. an exact nonvanishing/separation theorem for a nontrivial higher-dimensional irrep;
3. a rigorous counterexample showing that H15 first-harmonic dominance fails outside the dihedral family.

The first active strike is **A5 complete enumeration and observer separation**.
