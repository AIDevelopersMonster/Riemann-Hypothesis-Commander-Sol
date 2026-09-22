# Build instructions

Recommended publication build:

```bash
pandoc paper.md \
  --from markdown+tex_math_dollars \
  --citeproc \
  --bibliography references.bib \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V fontsize=10pt \
  -V documentclass=article \
  -o HATTER_SOL_20_21.pdf
```

Generate LaTeX source:

```bash
pandoc paper.md \
  --from markdown+tex_math_dollars \
  --citeproc \
  --bibliography references.bib \
  --standalone \
  -V geometry:margin=1in \
  -V fontsize=10pt \
  -V documentclass=article \
  -o HATTER_SOL_20_21.tex
```

Before release, render the PDF page-by-page and inspect tables, equations, citations and page breaks.
