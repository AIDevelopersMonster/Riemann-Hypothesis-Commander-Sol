#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

REPS = [(1, 0), (0, 1), (1, 1), (1, -1)]
SEEDS = {"bottom10": 20261001, "middle80": 20261002, "top10": 20261003}


def load(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as z:
        req = {"loops", "gamma0", "gamma1", "area_winding", "counts_winding_q16", "counts_winding_q32"}
        miss = req - set(z.files)
        if miss:
            raise SystemExit(f"{path} missing required keys: {sorted(miss)}")
        return {k: np.array(z[k]) for k in req}


def fft_coeffs(C: np.ndarray) -> np.ndarray:
    q = C.shape[-1]
    return np.fft.fft2(C, axes=(-2, -1)) / float(q * q)


def coeff(F: np.ndarray, a: int, b: int) -> np.ndarray:
    q = F.shape[-1]
    raw = F[:, b % q, a % q]
    return raw * np.exp(-1j * np.pi * (a + b) / q)


def residualize_area(area: np.ndarray, Y: np.ndarray, block_id: np.ndarray) -> np.ndarray:
    out = np.empty_like(Y, dtype=complex)
    for bid in np.unique(block_id):
        m = block_id == bid
        A = area[m]
        X = np.column_stack([np.ones_like(A), A])
        beta, *_ = np.linalg.lstsq(X, Y[m], rcond=None)
        out[m] = Y[m] - X @ beta
    return out


def score_group(t: np.ndarray, Y: np.ndarray, block_id: np.ndarray, omegas: np.ndarray) -> float:
    vals = []
    for bid in np.unique(block_id):
        m = block_id == bid
        if np.sum(m) < 10:
            continue
        tb = np.asarray(t[m], dtype=float)
        Yb = np.asarray(Y[m], dtype=complex)
        if Yb.ndim == 1:
            Yb = Yb[:, None]
        tc = tb - np.mean(tb)
        X = np.column_stack([np.ones_like(tc), tc])
        qx, _ = np.linalg.qr(X, mode="reduced")
        R = Yb - qx @ (qx.T @ Yb)
        total = max(float(np.sum(np.abs(R) ** 2)), 1e-30)
        ts = tb - tb[0]
        qs = []
        for omega in omegas:
            B = np.column_stack([np.cos(omega * ts), np.sin(omega * ts)])
            qb, _ = np.linalg.qr(B, mode="reduced")
            proj = qb.T @ R
            r2 = min(max(float(np.sum(np.abs(proj) ** 2)) / total, 0.0), 1.0)
            qs.append(float(-np.log(max(1.0 - r2, 1e-15))))
        vals.append(float(np.mean(qs)))
    return float(np.mean(vals)) if vals else float("nan")


def phase_stability(g16: dict, g32: dict, mask: np.ndarray) -> dict[str, object]:
    out = {}
    for mode in REPS:
        a16 = np.abs(g16[mode])
        a32 = np.abs(g32[mode])
        valid = mask & np.isfinite(a16) & np.isfinite(a32) & (a16 > 0.0) & (a32 > 0.0)
        z = (g16[mode][valid] / a16[valid]) * np.conj(g32[mode][valid] / a32[valid])
        d = np.angle(z)
        out[f"{mode[0]},{mode[1]}"] = {
            "n": int(np.sum(valid)),
            "rms_phase_error": float(np.sqrt(np.mean(d*d))) if len(d) else float("nan"),
            "median_abs_phase_error": float(np.median(np.abs(d))) if len(d) else float("nan"),
            "rho_phase": float(abs(np.mean(z))) if len(z) else float("nan"),
        }
    return out


def summarize_null(obs: float, vals: np.ndarray) -> dict[str, float]:
    vals = np.asarray(vals, dtype=float)
    return {
        "observed": float(obs),
        "null_median": float(np.median(vals)),
        "null_q95": float(np.quantile(vals, 0.95)),
        "null_q99": float(np.quantile(vals, 0.99)),
        "null_max": float(np.max(vals)),
        "empirical_p_ge": float((1 + np.sum(vals >= obs)) / (len(vals) + 1)),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--B", type=int, default=2000)
    args = ap.parse_args()

    d = load(args.data)
    order = np.argsort(d["loops"])
    loops = np.asarray(d["loops"], dtype=int)[order]
    if int(loops[0]) != 20001 or int(loops[-1]) != 40000 or len(loops) != 20000:
        raise SystemExit(f"Expected fresh OOS loops 20001..40000, got {loops[0]}..{loops[-1]} n={len(loops)}")

    area = np.asarray(d["area_winding"], dtype=float)[order]
    t = 0.5 * (np.asarray(d["gamma0"], dtype=float)[order] + np.asarray(d["gamma1"], dtype=float)[order])
    block_id = (np.arange(len(loops)) // 1000).astype(int)
    F16 = fft_coeffs(np.asarray(d["counts_winding_q16"], dtype=float)[order])
    F32 = fft_coeffs(np.asarray(d["counts_winding_q32"], dtype=float)[order])
    G16 = {m: coeff(F16, *m) for m in REPS}
    G32 = {m: coeff(F32, *m) for m in REPS}

    minamp = np.min(np.column_stack([np.abs(G32[m]) for m in REPS]), axis=1)
    q10, q90 = np.quantile(minamp, [0.10, 0.90])
    requested = {
        "bottom10": minamp <= q10,
        "middle80": (minamp > q10) & (minamp < q90),
        "top10": minamp >= q90,
    }

    omegas13 = np.log(np.arange(2, 14, dtype=float))
    omegas11 = np.log(np.arange(2, 12, dtype=float))

    strata = {}
    for name, req in requested.items():
        valid = req.copy()
        for m in REPS:
            a = np.abs(G32[m])
            valid &= np.isfinite(a) & (a > 0.0)

        idx = np.flatnonzero(valid)
        Y = np.column_stack([G32[m][idx] / np.abs(G32[m][idx]) for m in REPS])
        ts = t[idx]
        As = area[idx]
        bs = block_id[idx]
        Yr = residualize_area(As, Y, bs)

        obs13 = score_group(ts, Yr, bs, omegas13)
        obs11 = score_group(ts, Yr, bs, omegas11)
        rng = np.random.default_rng(SEEDS[name])
        null = np.empty(args.B, dtype=float)
        for i in range(args.B):
            jitter = rng.uniform(-0.20, 0.20, size=len(omegas13))
            null[i] = score_group(ts, Yr, bs, omegas13 + jitter)

        strata[name] = {
            "requested_n": int(np.sum(req)),
            "n": int(np.sum(valid)),
            "undefined_phase_dropped": int(np.sum(req) - np.sum(valid)),
            "q10": float(q10),
            "q90": float(q90),
            "area_residualized_m2_13": float(obs13),
            "area_residualized_m2_11": float(obs11),
            "target_jitter_null": summarize_null(obs13, null),
            "q16_q32_phase_stability": phase_stability(G16, G32, valid),
        }

    b = strata["bottom10"]["area_residualized_m2_13"]
    m = strata["middle80"]["area_residualized_m2_13"]
    h = strata["top10"]["area_residualized_m2_13"]
    b11 = strata["bottom10"]["area_residualized_m2_11"]
    m11 = strata["middle80"]["area_residualized_m2_11"]

    primary = {
        "ordering_bottom_gt_top_gt_middle": bool(b > h > m),
        "bottom_over_top": float(b / h) if h else float("nan"),
        "bottom_over_middle": float(b / m) if m else float("nan"),
        "sensitivity_bottom_gt_middle": bool(b11 > m11),
        "bottom10_null_pass": bool(
            b > strata["bottom10"]["target_jitter_null"]["null_q99"]
            and strata["bottom10"]["target_jitter_null"]["empirical_p_ge"] <= 0.01
        ),
        "top10_null_pass": bool(
            h > strata["top10"]["target_jitter_null"]["null_q99"]
            and strata["top10"]["target_jitter_null"]["empirical_p_ge"] <= 0.01
        ),
    }
    primary["phase_singularity_amplification_confirmed"] = bool(
        primary["ordering_bottom_gt_top_gt_middle"]
        and primary["bottom_over_top"] > 1.0
        and primary["bottom_over_middle"] > 1.0
        and primary["sensitivity_bottom_gt_middle"]
        and primary["bottom10_null_pass"]
        and primary["top10_null_pass"]
    )

    result = {
        "method": "RH-SOL-05 POISSON-04_PHASE_SINGULARITY_OOS",
        "range": [20001, 40000],
        "B": args.B,
        "amplitude_definition": "min abs(G32) across frozen four modes",
        "strata": strata,
        "primary_verdict": primary,
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    print(f"WROTE {args.out}")


if __name__ == "__main__":
    main()
