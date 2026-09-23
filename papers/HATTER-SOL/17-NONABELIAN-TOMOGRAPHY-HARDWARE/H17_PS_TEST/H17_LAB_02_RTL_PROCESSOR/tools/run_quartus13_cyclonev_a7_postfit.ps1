$ErrorActionPreference = "Stop"

$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$QDir = Join-Path $Lab "quartus13_cyclonev_a7"
$Project = "h17_lab02_q13_cyclonev_a7"

$QuartusBin = "C:\altera\13.1\quartus\bin64"
$QuartusSh = Join-Path $QuartusBin "quartus_sh.exe"
$QuartusEda = Join-Path $QuartusBin "quartus_eda.exe"

if (!(Test-Path $QuartusSh)) { throw "Quartus II 13.1 not found at $QuartusSh" }
if (!(Test-Path $QuartusEda)) { throw "quartus_eda not found at $QuartusEda" }

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

  Write-Host "== Generate ModelSim post-fit functional netlist =="
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

Write-Host ""
Write-Host "== Generated simulation files =="
$Vos | ForEach-Object { Write-Host ("VO : " + $_.Name) }
$Sdos | ForEach-Object { Write-Host ("SDO: " + $_.Name) }

if ($Vos.Count -eq 0) { throw "No post-fit .vo generated" }

if ($Sdos.Count -eq 0) {
  Write-Host ""
  Write-Host "EXPECTED RESULT FOR CYCLONE V:"
  Write-Host "Quartus II 13.1 does not support gate-level timing simulation"
  Write-Host "for Cyclone V, Arria V, or Stratix V."
  Write-Host ""
  Write-Host "Therefore no .sdo is generated."
  Write-Host "The .vo can be used only for gate-level FUNCTIONAL simulation."
  Write-Host ""
  Write-Host "Use TimeQuest for physical delays:"
  Write-Host "  .\tools\run_quartus13_cyclonev_a7_worst_path.ps1"
  Write-Host ""
  Write-Host "Measured slow 1100mV 85C critical path:"
  Write-Host "  data delay   = 35.694 ns"
  Write-Host "  cell delay   = 12.726 ns"
  Write-Host "  routing      = 22.969 ns"
  Write-Host "  logic levels = 34"
  Write-Host "  Fmax         = 27.85 MHz"
  Write-Host ""
  Write-Host "No SDF-backed Cyclone V timing WLF can be produced in Quartus II 13.1."
  exit 0
}

Write-Host ""
Write-Host "Unexpected: an SDO file was generated. Inspect it before continuing."
