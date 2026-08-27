#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from firewall_assignment_surrogates import target_omegas

REPS = [(1, 0), (0, 1), (1, 1), (1, -1)]
TRIMS = [0.0, 0.005, 0.01, 0.02, 0.05]


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


def phase_metrics(g16: np.ndarray, g32: np.ndarray, mask: np.ndarray) -> dict[str, float | int]:
    requested_n = int(np.sum(mask))
    a16 = np.abs(g16)
    a32 = np.abs(g32)
    valid = mask & np.isfinite(a16) & np.isfinite(a32) & (a16 > 0.0) & (a32 > 0.0)
    valid_n = int(np.sum(valid))
    invalid_n = requested_n - valid_n
    if valid_n == 0:
        return {
            "n": 0,
            "requested_n": requested_n,
            "invalid_phase_count": invalid_n,
            "rms_phase_error": float("nan"),
            "median_abs_phase_error": float("nan"),
            "rho_phase": float("nan"),
        }
    u16 = g16[valid] / a16[valid]
    u32 = g32[valid] / a32[valid]
    z = u16 * np.conj(u32)
    d = np.angle(z)
    return {
        "n": valid_n,
        "requested_n": requested_n,
        "invalid_phase_count": invalid_n,
        "rms_phase_error": float(np.sqrt(np.mean(d * d))),
        "median_abs_phase_error": float(np.median(np.abs(d))),
        "rho_phase": float(abs(np.mean(z))),
    }


def total_nonzero(F: np.ndarray) -> np.ndarray:
    P = np.abs(F) ** 2
    return np.sum(P, axis=(-2, -1)) - P[:, 0, 0]


def stable_energy(F: np.ndarray) -> np.ndarray:
    out = np.zeros(F.shape[0], dtype=float)
    for a, b in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
        out += np.abs(F[:, b % F.shape[-1], a % F.shape[-1]]) ** 2
    return out


def residualize_area(area: np.ndarray, y: np.ndarray, block_id: np.ndarray) -> np.ndarray:
    out = np.empty_like(y, dtype=complex)
    for bid in np.unique(block_id):
        m = block_id == bid
        A = area[m]
        X = np.column_stack([np.ones_like(A), A])
        beta, *_ = np.linalg.lstsq(X, y[m], rcond=None)
        out[m] = y[m] - X @ beta
    return out


def score_group(t: np.ndarray, Y: np.ndarray, block_id: np.ndarray, n_targets: int) -> float:
    omegas = target_omegas(2, 13)
    vals = []
    for bid in np.unique(block_id):
        m = block_id == bid
        if np.sum(m) < 10:
            continue
        tb = t[m]
        Yb = Y[m]
        if Yb.ndim == 1:
            Yb = Yb[:, None]
        tc = tb - np.mean(tb)
        X = np.column_stack([np.ones_like(tc), tc])
        qx, _ = np.linalg.qr(X, mode="reduced")
        R = Yb - qx @ (qx.T @ Yb)
        total = max(float(np.sum(np.abs(R) ** 2)), 1e-30)
        ts = tb - tb[0]
        qs = []
        for omega in omegas[:n_targets]:
            B = np.column_stack([np.cos(omega * ts), np.sin(omega * ts)])
            qb, _ = np.linalg.qr(B, mode="reduced")
            proj = qb.T @ R
            r2 = min(max(float(np.sum(np.abs(proj) ** 2)) / total, 0.0), 1.0)
            qs.append(float(-np.log(max(1.0-r2, 1e-15))))
        vals.append(float(np.mean(qs)))
    return float(np.mean(vals)) if vals else float("nan")


