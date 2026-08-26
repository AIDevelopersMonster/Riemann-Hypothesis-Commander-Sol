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

Write-Host "=== RH-SOL-04 FIREWALL-05 / PERMUTATION RIGIDITY MAP ==="
Write-Host "Preserve    : exact blockwise area-value multiset"
Write-Host "Vary        : controlled fraction of positions allowed to permute"
Write-Host "Measure     : order distance, spectral mismatch, exact log(m) score"
Write-Host "Replicates  : B=300 per fraction per range"
Write-Host "Fractions   : 0.01 0.02 0.05 0.10 0.20 0.40 0.60 0.80 1.00"

$Out1 = Join-Path $AnalysisDir "firewall_permutation_rigidity_calibration_1_20000.json"
& $Python ".\scripts\firewall_permutation_rigidity.py" $Cal1 $Cal2 --start 1 --stop 20000 --out $Out1 --block-size 1000 --B 300 --seed 20260902
if ($LASTEXITCODE -ne 0) { throw "FIREWALL-05 calibration failed" }

$Out2 = Join-Path $AnalysisDir "firewall_permutation_rigidity_holdout_20001_40000.json"
& $Python ".\scripts\firewall_permutation_rigidity.py" $Hold --start 20001 --stop 40000 --out $Out2 --block-size 1000 --B 300 --seed 20260903
if ($LASTEXITCODE -ne 0) { throw "FIREWALL-05 holdout failed" }

Write-Host "=== FIREWALL-05 COMPLETE ==="
Write-Host $Out1
Write-Host $Out2
