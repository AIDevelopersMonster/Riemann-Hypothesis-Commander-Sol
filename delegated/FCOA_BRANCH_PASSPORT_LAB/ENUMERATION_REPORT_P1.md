# Independent Automorphism Enumeration — P1

**Laboratory:** FCOA Branch Passport Laboratory  
**Target:** G3-S, G3-C, G3-A, G4-C, G4-A  
**Method:** exhaustive permutations of the entire active/base carrier `X_N`; no expected group-order formula is used by the enumerator  
**Range:** `N=3,4,5,6`

## 1. What is independently tested

For each branch and each `N`, the script constructs the partial-operation table directly.

It then enumerates all `(N+1)!` permutations of the base carrier and performs two independent tests.

### Definedness test

A permutation survives iff it preserves exactly the binary relation

`D(a,b) <=> op(a,b) is defined`.

This computes `Aut(D_star | X_N)` directly.

### Full-operation extension test

For inherited M0 outputs `P_i`, `E_i^*`, `E_i^x`, the output action is forced by the base permutation. For anonymous terminal outputs `Omega`, `Omega_+`, `Omega_-`, the script does not name or fix them. Instead it asks whether transport of cells induces a well-defined bijection of anonymous output fibers.

Thus the second count is the number of base permutations extendable to full-operation automorphisms. This is an independent finite implementation of the fiber-partition criterion, not a call to a target group formula.

`UNDEF` is represented by absence of a table cell, never as a value.

## 2. Exact results

| N | Branch | `|Aut(D|X_N)|` | extendable full base automorphisms |
|---:|---|---:|---:|
| 3 | G3-S | 2 | 2 |
| 3 | G3-C | 2 | 2 |
| 3 | G3-A | 4 | 1 |
| 3 | G4-C | 2 | 2 |
| 3 | G4-A | 4 | 1 |
| 4 | G3-S | 2 | 2 |
| 4 | G3-C | 2 | 2 |
| 4 | G3-A | 4 | 1 |
| 4 | G4-C | 6 | 2 |
| 4 | G4-A | 12 | 1 |
| 5 | G3-S | 2 | 2 |
| 5 | G3-C | 2 | 2 |
| 5 | G3-A | 4 | 1 |
| 5 | G4-C | 24 | 2 |
| 5 | G4-A | 48 | 1 |
| 6 | G3-S | 2 | 2 |
| 6 | G3-C | 2 | 2 |
| 6 | G3-A | 4 | 1 |
| 6 | G4-C | 120 | 2 |
| 6 | G4-A | 240 | 1 |

## 3. Generator/action observations

For G3-S and G3-C, the only nonidentity surviving base action is generic path reversal.

For G3-A, definedness has four base actions generated independently by:

- boundary transposition `(P_0 P_1)`;
- generic path reversal.

Only the identity extends to the full operation.

For G4-C, every permutation of `G_N` survives definedness, while only:

- identity;
- total generic reversal

extend to the full operation. Reversal transports the two anonymous orientation fibers into each other.

For G4-A, definedness consists of arbitrary generic permutations together with the independent boundary transposition, while only identity extends to the full operation.

## 4. Independently recovered finite VRI values

Using the independently enumerated orders:

### G4-C

- `N=3`: `2/2 = 1`;
- `N=4`: `6/2 = 3`;
- `N=5`: `24/2 = 12`;
- `N=6`: `120/2 = 60`.

These agree with `(N-1)!/2`.

### G4-A

- `N=3`: `4/1 = 4`;
- `N=4`: `12/1 = 12`;
- `N=5`: `48/1 = 48`;
- `N=6`: `240/1 = 240`.

These agree with `2(N-1)!`.

## 5. Audit consequence

Finding P0-01 is repaired at the laboratory level: the missing independent small-case group enumeration now exists and confirms the G4 claimed group orders and VRI values for `N=3,4,5,6`.

This finite evidence does not replace the general proof. It does, however, remove the specific verifier-evidence gap identified in P0-01.

No counterexample to the G4-C/G4-A symmetry claims was found in the mandatory small cases.

## 6. Status discipline

This report does **not** itself promote G4 from `WORKING` to `FIXED`. The source branch explicitly requires hostile-audit reconciliation before promotion. The correct current statement is:

> the independent finite automorphism gate has passed for `N=3..6`; remaining promotion gates are proof-level hostile audit, exact spectrum reconciliation, scope/sorting audit, and anonymous-output audit.
