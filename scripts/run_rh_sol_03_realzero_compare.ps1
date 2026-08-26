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
$AnalysisDir = Join-Path $Root "papers\RH-SOL-03-REALZERO\analysis"

foreach ($Path in @($Cal1, $Cal2, $Hold)) {
    if (-not (Test-Path $Path)) { throw "Missing required dataset: $Path" }
}

Write-Host "=== RH-SOL-03 REALZERO / MATCHED METHOD COMPARISON ==="
Write-Host "This comparison is descriptive and cannot alter the frozen primary verdict."

$Out1 = Join-Path $AnalysisDir "realzero_compare_calibration_1_20000.json"
$Csv1 = Join-Path $AnalysisDir "realzero_compare_calibration_1_20000.csv"
& $Python ".\scripts\realzero_compare_smooth.py" $Cal1 $Cal2 --start 1 --stop 20000 --out $Out1 --csv $Csv1 --block-size 1000
if ($LASTEXITCODE -ne 0) { throw "calibration comparison failed" }

$Out2 = Join-Path $AnalysisDir "realzero_compare_holdout_20001_40000.json"
$Csv2 = Join-Path $AnalysisDir "realzero_compare_holdout_20001_40000.csv"
& $Python ".\scripts\realzero_compare_smooth.py" $Hold --start 20001 --stop 40000 --out $Out2 --csv $Csv2 --block-size 1000
if ($LASTEXITCODE -ne 0) { throw "holdout comparison failed" }

Write-Host "=== MATCHED COMPARISON COMPLETE ==="
Write-Host $Out1
Write-Host $Out2
