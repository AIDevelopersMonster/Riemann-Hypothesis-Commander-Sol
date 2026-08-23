#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import numpy as np
from scipy.optimize import least_squares


@dataclass
class FitResult:
    name: str
    k: int
    theta: np.ndarray
    predict: Callable[[np.ndarray, np.ndarray], np.ndarray]
    aicc: float
    log_rmse: float
    relative_rmse: float
    loo_log_rmse: float
    loo_relative_rmse: float
    parameters: dict[str, float]


def _fit_once(name: str, x: np.ndarray, y: np.ndarray):
    logy = np.log(y)

    if name == "inv_log":
        k = 1
        init = np.array([math.log(float(np.median(y * x)))])
        bounds = (np.array([-50.0]), np.array([10.0]))
        pred = lambda th, xx: np.exp(th[0]) / xx
        param = lambda th: {"A": float(np.exp(th[0])), "p_fixed": 1.0}

    elif name == "inv_sqrt_log":
        k = 1
        init = np.array([math.log(float(np.median(y * np.sqrt(x))))])
        bounds = (np.array([-50.0]), np.array([10.0]))
        pred = lambda th, xx: np.exp(th[0]) / np.sqrt(xx)
        param = lambda th: {"A": float(np.exp(th[0])), "p_fixed": 0.5}

    elif name == "power_T":
        k = 2
        init = np.array([math.log(float(y[0])) + 0.5 * float(x[0]), math.log(0.5)])
        bounds = (np.array([-50.0, -10.0]), np.array([10.0, 5.0]))
        pred = lambda th, xx: np.exp(th[0] - np.exp(th[1]) * xx)
        param = lambda th: {"A": float(np.exp(th[0])), "alpha": float(np.exp(th[1]))}

    elif name == "inv_log_power":
        k = 2
        init = np.array([math.log(float(np.median(y * x))), 0.0])
        bounds = (np.array([-50.0, -10.0]), np.array([10.0, 5.0]))
        pred = lambda th, xx: np.exp(th[0]) / np.power(xx, np.exp(th[1]))
        param = lambda th: {"A": float(np.exp(th[0])), "p": float(np.exp(th[1]))}

    elif name == "floor_power_T":
        k = 3
        init = np.array([math.log(max(float(y[-1]) * 0.5, 1e-12)), math.log(max(float(y[0]), 1e-12)), math.log(0.5)])
        bounds = (np.array([-50.0, -50.0, -10.0]), np.array([0.0, 10.0, 5.0]))
        pred = lambda th, xx: np.exp(th[0]) + np.exp(th[1] - np.exp(th[2]) * xx)
        param = lambda th: {"c": float(np.exp(th[0])), "A": float(np.exp(th[1])), "alpha": float(np.exp(th[2]))}

    elif name == "floor_inv_log_power":
        k = 3
        init = np.array([math.log(max(float(y[-1]) * 0.5, 1e-12)), math.log(max(float(np.median(y * x)) * 0.5, 1e-12)), 0.0])
        bounds = (np.array([-50.0, -50.0, -10.0]), np.array([0.0, 10.0, 5.0]))
        pred = lambda th, xx: np.exp(th[0]) + np.exp(th[1]) / np.power(xx, np.exp(th[2]))
        param = lambda th: {"c": float(np.exp(th[0])), "A": float(np.exp(th[1])), "p": float(np.exp(th[2]))}

    else:
        raise ValueError(name)

    def residual(th):
        yp = pred(th, x)
        if np.any(~np.isfinite(yp)) or np.any(yp <= 0):
            return np.full_like(logy, 1e6)
        return np.log(yp) - logy

    res = least_squares(
        residual,
        init,
        bounds=bounds,
        max_nfev=100000,
        xtol=1e-13,
        ftol=1e-13,
        gtol=1e-13,
    )
    yp = pred(res.x, x)
    lr = np.log(yp) - logy
    rss = float(np.sum(lr * lr))
    n = len(y)
    aic = n * math.log(rss / n) + 2.0 * k
    aicc = aic + 2.0 * k * (k + 1.0) / (n - k - 1.0)
    return res.x, pred, param(res.x), k, aicc, float(np.sqrt(np.mean(lr * lr))), float(np.sqrt(np.mean((yp / y - 1.0) ** 2)))


