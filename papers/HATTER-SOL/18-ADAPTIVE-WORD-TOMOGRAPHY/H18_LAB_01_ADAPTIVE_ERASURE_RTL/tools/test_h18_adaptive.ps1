$ErrorActionPreference = "Stop"

$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H18 = Resolve-Path (Join-Path $Lab "..")
$H17 = Resolve-Path (Join-Path $H18 "..\17-NONABELIAN-TOMOGRAPHY-HARDWARE")
$Generated = Join-Path $Lab "generated"
$Build = Join-Path $Lab "build"

New-Item -ItemType Directory -Force $Generated | Out-Null
New-Item -ItemType Directory -Force $Build | Out-Null

Write-Host "== H18-LAB-01: generate exact adaptive controller =="
py -3 (Join-Path $Lab "tools\generate_h18_adaptive_controller.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "adaptive controller generator failed" }

Write-Host "== H18-LAB-01: generate H17 closure classifiers =="
py -3 (Join-Path $H17 "tools\generate_psl27_closure_classifiers.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "closure classifier generator failed" }

$Sim = Join-Path $Build "h18_adaptive_sim"

$Sources = @(
    "-g2012",
    "-s", "tb_h18_adaptive_vectors",
    "-o", $Sim,
    (Join-Path $Generated "psl27_membership_only.sv"),
    (Join-Path $Generated "psl27_member_class_only.sv"),
    (Join-Path $Generated "h18_adaptive_word_rom.sv"),
    (Join-Path $Generated "h18_adaptive_controller_rom.sv"),
    (Join-Path $Lab "rtl\h18_adaptive_sequential_core.sv"),
    (Join-Path $Lab "tb\tb_h18_adaptive_vectors.sv")
)

Write-Host "== H18-LAB-01: compile =="
& iverilog @Sources
if ($LASTEXITCODE -ne 0) { throw "iverilog compile failed" }

Write-Host "== H18-LAB-01: run 197 x 6 frozen vectors =="
Push-Location $Lab
try {
    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    & vvp $Sim "+VECTORS=generated/h18_adaptive_vectors.txt"
    $rc = $LASTEXITCODE
    $sw.Stop()
    if ($rc -ne 0) { throw "H18 adaptive simulation failed" }
}
finally {
    Pop-Location
}
Write-Host ("H18-LAB-01 ELAPSED: {0:N3} seconds" -f $sw.Elapsed.TotalSeconds)
