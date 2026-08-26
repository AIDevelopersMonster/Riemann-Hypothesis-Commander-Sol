#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dirichlet_spectrum import comb_score, score_comb_with_null, warped_spectrum


def load_cube(path: Path):
    with np.load(path, allow_pickle=False) as z:
        return {
            "loops": z["loops"].astype(int),
            "gamma0": z["gamma0"].astype(float),
            "gamma1": z["gamma1"].astype(float),
            "area": z["area_winding"].astype(float),
            "counts": z["counts_winding_q16"].astype(float),
        }


def normalized_excess(result) -> float:
    den = result.null_q95 - result.null_median
    return float((result.score - result.null_median) / den) if den > 0 else float("nan")


def qdist(a: np.ndarray) -> dict[str, float]:
    x = np.asarray(a, dtype=float)
    return {
        "q05": float(np.quantile(x, 0.05)),
        "median": float(np.median(x)),
        "q95": float(np.quantile(x, 0.95)),
        "mean": float(np.mean(x)),
    }


def map_scores(field: np.ndarray, t: np.ndarray) -> np.ndarray:
    q = field.shape[1]
    out = np.empty((q, q), dtype=float)
    for iy in range(q):
        for ix in range(q):
            out[iy, ix] = comb_score(warped_spectrum(field[:, iy, ix], t))
    return out


