#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from zeta_argand import load_zero_table, sample_argand_loop
from shifted_lattice import scan_translations_fast, filled_area


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--stop", type=int, required=True)
    ap.add_argument("--zero-table", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--dps", type=int, default=30)
    ap.add_argument("--segments", type=int, default=60)
    ap.add_argument("--adaptive", action="store_true")
    ap.add_argument("--q", type=int, nargs="+", default=[8, 16, 32])
    ap.add_argument(
        "--rules",
        nargs="+",
        choices=["winding", "even-odd"],
        default=["winding", "even-odd"],
    )
    ap.add_argument("--boundary-tol", type=float, default=1e-10)
    args = ap.parse_args()

    if args.stop < args.start:
        raise SystemExit("--stop must be >= --start")

    zeros = load_zero_table(args.zero_table)
    missing = [n for n in range(args.start, args.stop + 2) if n not in zeros]
    if missing:
        raise SystemExit(f"zero table missing indices: {missing[:10]}")

    L = args.stop - args.start + 1
    loops = np.arange(args.start, args.stop + 1, dtype=np.int32)
    gamma0 = np.empty(L, dtype=np.float64)
    gamma1 = np.empty(L, dtype=np.float64)
    vertices = np.empty(L, dtype=np.int32)
    area = {r: np.empty(L, dtype=np.float64) for r in args.rules}
    counts = {
        (r, q): np.empty((L, q, q), dtype=np.int16)
        for r in args.rules
        for q in args.q
    }

    for ii, n in enumerate(loops):
        loop = sample_argand_loop(
            int(n),
            dps=args.dps,
            initial_segments=args.segments,
            adaptive=args.adaptive,
            zeros=zeros,
        )
        gamma0[ii] = loop.metadata.gamma0
        gamma1[ii] = loop.metadata.gamma1
        vertices[ii] = loop.metadata.vertices

        for rule in args.rules:
            area[rule][ii] = filled_area(loop.vertices, rule=rule)
            for q in args.q:
                vals = np.array(
                    [
                        c.count
                        for c in scan_translations_fast(
                            loop.vertices,
                            q,
                            rule=rule,
                            boundary_tol=args.boundary_tol,
                        )
                    ],
                    dtype=np.int16,
                )
                counts[(rule, q)][ii] = vals.reshape(q, q)

        print(f"loop {n}: vertices={vertices[ii]}", flush=True)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "loops": loops,
        "gamma0": gamma0,
        "gamma1": gamma1,
        "vertices": vertices,
    }
    for rule in args.rules:
        key_rule = rule.replace("-", "_")
        payload[f"area_{key_rule}"] = area[rule]
        for q in args.q:
            payload[f"counts_{key_rule}_q{q}"] = counts[(rule, q)]

    metadata = {
        "start": args.start,
        "stop": args.stop,
        "dps": args.dps,
        "segments": args.segments,
        "adaptive": args.adaptive,
        "q": args.q,
        "rules": args.rules,
        "boundary_tol": args.boundary_tol,
        "zero_table": str(args.zero_table),
    }
    payload["metadata_json"] = np.array(json.dumps(metadata, sort_keys=True))
    np.savez_compressed(args.out, **payload)


if __name__ == "__main__":
    main()
