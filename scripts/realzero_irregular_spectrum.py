#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.signal import lombscargle

ROOT = Path(__file__).resolve().parents[1]


def load_and_concat(paths: list[Path]) -> dict[str, np.ndarray]:
    loaded = [np.load(p, allow_pickle=False) for p in paths]
    try:
        required = {"loops", "gamma0", "gamma1", "area_winding"}
        for p, z in zip(paths, loaded):
            missing = required - set(z.files)
            if missing:
                raise SystemExit(f"{p} missing keys: {sorted(missing)}")
        loops = np.concatenate([z["loops"] for z in loaded])
        gamma0 = np.concatenate([z["gamma0"] for z in loaded])
        gamma1 = np.concatenate([z["gamma1"] for z in loaded])
        area = np.concatenate([z["area_winding"] for z in loaded])
        order = np.argsort(loops)
        loops = loops[order]
        gamma0 = gamma0[order]
        gamma1 = gamma1[order]
        area = area[order]
        if len(np.unique(loops)) != len(loops):
            raise SystemExit("duplicate loop indices")
        if len(loops) > 1 and not np.all(np.diff(loops) == 1):
            raise SystemExit("gap in loop indices")
        return {"loops": loops, "gamma0": gamma0, "gamma1": gamma1, "area": area}
    finally:
        for z in loaded:
            z.close()


def detrend_time(t: np.ndarray, y: np.ndarray) -> np.ndarray:
    tc = t - np.mean(t)
    X = np.column_stack([np.ones_like(tc), tc])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return y - X @ beta


def direct_spectrum(
    y: np.ndarray,
    t: np.ndarray,
    *,
    block_size: int = 1000,
    omega_min: float = 0.40,
    omega_max: float = 3.50,
    omega_step: float = 0.0005,
) -> tuple[np.ndarray, np.ndarray]:
    if len(y) != len(t) or len(y) % block_size:
        raise ValueError("series and times must have equal length divisible by block_size")
    omega = np.arange(omega_min, omega_max + 0.5 * omega_step, omega_step)
    acc = np.zeros_like(omega)
    nblocks = len(y) // block_size
    for s0 in range(0, len(y), block_size):
        s1 = s0 + block_size
        tb = np.asarray(t[s0:s1], dtype=float)
        yb = np.asarray(y[s0:s1], dtype=float)
        r = detrend_time(tb, yb)
        tc = tb - tb[0]
        power = lombscargle(tc, r, omega, precenter=False, normalize=False)
        med = float(np.median(power))
        norm = power / (med + 1e-30)
        acc += np.log1p(norm)
    return omega, acc / nblocks


def comb_targets(m_min: int, m_max: int) -> np.ndarray:
    return np.log(np.arange(m_min, m_max + 1, dtype=float))


def comb_score(omega: np.ndarray, score: np.ndarray, m_min: int, m_max: int) -> float:
    targets = comb_targets(m_min, m_max)
    return float(np.mean(np.interp(targets, omega, score)))


def jitter_null(
    omega: np.ndarray,
    score: np.ndarray,
    *,
    m_min: int,
    m_max: int,
    B: int,
    half_width: float,
    seed: int,
) -> dict:
    targets = comb_targets(m_min, m_max)
    obs = float(np.mean(np.interp(targets, omega, score)))
    rng = np.random.default_rng(seed)
    vals = np.empty(B, dtype=float)
    for i in range(B):
        jit = rng.uniform(-half_width, half_width, size=len(targets))
        vals[i] = float(np.mean(np.interp(targets + jit, omega, score)))
    return {
        "observed": obs,
        "null_median": float(np.median(vals)),
        "null_q95": float(np.quantile(vals, 0.95)),
        "null_q99": float(np.quantile(vals, 0.99)),
        "empirical_p_ge": float((1 + np.sum(vals >= obs)) / (B + 1)),
    }


def common_shift(omega: np.ndarray, score: np.ndarray, m_min: int, m_max: int) -> dict:
    targets = comb_targets(m_min, m_max)
    shifts = np.linspace(-0.25, 0.25, 2001)
    vals = np.array([np.mean(np.interp(targets + d, omega, score)) for d in shifts])
    j = int(np.argmax(vals))
    return {"best_shift": float(shifts[j]), "best_shift_score": float(vals[j])}


def local_peaks(omega: np.ndarray, score: np.ndarray, m_min: int, m_max: int, half_window: float = 0.05) -> list[dict]:
    out = []
    for m in range(m_min, m_max + 1):
        target = math.log(m)
        mask = (omega >= target - half_window) & (omega <= target + half_window)
        idx = np.flatnonzero(mask)
        if not len(idx):
            continue
        j = idx[int(np.argmax(score[idx]))]
        out.append({
            "m": m,
            "target": target,
            "peak_omega": float(omega[j]),
            "delta": float(omega[j] - target),
            "peak_score": float(score[j]),
            "target_score": float(np.interp(target, omega, score)),
        })
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("datasets", nargs="+", type=Path)
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--stop", type=int, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--spectrum-csv", type=Path, required=True)
    ap.add_argument("--block-size", type=int, default=1000)
    ap.add_argument("--B", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=20260825)
    args = ap.parse_args()

    d = load_and_concat(args.datasets)
    sel = (d["loops"] >= args.start) & (d["loops"] <= args.stop)
    loops = d["loops"][sel]
    area = d["area"][sel]
    t = 0.5 * (d["gamma0"][sel] + d["gamma1"][sel])
    expected = np.arange(args.start, args.stop + 1)
    if len(loops) != len(expected) or not np.array_equal(loops, expected):
        raise SystemExit("requested loop range is not contiguous in supplied datasets")
    if len(loops) % args.block_size:
        raise SystemExit("requested range length must be divisible by block size")

    omega, score = direct_spectrum(area, t, block_size=args.block_size)
    primary = jitter_null(omega, score, m_min=2, m_max=13, B=args.B, half_width=0.20, seed=args.seed)
    primary.update(common_shift(omega, score, 2, 13))
    safe = jitter_null(omega, score, m_min=2, m_max=11, B=args.B, half_width=0.20, seed=args.seed + 1)
    safe.update(common_shift(omega, score, 2, 11))

    result = {
        "method": "direct irregular-time Lomb-Scargle on actual zero-pair midpoints",
        "observable": "area_winding",
        "start": args.start,
        "stop": args.stop,
        "n_loops": int(len(loops)),
        "block_size": args.block_size,
        "n_blocks": int(len(loops) // args.block_size),
        "omega_min": float(omega[0]),
        "omega_max": float(omega[-1]),
        "omega_step": float(omega[1] - omega[0]),
        "jitter_B": args.B,
        "jitter_half_width": 0.20,
        "jitter_seed_primary": args.seed,
        "primary_m2_13": primary,
        "nyquist_sensitivity_m2_11": safe,
        "local_peaks_m2_13": local_peaks(omega, score, 2, 13),
        "time_min": float(t[0]),
        "time_max": float(t[-1]),
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    args.spectrum_csv.parent.mkdir(parents=True, exist_ok=True)
    arr = np.column_stack([omega, score])
    np.savetxt(args.spectrum_csv, arr, delimiter=",", header="omega,score", comments="")

    print(json.dumps(result["primary_m2_13"], indent=2))
    print("m2_11", json.dumps(result["nyquist_sensitivity_m2_11"], indent=2))
    print(f"WROTE {args.out}")
    print(f"WROTE {args.spectrum_csv}")


if __name__ == "__main__":
    main()