def trend(x: np.ndarray, y: np.ndarray) -> dict[str, float]:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    pearson = stats.pearsonr(x, y)
    spearman = stats.spearmanr(x, y)
    slope, intercept, r, p, stderr = stats.linregress(x, y)
    return {
        "pearson_r": float(pearson.statistic),
        "pearson_p_descriptive": float(pearson.pvalue),
        "spearman_rho": float(spearman.statistic),
        "spearman_p_descriptive": float(spearman.pvalue),
        "ols_slope": float(slope),
        "ols_intercept": float(intercept),
        "ols_r": float(r),
        "ols_p_descriptive": float(p),
        "ols_stderr": float(stderr),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--calibration", type=Path, required=True)
    ap.add_argument("--holdout", type=Path, required=True)
    ap.add_argument("--block-size", type=int, default=1000)
    ap.add_argument("--B", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=20260822)
    ap.add_argument("--out-prefix", type=Path, required=True)
    args = ap.parse_args()

    if args.block_size != 1000:
        raise SystemExit("primary EXP-02 HEIGHT run is frozen to block-size=1000")

    a = load_cube(args.calibration)
    b = load_cube(args.holdout)

    for name, d, start, stop in [
        ("calibration", a, 1, 10000),
        ("holdout", b, 10001, 20000),
    ]:
        loops = d["loops"]
        if len(loops) != 10000 or int(loops[0]) != start or int(loops[-1]) != stop:
            raise SystemExit(f"unexpected {name} loop range")

    loops = np.concatenate([a["loops"], b["loops"]])
    gamma0 = np.concatenate([a["gamma0"], b["gamma0"]])
    gamma1 = np.concatenate([a["gamma1"], b["gamma1"]])
    area = np.concatenate([a["area"], b["area"]])
    counts = np.concatenate([a["counts"], b["counts"]], axis=0)
    tmid = 0.5 * (gamma0 + gamma1)

    if not (len(loops) == 20000 and int(loops[0]) == 1 and int(loops[-1]) == 20000):
        raise SystemExit("combined range must be loops 1..20000")

    rows: list[dict[str, object]] = []
    nblocks = len(loops) // args.block_size

    for ib in range(nblocks):
        s0 = ib * args.block_size
        s1 = s0 + args.block_size
        sl = slice(s0, s1)

        tb = tmid[sl]
        ab = area[sl]
        cb = counts[sl]
        cbar = cb.mean(axis=(1, 2))
        resid = cb - cbar[:, None, None]

        area_result = score_comb_with_null(
            warped_spectrum(ab, tb), B=args.B, seed=args.seed + 1000 * ib + 11
        )
        mean_result = score_comb_with_null(
            warped_spectrum(cbar, tb), B=args.B, seed=args.seed + 1000 * ib + 29
        )

        zero_var = float(np.var(cbar))
        residual_ms = float(np.mean(resid * resid))
        total = zero_var + residual_ms
        residual_fraction = float(residual_ms / total) if total > 0 else float("nan")

        count_map = map_scores(cb, tb)
        residual_map = map_scores(resid, tb)

        t_med = float(np.median(tb))
        t_mean = float(np.mean(tb))
        log_scale = float(math.log(t_med / (2.0 * math.pi)))

        row = {
            "block": ib + 1,
            "loop_start": int(loops[s0]),
            "loop_stop": int(loops[s1 - 1]),
            "source_half": "calibration" if ib < 10 else "holdout",
            "T_median": t_med,
            "T_mean": t_mean,
            "log_T_over_2pi": log_scale,
            "area_score": float(area_result.score),
            "area_null_median": float(area_result.null_median),
            "area_null_q95": float(area_result.null_q95),
            "area_null_q99": float(area_result.null_q99),
            "area_E95": normalized_excess(area_result),
            "area_p_jitter": float(area_result.empirical_p_ge),
            "area_best_shift": float(area_result.best_common_shift),
            "area_abs_best_shift": abs(float(area_result.best_common_shift)),
            "mean_score": float(mean_result.score),
            "mean_null_median": float(mean_result.null_median),
            "mean_null_q95": float(mean_result.null_q95),
            "mean_null_q99": float(mean_result.null_q99),
            "mean_E95": normalized_excess(mean_result),
            "mean_p_jitter": float(mean_result.empirical_p_ge),
            "mean_best_shift": float(mean_result.best_common_shift),
            "mean_abs_best_shift": abs(float(mean_result.best_common_shift)),
            "zero_mode_variance": zero_var,
            "residual_mean_square": residual_ms,
            "residual_variance_fraction": residual_fraction,
            "count_map_median": float(np.median(count_map)),
            "residual_map_q05": float(np.quantile(residual_map, 0.05)),
            "residual_map_median": float(np.median(residual_map)),
            "residual_map_q95": float(np.quantile(residual_map, 0.95)),
        }
        rows.append(row)
        print(
            f"block {ib+1:02d} loops {row['loop_start']}-{row['loop_stop']}: "
            f"T={t_med:.3f} area_E95={row['area_E95']:.3f} "
            f"shift={row['area_best_shift']:+.5f} Fres={residual_fraction:.6g}",
            flush=True,
        )

    x = np.array([r["log_T_over_2pi"] for r in rows], dtype=float)
    metrics = {
        "area_E95": np.array([r["area_E95"] for r in rows], dtype=float),
        "mean_E95": np.array([r["mean_E95"] for r in rows], dtype=float),
        "area_abs_best_shift": np.array([r["area_abs_best_shift"] for r in rows], dtype=float),
        "residual_variance_fraction": np.array([r["residual_variance_fraction"] for r in rows], dtype=float),
        "residual_map_median": np.array([r["residual_map_median"] for r in rows], dtype=float),
    }
    trends = {name: trend(x, y) for name, y in metrics.items()}

    out_csv = args.out_prefix.with_suffix(".csv")
    out_json = args.out_prefix.with_suffix(".json")
    out_csv.parent.mkdir(parents=True, exist_ok=True)

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "experiment": "RH-SOL-02 EXP-02 HEIGHT",
        "status": "exploratory",
        "range": {"start": 1, "stop": 20000, "n_loops": 20000},
        "block_size": args.block_size,
        "n_blocks": nblocks,
        "q": 16,
        "rule": "winding",
        "time_proxy": "zero-pair midpoint for all blocks",
        "B": args.B,
        "seed_base": args.seed,
        "normalized_excess_definition": "E95=(observed-null_median)/(null_q95-null_median)",
        "rows": rows,
        "trends_vs_log_T_over_2pi": trends,
        "guardrail": "Exploratory height-dependence analysis opened after EXP-01 holdout. Nominal trend p-values are descriptive, not confirmatory.",
    }
    out_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps({"trends_vs_log_T_over_2pi": trends}, indent=2))


if __name__ == "__main__":
    main()
