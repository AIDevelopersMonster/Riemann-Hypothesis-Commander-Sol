param(
    [ValidateSet("calibration", "holdout")]
    [string]$Stage = "calibration",
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$Cal1 = Join-Path $Root "data\derived\rh-sol-02-exp01\calibration_1_10000.npz"
$Cal2 = Join-Path $Root "data\derived\rh-sol-02-exp01-holdout\holdout_10001_20000.npz"
$Hold = Join-Path $Root "data\derived\rh-sol-02-exp04-rate-oos\rate_oos_20001_40000_q16_winding.npz"
$AnalysisDir = Join-Path $Root "papers\RH-SOL-03-REALZERO\analysis"
New-Item -ItemType Directory -Force -Path $AnalysisDir | Out-Null

if ($Stage -eq "calibration") {
    foreach ($Path in @($Cal1, $Cal2)) {
        if (-not (Test-Path $Path)) { throw "Missing required dataset: $Path" }
    }
    $Out = Join-Path $AnalysisDir "realzero_calibration_1_20000.json"
    $Csv = Join-Path $AnalysisDir "realzero_calibration_1_20000_spectrum.csv"
    Write-Host "=== RH-SOL-03 REALZERO / CALIBRATION ==="
    Write-Host "Loops      : 1..20000"
    Write-Host "Observable : winding filled area"
    Write-Host "Time       : actual zero-pair midpoint"
    Write-Host "Spectrum   : direct irregular-time Lomb-Scargle"
    Write-Host "IMPORTANT  : this stage does NOT inspect loops 20001..40000"
    & $Python ".\scripts\realzero_irregular_spectrum.py" $Cal1 $Cal2 --start 1 --stop 20000 --out $Out --spectrum-csv $Csv --block-size 1000 --B 20000 --seed 20260825
    if ($LASTEXITCODE -ne 0) { throw "REALZERO calibration failed" }
    Write-Host "=== REALZERO CALIBRATION COMPLETE ==="
    Write-Host $Out
    Write-Host $Csv
    exit 0
}

if (-not (Test-Path $Hold)) { throw "Missing required holdout dataset: $Hold" }
$Freeze = Join-Path $Root "papers\RH-SOL-03-REALZERO\CALIBRATION_FREEZE.md"
if (-not (Test-Path $Freeze)) {
    throw "Refusing holdout inspection: CALIBRATION_FREEZE.md does not exist. Review calibration first, freeze interpretation, then run -Stage holdout."
}
$Out = Join-Path $AnalysisDir "realzero_holdout_20001_40000.json"
$Csv = Join-Path $AnalysisDir "realzero_holdout_20001_40000_spectrum.csv"
Write-Host "=== RH-SOL-03 REALZERO / FROZEN HOLDOUT ==="
Write-Host "Loops      : 20001..40000"
Write-Host "Observable : winding filled area"
Write-Host "Time       : actual zero-pair midpoint"
Write-Host "Spectrum   : direct irregular-time Lomb-Scargle"
& $Python ".\scripts\realzero_irregular_spectrum.py" $Hold --start 20001 --stop 40000 --out $Out --spectrum-csv $Csv --block-size 1000 --B 20000 --seed 20260825
if ($LASTEXITCODE -ne 0) { throw "REALZERO holdout failed" }
Write-Host "=== REALZERO HOLDOUT COMPLETE ==="
Write-Host $Out
Write-Host $Csv
