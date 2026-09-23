$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H17 = Resolve-Path (Join-Path $Lab "..\..")
$Generated = Join-Path $Lab "generated_q13"
$QuartusDir = Join-Path $Lab "quartus13_cyclonev_a7"
$Project = "h17_lab02_q13_cyclonev_a7"
New-Item -ItemType Directory -Force $Generated | Out-Null

Write-Host "== H17-LAB-02 Cyclone V E benchmark =="
Write-Host "Target: 5CEFA7F23C6 (A7, 149,500 LE, speed grade 6)"

Write-Host "== Generate closure-aware frontend =="
py -3 (Join-Path $H17 "tools\generate_psl27_robust8_closure.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "closure generator failed" }

Write-Host "== Generate ROM-free repair =="
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

  Write-Host ("QUARTUS CYCLONE V A7 COMPILE ELAPSED: {0:N3} seconds" -f $sw.Elapsed.TotalSeconds)

  $ReportDir = Join-Path $QuartusDir "output_files"
  $Fit = Join-Path $ReportDir ($Project + ".fit.rpt")
  $Sta = Join-Path $ReportDir ($Project + ".sta.rpt")
  $Map = Join-Path $ReportDir ($Project + ".map.rpt")

  Write-Host "== CYCLONE V A7 UTILIZATION =="
  foreach ($rpt in @($Fit,$Map)) {
    if (Test-Path $rpt) {
      Select-String -Path $rpt -Pattern "Total logic elements","Total ALMs","Total combinational ALUTs","Dedicated logic registers","Total registers","Total pins","Total memory bits","DSP" |
        Select-Object -First 80 |
        ForEach-Object { $_.Line }
    }
  }

  Write-Host "== CYCLONE V A7 FITTER ROUTING =="
  if (Test-Path $Fit) {
    Select-String -Path $Fit -Pattern "average interconnect usage","peak interconnect usage","Auto Fit","Optimizations were skipped" |
      ForEach-Object { $_.Line }
  }

  Write-Host "== CYCLONE V A7 FMAX / SLACK =="
  if (Test-Path $Sta) {
    Select-String -Path $Sta -Pattern "Fmax Summary","Restricted Fmax","Setup Summary","Hold Summary","Worst-case setup slack","Worst-case hold slack","MHz" -Context 0,8 |
      Select-Object -First 160
  }

  Write-Host "Reports:"
  Write-Host $Map
  Write-Host $Fit
  Write-Host $Sta

  if ($rc -ne 0) { exit $rc }
}
finally { Pop-Location }
