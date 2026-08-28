# Pure Two-Output Rigidity Amplification — P3

**Laboratory:** FCOA — SOL-PASSPORT  
**Purpose:** answer the P2 question whether factorial VRI is possible with a globally bounded total terminal-output alphabet  
**Status:** theorem-level construction inside the passport laboratory; not yet promoted into the main FCOA branch

## 1. Pure construction

Let

`X_n = {x_1,...,x_n}`, `n >= 3`,

and let the total terminal-output carrier be exactly

`O = {Omega_+, Omega_-}`.

Define a partial operation on distinct base pairs by

`x_i star x_j = Omega_+` if `i < j`,

`x_i star x_j = Omega_-` if `i > j`,

and leave every diagonal pair undefined. No operation with an output element as an argument is defined.

Thus the total terminal-output alphabet has constant size

`|O| = 2`

for every `n`.

## 2. Definedness symmetry

On the active/base sort, the definedness relation is simply inequality:

`D(x_i,x_j) <=> i != j`.

Every permutation of `X_n` preserves inequality. Hence

`Aut(D | X_n) ~= S_n`.

## 3. Full-operation automorphisms

The two value fibers are

`D_+ = {(x_i,x_j): i<j}`,

`D_- = {(x_i,x_j): i>j}`.

Because the outputs are anonymous, a full automorphism may either preserve the two fibers individually or exchange them.

If a base permutation `g` preserves both fibers individually, then

`i<j <=> g(i)<g(j)`,

so `g` is an automorphism of the finite linear order and therefore identity.

If `g` exchanges the two fibers, then

`i<j <=> g(i)>g(j)`,

so `g` is an order anti-automorphism. The finite linear order has exactly one such permutation: reversal

`r(i)=n+1-i`.

Reversal extends by swapping

`Omega_+ <-> Omega_-`.

Therefore

`Aut(star) ~= C2`.

## 4. Exact VRI

Using the active-sort definition

`VRI(star) = [Aut(D|X_n) : pi_X Aut(star)]`,

we obtain

`VRI(star) = n!/2`.

Hence

`VRI(star) -> infinity`

factorially while the total terminal-output alphabet remains exactly two elements.

### Pure Two-Output Amplification Theorem

For every `n>=3`, there exists a partial operation with exactly two terminal outputs such that

- `Aut(D|X_n) ~= S_n`;
- `Aut(star) ~= C2`;
- `VRI(star)=n!/2`.

Therefore

`globally bounded total terminal-output alphabet does not imply bounded value-induced rigidity`.

This is strictly stronger, as an output-cardinality statement, than the M0-relative G4 construction.

## 5. One-sorted caveat — and why it still works

Now take the one-sorted universe

`U_n = X_n disjoint_union {Omega_+,Omega_-}`

with the same operation table.

For `n>=3`, every base point occurs as an argument in defined cells, whereas `Omega_+` and `Omega_-` never occur as arguments. Hence the active subset `X_n` is internally recoverable as the set of elements participating in the domain relation, and the output pair is its complement.

Thus the one-sorted presentation does not introduce carrier/output mixing.

After value erasure, the two outputs are isolated and can be exchanged independently, so

`Aut_full(D) ~= S_n x S_2`.

For the full operation, output exchange is not independent: it must be coupled to base reversal. Hence the full operation still has only two automorphisms.

The active-sort VRI remains `n!/2`. If one instead defines a full one-sorted index, its order ratio is

`(2 n!)/2 = n!`.

These are distinct invariants and must not be conflated.

## 6. Anchored rigid variant with the same two total outputs

Define `star_A` by adding one diagonal anchor

`x_1 star_A x_1 = Omega_+`.

All off-diagonal rules remain unchanged.

### Definedness group

The point `x_1` is now the unique base point with a defined diagonal cell. Therefore it is fixed by every definedness automorphism, while the remaining `n-1` base points may be permuted arbitrarily:

`Aut(D_A|X_n) ~= S_{n-1}`.

### Full-operation rigidity

Without the anchor the only nonidentity full-operation symmetry is reversal, and reversal sends `x_1` to `x_n`. Hence it cannot preserve the anchored diagonal cell. Therefore

`Aut(star_A)=1`.

Consequently

`VRI(star_A)=(n-1)!`.

Thus with exactly two terminal outputs one can have not only factorial VRI, but a rigid full operation with factorial definedness-to-value symmetry collapse.

## 7. Independent finite check

A formula-blind exhaustive enumerator was run for `n=3,4,5,6,7`.

Unanchored counts `(DefAut, FullAut)`:

- `n=3`: `(6,2)`;
- `n=4`: `(24,2)`;
- `n=5`: `(120,2)`;
- `n=6`: `(720,2)`;
- `n=7`: `(5040,2)`.

Anchored counts:

- `n=3`: `(2,1)`;
- `n=4`: `(6,1)`;
- `n=5`: `(24,1)`;
- `n=6`: `(120,1)`;
- `n=7`: `(720,1)`.

These match `n!/2` and `(n-1)!` VRI exactly.

## 8. Relationship to G4

This construction should not silently replace G4-C/G4-A in the main branch because G4 was intentionally built **relative to the inherited M0 multiplication backbone**.

The correct relationship is:

- G4 proves a relative amplification result over M0 using two added orientation outputs;
- P3 proves the stronger absolute output-cardinality statement in a pure orientation partial algebra;
- whether the pure theorem should become a new main-line checkpoint is a scientific-director decision, not a passport-lab governance decision.

## 9. Main conclusion

The P2 suspected obstruction is false.

There is no lower-bound obstruction forcing the number of terminal outputs to grow with factorial VRI. In fact

`|O|=2`

already supports

`VRI=n!/2`,

and with one anchor still using the same two outputs supports

`VRI=(n-1)!` with a rigid full operation.
