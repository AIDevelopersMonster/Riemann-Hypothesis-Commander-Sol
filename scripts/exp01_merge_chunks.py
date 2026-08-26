#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chunks", nargs="+", type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    files = sorted(args.chunks)
    loaded = [np.load(path, allow_pickle=False) for path in files]
    try:
        loops = np.concatenate([z["loops"] for z in loaded])
        order = np.argsort(loops)
        sorted_loops = loops[order]
        if len(np.unique(sorted_loops)) != len(sorted_loops):
            raise SystemExit("duplicate loop indices across chunks")
        if len(sorted_loops) > 1 and not np.all(np.diff(sorted_loops) == 1):
            raise SystemExit("gap in loop indices across chunks")

        common = set(loaded[0].files)
        for z in loaded[1:]:
            common &= set(z.files)

        payload = {}
        first_len = len(loaded[0]["loops"])
        for key in sorted(common):
            if key == "metadata_json":
                continue
            arrays = [z[key] for z in loaded]
            if arrays[0].ndim >= 1 and arrays[0].shape[0] == first_len:
                payload[key] = np.concatenate(arrays, axis=0)[order]

        # Store portable chunk identifiers only. Absolute local paths are not
        # scientific provenance and should never leak into published manifests.
        metadata = {
            "chunks": [path.name for path in files],
            "n_loops": int(len(sorted_loops)),
            "start": int(sorted_loops[0]),
            "stop": int(sorted_loops[-1]),
        }
        payload["metadata_json"] = np.array(json.dumps(metadata, sort_keys=True))
        args.out.parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(args.out, **payload)
    finally:
        for z in loaded:
            z.close()


if __name__ == "__main__":
    main()
