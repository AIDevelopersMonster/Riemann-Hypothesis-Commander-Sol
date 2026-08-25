#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


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


def target_omegas(m_min: int = 2, m_max: int = 13) -> np.ndarray:
    return np.log(np.arange(m_min, m_max + 1, dtype=float))


def orthonormal_columns(x: np.ndarray) -> np.ndarray:
    q, _ = np.linalg.qr(np.asarray(x, dtype=float), mode="reduced")
    return q


def block_target_scores_matrix(t: np.ndarray, Y: np.ndarray, omegas: np.ndarray) -> np.ndarray:
    """Return target scores for many candidate y columns on one fixed time block.

    Y shape: (n, k). Output shape: (k, n_targets).
    """
    t = np.asarray(t, dtype=float)
    Y = np.asarray(Y, dtype=float)
    if Y.ndim == 1:
        Y = Y[:, None]
    if Y.shape[0] != len(t):
        raise ValueError("time and Y row counts differ")

    tc = t - np.mean(t)
    X = np.column_stack([np.ones_like(tc), tc])
    qx = orthonormal_columns(X)
    R = Y - qx @ (qx.T @ Y)
    sst = np.sum(R * R, axis=0)
    sst = np.maximum(sst, 1e-30)

    out = np.empty((Y.shape[1], len(omegas)), dtype=float)
    ts = t - t[0]
    for j, omega in enumerate(omegas):
        B = np.column_stack([np.cos(omega * ts), np.sin(omega * ts)])
        qb = orthonormal_columns(B)
        proj = qb.T @ R
        explained = np.sum(proj * proj, axis=0)
        r2 = np.clip(explained / sst, 0.0, 1.0)
        out[:, j] = -np.log(np.maximum(1.0 - r2, 1e-15))
    return out


def circular_score_table(area_blocks: np.ndarray, time_blocks: np.ndarray, omegas: np.ndarray) -> np.ndarray:
    nblocks, block_size = area_blocks.shape
    table = np.empty((nblocks, block_size, len(omegas)), dtype=float)
    for b in range(nblocks):
        y = area_blocks[b]
        # Column k is y circularly shifted by k positions.
        Y = np.column_stack([np.roll(y, k) for k in range(block_size)])
        table[b] = block_target_scores_matrix(time_blocks[b], Y, omegas)
    return table


def block_pair_score_table(area_blocks: np.ndarray, time_blocks: np.ndarray, omegas: np.ndarray) -> np.ndarray:
    nblocks = area_blocks.shape[0]
    table = np.empty((nblocks, nblocks, len(omegas)), dtype=float)
    # table[j_time, i_area, target]
    Y_all = area_blocks.T
    for j in range(nblocks):
        table[j] = block_target_scores_matrix(time_blocks[j], Y_all, omegas)
    return table


def summarize_null(observed: float, vals: np.ndarray) -> dict[str, float]:
    vals = np.asarray(vals, dtype=float)
    return {
        "observed": float(observed),
        "null_median": float(np.median(vals)),
        "null_q95": float(np.quantile(vals, 0.95)),
        "null_q99": float(np.quantile(vals, 0.99)),
        "null_max": float(np.max(vals)),
        "empirical_p_ge": float((1.0 + np.sum(vals >= observed)) / (len(vals) + 1.0)),
    }


def aggregate_target_subset(target_scores: np.ndarray, n_targets: int) -> np.ndarray:
    return np.mean(target_scores[..., :n_targets], axis=-1)


def circular_surrogates(
    table: np.ndarray,
    *,
    B: int,
    seed: int,
    n_targets: int,
) -> tuple[float, np.ndarray]:
    nblocks, block_size, _ = table.shape
    block_scores = aggregate_target_subset(table, n_targets)
    observed = float(np.mean(block_scores[:, 0]))
    rng = np.random.default_rng(seed)
    offsets = rng.integers(1, block_size, size=(B, nblocks), endpoint=False)
    vals = np.empty(B, dtype=float)
    rows = np.arange(nblocks)
    for i in range(B):
        vals[i] = float(np.mean(block_scores[rows, offsets[i]]))
    return observed, vals


def block_reassignment_surrogates(
    pair_table: np.ndarray,
    *,
    B: int,
    seed: int,
    n_targets: int,
) -> tuple[float, np.ndarray]:
    nblocks = pair_table.shape[0]
    pair_scores = aggregate_target_subset(pair_table, n_targets)
    idx = np.arange(nblocks)
    observed = float(np.mean(pair_scores[idx, idx]))
    rng = np.random.default_rng(seed)
    vals = np.empty(B, dtype=float)
    for i in range(B):
        perm = rng.permutation(nblocks)
        while np.array_equal(perm, idx):
            perm = rng.permutation(nblocks)
        vals[i] = float(np.mean(pair_scores[idx, perm]))
    return observed, vals


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("datasets", nargs="+", type=Path)
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--stop", type=int, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--block-size", type=int, default=1000)
    ap.add_argument("--B", type=int, default=5000)
    ap.add_argument("--seed-circular", type=int, default=20260825)
    ap.add_argument("--seed-block", type=int, default=20260826)
    args = ap.parse_args()

    d = load_and_concat(args.datasets)
    sel = (d["loops"] >= args.start) & (d["loops"] <= args.stop)
    loops = d["loops"][sel]
    area = np.asarray(d["area"][sel], dtype=float)
    time = 0.5 * (np.asarray(d["gamma0"][sel], dtype=float) + np.asarray(d["gamma1"][sel], dtype=float))

    expected = np.arange(args.start, args.stop + 1)
    if len(loops) != len(expected) or not np.array_equal(loops, expected):
        raise SystemExit("requested loop range is not contiguous in supplied datasets")
    if len(loops) % args.block_size:
        raise SystemExit("requested range length must be divisible by block size")

    nblocks = len(loops) // args.block_size
    area_blocks = area.reshape(nblocks, args.block_size)
    time_blocks = time.reshape(nblocks, args.block_size)
    omegas = target_omegas(2, 13)

    print(f"PRECOMPUTE circular table: blocks={nblocks} shifts={args.block_size} targets={len(omegas)}")
    circ_table = circular_score_table(area_blocks, time_blocks, omegas)
    print(f"PRECOMPUTE block-pair table: time_blocks={nblocks} area_blocks={nblocks} targets={len(omegas)}")
    pair_table = block_pair_score_table(area_blocks, time_blocks, omegas)

    result: dict[str, object] = {
        "method": "target-only partial sinusoidal explained-variance firewall score",
        "start": args.start,
        "stop": args.stop,
        "n_loops": int(len(loops)),
        "block_size": args.block_size,
        "n_blocks": int(nblocks),
        "B": args.B,
        "seed_circular": args.seed_circular,
        "seed_block": args.seed_block,
        "targets": {str(m): float(math.log(m)) for m in range(2, 14)},
    }

    for label, nt in [("m2_13", 12), ("m2_11", 10)]:
        obs_c, null_c = circular_surrogates(
            circ_table, B=args.B, seed=args.seed_circular, n_targets=nt
        )
        obs_b, null_b = block_reassignment_surrogates(
            pair_table, B=args.B, seed=args.seed_block, n_targets=nt
        )
        result[label] = {
            "circular_offset": summarize_null(obs_c, null_c),
            "block_reassignment": summarize_null(obs_b, null_b),
        }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({"m2_13": result["m2_13"], "m2_11": result["m2_11"]}, indent=2))
    print(f"WROTE {args.out}")


if __name__ == "__main__":
    main()
