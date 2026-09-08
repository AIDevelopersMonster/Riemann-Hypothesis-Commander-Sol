#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

REPS = [(1, 0), (0, 1), (1, 1), (1, -1)]
SEED = 20261006


def load(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as z:
        req = {
            "loops", "gamma0", "gamma1", "area_winding",
            "counts_winding_q16", "counts_winding_q32",
        }
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
        per_omega = []
        for omega in omegas:
            B = np.column_stack([np.cos(omega * ts), np.sin(omega * ts)])
            qb, _ = np.linalg.qr(B, mode="reduced")
            proj = qb.T @ R
            r2 = min(max(float(np.sum(np.abs(proj) ** 2)) / total, 0.0), 1.0)
            per_omega.append(float(-np.log(max(1.0 - r2, 1e-15))))
        vals.append(float(np.mean(per_omega)))
    return float(np.mean(vals)) if vals else float("nan")


def summarize_null(obs: float, vals: np.ndarray) -> dict[str, float]:
    vals = np.asarray(vals, dtype=float)
    mu = float(np.mean(vals))
    sd = float(np.std(vals, ddof=1)) if len(vals) > 1 else float("nan")
    return {
        "observed": float(obs),
        "null_mean": mu,
        "null_median": float(np.median(vals)),
        "null_sd": sd,
        "null_q95": float(np.quantile(vals, 0.95)),
        "null_q99": float(np.quantile(vals, 0.99)),
        "null_min": float(np.min(vals)),
        "null_max": float(np.max(vals)),
        "empirical_p_ge": float((1 + np.sum(vals >= obs)) / (len(vals) + 1)),
        "z_from_null_mean": float((obs - mu) / sd) if sd > 0 else float("nan"),
    }


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
            "rms_phase_error": float(np.sqrt(np.mean(d * d))) if len(d) else float("nan"),
            "median_abs_phase_error": float(np.median(np.abs(d))) if len(d) else float("nan"),
            "rho_phase": float(abs(np.mean(z))) if len(z) else float("nan"),
        }
    return out


