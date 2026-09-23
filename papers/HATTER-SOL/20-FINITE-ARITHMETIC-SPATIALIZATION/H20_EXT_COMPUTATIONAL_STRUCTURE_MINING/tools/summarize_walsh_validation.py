#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def span(samples, key):
    vals=[x[key] for x in samples]
    return min(vals), max(vals), sum(vals)/len(vals)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("summary")
    args=ap.parse_args()
    data=json.loads(Path(args.summary).read_text())

    print("W,baseline,tv_mean,tv_min,tv_max,centroid_delta_mean,centroid_delta_min,centroid_delta_max,low2_delta_mean,low2_min,low2_max,low4_delta_mean,low4_min,low4_max,entropy_delta_mean,entropy_min,entropy_max")
    for e in data:
        w=e["width"]
        for baseline in ["wheel30_shuffle","wheel210_shuffle"]:
            b=e["baselines"][baseline]
            s=b["samples"]
            c=span(s,"centroid_delta")
            l2=span(s,"low_mass_2_delta")
            l4=span(s,"low_mass_4_delta")
            h=span(s,"entropy_delta")
            print(
                f"{w},{baseline},"
                f"{b['tv_renorm_mean']:.9f},{b['tv_renorm_min']:.9f},{b['tv_renorm_max']:.9f},"
                f"{c[2]:.9f},{c[0]:.9f},{c[1]:.9f},"
                f"{l2[2]:.9f},{l2[0]:.9f},{l2[1]:.9f},"
                f"{l4[2]:.9f},{l4[0]:.9f},{l4[1]:.9f},"
                f"{h[2]:.9f},{h[0]:.9f},{h[1]:.9f}"
            )

if __name__=="__main__":
    main()
