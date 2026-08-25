#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from dirichlet_spectrum import warped_spectrum  # noqa: E402
from realzero_irregular_spectrum import (  # noqa: E402
    common_shift,
    direct_spectrum,
    load_and_concat,
    local_peaks,
)


def score_targets(omega: np.ndarray, score: np.ndarray, m_min: int, m_max: int) -> float:
    targets = np.log(np.arange(m_min, m_max + 1, dtype=float))
    return float(np.mean(np.interp(targets, omega, score)))


def summarize(omega: np.ndarray, score: np.ndarray, m_min: int, m_max: int) -> dict:
    out = {
        "exact_target_score": score_targets(omega, score, m_min, m_max),
    }
    out.update(common_shift(omega, score, m_min, m_max))
    out["local_peaks"] = local_peaks(omega, score, m_min, m_max)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("datasets", nargs="+", type=Path)
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--stop", type=int, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--csv", type=Path, required=True)
    ap.add_argument("--block-size", type=int, default=1000)
    args = ap.parse_args()

    d = load_and_concat(args.datasets)
    sel = (d["loops"] >= args.start) & (d["loops"] <= args.stop)
    loops = d["loops"][sel]
    area = np.asarray(d["area"][sel], dtype=float)
    t = 0.5 * (d["gamma0"][sel] + d["gamma1"][sel])

    expected = np.arange(args.start, args.stop + 1)
    if len(loops) != len(expected) or not np.array_equal(loops, expected):
        raise SystemExit("requested loop range is not contiguous")

    omega_d, score_d = direct_spectrum(area, t, block_size=args.block_size)
    smooth = warped_spectrum(
        area,
        t,
        block_size=args.block_size,
        omega_min=0.40,
        omega_max=3.50,
        omega_step=0.0005,
    )
    omega_s = smooth.omega
    score_s = smooth.score

    result = {
        "start": args.start,
        "stop": args.stop,
        "n_loops": int(len(loops)),
        "block_size": args.block_size,
        "observable": "area_winding",
        "time": "actual zero-pair midpoint",
        "direct_method": "irregular-time Lomb-Scargle",
        "smooth_method": "RH-SOL-01/02 blockwise local dt/dn frequency mapping",
        "m2_13": {
            "direct": summarize(omega_d, score_d, 2, 13),
            "smooth": summarize(omega_s, score_s, 2, 13),
        },
        "m2_11": {
            "direct": summarize(omega_d, score_d, 2, 11),
            "smooth": summarize(omega_s, score_s, 2, 11),
        },
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    score_s_interp = np.interp(omega_d, omega_s, score_s)
    arr = np.column_stack([omega_d, score_d, score_s_interp])
    args.csv.parent.mkdir(parents=True, exist_ok=True)
    np.savetxt(args.csv, arr, delimiter=",", header="omega,direct_score,smooth_score", comments="")

    print(json.dumps({
        "m2_13": {
            "direct_score": result["m2_13"]["direct"]["exact_target_score"],
            "direct_shift": result["m2_13"]["direct"]["best_shift"],
            "smooth_score": result["m2_13"]["smooth"]["exact_target_score"],
            "smooth_shift": result["m2_13"]["smooth"]["best_shift"],
        },
        "m2_11": {
            "direct_score": result["m2_11"]["direct"]["exact_target_score"],
            "direct_shift": result["m2_11"]["direct"]["best_shift"],
            "smooth_score": result["m2_11"]["smooth"]["exact_target_score"],
            "smooth_shift": result["m2_11"]["smooth"]["best_shift"],
        },
    }, indent=2))
    print(f"WROTE {args.out}")
    print(f"WROTE {args.csv}")


if __name__ == "__main__":
    main()
