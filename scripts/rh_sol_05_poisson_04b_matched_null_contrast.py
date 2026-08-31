#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

REPS = [(1, 0), (0, 1), (1, 1), (1, -1)]
SEED = 20261004


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


def summarize(obs: float, vals: np.ndarray) -> dict[str, float]:
    vals = np.asarray(vals, dtype=float)
    mu = float(np.mean(vals))
    sd = float(np.std(vals, ddof=1)) if len(vals) > 1 else float("nan")
    return {
        "observed": float(obs),
        "null_mean": mu,
        "null_median": float(np.median(vals)),
        "null_sd": sd,
        "null_q01": float(np.quantile(vals, 0.01)),
        "null_q05": float(np.quantile(vals, 0.05)),
        "null_q95": float(np.quantile(vals, 0.95)),
        "null_q99": float(np.quantile(vals, 0.99)),
        "null_min": float(np.min(vals)),
        "null_max": float(np.max(vals)),
        "empirical_p_ge": float((1 + np.sum(vals >= obs)) / (len(vals) + 1)),
        "empirical_p_le": float((1 + np.sum(vals <= obs)) / (len(vals) + 1)),
        "z_from_null_mean": float((obs - mu) / sd) if sd > 0 else float("nan"),
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
        raise SystemExit(f"Expected loops 20001..40000 n=20000, got {loops[0]}..{loops[-1]} n={len(loops)}")

    area = np.asarray(d["area_winding"], dtype=float)[order]
    t = 0.5 * (np.asarray(d["gamma0"], dtype=float)[order] + np.asarray(d["gamma1"], dtype=float)[order])
    block_id_full = (np.arange(len(loops)) // 1000).astype(int)
    F32 = fft_coeffs(np.asarray(d["counts_winding_q32"], dtype=float)[order])
    G32 = {m: coeff(F32, *m) for m in REPS}

    minamp = np.min(np.column_stack([np.abs(G32[m]) for m in REPS]), axis=1)
    q10, q90 = np.quantile(minamp, [0.10, 0.90])
    requested = {
        "bottom10": minamp <= q10,
        "middle80": (minamp > q10) & (minamp < q90),
        "top10": minamp >= q90,
    }

    prepared = {}
    for name, req in requested.items():
        valid = req.copy()
        for m in REPS:
            a = np.abs(G32[m])
            valid &= np.isfinite(a) & (a > 0.0)
        idx = np.flatnonzero(valid)
        Y = np.column_stack([G32[m][idx] / np.abs(G32[m][idx]) for m in REPS])
        As = area[idx]
        bs = block_id_full[idx]
        Yr = residualize_area(As, Y, bs)
        prepared[name] = {
            "t": t[idx],
            "Y": Yr,
            "block_id": bs,
            "requested_n": int(np.sum(req)),
            "n": int(np.sum(valid)),
            "undefined_phase_dropped": int(np.sum(req)-np.sum(valid)),
        }

    exact_omegas = np.log(np.arange(2, 14, dtype=float))
    exact_scores = {
        name: score_group(v["t"], v["Y"], v["block_id"], exact_omegas)
        for name, v in prepared.items()
    }

    exact_contrasts = {
        "Delta_BT": exact_scores["bottom10"] - exact_scores["top10"],
        "Delta_BM": exact_scores["bottom10"] - exact_scores["middle80"],
        "Delta_MT": exact_scores["middle80"] - exact_scores["top10"],
    }

    rng = np.random.default_rng(SEED)
    score_null = {
        "bottom10": np.empty(args.B, dtype=float),
        "middle80": np.empty(args.B, dtype=float),
        "top10": np.empty(args.B, dtype=float),
    }
    for i in range(args.B):
        jitter = rng.uniform(-0.20, 0.20, size=len(exact_omegas))
        omegas = exact_omegas + jitter
        for name, v in prepared.items():
            score_null[name][i] = score_group(v["t"], v["Y"], v["block_id"], omegas)

    contrast_null = {
        "Delta_BT": score_null["bottom10"] - score_null["top10"],
        "Delta_BM": score_null["bottom10"] - score_null["middle80"],
        "Delta_MT": score_null["middle80"] - score_null["top10"],
    }

    corr = np.corrcoef(np.column_stack([
        score_null["bottom10"], score_null["middle80"], score_null["top10"]
    ]), rowvar=False)

    result = {
        "method": "RH-SOL-05 POISSON-04B_MATCHED_NULL_CONTRAST",
        "status": "post-hoc exploratory diagnostic; cannot alter POISSON-04 frozen FAIL",
        "range": [20001, 40000],
        "B": int(args.B),
        "seed": SEED,
        "amplitude_definition": "min abs(G32) across frozen four modes",
        "q10": float(q10),
        "q90": float(q90),
        "strata": {
            name: {
                "requested_n": int(v["requested_n"]),
                "n": int(v["n"]),
                "undefined_phase_dropped": int(v["undefined_phase_dropped"]),
                "exact_score": float(exact_scores[name]),
                "matched_null_score_mean": float(np.mean(score_null[name])),
                "matched_null_score_median": float(np.median(score_null[name])),
            }
            for name, v in prepared.items()
        },
        "exact_contrasts": {k: float(v) for k, v in exact_contrasts.items()},
        "matched_null_contrasts": {k: summarize(exact_contrasts[k], contrast_null[k]) for k in exact_contrasts},
        "matched_null_score_correlation_order": ["bottom10", "middle80", "top10"],
        "matched_null_score_correlation": corr.tolist(),
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    print(f"WROTE {args.out}")


if __name__ == "__main__":
    main()
