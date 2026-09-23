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

$ModelSimDirs = @(
  "C:\altera\13.1\modelsim_ase\win32aloem",
  "C:\altera\13.1\modelsim_ase\win32",
  "C:\intelFPGA\13.1\modelsim_ase\win32aloem",
  "C:\intelFPGA\13.1\modelsim_ase\win32"
)

$ModelSimDir = $null
foreach ($d in $ModelSimDirs) {
  $vsimCandidate = Join-Path $d "vsim.exe"
  $vlogCandidate = Join-Path $d "vlog.exe"
  $vlibCandidate = Join-Path $d "vlib.exe"
  if ((Test-Path $vsimCandidate) -and (Test-Path $vlogCandidate) -and (Test-Path $vlibCandidate)) {
    $ModelSimDir = $d
    break
  }
}

Push-Location $Gen
try {
  if ($ModelSimDir) {
    $VlibExe = Join-Path $ModelSimDir "vlib.exe"
    $VlogExe = Join-Path $ModelSimDir "vlog.exe"
    $VsimExe = Join-Path $ModelSimDir "vsim.exe"

    Write-Host "== Altera ModelSim exhaustive 197 x 5 regression =="
    Write-Host ("vlib: " + $VlibExe)
    Write-Host ("vlog: " + $VlogExe)
    Write-Host ("vsim: " + $VsimExe)

    if (Test-Path ".\work") {
      Remove-Item ".\work" -Recurse -Force
    }

    & $VlibExe work
    if ($LASTEXITCODE -ne 0) { throw "ModelSim vlib failed" }

    $vlogArgs = @(
      "-sv",
      "psl27_membership_only.sv",
      "psl27_member_class_only.sv",
      "h18_r12_microcoded_core.sv",
      "tb_h18_r12_microcoded.sv"
    )
    & $VlogExe @vlogArgs
    if ($LASTEXITCODE -ne 0) { throw "ModelSim vlog failed" }

    $vsimArgs = @(
      "-c",
      "work.tb_h18_r12_microcoded",
      "+VECTORS=h18_r12_vectors.txt",
      "-do",
      "run -all; quit -f"
    )
    & $VsimExe @vsimArgs | Tee-Object -FilePath "h18_r12_modelsim.log"
    if ($LASTEXITCODE -ne 0) { throw "ModelSim regression failed" }

    $pass = Select-String -Path "h18_r12_modelsim.log" -Pattern "PASS H18-LAB-03 restricted12: 197 states x 5 schedules = 985 runs" -Quiet
    if (-not $pass) {
      throw "ModelSim completed but the 985-run PASS marker was not found"
    }

    Write-Host "PASS: Altera ModelSim verified all 985 restricted-12 schedules"
  }
  else {
    Write-Host "Altera ModelSim ASE was not found in the Quartus 13.1 locations."
    Write-Host "Trying Icarus only as a fallback."

    $IverilogExe = Resolve-Tool "iverilog" @(
      "C:\iverilog\bin\iverilog.exe",
      "C:\iverilog\bin\iverilog",
      "C:\msys64\usr\bin\iverilog.exe",
      "C:\msys64\mingw64\bin\iverilog.exe",
      "C:\msys64\ucrt64\bin\iverilog.exe"
    )
    $VvpExe = Resolve-Tool "vvp" @(
      "C:\iverilog\bin\vvp.exe",
      "C:\iverilog\bin\vvp",
      "C:\msys64\usr\bin\vvp.exe",
      "C:\msys64\mingw64\bin\vvp.exe",
      "C:\msys64\ucrt64\bin\vvp.exe"
    )

    if (-not $IverilogExe -or -not $VvpExe) {
      throw "Neither Altera ModelSim ASE nor a usable Icarus installation was found"
    }

    Write-Host "== Icarus fallback exhaustive 197 x 5 regression =="
    Write-Host ("iverilog: " + $IverilogExe)
    Write-Host ("vvp     : " + $VvpExe)

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
    if ($LASTEXITCODE -ne 0) { throw "Icarus regression failed" }
  }

  if (Get-Command yosys -ErrorAction SilentlyContinue) {
    Write-Host "== Generic Yosys synthesis =="
    & yosys -Q -p "read_verilog -sv psl27_membership_only.sv psl27_member_class_only.sv h18_r12_microcoded_core.sv; synth -top h18_r12_microcoded_core; stat; write_json h18_r12_generic.json" | Tee-Object -FilePath "h18_r12_yosys.log"
    if ($LASTEXITCODE -ne 0) { throw "Yosys synthesis failed" }
  }
  else {
    Write-Host "Yosys not found in Windows PATH; this does not invalidate the ModelSim PASS."
    Write-Host "Generic synthesis remains covered by GitHub CI."
  }
}
finally {
  Pop-Location
}
