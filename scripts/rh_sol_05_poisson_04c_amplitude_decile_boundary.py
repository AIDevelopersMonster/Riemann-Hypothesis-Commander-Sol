#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

REPS = [(1, 0), (0, 1), (1, 1), (1, -1)]
SEED = 20261005


def load(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as z:
        req = {"loops", "gamma0", "gamma1", "area_winding", "counts_winding_q32"}
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
            qs.append(float(-np.log(max(1.0-r2, 1e-15))))
        vals.append(float(np.mean(qs)))
    return float(np.mean(vals)) if vals else float("nan")


def spearman_rank_corr(x: np.ndarray, y: np.ndarray) -> float:
    xr = np.argsort(np.argsort(x)).astype(float)
    yr = np.argsort(np.argsort(y)).astype(float)
    if np.std(xr) == 0 or np.std(yr) == 0:
        return float("nan")
    return float(np.corrcoef(xr, yr)[0, 1])


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
        raise SystemExit(f"Expected loops 20001..40000 n=20000, got {loops[0]}..{loops[-1]} n={len(loops)}")

    area = np.asarray(d["area_winding"], dtype=float)[order]
    t = 0.5 * (np.asarray(d["gamma0"], dtype=float)[order] + np.asarray(d["gamma1"], dtype=float)[order])
    block_id_full = (np.arange(len(loops)) // 1000).astype(int)
    F32 = fft_coeffs(np.asarray(d["counts_winding_q32"], dtype=float)[order])
    G32 = {m: coeff(F32, *m) for m in REPS}

    minamp = np.min(np.column_stack([np.abs(G32[m]) for m in REPS]), axis=1)
    edges = np.quantile(minamp, np.linspace(0.1, 0.9, 9))

    requested = []
    lower = -np.inf
    for i in range(10):
        if i == 0:
            mask = minamp <= edges[0]
        elif i == 9:
            mask = minamp > edges[-1]
        else:
            mask = (minamp > edges[i-1]) & (minamp <= edges[i])
        requested.append(mask)

    prepared = []
    for i, req in enumerate(requested, start=1):
        valid = req.copy()
        for m in REPS:
            a = np.abs(G32[m])
            valid &= np.isfinite(a) & (a > 0.0)
        idx = np.flatnonzero(valid)
        Y = np.column_stack([G32[m][idx] / np.abs(G32[m][idx]) for m in REPS])
        bs = block_id_full[idx]
        Yr = residualize_area(area[idx], Y, bs)
        prepared.append({
            "name": f"D{i}",
            "t": t[idx],
            "Y": Yr,
            "block_id": bs,
            "requested_n": int(np.sum(req)),
            "n": int(np.sum(valid)),
            "undefined_phase_dropped": int(np.sum(req)-np.sum(valid)),
            "amp_min": float(np.min(minamp[req])) if np.any(req) else float("nan"),
            "amp_max": float(np.max(minamp[req])) if np.any(req) else float("nan"),
        })

    exact_omegas = np.log(np.arange(2, 14, dtype=float))
    exact_scores = np.array([
        score_group(v["t"], v["Y"], v["block_id"], exact_omegas)
        for v in prepared
    ], dtype=float)

    rng = np.random.default_rng(SEED)
    null_scores = np.empty((args.B, 10), dtype=float)
    for j in range(args.B):
        jitter = rng.uniform(-0.20, 0.20, size=len(exact_omegas))
        omegas = exact_omegas + jitter
        for i, v in enumerate(prepared):
            null_scores[j, i] = score_group(v["t"], v["Y"], v["block_id"], omegas)
        if (j + 1) % 100 == 0 or j == 0:
            print(f"matched jitter {j+1}/{args.B}", flush=True)

    null_mean = np.mean(null_scores, axis=0)
    null_median = np.median(null_scores, axis=0)
    null_sd = np.std(null_scores, axis=0, ddof=1)
    excess = exact_scores - null_mean

    deciles = {}
    for i, v in enumerate(prepared):
        vals = null_scores[:, i]
        deciles[v["name"]] = {
            "requested_n": v["requested_n"],
            "n": v["n"],
            "undefined_phase_dropped": v["undefined_phase_dropped"],
            "amp_min": v["amp_min"],
            "amp_max": v["amp_max"],
            "exact_score": float(exact_scores[i]),
            "null_mean": float(null_mean[i]),
            "null_median": float(null_median[i]),
            "null_sd": float(null_sd[i]),
            "exact_minus_null_mean": float(excess[i]),
            "null_q95": float(np.quantile(vals, 0.95)),
            "null_q99": float(np.quantile(vals, 0.99)),
            "null_max": float(np.max(vals)),
            "empirical_p_ge": float((1 + np.sum(vals >= exact_scores[i])) / (args.B + 1)),
            "z_from_null_mean": float(excess[i] / null_sd[i]) if null_sd[i] > 0 else float("nan"),
        }

    split_null = np.empty((args.B, 9), dtype=float)
    split_exact = np.empty(9, dtype=float)
    split_mean = np.empty(9, dtype=float)
    split_sd = np.empty(9, dtype=float)
    split_z = np.empty(9, dtype=float)
    split_rows = {}

    for k in range(1, 10):
        split_exact[k-1] = float(np.mean(exact_scores[:k]) - np.mean(exact_scores[k:]))
        split_null[:, k-1] = np.mean(null_scores[:, :k], axis=1) - np.mean(null_scores[:, k:], axis=1)
        split_mean[k-1] = float(np.mean(split_null[:, k-1]))
        split_sd[k-1] = float(np.std(split_null[:, k-1], ddof=1))
        split_z[k-1] = (split_exact[k-1] - split_mean[k-1]) / split_sd[k-1]
        vals = split_null[:, k-1]
        split_rows[f"k={k}"] = {
            "low_deciles": [f"D{i}" for i in range(1, k+1)],
            "high_deciles": [f"D{i}" for i in range(k+1, 11)],
            "exact_contrast": float(split_exact[k-1]),
            "null_mean": float(split_mean[k-1]),
            "null_sd": float(split_sd[k-1]),
            "z_from_null_mean": float(split_z[k-1]),
            "unadjusted_p_ge": float((1 + np.sum(vals >= split_exact[k-1])) / (args.B + 1)),
        }

    standardized_null = (split_null - split_mean[None, :]) / split_sd[None, :]
    T_null = np.max(standardized_null, axis=1)
    best_idx = int(np.argmax(split_z))
    T_exact = float(split_z[best_idx])
    p_max = float((1 + np.sum(T_null >= T_exact)) / (args.B + 1))

    corr = np.corrcoef(null_scores, rowvar=False)
    ranks = np.arange(1, 11, dtype=float)
    spearman = spearman_rank_corr(ranks, excess)
    adjacent_excess_diff = {
        f"D{i+1}-D{i}": float(excess[i] - excess[i-1])
        for i in range(1, 10)
    }

    result = {
        "method": "RH-SOL-05 POISSON-04C_AMPLITUDE_DECILE_BOUNDARY",
        "status": "post-hoc exploratory diagnostic; cannot alter POISSON-04 frozen FAIL",
        "range": [20001, 40000],
        "B": int(args.B),
        "seed": SEED,
        "amplitude_definition": "min abs(G32) across frozen four modes",
        "decile_edges_q10_to_q90": [float(x) for x in edges],
        "deciles": deciles,
        "boundary_scan": split_rows,
        "max_over_splits": {
            "best_split_k": best_idx + 1,
            "T_exact_max_z": T_exact,
            "p_max_familywise": p_max,
            "null_T_q95": float(np.quantile(T_null, 0.95)),
            "null_T_q99": float(np.quantile(T_null, 0.99)),
            "null_T_max": float(np.max(T_null)),
        },
        "matched_null_decile_correlation_order": [f"D{i}" for i in range(1, 11)],
        "matched_null_decile_correlation": corr.tolist(),
        "spearman_decile_rank_vs_exact_minus_null_mean": spearman,
        "adjacent_exact_minus_null_mean_differences": adjacent_excess_diff,
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    print(f"WROTE {args.out}")


if __name__ == "__main__":
    main()
