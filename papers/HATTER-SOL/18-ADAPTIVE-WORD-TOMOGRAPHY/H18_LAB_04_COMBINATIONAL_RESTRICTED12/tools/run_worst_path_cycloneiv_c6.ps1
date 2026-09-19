$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$QDir = Join-Path $Lab "quartus13_cycloneiv_c6"
$Sta = "C:\altera\13.1\quartus\bin64\quartus_sta.exe"
if (!(Test-Path $Sta)) { throw "quartus_sta.exe not found at $Sta" }

Push-Location $QDir
try {
  & $Sta -t .\worst_path.tcl
  if ($LASTEXITCODE -ne 0) { throw "worst-path report failed" }
}
finally { Pop-Location }

$Rpt = Join-Path $QDir "worst_path_full.rpt"
if (!(Test-Path $Rpt)) { throw "Report not generated: $Rpt" }
Write-Host "PASS: $Rpt"
Get-Content $Rpt
