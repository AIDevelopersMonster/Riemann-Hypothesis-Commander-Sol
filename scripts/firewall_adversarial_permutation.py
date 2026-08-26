#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from firewall_assignment_surrogates import (
    block_target_scores_matrix,
    load_and_concat,
    target_omegas,
)


def spectral_mismatch(y0: np.ndarray, y1: np.ndarray) -> float:
    a = np.abs(np.fft.rfft(y0 - float(np.mean(y0))))
    b = np.abs(np.fft.rfft(y1 - float(np.mean(y1))))
    return float(np.linalg.norm(b - a) / (np.linalg.norm(a) + 1e-30))


def distances(perm: np.ndarray) -> tuple[float, float, float]:
    n = len(perm)
    idx = np.arange(n)
    delta = perm - idx
    dmove = float(np.mean(perm != idx))
    dabs = float(np.mean(np.abs(delta)) / (n - 1))
    drms = float(np.sqrt(np.mean(delta.astype(float) ** 2)) / (n - 1))
    return dmove, dabs, drms


def target_scores(t: np.ndarray, y: np.ndarray, omegas: np.ndarray) -> tuple[float, float]:
    s = block_target_scores_matrix(t, y, omegas)[0]
    return float(np.mean(s[:12])), float(np.mean(s[:10]))


def energy(espec: float, dabs: float, threshold: float) -> float:
    v = max(espec - threshold, 0.0)
    return 100.0 * v * v - dabs


def better_lex(a: tuple[float, float], b: tuple[float, float]) -> bool:
    # Tuple is (violation, -dabs); smaller is better.
    return a < b


def search_block(
    y: np.ndarray,
    *,
    rng: np.random.Generator,
    restarts: int,
    proposals: int,
    threshold: float,
    t0: float,
    tend: float,
) -> dict[str, object]:
    n = len(y)
    identity = np.arange(n)

    best_perm = identity.copy()
    best_espec = 0.0
    best_dmove, best_dabs, best_drms = distances(identity)
    best_key = (0.0, -best_dabs)
    best_restart = -1
    feasible_nonidentity_encountered = 0

    for r in range(restarts):
        perm = identity.copy()
        ys = y.copy()
        espec = 0.0
        dmove, dabs, drms = distances(perm)
        cur_e = energy(espec, dabs, threshold)

        for step in range(proposals):
            i, j = rng.choice(n, size=2, replace=False)
            cand_perm = perm.copy()
            cand_perm[i], cand_perm[j] = cand_perm[j], cand_perm[i]
            cand_y = y[cand_perm]
            cand_espec = spectral_mismatch(y, cand_y)
            cand_dmove, cand_dabs, cand_drms = distances(cand_perm)
            cand_e = energy(cand_espec, cand_dabs, threshold)

            frac = step / max(proposals - 1, 1)
            temp = t0 * ((tend / t0) ** frac)
            de = cand_e - cur_e
            accept = de <= 0.0 or rng.random() < math.exp(-de / max(temp, 1e-30))
            if accept:
                perm = cand_perm
                ys = cand_y
                espec = cand_espec
                dmove, dabs, drms = cand_dmove, cand_dabs, cand_drms
                cur_e = cand_e

            if espec <= threshold and not np.array_equal(perm, identity):
                feasible_nonidentity_encountered += 1
                key = (0.0, -dabs)
                if better_lex(key, best_key):
                    best_perm = perm.copy()
                    best_espec = espec
                    best_dmove, best_dabs, best_drms = dmove, dabs, drms
                    best_key = key
                    best_restart = r

    return {
        "perm": best_perm,
        "espec": float(best_espec),
        "dmove": float(best_dmove),
        "dabs": float(best_dabs),
        "drms": float(best_drms),
        "nonidentity_feasible": bool(not np.array_equal(best_perm, identity)),
        "feasible_nonidentity_encountered": int(feasible_nonidentity_encountered),
        "selected_restart": int(best_restart),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("datasets", nargs="+", type=Path)
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--stop", type=int, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--block-size", type=int, default=1000)
    ap.add_argument("--restarts", type=int, default=20)
    ap.add_argument("--proposals", type=int, default=20000)
    ap.add_argument("--threshold", type=float, default=0.05)
    ap.add_argument("--t0", type=float, default=0.02)
    ap.add_argument("--tend", type=float, default=1e-5)
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

    rng = np.random.default_rng(args.seed)
    selected = np.empty_like(area_blocks)
    blocks: list[dict[str, object]] = []

    for b in range(nblocks):
        res = search_block(
            area_blocks[b],
            rng=rng,
            restarts=args.restarts,
            proposals=args.proposals,
            threshold=args.threshold,
            t0=args.t0,
            tend=args.tend,
        )
        perm = np.asarray(res.pop("perm"), dtype=int)
        selected[b] = area_blocks[b][perm]
        res["block"] = b + 1
        blocks.append(res)
        print(
            f"block={b+1:02d}/{nblocks} espec={res['espec']:.6f} "
            f"dmove={res['dmove']:.4f} dabs={res['dabs']:.4f} "
            f"feasible_nonidentity={res['nonidentity_feasible']}",
            flush=True,
        )

    obs13 = []
    obs11 = []
    adv13 = []
    adv11 = []
    for b in range(nblocks):
        a13, a11 = target_scores(time_blocks[b], area_blocks[b], omegas)
        s13, s11 = target_scores(time_blocks[b], selected[b], omegas)
        obs13.append(a13)
        obs11.append(a11)
        adv13.append(s13)
        adv11.append(s11)

    especs = np.array([float(x["espec"]) for x in blocks])
    dmoves = np.array([float(x["dmove"]) for x in blocks])
    dabs = np.array([float(x["dabs"]) for x in blocks])
    drms = np.array([float(x["drms"]) for x in blocks])
    nonid = np.array([bool(x["nonidentity_feasible"]) for x in blocks])

    result = {
        "method": "adversarial constrained exact-multiset permutation search",
        "start": args.start,
        "stop": args.stop,
        "n_loops": int(len(loops)),
        "block_size": int(n),
        "n_blocks": int(nblocks),
        "restarts": int(args.restarts),
        "proposals_per_restart": int(args.proposals),
        "spectral_threshold": float(args.threshold),
        "t0": float(args.t0),
        "tend": float(args.tend),
        "seed": int(args.seed),
        "blocks": blocks,
        "range_summary": {
            "mean_espec": float(np.mean(especs)),
            "max_espec": float(np.max(especs)),
            "mean_dmove": float(np.mean(dmoves)),
            "mean_dabs": float(np.mean(dabs)),
            "mean_drms": float(np.mean(drms)),
            "blocks_nonidentity_feasible": int(np.sum(nonid)),
            "blocks_dmove_ge_0_10": int(np.sum(dmoves >= 0.10)),
            "blocks_dabs_ge_0_02": int(np.sum(dabs >= 0.02)),
        },
        "target_scores_posthoc": {
            "observed_m2_13": float(np.mean(obs13)),
            "adversarial_m2_13": float(np.mean(adv13)),
            "observed_m2_11": float(np.mean(obs11)),
            "adversarial_m2_11": float(np.mean(adv11)),
        },
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"range_summary": result["range_summary"], "target_scores_posthoc": result["target_scores_posthoc"]}, indent=2))
    print(f"WROTE {args.out}")


if __name__ == "__main__":
    main()
