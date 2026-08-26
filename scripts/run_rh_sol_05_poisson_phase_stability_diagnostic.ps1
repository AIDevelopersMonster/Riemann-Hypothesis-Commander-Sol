param(
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$Cal = Join-Path $Root "data\derived\rh-sol-02-exp01\calibration_1_10000.npz"
$Hold = Join-Path $Root "data\derived\rh-sol-02-exp01-holdout\holdout_10001_20000.npz"
$Out = Join-Path $Root "papers\RH-SOL-05-POISSON\analysis\poisson_phase_stability_diagnostic_1_20000.json"

foreach ($Path in @($Cal, $Hold)) {
    if (-not (Test-Path $Path)) { throw "Missing required dataset: $Path" }
}

Write-Host "=== RH-SOL-05 POISSON-03B / PHASE-STABILITY FAILURE DIAGNOSTIC ==="
Write-Host "Verdict lock : POISSON-03 remains statistical PASS / phase-stability FAIL"
Write-Host "Mask audit   : exact overlap of near-zero excluded loops"
Write-Host "Geometry     : E12 / Enonzero / translation variance on excluded loops"
Write-Host "Strata       : target-blind amplitude quantiles"
Write-Host "Trim map     : 0, 0.5, 1, 2, 5 percent amplitude trimming"
Write-Host "Temporal     : exploratory bottom10 / middle80 / top10 phase-only scores"

& $Python ".\scripts\poisson_phase_stability_diagnostic.py" `
    --calibration $Cal `
    --holdout $Hold `
    --out $Out

if ($LASTEXITCODE -ne 0) { throw "POISSON-03B failed" }

Write-Host "=== POISSON-03B COMPLETE ==="
Write-Host $Out
