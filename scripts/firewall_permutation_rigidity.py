#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from firewall_assignment_surrogates import (
    block_target_scores_matrix,
    load_and_concat,
    target_omegas,
)

FRACTIONS = np.array([0.01, 0.02, 0.05, 0.10, 0.20, 0.40, 0.60, 0.80, 1.00], dtype=float)


def qsummary(x: np.ndarray) -> dict[str, float]:
    x = np.asarray(x, dtype=float)
    return {
        "min": float(np.min(x)),
        "q05": float(np.quantile(x, 0.05)),
        "median": float(np.median(x)),
        "q95": float(np.quantile(x, 0.95)),
        "max": float(np.max(x)),
    }


def spectral_mismatch(y0: np.ndarray, y1: np.ndarray) -> float:
    a = np.abs(np.fft.rfft(y0 - float(np.mean(y0))))
    b = np.abs(np.fft.rfft(y1 - float(np.mean(y1))))
    return float(np.linalg.norm(b - a) / (np.linalg.norm(a) + 1e-30))


def block_scores(t: np.ndarray, y: np.ndarray, omegas: np.ndarray) -> tuple[float, float]:
    s = block_target_scores_matrix(t, y, omegas)[0]
    return float(np.mean(s[:12])), float(np.mean(s[:10]))


def make_partial_permutation(n: int, frac: float, rng: np.random.Generator) -> np.ndarray:
    k = max(2, int(round(frac * n)))
    k = min(k, n)
    pos = rng.choice(n, size=k, replace=False)
    perm = np.arange(n)
    while True:
        src = rng.permutation(pos)
        if not np.array_equal(src, pos):
            break
    perm[pos] = src
    return perm