def prepare_group(req: np.ndarray, g32: dict, area: np.ndarray, t: np.ndarray, block_id: np.ndarray) -> dict:
    valid = req.copy()
    for mode in REPS:
        a = np.abs(g32[mode])
        valid &= np.isfinite(a) & (a > 0.0)
    idx = np.flatnonzero(valid)
    Y = np.column_stack([g32[m][idx] / np.abs(g32[m][idx]) for m in REPS])
    Yr = residualize_area(area[idx], Y, block_id[idx])
    return {
        "requested_mask": req,
        "valid_mask": valid,
        "idx": idx,
        "t": t[idx],
        "Y": Yr,
        "block_id": block_id[idx],
        "requested_n": int(np.sum(req)),
        "n": int(np.sum(valid)),
        "undefined_phase_dropped": int(np.sum(req) - np.sum(valid)),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--B", type=int, default=5000)
    args = ap.parse_args()

    print("=== RH-SOL-05 POISSON-05 / AMPLITUDE 70-30 OOS ===", flush=True)
    print("Identity     : POISSON-05_AMPLITUDE_70_30_OOS", flush=True)
    print("Fresh range  : loops 40001..60000", flush=True)
    print("Primary      : fixed empirical lower70 vs upper30 matched contrast", flush=True)
    print(f"Null         : common target jitter +/-0.20, B={args.B}", flush=True)

    d = load(args.data)
    order = np.argsort(d["loops"])
    loops = np.asarray(d["loops"], dtype=int)[order]
    if len(loops) != 20000 or int(loops[0]) != 40001 or int(loops[-1]) != 60000:
        raise SystemExit(
            f"Expected fresh loops 40001..60000 n=20000, got {loops[0]}..{loops[-1]} n={len(loops)}"
        )
    if not np.array_equal(loops, np.arange(40001, 60001, dtype=int)):
        raise SystemExit("Fresh loop indices are not exactly contiguous 40001..60000")

    area = np.asarray(d["area_winding"], dtype=float)[order]
    t = 0.5 * (
        np.asarray(d["gamma0"], dtype=float)[order]
        + np.asarray(d["gamma1"], dtype=float)[order]
    )
    block_id = (np.arange(len(loops)) // 1000).astype(int)

    F16 = fft_coeffs(np.asarray(d["counts_winding_q16"], dtype=float)[order])
    F32 = fft_coeffs(np.asarray(d["counts_winding_q32"], dtype=float)[order])
    G16 = {m: coeff(F16, *m) for m in REPS}
    G32 = {m: coeff(F32, *m) for m in REPS}

    minamp = np.min(np.column_stack([np.abs(G32[m]) for m in REPS]), axis=1)
    q70 = float(np.quantile(minamp, 0.70))
    q90 = float(np.quantile(minamp, 0.90))
    requested = {
        "lower70": minamp <= q70,
        "upper30": minamp > q70,
    }
    prepared = {
        name: prepare_group(mask, G32, area, t, block_id)
        for name, mask in requested.items()
    }

    omega13 = np.log(np.arange(2, 14, dtype=float))
    omega11 = np.log(np.arange(2, 12, dtype=float))
    exact13 = {
        name: score_group(v["t"], v["Y"], v["block_id"], omega13)
        for name, v in prepared.items()
    }
    exact11 = {
        name: score_group(v["t"], v["Y"], v["block_id"], omega11)
        for name, v in prepared.items()
    }
    delta13 = exact13["lower70"] - exact13["upper30"]
    delta11 = exact11["lower70"] - exact11["upper30"]

    rng = np.random.default_rng(SEED)
    lower_null = np.empty(args.B, dtype=float)
    upper_null = np.empty(args.B, dtype=float)
    for i in range(args.B):
        if i == 0 or (i + 1) % 250 == 0:
            print(f"matched jitter {i + 1}/{args.B}", flush=True)
        jitter = rng.uniform(-0.20, 0.20, size=len(omega13))
        om = omega13 + jitter
        lower_null[i] = score_group(
            prepared["lower70"]["t"], prepared["lower70"]["Y"], prepared["lower70"]["block_id"], om
        )
        upper_null[i] = score_group(
            prepared["upper30"]["t"], prepared["upper30"]["Y"], prepared["upper30"]["block_id"], om
        )
    delta_null = lower_null - upper_null

    delta_summary = summarize_null(delta13, delta_null)
    lower_summary = summarize_null(exact13["lower70"], lower_null)
    upper_summary = summarize_null(exact13["upper30"], upper_null)

    primary = {
        "delta_exact_positive": bool(delta13 > 0.0),
        "delta_above_null_q99": bool(delta13 > delta_summary["null_q99"]),
        "delta_p_le_0_01": bool(delta_summary["empirical_p_ge"] <= 0.01),
        "sensitivity_m2_11_delta_positive": bool(delta11 > 0.0),
        "lower70_above_own_null_q99": bool(exact13["lower70"] > lower_summary["null_q99"]),
        "lower70_own_p_le_0_01": bool(lower_summary["empirical_p_ge"] <= 0.01),
    }
    primary["amplitude_70_30_oos_confirmed"] = bool(all(primary.values()))

    # Frozen secondary diagnostics only.
    top10_req = minamp >= q90
    top10 = prepare_group(top10_req, G32, area, t, block_id)
    top10_exact = score_group(top10["t"], top10["Y"], top10["block_id"], omega13)
    top10_null = np.empty(args.B, dtype=float)
    # Reproduce the same common jitter sequence deterministically without changing primary inference.
    rng2 = np.random.default_rng(SEED)
    for i in range(args.B):
        jitter = rng2.uniform(-0.20, 0.20, size=len(omega13))
        top10_null[i] = score_group(top10["t"], top10["Y"], top10["block_id"], omega13 + jitter)

    groups = {}
    for name, v in prepared.items():
        score_null = lower_null if name == "lower70" else upper_null
        groups[name] = {
            "requested_n": v["requested_n"],
            "n": v["n"],
            "undefined_phase_dropped": v["undefined_phase_dropped"],
            "exact_score_m2_13": float(exact13[name]),
            "exact_score_m2_11": float(exact11[name]),
            "target_jitter_null_m2_13": summarize_null(exact13[name], score_null),
            "exact_minus_null_mean": float(exact13[name] - np.mean(score_null)),
            "q16_q32_phase_stability": phase_stability(G16, G32, v["valid_mask"]),
        }

    result = {
        "method": "RH-SOL-05 POISSON-05_AMPLITUDE_70_30_OOS",
        "status": "frozen independent OOS confirmatory test",
        "range": [40001, 60000],
        "B": int(args.B),
        "seed": SEED,
        "amplitude_definition": "min abs(G32) across frozen four modes",
        "q70": q70,
        "q90_secondary": q90,
        "groups": groups,
        "primary_contrast": {
            "Delta_70_30_m2_13": float(delta13),
            "Delta_70_30_m2_11": float(delta11),
            "matched_null": delta_summary,
        },
        "primary_verdict": primary,
        "secondary_top10": {
            "requested_n": top10["requested_n"],
            "n": top10["n"],
            "undefined_phase_dropped": top10["undefined_phase_dropped"],
            "exact_score_m2_13": float(top10_exact),
            "target_jitter_null_m2_13": summarize_null(top10_exact, top10_null),
            "exact_minus_null_mean": float(top10_exact - np.mean(top10_null)),
            "q16_q32_phase_stability": phase_stability(G16, G32, top10["valid_mask"]),
        },
        "matched_null_score_correlation_lower70_upper30": float(np.corrcoef(lower_null, upper_null)[0, 1]),
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2), flush=True)
    print(f"WROTE {args.out}", flush=True)
    print("=== POISSON-05_AMPLITUDE_70_30_OOS COMPLETE ===", flush=True)


if __name__ == "__main__":
    main()
