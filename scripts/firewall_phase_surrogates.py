#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from firewall_assignment_surrogates import load_and_concat, target_omegas, block_target_scores_matrix, summarize_null


def phase_randomized_blocks(area_blocks: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    nblocks, n = area_blocks.shape
    out = np.empty_like(area_blocks, dtype=float)
    for b in range(nblocks):
        y = np.asarray(area_blocks[b], dtype=float)
        mu = float(np.mean(y))
        yc = y - mu
        spec = np.fft.rfft(yc)
        mag = np.abs(spec)
        new = np.zeros_like(spec)
        new[0] = 0.0
        last = len(spec) - 1
        has_nyquist = (n % 2 == 0)
        phase_end = last if has_nyquist else last + 1
        if phase_end > 1:
            phases = rng.uniform(0.0, 2.0 * math.pi, size=phase_end - 1)
            new[1:phase_end] = mag[1:phase_end] * np.exp(1j * phases)
        if has_nyquist:
            sign = -1.0 if rng.random() < 0.5 else 1.0
            new[last] = sign * mag[last]
        yr = np.fft.irfft(new, n=n)
        out[b] = yr + mu
    return out


def range_score(area_blocks: np.ndarray, time_blocks: np.ndarray, omegas: np.ndarray, n_targets: int) -> float:
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
    ap.add_argument("--B", type=int, default=5000)
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
    area_blocks = area.reshape(nblocks, args.block_size)
    time_blocks = time.reshape(nblocks, args.block_size)
    omegas = target_omegas(2, 13)

    obs13 = range_score(area_blocks, time_blocks, omegas, 12)
    obs11 = range_score(area_blocks, time_blocks, omegas, 10)

    rng = np.random.default_rng(args.seed)
    null13 = np.empty(args.B, dtype=float)
    null11 = np.empty(args.B, dtype=float)

    for i in range(args.B):
        surr = phase_randomized_blocks(area_blocks, rng)
        null13[i] = range_score(surr, time_blocks, omegas, 12)
        null11[i] = range_score(surr, time_blocks, omegas, 10)
        if (i + 1) % 250 == 0:
            print(f"SURROGATES {i+1}/{args.B}")

    result = {
        "method": "blockwise loop-index FFT phase randomization with exact magnitude preservation",
        "start": args.start,
        "stop": args.stop,
        "n_loops": int(len(loops)),
        "block_size": int(args.block_size),
        "n_blocks": int(nblocks),
        "B": int(args.B),
        "seed": int(args.seed),
        "m2_13": summarize_null(obs13, null13),
        "m2_11": summarize_null(obs11, null11),
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    print(f"WROTE {args.out}")


if __name__ == "__main__":
    main()
