#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dirichlet_spectrum import (
    benjamini_hochberg,
    jitter_null,
    score_comb_with_null,
    warped_spectrum,
)


def load_legacy_time(path: Path, loops: np.ndarray) -> np.ndarray:
    mapping: dict[int, float] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or "loop" not in reader.fieldnames or "t_near" not in reader.fieldnames:
            raise SystemExit("legacy time CSV must contain loop,t_near columns")
        for row in reader:
            mapping[int(row["loop"])] = float(row["t_near"])
    try:
        return np.array([mapping[int(n)] for n in loops], dtype=float)
    except KeyError as exc:
        raise SystemExit(f"legacy time CSV missing loop {exc.args[0]}") from exc


def comb_dict(result) -> dict[str, float]:
    return {
        "score": float(result.score),
        "null_median": float(result.null_median),
        "null_q95": float(result.null_q95),
        "null_q99": float(result.null_q99),
        "empirical_p_ge": float(result.empirical_p_ge),
        "best_common_shift": float(result.best_common_shift),
        "best_common_shift_score": float(result.best_common_shift_score),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", type=Path, required=True)
    ap.add_argument("--rule", choices=["winding", "even-odd"], default="winding")
    ap.add_argument("--q", type=int, default=16)
    ap.add_argument("--legacy-time-csv", type=Path)
    ap.add_argument("--B", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=20260822)
    ap.add_argument("--out-prefix", type=Path, required=True)
    args = ap.parse_args()

    key_rule = args.rule.replace("-", "_")
    with np.load(args.dataset, allow_pickle=False) as z:
        loops = z["loops"].astype(int)
        counts = z[f"counts_{key_rule}_q{args.q}"].astype(float)
        area = z[f"area_{key_rule}"].astype(float)
        gamma0 = z["gamma0"].astype(float)
        gamma1 = z["gamma1"].astype(float)

    if len(loops) % 1000:
        raise SystemExit("EXP-01 spectral analysis requires loop count divisible by 1000")

    if args.legacy_time_csv:
        time_proxy = load_legacy_time(args.legacy_time_csv, loops)
        time_mode = "RH-SOL-01 legacy t_near"
    else:
        time_proxy = 0.5 * (gamma0 + gamma1)
        time_mode = "zero-pair midpoint"

    # Finite-q translation zero mode and exact continuous-area calibration target.
    translation_mean = counts.mean(axis=(1, 2))
    residual = counts - translation_mean[:, None, None]

    diff = translation_mean - area
    mae = float(np.mean(np.abs(diff)))
    rms = float(math.sqrt(np.mean(diff * diff)))
    max_abs = float(np.max(np.abs(diff)))
    corr = float(np.corrcoef(translation_mean, area)[0, 1])

    zero_var = float(np.var(translation_mean))
    residual_var = float(np.mean(residual * residual))
    variance_fraction_zero_mode = zero_var / (zero_var + residual_var) if zero_var + residual_var > 0 else float("nan")

    area_result = score_comb_with_null(
        warped_spectrum(area, time_proxy), B=args.B, seed=args.seed
    )
    mean_result = score_comb_with_null(
        warped_spectrum(translation_mean, time_proxy), B=args.B, seed=args.seed + 1
    )

    rows: list[dict[str, float | int]] = []
    q = args.q
    for iy in range(q):
        for ix in range(q):
            spectrum = warped_spectrum(residual[:, iy, ix], time_proxy)
            observed, null = jitter_null(
                spectrum,
                B=args.B,
                seed=args.seed + 1000 + iy * q + ix,
            )
            p = (1.0 + float(np.sum(null >= observed))) / (args.B + 1.0)
            rows.append(
                {
                    "iy": iy,
                    "ix": ix,
                    "dx": (ix + 0.5) / q,
                    "dy": (iy + 0.5) / q,
                    "residual_comb_score": float(observed),
                    "p_jitter": float(p),
                    "null_median": float(np.median(null)),
                    "null_q95": float(np.quantile(null, 0.95)),
                    "null_q99": float(np.quantile(null, 0.99)),
                }
            )

    p_values = np.array([float(r["p_jitter"]) for r in rows], dtype=float)
    q_values = benjamini_hochberg(p_values)
    for row, q_bh in zip(rows, q_values):
        row["q_bh"] = float(q_bh)

    residual_scores = np.array([float(r["residual_comb_score"]) for r in rows])
    strongest = rows[int(np.argmax(residual_scores))]
    weakest = rows[int(np.argmin(residual_scores))]

    csv_path = args.out_prefix.with_suffix(".csv")
    json_path = args.out_prefix.with_suffix(".json")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "n_loops": int(len(loops)),
        "start": int(loops.min()),
        "stop": int(loops.max()),
        "q": q,
        "rule": args.rule,
        "time_proxy": time_mode,
        "B": args.B,
        "seed_base": args.seed,
        "geometry_calibration": {
            "translation_mean_minus_area_mae": mae,
            "translation_mean_minus_area_rms": rms,
            "translation_mean_minus_area_max_abs": max_abs,
            "translation_mean_area_correlation": corr,
        },
        "variance_decomposition": {
            "zero_mode_variance": zero_var,
            "translation_residual_mean_square": residual_var,
            "fraction_zero_mode": variance_fraction_zero_mode,
        },
        "area_spectrum": comb_dict(area_result),
        "finite_q_translation_mean_spectrum": comb_dict(mean_result),
        "translation_residual_map": {
            "median_comb_score": float(np.median(residual_scores)),
            "mean_comb_score": float(np.mean(residual_scores)),
            "min_comb_score": float(np.min(residual_scores)),
            "max_comb_score": float(np.max(residual_scores)),
            "fraction_p_lt_0_05": float(np.mean(p_values < 0.05)),
            "fraction_q_bh_lt_0_05": float(np.mean(q_values < 0.05)),
            "strongest_shift": strongest,
            "weakest_shift": weakest,
        },
    }
    json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
