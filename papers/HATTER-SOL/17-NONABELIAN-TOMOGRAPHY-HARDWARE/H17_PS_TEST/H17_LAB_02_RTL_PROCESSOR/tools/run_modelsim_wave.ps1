$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H17 = Resolve-Path (Join-Path $Lab "..\..")
$Generated = Join-Path $Lab "generated_modelsim"
$Build = Join-Path $Lab "build_modelsim"
New-Item -ItemType Directory -Force $Generated | Out-Null
New-Item -ItemType Directory -Force $Build | Out-Null

Write-Host "== Generate exact H17-LAB-02 RTL =="
py -3 (Join-Path $H17 "tools\generate_psl27_robust8_closure.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "closure generator failed" }
py -3 (Join-Path $H17 "tools\generate_psl27_romfree_repair.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "repair generator failed" }

$Roots = @(
  "C:\altera\13.1\modelsim_ase\win32aloem",
  "C:\altera\13.1\modelsim_ae\win32aloem",
  "C:\altera\13.1\modelsim_ase\win32",
  "C:\altera\13.1\modelsim_ae\win32"
)
$ModelSim = $null
foreach ($r in $Roots) { if (Test-Path (Join-Path $r "vsim.exe")) { $ModelSim = $r; break } }
if (-not $ModelSim) { throw "ModelSim-Altera not found under C:\altera\13.1" }
$Vlib = Join-Path $ModelSim "vlib.exe"
$Vlog = Join-Path $ModelSim "vlog.exe"
$Vsim = Join-Path $ModelSim "vsim.exe"
Write-Host ("ModelSim: " + $Vsim)

Push-Location $Build
try {
  if (Test-Path ".\work") { Remove-Item -Recurse -Force ".\work" }
  & $Vlib work
  if ($LASTEXITCODE -ne 0) { throw "vlib failed" }

  & $Vlog -sv `
    (Join-Path $Generated "psl27_membership_only.sv") `
    (Join-Path $Generated "psl27_member_class_only.sv") `
    (Join-Path $Generated "psl27_robust8_engine.sv") `
    (Join-Path $Generated "psl27_robust8_repair.sv") `
    (Join-Path $Lab "rtl\h17_lab02_core.sv") `
    (Join-Path $Lab "rtl\h17_lab02_controller.sv") `
    (Join-Path $Lab "tb\tb_h17_lab02_waveform.sv")
  if ($LASTEXITCODE -ne 0) { throw "vlog failed" }

  Copy-Item (Join-Path $Lab "tb\h17_lab02_wave.do") ".\h17_lab02_wave.do" -Force
  & $Vsim -c -wlf h17_lab02_wave.wlf work.tb_h17_lab02_waveform -do "do h17_lab02_wave.do; quit -f"
  if ($LASTEXITCODE -ne 0) { throw "ModelSim simulation failed" }

  Write-Host "PASS: WLF created"
  Write-Host (Join-Path $Build "h17_lab02_wave.wlf")
  Write-Host "Open with:"
  Write-Host ('& "' + $Vsim + '" -view "' + (Join-Path $Build "h17_lab02_wave.wlf") + '"')
} finally { Pop-Location }
