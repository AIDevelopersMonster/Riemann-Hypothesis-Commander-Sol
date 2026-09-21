#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("lab03", HERE / "walsh_degree_spectrum.py")
lab03 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab03)

SEEDS = lab03.SEEDS


def shell(n: int) -> int:
    return -1 if n == 0 else n.bit_length() - 1


def stratified_shuffle(values, seed: int):
    out = values[:]
    groups = {}
    for n, v in enumerate(values):
        groups.setdefault((n % 210, shell(n)), []).append(n)

    for (residue, sh), idx in groups.items():
        labels = [values[i] for i in idx]
        lab03.deterministic_shuffle(
            labels,
            seed + 1000003 * residue + 10000019 * (sh + 2)
        )
        for i, v in zip(idx, labels):
            out[i] = v
    return out


def tv(a, b):
    return 0.5 * sum(abs(x-y) for x, y in zip(a[1:], b[1:]))


def span(vals):
    return min(vals), max(vals), statistics.mean(vals)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default="lab04_out")
    ap.add_argument("--widths", nargs="+", type=int, default=list(range(8,17)))
    a = ap.parse_args()

    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    summary = []

    for w in a.widths:
        prime = lab03.prime_indicator(w)
        psp = lab03.spectrum(prime, w)

        samples = []
        for seed in SEEDS:
            b = stratified_shuffle(prime, seed + 7000003*w)
            bsp = lab03.spectrum(b, w)
            samples.append({
                "seed": seed,
                "tv_renorm": tv(psp["renorm"], bsp["renorm"]),
                "centroid_delta": psp["centroid"] - bsp["centroid"],
                "low2_delta": psp["low_mass_2"] - bsp["low_mass_2"],
                "low4_delta": psp["low_mass_4"] - bsp["low_mass_4"],
                "entropy_delta": psp["entropy"] - bsp["entropy"],
            })

        e = {
            "width": w,
            "prime_low2": psp["low_mass_2"],
            "prime_low4": psp["low_mass_4"],
            "prime_centroid": psp["centroid"],
            "samples": samples,
        }
        for key in ["tv_renorm","centroid_delta","low2_delta","low4_delta","entropy_delta"]:
            vals=[x[key] for x in samples]
            e[key+"_min"]=min(vals)
            e[key+"_max"]=max(vals)
            e[key+"_mean"]=statistics.mean(vals)
        summary.append(e)
        print(f"done W={w}")

    (out / "walsh_stratified_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    lines=[
        "# H20-EXT-LAB-04 · Walsh spectrum with wheel-210 + dyadic-density preservation",
        "",
        "Status: **COMPUTATION COMPLETE**",
        "",
        "| W | TV mean | low2 delta mean [min,max] | low4 delta mean [min,max] | centroid delta mean [min,max] |",
        "|---:|---:|---:|---:|---:|",
    ]
    for e in summary:
        lines.append(
            f"| {e['width']} | {e['tv_renorm_mean']:.8f} | "
            f"{e['low2_delta_mean']:.9f} [{e['low2_delta_min']:.9f},{e['low2_delta_max']:.9f}] | "
            f"{e['low4_delta_mean']:.9f} [{e['low4_delta_min']:.9f},{e['low4_delta_max']:.9f}] | "
            f"{e['centroid_delta_mean']:.9f} [{e['centroid_delta_min']:.9f},{e['centroid_delta_max']:.9f}] |"
        )

    lines += [
        "",
        "## Exact finite statement",
        "",
        f"The frozen stratified baseline was evaluated for W={min(a.widths)}..{max(a.widths)} with all five fixed seeds.",
        "",
        "## Non-claim",
        "",
        "This finite experiment alone implies no asymptotic theorem, novelty claim, circuit lower bound, or RH relation.",
    ]
    (out / "H20_EXT_LAB04_REPORT.md").write_text("\n".join(lines)+"\n", encoding="utf-8")


if __name__ == "__main__":
    main()
