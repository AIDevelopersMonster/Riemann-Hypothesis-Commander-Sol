#!/usr/bin/env python3
"""Fetch a reproducible Riemann-zeta zero table from LMFDB.

LMFDB's public zeta-zero list endpoint returns lines
    N imaginary_part
and supports up to 100000 rows in one request.
"""
from __future__ import annotations
import argparse, csv, hashlib, urllib.parse, urllib.request
from pathlib import Path


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--limit", type=int, default=10001)
    ap.add_argument("--out", type=Path, default=Path("data/zeros/lmfdb_zeta_zeros_1_10001.csv"))
    args = ap.parse_args()
    if args.limit < 2 or args.limit > 100000:
        raise SystemExit("LMFDB list endpoint supports 2..100000 rows for this script")

    query = urllib.parse.urlencode({"N": args.start, "limit": args.limit})
    url = "https://www.lmfdb.org/zeros/zeta/list?" + query
    req = urllib.request.Request(url, headers={"User-Agent": "RH-SOL reproducibility script"})
    with urllib.request.urlopen(req, timeout=120) as response:
        raw = response.read()

    rows = []
    for line in raw.decode("utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        rows.append((int(parts[0]), parts[1]))

    if len(rows) != args.limit:
        raise SystemExit(f"expected {args.limit} rows, received {len(rows)}")
    if rows[0][0] != args.start:
        raise SystemExit("unexpected first zero index")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "gamma"])
        writer.writerows(rows)

    print(f"source_url={url}")
    print(f"raw_sha256={sha256_bytes(raw)}")
    print(f"rows={len(rows)}")
    print(f"csv={args.out}")


if __name__ == "__main__":
    main()
