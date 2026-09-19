$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$QDir = Join-Path $Lab "quartus13"
$Project = "h17_lab02_q13"
$Build = Join-Path $Lab "build_postfit"
New-Item -ItemType Directory -Force $Build | Out-Null

$QuartusBin = "C:\altera\13.1\quartus\bin64"
$QuartusSh = Join-Path $QuartusBin "quartus_sh.exe"
$QuartusEda = Join-Path $QuartusBin "quartus_eda.exe"
if (!(Test-Path $QuartusSh)) { throw "Quartus II 13.1 64-bit not found at $QuartusSh" }
if (!(Test-Path $QuartusEda)) { throw "quartus_eda not found at $QuartusEda" }

$ModelSim = "C:\altera\13.1\modelsim_ase\win32aloem"
$Vlib = Join-Path $ModelSim "vlib.exe"
$Vlog = Join-Path $ModelSim "vlog.exe"
$Vsim = Join-Path $ModelSim "vsim.exe"
if (!(Test-Path $Vsim)) { throw "ModelSim-Altera not found at $Vsim" }

Push-Location $QDir
try {
  Write-Host "== Physical fit status =="
  $Fit = Join-Path $QDir "output_files\$Project.fit.rpt"
  if (!(Test-Path $Fit)) {
    Write-Host "No fitted database found; running full Quartus compile."
    & $QuartusSh --flow compile $Project
    if ($LASTEXITCODE -ne 0) { throw "Quartus full compile failed" }
  } else {
    Write-Host "Reusing existing fitted database."
  }

  $Pin = Join-Path $QDir "output_files\$Project.pin"
  if (Test-Path $Pin) {
    Copy-Item $Pin (Join-Path $Build "$Project.auto_pins.pin") -Force
    Write-Host "Automatic package-pin assignment saved:"
    Write-Host (Join-Path $Build "$Project.auto_pins.pin")
  } else {
    Write-Host "WARNING: .pin report not found; fit report still records placement."
  }

  Write-Host "== Generate post-fit ModelSim Verilog + SDF =="
  & $QuartusEda $Project --simulation=on --tool=modelsim --format=verilog
  if ($LASTEXITCODE -ne 0) { throw "quartus_eda failed" }
} finally { Pop-Location }

$Vo = Get-ChildItem -Path $QDir -Recurse -Filter "$Project.vo" | Select-Object -First 1
if (-not $Vo) { $Vo = Get-ChildItem -Path $QDir -Recurse -Filter "*.vo" | Select-Object -First 1 }
$Sdo = Get-ChildItem -Path $QDir -Recurse -Filter "*.sdo" | Where-Object { $_.Name -like "$Project*" } | Select-Object -First 1
if (-not $Sdo) { $Sdo = Get-ChildItem -Path $QDir -Recurse -Filter "*.sdo" | Select-Object -First 1 }
if (-not $Vo) { throw "No post-fit .vo generated" }
if (-not $Sdo) { throw "No post-fit .sdo generated" }

Write-Host ("VO : " + $Vo.FullName)
Write-Host ("SDO: " + $Sdo.FullName)
Copy-Item $Vo.FullName (Join-Path $Build $Vo.Name) -Force
Copy-Item $Sdo.FullName (Join-Path $Build $Sdo.Name) -Force
Copy-Item (Join-Path $Lab "tb\tb_h17_lab02_postfit.sv") (Join-Path $Build "tb_h17_lab02_postfit.sv") -Force
Copy-Item (Join-Path $Lab "tb\h17_lab02_postfit.do") (Join-Path $Build "h17_lab02_postfit.do") -Force

Push-Location $Build
try {
  if (Test-Path ".\work") { Remove-Item -Recurse -Force ".\work" }
  & $Vlib work
  if ($LASTEXITCODE -ne 0) { throw "vlib failed" }

  & $Vlog -sv $Vo.Name "tb_h17_lab02_postfit.sv"
  if ($LASTEXITCODE -ne 0) { throw "vlog failed" }

  # Quartus .vo normally carries its own SDF annotation reference.
  # If not, annotate the generated SDO explicitly on /tb/dut.
  $VoText = Get-Content $Vo.Name -Raw
  $VsimArgs = @(
    "-c",
    "-t", "1ps",
    "-L", "cycloneive_ver",
    "-L", "altera_ver",
    "-L", "altera_mf_ver"
  )
  if (($VoText -notmatch '\$sdf_annotate') -and ($VoText -notmatch '\.sdo')) {
    $VsimArgs += "-sdfmax"
    $VsimArgs += "/tb_h17_lab02_postfit/dut=$($Sdo.Name)"
  }
  $VsimArgs += "-wlf"
  $VsimArgs += "h17_lab02_postfit.wlf"
  $VsimArgs += "work.tb_h17_lab02_postfit"
  $VsimArgs += "-do"
  $VsimArgs += "do h17_lab02_postfit.do; quit -f"

  Write-Host "== ModelSim post-fit timing simulation =="
  $sw = [System.Diagnostics.Stopwatch]::StartNew()
  & $Vsim $VsimArgs
  $rc = $LASTEXITCODE
  $sw.Stop()
  Write-Host ("POSTFIT MODELSIM ELAPSED: {0:N3} seconds" -f $sw.Elapsed.TotalSeconds)
  if ($rc -ne 0) { throw "post-fit ModelSim failed" }

  Write-Host "PASS: post-fit WLF created:"
  Write-Host (Join-Path $Build "h17_lab02_postfit.wlf")
  Write-Host "Open with:"
  Write-Host ('& "' + $Vsim + '" -view "' + (Join-Path $Build "h17_lab02_postfit.wlf") + '"')
} finally { Pop-Location }
