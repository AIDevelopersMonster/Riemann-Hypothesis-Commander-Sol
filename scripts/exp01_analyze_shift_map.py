#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, json, sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dirichlet_spectrum import (
    warped_spectrum,
    comb_score,
    jitter_null,
    benjamini_hochberg,
)

FROZEN_UNSHIFTED_BASELINE = 2.0335818528


def load_legacy_time_csv(path: Path, loops: np.ndarray) -> np.ndarray:
    mapping: dict[int, float] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None or "loop" not in reader.fieldnames or "t_near" not in reader.fieldnames:
            raise SystemExit("legacy time CSV must contain loop,t_near columns")
        for row in reader:
            mapping[int(row["loop"])] = float(row["t_near"])
    missing = [int(n) for n in loops if int(n) not in mapping]
    if missing:
        raise SystemExit(f"legacy time CSV missing loops: {missing[:10]}")
    return np.array([mapping[int(n)] for n in loops], dtype=float)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", type=Path, required=True)
    ap.add_argument("--rule", default="winding")
    ap.add_argument("--q", type=int, default=16)
    ap.add_argument("--legacy-time-csv", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--B", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=20260822)
    args = ap.parse_args()

    key_rule = args.rule.replace("-", "_")
    with np.load(args.dataset, allow_pickle=False) as z:
        loops = z["loops"].astype(int)
        counts = z[f"counts_{key_rule}_q{args.q}"].astype(float)
        gamma0 = z["gamma0"].astype(float)
        gamma1 = z["gamma1"].astype(float)

    if args.legacy_time_csv:
        time_proxy = load_legacy_time_csv(args.legacy_time_csv, loops)
        time_mode = "RH-SOL-01 legacy t_near"
    else:
        time_proxy = 0.5 * (gamma0 + gamma1)
        time_mode = "zero-pair midpoint"

    if len(loops) % 1000:
        raise SystemExit("EXP-01 spectral map requires a loop count divisible by 1000")

    rows = []
    q = args.q
    for iy in range(q):
        for ix in range(q):
            spectrum = warped_spectrum(counts[:, iy, ix], time_proxy)
            observed, null = jitter_null(
                spectrum,
                B=args.B,
                seed=args.seed + iy * q + ix,
            )
            p = (1.0 + float(np.sum(null >= observed))) / (args.B + 1.0)
            rows.append(
                {
                    "iy": iy,
                    "ix": ix,
                    "dx": (ix + 0.5) / q,
                    "dy": (iy + 0.5) / q,
                    "comb_score": comb_score(spectrum),
                    "p_jitter": p,
                    "null_median": float(np.median(null)),
                    "null_q95": float(np.quantile(null, 0.95)),
                    "null_q99": float(np.quantile(null, 0.99)),
                }
            )

    pvals = np.array([r["p_jitter"] for r in rows], dtype=float)
    qvals = benjamini_hochberg(pvals)
    for row, qv in zip(rows, qvals):
        row["q_bh"] = float(qv)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "iy", "ix", "dx", "dy", "comb_score", "p_jitter",
        "null_median", "null_q95", "null_q99", "q_bh",
    ]
    with args.out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    scores = np.array([r["comb_score"] for r in rows], dtype=float)
    jmax = int(np.argmax(scores))
    jmin = int(np.argmin(scores))
    top = rows[jmax]
    bottom = rows[jmin]

    summary = {
        "n_loops": int(len(loops)),
        "start": int(loops.min()),
        "stop": int(loops.max()),
        "q": q,
        "rule": args.rule,
        "time_proxy": time_mode,
        "B": args.B,
        "seed_base": args.seed,
        "frozen_unshifted_baseline": FROZEN_UNSHIFTED_BASELINE,
        "median_comb_score": float(np.median(scores)),
        "min_comb_score": float(np.min(scores)),
        "max_comb_score": float(np.max(scores)),
        "mean_comb_score": float(np.mean(scores)),
        "fraction_above_unshifted_baseline": float(np.mean(scores > FROZEN_UNSHIFTED_BASELINE)),
        "fraction_p_lt_0_05": float(np.mean(pvals < 0.05)),
        "fraction_q_bh_lt_0_05": float(np.mean(qvals < 0.05)),
        "strongest_shift": {
            "dx": float(top["dx"]),
            "dy": float(top["dy"]),
            "comb_score": float(top["comb_score"]),
            "p_jitter": float(top["p_jitter"]),
            "q_bh": float(top["q_bh"]),
        },
        "weakest_shift": {
            "dx": float(bottom["dx"]),
            "dy": float(bottom["dy"]),
            "comb_score": float(bottom["comb_score"]),
            "p_jitter": float(bottom["p_jitter"]),
            "q_bh": float(bottom["q_bh"]),
        },
    }
    args.out.with_suffix(".json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
