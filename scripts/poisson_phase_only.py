#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

REPS = [(1, 0), (0, 1), (1, 1), (1, -1)]
GROUPS = {
    "mode_1_0": [(1, 0)],
    "mode_0_1": [(0, 1)],
    "mode_1_1": [(1, 1)],
    "mode_1_m1": [(1, -1)],
    "shell_r2eq1": [(1, 0), (0, 1)],
    "shell_r2eq2": [(1, 1), (1, -1)],
    "stable_all4": REPS,
}


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


def corrected_coeff(F: np.ndarray, a: int, b: int) -> np.ndarray:
    q = F.shape[-1]
    raw = F[:, b % q, a % q]
    return raw * np.exp(-1j * np.pi * (a + b) / q)


def orthonormal_columns(X: np.ndarray) -> np.ndarray:
    q, _ = np.linalg.qr(np.asarray(X, dtype=float), mode="reduced")
    return q


def score_complex_blocks(t, Y, block_id, omegas):
    vals = []
    for bid in np.unique(block_id):
        m = block_id == bid
        tb = np.asarray(t[m], dtype=float)
        Yb = np.asarray(Y[m], dtype=complex)
        if len(tb) < 10:
            continue
        if Yb.ndim == 1:
            Yb = Yb[:, None]
        tc = tb - np.mean(tb)
        X = np.column_stack([np.ones_like(tc), tc])
        qx = orthonormal_columns(X)
        R = Yb - qx @ (qx.T @ Yb)
        total = max(float(np.sum(np.abs(R) ** 2)), 1e-30)
        ts = tb - tb[0]
        qs = []
        for omega in omegas:
            B = np.column_stack([np.cos(omega * ts), np.sin(omega * ts)])
            qb = orthonormal_columns(B)
            proj = qb.T @ R
            explained = float(np.sum(np.abs(proj) ** 2))
            r2 = min(max(explained / total, 0.0), 1.0)
            qs.append(float(-np.log(max(1.0 - r2, 1e-15))))
        vals.append(float(np.mean(qs)))
    return float(np.mean(vals))


def residualize_area_group(area, Y, block_id):
    out = np.empty_like(Y, dtype=complex)
    for bid in np.unique(block_id):
        m = block_id == bid
        A = np.asarray(area[m], dtype=float)
        X = np.column_stack([np.ones_like(A), A])
        beta, *_ = np.linalg.lstsq(X, Y[m], rcond=None)
        out[m] = Y[m] - X @ beta
    return out


def summarize_null(obs, vals):
    vals = np.asarray(vals, dtype=float)
    return {
        "observed": float(obs),
        "null_median": float(np.median(vals)),
        "null_q95": float(np.quantile(vals, 0.95)),
        "null_q99": float(np.quantile(vals, 0.99)),
        "null_max": float(np.max(vals)),
        "empirical_p_ge": float((1 + np.sum(vals >= obs)) / (len(vals) + 1)),
    }


