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

py -3 (Join-Path $H17 "tools\generate_psl27_robust8_closure.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "closure generator failed" }

py -3 (Join-Path $H17 "tools\generate_psl27_romfree_repair.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "ROM-free generator failed" }

$VectorFile = Resolve-Path (Join-Path $Ref "vectors\$Set.txt")
$Sim = Join-Path $Build "h17_lab02_controller_sim"

$Sources = @(
    "-g2012",
    "-s", "tb_h17_lab02_controller",
    "-o", $Sim,
    (Join-Path $Generated "psl27_membership_only.sv"),
    (Join-Path $Generated "psl27_member_class_only.sv"),
    (Join-Path $Generated "psl27_robust8_engine.sv"),
    (Join-Path $Generated "psl27_robust8_repair.sv"),
    (Join-Path $Lab "rtl\h17_lab02_core.sv"),
    (Join-Path $Lab "rtl\h17_lab02_controller.sv"),
    (Join-Path $Lab "tb\tb_h17_lab02_controller.sv")
)

& iverilog @Sources
if ($LASTEXITCODE -ne 0) { throw "iverilog compile failed" }

& vvp $Sim "+VECTORS=$($VectorFile.Path)"
if ($LASTEXITCODE -ne 0) { throw "controller simulation failed" }
