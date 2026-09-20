$ErrorActionPreference = "Stop"
$Tools = $PSScriptRoot

foreach ($mode in @("direct12","prefix19","nielsen12")) {
  Write-Host ""
  Write-Host "============================================================"
  Write-Host ("H19-LAB-01: {0}" -f $mode)
  Write-Host "============================================================"
  & (Join-Path $Tools "run_cyclonev_a7.ps1") -Mode $mode
  if ($LASTEXITCODE -ne 0) { throw "H19-LAB-01 failed for $mode" }
}

Write-Host ""
Write-Host "PASS: all H19-LAB-01 Cyclone V presentations completed"

Write-Host ""
Write-Host "== FINAL MATCHED SUMMARY =="
& (Join-Path $Tools "summarize_cyclonev_a7.ps1")
