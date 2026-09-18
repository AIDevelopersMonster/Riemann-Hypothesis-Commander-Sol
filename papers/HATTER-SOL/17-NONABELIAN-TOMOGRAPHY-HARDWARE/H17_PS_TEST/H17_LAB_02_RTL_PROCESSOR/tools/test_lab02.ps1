param(
    [ValidateSet("quick","full")]
    [string]$Set = "quick"
)

$ErrorActionPreference = "Stop"

$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H17 = Resolve-Path (Join-Path $Lab "..\..")
$Ref = Resolve-Path (Join-Path $Lab "..\H17_LAB_COMPLETE_clean")

$Generated = Join-Path $Lab "generated"
$Build = Join-Path $Lab "build"

New-Item -ItemType Directory -Force $Generated | Out-Null
New-Item -ItemType Directory -Force $Build | Out-Null

Write-Host "== H17-LAB-02: generate closure-aware frontend =="
py -3 (Join-Path $H17 "tools\generate_psl27_robust8_closure.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "closure generator failed" }

Write-Host "== H17-LAB-02: generate ROM-free repair =="
py -3 (Join-Path $H17 "tools\generate_psl27_romfree_repair.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "ROM-free generator failed" }

$VectorFile = Resolve-Path (Join-Path $Ref "vectors\$Set.txt")
$Sim = Join-Path $Build "h17_lab02_sim"

Write-Host "== H17-LAB-02: compile pure SystemVerilog =="

$Sources = @(
    "-g2012",
    "-s", "tb_h17_lab02_vectors",
    "-o", $Sim,
    (Join-Path $Generated "psl27_membership_only.sv"),
    (Join-Path $Generated "psl27_member_class_only.sv"),
    (Join-Path $Generated "psl27_robust8_engine.sv"),
    (Join-Path $Generated "psl27_robust8_repair.sv"),
    (Join-Path $Lab "rtl\h17_lab02_core.sv"),
    (Join-Path $Lab "tb\tb_h17_lab02_vectors.sv")
)

& iverilog @Sources
if ($LASTEXITCODE -ne 0) { throw "iverilog compile failed" }

Write-Host "== H17-LAB-02: run $Set vectors =="
& vvp $Sim "+VECTORS=$($VectorFile.Path)"
if ($LASTEXITCODE -ne 0) { throw "H17-LAB-02 simulation failed" }
