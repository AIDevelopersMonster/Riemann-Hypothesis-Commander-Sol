# Release manifest — FCOA Hybrid Memory Article A

**Version:** 1.0.0  
**Publication date:** 2026-08-29  
**Release gate:** PUBLISHED / AUDIT CLOSED  
**Zenodo DOI:** **10.5281/zenodo.22165651**  
**Persistent URL:** https://doi.org/10.5281/zenodo.22165651

## Audited release-candidate provenance

Before DOI publication, the deterministic audited build produced:

| File | Purpose | SHA-256 |
|---|---|---|
| `FCOA_HYBRID_MEMORY_EN_RC0.9.0.pdf` | English audited preprint candidate | `d0cb37bff7bdaef91fddd12536e3be25ce625decdd3a478d06773a0d3fbdc030` |
| `FCOA_HYBRID_MEMORY_RU_RC0.9.0.pdf` | Russian audited preprint candidate | `978035b0cb5775e3fb9230c39169191448712930425eb08012deb48b5e914234` |
| `FCOA_HYBRID_MEMORY_SOURCE_RC0.9.0.zip` | Source + metadata + verifier candidate | `d5f29d8af33d14318b00785363619b39ee2d7c630532d6e672336f021e441810` |

Verifier source at audit time:

`95a323c40252689f174d81f65570ba91036ff5ce461fe5585bc595dbe3baf733  supplement/verify_minimal_classifications.py`

These hashes document the pre-publication audited RC provenance. The canonical archival publication is the Zenodo record identified by DOI **10.5281/zenodo.22165651**; the DOI record is authoritative for the deposited final binaries.

## Mathematical gate

- all non-enumerative theorem statements in the manuscript have proofs;
- computer-assisted counts are released with an exhaustive verifier;
- verifier passes the expected `0/0`, `0/0`, `24/1`, `48/8` counts;
- output semantics are explicit in every minimality claim;
- the general typed Lift-Compatibility theorem states its surjectivity hypothesis;
- one-sorted and typed lower bounds are not conflated;
- arithmetic/order claims are excluded from Article A.

## Render gate

English audited RC:

- XeLaTeX build successful;
- 13 rendered pages;
- no undefined references;
- no overfull boxes in final build log;
- title, theorem, classification and final-reference pages visually inspected.

Russian audited RC:

- XeLaTeX build successful;
- 14 rendered pages;
- Cyrillic and mathematical glyphs verified;
- no undefined references;
- no overfull boxes in final build log;
- title, theorem and final-reference pages visually inspected.

## Publication record

Article A is published and closed as a theorem package:

\[
\boxed{\text{Zenodo DOI }10.5281/zenodo.22165651}
\]

Any later correction must be recorded explicitly as a new version/erratum. New AL0/AL1/AL2, sparse-order, CRT, RTP, or restricted-interpretation results belong to Article B / subsequent publications.