# Release manifest — FCOA Hybrid Memory Article A

**Version:** 0.9.0-rc1  
**Package date:** 2026-08-29  
**Release gate:** REVIEWED_CLEAN — DOI reservation pending  
**Zenodo DOI:** pending reservation (not fabricated)

## Generated release candidates

The audited local build produced:

| File | Purpose | SHA-256 |
|---|---|---|
| `FCOA_HYBRID_MEMORY_EN_RC0.9.0.pdf` | English preprint | `d0cb37bff7bdaef91fddd12536e3be25ce625decdd3a478d06773a0d3fbdc030` |
| `FCOA_HYBRID_MEMORY_RU_RC0.9.0.pdf` | Russian preprint | `978035b0cb5775e3fb9230c39169191448712930425eb08012deb48b5e914234` |
| `FCOA_HYBRID_MEMORY_SOURCE_RC0.9.0.zip` | Source + metadata + verifier package | `d5f29d8af33d14318b00785363619b39ee2d7c630532d6e672336f021e441810` |

Verifier:

`95a323c40252689f174d81f65570ba91036ff5ce461fe5585bc595dbe3baf733  supplement/verify_minimal_classifications.py`

The RC binaries are Zenodo release artifacts; they are intentionally not treated as final archival files until a DOI is reserved and embedded.

## Mathematical gate

- all non-enumerative theorem statements in the manuscript have proofs;
- computer-assisted counts are released with an exhaustive verifier;
- verifier passes the expected `0/0`, `0/0`, `24/1`, `48/8` counts;
- output semantics are explicit in every minimality claim;
- the general typed Lift-Compatibility theorem states its surjectivity hypothesis;
- one-sorted and typed lower bounds are not conflated;
- arithmetic/order claims are excluded from Article A.

## Render gate

English RC:

- XeLaTeX build successful;
- 13 rendered pages;
- no undefined references;
- no overfull boxes in final build log;
- title, theorem, classification and final-reference pages visually inspected.

Russian RC:

- XeLaTeX build successful;
- 14 rendered pages;
- Cyrillic and mathematical glyphs verified;
- no undefined references;
- no overfull boxes in final build log;
- title, theorem and final-reference pages visually inspected.

## DOI gate

These files are **release candidates**, not the final archival PDFs, because the DOI has not yet been reserved.

Final release procedure:

1. reserve Zenodo DOI;
2. insert DOI in both TeX sources and package metadata;
3. change version to `1.0.0`;
4. rebuild both PDFs;
5. rerun verifier;
6. rerender/inspect PDFs;
7. regenerate source ZIP and checksums;
8. publish Zenodo record;
9. commit final DOI metadata to GitHub.