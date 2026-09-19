#!/usr/bin/env python3
"""Compare generic Yosys JSON netlists for H17-LAB-03 and H18-LAB-01."""

from __future__ import annotations
import argparse
import json
from collections import Counter
from pathlib import Path


def summarize(path: Path, top: str):
    data = json.loads(path.read_text(encoding="utf-8"))
    mod = data["modules"][top]
    cells = mod.get("cells", {})
    types = Counter(cell["type"] for cell in cells.values())
    total = len(cells)
    seq = sum(
        n for t, n in types.items()
        if "DFF" in t or "DLATCH" in t or t.startswith("$_SDFF")
    )
    mux = sum(n for t, n in types.items() if "MUX" in t)
    return {
        "total_cells": total,
        "sequential_cells": seq,
        "mux_cells": mux,
        "top_cell_types": dict(types.most_common(20)),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--h17", type=Path, required=True)
    ap.add_argument("--h18", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    h17 = summarize(args.h17, "h17_lab03_sequential_core")
    h18 = summarize(args.h18, "h18_adaptive_erasure_core")

    delta = h18["total_cells"] - h17["total_cells"]
    pct = 100.0 * delta / h17["total_cells"]

    lines = [
        "# H17-LAB-03 vs H18-LAB-01 generic Yosys comparison",
        "",
        "Technology-independent generic synthesis only.",
        "No LUT/FF/Fmax/power claim is made.",
        "",
        "| Metric | H17-LAB-03 fixed robust8 | H18-LAB-01 adaptive erasure | Delta |",
        "|---|---:|---:|---:|",
        f"| total generic cells | {h17['total_cells']} | {h18['total_cells']} | {delta:+d} ({pct:+.2f}%) |",
        f"| sequential generic cells | {h17['sequential_cells']} | {h18['sequential_cells']} | {h18['sequential_cells']-h17['sequential_cells']:+d} |",
        f"| mux-family cells | {h17['mux_cells']} | {h18['mux_cells']} | {h18['mux_cells']-h17['mux_cells']:+d} |",
        "",
        "## H17 top cell types",
        "",
    ]
    for t, n in h17["top_cell_types"].items():
        lines.append(f"- {t}: {n}")
    lines += ["", "## H18 top cell types", ""]
    for t, n in h18["top_cell_types"].items():
        lines.append(f"- {t}: {n}")

    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
