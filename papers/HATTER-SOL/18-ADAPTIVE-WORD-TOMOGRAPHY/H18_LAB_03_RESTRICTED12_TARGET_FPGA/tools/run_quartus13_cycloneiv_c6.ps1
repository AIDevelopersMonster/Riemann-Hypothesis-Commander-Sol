$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H18 = Resolve-Path (Join-Path $Lab "..")
$Hatter = Resolve-Path (Join-Path $H18 "..")
$H17 = Join-Path $Hatter "17-NONABELIAN-TOMOGRAPHY-HARDWARE"
$Gen = Join-Path $Lab "generated_r12"
$QDir = Join-Path $Lab "quartus13_cycloneiv_c6"
$Project = "h18_r12_c4c6"
New-Item -ItemType Directory -Force $Gen | Out-Null

Write-Host "== H18-LAB-03 restricted-12 Cyclone IV C6 =="
py -3 (Join-Path $H17 "tools\generate_psl27_closure_classifiers.py") --out-dir $Gen
if ($LASTEXITCODE -ne 0) { throw "closure classifier generation failed" }
py -3 (Join-Path $Lab "tools\generate_h18_r12_rtl.py") --out-dir $Gen
if ($LASTEXITCODE -ne 0) { throw "restricted-12 generation failed" }

Get-ChildItem $Gen -Filter "h18_r12_*.mem" | ForEach-Object {
  Copy-Item $_.FullName (Join-Path $QDir $_.Name) -Force
}

$QuartusExe = "C:\altera\13.1\quartus\bin64\quartus_sh.exe"
if (!(Test-Path $QuartusExe)) { throw "Quartus II 13.1 not found at $QuartusExe" }

Push-Location $QDir
try {
  $sw = [System.Diagnostics.Stopwatch]::StartNew()
  & $QuartusExe --flow compile $Project
  $rc = $LASTEXITCODE
  $sw.Stop()
  Write-Host ("H18 R12 CYCLONE IV C6 COMPILE ELAPSED: {0:N3} seconds" -f $sw.Elapsed.TotalSeconds)

  $Fit = Join-Path $QDir "output_files\$Project.fit.rpt"
  $Sta = Join-Path $QDir "output_files\$Project.sta.rpt"
  $Map = Join-Path $QDir "output_files\$Project.map.rpt"

  Write-Host "== UTILIZATION =="
  foreach ($rpt in @($Fit,$Map)) {
    if (Test-Path $rpt) {
      Select-String -Path $rpt -Pattern "Total logic elements","Total combinational functions","Dedicated logic registers","Total registers","Total memory bits","Total pins","DSP" |
        Select-Object -First 100 | ForEach-Object { $_.Line }
    }
  }

  Write-Host "== TIMEQUEST =="
  if (Test-Path $Sta) {
    Select-String -Path $Sta -Pattern "Fmax Summary","Restricted Fmax","Worst-case setup slack","Worst-case hold slack","Setup Summary","Hold Summary","MHz" -Context 0,8 |
      Select-Object -First 180
  }

  Write-Host "Reports:"
  Write-Host $Map
  Write-Host $Fit
  Write-Host $Sta
  if ($rc -ne 0) { exit $rc }
}
finally { Pop-Location }
