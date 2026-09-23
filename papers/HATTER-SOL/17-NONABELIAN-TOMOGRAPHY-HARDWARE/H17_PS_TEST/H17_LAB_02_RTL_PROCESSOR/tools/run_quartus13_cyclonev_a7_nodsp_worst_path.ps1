$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$QDir = Join-Path $Lab "quartus13_cyclonev_a7_nodsp"
$Sta = "C:\altera\13.1\quartus\bin64\quartus_sta.exe"
$Rpt = Join-Path $QDir "worst_path_full.rpt"

Push-Location $QDir
try {
  & $Sta -t .\worst_path.tcl
  if ($LASTEXITCODE -ne 0) { throw "TimeQuest Cyclone V A7 no-DSP report failed" }
}
finally { Pop-Location }

if (!(Test-Path $Rpt)) { throw "Report was not generated: $Rpt" }
Write-Host "PASS: Cyclone V A7 NO-DSP detailed worst-path report:"
Write-Host $Rpt
Get-Content $Rpt
