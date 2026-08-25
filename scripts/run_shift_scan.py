#!/usr/bin/env python3
"""Run RH-SOL-02 shifted-lattice counts from sampled loop boundaries.

Input CSV columns (minimum): loop,x,y
Rows for each loop must be ordered along the sampled closed Argand curve.
"""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve()
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / "src"))

from shifted_lattice import polygon_area, scan_translations, translation_mean, translation_variance


def load_loops(path: Path) -> dict[int, np.ndarray]:
    rows: dict[int, list[tuple[float, float]]] = defaultdict(list)
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = {"loop", "x", "y"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError(f"input must contain columns {sorted(required)}")
        for row in reader:
            rows[int(row["loop"])].append((float(row["x"]), float(row["y"])))
    return {loop: np.asarray(vertices, dtype=float) for loop, vertices in rows.items()}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("input", type=Path, help="CSV with ordered loop,x,y rows")
    p.add_argument("--out", type=Path, required=True, help="output CSV")
    p.add_argument("--q", type=int, default=16, help="q x q midpoint translation grid")
    p.add_argument("--rule", choices=["winding", "even-odd"], default="winding")
    p.add_argument("--boundary-tol", type=float, default=1e-10)
    p.add_argument("--start-loop", type=int, default=None)
    p.add_argument("--end-loop", type=int, default=None)
    args = p.parse_args()

    loops = load_loops(args.input)
    selected = [n for n in sorted(loops) if (args.start_loop is None or n >= args.start_loop) and (args.end_loop is None or n <= args.end_loop)]
    if not selected:
        raise SystemExit("no loops selected")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as f:
        fields = ["loop", "dx", "dy", "count", "polygon_area", "translation_mean", "translation_variance", "q", "rule"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for n in selected:
            vertices = loops[n]
            counts = scan_translations(vertices, args.q, rule=args.rule, boundary_tol=args.boundary_tol)
            area = polygon_area(vertices)
            mean = translation_mean(counts)
            var = translation_variance(counts)
            for c in counts:
                writer.writerow({
                    "loop": n,
                    "dx": f"{c.dx:.17g}",
                    "dy": f"{c.dy:.17g}",
                    "count": c.count,
                    "polygon_area": f"{area:.17g}",
                    "translation_mean": f"{mean:.17g}",
                    "translation_variance": f"{var:.17g}",
                    "q": args.q,
                    "rule": args.rule,
                })
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