def analyze(path: Path) -> dict[str, object]:
    d = load(path)
    order = np.argsort(d["loops"])
    loops = np.asarray(d["loops"], int)[order]
    area = np.asarray(d["area_winding"], float)[order]
    t = 0.5 * (np.asarray(d["gamma0"], float)[order] + np.asarray(d["gamma1"], float)[order])
    block_id = (np.arange(len(loops)) // 1000).astype(int)
    C16 = np.asarray(d["counts_winding_q16"], float)[order]
    C32 = np.asarray(d["counts_winding_q32"], float)[order]
    F16, F32 = fft_coeffs(C16), fft_coeffs(C32)
    G16 = {m: coeff(F16, *m) for m in REPS}
    G32 = {m: coeff(F32, *m) for m in REPS}

    excluded_sets = {}
    amp = {}
    per_mode = {}
    for m in REPS:
        a16, a32 = np.abs(G16[m]), np.abs(G32[m])
        tau16 = 1e-6 * float(np.median(a16)); tau32 = 1e-6 * float(np.median(a32))
        reliable = (a16 > tau16) & (a32 > tau32)
        excluded_sets[m] = set(np.flatnonzero(~reliable).tolist())
        amp[m] = np.sqrt(a16 * a32)

        qcuts = np.quantile(amp[m], [0.01, 0.05, 0.20, 0.50])
        strata = {
            "Q0_bottom1": amp[m] <= qcuts[0],
            "Q1_1to5": (amp[m] > qcuts[0]) & (amp[m] <= qcuts[1]),
            "Q2_5to20": (amp[m] > qcuts[1]) & (amp[m] <= qcuts[2]),
            "Q3_20to50": (amp[m] > qcuts[2]) & (amp[m] <= qcuts[3]),
            "Q4_top50": amp[m] > qcuts[3],
        }
        trim = {}
        for f in TRIMS:
            cut = np.quantile(amp[m], f) if f > 0 else -np.inf
            trim[str(f)] = phase_metrics(G16[m], G32[m], amp[m] > cut)
        per_mode[f"{m[0]},{m[1]}"] = {
            "tau16": tau16, "tau32": tau32,
            "excluded_count": int(np.sum(~reliable)),
            "excluded_fraction": float(np.mean(~reliable)),
            "strata": {k: phase_metrics(G16[m], G32[m], sm) for k, sm in strata.items()},
            "trim_sensitivity": trim,
        }

    jac = {}
    for i, m1 in enumerate(REPS):
        for m2 in REPS[i+1:]:
            A, B = excluded_sets[m1], excluded_sets[m2]
            u = A | B
            jac[f"{m1}-{m2}"] = 1.0 if not u else float(len(A & B) / len(u))
    inter = set.intersection(*(excluded_sets[m] for m in REPS)) if REPS else set()
    union = set.union(*(excluded_sets[m] for m in REPS)) if REPS else set()

    E12 = stable_energy(F32)
    Enz = total_nonzero(F32)
    V = np.var(C32, axis=(-2, -1))
    excl = np.zeros(len(loops), dtype=bool)
    if union:
        excl[list(union)] = True
    incl = ~excl

    def stats(x, m):
        return {"mean": float(np.mean(x[m])) if np.any(m) else float("nan"), "median": float(np.median(x[m])) if np.any(m) else float("nan")}

    relation = {}
    for name, x in [("E12", E12), ("Enonzero", Enz), ("V", V)]:
        se, si = stats(x, excl), stats(x, incl)
        relation[name] = {
            "excluded": se, "included": si,
            "mean_ratio_excluded_included": float(se["mean"] / si["mean"]) if si["mean"] else float("nan"),
            "median_ratio_excluded_included": float(se["median"] / si["median"]) if si["median"] else float("nan"),
        }
    relation["zero_fractions"] = {
        "excluded_E12_zero": float(np.mean(E12[excl] == 0.0)) if np.any(excl) else float("nan"),
        "excluded_Enonzero_zero": float(np.mean(Enz[excl] == 0.0)) if np.any(excl) else float("nan"),
    }

    minamp = np.min(np.column_stack([amp[m] for m in REPS]), axis=1)
    lo, hi = np.quantile(minamp, [0.10, 0.90])
    strata3 = {
        "bottom10": minamp <= lo,
        "middle80": (minamp > lo) & (minamp < hi),
        "top10": minamp >= hi,
    }
    temporal = {}
    for name, requested in strata3.items():
        sm = requested.copy()
        for m in REPS:
            a = np.abs(G32[m])
            sm &= np.isfinite(a) & (a > 0.0)
        Y = np.column_stack([G32[m][sm] / np.abs(G32[m][sm]) for m in REPS])
        ts, As, bs = t[sm], area[sm], block_id[sm]
        Yr = residualize_area(As, Y, bs) if np.any(sm) else Y
        temporal[name] = {
            "requested_n": int(np.sum(requested)),
            "n": int(np.sum(sm)),
            "undefined_phase_dropped": int(np.sum(requested) - np.sum(sm)),
            "m2_13": score_group(ts, Y, bs, 12) if np.any(sm) else float("nan"),
            "m2_11": score_group(ts, Y, bs, 10) if np.any(sm) else float("nan"),
            "area_residualized_m2_13": score_group(ts, Yr, bs, 12) if np.any(sm) else float("nan"),
            "area_residualized_m2_11": score_group(ts, Yr, bs, 10) if np.any(sm) else float("nan"),
        }

    return {
        "start": int(loops[0]), "stop": int(loops[-1]),
        "mask_overlap": {
            "pairwise_jaccard": jac,
            "four_way_intersection_count": len(inter),
            "four_way_union_count": len(union),
            "intersection_over_union": float(len(inter)/len(union)) if union else 1.0,
            "all_masks_identical": all(excluded_sets[m] == excluded_sets[REPS[0]] for m in REPS[1:]),
        },
        "translation_relation": relation,
        "per_mode": per_mode,
        "temporal_by_min_amplitude_stratum": temporal,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--calibration", type=Path, required=True)
    ap.add_argument("--holdout", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    cal, hold = analyze(args.calibration), analyze(args.holdout)
    out = {"method":"RH-SOL-05 POISSON-03B ZERO-SAFE phase-stability diagnostic","calibration":cal,"holdout":hold}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
    print(f"WROTE {args.out}")

if __name__ == "__main__":
    main()
