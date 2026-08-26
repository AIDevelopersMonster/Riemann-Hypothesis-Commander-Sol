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

from dirichlet_spectrum import comb_score, score_comb_with_null, warped_spectrum


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


def comb_result_dict(result) -> dict[str, float]:
    return {
        "score": float(result.score),
        "null_median": float(result.null_median),
        "null_q95": float(result.null_q95),
        "null_q99": float(result.null_q99),
        "empirical_p_ge": float(result.empirical_p_ge),
        "best_common_shift": float(result.best_common_shift),
        "best_common_shift_score": float(result.best_common_shift_score),
    }


def distribution(x: np.ndarray) -> dict[str, float]:
    a = np.asarray(x, dtype=float)
    return {
        "min": float(np.min(a)),
        "q01": float(np.quantile(a, 0.01)),
        "q05": float(np.quantile(a, 0.05)),
        "q25": float(np.quantile(a, 0.25)),
        "median": float(np.median(a)),
        "mean": float(np.mean(a)),
        "q75": float(np.quantile(a, 0.75)),
        "q95": float(np.quantile(a, 0.95)),
        "q99": float(np.quantile(a, 0.99)),
        "max": float(np.max(a)),
        "range": float(np.max(a) - np.min(a)),
        "std": float(np.std(a)),
    }


