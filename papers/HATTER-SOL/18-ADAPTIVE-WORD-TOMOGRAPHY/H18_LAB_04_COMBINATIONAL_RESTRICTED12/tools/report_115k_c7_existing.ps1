$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$QDir = Join-Path $Lab "quartus13_115k_c7"
$Project = "h18_r12_comb_115k_c7"

$Fit = Join-Path $QDir "output_files\$Project.fit.rpt"
$Map = Join-Path $QDir "output_files\$Project.map.rpt"
$Sta = Join-Path $QDir "output_files\$Project.sta.rpt"

foreach ($p in @($Fit,$Map,$Sta)) {
  if (!(Test-Path $p)) { throw "Missing existing Quartus report: $p" }
}

Write-Host "== H18-LAB-04 EXISTING EP4CE115F29C7 REPORTS =="
Write-Host "No compilation is run by this script."
Write-Host ""

Write-Host "== DEVICE / UTILIZATION =="
$patterns = @("Family","Device","Total logic elements","Total combinational functions","Dedicated logic registers","Total registers","Total pins","Total memory bits","DSP","Average interconnect usage","Peak interconnect usage")
Select-String -Path $Fit -Pattern $patterns | Select-Object -First 160 | ForEach-Object { $_.Line }

Write-Host ""
Write-Host "== MAP ESTIMATE =="
$mapPatterns = @("Estimated Total logic elements","Total logic elements","Total combinational functions","Dedicated logic registers","Total registers")
Select-String -Path $Map -Pattern $mapPatterns | Select-Object -First 100 | ForEach-Object { $_.Line }

Write-Host ""
Write-Host "== TIMEQUEST SUMMARY =="
$staPatterns = @("Fmax Summary","Restricted Fmax","Worst-case setup slack","Worst-case hold slack","MHz")
Select-String -Path $Sta -Pattern $staPatterns -Context 0,8 | Select-Object -First 180

Write-Host ""
Write-Host "Reports:"
Write-Host $Fit
Write-Host $Map
Write-Host $Sta
