$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H18 = Resolve-Path (Join-Path $Lab "..")
$Hatter = Resolve-Path (Join-Path $H18 "..")
$H17 = Join-Path $Hatter "17-NONABELIAN-TOMOGRAPHY-HARDWARE"
$Gen = Join-Path $Lab "generated_comb"
New-Item -ItemType Directory -Force $Gen | Out-Null

Write-Host "== Generate H18-LAB-04 RTL and waveform scenario =="

py -3 (Join-Path $H17 "tools\generate_psl27_closure_classifiers.py") --out-dir $Gen
if ($LASTEXITCODE -ne 0) { throw "H17 classifier generation failed" }

py -3 (Join-Path $Lab "tools\generate_h18_r12_comb.py") --out-dir $Gen
if ($LASTEXITCODE -ne 0) { throw "H18 combinational generation failed" }

py -3 (Join-Path $Lab "tools\generate_waveform_assets.py")
if ($LASTEXITCODE -ne 0) { throw "waveform asset generation failed" }

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
    "tb_h18_r12_comb_wave.sv"
  )
  & $VlogExe @vlogArgs
  if ($LASTEXITCODE -ne 0) { throw "vlog failed" }

  Write-Host ""
  Write-Host "Opening ModelSim waveform..."
  Write-Host "Scenario:"
  Get-Content ".\H18_R12_WAVE_SCENARIO.md"
  Write-Host ""

  $vsimArgs = @(
    "-gui",
    "-voptargs=+acc",
    "work.tb_h18_r12_comb_wave",
    "-do",
    "do wave_h18_r12_comb.do"
  )
  & $VsimExe @vsimArgs
}
finally {
  Pop-Location
}
