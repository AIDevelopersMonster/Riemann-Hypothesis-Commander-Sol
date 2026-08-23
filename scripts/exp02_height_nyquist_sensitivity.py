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

from dirichlet_spectrum import score_comb_with_null, warped_spectrum


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


def trend(x: np.ndarray, y: np.ndarray) -> dict[str, float]:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    pearson = stats.pearsonr(x, y)
    spearman = stats.spearmanr(x, y)
    slope, intercept, r, p, stderr = stats.linregress(x, y)
    return {
        "n": int(len(x)),
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


def slice_trends(rows: list[dict[str, object]], start_index: int) -> dict[str, object]:
    sub = rows[start_index:]
    x = np.array([r["log_T_over_2pi"] for r in sub], dtype=float)
    out: dict[str, object] = {}
    for key in ["area_E95_m2_11", "mean_E95_m2_11", "area_abs_best_shift_m2_11", "residual_variance_fraction", "residual_mean_square", "zero_mode_variance"]:
        y = np.array([r[key] for r in sub], dtype=float)
        out[key] = trend(x, y)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--calibration", type=Path, required=True)
    ap.add_argument("--holdout", type=Path, required=True)
    ap.add_argument("--B", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=20260822)
    ap.add_argument("--out-prefix", type=Path, required=True)
    args = ap.parse_args()

    a = load_cube(args.calibration)
    b = load_cube(args.holdout)
    loops = np.concatenate([a["loops"], b["loops"]])
    gamma0 = np.concatenate([a["gamma0"], b["gamma0"]])
    gamma1 = np.concatenate([a["gamma1"], b["gamma1"]])
    area = np.concatenate([a["area"], b["area"]])
    counts = np.concatenate([a["counts"], b["counts"]], axis=0)
    tmid = 0.5 * (gamma0 + gamma1)

    if len(loops) != 20000 or int(loops[0]) != 1 or int(loops[-1]) != 20000:
        raise SystemExit("combined range must be loops 1..20000")

    rows: list[dict[str, object]] = []
    for ib in range(20):
        s0 = ib * 1000
        s1 = s0 + 1000
        sl = slice(s0, s1)
        tb = tmid[sl]
        ab = area[sl]
        cb = counts[sl]
        cbar = cb.mean(axis=(1, 2))
        resid = cb - cbar[:, None, None]

        area_result = score_comb_with_null(
            warped_spectrum(ab, tb), m_min=2, m_max=11,
            B=args.B, seed=args.seed + 1000 * ib + 211,
        )
        mean_result = score_comb_with_null(
            warped_spectrum(cbar, tb), m_min=2, m_max=11,
            B=args.B, seed=args.seed + 1000 * ib + 229,
        )

        zero_var = float(np.var(cbar))
        residual_ms = float(np.mean(resid * resid))
        total = zero_var + residual_ms
        fres = float(residual_ms / total) if total > 0 else float("nan")

        t_med = float(np.median(tb))
        log_scale = float(math.log(t_med / (2.0 * math.pi)))
        omega_nyq_asym = 0.5 * log_scale
        m_safe_asym = int(math.floor(math.sqrt(t_med / (2.0 * math.pi))))

        row = {
            "block": ib + 1,
            "loop_start": int(loops[s0]),
            "loop_stop": int(loops[s1 - 1]),
            "T_median": t_med,
            "log_T_over_2pi": log_scale,
            "omega_nyq_asym": omega_nyq_asym,
            "m_safe_asym": m_safe_asym,
            "area_score_m2_11": float(area_result.score),
            "area_null_median_m2_11": float(area_result.null_median),
            "area_null_q95_m2_11": float(area_result.null_q95),
            "area_E95_m2_11": normalized_excess(area_result),
            "area_p_jitter_m2_11": float(area_result.empirical_p_ge),
            "area_best_shift_m2_11": float(area_result.best_common_shift),
            "area_abs_best_shift_m2_11": abs(float(area_result.best_common_shift)),
            "mean_score_m2_11": float(mean_result.score),
            "mean_E95_m2_11": normalized_excess(mean_result),
            "mean_best_shift_m2_11": float(mean_result.best_common_shift),
            "zero_mode_variance": zero_var,
            "residual_mean_square": residual_ms,
            "residual_variance_fraction": fres,
        }
        rows.append(row)
        print(
            f"block {ib+1:02d} T={t_med:.3f} m_safe~{m_safe_asym:02d} "
            f"area_E95(m2-11)={row['area_E95_m2_11']:.3f} "
            f"shift={row['area_best_shift_m2_11']:+.5f} "
            f"Rms={residual_ms:.6g} Fres={fres:.6g}",
            flush=True,
        )

    e_high = np.array([r["area_E95_m2_11"] for r in rows[9:]], dtype=float)
    summary = {
        "experiment": "RH-SOL-02 EXP-02 HEIGHT post-view Nyquist sensitivity",
        "status": "exploratory sensitivity",
        "dictionary": "common Nyquist-safe subset log(m), m=2..11",
        "reason": "At block-1 median height, asymptotic Nyquist thresholds for m=12 and m=13 exceed T; m=2..11 is safe across all 20 block medians.",
        "B": args.B,
        "seed_base": args.seed,
        "rows": rows,
        "trends": {
            "all_20": slice_trends(rows, 0),
            "blocks_2_20": slice_trends(rows, 1),
            "high_half_blocks_11_20": slice_trends(rows, 10),
        },
        "high_region_blocks_10_20": {
            "area_E95_mean_m2_11": float(np.mean(e_high)),
            "area_E95_std_m2_11": float(np.std(e_high, ddof=1)),
            "area_E95_min_m2_11": float(np.min(e_high)),
            "area_E95_max_m2_11": float(np.max(e_high)),
        },
        "residual_fraction_first_to_last_ratio": float(rows[0]["residual_variance_fraction"] / rows[-1]["residual_variance_fraction"]),
        "guardrail": "This sensitivity was designed after viewing the primary EXP-02 m=2..13 result. It cannot replace or retroactively redefine the primary HEIGHT analysis.",
    }

    out_csv = args.out_prefix.with_suffix(".csv")
    out_json = args.out_prefix.with_suffix(".json")
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    out_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps({"trends": summary["trends"], "high_region_blocks_10_20": summary["high_region_blocks_10_20"], "residual_fraction_first_to_last_ratio": summary["residual_fraction_first_to_last_ratio"]}, indent=2))


if __name__ == "__main__":
    main()
