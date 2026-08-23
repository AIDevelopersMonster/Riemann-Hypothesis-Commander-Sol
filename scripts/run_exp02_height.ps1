param(
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

$Calibration = Join-Path $RepoRoot "data\derived\rh-sol-02-exp01\calibration_1_10000.npz"
$Holdout = Join-Path $RepoRoot "data\derived\rh-sol-02-exp01-holdout\holdout_10001_20000.npz"
$OutPrefix = Join-Path $RepoRoot "papers\RH-SOL-02-SHIFT\analysis\exp02_height_blocks_1000"

if (-not (Test-Path $Calibration)) { throw "Missing calibration cube: $Calibration" }
if (-not (Test-Path $Holdout)) { throw "Missing holdout cube: $Holdout" }

Write-Host "=== EXP-02 HEIGHT ==="
Write-Host "Calibration: $Calibration"
Write-Host "Holdout    : $Holdout"
Write-Host "Blocks     : 20 x 1000"
Write-Host "Time proxy : zero-pair midpoint for all blocks"
Write-Host "Rule / q   : winding / 16"

& $Python "scripts\exp02_height_analysis.py" `
    --calibration $Calibration `
    --holdout $Holdout `
    --block-size 1000 `
    --B 20000 `
    --seed 20260822 `
    --out-prefix $OutPrefix

if ($LASTEXITCODE -ne 0) { throw "EXP-02 HEIGHT failed" }

Write-Host "=== EXP-02 HEIGHT COMPLETE ==="
Write-Host ($OutPrefix + ".csv")
Write-Host ($OutPrefix + ".json")
