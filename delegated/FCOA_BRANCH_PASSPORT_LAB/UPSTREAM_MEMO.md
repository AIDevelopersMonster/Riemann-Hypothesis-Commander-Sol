# FCOA Branch Passport Laboratory — Upstream Memo

**Rounds:** P0–P2  
**Audience:** main Commander Sol scientific director

## U2-01 — THEOREM-SCOPE REPAIR REQUIRED BEFORE G4 PROMOTION

The G4 automorphism and VRI formulas survived independent enumeration and translation-profile audit. However the headline language `bounded output alphabet` is too strong if read as a statement about the full operation.

The M0 backbone already contains terminal families `E_i^*` and `E_i^x`, each with `N-1` distinct values. G4 adds two anonymous orientation outputs. Thus

`|T_G4| = 2(N-1)+2 = 2N`.

The total terminal-output alphabet grows with `N`.

### Safe corrected theorem

> Over the M0 backbone family, two new anonymous orientation values suffice to reduce the projected full-operation symmetry from `S_{N-1}` to `C2`, producing `VRI=(N-1)!/2`; with one boundary anchor, the same two-value layer yields full rigidity and `VRI=2(N-1)!`.

Equivalent safe headline:

> **Bounded added value alphabet can produce unbounded factorial value-rigidity amplification over a fixed backbone scheme.**

### Unsafe without further construction

Do not claim that the present G4 family has a globally bounded total output carrier independent of `N`.

That stronger problem remains open and would require collapsing/removing/replacing the inherited `E_i` output families without destroying the needed backbone geometry.

This is a theorem-scope repair, not a refutation of G4's group calculations.

## U2-02 — Independent translation-fingerprint proof of G4 rigidity

For generic `P_i`, the G4-C left translation contains

`i-2` copies of `Omega_-` and `N-i` copies of `Omega_+`.

Since the two outputs are anonymous, the invariant is the unordered pair

`{i-2,N-i}`,

which determines `P_i` exactly up to global reflection `i <-> N+2-i`. Thus translation fingerprints independently force the projected full group down to `C2`.

In G4-A the boundary anchor fixes `Omega_+`, so the pair is ordered and determines every generic index uniquely. This independently forces the full group to `1`.

This gives a second proof route, distinct from Fiber Transport, and should be considered for inclusion in the eventual G4 proof because it makes the mechanism transparent.

## U1-01 — Independent small-case automorphism gate PASSED

For `N=3,4,5,6`, direct enumeration gives G4-C definedness/full orders `2/2, 6/2, 24/2, 120/2` and G4-A `4/1, 12/1, 48/1, 240/1`. Hence the small-case VRI data agree with `(N-1)!/2` and `2(N-1)!`. No counterexample found.

## U1-02 — G3 hostile-audit repair independently reproduced

For `N=3..6`, G3-S and G3-C give definedness/full `2/2`; G3-A gives `4/1`, reproducing the `C2 x C2` definedness correction.

## U0-02 — Passport methodology

G3 already proves that domain, value fibers, commutation, Association Spectrum, full automorphisms and definedness automorphisms are mutually nonredundant enough that no domain+spectrum+`|Aut|` summary is adequate. Translation fingerprints now add a mechanistically useful local coordinate rather than merely a descriptive statistic.

## Director recommendation

**Do not promote the current wording of G4 unchanged.** Repair the alphabet scope first. After that repair, the core G4 factorial-rigidity result has now passed two independent finite/mechanistic checks:

1. exhaustive carrier-permutation enumeration;
2. translation-fingerprint reconstruction.

The most valuable next research question is now the stronger one exposed by the audit:

> Can factorial VRI be achieved with a globally bounded total terminal-output alphabet, rather than merely a bounded two-value layer added over M0?

That is a genuine next mathematical strike, not a wording cleanup.
