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

Write-Host "=== RH-SOL-04 FIREWALL-03 / PHASE RANDOMIZATION ==="
Write-Host "Preserve    : exact blockwise loop-index FFT magnitudes"
Write-Host "Destroy     : original Fourier phases and pointwise sequence"
Write-Host "Score       : frozen target-only exact log(m) statistic"
Write-Host "Surrogates  : B=5000 per range"

$Out1 = Join-Path $AnalysisDir "firewall_phase_calibration_1_20000.json"
& $Python ".\scripts\firewall_phase_surrogates.py" $Cal1 $Cal2 --start 1 --stop 20000 --out $Out1 --block-size 1000 --B 5000 --seed 20260827
if ($LASTEXITCODE -ne 0) { throw "FIREWALL-03 calibration phase test failed" }

$Out2 = Join-Path $AnalysisDir "firewall_phase_holdout_20001_40000.json"
& $Python ".\scripts\firewall_phase_surrogates.py" $Hold --start 20001 --stop 40000 --out $Out2 --block-size 1000 --B 5000 --seed 20260828
if ($LASTEXITCODE -ne 0) { throw "FIREWALL-03 holdout phase test failed" }

Write-Host "=== FIREWALL-03 COMPLETE ==="
Write-Host $Out1
Write-Host $Out2
