#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("summary")
    a=ap.parse_args()
    d=json.loads(Path(a.summary).read_text())
    print("W,low4_mean,low4_min,low4_max,criterion_all_negative")
    ok=True
    for e in d:
        w=e["width"]
        passed=e["low4_delta_max"] < 0
        if w in (17,18) and not passed:
            ok=False
        print(f"{w},{e['low4_delta_mean']:.12f},{e['low4_delta_min']:.12f},{e['low4_delta_max']:.12f},{passed}")
    print("VALIDATION_PASS="+str(ok))
    if not ok:
        raise SystemExit(2)

if __name__=="__main__":
    main()
