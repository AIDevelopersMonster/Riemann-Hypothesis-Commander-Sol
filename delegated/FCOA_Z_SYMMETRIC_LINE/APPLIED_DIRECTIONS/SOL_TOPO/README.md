# SOL-TOPO

**Scientific direction:** non-Abelian anyons, fusion channels, braid/path memory  
**Parent:** `delegated/FCOA_Z_SYMMETRIC_LINE/APPLIED_DIRECTIONS/`  
**Base:** FCOA-Z v1.1, DOI `10.5281/zenodo.22169264`  
**Status:** RESEARCH ARC COMPLETE / RU+EN PUBLICATION PACKAGE ASSEMBLED / PRE-ZENODO FREEZE

## Final programme verdict

The useful correspondence is

\[
\boxed{\text{mixed/typed interaction}\to\text{output-channel fiber},}
\]

not `+ - -> commutativity` and not a direct physical identification with anyons.

The final audited verdict is

\[
\boxed{\texttt{FORMAL FUSION SHADOW + COHERENCE-BARRIER THEOREM}.}
\]

Spatially,

\[
\boxed{\texttt{1D-CLOSED WITH RESPECT TO CARRIER DIMENSION}.}
\]

The missing resources are internal channel/compositional/coherence data, not a proved second spatial coordinate.

---

## Research arc

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

A conservative mixed-sector realization opens only previously undefined opposite-sign cells and leaves every inherited FCOA value unchanged.

Strict collision-free line geometry has contractible unordered configuration space and therefore cannot itself generate nontrivial braid topology.

### Strike 2 — local split-provenance algebra

A split terminal orbit has a reflection involution `J` and a provenance sign `S` satisfying

\[
J^2=S^2=I,
\qquad JS=-SJ,
\qquad (JS)^2=-I.
\]

After free linearization this yields a valid local Pauli/Clifford-style two-state mechanism and a Hadamard transform on the **provenance** fiber. An abstract two-state braid template with this Hadamard selects the nontrivial projective relative phases

\[
t=\pm i
\]

when the braid relation is imposed.

### Strike 3 — hostile correction and coherence barrier

The hostile audit found that v0.2 originally conflated two different binary degrees of freedom:

1. fusion channel: `E_n^+` versus `E_n^times`, corresponding to `1` versus `psi` in the v0.1 dictionary;
2. mirror provenance: `E_n^alpha` versus `bar E_n^alpha`.

Reflection acts on the second, while the Ising associator mixes the first. Therefore the v0.2 local matrix calculation is retained, but its identification with the Ising fusion-channel associator is superseded.

The corrected decomposition is

\[
H_n\cong H_{ch}\otimes H_{pr}.
\]

All old reflection/provenance-generated maps are block diagonal in the channel decomposition and cannot generate the Ising channel-mixing Hadamard without a new cross-type morphism.

Moreover, an LC2 structure consisting only of active finite fibers and unary endomorphisms cannot formulate the categorical pentagon intrinsically. A tensor/fusion-tree address layer is required first.

Conditional on adding the Ising fusion ring and a genuine tensor/fusion-tree layer, standard Tambara-Yamagami/Ising classification gives two monoidal completions and four braidings on each, hence eight braided Ising categories in total. These residual coherence choices are independent data, not consequences of the signed FCOA line.

---

## Exact minimum-resource ladder

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

---

## Publication package

### Current manuscripts

- `SOL_TOPO_ARTICLE_EN_v1_0.md` — corrected English prepublication manuscript.
- `SOL_TOPO_ARTICLE_RU_v1_0.md` — corrected Russian prepublication manuscript.
- `CORRIGENDUM_SOL_TOPO_v0_2.md` — mandatory interpretation correction for the historical v0.2 report.

### Research-history documents

- `SOL_TOPO_REPORT_v0_1.md` — fusion-support embedding, conservative mixed-sector construction, terminal-sink obstruction, strict-line braid no-go.
- `SOL_TOPO_LC2_REFLECTION_BRAID_v0_2.md` — local split-provenance matrix mechanism and abstract projective braid template. **Historical status:** mathematical local calculations retained; Ising fusion-channel interpretation superseded. Must be cited together with the corrigendum.
- `SOL_TOPO_COHERENCE_BARRIER_v0_3.md` — channel/provenance separation, channel-mixing obstruction, pentagon expressibility barrier, conditional Tambara-Yamagami/Ising classification, minimum-resource theorem.

---

## Novelty boundary

The publication does **not** claim novelty for Ising fusion rules, standard `F/R` matrices, braid-group representations, Tambara-Yamagami classification, or the classification of braided Ising categories.

The FCOA-specific contribution is the conjunction of:

1. exact typed-output encoding of one-step Ising fusion support in the existing terminal alphabet;
2. conservative mixed-sector realization preserving the legacy table;
3. strict-line braid-topology and terminal-reentry obstructions;
4. channel/provenance separation and a minimum-resource theorem for the missing categorical layer.

The intended publication type is therefore a **structural embedding/no-go note**, not a physical anyon model.

---

## Literature anchors

- D. Tambara, S. Yamagami, *Tensor Categories with Fusion Rules of Self-Duality for Finite Abelian Groups*, Journal of Algebra 209 (1998), 692–707. DOI `10.1006/jabr.1998.7558`.
- V. Drinfeld, S. Gelaki, D. Nikshych, V. Ostrik, *On braided fusion categories I*, Selecta Mathematica 16 (2010), 1–119. DOI `10.1007/s00029-010-0017-z`.
- C. Nayak, S. H. Simon, A. Stern, M. Freedman, S. Das Sarma, *Non-Abelian Anyons and Topological Quantum Computation*, Reviews of Modern Physics 80 (2008), 1083–1159. DOI `10.1103/RevModPhys.80.1083`.
- J. Preskill, *Lecture Notes for Physics 219: Quantum Computation*, Chapter 9, Topological Quantum Computation.
- J. S. Birman, *Braids, Links, and Mapping Class Groups*, Princeton University Press, 1974.

---

## Publication status

\[
\boxed{\texttt{PUBLICATION PACKAGE ASSEMBLED}.}
\]

The RU/EN manuscripts, explicit corrigendum, hostile-audit conclusions, theorem numbering, resource ladder, novelty boundary, and core bibliography are now present in the branch.

The next operational publication step is branch freeze / final metadata audit / conversion to the release formats used by the Commander Sol programme, followed by Zenodo deposition. No further mathematical theorem is required for the present SOL-TOPO note unless the publication audit exposes a substantive defect.