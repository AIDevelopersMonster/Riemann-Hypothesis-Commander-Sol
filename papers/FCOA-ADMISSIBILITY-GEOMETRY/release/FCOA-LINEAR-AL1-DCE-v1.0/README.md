# Zenodo release package — FCOA Linear Additive Memory v1.0

## Record title

**Optimal Linear Additive Memory in Finite Ordered Structures: Zeckendorf Events and Decidable-Envelope Phase Barriers**

Russian title: **Оптимальная линейная аддитивная память в конечных упорядоченных структурах: события Цекендорфа и фазовые барьеры разрешимой оболочки**

Author: **Alex Malachevsky**  
ORCID: **0009-0008-6009-3196**  
Version: **1.0**  
Publication date: **2026-08-30**

## Recommended Zenodo files

Upload the entire ZIP or, preferably, upload the following visible files individually and keep the source archive as an additional file:

1. `FCOA_Linear_Additive_Memory_EN_v1.0.pdf`
2. `FCOA_Linear_Additive_Memory_RU_v1.0.pdf`
3. `FCOA_Linear_Additive_Memory_Sources_v1.0.zip`
4. `PREPUBLICATION_AUDIT.md`
5. `RELEASE_MANIFEST.md`
6. `SHA256SUMS.txt`

The full package also contains metadata, citation, license, source, and reproducibility files.

## DOI workflow

The PDFs intentionally contain the line `Zenodo DOI ... to be reserved`. Before publication, create a Zenodo draft and reserve a DOI if you want the DOI printed inside the PDFs. After a DOI is reserved, replace the placeholder in both TeX sources, rebuild both PDFs, re-render them, rerun the audit, and regenerate the checksums and ZIP. If embedding the DOI is not required, the present PDFs are deposit-ready and Zenodo will assign the DOI to the record.

## Resource type

Recommended Zenodo type: **Publication / Working paper**.

## License

The repository and previous FCOA publication packages use the **MIT License**. This package therefore ships with the same license. If a later deposit intentionally separates article text and code licensing, Zenodo supports mixed-license records; that is a new publication decision and is not assumed by this package.

## Related record

The direct predecessor in the FCOA Admissibility Geometry programme is:

- Alex Malachevsky, *Reflections on Admissibility Geometry with Commander Sol: How a Partial Operation Remembers an Oriented Carrier*, Zenodo (2026), DOI `10.5281/zenodo.22129787`.

## Reproducibility

Two executable certificates are included under `reproducibility/`:

- `verify_zeckendorf_adder_aperiodic.py`
- `verify_event_compression_phase_split.py`

Their captured outputs are included next to the scripts. The scripts supplement, but do not replace, the general proofs in the article.
