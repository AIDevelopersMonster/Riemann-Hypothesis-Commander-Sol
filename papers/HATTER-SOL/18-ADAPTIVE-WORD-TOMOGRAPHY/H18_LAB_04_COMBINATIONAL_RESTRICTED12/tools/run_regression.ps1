$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H18 = Resolve-Path (Join-Path $Lab "..")
$Hatter = Resolve-Path (Join-Path $H18 "..")
$H17 = Join-Path $Hatter "17-NONABELIAN-TOMOGRAPHY-HARDWARE"
$Gen = Join-Path $Lab "generated_comb"
New-Item -ItemType Directory -Force $Gen | Out-Null

Write-Host "== Generate H17 closure-aware membership/classifier =="
py -3 (Join-Path $H17 "tools\generate_psl27_closure_classifiers.py") --out-dir $Gen
if ($LASTEXITCODE -ne 0) { throw "H17 classifier generation failed" }

Write-Host "== Generate H18-LAB-04 combinational RTL =="
py -3 (Join-Path $Lab "tools\generate_h18_r12_comb.py") --out-dir $Gen
if ($LASTEXITCODE -ne 0) { throw "H18 combinational generation failed" }

$ModelSimDir = "C:\altera\13.1\modelsim_ase\win32aloem"
$VlibExe = Join-Path $ModelSimDir "vlib.exe"
$VlogExe = Join-Path $ModelSimDir "vlog.exe"
$VsimExe = Join-Path $ModelSimDir "vsim.exe"

foreach ($exe in @($VlibExe,$VlogExe,$VsimExe)) {
  if (!(Test-Path $exe)) { throw "ModelSim executable not found: $exe" }
}

Push-Location $Gen
try {
  if (Test-Path ".\work") { Remove-Item ".\work" -Recurse -Force }

  & $VlibExe work
  if ($LASTEXITCODE -ne 0) { throw "vlib failed" }

  $vlogArgs = @(
    "-sv",
    "psl27_membership_only.sv",
    "psl27_member_class_only.sv",
    "h18_r12_comb_core.sv",
    "h18_r12_comb_controller.sv",
    "tb_h18_r12_comb_controller.sv"
  )
  & $VlogExe @vlogArgs
  if ($LASTEXITCODE -ne 0) { throw "vlog failed" }

  $vsimArgs = @(
    "-c",
    "work.tb_h18_r12_comb_controller",
    "+VECTORS=h18_r12_comb_vectors.txt",
    "-do",
    "run -all; quit -f"
  )
  & $VsimExe @vsimArgs | Tee-Object -FilePath "h18_r12_comb_modelsim.log"
  if ($LASTEXITCODE -ne 0) { throw "ModelSim regression failed" }

  $pass = Select-String -Path "h18_r12_comb_modelsim.log" -Pattern "PASS H18-LAB-04 comb:" -Quiet
  if (-not $pass) { throw "PASS marker not found" }

  Write-Host "PASS: H18-LAB-04 ModelSim exhaustive regression"
}
finally {
  Pop-Location
}
