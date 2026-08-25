#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import io
import json
import urllib.request
import zipfile
from pathlib import Path

RECORD_ID = "22060296"
TARGET = "zeta_gaussian_phase_10000.csv"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def extract_from_zip_bytes(blob: bytes, target_name: str) -> tuple[str, bytes] | None:
    with zipfile.ZipFile(io.BytesIO(blob)) as zf:
        for name in zf.namelist():
            if Path(name).name == target_name:
                return name, zf.read(name)
        for name in zf.namelist():
            if name.lower().endswith(".zip"):
                nested = zf.read(name)
                found = extract_from_zip_bytes(nested, target_name)
                if found is not None:
                    inner_name, data = found
                    return f"{name}!{inner_name}", data
    return None


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "RH-SOL/1.0"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "RH-SOL/1.0"})
    with urllib.request.urlopen(req) as r:
        return r.read()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--record", default=RECORD_ID)
    ap.add_argument("--out", type=Path, default=Path("data/rh-sol-01/zeta_gaussian_phase_10000.csv"))
    args = ap.parse_args()

    meta_url = f"https://zenodo.org/api/records/{args.record}"
    meta = fetch_json(meta_url)
    files = meta.get("files", [])
    if not files:
        raise SystemExit("Zenodo record exposes no files")

    attempts: list[str] = []
    for item in files:
        key = str(item.get("key", ""))
        links = item.get("links", {}) or {}
        url = links.get("self") or links.get("content")
        if not url:
            continue
        attempts.append(key)
        blob = fetch_bytes(url)
        if Path(key).name == TARGET:
            found_name, data = key, blob
        elif key.lower().endswith(".zip"):
            found = extract_from_zip_bytes(blob, TARGET)
            if found is None:
                continue
            found_name, data = found
        else:
            continue

        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_bytes(data)
        manifest = {
            "zenodo_record": str(args.record),
            "record_doi": meta.get("doi"),
            "source_file": key,
            "member": found_name,
            "output": args.out.as_posix(),
            "size_bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        manifest_path = args.out.with_suffix(".manifest.json")
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        print(json.dumps(manifest, indent=2))
        return

    raise SystemExit(f"{TARGET} not found; inspected Zenodo files: {attempts}")


if __name__ == "__main__":
    main()
