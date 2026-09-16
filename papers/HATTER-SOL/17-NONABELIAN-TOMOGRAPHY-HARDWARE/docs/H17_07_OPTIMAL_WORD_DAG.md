# HATTER-SOL-17 · H17-07 · Optimal common-subexpression word DAG

## 1. Problem

The H17 robust observer uses the ordered words

```text
AAB
Abb
AAAB
Abbb
AABAb
AAbAb
ABABB
ABaBB
```

If every word is evaluated independently from `A`, `B`, `A^{-1}`, `B^{-1}`, the number of permutation compositions is

```text
(3-1)+(3-1)+(4-1)+(4-1)+4*(5-1) = 26.
```

This is mathematically correct but a poor hardware implementation because many prefixes/subwords are repeated.

## 2. Exact optimization model

H17-07 allows every contiguous subword of one of the eight target words to become a shared DAG node. Atomic symbols `A,a,B,b` have zero composition cost. Every selected non-atomic word must be produced by a split

```text
w = left · right
```

whose two operands are atoms or selected shorter nodes.

A binary MILP minimizes the number of selected non-atomic nodes while forcing all eight target words to be present.

The zero-gap optimum is

```text
14 permutation compositions.
```

This is an exact optimum **within the contiguous-subword concatenation DAG model**. It is not promoted to a universal lower bound allowing arbitrary group identities or algebraic rewriting.

Certificate:

`certificates/psl27_word_dag_certificate.py`

## 3. One optimal 14-node DAG

```text
level 1
  AB   = A  · B
  Ab   = A  · b
  BB   = B  · B

level 2
  AAB  = A  · AB
  ABA  = AB · A
  ABa  = AB · a
  Abb  = Ab · b
  AbAb = Ab · Ab

level 3
  AAAB  = A    · AAB
  Abbb  = Abb  · b
  AABAb = AAB  · Ab
  AAbAb = A    · AbAb
  ABABB = ABA  · BB
  ABaBB = ABa  · BB
```

Thus the target word engine has

```text
composition count: 26 -> 14
maximum composition depth: 4 naive word length levels -> 3 DAG levels
```

where inversions of the two raw inputs are treated separately from permutation composition nodes.

## 4. Exact semantic verification

The displayed DAG is evaluated on every ordered pair

```text
(A,B) in PSL(2,7)^2,
```

that is

```text
168^2 = 28,224
```

input pairs.

For every pair, all eight DAG outputs are checked against direct letter-by-letter evaluation of the corresponding free-group word. The outputs agree exactly.

## 5. Hardware consequence

The preferred front end is therefore

```text
A,B
 -> invA,invB
 -> 3-level / 14-compose shared word DAG
 -> eight structural class engines
 -> robust signature
```

rather than eight independent word evaluators.

This optimization is orthogonal to H17-06. The same 14-compose front end can feed either:

1. the flat historical `orbit_id` decoder, or
2. the ROM-free erasure-repair/fingerprint processor.

The latter remains the preferred mathematical core.

## 6. Verification boundary

Generator:

`tools/generate_psl27_robust8_dag.py`

GitHub Actions has been switched so both the flat robust8 and ROM-free variants are regenerated from this DAG implementation before simulation and synthesis.

The HDL simulation and Yosys synthesis status of the optimized generator are recorded in `STATUS.md` only after the corresponding CI run completes.
