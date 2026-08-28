# FCOA Branch Passport Laboratory — Audit Findings

**Audit round:** P0  
**Target:** M0–G4 source chain and existing verifier discipline

## Finding P0-01 — G4 definedness automorphism counts are not independently enumerated by `verify_g4.py`

**Severity:** methodological / evidence gap  
**Theorem status affected:** G4 remains a working candidate; no contradiction found  
**Upstream significance:** yes if G4 is to be promoted

The current `verify_g4.py` exhaustively computes and checks:

- Association Spectra for G4-C and G4-A;
- commutation counts;
- spectrum checksums.

However the function

```python
def base_definedness_automorphism_count(N, anchored):
    return (2 if anchored else 1) * factorial(N - 1)
```

does not enumerate automorphisms of the definedness reduct. It returns the claimed formula itself. Therefore its printed values `DefAut4C` and `DefAut4A` are regression display values, not independent machine evidence for

`Aut(D_4C | X_N) ~= S_{N-1}`

or

`Aut(D_4A | X_N) ~= C_2 x S_{N-1}`.

The same issue propagates to machine evidence for the VRI formulas, because those use the asserted group orders.

### Required repair

Add an independent finite automorphism enumerator for the active/base definedness relation, at least for `N=3,4,5,6`. It must construct the relation from operation definedness and test carrier permutations directly. It must not use the target group formula to generate only expected automorphisms.

A second enumerator should test full-operation automorphisms including anonymous terminal-output permutations for small `N`, or equivalently independently verify the fiber-partition stabilizer inside the enumerated definedness group.

### Current verdict

No mathematical counterexample has been found. The prose proofs in `G4_BOUNDED_OUTPUT_AMPLIFICATION.md` are plausible and structurally clean, but the verifier currently overstates what it independently checks.

---

## Finding P0-02 — Multi-coordinate passports are necessary; standard invariants collide

**Severity:** structural / design result  
**Upstream significance:** methods theorem, not a correction

The audited G3 pair G3-S and G3-C demonstrates that the tuple

- operation domain;
- Association Spectrum;
- automorphism-group order

is not a complete discriminator: all three agree, while the commutation locus differs.

Specifically,

`Aut(G3-S) ~= Aut(G3-C) ~= C2`,

the Association Spectra are identical, but

`|Comm_S| = 5N-7`,

`|Comm_C| = 3(N-1)`.

Thus commutation geometry must be a mandatory independent passport coordinate.

---

## Finding P0-03 — Group order alone is also insufficient across value-erasure comparisons

**Severity:** structural / design result

G3-C -> G3-A shows a different orthogonal change. The commutation count remains `3(N-1)`, while the full-operation group changes `C2 -> 1`; moreover the intrinsic active-sort definedness group of G3-A is `C2 x C2`, not merely the generic reflection `C2`.

Therefore a passport must separately record:

- full-operation automorphisms;
- active-sort definedness automorphisms;
- one-sorted definedness automorphisms when terminal outputs are retained;
- stabilizers after fixing inherited boundary roles.

Collapsing these into a single `Aut` field loses the mechanism under study.

---

## Finding P0-04 — Evidence labels are required

**Severity:** methodological

Existing notes mix proof statements, exhaustive finite checks, and formula-printing regression output. The passport schema therefore introduces explicit evidence labels:

- `PROVED`;
- `ENUM`;
- `REGRESSION`;
- `WORKING`;
- `OPEN`.

This is not cosmetic. It prevents a closed-form function from being mistaken for an independent verification of the same closed form.

---

## Finding P0-05 — G4 small-case coincidence must remain explicit

For `N=3`, the generic sector has two points and

`S_2 = C_2`.

Hence G4-C has VRI `1`: the two-value orientation coloring produces no symmetry reduction relative to definedness in this smallest case. This does not contradict unbounded amplification, but every passport and theorem statement must retain the edge case explicitly.

---

## Next audit targets

1. independent active-sort definedness automorphism enumeration for G3/G4;
2. independent full-operation automorphism enumeration with anonymous outputs for `N=3,4,5`;
3. translation-profile generator and branch deltas;
4. exact terminal-output orbit computation;
5. machine-readable branch passport serialization;
6. benchmark diffs M0->G1, G1->G2, G3-S->G3-C, G3-C->G3-A, and provisionally G4-C->G4-A.
