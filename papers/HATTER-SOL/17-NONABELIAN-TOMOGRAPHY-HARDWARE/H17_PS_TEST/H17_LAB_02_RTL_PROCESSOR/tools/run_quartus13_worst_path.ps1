$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$QDir = Join-Path $Lab "quartus13"
$Sta = "C:\altera\13.1\quartus\bin64\quartus_sta.exe"
$Tcl = Join-Path $QDir "worst_path.tcl"
$Rpt = Join-Path $QDir "worst_path_full.rpt"

if (!(Test-Path $Sta)) { throw "quartus_sta.exe not found at $Sta" }
if (!(Test-Path $Tcl)) { throw "Timing Tcl not found at $Tcl" }

Push-Location $QDir
try {
  & $Sta -t .\worst_path.tcl
  if ($LASTEXITCODE -ne 0) { throw "TimeQuest worst-path report failed" }
} finally { Pop-Location }

if (!(Test-Path $Rpt)) { throw "Report was not generated: $Rpt" }
Write-Host "PASS: detailed worst-path report:"
Write-Host $Rpt
Get-Content $Rpt
