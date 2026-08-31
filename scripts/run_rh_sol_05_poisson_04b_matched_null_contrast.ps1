param(
    [string]$Python = "python",
    [int]$B = 2000
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$Data = Join-Path $Root "data\derived\rh-sol-05-poisson-04-phase-singularity-oos\oos_20001_40000_q16_q32.npz"
$Out = Join-Path $Root "papers\RH-SOL-05-POISSON\analysis\poisson_04b_matched_null_contrast_20001_40000.json"

if (-not (Test-Path $Data)) {
    throw "Missing POISSON-04 OOS tensor: $Data"
}

Write-Host "=== RH-SOL-05 POISSON-04B / MATCHED-NULL CONTRAST ==="
Write-Host "Identity     : POISSON-04B_MATCHED_NULL_CONTRAST"
Write-Host "Status       : exploratory only; POISSON-04 frozen FAIL unchanged"
Write-Host "Data         : existing OOS tensor 20001..40000"
Write-Host "Null         : same jitter dictionary applied to all three strata"
Write-Host "Contrasts    : Delta_BT / Delta_BM / Delta_MT"
Write-Host "B            : $B"
Write-Host "Output       : $Out"

& $Python ".\scripts\rh_sol_05_poisson_04b_matched_null_contrast.py" `
    --data $Data `
    --out $Out `
    --B $B

if ($LASTEXITCODE -ne 0) {
    throw "POISSON-04B_MATCHED_NULL_CONTRAST failed"
}

Write-Host "=== POISSON-04B_MATCHED_NULL_CONTRAST COMPLETE ==="
Write-Host $Out
