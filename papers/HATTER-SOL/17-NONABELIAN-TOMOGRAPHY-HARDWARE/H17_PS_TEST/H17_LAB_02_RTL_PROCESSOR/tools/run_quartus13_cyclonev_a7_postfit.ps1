$ErrorActionPreference = "Stop"

$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$QDir = Join-Path $Lab "quartus13_cyclonev_a7"
$Project = "h17_lab02_q13_cyclonev_a7"
$Build = Join-Path $Lab "build_postfit_cyclonev_a7"
New-Item -ItemType Directory -Force $Build | Out-Null

$QuartusBin = "C:\altera\13.1\quartus\bin64"
$QuartusSh = Join-Path $QuartusBin "quartus_sh.exe"
$QuartusEda = Join-Path $QuartusBin "quartus_eda.exe"
if (!(Test-Path $QuartusSh)) { throw "Quartus II 13.1 not found at $QuartusSh" }
if (!(Test-Path $QuartusEda)) { throw "quartus_eda not found at $QuartusEda" }

$Roots = @(
  "C:\altera\13.1\modelsim_ase\win32aloem",
  "C:\altera\13.1\modelsim_ae\win32aloem",
  "C:\altera\13.1\modelsim_ase\win32",
  "C:\altera\13.1\modelsim_ae\win32"
)
$ModelSim = $null
foreach ($r in $Roots) {
  if (Test-Path (Join-Path $r "vsim.exe")) { $ModelSim = $r; break }
}
if (-not $ModelSim) { throw "ModelSim-Altera not found under C:\altera\13.1" }

$Vlib = Join-Path $ModelSim "vlib.exe"
$Vlog = Join-Path $ModelSim "vlog.exe"
$Vsim = Join-Path $ModelSim "vsim.exe"

Push-Location $QDir
try {
  Write-Host "== Cyclone V physical fit status =="
  $Fit = Join-Path $QDir "output_files\$Project.fit.rpt"
  if (!(Test-Path $Fit)) {
    Write-Host "No fitted database found; running full Quartus compile."
    & $QuartusSh --flow compile $Project
    if ($LASTEXITCODE -ne 0) { throw "Quartus full compile failed" }
  } else {
    Write-Host "Reusing existing fitted Cyclone V database."
  }

  Write-Host "== Generate Cyclone V post-fit ModelSim Verilog + SDF =="
  & $QuartusEda $Project --simulation=on --tool=modelsim --format=verilog
  if ($LASTEXITCODE -ne 0) { throw "quartus_eda failed" }
}
finally {
  Pop-Location
}

$SimDir = Join-Path $QDir "simulation\modelsim"
if (!(Test-Path $SimDir)) { throw "Quartus ModelSim directory not found: $SimDir" }

$Vos = @(Get-ChildItem $SimDir -Filter ($Project + "*.vo") -File)
$Sdos = @(Get-ChildItem $SimDir -Filter ($Project + "*.sdo") -File)

Write-Host "== Generated timing netlists =="
$Vos | ForEach-Object { Write-Host ("VO : " + $_.Name) }
$Sdos | ForEach-Object { Write-Host ("SDO: " + $_.Name) }

if ($Vos.Count -eq 0) { throw "No post-fit .vo generated" }
if ($Sdos.Count -eq 0) { throw "No post-fit .sdo generated" }

# Prefer the exact slow 1.1 V / 85 C netlist when Quartus emits it.
$Vo = $Vos | Where-Object { $_.Name -match "1100mv_85c.*slow" } | Select-Object -First 1
if (-not $Vo) {
  $Vo = $Vos | Where-Object { $_.Name -eq ($Project + ".vo") } | Select-Object -First 1
}
if (-not $Vo) { $Vo = $Vos | Select-Object -First 1 }

$Sdo = $Sdos | Where-Object { $_.Name -match "1100mv_85c.*slow" } | Select-Object -First 1
if (-not $Sdo) {
  $Sdo = $Sdos | Where-Object { $_.Name -eq ($Project + "_v.sdo") } | Select-Object -First 1
}
if (-not $Sdo) { $Sdo = $Sdos | Select-Object -First 1 }

Write-Host "== Selected post-fit pair =="
Write-Host ("VO : " + $Vo.FullName)
Write-Host ("SDO: " + $Sdo.FullName)

# Copy all generated VO/SDO files because Quartus-generated VO can reference
# a companion SDO by file name internally.
Get-ChildItem $SimDir -File | Where-Object {
  $_.Extension -in @(".vo", ".sdo")
} | ForEach-Object {
  Copy-Item $_.FullName (Join-Path $Build $_.Name) -Force
}

Copy-Item (Join-Path $Lab "tb\tb_h17_lab02_postfit.sv") (Join-Path $Build "tb_h17_lab02_postfit.sv") -Force
Copy-Item (Join-Path $Lab "tb\h17_lab02_postfit.do") (Join-Path $Build "h17_lab02_postfit.do") -Force

Push-Location $Build
try {
  if (Test-Path ".\work") { Remove-Item -Recurse -Force ".\work" }

  & $Vlib work
  if ($LASTEXITCODE -ne 0) { throw "vlib failed" }

  & $Vlog -sv $Vo.Name "tb_h17_lab02_postfit.sv"
  if ($LASTEXITCODE -ne 0) { throw "vlog failed" }

  $VoText = Get-Content $Vo.Name -Raw

  $VsimArgs = @(
    "-c",
    "-t", "1ps",
    "-L", "cyclonev_ver",
    "-L", "altera_ver",
    "-L", "altera_mf_ver"
  )

  # If Quartus did not embed an SDF annotation in the VO, apply the selected
  # SDO explicitly to the DUT.
  if (($VoText -notmatch '\$sdf_annotate') -and ($VoText -notmatch '\.sdo')) {
    Write-Host "VO has no embedded SDF reference; adding explicit -sdfmax."
    $VsimArgs += "-sdfmax"
    $VsimArgs += "/tb_h17_lab02_postfit/dut=$($Sdo.Name)"
  } else {
    Write-Host "VO contains an embedded SDF reference; using that annotation."
  }

  $VsimArgs += "-wlf"
  $VsimArgs += "h17_lab02_cyclonev_postfit.wlf"
  $VsimArgs += "work.tb_h17_lab02_postfit"
  $VsimArgs += "-do"
  $VsimArgs += "do h17_lab02_postfit.do; quit -f"

  Write-Host "== ModelSim Cyclone V post-fit timing simulation =="
  $sw = [System.Diagnostics.Stopwatch]::StartNew()
  & $Vsim $VsimArgs
  $rc = $LASTEXITCODE
  $sw.Stop()

  Write-Host ("CYCLONE V POSTFIT MODELSIM ELAPSED: {0:N3} seconds" -f $sw.Elapsed.TotalSeconds)
  if ($rc -ne 0) { throw "Cyclone V post-fit ModelSim failed" }

  $Wlf = Join-Path $Build "h17_lab02_cyclonev_postfit.wlf"
  if (!(Test-Path $Wlf)) { throw "WLF was not created: $Wlf" }

  Write-Host ""
  Write-Host "PASS: Cyclone V post-fit WLF created:"
  Write-Host $Wlf
  Write-Host ""
  Write-Host "Open WLF:"
  Write-Host ('& "' + $Vsim + '" -view "' + $Wlf + '"')
}
finally {
  Pop-Location
}
