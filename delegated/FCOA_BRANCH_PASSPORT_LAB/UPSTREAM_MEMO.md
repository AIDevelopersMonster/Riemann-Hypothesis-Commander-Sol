# FCOA Branch Passport Laboratory — Upstream Memo

**Round:** P0  
**Audience:** main Commander Sol scientific director

## U0-01 — Do not treat current G4 verifier output as an independent automorphism-group check

The present G4 verifier independently enumerates Association Spectra and commutation counts, but its `base_definedness_automorphism_count()` returns the claimed formula directly. Therefore the displayed definedness-group orders and the VRI values are not independent computational evidence.

This does **not** presently refute the G4 theorem candidate. The prose group arguments remain plausible. It does mean that G4 should stay at its existing `WORKING / hostile audit pending` status until an independent small-case group enumerator is run.

Recommended hostile-audit gate before promotion:

1. enumerate `Aut(D_4C | X_N)` and `Aut(D_4A | X_N)` directly for `N=3,4,5,6`;
2. enumerate or fiber-stabilizer-check the full-operation carrier groups for at least `N=3,4,5`;
3. verify VRI from those independently obtained orders;
4. retain the `N=3` coincidence `S_2=C_2`, hence `VRI(G4-C)=1`.

## U0-02 — General methods result: FCOA needs a genuinely multi-coordinate invariant passport

The audited G3 transitions provide a clean internal demonstration that common structural summaries are mutually nonredundant.

- G3-S and G3-C: same domain, same Association Spectrum, same automorphism-group size, different commutation geometry.
- G3-C and G3-A: same commutation count, but different full-operation rigidity and different value-erasure behavior.

Therefore no passport based only on domain + spectrum + `|Aut|` is adequate. At minimum, branch comparison must separately carry:

- domain geometry;
- value-fiber partition;
- commutation locus;
- Association Spectrum;
- full-operation automorphisms;
- active-sort definedness automorphisms;
- one-sorted definedness caveat;
- translation profiles;
- output orbits;
- erasure/recoverability data.

This is a generally useful methodological conclusion for all later FCOA branches.
