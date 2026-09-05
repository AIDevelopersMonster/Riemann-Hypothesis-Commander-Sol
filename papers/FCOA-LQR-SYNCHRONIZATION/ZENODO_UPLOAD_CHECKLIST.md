# Zenodo Upload Checklist — FCOA LQR Synchronization

**Target release:** v1.0  
**Package:** `papers/FCOA-LQR-SYNCHRONIZATION/`  
**Foundation DOI:** `10.5281/zenodo.22164246`

## 1. Files to upload

Primary recommended set:

- `artifacts/article_en.pdf` — primary archival article;
- `artifacts/article_ru.pdf` — complete Russian version;
- `artifacts/article_en.docx`;
- `artifacts/article_ru.docx`;
- `artifacts/article_en.html`;
- `artifacts/article_ru.html`;
- `FCOA-LQR-SYNCHRONIZATION-v1.0-rc1.zip` — full reproducibility bundle.

Optional direct-source attachments if Zenodo file count is not a concern:

- `article_en.md`;
- `article_ru.md`;
- `artifacts/article_en.tex`;
- `artifacts/article_ru.tex`;
- `artifacts/MANIFEST.sha256`;
- `artifacts/reproducibility/VERIFICATION_LOG.txt`.

## 2. Zenodo metadata

Use `ZENODO_METADATA.json` as the canonical metadata source.

Before publish, verify:

- title exactly matches the English article title;
- creator is `Malachevsky, Alex`;
- ORCID is `0009-0008-6009-3196`;
- upload type is publication/article;
- license is CC BY 4.0;
- version is `1.0`;
- description includes the exact stabilization theorem;
- Foundation DOI `10.5281/zenodo.22164246` is present as related work;
- repository URL is present as supplemental software/research source.

## 3. Final file integrity check

Before upload:

1. open both PDFs and inspect title page, equations, bibliography and final page;
2. open both DOCX files and confirm no clipped equations or broken Cyrillic glyphs;
3. confirm both HTML files display formulas correctly;
4. run SHA-256 verification against `artifacts/MANIFEST.sha256`;
5. confirm `VERIFICATION_LOG.txt` records successful execution of both finite verifiers;
6. confirm no archival DOI for this article has been prefilled anywhere before Zenodo minting.

## 4. Suggested Zenodo description headline

> Exact point-image phase-synchronization costs in FCOA, including the complete q=3 and r<=4 families, a binary cut-space packing bound, and the sharp stabilization law L_q(r)=(r-1)q-(2^{r-1}-1) for q>=2^{r-1}-1.

## 5. After Zenodo minting

Record the actual article DOI and propagate it to all of:

- `CITATION.cff`;
- `metadata.json`;
- `README.md`;
- `RELEASE_NOTES.md`;
- `article_en.md`;
- `article_ru.md`;
- relevant upstream/publication index files in `delegated/FCOA_RIGIDITY_COST/`;
- any GitHub release notes for the archival tag.

Do not alter the already published Foundation DOI.

## 6. Repository freeze

After DOI propagation:

- rerun the publication workflow;
- verify fresh `MANIFEST.sha256` and verifier log;
- tag the archival source commit with a release tag such as `fcoa-lqr-v1.0`;
- treat the Zenodo-associated v1.0 manuscript as immutable except through a formally versioned correction or successor release.

## 7. Research continuation boundary

The archival v1.0 release closes the proved synchronization package through the sharp stabilization theorem. New work on

`4 <= q < 2^{r-1}-1`, `r>=5`

belongs to a successor research cycle and must not silently modify the claims of the frozen v1.0 article.
