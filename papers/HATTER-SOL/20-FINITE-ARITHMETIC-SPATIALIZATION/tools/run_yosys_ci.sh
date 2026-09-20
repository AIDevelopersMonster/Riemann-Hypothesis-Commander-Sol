#!/usr/bin/env bash
set -euo pipefail

LAB="$(cd "$(dirname "$0")/.." && pwd)"
GEN="$LAB/generated"
OUT="$LAB/yosys_ci_out"
mkdir -p "$OUT"

python3 "$LAB/tools/verify_python_models.py" --widths 4 5 6 7 8 9 10
python3 "$LAB/tools/generate_prime_spatial_lab.py" --out-dir "$GEN" --widths 4 5 6
python3 "$LAB/tools/generate_equiv_miter.py" --out-dir "$GEN" --widths 4 5 6

echo "width,mode,stage,cells,wires,wire_bits" > "$OUT/PRIME_SPATIAL_YOSYS_SUMMARY.csv"

extract_stat () {
  local width="$1"
  local mode="$2"
  local stage="$3"
  local file="$4"
  local cells wires bits
  cells="$(grep -E 'Number of cells:' "$file" | tail -1 | awk '{print $4}')"
  wires="$(grep -E 'Number of wires:' "$file" | tail -1 | awk '{print $4}')"
  bits="$(grep -E 'Number of wire bits:' "$file" | tail -1 | awk '{print $5}')"
  echo "$width,$mode,$stage,$cells,$wires,$bits" >> "$OUT/PRIME_SPATIAL_YOSYS_SUMMARY.csv"
}

for w in 4 5 6; do
  echo "=== FORMAL EQUIVALENCE W=$w ==="
  formal_log="$OUT/w"$w"_formal.log"
  miter="$GEN/w"$w"/nextprime_equiv_miter.sv"
  yosys -ql "$formal_log" -p "
    read_verilog -sv $miter;
    prep -top equiv_top -flatten;
    memory_map;
    opt;
    sat -verify -prove bad 0 -show x
  "

  for mode in direct linear balanced; do
    src="$GEN/w"$w"/nextprime_"$mode".sv"
    od="$OUT/w"$w"_"$mode
    mkdir -p "$od"

    yosys -ql "$od/run.log" -p "
      read_verilog -sv $src;
      hierarchy -top nextprime_top;
      proc; flatten; opt;
      tee -o $od/post_proc_raw.stat stat;
      memory_map; opt;
      tee -o $od/post_boolnorm.stat stat;
      techmap; opt;
      tee -o $od/post_techmap.stat stat;
      abc -fast; opt;
      tee -o $od/post_abc.stat stat;
      write_json $od/post_abc.json
    "

    extract_stat "$w" "$mode" "proc_raw" "$od/post_proc_raw.stat"
    extract_stat "$w" "$mode" "boolnorm" "$od/post_boolnorm.stat"
    extract_stat "$w" "$mode" "techmap" "$od/post_techmap.stat"
    extract_stat "$w" "$mode" "abc" "$od/post_abc.stat"
  done
done

cat "$OUT/PRIME_SPATIAL_YOSYS_SUMMARY.csv"
