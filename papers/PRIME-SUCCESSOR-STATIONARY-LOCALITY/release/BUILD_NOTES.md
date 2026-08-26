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
- margins: 1.00 in left/right unless a later visual pass proves a small adjustment necessary;
- body: professional serif, approximately 11 pt;
- display equations centered with breathing room above and below;
- title page with title, subtitle, author, ORCID, version/date;
- Heading 1/2 hierarchy preserved;
- no decorative heavy borders;
- restrained monochrome/accent treatment suitable for a mathematical preprint;
- references kept together where possible;
- no internal research-status notes in the publication body.

## Equation numbering geometry - hard layout rule

Numbered display equations must never be positioned with manual spaces or tab characters.

For the DOCX master, every numbered equation is laid out in a **borderless three-column row** spanning the text block:

1. left balancing cell: **0.80 in**;
2. equation cell: remaining width, equation centered;
3. equation-number cell: **0.80 in**, number right-aligned.

The left and right balancing cells are equal so the equation remains centered on the page independently of the width of the equation number.

The equation-number cell has a fixed **0.10 in right inset** from the text-block edge. With a 1.00 in page margin this places the right edge of every equation number at the same position: **1.10 in from the paper edge**.

The equation cell and number cell must preserve a minimum visible horizontal gutter of **0.25 in (18 pt)** between the mathematical content and the left edge of the equation number. If a long equation would violate this gutter, the equation must be broken over multiple centered lines; the number must never be pushed inward toward the formula and the formula must never be squeezed to make room for the number.

Equation numbers are vertically centered against the display row and use one consistent format throughout both language editions. The EN and RU builds must use the same numbering sequence.

### Equation-number visual QA

Inspect every page containing numbered equations and verify all of the following:

- equation-number right edges form one visually straight vertical line;
- the distance from that line to the right text margin is constant;
- no number visually touches or crowds the formula;
- the minimum equation-to-number gutter is at least 0.25 in;
- long equations wrap/break before the gutter is violated;
- multi-line equations keep one number centered vertically against the entire display block;
- EN and RU versions use identical equation numbers for corresponding formulas.

### Equation-number coordinate QA

In addition to visual inspection, the final PDF preflight should verify the geometry numerically from text bounding boxes whenever extraction permits it:

- right-edge spread of all equation-number boxes on ordinary text pages: target `<= 1 pt`;
- nominal right-edge location: text-block right edge minus `7.2 pt` (0.10 in);
- minimum horizontal gap from formula box to equation-number box: `>= 18 pt`;
- any violation is a release blocker and requires re-layout plus full re-render.

This check supplements, but does not replace, page-image inspection.

## Required DOCX workflow

Author the DOCX from the final Markdown with proper Word paragraph styles and equation-safe text. Then render each DOCX using the canonical DOCX renderer:

```bash
python /home/oai/skills/docx/render_docx.py stationary_locality_en.docx --output_dir qa_docx_en --emit_pdf
python /home/oai/skills/docx/render_docx.py stationary_locality_ru.docx --output_dir qa_docx_ru --emit_pdf
```

Inspect **every** `page-*.png` at 100% zoom. Required checks:

- all equations visible;
- equation numbers obey the fixed geometry above;
- no missing Greek/Cyrillic glyphs;
- no clipping or overlap;
- no orphaned section headings;
- no malformed bibliography entries;
- consistent title-page metadata;
- EN/RU theorem and equation numbering aligned.

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

Inspect every PDF page. PDF page count and visible content must agree with the final DOCX build. Re-check the equation-number vertical line and the minimum formula-number gutter after PDF conversion.

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
Equation-number geometry: LOCKED by the rule above.  
DOCX/PDF visual QA: REQUIRED BEFORE RELEASE.  
Zenodo DOI: NOT YET ASSIGNED.
