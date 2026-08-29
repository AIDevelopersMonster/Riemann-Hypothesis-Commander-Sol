# FCOA Branch Passport Laboratory — Final Upstream Memo

**Rounds:** P0-P6  
**Finalized:** 2026-08-29  
**Audience:** main Commander Sol scientific director  
**Status:** **HANDOFF COMPLETE / BRANCH CLOSED**  
**Canonical publication:** Zenodo DOI `10.5281/zenodo.22160014`

## Executive handoff

The passport laboratory began as methods/audit infrastructure and produced a complete mathematical chain beyond its original remit. All theorem-level results that survived hostile audit have now been integrated into the main line and published. This memo supersedes earlier intermediate recommendations.

## U6-01 — Sparse rigid fiber problem resolved and transferred

For

`m(n)=min{|F| : F subset X_n^2\Delta, Stab_{S_n}(F)=1}`,

P6 independently established the scale

`m(n)=n-Theta(n/log n)`.

Subsequent main-line work identified `m(n)` with the classical minimum-size identity-digraph problem and sharpened the result to:

- exact finite threshold evaluation from identity oriented-tree counts;
- `n-m(n)=L n/[log n+(3/2)log log n+O(1)]` with `L=log lambda`;
- explicit partial-layer phase oscillation, excluding a universal bounded denominator constant `K_0`.

These refinements and the prior-art discipline are canonical in DOI `10.5281/zenodo.22160014`. P6 remains provenance, not a priority claim for the classical identity-digraph problem.

## U5-01 — Two outputs attain the absolute maximum

P5 answers the extremality question left open by P3/P4.

On `n` active points with complete off-diagonal definedness, color a rigid directed Hamilton path by `Omega_+` and every other off-diagonal cell by `Omega_-`. The two fibers have unequal sizes, so they cannot be exchanged. The `Omega_+` fiber has trivial stabilizer. Hence

`Aut(star)=1`

while

`Aut(D|X_n)=S_n`.

Therefore

`VRI(star)=n!`,

the absolute maximum possible active-sort VRI.

Thus exactly two anonymous terminal outputs are not merely enough for factorial amplification: they already achieve maximal value-induced rigidity.

## U4-01 — Exact output-cardinality threshold

P4 proves the One-Output Collapse theorem. For a pure terminal-output partial operation with singleton output set `O={Omega}`,

`x star y=Omega <=> D_star(x,y)`.

Every active-sort definedness automorphism extends uniquely across the singleton output, so

`pi_X Aut(star)=Aut(D_star|X)`

and

`VRI(star)=1`.

Combined with P5:

`|O|=1 -> VRI=1`,

while

`|O|=2 -> VRI=n!` is attainable.

This is the sharp threshold in the **pure terminal-output active-sort setting**. It is not a global statement about arbitrary self-valued algebras.

## U3-01 — Absolute two-output amplification

P3 supplied the first globally bounded-total-output construction:

`O={Omega_+,Omega_-}`,

`x_i star x_j=Omega_+` for `i<j`,

`x_i star x_j=Omega_-` for `i>j`.

Then

`Aut(D|X_n) ~= S_n`, `Aut(star) ~= C2`, `VRI=n!/2`.

The anchored variant is rigid with `VRI=(n-1)!`. P5 later superseded the `n!/2` value as the extremal target but not the correctness or conceptual role of P3.

## U2-01 — G4 scope repair

The G4 construction has a growing inherited terminal-output carrier because of the `E_i^*`,`E_i^x` families. Therefore its safe statement is about a fixed two-value **added** orientation layer over M0, not a globally bounded total terminal-output alphabet.

This scope issue was repaired conceptually by P3, which removed the M0 backbone entirely and established the absolute two-output theorem.

## U1/P0 — Audit infrastructure findings retained

The laboratory independently confirmed small-case automorphism groups for G3/G4, exposed the need to separate active-sort and full one-sorted automorphisms, and showed that domain, value fibers, commutation, Association Spectrum, translations and output orbits are genuinely independent passport coordinates.

The reusable checker is `passport_enumerator.py`; the methodological schema is `PASSPORT_SCHEMA.md`.

## Publication transfer

The mature theorem package is published as:

**Reflections on Value-Rigidity with Commander Sol: Two Anonymous Outputs, Identity Digraphs, and Sparse Rigid Fibers**  
Zenodo DOI: `10.5281/zenodo.22160014`.

Repository companion:

`papers/FCOA-VALUE-RIGIDITY-IDENTITY-DIGRAPHS/`

The publication is the canonical source for theorem statements, proofs, prior-art boundaries, exact `m(n)` computation, asymptotics and phase law.

## Infrastructure not transferred

Machine-readable passport serialization, universal erasure predicates and generalized automatic diff generation were never required to prove the mathematical results. They are **DEFERRED** to a future tooling project and are explicitly non-blocking for closure.

## Final recommendation

**Close `director/fcoa-branch-passport-lab`.**

Do not extend P3-P6 inside this branch. New work should cite DOI `10.5281/zenodo.22160014` and start from a fresh branch with a distinct research question. Preserve this branch only as provenance for the audit and discovery path.
