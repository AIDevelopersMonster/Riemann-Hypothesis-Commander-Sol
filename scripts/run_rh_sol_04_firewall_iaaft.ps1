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

Write-Host "=== RH-SOL-04 FIREWALL-04 / IAAFT ==="
Write-Host "Preserve    : exact blockwise area-value multiset"
Write-Host "Approx match: blockwise loop-index FFT magnitudes"
Write-Host "Destroy     : original phase / higher-order ordering"
Write-Host "Score       : frozen target-only exact log(m) statistic"
Write-Host "Surrogates  : B=2000 per range, 200 IAAFT iterations"

$Out1 = Join-Path $AnalysisDir "firewall_iaaft_calibration_1_20000.json"
& $Python ".\scripts\firewall_iaaft_surrogates.py" $Cal1 $Cal2 --start 1 --stop 20000 --out $Out1 --B 2000 --iterations 200 --seed 20260829
if ($LASTEXITCODE -ne 0) { throw "FIREWALL-04 calibration run failed" }

$Out2 = Join-Path $AnalysisDir "firewall_iaaft_holdout_20001_40000.json"
& $Python ".\scripts\firewall_iaaft_surrogates.py" $Hold --start 20001 --stop 40000 --out $Out2 --B 2000 --iterations 200 --seed 20260830
if ($LASTEXITCODE -ne 0) { throw "FIREWALL-04 holdout run failed" }

Write-Host "=== FIREWALL-04 COMPLETE ==="
Write-Host $Out1
Write-Host $Out2