def analyze(path: Path, seed: int, B: int):
    d = load(path)
    order = np.argsort(d["loops"])
    loops = np.asarray(d["loops"], dtype=int)[order]
    area = np.asarray(d["area_winding"], dtype=float)[order]
    time = 0.5 * (np.asarray(d["gamma0"], dtype=float)[order] + np.asarray(d["gamma1"], dtype=float)[order])
    block_id = (np.arange(len(loops)) // 1000).astype(int)

    F16 = fft_coeffs(np.asarray(d["counts_winding_q16"], dtype=float)[order])
    F32 = fft_coeffs(np.asarray(d["counts_winding_q32"], dtype=float)[order])
    G16 = {m: corrected_coeff(F16, *m) for m in REPS}
    G32 = {m: corrected_coeff(F32, *m) for m in REPS}

    reliability = {}
    U16, U32, masks = {}, {}, {}
    for m in REPS:
        a16 = np.abs(G16[m]); a32 = np.abs(G32[m])
        tau16 = 1e-6 * float(np.median(a16))
        tau32 = 1e-6 * float(np.median(a32))
        mask = (a16 > tau16) & (a32 > tau32)
        masks[m] = mask
        U16[m] = G16[m][mask] / a16[mask]
        U32[m] = G32[m][mask] / a32[mask]
        z = U16[m] * np.conj(U32[m])
        dphi = np.angle(z)
        rms = float(np.sqrt(np.mean(dphi ** 2))) if len(dphi) else float("nan")
        med = float(np.median(np.abs(dphi))) if len(dphi) else float("nan")
        rho = float(abs(np.mean(z))) if len(z) else float("nan")
        excl = float(1.0 - np.mean(mask))
        reliability[f"{m[0]},{m[1]}"] = {
            "tau16": tau16, "tau32": tau32,
            "excluded_fraction": excl,
            "rms_phase_error": rms,
            "median_abs_phase_error": med,
            "rho_phase": rho,
            "passes": bool(excl <= 0.001 and rms <= 0.10 and rho >= 0.995),
        }

    omegas13 = np.log(np.arange(2, 14, dtype=float))
    omegas11 = np.log(np.arange(2, 12, dtype=float))
    groups = {}
    for name, modes in GROUPS.items():
        common = np.ones(len(loops), dtype=bool)
        for m in modes:
            common &= masks[m]
        idx = np.flatnonzero(common)
        t = time[idx]; A = area[idx]; b = block_id[idx]
        Y16 = np.column_stack([G16[m][idx] / np.abs(G16[m][idx]) for m in modes])
        Y32 = np.column_stack([G32[m][idx] / np.abs(G32[m][idx]) for m in modes])
        out = {"excluded_fraction": float(1.0 - np.mean(common))}
        for qname, Y in [("q16", Y16), ("q32", Y32)]:
            Yr = residualize_area_group(A, Y, b)
            out[qname] = {
                "phase_only_m2_13": score_complex_blocks(t, Y, b, omegas13),
                "phase_only_m2_11": score_complex_blocks(t, Y, b, omegas11),
                "phase_only_area_residualized_m2_13": score_complex_blocks(t, Yr, b, omegas13),
                "phase_only_area_residualized_m2_11": score_complex_blocks(t, Yr, b, omegas11),
            }
        groups[name] = out

    # Confirmatory q32 combined four-channel area-residualized target-jitter null.
    common = np.ones(len(loops), dtype=bool)
    for m in REPS:
        common &= masks[m]
    idx = np.flatnonzero(common)
    t = time[idx]; A = area[idx]; b = block_id[idx]
    Y = np.column_stack([G32[m][idx] / np.abs(G32[m][idx]) for m in REPS])
    Yr = residualize_area_group(A, Y, b)
    obs = score_complex_blocks(t, Yr, b, omegas13)
    rng = np.random.default_rng(seed)
    vals = np.empty(B, dtype=float)
    for i in range(B):
        jit = rng.uniform(-0.20, 0.20, size=len(omegas13))
        vals[i] = score_complex_blocks(t, Yr, b, omegas13 + jit)

    return {
        "start": int(loops[0]),
        "stop": int(loops[-1]),
        "phase_stability": reliability,
        "groups": groups,
        "confirmatory_q32_stable_all4_area_residualized_m2_13": summarize_null(obs, vals),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--calibration", type=Path, required=True)
    ap.add_argument("--holdout", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--B", type=int, default=2000)
    args = ap.parse_args()

    cal = analyze(args.calibration, 20260906, args.B)
    hold = analyze(args.holdout, 20260907, args.B)
    joint = {}
    for m in REPS:
        k = f"{m[0]},{m[1]}"
        joint[k] = bool(cal["phase_stability"][k]["passes"] and hold["phase_stability"][k]["passes"])

    result = {
        "method": "RH-SOL-05 POISSON-03 phase-only unit-phasor analysis",
        "representatives": [list(m) for m in REPS],
        "B": args.B,
        "joint_phase_stable": joint,
        "calibration": cal,
        "holdout": hold,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({
        "joint_phase_stable": joint,
        "calibration_stability": cal["phase_stability"],
        "holdout_stability": hold["phase_stability"],
        "calibration_groups": cal["groups"],
        "holdout_groups": hold["groups"],
        "calibration_null": cal["confirmatory_q32_stable_all4_area_residualized_m2_13"],
        "holdout_null": hold["confirmatory_q32_stable_all4_area_residualized_m2_13"],
    }, indent=2))
    print(f"WROTE {args.out}")

if __name__ == "__main__":
    main()
