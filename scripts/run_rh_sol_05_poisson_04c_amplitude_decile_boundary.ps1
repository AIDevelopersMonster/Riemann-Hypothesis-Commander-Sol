param(
    [string]$Python = "python",
    [int]$B = 2000
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$Data = Join-Path $Root "data\derived\rh-sol-05-poisson-04-phase-singularity-oos\oos_20001_40000_q16_q32.npz"
$Out = Join-Path $Root "papers\RH-SOL-05-POISSON\analysis\poisson_04c_amplitude_decile_boundary_20001_40000.json"

if (-not (Test-Path $Data)) {
    throw "Missing POISSON-04 OOS tensor: $Data"
}

Write-Host "=== RH-SOL-05 POISSON-04C / AMPLITUDE-DECILE BOUNDARY ==="
Write-Host "Identity     : POISSON-04C_AMPLITUDE_DECILE_BOUNDARY"
Write-Host "Status       : exploratory only; POISSON-04 frozen FAIL unchanged"
Write-Host "Data         : existing OOS tensor 20001..40000"
Write-Host "Profile      : ten amplitude deciles D1..D10"
Write-Host "Boundary     : k=1..9 with max-over-splits correction"
Write-Host "Null         : common matched jitter across all ten deciles"
Write-Host "B            : $B"
Write-Host "Output       : $Out"

& $Python ".\scripts\rh_sol_05_poisson_04c_amplitude_decile_boundary.py" `
    --data $Data `
    --out $Out `
    --B $B

if ($LASTEXITCODE -ne 0) {
    throw "POISSON-04C_AMPLITUDE_DECILE_BOUNDARY failed"
}

Write-Host "=== POISSON-04C_AMPLITUDE_DECILE_BOUNDARY COMPLETE ==="
Write-Host $Out
