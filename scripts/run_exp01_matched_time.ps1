param(
    [string]$Python = "python",
    [int]$B = 20000
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

$Cube = Join-Path $RepoRoot "data\derived\rh-sol-02-exp01\calibration_1_10000.npz"
$Phase = Join-Path $RepoRoot "data\rh-sol-01\zeta_gaussian_phase_10000.csv"
$Analysis = Join-Path $RepoRoot "papers\RH-SOL-02-SHIFT\analysis"

if (-not (Test-Path $Cube)) {
    throw "EXP-01 calibration cube not found: $Cube"
}

Write-Host "=== RH-SOL-01 LEGACY PHASE ==="
if (-not (Test-Path $Phase)) {
    & $Python "scripts\fetch_rhsol01_legacy_phase.py" --out $Phase
    if ($LASTEXITCODE -ne 0) { throw "legacy phase acquisition failed" }
} else {
    Write-Host "REUSE $Phase"
}

Write-Host "=== VALIDATE LEGACY PHASE ==="
& $Python -c "import csv,sys; p=sys.argv[1]; r=list(csv.DictReader(open(p,encoding='utf-8-sig'))); assert len(r)==10000, len(r); assert {'loop','t_near'} <= set(r[0]); assert int(r[0]['loop'])==1 and int(r[-1]['loop'])==10000; print('rows=10000; loops=1..10000; columns=loop,t_near OK')" $Phase
if ($LASTEXITCODE -ne 0) { throw "legacy phase validation failed" }

Write-Host "=== MATCHED q=16 WINDING SHIFT MAP ==="
$MapOut = Join-Path $Analysis "exp01_shift_map_winding_q16_legacy_tnear.csv"
& $Python "scripts\exp01_analyze_shift_map.py" `
    --dataset $Cube `
    --rule winding `
    --q 16 `
    --legacy-time-csv $Phase `
    --B $B `
    --out $MapOut
if ($LASTEXITCODE -ne 0) { throw "matched q16 shift map failed" }

Write-Host "=== MATCHED q=16 ZERO-MODE DECOMPOSITION ==="
$ZeroPrefix = Join-Path $Analysis "exp01_zero_mode_winding_q16_legacy_tnear"
& $Python "scripts\exp01_decompose_zero_mode.py" `
    --dataset $Cube `
    --rule winding `
    --q 16 `
    --legacy-time-csv $Phase `
    --B $B `
    --out-prefix $ZeroPrefix
if ($LASTEXITCODE -ne 0) { throw "matched zero-mode decomposition failed" }

Write-Host "=== MATCHED-TIME CALIBRATION READY ==="
Write-Host ($MapOut -replace '\.csv$','.json')
Write-Host ($ZeroPrefix + '.json')
