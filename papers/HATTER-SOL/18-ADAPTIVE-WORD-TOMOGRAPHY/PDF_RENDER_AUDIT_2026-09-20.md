# HATTER-SOL-18 · PDF RENDER AUDIT

**Date:** 20 September 2026  
**Status:** CLEAN  
**Release status after this audit:** \`PUBLICATION_READY\`

## Inputs

Canonical frozen Markdown:

- \`HATTER_SOL_18_RU_FROZEN_v1.0-rc1.md\`
- \`HATTER_SOL_18_EN_FROZEN_v1.0-rc1.md\`

Build workflow:

- \`.github/workflows/hatter-sol-18-publication-pdf.yml\`
- successful final run: \`35470003010\`
- head SHA: \`9d6c0bdc4432953e05bbaff39c53ddb7afbdd7fe\`
- artifact: \`HATTER-SOL-18-publication-pdfs\`
- artifact ID: \`10592557220\`

## Final PDF outputs

### Russian

\`\`\`text
HATTER_SOL_18_RU_v1.0.pdf
pages: 18
paper: A4
SHA-256:
12f07e2ec2f21ec551eadbda4f8ec71e7b999ae51a9b9ccaa6a8c672d2c8a70d
\`\`\`

### English

\`\`\`text
HATTER_SOL_18_EN_v1.0.pdf
pages: 15
paper: A4
SHA-256:
270e8c24b75cb97c71aee281147e5d7652f262d90dfdb476bd5cd91bcdf05190
\`\`\`

## Render procedure

Both PDFs were rendered page-by-page to PNG at 160 DPI with the canonical PDF
render script:

\`\`\`text
python /home/oai/skills/pdfs/scripts/render_pdf.py <pdf> --out_dir <dir> --dpi 160
\`\`\`

All 18 RU pages and all 15 EN pages rendered successfully.

A complete contact-sheet review was followed by full-size inspection of the
publication-critical pages, including:

- title and table of contents;
- H18 temporal/spatial Cyclone-V comparison table;
- H17/H18 matched Cyclone-V comparison table;
- H18-12 hardware-image section;
- publication-freeze section;
- final bibliography pages.

## Visual findings

No blocking render defect was observed:

- no clipped page content;
- no table overflow outside the text block;
- no formula clipping;
- no overlapping text;
- no broken Cyrillic glyphs;
- no visible replacement/tofu glyphs;
- no missing final bibliography entries;
- page numbers and margins remain consistent.

The final last pages visibly contain

\`\`\`text
Release status: PUBLICATION_READY.
\`\`\`

## Text-extraction sanity checks

For both final PDFs:

- \`PUBLICATION_READY_PENDING_RENDER_AUDIT\` count: 0;
- \`PUBLICATION_READY\` count: 1;
- Unicode replacement glyph U+FFFD count: 0;
- NUL byte count in extracted text: 0.

## Build note

The first reproducible PDF build exposed an ordering defect in the custom
LaTeX header (\`\hypersetup\` appeared before Hyperref was available).  The
workflow was repaired without changing manuscript content.  The subsequent
build completed successfully.

During pre-build source hygiene, frozen Markdown was also checked for accidental
control characters introduced by an earlier scripted edit.  Those render-only
source defects were repaired before the final build; no mathematical claim was
changed.

## Final gate

- source compiled: **yes**
- PDF visually inspected: **yes**
- bibliography visually present: **yes**
- metadata/title/author checked: **yes**
- final release status: **PUBLICATION_READY**