def _loo(name: str, x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    log_err = []
    rel_err = []
    n = len(y)
    for i in range(n):
        keep = np.ones(n, dtype=bool)
        keep[i] = False
        th, pred, _, _, _, _, _ = _fit_once(name, x[keep], y[keep])
        yp = float(pred(th, np.array([x[i]], dtype=float))[0])
        log_err.append(math.log(yp) - math.log(float(y[i])))
        rel_err.append(yp / float(y[i]) - 1.0)
    return float(np.sqrt(np.mean(np.square(log_err)))), float(np.sqrt(np.mean(np.square(rel_err))))


def fit(name: str, x: np.ndarray, y: np.ndarray) -> FitResult:
    th, pred, params, k, aicc, log_rmse, relative_rmse = _fit_once(name, x, y)
    loo_log_rmse, loo_relative_rmse = _loo(name, x, y)
    return FitResult(
        name=name,
        k=k,
        theta=th,
        predict=pred,
        aicc=aicc,
        log_rmse=log_rmse,
        relative_rmse=relative_rmse,
        loo_log_rmse=loo_log_rmse,
        loo_relative_rmse=loo_relative_rmse,
        parameters=params,
    )


def fit_power_in_x(x: np.ndarray, y: np.ndarray) -> dict[str, float]:
    X = np.column_stack([np.ones(len(x)), np.log(x)])
    beta, *_ = np.linalg.lstsq(X, np.log(y), rcond=None)
    pred = np.exp(X @ beta)
    return {
        "C": float(np.exp(beta[0])),
        "exponent": float(beta[1]),
        "log_rmse": float(np.sqrt(np.mean((np.log(pred) - np.log(y)) ** 2))),
    }


def ranking_payload(fits: list[FitResult]) -> list[dict[str, object]]:
    best = min(f.aicc for f in fits)
    out = []
    for f in sorted(fits, key=lambda z: z.aicc):
        out.append({
            "model": f.name,
            "parameters": f.parameters,
            "aicc": f.aicc,
            "delta_aicc": f.aicc - best,
            "log_rmse": f.log_rmse,
            "relative_rmse": f.relative_rmse,
            "loo_log_rmse": f.loo_log_rmse,
            "loo_relative_rmse": f.loo_relative_rmse,
        })
    return out


def run_set(rows: list[dict[str, object]], label: str) -> dict[str, object]:
    x = np.array([float(r["log_T_over_2pi"]) for r in rows], dtype=float)
    y = np.array([float(r["residual_variance_fraction"]) for r in rows], dtype=float)
    r_ms = np.array([float(r["residual_mean_square"]) for r in rows], dtype=float)
    z_var = np.array([float(r["zero_mode_variance"]) for r in rows], dtype=float)

    primary_names = ["inv_log", "inv_sqrt_log", "power_T", "inv_log_power"]
    primary = [fit(name, x, y) for name in primary_names]
    floor = [fit(name, x, y) for name in ["floor_power_T", "floor_inv_log_power"]]

    r_fit = fit_power_in_x(x, r_ms)
    z_fit = fit_power_in_x(x, z_var)
    implied_p = z_fit["exponent"] - r_fit["exponent"]

    inv_log_power = next(f for f in primary if f.name == "inv_log_power")
    direct_p = float(inv_log_power.parameters["p"])

    return {
        "label": label,
        "n_blocks": len(rows),
        "loop_start": int(rows[0]["loop_start"]),
        "loop_stop": int(rows[-1]["loop_stop"]),
        "primary_ranking": ranking_payload(primary),
        "floor_sensitivity_ranking": ranking_payload(floor),
        "mechanistic_component_fits": {
            "residual_mean_square": r_fit,
            "zero_mode_variance": z_fit,
            "implied_F_decay_exponent_z_minus_r": float(implied_p),
            "direct_inv_log_power_exponent_p": direct_p,
            "absolute_exponent_difference": float(abs(implied_p - direct_p)),
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--height-json", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    payload = json.loads(args.height_json.read_text(encoding="utf-8"))
    rows = payload.get("rows")
    if not isinstance(rows, list) or len(rows) != 20:
        raise SystemExit("EXP-03 RATE expects the 20 primary EXP-02 HEIGHT blocks")

    all20 = run_set(rows, "all_20_blocks")
    blocks2 = run_set(rows[1:], "blocks_2_20_sensitivity")

    summary = {
        "experiment": "RH-SOL-02 EXP-03 RATE",
        "status": "exploratory post-view",
        "x_definition": "x=log(T_median/(2*pi))",
        "target": "residual_variance_fraction",
        "fit_scale": "log-space relative-error fit",
        "all_20_blocks": all20,
        "blocks_2_20_sensitivity": blocks2,
        "guardrail": "The rate law is descriptive over loops 1..20000 and is not an asymptotic theorem. Floor models are post-view sensitivity only.",
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print("=== EXP-03 RATE ===")
    for section in [all20, blocks2]:
        print(f"[{section['label']}]")
        for item in section["primary_ranking"]:
            print(
                f"{item['model']}: AICc={item['aicc']:.6f} "
                f"dAICc={item['delta_aicc']:.6f} "
                f"LOOlogRMSE={item['loo_log_rmse']:.6f} "
                f"params={item['parameters']}"
            )
        mech = section["mechanistic_component_fits"]
        print(
            "component exponents: "
            f"r={mech['residual_mean_square']['exponent']:.6f}, "
            f"z={mech['zero_mode_variance']['exponent']:.6f}, "
            f"z-r={mech['implied_F_decay_exponent_z_minus_r']:.6f}, "
            f"direct p={mech['direct_inv_log_power_exponent_p']:.6f}"
        )
    print(f"WROTE {args.out}")


if __name__ == "__main__":
    main()
