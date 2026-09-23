$ErrorActionPreference = "Stop"
$Tools = $PSScriptRoot

Write-Host "== H18-LAB-03 Cyclone V architecture-control run =="
Write-Host "Target: 5CEFA7F23C6"
Write-Host "Step 1/2: compile + utilization + TimeQuest summary"
& (Join-Path $Tools "run_quartus13_cyclonev_a7.ps1")
if ($LASTEXITCODE -ne 0) { throw "Cyclone V compile failed" }

Write-Host ""
Write-Host "Step 2/2: detailed worst path"
& (Join-Path $Tools "run_worst_path_cyclonev_a7.ps1")
if ($LASTEXITCODE -ne 0) { throw "Cyclone V worst-path analysis failed" }

Write-Host ""
Write-Host "PASS: H18-LAB-03 Cyclone V architecture-control reports produced"
