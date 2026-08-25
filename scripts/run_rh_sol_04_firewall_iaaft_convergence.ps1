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

Write-Host "=== RH-SOL-04 FIREWALL-04B / IAAFT CONVERGENCE ==="
Write-Host "Preserve    : exact blockwise area-value multiset"
Write-Host "Optimize    : spectral fidelity only, never target score"
Write-Host "Construction: 4 starts x 2000 IAAFT iterations"
Write-Host "Surrogates  : B=500 per range"
Write-Host "Gate        : median mean spectral mismatch <= 0.05"

$Out1 = Join-Path $AnalysisDir "firewall_iaaft_convergence_calibration_1_20000.json"
& $Python ".\scripts\firewall_iaaft_convergence.py" $Cal1 $Cal2 --start 1 --stop 20000 --out $Out1 --block-size 1000 --B 500 --iterations 2000 --starts 4 --seed 20260831
if ($LASTEXITCODE -ne 0) { throw "FIREWALL-04B calibration failed" }

$Out2 = Join-Path $AnalysisDir "firewall_iaaft_convergence_holdout_20001_40000.json"
& $Python ".\scripts\firewall_iaaft_convergence.py" $Hold --start 20001 --stop 40000 --out $Out2 --block-size 1000 --B 500 --iterations 2000 --starts 4 --seed 20260901
if ($LASTEXITCODE -ne 0) { throw "FIREWALL-04B holdout failed" }

Write-Host "=== FIREWALL-04B COMPLETE ==="
Write-Host $Out1
Write-Host $Out2
