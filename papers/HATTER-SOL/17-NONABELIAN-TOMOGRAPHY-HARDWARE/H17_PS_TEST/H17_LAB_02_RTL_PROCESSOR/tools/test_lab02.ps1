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

# IMPORTANT:
# tb_h17_lab02_vectors.sv stores +VECTORS in a 1024-bit packed string
# (128 bytes). The absolute Windows repository path is longer than that,
# so passing the resolved absolute path truncates its LEFT side.
#
# Run vvp from $Lab and pass a short relative path instead.
$VectorArg = "../H17_LAB_COMPLETE_clean/vectors/$Set.txt"
if (-not (Test-Path (Join-Path $Ref "vectors\$Set.txt"))) {
    throw "vector file missing: $(Join-Path $Ref "vectors\$Set.txt")"
}

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
Push-Location $Lab
try {
    & vvp $Sim "+VECTORS=$VectorArg"
    if ($LASTEXITCODE -ne 0) { throw "H17-LAB-02 simulation failed" }
}
finally {
    Pop-Location
}
