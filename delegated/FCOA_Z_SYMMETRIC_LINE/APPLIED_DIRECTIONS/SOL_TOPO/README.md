# SOL-TOPO

**Scientific direction:** non-Abelian anyons, fusion channels, braid/path memory  
**Parent:** `delegated/FCOA_Z_SYMMETRIC_LINE/APPLIED_DIRECTIONS/`  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264  
**Status:** RESEARCH ARC COMPLETE / PUBLICATION THRESHOLD REACHED FOR STRUCTURAL NO-GO NOTE

## Final result of the three-strike sequence

The useful correspondence remains

\[
\boxed{\text{mixed/typed interaction}\to\text{output-channel fiber},}
\]

not `+ - -> commutativity` and not a direct physical identification with anyons.

### Strike 1 — one-step fusion support

At fixed radial level, the existing terminal alphabet

\[
E_n^+,\ E_n^*,\ E_n^\times
\]

can encode the three simple Ising labels and exactly reproduce the support of the multiplicity-free fusion rules, including

\[
\sigma\times\sigma=1+\psi
\]

as a two-element typed output fiber.

Strict collision-free line geometry itself has trivial unordered configuration-space fundamental group and therefore cannot generate nontrivial braid topology.

### Strike 2 — local split-fiber matrix mechanism

A split terminal orbit has a reflection involution `J` and a provenance sign `S` satisfying

\[
J^2=S^2=I,
\qquad JS=-SJ.
\]

After free linearization this gives a valid local Pauli/Clifford-style two-state mechanism and a Hadamard transform on the **provenance** fiber. The associated two-state braid template selects relative phases `t=±i` when the braid relation is imposed.

### Strike 3 — hostile correction and coherence barrier

The hostile audit found that v0.2 originally conflated two different two-state spaces:

1. fusion channel: `E_n^+` versus `E_n^times`, corresponding to `1` versus `psi` in the v0.1 dictionary;
2. mirror provenance: `E_n^alpha` versus `bar E_n^alpha`.

Reflection acts on the second, while the Ising associator mixes the first.

Hence the v0.2 matrix calculation is mathematically valid, but its identification with the Ising fusion-channel associator is superseded.

The corrected four-state decomposition is

\[
H_n\cong H_{ch}\otimes H_{pr}.
\]

All old reflection/provenance-generated maps are block diagonal in the channel decomposition and therefore cannot generate the Ising channel-mixing Hadamard.

Moreover, an LC2 model consisting only of active fibers and unary endomorphisms cannot even formulate the categorical pentagon intrinsically: a tensor/fusion-tree address layer is required first.

## Exact minimum-resource barrier

The current resource ladder is

\[
\boxed{
\text{line}
<
\text{typed channels}
<
\text{provenance fiber}
<
\text{linear channel mixing}
<
\text{fusion-tree composition}
<
\text{monoidal coherence class}
<
\text{braided class}.
}
\]

The final four resources are not forced by the audited one-line FCOA-Z structure.

Conditional on adding the Ising fusion ring and a genuine tensor/fusion-tree layer, standard Tambara–Yamagami/Ising classification gives exactly two pentagon-complete monoidal categories and four braidings for each, hence eight braided Ising categories in total.

Thus raw FCOA-Z does not select a unique Frobenius–Schur sign, braiding phase, twist, or full hexagon solution.

## Current verdict

\[
\boxed{\texttt{FORMAL FUSION SHADOW + COHERENCE-BARRIER THEOREM}}
\]

Spatially:

\[
\boxed{\texttt{1D-CLOSED WITH RESPECT TO CARRIER DIMENSION}.}
\]

The missing resources are internal compositional/channel data, not a proved second spatial coordinate.

## Files

- `SOL_TOPO_REPORT_v0_1.md` — fusion-support embedding, conservative mixed-sector construction, terminal-sink obstruction, strict-line braid no-go.
- `SOL_TOPO_LC2_REFLECTION_BRAID_v0_2.md` — local split-provenance matrix mechanism and projective braid template. **Interpretation warning:** its identification of that split orbit with the Ising fusion-channel qubit is superseded by v0.3.
- `SOL_TOPO_COHERENCE_BARRIER_v0_3.md` — channel/provenance separation, channel-mixing obstruction, pentagon expressibility barrier, conditional Tambara–Yamagami/Ising completion, and minimum-resource theorem.

## Publication status

\[
\boxed{\texttt{PUBLICATION THRESHOLD REACHED}.}
\]

The publishable object should be a conservative structural/no-go note, not a claim that FCOA derives non-Abelian anyons.

Before Zenodo release, consolidate v0.1–v0.3 into one corrected RU/EN manuscript, retain the v0.2 correction explicitly, audit formula numbering and bibliography, and freeze the branch snapshot.