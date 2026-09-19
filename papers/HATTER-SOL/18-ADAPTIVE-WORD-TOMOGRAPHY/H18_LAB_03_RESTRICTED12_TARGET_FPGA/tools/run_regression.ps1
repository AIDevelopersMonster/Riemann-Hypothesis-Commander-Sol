$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H18 = Resolve-Path (Join-Path $Lab "..")
$Hatter = Resolve-Path (Join-Path $H18 "..")
$H17 = Join-Path $Hatter "17-NONABELIAN-TOMOGRAPHY-HARDWARE"
$Gen = Join-Path $Lab "generated_r12"
New-Item -ItemType Directory -Force $Gen | Out-Null

Write-Host "== Generate H17 closure-aware membership/classifier =="
py -3 (Join-Path $H17 "tools\generate_psl27_closure_classifiers.py") --out-dir $Gen
if ($LASTEXITCODE -ne 0) { throw "H17 closure classifier generation failed" }

Write-Host "== Generate H18 restricted-12 microcode and RTL =="
py -3 (Join-Path $Lab "tools\generate_h18_r12_rtl.py") --out-dir $Gen
if ($LASTEXITCODE -ne 0) { throw "H18 restricted-12 generation failed" }

function Resolve-Tool([string]$Name, [string[]]$Candidates) {
  $cmd = Get-Command $Name -ErrorAction SilentlyContinue
  if ($cmd) {
    if ($cmd.Path) { return $cmd.Path }
    if ($cmd.Source) { return $cmd.Source }
  }
  foreach ($candidate in $Candidates) {
    if (Test-Path $candidate) {
      return (Resolve-Path $candidate).Path
    }
  }
  return $null
}

$IverilogExe = Resolve-Tool "iverilog" @(
  "C:\iverilog\bin\iverilog.exe",
  "C:\iverilog\bin\iverilog"
)
$VvpExe = Resolve-Tool "vvp" @(
  "C:\iverilog\bin\vvp.exe",
  "C:\iverilog\bin\vvp"
)

if (-not $IverilogExe) { throw "iverilog not found in PATH or C:\iverilog\bin" }
if (-not $VvpExe) { throw "vvp not found in PATH or C:\iverilog\bin" }

Write-Host ("Icarus compiler: " + $IverilogExe)
Write-Host ("Icarus runtime : " + $VvpExe)

Push-Location $Gen
try {
  Write-Host "== Icarus exhaustive 197 x 5 regression =="
  $iverilogArgs = @(
    "-g2012",
    "-s", "tb_h18_r12_microcoded",
    "-o", "h18_r12_sim",
    "psl27_membership_only.sv",
    "psl27_member_class_only.sv",
    "h18_r12_microcoded_core.sv",
    "tb_h18_r12_microcoded.sv"
  )
  & $IverilogExe @iverilogArgs
  if ($LASTEXITCODE -ne 0) { throw "iverilog compile failed" }

  & $VvpExe ".\h18_r12_sim" "+VECTORS=h18_r12_vectors.txt" | Tee-Object -FilePath "h18_r12_sim.log"
  if ($LASTEXITCODE -ne 0) { throw "restricted-12 regression failed" }

  if (Get-Command yosys -ErrorAction SilentlyContinue) {
    Write-Host "== Generic Yosys synthesis =="
    & yosys -Q -p "read_verilog -sv psl27_membership_only.sv psl27_member_class_only.sv h18_r12_microcoded_core.sv; synth -top h18_r12_microcoded_core; stat; write_json h18_r12_generic.json" |
      Tee-Object -FilePath "h18_r12_yosys.log"
    if ($LASTEXITCODE -ne 0) { throw "Yosys synthesis failed" }
  } else {
    Write-Host "Yosys not found; simulation PASS is still usable."
  }
}
finally {
  Pop-Location
}
