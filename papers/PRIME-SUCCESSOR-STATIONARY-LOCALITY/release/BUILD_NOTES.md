# Reproducible Build Notes - Stationary Locality v1.0

These notes describe the final binary build and QA sequence. The Markdown manuscripts are the canonical text sources.

## Canonical sources

- `../manuscript/article_en.md`
- `../manuscript/article_ru.md`
- `../FINITE_STATIONARY_LOCALITY_THEOREM.md`
- `../FINAL_LINE_BY_LINE_AUDIT.md`

## Output names

- `stationary_locality_en.docx`
- `stationary_locality_ru.docx`
- `stationary_locality_en.pdf`
- `stationary_locality_ru.pdf`

## Document design

- page size: Letter, portrait;
- body: professional serif, approximately 11 pt;
- display equations centered with breathing room above and below;
- title page with title, subtitle, author, ORCID, version/date;
- Heading 1/2 hierarchy preserved;
- no decorative heavy borders;
- restrained monochrome/accent treatment suitable for a mathematical preprint;
- references kept together where possible;
- no internal research-status notes in the publication body.

## Required DOCX workflow

Author the DOCX from the final Markdown with proper Word paragraph styles and equation-safe text. Then render each DOCX using the canonical DOCX renderer:

```bash
python /home/oai/skills/docx/render_docx.py stationary_locality_en.docx --output_dir qa_docx_en --emit_pdf
python /home/oai/skills/docx/render_docx.py stationary_locality_ru.docx --output_dir qa_docx_ru --emit_pdf
```

Inspect **every** `page-*.png` at 100% zoom. Required checks:

- all equations visible;
- no missing Greek/Cyrillic glyphs;
- no clipping or overlap;
- no orphaned section headings;
- no malformed bibliography entries;
- consistent title-page metadata;
- EN/RU theorem numbering aligned.

Any edit requires a new full render pass.

## Required PDF workflow

Generate PDF from the verified document/source. LibreOffice conversion from the visually verified DOCX is acceptable:

```bash
python /home/oai/skills/pdfs/scripts/lo_convert_to_pdf.py stationary_locality_en.docx --out_dir pdf_out
python /home/oai/skills/pdfs/scripts/lo_convert_to_pdf.py stationary_locality_ru.docx --out_dir pdf_out
```

Then render each final PDF:

```bash
python /home/oai/skills/pdfs/scripts/render_pdf.py pdf_out/stationary_locality_en.pdf --out_dir qa_pdf_en --dpi 200
python /home/oai/skills/pdfs/scripts/render_pdf.py pdf_out/stationary_locality_ru.pdf --out_dir qa_pdf_ru --dpi 200
```

Inspect every PDF page. PDF page count and visible content must agree with the final DOCX build.

## Text-level preflight

Before checksums, verify the final sources and binaries contain none of:

- `TODO`;
- placeholder DOI text presented as an assigned DOI;
- internal tool citation markers;
- claims of decidability/NIP/stability not present in the theorem;
- a claim that the uniformly indexed atlas has GIR infinity;
- the obsolete bounded-complete-affine-tuple lemma;
- the false claim that `Q/H_m` is finite.

## Package assembly

Copy into one clean package directory:

1. four final binaries;
2. two canonical Markdown manuscripts;
3. theorem proof checkpoint;
4. final line-by-line audit;
5. paper README;
6. `zenodo_metadata.md`;
7. `zenodo_metadata.json`;
8. `CITATION.cff`;
9. `LICENSE.md`;
10. this file.

Compute checksums only after all files are final:

```bash
sha256sum * > SHA256SUMS.txt
```

Then create the deposit ZIP:

```bash
zip -9 -r stationary_locality_zenodo_package_v1.0.zip .
```

Finally compute the ZIP checksum separately.

## Zenodo gate

The Zenodo DOI must not be written into the canonical metadata or CFF until the deposit record has assigned it. After assignment, update:

- Zenodo metadata;
- `CITATION.cff`;
- README/release note if desired;
- checksum files if any packaged source changed.

## Current build state

Mathematical line-by-line audit: PASS after incorporated local repairs.  
Canonical EN/RU Markdown sources: READY.  
DOCX/PDF visual QA: REQUIRED BEFORE RELEASE.  
Zenodo DOI: NOT YET ASSIGNED.
