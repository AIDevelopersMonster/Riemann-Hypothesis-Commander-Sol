#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, getcontext
from pathlib import Path
from urllib.request import Request, urlopen

SOURCE_URL = (
    "https://www.lmfdb.org/zeros/zeta/list?"
    "N=40001&limit=20001&format=plain&download=yes"
)
EXPECTED_START = 40001
EXPECTED_STOP = 60001
EXPECTED_COUNT = EXPECTED_STOP - EXPECTED_START + 1
OVERLAP_TOL = Decimal("1e-27")

getcontext().prec = 80


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_lmfdb_plain(raw: bytes) -> list[tuple[int, str, Decimal]]:
    text = raw.decode("utf-8")
    rows: list[tuple[int, str, Decimal]] = []
    for line_no, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2:
            raise SystemExit(
                f"Malformed LMFDB row at line {line_no}: expected 2 fields, got {len(parts)}"
            )
        try:
            idx = int(parts[0])
            gamma = Decimal(parts[1])
        except (ValueError, InvalidOperation) as exc:
            raise SystemExit(f"Malformed LMFDB row at line {line_no}: {line!r}") from exc
        if not gamma.is_finite():
            raise SystemExit(f"Non-finite ordinate at index {idx}")
        rows.append((idx, parts[1], gamma))
    return rows


def load_overlap(path: Path, index: int) -> Decimal:
    if not path.exists():
        raise SystemExit(f"Missing overlap table: {path}")
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None or not {"n", "gamma"}.issubset(reader.fieldnames):
            raise SystemExit(f"Overlap table has unexpected schema: {reader.fieldnames}")
        for row in reader:
            if int(row["n"]) == index:
                try:
                    return Decimal(row["gamma"])
                except InvalidOperation as exc:
                    raise SystemExit(f"Invalid overlap gamma at index {index}") from exc
    raise SystemExit(f"Overlap table does not contain index {index}")


def validate(rows: list[tuple[int, str, Decimal]], overlap_gamma: Decimal) -> Decimal:
    if len(rows) != EXPECTED_COUNT:
        raise SystemExit(f"Expected {EXPECTED_COUNT} rows, got {len(rows)}")
    indices = [r[0] for r in rows]
    if indices[0] != EXPECTED_START:
        raise SystemExit(f"Expected first index {EXPECTED_START}, got {indices[0]}")
    if indices[-1] != EXPECTED_STOP:
        raise SystemExit(f"Expected last index {EXPECTED_STOP}, got {indices[-1]}")
    for prev, cur in zip(indices, indices[1:]):
        if cur != prev + 1:
            raise SystemExit(f"Non-contiguous indices: {prev} -> {cur}")

    gammas = [r[2] for r in rows]
    if gammas[0] <= 0:
        raise SystemExit("First ordinate is not positive")
    for i, (prev, cur) in enumerate(zip(gammas, gammas[1:]), start=EXPECTED_START + 1):
        if cur <= prev:
            raise SystemExit(f"Ordinates not strictly increasing at index {i}")

    overlap_delta = abs(gammas[0] - overlap_gamma)
    if overlap_delta > OVERLAP_TOL:
        raise SystemExit(
            "LMFDB overlap mismatch at index 40001: "
            f"delta={overlap_delta} > {OVERLAP_TOL}"
        )
    return overlap_delta


def normalized_csv_bytes(rows: list[tuple[int, str, Decimal]]) -> bytes:
    lines = ["n,gamma"]
    lines.extend(f"{idx},{gamma_text}" for idx, gamma_text, _ in rows)
    return ("\n".join(lines) + "\n").encode("utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--overlap", type=Path, required=True)
    ap.add_argument("--timeout", type=float, default=120.0)
    args = ap.parse_args()

    print("=== RH-SOL-05 POISSON-05 / LMFDB ZERO ACQUISITION ===", flush=True)
    print("Identity     : POISSON-05_LMFDB_ZEROS_40001_60001", flush=True)
    print("Range        : zero indices 40001..60001", flush=True)
    print("Primary src  : official LMFDB zeta-zero plain route", flush=True)
    print("Guard        : exact count + continuity + monotonicity + overlap", flush=True)

    req = Request(
        SOURCE_URL,
        headers={
            "User-Agent": "Riemann-Hypothesis-Commander-Sol/POISSON-05 data acquisition",
            "Accept": "text/plain,*/*;q=0.1",
        },
    )
    try:
        with urlopen(req, timeout=args.timeout) as response:
            raw = response.read()
            content_type = response.headers.get("Content-Type", "")
    except Exception as exc:
        raise SystemExit(f"LMFDB acquisition failed: {exc}") from exc

    if not raw:
        raise SystemExit("LMFDB acquisition returned an empty response")

    rows = parse_lmfdb_plain(raw)
    overlap_gamma = load_overlap(args.overlap, EXPECTED_START)
    overlap_delta = validate(rows, overlap_gamma)
    csv_bytes = normalized_csv_bytes(rows)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(csv_bytes)

    manifest = {
        "identity": "POISSON-05_LMFDB_ZEROS_40001_60001",
        "source_url": SOURCE_URL,
        "acquired_utc": datetime.now(timezone.utc).isoformat(),
        "http_content_type": content_type,
        "expected_start": EXPECTED_START,
        "expected_stop": EXPECTED_STOP,
        "row_count": len(rows),
        "first_index": rows[0][0],
        "last_index": rows[-1][0],
        "first_gamma": rows[0][1],
        "last_gamma": rows[-1][1],
        "overlap_index": EXPECTED_START,
        "overlap_reference": str(args.overlap).replace("\\", "/"),
        "overlap_abs_delta": str(overlap_delta),
        "overlap_tolerance": str(OVERLAP_TOL),
        "raw_sha256": sha256_bytes(raw),
        "normalized_csv_sha256": sha256_bytes(csv_bytes),
    }
    args.manifest.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    print(f"Rows         : {len(rows)}", flush=True)
    print(f"First/last   : {rows[0][0]} / {rows[-1][0]}", flush=True)
    print(f"Overlap delta: {overlap_delta}", flush=True)
    print(f"Raw SHA256   : {manifest['raw_sha256']}", flush=True)
    print(f"CSV SHA256   : {manifest['normalized_csv_sha256']}", flush=True)
    print(f"WROTE {args.out}", flush=True)
    print(f"WROTE {args.manifest}", flush=True)
    print("=== POISSON-05_LMFDB_ZEROS_40001_60001 COMPLETE ===", flush=True)


if __name__ == "__main__":
    main()
