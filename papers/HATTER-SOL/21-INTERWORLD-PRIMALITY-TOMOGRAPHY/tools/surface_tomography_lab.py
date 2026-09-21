#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import itertools
import json
from collections import Counter
from pathlib import Path


def signature(a, p: int, g: int, observer: str):
    coords = a[:g]
    local = tuple((2 * x) % p for x in coords)
    global_h = sum(local) % p

    if observer == "global_flat":
        return (int(global_h != 0),)
    if observer == "global_oriented":
        return (global_h,)
    if observer == "handle_flat":
        return tuple(int(x != 0) for x in local)
    if observer == "handle_oriented":
        return local
    raise ValueError(observer)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, default=7)
    ap.add_argument("--rank", type=int, default=3)
    ap.add_argument("--out-dir", default="lab02_out")
    args = ap.parse_args()

    p = args.p
    r = args.rank
    if p % 2 == 0:
        raise SystemExit("p must be odd")

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    states = list(itertools.product(range(p), repeat=r))
    observers = [
        "global_flat",
        "global_oriented",
        "handle_flat",
        "handle_oriented",
    ]

    rows = []
    detail = {}

    for g in range(r + 1):
        detail[str(g)] = {}
        for obs in observers:
            fibers = Counter(signature(a, p, g, obs) for a in states)
            sizes = sorted(fibers.values())
            row = {
                "p": p,
                "rank": r,
                "genus": g,
                "observer": obs,
                "distinct_signatures": len(fibers),
                "min_fiber": min(sizes),
                "max_fiber": max(sizes),
            }
            rows.append(row)
            detail[str(g)][obs] = {
                "distinct_signatures": len(fibers),
                "fiber_histogram": dict(sorted(Counter(sizes).items())),
            }

    for g in range(r + 1):
        def get(obs):
            return next(
                x for x in rows
                if x["genus"] == g and x["observer"] == obs
            )

        assert get("handle_oriented")["distinct_signatures"] == p ** g
        assert get("handle_oriented")["max_fiber"] == p ** (r - g)
        assert get("handle_flat")["distinct_signatures"] == 2 ** g
        assert get("global_oriented")["distinct_signatures"] == (1 if g == 0 else p)
        assert get("global_flat")["distinct_signatures"] == (1 if g == 0 else 2)

    payload = {
        "p": p,
        "rank": r,
        "states": len(states),
        "rows": rows,
        "detail": detail,
    }
    (out / "surface_tomography.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )

    with (out / "surface_tomography.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        wr.writeheader()
        wr.writerows(rows)

    md = [
        "# H21-LAB-02 · Multiworld surface tomography",
        "",
        f"Algebraic laboratory: p={p}, rank={r}, states={len(states)}.",
        "",
        "| genus | global flat | global oriented | handle flat | handle oriented | max oriented fiber |",
        "|---:|---:|---:|---:|---:|---:|",
    ]

    for g in range(r + 1):
        def count(obs):
            return next(
                x for x in rows
                if x["genus"] == g and x["observer"] == obs
            )
        md.append(
            f"| {g} | {count('global_flat')['distinct_signatures']} | "
            f"{count('global_oriented')['distinct_signatures']} | "
            f"{count('handle_flat')['distinct_signatures']} | "
            f"{count('handle_oriented')['distinct_signatures']} | "
            f"{count('handle_oriented')['max_fiber']} |"
        )

    md += [
        "",
        "## Exact observation",
        "",
        "Handle-resolved oriented tomography gains one independent F_p coordinate per independent handle.",
        "",
        f"Signature counts for genus 0 -> 1 -> 2 -> 3 are 1 -> {p} -> {p**2} -> {p**3}.",
        "",
        f"The global oriented holonomy is capped at {p} signatures for every positive genus.",
        "",
        "## Non-claim",
        "",
        "This is an exact finite linear-algebra/holonomy laboratory, not evidence that geometric curvature alone detects primality.",
    ]
    (out / "H21_LAB02_REPORT.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print("\n".join(md))
    print("PASS: all exact surface-tomography counts verified")


if __name__ == "__main__":
    main()
