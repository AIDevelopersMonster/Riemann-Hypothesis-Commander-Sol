# LaTeX build - Stationary Locality v1.0

The canonical mathematical text remains in `../manuscript/article_en.md` and `../manuscript/article_ru.md`. This directory provides the publication LaTeX layer.

## Files

- `stationary_locality.sty` - shared typography, Letter layout, title page, and equation-number geometry;
- `md_to_tex.py` - dependency-free converter for the limited Markdown used by the canonical manuscripts;
- `article_en.tex` - English master;
- `article_ru.tex` - Russian master;
- generated at build time: `article_en_body.tex`, `article_ru_body.tex`.

## Build

From this directory:

```bash
python md_to_tex.py ../manuscript/article_en.md article_en_body.tex --language en
python md_to_tex.py ../manuscript/article_ru.md article_ru_body.tex --language ru

lualatex -interaction=nonstopmode -halt-on-error article_en.tex
lualatex -interaction=nonstopmode -halt-on-error article_en.tex

lualatex -interaction=nonstopmode -halt-on-error article_ru.tex
lualatex -interaction=nonstopmode -halt-on-error article_ru.tex
```

LuaLaTeX is intentional: the Russian edition and the mathematical typography use Unicode/OpenType fonts.

## Display-equation policy

The converter turns ordinary canonical `\[ ... \]` display blocks into numbered `equation` environments. Long boxed prose slogans and exceptionally long display blocks are left unnumbered so that a formula number is never squeezed against mathematical content.

The shared style implements the release gate requested for equation numbers:

- centered display mathematics;
- all printed equation-number right edges aligned by the TeX display mechanism;
- printed number inset: `0.10 in` from the text-block right edge;
- `\minalignsep = 18pt`, matching the required minimum formula-to-number breathing room for aligned displays;
- long displays must be broken or left unnumbered rather than allowing the number to crowd the formula.

## Required QA before release

After compiling both editions:

1. render every PDF page to PNG at 200 dpi;
2. inspect every page visually;
3. confirm no clipping, missing Cyrillic/Greek glyphs, bad line breaks, or orphan headings;
4. verify that equation-number right edges form one vertical line;
5. verify a minimum visible formula-to-number gutter of 18 pt wherever a tag shares the display line;
6. compare EN/RU equation-number sequences;
7. only after the PDFs pass, compute release checksums and build the Zenodo ZIP.

The LaTeX layer does not introduce new mathematics. It is a publication rendering of the audited canonical manuscripts.
