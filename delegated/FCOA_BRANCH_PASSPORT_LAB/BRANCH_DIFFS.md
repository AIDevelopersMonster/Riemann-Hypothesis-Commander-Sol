# FCOA Branch Diff Register

**Version:** P0.1  
**Rule:** record only changed coordinates; zero deltas are explicit.

## Benchmark 1 — M0 -> G1 directed external skeleton

**Status:** fixed/published checkpoint

- Operation cells: **no change**.
- Operation domain: **no change**.
- Operation values: **no change**.
- External structure: add directed path `P_2 -> ... -> P_N` on `G_N`.
- Full multiplication automorphisms relative to external relation: `S_{N-1} -> 1`.
- Erase external relation: restores M0 `S_{N-1}`.
- Commutation: **no change**, `3(N-1)`.
- Association Spectrum: **no change** from M0.
- Translation profiles: **no operation-level change**.
- Recoverability: directed path is available only through the external relation; not internally remembered by multiplication after relation erasure.
- Arithmetic Leakage: external directed adjacency is imported; no arithmetic operation on indices is reconstructed.

**Diagnostic:** rigidity is external, not operation memory.

---

## Benchmark 2 — G1 directed skeleton -> G2 domain compilation

**Status:** fixed/published checkpoint

- External relation: may be erased after compilation.
- New operation cells: `P_i star P_{i+1}=Omega`, `2 <= i < N`; exactly `N-2` cells.
- New terminal outputs: one anonymous terminal `Omega`.
- Generic off-diagonal domain: directed path becomes internal operation definedness.
- Full operation automorphisms: `1 -> 1` if G1 retains the directed external relation during comparison; relative to M0 operation alone the meaningful internal jump is `S_{N-1} -> 1`.
- Definedness memory: directed adjacency uniformly recoverable from off-diagonal generic definedness.
- Commutation: **no change**, `3(N-1)`.
- Association Spectrum delta relative to M0/G1:
  - `Delta EQ = N-2`;
  - `Delta NEQ = 0`;
  - `Delta LEFT = N-2`;
  - `Delta RIGHT = N-2`;
  - `Delta NONE = -3(N-2)`.
- Translation profiles: changed exactly at arguments incident to compiled directed edges; detailed profile table remains to be generated.
- Arithmetic Leakage: successor/directed adjacency on the finite generic path is internally recoverable; no claim of uniform infinite transitive closure or ordinary arithmetic.

**Diagnostic:** external geometry becomes internal domain memory without changing commutation.

---

## Benchmark 3 — G3-S -> G3-C

**Status:** hostile-audited with repair

- Operation domain: **no change**; both orientations of adjacent generic pairs are defined.
- New/removed cells: **none**.
- Value-fiber partition: one constant adjacency fiber is split into two orientation fibers `Omega_+` and `Omega_-`.
- Full operation automorphisms: **no group-size change**, `C2 -> C2`; the surviving reflection in G3-C acts with output swap.
- Active-sort definedness automorphisms: **no change**, `C2 -> C2`.
- Association Spectrum: **no change**:
  `(6N-8, 0, N^2+4N-6, N^2+3N-6, N^3+N^2-10N+21)`.
- Commutation count:
  `5N-7 -> 3(N-1)`.
- Exact commutation delta:
  `Delta |Comm| = -2(N-2)`.
- Translation profiles: domain-size profiles are unchanged; value-fiber profiles change on generic adjacency translations. Exact multiset delta remains to be generated.
- Output orbits: G3-S has one new adjacency output; G3-C has an anonymous two-output orbit exchanged by reflection.
- VRI: `1 -> 1`.
- Recoverability: absolute orientation is not fixed; it is recoverable only up to simultaneous path reversal/output swap.
- Arithmetic Leakage: no new domain geometry; orientation is moved into anonymous value fibers.

**Diagnostic:** same domain + same Association Spectrum + same `|Aut|` does not imply same commutation geometry.

---

## Benchmark 4 — G3-C -> G3-A

**Status:** hostile-audited with repair

- New cells: exactly one anchor, `P_1 star P_0 = Omega_+`.
- Domain delta: one boundary ordered pair becomes defined.
- Value-fiber delta: anchor joins the `Omega_+` fiber.
- Full operation automorphisms: `C2 -> 1`.
- Active-sort definedness automorphisms: `C2 -> C2 x C2` intrinsically; the extra factor is the boundary swap `P_0 <-> P_1` after values are erased.
- Boundary-role stabilizer in definedness: remains `C2` on the generic path reflection.
- Commutation: **no change**, `3(N-1)`.
- Association Spectrum delta:
  - `Delta EQ = 0`;
  - `Delta NEQ = 0`;
  - `Delta LEFT = 0`;
  - `Delta RIGHT = N`;
  - `Delta NONE = -N`.
- Output orbit delta: `Omega_+` is anchored and can no longer be exchanged with `Omega_-` by a full-operation automorphism.
- VRI: `1 -> 4`.
- Recoverability: values restore both the boundary-role distinction and generic orientation that definedness alone loses.
- Arithmetic Leakage: no arithmetic operation added.

**Diagnostic:** a one-cell value anchor can destroy residual full-operation symmetry while definedness itself becomes more symmetric in the boundary sector.

---

## Benchmark 5 — G4-C -> G4-A

**Status:** WORKING; G4 hostile audit pending

- New cells: exactly one anchor, `P_1 star P_0 = Omega_+`.
- Generic off-diagonal domain: **no change**, complete.
- Full operation automorphisms: candidate `C2 -> 1`.
- Active-sort definedness automorphisms: candidate `S_{N-1} -> C2 x S_{N-1}`.
- Commutation: candidate **no change**, `3(N-1)`; independently enumerated by current verifier.
- Association Spectrum delta, independently enumerated for finite regression range:
  - `Delta EQ = 0`;
  - `Delta NEQ = 0`;
  - `Delta LEFT = 0`;
  - `Delta RIGHT = N`;
  - `Delta NONE = -N`.
- VRI: candidate `(N-1)!/2 -> 2(N-1)!`, a factor `4` increase.
- Evidence caveat: current `verify_g4.py` does **not** independently enumerate the definedness automorphism groups; it prints their asserted closed forms.

**Diagnostic:** do not promote this diff to fixed until independent group enumeration and hostile audit are complete.

---

## Cross-benchmark lesson

The benchmark transitions already prove that no one of the following coordinates subsumes the others:

- domain geometry;
- value-fiber geometry;
- commutation geometry;
- Association Spectrum;
- full-operation automorphism group;
- definedness automorphism group.

The passport must therefore remain multi-coordinate and the branch diff must report zero as well as nonzero deltas.
