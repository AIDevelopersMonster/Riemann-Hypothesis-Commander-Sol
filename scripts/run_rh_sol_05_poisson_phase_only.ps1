param(
    [string]$Python = "python",
    [int]$B = 2000
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$Cal = Join-Path $Root "data\derived\rh-sol-02-exp01\calibration_1_10000.npz"
$Hold = Join-Path $Root "data\derived\rh-sol-02-exp01-holdout\holdout_10001_20000.npz"
$Out = Join-Path $Root "papers\RH-SOL-05-POISSON\analysis\poisson_phase_only_1_20000.json"

foreach ($Path in @($Cal, $Hold)) {
    if (-not (Test-Path $Path)) { throw "Missing required dataset: $Path" }
}

Write-Host "=== RH-SOL-05 POISSON-03 / PHASE-ONLY UNIT-PHASOR TEST ==="
Write-Host "Modes       : (1,0) (0,1) (1,1) (1,-1)"
Write-Host "Observable  : U = G / |G|"
Write-Host "Stability   : rms phase <= 0.10 rad and rho_phase >= 0.995"
Write-Host "Reliability : excluded fraction <= 0.001"
Write-Host "Temporal    : exact log(m), m=2..13; sensitivity m=2..11"
Write-Host "Null        : target jitter +/-0.20, B=$B"
Write-Host "Incremental : blockwise residualization against area"

& $Python ".\scripts\poisson_phase_only.py" `
    --calibration $Cal `
    --holdout $Hold `
    --out $Out `
    --B $B

if ($LASTEXITCODE -ne 0) { throw "POISSON-03 failed" }

Write-Host "=== POISSON-03 COMPLETE ==="
Write-Host $Out
