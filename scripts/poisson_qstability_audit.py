#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from firewall_assignment_surrogates import block_target_scores_matrix, target_omegas

CANDIDATES = [(a, b) for b in range(-3, 4) for a in range(-3, 4) if not (a == 0 and b == 0)]
SHELLS = {
    "r2eq1": {(1, 0), (-1, 0), (0, 1), (0, -1)},
    "r2eq2": {(1, 1), (1, -1), (-1, 1), (-1, -1)},
    "r2eq4": {(2, 0), (-2, 0), (0, 2), (0, -2)},
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


def pwr(F: np.ndarray, a: int, b: int) -> np.ndarray:
    q = F.shape[-1]
    return np.abs(F[:, b % q, a % q]) ** 2


def rel_med(x: np.ndarray, y: np.ndarray, eps: float = 1e-15) -> float:
    return float(np.median(np.abs(x - y) / (np.abs(y) + eps)))


def energy(F: np.ndarray, modes: list[tuple[int, int]]) -> np.ndarray:
    out = np.zeros(F.shape[0], dtype=float)
    for a, b in modes:
        out += pwr(F, a, b)
    return out


def score_scalar(t: np.ndarray, y: np.ndarray, block_size: int, nt: int) -> float:
    omegas = target_omegas(2, 13)
    vals = []
    for i in range(0, len(y), block_size):
        s = block_target_scores_matrix(t[i:i+block_size], y[i:i+block_size], omegas)[0]
        vals.append(float(np.mean(s[:nt])))
    return float(np.mean(vals))


def residualize_area(area: np.ndarray, y: np.ndarray, block_size: int) -> np.ndarray:
    out = np.empty_like(y, dtype=float)
    for i in range(0, len(y), block_size):
        A = np.asarray(area[i:i+block_size], dtype=float)
        Y = np.asarray(y[i:i+block_size], dtype=float)
        X = np.column_stack([np.ones_like(A), A])
        beta, *_ = np.linalg.lstsq(X, Y, rcond=None)
        out[i:i+block_size] = Y - X @ beta
    return out


def prep(path: Path) -> dict[str, object]:
    d = load(path)
    order = np.argsort(d["loops"])
    loops = np.asarray(d["loops"], dtype=int)[order]
    gamma0 = np.asarray(d["gamma0"], dtype=float)[order]
    gamma1 = np.asarray(d["gamma1"], dtype=float)[order]
    area = np.asarray(d["area_winding"], dtype=float)[order]
    C16 = np.asarray(d["counts_winding_q16"], dtype=float)[order]
    C32 = np.asarray(d["counts_winding_q32"], dtype=float)[order]
    F16 = fft_coeffs(C16)
    F32 = fft_coeffs(C32)
    table = {}
    stable = []
    for a, b in CANDIDATES:
        r = rel_med(pwr(F16, a, b), pwr(F32, a, b))
        table[f"{a},{b}"] = r
        if r <= 0.10:
            stable.append((a, b))
    return {
        "path": str(path), "loops": loops, "time": 0.5 * (gamma0 + gamma1), "area": area,
        "F16": F16, "F32": F32, "R": table, "stable": stable,
    }


def shell_status(stable: set[tuple[int, int]]) -> dict[str, object]:
    out = {}
    for name, shell in SHELLS.items():
        present = sorted(shell & stable)
        out[name] = {
            "stable_count": len(present),
            "shell_size": len(shell),
            "complete": shell <= stable,
            "stable_vectors": [[a, b] for a, b in present],
        }
    return out


def summarize_range(d: dict[str, object], intersection: list[tuple[int, int]], block_size: int) -> dict[str, object]:
    t = np.asarray(d["time"], dtype=float)
    area = np.asarray(d["area"], dtype=float)
    F16 = np.asarray(d["F16"])
    F32 = np.asarray(d["F32"])
    E16 = energy(F16, intersection)
    E32 = energy(F32, intersection)
    rel = rel_med(E16, E32) if intersection else float("nan")
    corr1632 = float(np.corrcoef(E16, E32)[0, 1]) if intersection and np.std(E16) and np.std(E32) else float("nan")

    def obs(y: np.ndarray) -> dict[str, float]:
        yr = residualize_area(area, y, block_size)
        return {
            "mean": float(np.mean(y)),
            "median": float(np.median(y)),
            "corr_with_area": float(np.corrcoef(area, y)[0, 1]) if np.std(y) and np.std(area) else float("nan"),
            "m2_13": score_scalar(t, y, block_size, 12),
            "m2_11": score_scalar(t, y, block_size, 10),
            "residualized_m2_13": score_scalar(t, yr, block_size, 12),
            "residualized_m2_11": score_scalar(t, yr, block_size, 10),
        }

    partial_shells = {}
    interset = set(intersection)
    for name, shell in SHELLS.items():
        modes = sorted(shell & interset)
        if not modes:
            partial_shells[name] = {"modes": [], "complete": False}
            continue
        y16 = energy(F16, modes)
        y32 = energy(F32, modes)
        partial_shells[name] = {
            "modes": [[a, b] for a, b in modes],
            "complete": shell <= interset,
            "q16": obs(y16),
            "q32": obs(y32),
            "R_16_32_energy": rel_med(y16, y32),
            "corr_q16_q32": float(np.corrcoef(y16, y32)[0, 1]) if np.std(y16) and np.std(y32) else float("nan"),
        }

    return {
        "start": int(np.asarray(d["loops"])[0]),
        "stop": int(np.asarray(d["loops"])[-1]),
        "mode_R_16_32": d["R"],
        "stable_vectors": [[a, b] for a, b in sorted(d["stable"])],
        "shell_status": shell_status(set(d["stable"])),
        "intersection_energy": {
            "modes": [[a, b] for a, b in intersection],
            "R_16_32_energy": rel,
            "corr_q16_q32": corr1632,
            "q16": obs(E16),
            "q32": obs(E32),
        },
        "intersection_shells": partial_shells,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--calibration", type=Path, required=True)
    ap.add_argument("--holdout", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--block-size", type=int, default=1000)
    args = ap.parse_args()

    cal = prep(args.calibration)
    hold = prep(args.holdout)
    S_cal = set(cal["stable"])
    S_hold = set(hold["stable"])
    inter = sorted(S_cal & S_hold)

    result = {
        "method": "POISSON-01B q-stability audit",
        "threshold_R_16_32": 0.10,
        "candidate_max_abs_index": 3,
        "stable_intersection": [[a, b] for a, b in inter],
        "n_stable_intersection": len(inter),
        "intersection_shell_status": shell_status(set(inter)),
        "calibration": summarize_range(cal, inter, args.block_size),
        "holdout": summarize_range(hold, inter, args.block_size),
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    compact = {
        "stable_intersection": result["stable_intersection"],
        "intersection_shell_status": result["intersection_shell_status"],
        "calibration_intersection_energy": result["calibration"]["intersection_energy"],
        "holdout_intersection_energy": result["holdout"]["intersection_energy"],
    }
    print(json.dumps(compact, indent=2))
    print(f"WROTE {args.out}")


if __name__ == "__main__":
    main()
