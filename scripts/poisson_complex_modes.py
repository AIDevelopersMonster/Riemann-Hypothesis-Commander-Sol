#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from firewall_assignment_surrogates import target_omegas

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
    phase = np.exp(-1j * np.pi * (a + b) / q)
    return raw * phase


def complex_stability(g16: np.ndarray, g32: np.ndarray, eps: float = 1e-30) -> dict[str, float | bool]:
    e = float(np.linalg.norm(g16 - g32) / (np.linalg.norm(g32) + eps))
    rho = float(abs(np.vdot(g16, g32)) / ((np.linalg.norm(g16) * np.linalg.norm(g32)) + eps))
    return {
        "E_complex": e,
        "rho_complex": rho,
        "passes": bool(e <= 0.10 and rho >= 0.995),
    }


def orthonormal_columns(X: np.ndarray) -> np.ndarray:
    q, _ = np.linalg.qr(np.asarray(X, dtype=float), mode="reduced")
    return q


def detrend_complex(t: np.ndarray, Y: np.ndarray) -> np.ndarray:
    tc = t - np.mean(t)
    X = np.column_stack([np.ones_like(tc), tc])
    qx = orthonormal_columns(X)
    return Y - qx @ (qx.T @ Y)


def residualize_area_complex(area: np.ndarray, Y: np.ndarray) -> np.ndarray:
    X = np.column_stack([np.ones_like(area), area])
    beta, *_ = np.linalg.lstsq(X, Y, rcond=None)
    return Y - X @ beta


def score_complex(t: np.ndarray, Y: np.ndarray, block_size: int, n_targets: int) -> float:
    omegas = target_omegas(2, 13)
    vals = []
    for i in range(0, len(t), block_size):
        tb = np.asarray(t[i:i+block_size], dtype=float)
        Yb = np.asarray(Y[i:i+block_size], dtype=complex)
        if Yb.ndim == 1:
            Yb = Yb[:, None]
        R = detrend_complex(tb, Yb)
        total = float(np.sum(np.abs(R) ** 2))
        total = max(total, 1e-30)
        ts = tb - tb[0]
        qs = []
        for omega in omegas[:n_targets]:
            B = np.column_stack([np.cos(omega * ts), np.sin(omega * ts)])
            qb = orthonormal_columns(B)
            proj = qb.T @ R
            explained = float(np.sum(np.abs(proj) ** 2))
            r2 = min(max(explained / total, 0.0), 1.0)
            qs.append(float(-np.log(max(1.0 - r2, 1e-15))))
        vals.append(float(np.mean(qs)))
    return float(np.mean(vals))


def score_power(t: np.ndarray, Y: np.ndarray, block_size: int, n_targets: int) -> float:
    from firewall_assignment_surrogates import block_target_scores_matrix
    p = np.sum(np.abs(Y) ** 2, axis=1)
    vals = []
    omegas = target_omegas(2, 13)
    for i in range(0, len(t), block_size):
        s = block_target_scores_matrix(t[i:i+block_size], p[i:i+block_size], omegas)[0]
        vals.append(float(np.mean(s[:n_targets])))
    return float(np.mean(vals))


def analyze(path: Path, block_size: int) -> dict[str, object]:
    d = load(path)
    order = np.argsort(d["loops"])
    area = np.asarray(d["area_winding"], dtype=float)[order]
    time = 0.5 * (np.asarray(d["gamma0"], dtype=float)[order] + np.asarray(d["gamma1"], dtype=float)[order])
    F16 = fft_coeffs(np.asarray(d["counts_winding_q16"], dtype=float)[order])
    F32 = fft_coeffs(np.asarray(d["counts_winding_q32"], dtype=float)[order])

    coeff16 = {m: corrected_coeff(F16, *m) for m in REPS}
    coeff32 = {m: corrected_coeff(F32, *m) for m in REPS}

    stability = {}
    for m in REPS:
        stability[f"{m[0]},{m[1]}"] = complex_stability(coeff16[m], coeff32[m])

    groups = {}
    for name, modes in GROUPS.items():
        Y16 = np.column_stack([coeff16[m] for m in modes])
        Y32 = np.column_stack([coeff32[m] for m in modes])
        out = {}
        for qname, Y in [("q16", Y16), ("q32", Y32)]:
            Yr = np.empty_like(Y, dtype=complex)
            for i in range(0, len(area), block_size):
                Yr[i:i+block_size] = residualize_area_complex(area[i:i+block_size], Y[i:i+block_size])
            out[qname] = {
                "complex_m2_13": score_complex(time, Y, block_size, 12),
                "complex_m2_11": score_complex(time, Y, block_size, 10),
                "complex_area_residualized_m2_13": score_complex(time, Yr, block_size, 12),
                "complex_area_residualized_m2_11": score_complex(time, Yr, block_size, 10),
                "power_m2_13": score_power(time, Y, block_size, 12),
                "power_m2_11": score_power(time, Y, block_size, 10),
            }
        groups[name] = out

    return {
        "start": int(np.min(d["loops"])),
        "stop": int(np.max(d["loops"])),
        "complex_stability": stability,
        "groups": groups,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--calibration", type=Path, required=True)
    ap.add_argument("--holdout", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--block-size", type=int, default=1000)
    args = ap.parse_args()

    cal = analyze(args.calibration, args.block_size)
    hold = analyze(args.holdout, args.block_size)

    joint = {}
    for m in REPS:
        key = f"{m[0]},{m[1]}"
        joint[key] = bool(cal["complex_stability"][key]["passes"] and hold["complex_stability"][key]["passes"])

    result = {
        "method": "RH-SOL-05 POISSON-02 midpoint-phase-corrected complex stable-mode analysis",
        "representatives": [list(m) for m in REPS],
        "joint_complex_stable": joint,
        "calibration": cal,
        "holdout": hold,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    compact = {
        "joint_complex_stable": joint,
        "calibration_stability": cal["complex_stability"],
        "holdout_stability": hold["complex_stability"],
        "calibration_groups": cal["groups"],
        "holdout_groups": hold["groups"],
    }
    print(json.dumps(compact, indent=2))
    print(f"WROTE {args.out}")


if __name__ == "__main__":
    main()
