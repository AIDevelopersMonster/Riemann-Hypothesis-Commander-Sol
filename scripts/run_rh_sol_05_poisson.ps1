param(
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$Cal = Join-Path $Root "data\derived\rh-sol-02-exp01\calibration_1_10000.npz"
$Hold = Join-Path $Root "data\derived\rh-sol-02-exp01-holdout\holdout_10001_20000.npz"
$OutDir = Join-Path $Root "papers\RH-SOL-05-POISSON\analysis"
$Out = Join-Path $OutDir "poisson_translation_modes_1_20000.json"
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

foreach ($Path in @($Cal, $Hold)) {
    if (-not (Test-Path $Path)) { throw "Missing required dataset: $Path" }
}

Write-Host "=== RH-SOL-05 POISSON-01 / TRANSLATION MODE DECOMPOSITION ==="
Write-Host "Data        : existing SHIFT q=8/16/32 winding tensors"
Write-Host "Spatial     : 2D DFT on translation torus"
Write-Host "Resolve     : modes max(|a|,|b|)<=3"
Write-Host "Stability   : q16 vs q32 relative power discrepancy <= 0.10"
Write-Host "Temporal    : actual zero-pair midpoint time"
Write-Host "Targets     : exact log(m), m=2..13; sensitivity m=2..11"
Write-Host "Incremental : nonzero-mode energies residualized against area"

& $Python ".\scripts\poisson_translation_modes.py" `
    --calibration $Cal `
    --holdout $Hold `
    --out $Out `
    --block-size 1000

if ($LASTEXITCODE -ne 0) { throw "RH-SOL-05 POISSON-01 failed" }

Write-Host "=== POISSON-01 COMPLETE ==="
Write-Host $Out
