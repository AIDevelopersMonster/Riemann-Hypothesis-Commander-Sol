param(
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$Cal1 = Join-Path $Root "data\derived\rh-sol-02-exp01\calibration_1_10000.npz"
$Cal2 = Join-Path $Root "data\derived\rh-sol-02-exp01-holdout\holdout_10001_20000.npz"
$Hold = Join-Path $Root "data\derived\rh-sol-02-exp04-rate-oos\rate_oos_20001_40000_q16_winding.npz"
$AnalysisDir = Join-Path $Root "papers\RH-SOL-04-FIREWALL\analysis"
New-Item -ItemType Directory -Force -Path $AnalysisDir | Out-Null

foreach ($Path in @($Cal1, $Cal2, $Hold)) {
    if (-not (Test-Path $Path)) { throw "Missing required dataset: $Path" }
}

Write-Host "=== RH-SOL-04 FIREWALL-06 / ADVERSARIAL PERMUTATION ==="
Write-Host "Preserve    : exact blockwise area-value multiset"
Write-Host "Constraint  : E_spec <= 0.05"
Write-Host "Objective   : maximize normalized mean absolute displacement"
Write-Host "Search      : 20 restarts x 20000 transposition proposals per block"
Write-Host "Target score: excluded from optimization; computed only after freeze"

$Out1 = Join-Path $AnalysisDir "firewall_adversarial_permutation_calibration_1_20000.json"
& $Python ".\scripts\firewall_adversarial_permutation.py" $Cal1 $Cal2 --start 1 --stop 20000 --out $Out1 --block-size 1000 --restarts 20 --proposals 20000 --threshold 0.05 --t0 0.02 --tend 1e-5 --seed 20260904
if ($LASTEXITCODE -ne 0) { throw "FIREWALL-06 calibration failed" }

$Out2 = Join-Path $AnalysisDir "firewall_adversarial_permutation_holdout_20001_40000.json"
& $Python ".\scripts\firewall_adversarial_permutation.py" $Hold --start 20001 --stop 40000 --out $Out2 --block-size 1000 --restarts 20 --proposals 20000 --threshold 0.05 --t0 0.02 --tend 1e-5 --seed 20260905
if ($LASTEXITCODE -ne 0) { throw "FIREWALL-06 holdout failed" }

Write-Host "=== FIREWALL-06 COMPLETE ==="
Write-Host $Out1
Write-Host $Out2
