#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from firewall_assignment_surrogates import block_target_scores_matrix, target_omegas


def load_dataset(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as z:
        required = {
            "loops", "gamma0", "gamma1", "area_winding",
            "counts_winding_q8", "counts_winding_q16", "counts_winding_q32",
        }
        missing = required - set(z.files)
        if missing:
            raise SystemExit(f"{path} missing required keys: {sorted(missing)}")
        return {k: np.array(z[k]) for k in required}


def mode_index(k: int, q: int) -> int:
    return k % q


def fft_coeffs(counts: np.ndarray) -> np.ndarray:
    q = counts.shape[-1]
    if counts.shape[-2] != q:
        raise ValueError("count map must be square")
    return np.fft.fft2(counts, axes=(-2, -1)) / float(q * q)


def power_at(F: np.ndarray, a: int, b: int) -> np.ndarray:
    q = F.shape[-1]
    return np.abs(F[:, mode_index(b, q), mode_index(a, q)]) ** 2


def shell_energy(F: np.ndarray, radii2: set[int]) -> np.ndarray:
    q = F.shape[-1]
    out = np.zeros(F.shape[0], dtype=float)
    maxk = q // 2
    ks = np.arange(-maxk, maxk + 1)
    if q % 2 == 0:
        ks = ks[ks != maxk]
    for b in ks:
        for a in ks:
            if a == 0 and b == 0:
                continue
            if a * a + b * b in radii2:
                out += power_at(F, int(a), int(b))
    return out


def total_nonzero_energy(F: np.ndarray) -> np.ndarray:
    P = np.abs(F) ** 2
    return np.sum(P, axis=(-2, -1)) - P[:, 0, 0]


def rel_median_discrepancy(x: np.ndarray, y: np.ndarray, eps: float = 1e-15) -> float:
    return float(np.median(np.abs(x - y) / (np.abs(y) + eps)))


def score_scalar(t: np.ndarray, y: np.ndarray, block_size: int, n_targets: int) -> float:
    if len(y) % block_size:
        raise ValueError("range length not divisible by block size")
    omegas = target_omegas(2, 13)
    vals = []
    for i in range(0, len(y), block_size):
        s = block_target_scores_matrix(t[i:i+block_size], y[i:i+block_size], omegas)[0]
        vals.append(float(np.mean(s[:n_targets])))
    return float(np.mean(vals))


def residualize_area(t: np.ndarray, area: np.ndarray, y: np.ndarray, block_size: int) -> np.ndarray:
    out = np.empty_like(y, dtype=float)
    for i in range(0, len(y), block_size):
        A = np.asarray(area[i:i+block_size], dtype=float)
        Y = np.asarray(y[i:i+block_size], dtype=float)
        X = np.column_stack([np.ones_like(A), A])
        beta, *_ = np.linalg.lstsq(X, Y, rcond=None)
        out[i:i+block_size] = Y - X @ beta
    return out


def analyze(path: Path, block_size: int) -> dict[str, object]:
    d = load_dataset(path)
    loops = np.asarray(d["loops"], dtype=int)
    order = np.argsort(loops)
    loops = loops[order]
    gamma0 = np.asarray(d["gamma0"], dtype=float)[order]
    gamma1 = np.asarray(d["gamma1"], dtype=float)[order]
    area = np.asarray(d["area_winding"], dtype=float)[order]
    time = 0.5 * (gamma0 + gamma1)

    C8 = np.asarray(d["counts_winding_q8"], dtype=float)[order]
    C16 = np.asarray(d["counts_winding_q16"], dtype=float)[order]
    C32 = np.asarray(d["counts_winding_q32"], dtype=float)[order]

    F8, F16, F32 = fft_coeffs(C8), fft_coeffs(C16), fft_coeffs(C32)

    parseval = {}
    for q, C, F in [(8, C8, F8), (16, C16, F16), (32, C32, F32)]:
        mean_c = np.mean(C, axis=(-2, -1))
        zero = np.real(F[:, 0, 0])
        var_c = np.var(C, axis=(-2, -1))
        nz = total_nonzero_energy(F)
        mean_err = float(np.max(np.abs(mean_c - zero)))
        parseval_err = float(np.max(np.abs(var_c - nz)))
        tol = 1e-12 + 1e-10 * float(np.max(np.abs(var_c)))
        if mean_err > 1e-12:
            raise SystemExit(f"q={q} zero-mode/mean identity failed: {mean_err}")
        if parseval_err > tol:
            raise SystemExit(f"q={q} Parseval identity failed: {parseval_err} > {tol}")
        parseval[str(q)] = {
            "max_zero_mode_mean_abs_error": mean_err,
            "max_variance_parseval_abs_error": parseval_err,
        }

    stability = {}
    stable_modes = []
    for b in range(-3, 4):
        for a in range(-3, 4):
            if a == 0 and b == 0:
                continue
            p8 = power_at(F8, a, b)
            p16 = power_at(F16, a, b)
            p32 = power_at(F32, a, b)
            r816 = rel_median_discrepancy(p8, p16)
            r1632 = rel_median_discrepancy(p16, p32)
            key = f"{a},{b}"
            stability[key] = {"R_8_16": r816, "R_16_32": r1632, "q_stable": bool(r1632 <= 0.10)}
            if r1632 <= 0.10:
                stable_modes.append([a, b])

    Z = np.real(F32[:, 0, 0])
    E1 = shell_energy(F32, {1})
    E2 = shell_energy(F32, {2})
    E4 = shell_energy(F32, {4})
    Elow = E1 + E2 + E4
    Enz = total_nonzero_energy(F32)
    Ehigh = Enz - Elow
    V = np.var(C32, axis=(-2, -1))

    observables = {
        "A_area": area,
        "Z_translation_mean": Z,
        "E1_r2eq1": E1,
        "E1_plus_E2": E1 + E2,
        "Elow_r2le4": Elow,
        "Ehigh": Ehigh,
        "Enonzero_total": Enz,
        "V_translation_variance": V,
    }

    scores = {}
    for name, y in observables.items():
        scores[name] = {
            "m2_13": score_scalar(time, y, block_size, 12),
            "m2_11": score_scalar(time, y, block_size, 10),
        }

    residual_scores = {}
    for name in ["E1_r2eq1", "E1_plus_E2", "Elow_r2le4", "Ehigh", "Enonzero_total"]:
        yr = residualize_area(time, area, observables[name], block_size)
        residual_scores[name] = {
            "m2_13": score_scalar(time, yr, block_size, 12),
            "m2_11": score_scalar(time, yr, block_size, 10),
            "corr_with_area": float(np.corrcoef(area, observables[name])[0, 1]),
        }

    result = {
        "source": str(path),
        "start": int(loops[0]),
        "stop": int(loops[-1]),
        "n_loops": int(len(loops)),
        "block_size": int(block_size),
        "parseval_checks": parseval,
        "zero_mode_area": {
            "mean_abs_Z_minus_area": float(np.mean(np.abs(Z - area))),
            "median_abs_Z_minus_area": float(np.median(np.abs(Z - area))),
            "max_abs_Z_minus_area": float(np.max(np.abs(Z - area))),
            "corr_Z_area": float(np.corrcoef(Z, area)[0, 1]),
        },
        "mode_stability": stability,
        "n_q_stable_modes_max3": int(len(stable_modes)),
        "q_stable_modes_max3": stable_modes,
        "energy_summary": {
            name: {
                "mean": float(np.mean(y)),
                "median": float(np.median(y)),
                "std": float(np.std(y)),
            }
            for name, y in observables.items()
        },
        "target_scores": scores,
        "area_residualized_target_scores": residual_scores,
    }
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--calibration", type=Path, required=True)
    ap.add_argument("--holdout", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--block-size", type=int, default=1000)
    args = ap.parse_args()

    cal = analyze(args.calibration, args.block_size)
    hold = analyze(args.holdout, args.block_size)

    out = {"method": "RH-SOL-05 POISSON-01 translation-mode decomposition", "calibration": cal, "holdout": hold}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    compact = {
        "calibration": {
            "n_q_stable_modes_max3": cal["n_q_stable_modes_max3"],
            "zero_mode_area": cal["zero_mode_area"],
            "target_scores": cal["target_scores"],
            "area_residualized_target_scores": cal["area_residualized_target_scores"],
        },
        "holdout": {
            "n_q_stable_modes_max3": hold["n_q_stable_modes_max3"],
            "zero_mode_area": hold["zero_mode_area"],
            "target_scores": hold["target_scores"],
            "area_residualized_target_scores": hold["area_residualized_target_scores"],
        },
    }
    print(json.dumps(compact, indent=2))
    print(f"WROTE {args.out}")


if __name__ == "__main__":
    main()
