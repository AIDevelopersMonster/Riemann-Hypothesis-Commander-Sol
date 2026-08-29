# FCOA Branch Diff Register

**Version:** P2  
**Rule:** record only changed coordinates; zero deltas are explicit.

## Benchmark 1 — M0 -> G1 directed external skeleton

**Status:** fixed/published checkpoint

- Operation cells/domain/values: **no change**.
- External structure: add directed path `P_2 -> ... -> P_N` on `G_N`.
- Full multiplication automorphisms relative to external relation: `S_{N-1} -> 1`.
- Erase external relation: restores M0 `S_{N-1}`.
- Commutation: **no change**, `3(N-1)`.
- Association Spectrum: **no change**.
- Translation profiles: **no operation-level change**.
- Recoverability: directed path is external only.

**Diagnostic:** rigidity is external, not operation memory.

---

## Benchmark 2 — G1 -> G2 domain compilation

**Status:** fixed/published checkpoint

- New cells: `P_i star P_{i+1}=Omega`, `2 <= i < N`; exactly `N-2`.
- New outputs: one anonymous `Omega`.
- Directed adjacency becomes recoverable from generic off-diagonal definedness.
- Commutation: **no change**, `3(N-1)`.
- Spectrum delta: `(+N-2, 0, +N-2, +N-2, -3(N-2))` in `(EQ,NEQ,LEFT,RIGHT,NONE)`.
- Translation profiles change exactly at vertices incident to compiled path edges.
- No infinite-order/arithmetic reconstruction claim.

**Diagnostic:** external geometry becomes internal domain memory.

---

## Benchmark 3 — G3-S -> G3-C

**Status:** hostile-audited with repair

- Domain: **no change**.
- Cells: **no change**.
- Fiber partition: one adjacency fiber splits into `Omega_+`,`Omega_-`.
- Full Aut: `C2 -> C2`.
- Active definedness Aut: `C2 -> C2`.
- Association Spectrum: **no change**.
- Commutation: `5N-7 -> 3(N-1)`, delta `-2(N-2)`.
- Translation domain sizes: **no change**.
- Translation value profiles: undirected adjacency degree is replaced by anonymous oriented in/out multiplicities; reflection remains.
- New-output orbits: singleton adjacency output -> one two-element orbit `{Omega_+,Omega_-}`.
- VRI: `1 -> 1`.

**Diagnostic:** same domain+spectrum+`|Aut|` does not imply same commutation or value geometry.

---

## Benchmark 4 — G3-C -> G3-A

**Status:** hostile-audited with repair

- New cell: `P_1 star P_0=Omega_+`.
- Full Aut: `C2 -> 1`.
- Active definedness Aut: `C2 -> C2 x C2` intrinsically.
- Commutation: **no change**, `3(N-1)`.
- Spectrum delta: `(0,0,0,+N,-N)`.
- Translation delta: `L_{P_1}` and `R_{P_0}` each gain exactly the anchor occurrence `Omega_+`.
- Output orbit: `{Omega_+,Omega_-}` splits into singleton orbits under the now-trivial full group.
- VRI: `1 -> 4`.

**Diagnostic:** one value anchor kills full symmetry while value erasure makes the boundary definedness more symmetric.

---

## Benchmark 5 — G4-C -> G4-A

**Status:** automorphism/VRI finite gate passed; theorem-scope repair required before promotion

- New cell: exactly `P_1 star P_0=Omega_+`.
- Generic off-diagonal domain: **no change**, complete.
- Full Aut: `C2 -> 1`, independently enumerated for `N=3..6` and independently recovered by translation fingerprints.
- Active definedness Aut: `S_{N-1} -> C2 x S_{N-1}`, independently enumerated for `N=3..6`.
- Commutation: **no change**, `3(N-1)`.
- Spectrum delta: `(0,0,0,+N,-N)`.
- VRI: `(N-1)!/2 -> 2(N-1)!`; finite values independently checked.
- Translation delta at boundary: `L_{P_1}` and `R_{P_0}` gain one `Omega_+` occurrence.
- Generic translation mechanism in G4-C:
  `P_i` has orientation pair `(i-2,N-i)`; anonymity makes this unordered and leaves exactly global reversal.
- In G4-A the anchor distinguishes `Omega_+`; the pair becomes ordered and every generic point becomes individually identifiable.
- New-output orbit: two-element orbit `{Omega_+,Omega_-}` -> two singleton orbits.
- **Scope correction:** G4 adds only two new anonymous values, but the inherited M0 terminal families grow with `N`; total terminal-output count is `2N`. Therefore the established result concerns a bounded **added** value alphabet over M0, not a globally bounded total output alphabet.

**Diagnostic:** one anchor converts an anonymous reflection-invariant rank fingerprint into an oriented pointwise rank fingerprint.

---

## Cross-benchmark lesson

The benchmark transitions show that domain geometry, value-fiber geometry, commutation, Association Spectrum, full Aut, definedness Aut, translation fingerprints and output-orbit geometry carry distinct information. The passport remains necessarily multi-coordinate.
