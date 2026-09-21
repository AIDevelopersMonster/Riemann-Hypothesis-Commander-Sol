#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from pathlib import Path

SEEDS = [1729, 271828, 314159, 1618033, 5772157]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def deterministic_shuffle(a, seed: int):
    state = seed & ((1 << 64) - 1)

    def next_u64():
        nonlocal state
        state = (state + 0x9E3779B97F4A7C15) & ((1 << 64) - 1)
        z = state
        z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9 & ((1 << 64) - 1)
        z = (z ^ (z >> 27)) * 0x94D049BB133111EB & ((1 << 64) - 1)
        return (z ^ (z >> 31)) & ((1 << 64) - 1)

    for i in range(len(a) - 1, 0, -1):
        j = next_u64() % (i + 1)
        a[i], a[j] = a[j], a[i]


def prime_indicator(width: int):
    n = 1 << width
    return [1 if is_prime(x) else 0 for x in range(n)]


def fixed_count_random(values, seed: int):
    idx = list(range(len(values)))
    deterministic_shuffle(idx, seed)
    k = sum(values)
    ones = set(idx[:k])
    return [1 if i in ones else 0 for i in range(len(values))]


def shuffled(values, seed: int):
    out = values[:]
    deterministic_shuffle(out, seed)
    return out


def wheel_shuffle(values, modulus: int, seed: int):
    out = values[:]
    for residue in range(modulus):
        idx = list(range(residue, len(values), modulus))
        labels = [values[i] for i in idx]
        deterministic_shuffle(labels, seed + 1000003 * modulus + 8191 * residue)
        for i, v in zip(idx, labels):
            out[i] = v
    return out


def fwht(a):
    out = a[:]
    h = 1
    n = len(out)
    while h < n:
        step = h << 1
        for i in range(0, n, step):
            for j in range(i, i + h):
                x = out[j]
                y = out[j + h]
                out[j] = x + y
                out[j + h] = x - y
        h = step
    return out


def spectrum(values, width: int):
    signed = [1 if v == 0 else -1 for v in values]
    coeff = fwht(signed)
    energies = [0] * (width + 1)
    for mask, c in enumerate(coeff):
        energies[mask.bit_count()] += c * c

    total = 1 << (2 * width)
    if sum(energies) != total:
        raise AssertionError((width, sum(energies), total))

    norm = [e / total for e in energies]
    nonconst_total = sum(norm[1:])
    renorm = [0.0] + ([x / nonconst_total for x in norm[1:]] if nonconst_total else [0.0] * width)
    centroid = sum(k * norm[k] for k in range(width + 1))
    variance = sum(((k - centroid) ** 2) * norm[k] for k in range(width + 1))
    nz = norm[1:]
    max_degree = 1 + max(range(len(nz)), key=lambda i: nz[i]) if nz else 0
    entropy = -sum(x * math.log2(x) for x in norm if x > 0)

    return {
        "energies": energies,
        "norm": norm,
        "renorm": renorm,
        "dc_mass": norm[0],
        "nonconstant_mass": nonconst_total,
        "centroid": centroid,
        "variance": variance,
        "max_nonconstant_degree": max_degree,
        "max_nonconstant_mass": norm[max_degree] if max_degree else 0.0,
        "low_mass_1": sum(norm[1:2]),
        "low_mass_2": sum(norm[1:3]),
        "low_mass_3": sum(norm[1:4]),
        "low_mass_4": sum(norm[1:5]),
        "entropy": entropy,
    }


