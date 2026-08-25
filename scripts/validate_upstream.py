#!/usr/bin/env python3
"""Validate regenerated unshifted lattice incidences against RH-SOL-01 CSV."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from zeta_argand import sample_argand_loop
from shifted_lattice import interior_lattice_points


def read_incidence_csv(path: Path) -> dict[int, set[tuple[int, int]]]:
    out: dict[int, set[tuple[int, int]]] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            n = int(row["loop"])
            out.setdefault(n, set()).add((int(row["a"]), int(row["b"])))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("incidences", type=Path)
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--stop", type=int, default=30)
    ap.add_argument("--segments", type=int, nargs="+", default=[60, 120, 240])
    ap.add_argument("--dps", type=int, default=30)
    ap.add_argument("--boundary-tol", type=float, default=1e-10)
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("papers/RH-SOL-02-SHIFT/analysis/upstream_validation.json"),
    )
    args = ap.parse_args()

    published = read_incidence_csv(args.incidences)
    report = {
        "range": [args.start, args.stop],
        "dps": args.dps,
        "boundary_tol": args.boundary_tol,
        "runs": [],
    }

    for segments in args.segments:
        mismatches = []
        extra_total = 0
        missing_total = 0
        generated_total = 0
        published_total = 0

        for n in range(args.start, args.stop + 1):
            loop = sample_argand_loop(
                n,
                dps=args.dps,
                initial_segments=segments,
                adaptive=False,
            )
            pts = interior_lattice_points(
                loop.vertices,
                (0.0, 0.0),
                rule="winding",
                boundary_tol=args.boundary_tol,
            )
            got = {
                (int(round(x)), int(round(y)))
                for x, y in pts
                if not (abs(x) < 1e-12 and abs(y) < 1e-12)
            }
            ref = published.get(n, set())
            generated_total += len(got)
            published_total += len(ref)
            extra = sorted(got - ref)
            missing = sorted(ref - got)
            extra_total += len(extra)
            missing_total += len(missing)
            if extra or missing:
                mismatches.append(
                    {"loop": n, "extra": extra, "missing": missing}
                )

        report["runs"].append(
            {
                "segments": segments,
                "mismatch_loops": len(mismatches),
                "extra_points": extra_total,
                "missing_points": missing_total,
                "generated_total": generated_total,
                "published_total": published_total,
                "mismatches": mismatches,
            }
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
