#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy import stats

A1 = 0.21368139779723283
P1 = 3.137757448939574
A2 = 0.014291857670165177
ALPHA2 = 0.48215823718583606


def pred_m1(T: np.ndarray) -> np.ndarray:
    x = np.log(T / (2.0 * math.pi))
    return A1 / np.power(x, P1)


def pred_m2(T: np.ndarray) -> np.ndarray:
    return A2 * np.power(T / (2.0 * math.pi), -ALPHA2)


def summarize(obs: np.ndarray, pred: np.ndarray) -> dict[str, float]:
    le = np.log(pred) - np.log(obs)
    rel = (pred - obs) / obs
    return {
        "rmse_log": float(np.sqrt(np.mean(le * le))),
        "mae_log": float(np.mean(np.abs(le))),
        "mean_signed_log_error": float(np.mean(le)),
        "relative_rmse": float(np.sqrt(np.mean(rel * rel))),
        "median_absolute_relative_error": float(np.median(np.abs(rel))),
        "log_sse": float(np.sum(le * le)),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    with np.load(args.dataset, allow_pickle=False) as z:
        loops = z["loops"].astype(int)
        gamma0 = z["gamma0"].astype(float)
        gamma1 = z["gamma1"].astype(float)
        counts = z["counts_winding_q16"].astype(float)

    if len(loops) != 20000 or int(loops[0]) != 20001 or int(loops[-1]) != 40000:
        raise SystemExit("EXP-04 dataset must contain loops 20001..40000")

    tmid = 0.5 * (gamma0 + gamma1)
    rows = []
    obs = []
    Tvals = []

    for ib in range(20):
        s0 = ib * 1000
        s1 = s0 + 1000
        cb = counts[s0:s1]
        cbar = cb.mean(axis=(1, 2))
        resid = cb - cbar[:, None, None]
        zvar = float(np.var(cbar))
        rms = float(np.mean(resid * resid))
        fres = float(rms / (zvar + rms))
        T = float(np.median(tmid[s0:s1]))
        p1 = float(pred_m1(np.array([T]))[0])
        p2 = float(pred_m2(np.array([T]))[0])
        e1 = float(abs(math.log(p1) - math.log(fres)))
        e2 = float(abs(math.log(p2) - math.log(fres)))
        rows.append({
            "block": ib + 21,
            "loop_start": int(loops[s0]),
            "loop_stop": int(loops[s1 - 1]),
            "T_median": T,
            "log_T_over_2pi": float(math.log(T / (2.0 * math.pi))),
            "zero_mode_variance": zvar,
            "residual_mean_square": rms,
            "F_res_observed": fres,
            "M1_inv_log_power_pred": p1,
            "M2_power_T_pred": p2,
            "abs_log_error_M1": e1,
            "abs_log_error_M2": e2,
            "block_winner": "M1" if e1 < e2 else ("M2" if e2 < e1 else "tie"),
        })
        obs.append(fres)
        Tvals.append(T)
        print(
            f"block {ib+21:02d} loops {loops[s0]}-{loops[s1-1]}: "
            f"T={T:.3f} F={fres:.9g} M1={p1:.9g} M2={p2:.9g} "
            f"winner={rows[-1]['block_winner']}",
            flush=True,
        )

    obs_a = np.asarray(obs, dtype=float)
    T_a = np.asarray(Tvals, dtype=float)
    p1_a = pred_m1(T_a)
    p2_a = pred_m2(T_a)
    s1 = summarize(obs_a, p1_a)
    s2 = summarize(obs_a, p2_a)

    wins1 = int(sum(r["block_winner"] == "M1" for r in rows))
    wins2 = int(sum(r["block_winner"] == "M2" for r in rows))
    ties = 20 - wins1 - wins2

    x = np.log(T_a / (2.0 * math.pi))
    pear = stats.pearsonr(x, obs_a)
    spear = stats.spearmanr(x, obs_a)

    primary_winner = "M1_inv_log_power" if s1["rmse_log"] < s2["rmse_log"] else ("M2_power_T" if s2["rmse_log"] < s1["rmse_log"] else "tie")
    result = {
        "experiment": "RH-SOL-02 EXP-04 RATE-OOS",
        "status": "frozen out-of-sample score",
        "range": {"start": 20001, "stop": 40000, "n_loops": 20000, "block_size": 1000, "n_blocks": 20},
        "frozen_models": {
            "M1_inv_log_power": {"A": A1, "p": P1, "formula": "A/[log(T/(2*pi))]^p"},
            "M2_power_T": {"A": A2, "alpha": ALPHA2, "formula": "A*(T/(2*pi))^(-alpha)"},
        },
        "primary_winner": primary_winner,
        "M1": s1,
        "M2": s2,
        "rmse_log_ratio_M2_over_M1": float(s2["rmse_log"] / s1["rmse_log"]),
        "block_wins": {"M1": wins1, "M2": wins2, "ties": ties},
        "observed": {
            "first_F_res": float(obs_a[0]),
            "last_F_res": float(obs_a[-1]),
            "pearson_vs_log_T": float(pear.statistic),
            "pearson_p_descriptive": float(pear.pvalue),
            "spearman_vs_log_T": float(spear.statistic),
            "spearman_p_descriptive": float(spear.pvalue),
        },
        "rows": rows,
        "guardrail": "No parameters were refit on loops 20001..40000 before computing the primary score.",
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({
        "primary_winner": primary_winner,
        "M1": s1,
        "M2": s2,
        "rmse_log_ratio_M2_over_M1": result["rmse_log_ratio_M2_over_M1"],
        "block_wins": result["block_wins"],
    }, indent=2))
    print(f"WROTE {args.out}")


if __name__ == "__main__":
    main()
