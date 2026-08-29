# Zenodo finalization checklist

This package intentionally contains **no invented DOI**.

## 1. Create draft and reserve DOI

1. Create a new Zenodo upload.
2. Resource type: **Publication**.
3. Publication subtype: **Preprint** (unless a different final publication type is intentionally chosen).
4. In the DOI field choose that the upload does not already have a DOI, then use **Get a DOI now!**.
5. Do not delete the draft after reservation; a reserved DOI belongs to that draft until publication.

## 2. Metadata

Main title:

> Reflections on Hybrid Memory with Commander Sol: Minimal Joint Rigidity of Partial Operations

Translated Russian title:

> Размышлизмы о гибридной памяти с Commander Sol: минимальная совместная жёсткость частичных операций

Creator:

- Family name: Malachevsky
- Given name: Alex
- ORCID: 0009-0008-6009-3196

Publication date: the actual first-publication date (currently planned as 2026-08-29).

License: **CC BY 4.0**.

Access: **Open**.

Suggested keywords are in `ZENODO_METADATA.json`.

If the project community identifier is confirmed in the Zenodo UI, submit the record to the Commander Sol mathematics community as part of the deposit workflow.

## 3. Insert reserved DOI before upload

Replace every explicit `pending reservation` / `ожидает резервирования` marker in the publication sources and metadata, then rebuild both PDFs with XeLaTeX.

## 4. Reproducibility gate

Run:

```bash
python3 supplement/verify_minimal_classifications.py
```

Required tail line:

```text
ALL CHECKS PASSED
```

The expected counts are recorded in `supplement/verification_output.txt`.

## 5. Render audit

Render the rebuilt PDFs to images and inspect at least:

- title page;
- one theorem/proof page;
- classification page;
- final references page.

Reject the build if there are clipped equations, missing Cyrillic glyphs, undefined references, overfull boxes that leave the text area, or metadata mismatches.

## 6. Files recommended for the Zenodo record

Primary files:

- final English PDF;
- final Russian PDF.

Reproducibility/source files:

- source-package ZIP containing the two TeX files, bibliography companion, verification script, verification output, README, audit, CFF and metadata.

The record is still a **Publication**, because the paper is the primary contribution; the script is supporting material.

## 7. Final repository update

After Zenodo publication:

1. record the final DOI and persistent URL in `CITATION.cff` and `README.md`;
2. change version from RC to `1.0.0`;
3. replace release-candidate checksums in the manifest with final ones;
4. commit the DOI update to the paper branch;
5. if a GitHub release is used, tag it consistently with the Zenodo version.