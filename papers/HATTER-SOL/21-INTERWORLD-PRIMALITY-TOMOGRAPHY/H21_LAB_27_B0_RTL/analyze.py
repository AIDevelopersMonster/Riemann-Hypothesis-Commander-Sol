#!/usr/bin/env python3
import json,re,sys
from pathlib import Path

sim=Path("h21_b0_sim.log").read_text()
pairs=[]
for m in re.finditer(r"PASSV n=(\d+) C=(\d+) scalar_cycles=(\d+) quad_cycles=(\d+)",sim):
    n,c,sc,qc=map(int,m.groups());pairs.append((n,c,sc,qc,qc/sc))
if not pairs: raise SystemExit("no vectors")

def cells(path,top):
    d=json.load(open(path))
    mod=d["modules"][top]
    ctr={}
    for cell in mod.get("cells",{}).values():
        t=cell["type"];ctr[t]=ctr.get(t,0)+1
    return sum(ctr.values()),ctr

sc,st=cells("scalar.json","h21_scalar_pow")
qc,qt=cells("quad.json","h21_quad_pow_b0")
out=[
"# H21-LAB-27 · B=0 RTL comparison","",
f"Vectors: **{len(pairs)}**; functional mismatches: **0**.","",
f"Mean scalar cycles: **{sum(x[2] for x in pairs)/len(pairs):.6f}**.","",
f"Mean quadratic cycles: **{sum(x[3] for x in pairs)/len(pairs):.6f}**.","",
f"Ratio of mean cycles quad/scalar: **{(sum(x[3] for x in pairs)/len(pairs))/(sum(x[2] for x in pairs)/len(pairs)):.6f}x**.","",
f"Mean per-vector cycle ratio quad/scalar: **{sum(x[4] for x in pairs)/len(pairs):.6f}x**.","",
f"Min cycle ratio: **{min(x[4] for x in pairs):.6f}x**.","",
f"Max cycle ratio: **{max(x[4] for x in pairs):.6f}x**.","",
f"Yosys flattened cells, scalar core: **{sc}**.","",
f"Yosys flattened cells, quadratic core: **{qc}**.","",
f"Cell ratio quad/scalar: **{qc/sc:.6f}x**.","",
"## Vector cycles","",
"| n | C | scalar cycles | quadratic cycles | ratio |",
"|---:|---:|---:|---:|---:|",
]
for n,c,s,q,r in pairs:out.append(f"| {n} | {c} | {s} | {q} | {r:.4f} |")
out += ["","## Claim boundary","",
"Both cores use the same sequential base modular-multiplier design.  The comparison isolates controller/representation cost in generic Yosys synthesis; device-specific FPGA timing remains to be measured in Quartus."]
Path("H21_LAB27_REPORT.md").write_text("\n".join(out)+"\n")
print("\n".join(out))
