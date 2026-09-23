$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H17 = Resolve-Path (Join-Path $Lab "..\..")
$Generated = Join-Path $Lab "generated_q13"
$QuartusDir = Join-Path $Lab "quartus13_115k_c6"
$Project = "h17_lab02_q13_115k_c6"
New-Item -ItemType Directory -Force $Generated | Out-Null

Write-Host "== H17-LAB-02 large Cyclone IV E C6 benchmark =="
Write-Host "Target: EP4CE115F29C6 (114,480 LE, speed grade 6)"

py -3 (Join-Path $H17 "tools\generate_psl27_robust8_closure.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "closure generator failed" }
py -3 (Join-Path $H17 "tools\generate_psl27_romfree_repair.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "ROM-free generator failed" }

$QuartusExe = "C:\altera\13.1\quartus\bin64\quartus_sh.exe"
if (!(Test-Path $QuartusExe)) { throw "Quartus II 13.1 64-bit not found at $QuartusExe" }

Push-Location $QuartusDir
try {
  $sw = [System.Diagnostics.Stopwatch]::StartNew()
  & $QuartusExe --flow compile $Project
  $rc = $LASTEXITCODE
  $sw.Stop()
  Write-Host ("QUARTUS 115K C6 COMPILE ELAPSED: {0:N3} seconds" -f $sw.Elapsed.TotalSeconds)

  $ReportDir = Join-Path $QuartusDir "output_files"
  $Fit = Join-Path $ReportDir ($Project + ".fit.rpt")
  $Sta = Join-Path $ReportDir ($Project + ".sta.rpt")

  Write-Host "== 115K C6 UTILIZATION =="
  if (Test-Path $Fit) {
    Select-String -Path $Fit -Pattern "Total logic elements","Total combinational functions","Dedicated logic registers","Total registers","Total pins","Total memory bits" |
      ForEach-Object { $_.Line }
  }

  Write-Host "== 115K C6 FMAX / SLACK =="
  if (Test-Path $Sta) {
    Select-String -Path $Sta -Pattern "Fmax Summary","Restricted Fmax","Setup Summary","Hold Summary","Worst-case setup slack","Worst-case hold slack" -Context 0,8 |
      Select-Object -First 120
  }

  if ($rc -ne 0) { exit $rc }
}
finally { Pop-Location }
