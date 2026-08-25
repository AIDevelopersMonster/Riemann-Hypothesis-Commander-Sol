#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from firewall_assignment_surrogates import (
    block_target_scores_matrix,
    load_and_concat,
    summarize_null,
    target_omegas,
)


def iaaft_one(y: np.ndarray, rng: np.random.Generator, iterations: int) -> tuple[np.ndarray, float]:
    y = np.asarray(y, dtype=float)
    n = len(y)
    mu = float(np.mean(y))
    sorted_y = np.sort(y)
    target_mag = np.abs(np.fft.rfft(y - mu))

    cur = rng.permutation(y)
    for _ in range(iterations):
        centered = cur - float(np.mean(cur))
        spec = np.fft.rfft(centered)
        amp = np.abs(spec)
        phase = np.ones_like(spec, dtype=complex)
        nz = amp > 0
        phase[nz] = spec[nz] / amp[nz]
        spectral = np.fft.irfft(target_mag * phase, n=n)

        order = np.argsort(spectral, kind="mergesort")
        ranked = np.empty_like(spectral)
        ranked[order] = sorted_y
        cur = ranked

    final_centered = cur - float(np.mean(cur))
    final_mag = np.abs(np.fft.rfft(final_centered))
    denom = float(np.linalg.norm(target_mag)) + 1e-30
    mismatch = float(np.linalg.norm(final_mag - target_mag) / denom)
    return cur, mismatch


def iaaft_best_of_starts(
    y: np.ndarray,
    rng: np.random.Generator,
    *,
    iterations: int,
    starts: int,
) -> tuple[np.ndarray, float]:
    best_y = None
    best_mm = np.inf
    for _ in range(starts):
        cand, mm = iaaft_one(y, rng, iterations)
        if mm < best_mm:
            best_y = cand
            best_mm = mm
    assert best_y is not None
    return best_y, float(best_mm)


def score_range(area_blocks: np.ndarray, time_blocks: np.ndarray, omegas: np.ndarray, n_targets: int) -> float:
    vals = []
    for b in range(area_blocks.shape[0]):
        s = block_target_scores_matrix(time_blocks[b], area_blocks[b], omegas)
        vals.append(float(np.mean(s[0, :n_targets])))
    return float(np.mean(vals))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("datasets", nargs="+", type=Path)
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--stop", type=int, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--block-size", type=int, default=1000)
    ap.add_argument("--B", type=int, default=500)
    ap.add_argument("--iterations", type=int, default=2000)
    ap.add_argument("--starts", type=int, default=4)
    ap.add_argument("--seed", type=int, required=True)
    args = ap.parse_args()

    d = load_and_concat(args.datasets)
    sel = (d["loops"] >= args.start) & (d["loops"] <= args.stop)
    loops = d["loops"][sel]
    area = np.asarray(d["area"][sel], dtype=float)
    time = 0.5 * (
        np.asarray(d["gamma0"][sel], dtype=float)
        + np.asarray(d["gamma1"][sel], dtype=float)
    )

    expected = np.arange(args.start, args.stop + 1)
    if len(loops) != len(expected) or not np.array_equal(loops, expected):
        raise SystemExit("requested loop range is not contiguous")
    if len(loops) % args.block_size:
        raise SystemExit("range length must be divisible by block size")

    nblocks = len(loops) // args.block_size
    area_blocks = area.reshape(nblocks, args.block_size)
    time_blocks = time.reshape(nblocks, args.block_size)
    omegas = target_omegas(2, 13)

    obs13 = score_range(area_blocks, time_blocks, omegas, 12)
    obs11 = score_range(area_blocks, time_blocks, omegas, 10)

    rng = np.random.default_rng(args.seed)
    null13 = np.empty(args.B, dtype=float)
    null11 = np.empty(args.B, dtype=float)
    mean_mismatch = np.empty(args.B, dtype=float)
    max_mismatch = np.empty(args.B, dtype=float)

    for i in range(args.B):
        surr = np.empty_like(area_blocks)
        mm = np.empty(nblocks, dtype=float)
        for b in range(nblocks):
            surr[b], mm[b] = iaaft_best_of_starts(
                area_blocks[b],
                rng,
                iterations=args.iterations,
                starts=args.starts,
            )
        null13[i] = score_range(surr, time_blocks, omegas, 12)
        null11[i] = score_range(surr, time_blocks, omegas, 10)
        mean_mismatch[i] = float(np.mean(mm))
        max_mismatch[i] = float(np.max(mm))
        if (i + 1) % 25 == 0:
            print(f"SURROGATES {i+1}/{args.B}", flush=True)

    result = {
        "method": "blockwise IAAFT convergence stress test, best spectral-fidelity start",
        "start": args.start,
        "stop": args.stop,
        "n_loops": int(len(loops)),
        "block_size": int(args.block_size),
        "n_blocks": int(nblocks),
        "B": int(args.B),
        "iterations": int(args.iterations),
        "starts": int(args.starts),
        "seed": int(args.seed),
        "m2_13": summarize_null(obs13, null13),
        "m2_11": summarize_null(obs11, null11),
        "spectral_mismatch": {
            "median_mean": float(np.median(mean_mismatch)),
            "q95_mean": float(np.quantile(mean_mismatch, 0.95)),
            "max_mean": float(np.max(mean_mismatch)),
            "median_max_block": float(np.median(max_mismatch)),
            "max_max_block": float(np.max(max_mismatch)),
            "fraction_mean_le_0_05": float(np.mean(mean_mismatch <= 0.05)),
            "fraction_mean_le_0_02": float(np.mean(mean_mismatch <= 0.02)),
            "fidelity_gate_median_mean_le_0_05": bool(np.median(mean_mismatch) <= 0.05),
        },
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    print(f"WROTE {args.out}")


if __name__ == "__main__":
    main()
