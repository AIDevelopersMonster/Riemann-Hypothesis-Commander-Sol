$ErrorActionPreference = "Stop"

$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H17 = Resolve-Path (Join-Path $Lab "..\..")
$Generated = Join-Path $Lab "generated"
$Build = Join-Path $Lab "build"

New-Item -ItemType Directory -Force $Generated | Out-Null
New-Item -ItemType Directory -Force $Build | Out-Null

Write-Host "== H17-LAB-03 smoke: generate closure classifiers =="
py -3 (Join-Path $H17 "tools\generate_psl27_closure_classifiers.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "closure classifier generator failed" }

Write-Host "== H17-LAB-03 smoke: generate ROM-free repair =="
py -3 (Join-Path $H17 "tools\generate_psl27_romfree_repair.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "ROM-free generator failed" }

$Smoke = Join-Path $Build "smoke1.txt"
"5e3b88 7ecc11 1 2 00 8d256a ed256a 8d256a" |
    Set-Content $Smoke -Encoding ascii

$Sim = Join-Path $Build "h17_lab03_smoke_sim"

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

Write-Host "== H17-LAB-03 smoke: compile =="
& iverilog @Sources
if ($LASTEXITCODE -ne 0) { throw "iverilog compile failed" }

Write-Host "== H17-LAB-03 smoke: run exactly one vector =="
Push-Location $Lab
try {
    $elapsed = Measure-Command {
        & vvp $Sim "+VECTORS=build/smoke1.txt"
        if ($LASTEXITCODE -ne 0) { throw "smoke simulation failed" }
    }
}
finally {
    Pop-Location
}
Write-Host ("SMOKE ELAPSED: {0:N3} seconds" -f $elapsed.TotalSeconds)
