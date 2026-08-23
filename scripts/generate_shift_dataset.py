#!/usr/bin/env python3
"""Generate RH-SOL-02 shifted-lattice calibration data from zeta zeros."""
from __future__ import annotations

import argparse
import csv
import json
import platform
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from zeta_argand import load_zero_table, sample_argand_loop, save_loop
from shifted_lattice import (
    filled_area,
    scan_translations_fast,
)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--stop", type=int, default=10)
    ap.add_argument("--dps", type=int, default=30)
    ap.add_argument("--segments", type=int, default=60)
    ap.add_argument("--adaptive", action="store_true")
    ap.add_argument("--curve-rel-tol", type=float, default=2e-5)
    ap.add_argument("--curve-abs-tol", type=float, default=2e-8)
    ap.add_argument("--max-depth", type=int, default=10)
    ap.add_argument("--q", type=int, nargs="+", default=[8, 16, 32])
    ap.add_argument(
        "--rules",
        nargs="+",
        choices=["winding", "even-odd"],
        default=["winding", "even-odd"],
    )
    ap.add_argument("--boundary-tol", type=float, default=1e-10)
    ap.add_argument("--zero-table", type=Path)
    ap.add_argument("--save-loops", action="store_true")
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("data/derived/rh-sol-02-shift"),
    )
    args = ap.parse_args()

    zeros = load_zero_table(args.zero_table) if args.zero_table else None
    args.out.mkdir(parents=True, exist_ok=True)
    rows = []

    for n in range(args.start, args.stop + 1):
        loop = sample_argand_loop(
            n,
            dps=args.dps,
            initial_segments=args.segments,
            adaptive=args.adaptive,
            curve_rel_tol=args.curve_rel_tol,
            curve_abs_tol=args.curve_abs_tol,
            max_depth=args.max_depth,
            zeros=zeros,
        )
        if args.save_loops:
            save_loop(loop, args.out / "loops" / f"loop_{n:06d}.npz")

        for rule in args.rules:
            area = filled_area(loop.vertices, rule=rule)
            for q in args.q:
                counts = scan_translations_fast(
                    loop.vertices,
                    q,
                    rule=rule,
                    boundary_tol=args.boundary_tol,
                )
                values = np.array([c.count for c in counts], dtype=np.int32)
                np.savez_compressed(
                    args.out / f"loop_{n:06d}_{rule}_q{q}.npz",
                    counts=values.reshape(q, q),
                )
                rows.append(
                    {
                        "loop": n,
                        "gamma0": loop.metadata.gamma0,
                        "gamma1": loop.metadata.gamma1,
                        "vertices": loop.metadata.vertices,
                        "zeta_evaluations": loop.metadata.zeta_evaluations,
                        "zero_source": loop.metadata.zero_source,
                        "rule": rule,
                        "q": q,
                        "filled_area": area,
                        "mean_count": float(values.mean()),
                        "variance": float(values.var()),
                        "mean_minus_area": float(values.mean() - area),
                        "min_count": int(values.min()),
                        "max_count": int(values.max()),
                    }
                )
        print(f"loop {n}: vertices={loop.metadata.vertices}")

    with (args.out / "summary.csv").open(
        "w", encoding="utf-8", newline=""
    ) as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    manifest = {
        "range": [args.start, args.stop],
        "dps": args.dps,
        "segments": args.segments,
        "adaptive": args.adaptive,
        "curve_rel_tol": args.curve_rel_tol,
        "curve_abs_tol": args.curve_abs_tol,
        "max_depth": args.max_depth,
        "q": args.q,
        "rules": args.rules,
        "boundary_tol": args.boundary_tol,
        "zero_table": str(args.zero_table) if args.zero_table else None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "mpmath": mp.__version__,
    }
    (args.out / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
