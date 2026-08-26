#!/usr/bin/env python3
"""Minimal, dependency-free converter for the canonical Stationary Locality manuscripts.

The manuscripts already contain LaTeX math delimiters. This script preserves inline math,
turns display blocks into numbered equation environments, keeps long boxed slogan displays
unnumbered, and converts the limited Markdown used by the article into LaTeX prose.

Usage:
  python md_to_tex.py ../manuscript/article_en.md article_en_body.tex --language en
  python md_to_tex.py ../manuscript/article_ru.md article_ru_body.tex --language ru
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

SPECIAL = {
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
}


def esc_plain(s: str) -> str:
    out = []
    for ch in s:
        if ch == "~":
            out.append(r"\textasciitilde{}")
        elif ch == "^":
            out.append(r"\textasciicircum{}")
        elif ch == "\\":
            out.append(r"\textbackslash{}")
        else:
            out.append(SPECIAL.get(ch, ch))
    return "".join(out)


def inline_convert(s: str) -> str:
    """Convert prose while preserving \(...\), markdown bold, italics, and code spans."""
    result = []
    i = 0
    n = len(s)
    while i < n:
        if s.startswith(r"\(", i):
            j = s.find(r"\)", i + 2)
            if j == -1:
                result.append(esc_plain(s[i:]))
                break
            result.append(s[i:j + 2])
            i = j + 2
            continue
        if s.startswith("**", i):
            j = s.find("**", i + 2)
            if j != -1:
                result.append(r"\textbf{" + inline_convert(s[i + 2:j]) + "}")
                i = j + 2
                continue
        if s[i] == "*":
            j = s.find("*", i + 1)
            if j != -1:
                result.append(r"\emph{" + inline_convert(s[i + 1:j]) + "}")
                i = j + 1
                continue
        if s[i] == "`":
            j = s.find("`", i + 1)
            if j != -1:
                code = s[i + 1:j].replace("\\", r"\textbackslash{}")
                code = code.replace("_", r"\_").replace("#", r"\#")
                result.append(r"\texttt{" + code + "}")
                i = j + 1
                continue
        # Consume ordinary prose up to the next special construct.
        candidates = [p for p in (
            s.find(r"\(", i), s.find("**", i), s.find("*", i), s.find("`", i)
        ) if p != -1]
        j = min(candidates) if candidates else n
        if j == i:
            result.append(esc_plain(s[i]))
            i += 1
        else:
            result.append(esc_plain(s[i:j]))
            i = j
    return "".join(result)


def display_env(content: str) -> str:
    c = content.strip()
    # Long boxed prose slogans should remain display statements but not acquire a cramped tag.
    unnumbered = (r"\boxed" in c and r"\text" in c) or len(c) > 420
    env = "equation*" if unnumbered else "equation"
    return f"\\begin{{{env}}}\n{c}\n\\end{{{env}}}\n"


def convert(md: str, language: str) -> str:
    lines = md.splitlines()
    out = []
    in_display = False
    display = []
    list_mode = None
    skipped_frontmatter = 0

    def close_list():
        nonlocal list_mode
        if list_mode:
            out.append(f"\\end{{{list_mode}}}\n")
            list_mode = None

    for raw in lines:
        line = raw.rstrip()

        # Canonical title/author metadata are rebuilt by the LaTeX master.
        if skipped_frontmatter < 7:
            skipped_frontmatter += 1
            continue

        if in_display:
            if line.strip() == r"\]":
                out.append(display_env("\n".join(display)))
                display = []
                in_display = False
            else:
                display.append(line)
            continue

        if line.strip() == r"\[":
            close_list()
            in_display = True
            continue

        if line.strip() == "---":
            close_list()
            out.append("\n")
            continue

        if not line.strip():
            close_list()
            out.append("\n")
            continue

        if line.startswith("## "):
            close_list()
            title = line[3:].strip()
            if title in {"Abstract", "Аннотация"}:
                continue
            if title in {"References", "Литература", "Author note", "Авторская заметка"}:
                out.append(r"\section*{" + inline_convert(title) + "}\n")
            else:
                out.append(r"\section*{" + inline_convert(title) + "}\n")
                out.append(r"\addcontentsline{toc}{section}{" + inline_convert(title) + "}\n")
            continue

        if line.startswith("### "):
            close_list()
            out.append(r"\subsection*{" + inline_convert(line[4:].strip()) + "}\n")
            continue

        m = re.match(r"^\s*-\s+(.*)$", line)
        if m:
            if list_mode != "itemize":
                close_list()
                list_mode = "itemize"
                out.append(r"\begin{itemize}" + "\n")
            out.append(r"\item " + inline_convert(m.group(1)) + "\n")
            continue

        m = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
        if m:
            if list_mode != "enumerate":
                close_list()
                list_mode = "enumerate"
                out.append(r"\begin{enumerate}" + "\n")
            out.append(r"\item " + inline_convert(m.group(2)) + "\n")
            continue

        close_list()
        out.append(inline_convert(line) + "\n")

    close_list()
    if in_display:
        raise ValueError("Unclosed display-math block")

    return "".join(out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--language", choices=("en", "ru"), required=True)
    args = ap.parse_args()
    text = args.source.read_text(encoding="utf-8")
    converted = convert(text, args.language)
    args.output.write_text(converted, encoding="utf-8")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
