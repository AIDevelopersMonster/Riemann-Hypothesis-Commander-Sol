$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H17 = Resolve-Path (Join-Path $Lab "..\..")
$Generated = Join-Path $Lab "generated_q13"
$QuartusDir = Join-Path $Lab "quartus13"
$Project = "h17_lab02_q13"
New-Item -ItemType Directory -Force $Generated | Out-Null
Write-Host "== Generate closure-aware frontend =="
py -3 (Join-Path $H17 "tools\generate_psl27_robust8_closure.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "closure generator failed" }
Write-Host "== Generate ROM-free repair =="
py -3 (Join-Path $H17 "tools\generate_psl27_romfree_repair.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "ROM-free generator failed" }
$Quartus = Get-Command quartus_sh -ErrorAction SilentlyContinue
if (-not $Quartus) {
  $Candidates = @(
    "C:\altera\13.1\quartus\bin64\quartus_sh.exe",
    "C:\altera\13.1\quartus\bin\quartus_sh.exe",
    "C:\intelFPGA\13.1\quartus\bin64\quartus_sh.exe",
    "C:\intelFPGA\13.1\quartus\bin\quartus_sh.exe"
  )
  foreach ($c in $Candidates) { if (Test-Path $c) { $Quartus = Get-Item $c; break } }
}
if (-not $Quartus) { throw "quartus_sh not found" }
Write-Host ("Quartus: " + $Quartus.Source)
& $Quartus.Source --version
Push-Location $QuartusDir
try {
  $sw = [System.Diagnostics.Stopwatch]::StartNew()
  & $Quartus.Source --flow compile $Project
  $rc = $LASTEXITCODE
  $sw.Stop()
  Write-Host ("QUARTUS COMPILE ELAPSED: {0:N3} seconds" -f $sw.Elapsed.TotalSeconds)
  $Fit = Join-Path $QuartusDir ($Project + ".fit.rpt")
  $Sta = Join-Path $QuartusDir ($Project + ".sta.rpt")
  $Map = Join-Path $QuartusDir ($Project + ".map.rpt")
  Write-Host "== Utilization lines =="
  if (Test-Path $Fit) { Select-String -Path $Fit -Pattern "Total logic elements","Total combinational functions","Dedicated logic registers","Total registers" | ForEach-Object { $_.Line } }
  if (Test-Path $Map) { Select-String -Path $Map -Pattern "Total logic elements","Total combinational functions","Total registers" | ForEach-Object { $_.Line } }
  Write-Host "== TimeQuest lines =="
  if (Test-Path $Sta) { Select-String -Path $Sta -Pattern "Fmax Summary","Restricted Fmax","Worst-case Slack","Slack","clk" | Select-Object -First 80 | ForEach-Object { $_.Line } }
  Write-Host "Reports:"
  Write-Host $Map
  Write-Host $Fit
  Write-Host $Sta
  if ($rc -ne 0) { exit $rc }
} finally { Pop-Location }
