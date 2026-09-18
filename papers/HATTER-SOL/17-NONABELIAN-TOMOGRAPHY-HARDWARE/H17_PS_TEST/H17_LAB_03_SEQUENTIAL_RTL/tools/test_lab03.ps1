param(
    [ValidateSet("quick","full")]
    [string]$Set = "quick"
)

$ErrorActionPreference = "Stop"

$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H17 = Resolve-Path (Join-Path $Lab "..\..")
$Generated = Join-Path $Lab "generated"
$Build = Join-Path $Lab "build"

New-Item -ItemType Directory -Force $Generated | Out-Null
New-Item -ItemType Directory -Force $Build | Out-Null

Write-Host "== H17-LAB-03: generate closure classifiers =="
py -3 (Join-Path $H17 "tools\generate_psl27_closure_classifiers.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "closure classifier generator failed" }

Write-Host "== H17-LAB-03: generate ROM-free repair =="
py -3 (Join-Path $H17 "tools\generate_psl27_romfree_repair.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "ROM-free generator failed" }

$Sim = Join-Path $Build "h17_lab03_sim"
$Sources = @(
    "-g2012",
    "-s", "tb_h17_lab03_vectors",
    "-o", $Sim,
    (Join-Path $Generated "psl27_membership_only.sv"),
    (Join-Path $Generated "psl27_member_class_only.sv"),
    (Join-Path $Generated "psl27_robust8_repair.sv"),
    (Join-Path $Lab "rtl\h17_lab03_sequential_core.sv"),
    (Join-Path $Lab "tb\tb_h17_lab03_vectors.sv")
)

Write-Host "== H17-LAB-03: compile =="
& iverilog @Sources
if ($LASTEXITCODE -ne 0) { throw "iverilog compile failed" }

$VectorArg = "../H17_LAB_COMPLETE_clean/vectors/$Set.txt"

Write-Host "== H17-LAB-03: run $Set vectors =="
Push-Location $Lab
try {
    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    & vvp $Sim "+VECTORS=$VectorArg"
    $rc = $LASTEXITCODE
    $sw.Stop()
    if ($rc -ne 0) { throw "LAB-03 simulation failed" }
}
finally {
    Pop-Location
}
Write-Host ("LAB-03 {0} ELAPSED: {1:N3} seconds" -f $Set,$sw.Elapsed.TotalSeconds)