def score_map(field: np.ndarray, time_proxy: np.ndarray, q: int) -> np.ndarray:
    out = np.empty((q, q), dtype=float)
    for iy in range(q):
        for ix in range(q):
            out[iy, ix] = comb_score(warped_spectrum(field[:, iy, ix], time_proxy))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", type=Path, required=True)
    ap.add_argument("--legacy-time-csv", type=Path)
    ap.add_argument("--q", type=int, nargs="+", default=[8, 16, 32])
    ap.add_argument("--rules", nargs="+", choices=["winding", "even-odd"], default=["winding", "even-odd"])
    ap.add_argument("--B", type=int, default=20000, help="jitter surrogates for scalar area/translation-mean controls")
    ap.add_argument("--seed", type=int, default=20260822)
    ap.add_argument("--expected-start", type=int)
    ap.add_argument("--expected-stop", type=int)
    ap.add_argument("--out-prefix", type=Path, required=True)
    args = ap.parse_args()

    with np.load(args.dataset, allow_pickle=False) as z:
        loops = z["loops"].astype(int)
        gamma0 = z["gamma0"].astype(float)
        gamma1 = z["gamma1"].astype(float)
        cube = {key: z[key].copy() for key in z.files if key.startswith("area_") or key.startswith("counts_")}

    if len(loops) < 1000 or len(loops) % 1000:
        raise SystemExit("control suite requires a loop count that is a positive multiple of 1000")
    if len(np.unique(loops)) != len(loops) or (len(loops) > 1 and not np.all(np.diff(loops) == 1)):
        raise SystemExit("dataset loop indices must be unique and contiguous")
    if args.expected_start is not None and int(loops[0]) != args.expected_start:
        raise SystemExit(f"unexpected first loop: {loops[0]} != {args.expected_start}")
    if args.expected_stop is not None and int(loops[-1]) != args.expected_stop:
        raise SystemExit(f"unexpected last loop: {loops[-1]} != {args.expected_stop}")

    if args.legacy_time_csv:
        time_proxy = load_legacy_time(args.legacy_time_csv, loops)
        time_mode = "RH-SOL-01 legacy t_near"
    else:
        time_proxy = 0.5 * (gamma0 + gamma1)
        time_mode = "zero-pair midpoint"

    configs: list[dict[str, object]] = []
    cell_rows: list[dict[str, object]] = []
    per_rule_area: dict[str, dict[str, float]] = {}

    for irule, rule in enumerate(args.rules):
        key_rule = rule.replace("-", "_")
        area = cube[f"area_{key_rule}"].astype(float)
        area_result = score_comb_with_null(
            warped_spectrum(area, time_proxy),
            B=args.B,
            seed=args.seed + 100000 * irule,
        )
        per_rule_area[rule] = comb_result_dict(area_result)

        for iq, q in enumerate(args.q):
            counts = cube[f"counts_{key_rule}_q{q}"].astype(float)
            translation_mean = counts.mean(axis=(1, 2))
            residual = counts - translation_mean[:, None, None]

            diff = translation_mean - area
            geometry = {
                "mae": float(np.mean(np.abs(diff))),
                "rms": float(math.sqrt(np.mean(diff * diff))),
                "max_abs": float(np.max(np.abs(diff))),
                "correlation": float(np.corrcoef(translation_mean, area)[0, 1]),
            }

            zero_var = float(np.var(translation_mean))
            residual_ms = float(np.mean(residual * residual))
            denom = zero_var + residual_ms
            variance = {
                "zero_mode_variance": zero_var,
                "translation_residual_mean_square": residual_ms,
                "fraction_zero_mode": float(zero_var / denom) if denom > 0 else float("nan"),
            }

            mean_result = score_comb_with_null(
                warped_spectrum(translation_mean, time_proxy),
                B=args.B,
                seed=args.seed + 10000 * irule + 100 * iq + 1,
            )

            count_scores = score_map(counts, time_proxy, q)
            residual_scores = score_map(residual, time_proxy, q)

            config = {
                "rule": rule,
                "q": q,
                "geometry_calibration": geometry,
                "variance_decomposition": variance,
                "area_spectrum": per_rule_area[rule],
                "finite_q_translation_mean_spectrum": comb_result_dict(mean_result),
                "count_map_score_distribution": distribution(count_scores),
                "residual_map_score_distribution": distribution(residual_scores),
            }
            configs.append(config)

            for iy in range(q):
                for ix in range(q):
                    cell_rows.append({
                        "rule": rule,
                        "q": q,
                        "iy": iy,
                        "ix": ix,
                        "dx": (ix + 0.5) / q,
                        "dy": (iy + 0.5) / q,
                        "count_comb_score": float(count_scores[iy, ix]),
                        "residual_comb_score": float(residual_scores[iy, ix]),
                    })

            print(
                f"done rule={rule} q={q}: "
                f"area_mae={geometry['mae']:.6g}, "
                f"mean_score={mean_result.score:.6g}, "
                f"count_median={np.median(count_scores):.6g}, "
                f"residual_median={np.median(residual_scores):.6g}",
                flush=True,
            )

    fill_rule_comparison: dict[str, object] = {}
    if "winding" in args.rules and "even-odd" in args.rules:
        area_w = cube["area_winding"].astype(float)
        area_e = cube["area_even_odd"].astype(float)
        area_diff = area_w - area_e
        fill_rule_comparison["area"] = {
            "fraction_exactly_equal": float(np.mean(area_w == area_e)),
            "mean_abs_difference": float(np.mean(np.abs(area_diff))),
            "max_abs_difference": float(np.max(np.abs(area_diff))),
            "correlation": float(np.corrcoef(area_w, area_e)[0, 1]),
        }
        q_comparisons: dict[str, object] = {}
        for q in args.q:
            w = cube[f"counts_winding_q{q}"].astype(np.int32)
            e = cube[f"counts_even_odd_q{q}"].astype(np.int32)
            d = w - e
            per_loop_any = np.any(d != 0, axis=(1, 2))
            mean_w = w.mean(axis=(1, 2))
            mean_e = e.mean(axis=(1, 2))
            q_comparisons[str(q)] = {
                "fraction_cells_exactly_equal": float(np.mean(d == 0)),
                "fraction_loops_with_any_difference": float(np.mean(per_loop_any)),
                "mean_abs_cell_difference": float(np.mean(np.abs(d))),
                "max_abs_cell_difference": int(np.max(np.abs(d))),
                "translation_mean_correlation": float(np.corrcoef(mean_w, mean_e)[0, 1]),
                "translation_mean_mae_between_rules": float(np.mean(np.abs(mean_w - mean_e))),
            }
        fill_rule_comparison["counts"] = q_comparisons

    out_csv = args.out_prefix.with_suffix(".csv")
    out_json = args.out_prefix.with_suffix(".json")
    out_csv.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "rule", "q", "iy", "ix", "dx", "dy",
        "count_comb_score", "residual_comb_score",
    ]
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cell_rows)

    summary = {
        "experiment": "RH-SOL-02 EXP-01 resolution/fill-rule control suite",
        "n_loops": int(len(loops)),
        "start": int(loops.min()),
        "stop": int(loops.max()),
        "time_proxy": time_mode,
        "q_values": args.q,
        "rules": args.rules,
        "scalar_jitter_B": args.B,
        "seed_base": args.seed,
        "configs": configs,
        "fill_rule_comparison": fill_rule_comparison,
        "interpretation_guardrail": (
            "Per-cell q=8/q=32 maps are descriptive resolution controls. "
            "The predeclared q=16 winding map retains the full per-cell jitter/BH inference. "
            "Do not reinterpret control-map extrema as newly selected primary tests."
        ),
    }
    out_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
