param(
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$Cal = Join-Path $Root "data\derived\rh-sol-02-exp01\calibration_1_10000.npz"
$Hold = Join-Path $Root "data\derived\rh-sol-02-exp01-holdout\holdout_10001_20000.npz"
$Out = Join-Path $Root "papers\RH-SOL-05-POISSON\analysis\poisson_qstability_audit_1_20000.json"

foreach ($Path in @($Cal, $Hold)) {
    if (-not (Test-Path $Path)) { throw "Missing required dataset: $Path" }
}

Write-Host "=== RH-SOL-05 POISSON-01B / Q-STABILITY AUDIT ==="
Write-Host "Select      : q-stable vectors by R_16_32 <= 0.10 only"
Write-Host "Freeze      : calibration intersection holdout"
Write-Host "Audit       : shell completeness r2=1,2,4"
Write-Host "Temporal    : q16/q32 stable-intersection energies"
Write-Host "Incremental : blockwise residualization against area"

& $Python ".\scripts\poisson_qstability_audit.py" `
    --calibration $Cal `
    --holdout $Hold `
    --out $Out `
    --block-size 1000

if ($LASTEXITCODE -ne 0) { throw "POISSON-01B failed" }

Write-Host "=== POISSON-01B COMPLETE ==="
Write-Host $Out
