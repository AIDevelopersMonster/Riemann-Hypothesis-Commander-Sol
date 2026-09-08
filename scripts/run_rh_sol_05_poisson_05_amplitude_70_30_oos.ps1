param(
    [string]$Python = "python",
    [int]$B = 5000
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$OldZeroTable = Join-Path $Root "data\zeros\lmfdb_zeta_zeros_20001_40001.csv"
$NewZeroTable = Join-Path $Root "data\zeros\lmfdb_zeta_zeros_40001_60001.csv"
$Manifest = Join-Path $Root "data\zeros\lmfdb_zeta_zeros_40001_60001.manifest.json"
$ChunkDir = Join-Path $Root "data\derived\rh-sol-05-poisson-05-amplitude-70-30-oos\chunks"
$Merged = Join-Path $Root "data\derived\rh-sol-05-poisson-05-amplitude-70-30-oos\oos_40001_60000_q16_q32.npz"
$Out = Join-Path $Root "papers\RH-SOL-05-POISSON\analysis\poisson_05_amplitude_70_30_oos_40001_60000.json"

Write-Host "=== RH-SOL-05 POISSON-05 / AMPLITUDE 70-30 OOS ==="
Write-Host "Identity     : POISSON-05_AMPLITUDE_70_30_OOS"
Write-Host "Fresh zeros  : 40001..60001 from frozen LMFDB source"
Write-Host "Fresh loops  : 40001..60000"
Write-Host "Tensor       : winding-only q16/q32"
Write-Host "Primary      : empirical lower70 vs upper30"
Write-Host "Null         : common target jitter +/-0.20, B=$B"
Write-Host "Resumable    : 20 chunks of 1000 loops"
Write-Host "Output       : $Out"

if (-not (Test-Path $OldZeroTable)) {
    throw "Missing overlap zero table: $OldZeroTable"
}

if (-not (Test-Path $NewZeroTable)) {
    Write-Host "Fresh zero table absent; acquiring and auditing frozen LMFDB range."
    & $Python ".\scripts\rh_sol_05_poisson_05_acquire_lmfdb_zeros_40001_60001.py" `
        --out $NewZeroTable `
        --manifest $Manifest `
        --overlap $OldZeroTable
    if ($LASTEXITCODE -ne 0) {
        throw "POISSON-05 LMFDB zero acquisition/audit failed"
    }
}
else {
    Write-Host "Using existing audited zero table: $NewZeroTable"
    if (-not (Test-Path $Manifest)) {
        throw "Zero table exists but provenance manifest is missing: $Manifest"
    }
}

New-Item -ItemType Directory -Force -Path $ChunkDir | Out-Null

if (-not (Test-Path $Merged)) {
    Write-Host "Fresh POISSON-05 tensor not found; building resumable 1000-loop chunks."

    for ($Start = 40001; $Start -le 59001; $Start += 1000) {
        $Stop = $Start + 999
        $Chunk = Join-Path $ChunkDir ("chunk_{0}_{1}.npz" -f $Start, $Stop)
        if (Test-Path $Chunk) {
            Write-Host "SKIP existing $Chunk"
            continue
        }

        Write-Host "BUILD $Start..$Stop"
        & $Python ".\scripts\exp01_build_chunk.py" `
            --start $Start `
            --stop $Stop `
            --zero-table $NewZeroTable `
            --out $Chunk `
            --dps 30 `
            --segments 60 `
            --q 16 32 `
            --rules winding `
            --boundary-tol 1e-10

        if ($LASTEXITCODE -ne 0) {
            throw "POISSON-05 OOS chunk build failed for $Start..$Stop"
        }
    }

    $Chunks = Get-ChildItem -Path $ChunkDir -Filter "chunk_*.npz" | Sort-Object Name | ForEach-Object { $_.FullName }
    if ($Chunks.Count -ne 20) {
        throw "Expected 20 POISSON-05 chunks, found $($Chunks.Count)"
    }

    & $Python ".\scripts\exp01_merge_chunks.py" @Chunks --out $Merged
    if ($LASTEXITCODE -ne 0) {
        throw "POISSON-05 OOS chunk merge failed"
    }
}
else {
    Write-Host "Using existing fresh POISSON-05 tensor: $Merged"
}

& $Python ".\scripts\rh_sol_05_poisson_05_amplitude_70_30_oos.py" `
    --data $Merged `
    --out $Out `
    --B $B

if ($LASTEXITCODE -ne 0) {
    throw "POISSON-05_AMPLITUDE_70_30_OOS failed"
}

Write-Host "=== POISSON-05_AMPLITUDE_70_30_OOS COMPLETE ==="
Write-Host $Out
