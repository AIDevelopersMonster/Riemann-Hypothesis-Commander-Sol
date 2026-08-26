param(
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$Cal = Join-Path $Root "data\derived\rh-sol-02-exp01\calibration_1_10000.npz"
$Hold = Join-Path $Root "data\derived\rh-sol-02-exp01-holdout\holdout_10001_20000.npz"
$Out = Join-Path $Root "papers\RH-SOL-05-POISSON\analysis\poisson_complex_modes_1_20000.json"

foreach ($Path in @($Cal, $Hold)) {
    if (-not (Test-Path $Path)) { throw "Missing required dataset: $Path" }
}

Write-Host "=== RH-SOL-05 POISSON-02 / COMPLEX STABLE-MODE PHASE LAYER ==="
Write-Host "Modes       : (1,0) (0,1) (1,1) (1,-1)"
Write-Host "Correction  : midpoint-grid deterministic phase removed"
Write-Host "Stability   : E_complex <= 0.10 and rho_complex >= 0.995 on both ranges"
Write-Host "Temporal    : phase-invariant complex Frobenius target score"
Write-Host "Incremental : complex blockwise residualization against area"
Write-Host "Comparator  : power-only score for same frozen channels"

& $Python ".\scripts\poisson_complex_modes.py" `
    --calibration $Cal `
    --holdout $Hold `
    --out $Out `
    --block-size 1000

if ($LASTEXITCODE -ne 0) { throw "POISSON-02 failed" }

Write-Host "=== POISSON-02 COMPLETE ==="
Write-Host $Out
