#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dirichlet_spectrum import (
    warped_spectrum,
    comb_score,
    jitter_null,
    benjamini_hochberg,
)


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
        phase = pd.read_csv(args.legacy_time_csv).sort_values("loop")
        mapping = phase.set_index("loop")["t_near"]
        time_proxy = np.array([mapping.loc[int(n)] for n in loops], dtype=float)
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

    out = pd.DataFrame(rows)
    out["q_bh"] = benjamini_hochberg(out["p_jitter"].to_numpy())
    args.out.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False)

    summary = {
        "n_loops": int(len(loops)),
        "start": int(loops.min()),
        "stop": int(loops.max()),
        "q": q,
        "rule": args.rule,
        "time_proxy": time_mode,
        "B": args.B,
        "seed_base": args.seed,
        "median_comb_score": float(out["comb_score"].median()),
        "min_comb_score": float(out["comb_score"].min()),
        "max_comb_score": float(out["comb_score"].max()),
        "fraction_p_lt_0_05": float(np.mean(out["p_jitter"] < 0.05)),
        "fraction_q_bh_lt_0_05": float(np.mean(out["q_bh"] < 0.05)),
    }
    args.out.with_suffix(".json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