def corr(x: np.ndarray, y: np.ndarray) -> float:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if np.std(x) == 0 or np.std(y) == 0:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("datasets", nargs="+", type=Path)
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--stop", type=int, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--block-size", type=int, default=1000)
    ap.add_argument("--B", type=int, default=300)
    ap.add_argument("--seed", type=int, required=True)
    args = ap.parse_args()

    d = load_and_concat(args.datasets)
    sel = (d["loops"] >= args.start) & (d["loops"] <= args.stop)
    loops = d["loops"][sel]
    area = np.asarray(d["area"][sel], dtype=float)
    time = 0.5 * (np.asarray(d["gamma0"][sel], dtype=float) + np.asarray(d["gamma1"][sel], dtype=float))

    expected = np.arange(args.start, args.stop + 1)
    if len(loops) != len(expected) or not np.array_equal(loops, expected):
        raise SystemExit("requested loop range is not contiguous")
    if len(loops) % args.block_size:
        raise SystemExit("range length must be divisible by block size")

    nblocks = len(loops) // args.block_size
    n = args.block_size
    area_blocks = area.reshape(nblocks, n)
    time_blocks = time.reshape(nblocks, n)
    omegas = target_omegas(2, 13)

    observed13 = float(np.mean([block_scores(time_blocks[b], area_blocks[b], omegas)[0] for b in range(nblocks)]))
    observed11 = float(np.mean([block_scores(time_blocks[b], area_blocks[b], omegas)[1] for b in range(nblocks)]))

    rng = np.random.default_rng(args.seed)
    by_fraction: dict[str, object] = {}
    all_moved: list[float] = []
    all_abs: list[float] = []
    all_rms: list[float] = []
    all_spec: list[float] = []
    all_s13: list[float] = []
    all_s11: list[float] = []

    for fi, frac in enumerate(FRACTIONS):
        moved = np.empty(args.B)
        dabs = np.empty(args.B)
        drms = np.empty(args.B)
        espec = np.empty(args.B)
        emax = np.empty(args.B)
        s13 = np.empty(args.B)
        s11 = np.empty(args.B)

        for r in range(args.B):
            bmoved = []
            bdabs = []
            bdrms = []
            bspec = []
            bs13 = []
            bs11 = []
            for b in range(nblocks):
                perm = make_partial_permutation(n, float(frac), rng)
                idx = np.arange(n)
                ys = area_blocks[b][perm]
                delta = perm - idx
                bmoved.append(float(np.mean(perm != idx)))
                bdabs.append(float(np.mean(np.abs(delta)) / (n - 1)))
                bdrms.append(float(np.sqrt(np.mean(delta.astype(float) ** 2)) / (n - 1)))
                bspec.append(spectral_mismatch(area_blocks[b], ys))
                a13, a11 = block_scores(time_blocks[b], ys, omegas)
                bs13.append(a13)
                bs11.append(a11)
            moved[r] = np.mean(bmoved)
            dabs[r] = np.mean(bdabs)
            drms[r] = np.mean(bdrms)
            espec[r] = np.mean(bspec)
            emax[r] = np.max(bspec)
            s13[r] = np.mean(bs13)
            s11[r] = np.mean(bs11)

            if (r + 1) % 50 == 0:
                print(f"fraction={frac:.2f} {r+1}/{args.B}", flush=True)

        key = f"{frac:.2f}"
        by_fraction[key] = {
            "shuffle_fraction": float(frac),
            "moved_fraction": qsummary(moved),
            "mean_abs_displacement": qsummary(dabs),
            "mean_rms_displacement": qsummary(drms),
            "spectral_mismatch_mean": qsummary(espec),
            "spectral_mismatch_max_block": qsummary(emax),
            "score_m2_13": qsummary(s13),
            "score_m2_11": qsummary(s11),
            "count_mean_espec_le_0_05": int(np.sum(espec <= 0.05)),
            "count_mean_espec_le_0_10": int(np.sum(espec <= 0.10)),
            "count_espec_le_0_05_and_moved_ge_0_10": int(np.sum((espec <= 0.05) & (moved >= 0.10))),
            "count_espec_le_0_05_and_abs_ge_0_02": int(np.sum((espec <= 0.05) & (dabs >= 0.02))),
        }

        all_moved.extend(moved.tolist())
        all_abs.extend(dabs.tolist())
        all_rms.extend(drms.tolist())
        all_spec.extend(espec.tolist())
        all_s13.extend(s13.tolist())
        all_s11.extend(s11.tolist())

    A_moved = np.asarray(all_moved)
    A_abs = np.asarray(all_abs)
    A_rms = np.asarray(all_rms)
    A_spec = np.asarray(all_spec)
    A_s13 = np.asarray(all_s13)
    A_s11 = np.asarray(all_s11)

    result = {
        "method": "controlled exact-multiset partial-permutation rigidity map",
        "start": args.start,
        "stop": args.stop,
        "n_loops": int(len(loops)),
        "block_size": int(n),
        "n_blocks": int(nblocks),
        "B_per_fraction": int(args.B),
        "seed": int(args.seed),
        "fractions": [float(x) for x in FRACTIONS],
        "observed": {"m2_13": observed13, "m2_11": observed11},
        "by_fraction": by_fraction,
        "global_correlations": {
            "spectral_mismatch_vs_moved_fraction": corr(A_spec, A_moved),
            "spectral_mismatch_vs_abs_displacement": corr(A_spec, A_abs),
            "spectral_mismatch_vs_rms_displacement": corr(A_spec, A_rms),
            "score_m2_13_vs_spectral_mismatch": corr(A_s13, A_spec),
            "score_m2_13_vs_moved_fraction": corr(A_s13, A_moved),
            "score_m2_13_vs_abs_displacement": corr(A_s13, A_abs),
            "score_m2_11_vs_spectral_mismatch": corr(A_s11, A_spec),
        },
        "global_feasibility_counts": {
            "total_realizations": int(len(A_spec)),
            "mean_espec_le_0_05": int(np.sum(A_spec <= 0.05)),
            "mean_espec_le_0_10": int(np.sum(A_spec <= 0.10)),
            "espec_le_0_05_and_moved_ge_0_10": int(np.sum((A_spec <= 0.05) & (A_moved >= 0.10))),
            "espec_le_0_05_and_abs_ge_0_02": int(np.sum((A_spec <= 0.05) & (A_abs >= 0.02))),
        },
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"observed": result["observed"], "global_correlations": result["global_correlations"], "global_feasibility_counts": result["global_feasibility_counts"]}, indent=2))
    print(f"WROTE {args.out}")


if __name__ == "__main__":
    main()