def tv(a, b, start=1):
    return 0.5 * sum(abs(x - y) for x, y in zip(a[start:], b[start:]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default="lab03_out")
    ap.add_argument("--widths", nargs="+", type=int, default=list(range(6, 17)))
    args = ap.parse_args()

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    spectrum_rows = []
    summary = []

    for w in args.widths:
        prime = prime_indicator(w)
        psp = spectrum(prime, w)

        families = [("prime", None, prime, psp)]

        for seed in SEEDS:
            families.append(("random_fixed", seed, fixed_count_random(prime, seed + 1000003 * w), None))
            families.append(("shuffled_prime", seed, shuffled(prime, seed + 2000003 * w), None))
            families.append(("wheel30_shuffle", seed, wheel_shuffle(prime, 30, seed + 3000003 * w), None))
            families.append(("wheel210_shuffle", seed, wheel_shuffle(prime, 210, seed + 4000003 * w), None))

        evaluated = []
        for family, seed, vals, sp in families:
            if sp is None:
                sp = spectrum(vals, w)
            evaluated.append((family, seed, sp))

            for degree in range(w + 1):
                spectrum_rows.append({
                    "width": w,
                    "family": family,
                    "seed": "" if seed is None else seed,
                    "degree": degree,
                    "energy_exact": sp["energies"][degree],
                    "energy_fraction": sp["norm"][degree],
                    "nonconstant_renorm_fraction": sp["renorm"][degree],
                })

        entry = {
            "width": w,
            "prime": {
                k: v for k, v in psp.items()
                if k not in ("energies", "norm", "renorm")
            },
            "baselines": {},
        }

        for baseline in ["random_fixed", "shuffled_prime", "wheel30_shuffle", "wheel210_shuffle"]:
            vals = []
            for family, seed, sp in evaluated:
                if family != baseline:
                    continue
                vals.append({
                    "seed": seed,
                    "tv_nonconstant_raw": tv(psp["norm"], sp["norm"], 1),
                    "tv_nonconstant_renorm": tv(psp["renorm"], sp["renorm"], 1),
                    "centroid_delta": psp["centroid"] - sp["centroid"],
                    "low_mass_2_delta": psp["low_mass_2"] - sp["low_mass_2"],
                    "low_mass_4_delta": psp["low_mass_4"] - sp["low_mass_4"],
                    "entropy_delta": psp["entropy"] - sp["entropy"],
                })
            entry["baselines"][baseline] = {
                "samples": vals,
                "tv_renorm_mean": statistics.mean(x["tv_nonconstant_renorm"] for x in vals),
                "tv_renorm_min": min(x["tv_nonconstant_renorm"] for x in vals),
                "tv_renorm_max": max(x["tv_nonconstant_renorm"] for x in vals),
                "centroid_delta_mean": statistics.mean(x["centroid_delta"] for x in vals),
                "low_mass_2_delta_mean": statistics.mean(x["low_mass_2_delta"] for x in vals),
                "low_mass_4_delta_mean": statistics.mean(x["low_mass_4_delta"] for x in vals),
                "entropy_delta_mean": statistics.mean(x["entropy_delta"] for x in vals),
            }

        summary.append(entry)
        print(f"done W={w}")

    with (out / "walsh_degree_spectrum.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(spectrum_rows[0].keys()))
        wr.writeheader()
        wr.writerows(spectrum_rows)

    (out / "walsh_degree_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    lines = [
        "# H20-EXT-LAB-03 · Exact Walsh degree spectrum",
        "",
        "Status: **COMPUTATION COMPLETE**",
        "",
        "| W | prime centroid | prime low-mass <=2 | TV wheel30 | TV wheel210 |",
        "|---:|---:|---:|---:|---:|",
    ]
    for e in summary:
        lines.append(
            f"| {e['width']} | {e['prime']['centroid']:.6f} | "
            f"{e['prime']['low_mass_2']:.8f} | "
            f"{e['baselines']['wheel30_shuffle']['tv_renorm_mean']:.6f} | "
            f"{e['baselines']['wheel210_shuffle']['tv_renorm_mean']:.6f} |"
        )

    lines += [
        "",
        "## Exact finite statement",
        "",
        f"Exact integer FWHT degree energies were computed for W={min(args.widths)}..{max(args.widths)} and all declared fixed-seed baselines.",
        "",
        "## Non-claim",
        "",
        "No asymptotic law, novelty claim, prime-distribution theorem, circuit lower bound, or RH implication is asserted by the generated data alone.",
    ]
    (out / "H20_EXT_LAB03_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
